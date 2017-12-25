import requests
import sys


''' I have assumed usernames are unique (as they indeed are on keybase). I have also assumed that the data is sane.

There are two options here:
1. Greedy approach: construct all possible 3 member teams. This will be (~47000!)/(6)*(46997!),  n~= 10^13 possible teams. 
Sort ( O(n*nlgn) ) by score calculation and pick highest scored teams, etc. Not practical since program must run in 1 min.

2. Heuristics based approach: Maximize the multiplier effect.

Let us refer to 'hasPgp', 'hasTwitter', etc as 'attributes'.
'Tag' users and organize them into groups based on the combination of attributes they have.
Some such attributes are:
'None','PGP','Twitter','PGP + Twitter', 'PGP + HN + GitHub', 'Follow each other'.

Prioritize :
First priority to form groupings between members who follow each other ( *4 multiplicative factor. Also likely that if I follow you, you follow me).
This is why I figured out 'instant matches' - those with the same attribute values and also mutually follow.

Now, maximizing number of common attributes, form groups of 3.

Future work:
Count number of followers any user has. Select, the top 1% such 'influencers'. Use 'followsChris' or 'followsMax'
as attributes.
'''

class MakeFriends(object):
    def __init__(self, inputUrl):
        if inputUrl and len(inputUrl) > 0:
            inputUrl = inputUrl[0]
            self.gotData = self.getJsonFromUrl(inputUrl)

            if self.gotData == None:
                print("Http Request failed, check if the link is up!")
                sys.exit()

            # userData - looks like, ashur :  {'tag': 25, follows: [..], mutuals:[] }
            # tagGroup - [ashur, max, chris, thegrugq, ...]
            # instantMatches - those with the same attribute tag AND follow each other.
            # looks like {'25':[ people ..]}
        
            self.userData,self.tagGroup, instantMatches = self.preprocess()

            self.friends = self.match(instantMatches)

            self.score = self.calculateScore()
            print(self.friends)
            #print('#---------- Score ----------#')
            #print(self.score)
        else:
            print("Please enter a valid/invalid url!") # have not checked for url validity

    ''' 
    Out of all attributes,contruct a tag:
    PTRHG - 00110 or 6 means, user has reddit & HN attached.
    Add list of users anyone follows. This will help in calculating the quality later.
    Find mutuals - list of usernames who the user mutually follows
    '''
    def preprocess(self):
        # First key data by username
        userData = {}
        tagGroup = [[] for i in range(32)] # 32 possible combination of tags 
        
        for user in self.gotData:
            name = user['keybase']
            userData[name] = {}
            attrs = ['pgp','twitter','reddit', 'hackernews', 'github']
            attrScore = 0
            score = 16

            #print(user)

            for attr in attrs:
                if attr in user:
                    attrScore = int(attrScore + score)
                score = score/2

            userData[name]['tag'] = attrScore
            tagGroup[attrScore].append(name)
            
            # for now put mutuals as empty
            userData[name]['mutuals'] = []
            userData[name]['follows'] = user['follows']

        # Find mutuals and instantMatches!
        instantMatches = {}
        
        for key,value in userData.items():
            # Check dict
            #print(str(key)+' :  '+str(value))
            
            for followedUser in userData[key]['follows']:         
                if key in userData[followedUser]['follows']:

                    user1tag = userData[key]['tag']
                    user2tag = userData[followedUser]['tag']

                    # instant match!
                    if user1tag == user2tag:
                        if user1tag in instantMatches:
                            instantMatches[user1tag].append(key)
                            # not adding other person since they will add themselves in another iteration
                        else:
                            instantMatches[user1tag] = [key]
                        
                    userData[key]['mutuals'].append(followedUser)

        # Check dict
        # for key,value in userData.items():
        #    print(str(key)+' :  '+str(value))

        return (userData,tagGroup,instantMatches)

    '''
    Make friend circles here
    '''
    def match(self, instantMatches):
        # store all the circles in this list
        friends = []

        numTags = len(self.tagGroup)

        # We want to separate those users who have been matched
        # from those who have not so that a user does not end up in multiple groups.
        # Sort of a 'visited' in a BFS!
        # This also turns out useful for finding those who did not get matched at all
        # because of the only 3 in a team rule.
        
        userMatched = {}

        for user,value in self.userData.items():
            userMatched[user] = False

        # First add instant matches to friend circles
        # Those who have been assigned circles will be removed from their respective
        # tag groups

        for tag,people in instantMatches.items():
            numPeople = len(people)
            numGroup = int(numPeople/3)
            circle,userMatched = self.formCircle(people, numGroup, userMatched, tag)
            friends.append(circle)

            
        # Now, group those who have the same attribute tags together.
        for tag in range(numTags): 
            numUsers = len(self.tagGroup[tag])

            # what if number in the group is not a divisible of 3
            numGroup = numUsers - numUsers%3 if numUsers > 3 else 0
            proletariat = self.tagGroup[tag]
            circle,userMatched = self.formCircle(proletariat, numGroup, userMatched, tag)
            friends.append(circle)

        # Those left over, just bunch them together in groups of 3
        count = 0
        proletariat = []
        for user,matched in userMatched.items():
            if not matched and count == 3:
                usertag1 = self.userData[proletariat[0]]['tag']
                usertag2 = self.userData[proletariat[1]]['tag']
                usertag3 = self.userData[proletariat[2]]['tag']
                # common attributes!
                common = usertag1 & usertag2 & usertag3
                
                circle,userMatched = self.formCircle(proletariat, 1, userMatched, common)
                friends.append(circle)
                proletariat = []
                count = 0
            elif not matched:
                proletariat.append(user)
                count = count + 1

        return friends
                
    def calculateQuality(self, users, attrScore):
        base = 1

        # Converting score to binary and counting all set bits
        while attrScore > 0:
            if attrScore%2 == 1:
                base = base + 1
                
            attrScore = int(attrScore/2)

        # Rule .. +1 for each person outside the group they all follow
        followingList1 = self.userData[users[0]]['follows']
        followingList2 = self.userData[users[1]]['follows']
        followingList3 = self.userData[users[2]]['follows'] 

        for user in followingList1:
            if user in followingList2 and user in followingList3 and user not in users:
                base = base + 1

        # Rule .. *2 for each person inside the group
        mutuals = [self.userData[users[0]]['mutuals'], self.userData[users[1]]['mutuals'], self.userData[users[2]]['mutuals'] ]

        for i in range(3):
            for user in users: # I know user cannot be in his/her own mutuals.
                if user in mutuals[i]:
                    base = base * 2
            
        return base

    def calculateScore(self):

        score = 0
        for circle in self.friends:
            score = score + circle['quality']

        return score
    
    # helper method
    def formCircle(self,proletariat, numGroup, userMatched, tag):        
        # This template will be re-used as we construct the friend circles
        circle= {"people":[],"quality":0}
        for i in range(0,numGroup,3):
            user1 = proletariat[i]
            user2 = proletariat[i+1]
            user3 = proletariat[i+2]

            
            circle["people"].append(user1)
            circle["people"].append(user2)
            circle["people"].append(user3)

            circle["quality"] = self.calculateQuality(circle["people"], tag)

        return (circle,userMatched)

    ''' Used the requests library to retrieve user info from Keybase'''
    def getJsonFromUrl(self, url):
        headers = {'content-type': 'application/json'}
        response = requests.get(url, headers=headers)
        if response != None:
            return response.json()
        else:
            return None

if __name__ == '__main__':
    MakeFriends(sys.argv[1:])

    
