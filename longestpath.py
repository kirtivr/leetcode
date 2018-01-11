class Node(object):
    def __init__(self, filename):
        self.fname = filename
        self.weight = len(filename)
        self.childs = []
    
    def addChild(self,child):
        self.childs.append(child)            

class Solution(object):
    def __init__(self):
        self.roots = []
        self.maxLen = 0

    def isFile(self,fname):
        dotIdx = fname.find('.')
        if dotIdx == -1:
            return False
        else:
            return len(fname) - 1 > dotIdx

    def getMaximumLength(self, rootNode, currLen):
        # DFS
        currNode = rootNode        
        currLen = currLen + len(currNode.fname)
        isFile = False
        if self.isFile(currNode.fname):
            isFile = True

        if currLen > self.maxLen and isFile:
            self.maxLen = currLen

        if len(currNode.childs) > 0:
            currLen = currLen + 1 # the extra slashh

        for child in currNode.childs:
#            print 'child '+child.fname+ 'of '+currNode.fname
            pathLen = self.getMaximumLength(child, currLen)
            
            if len(child.childs) == 0 and pathLen > self.maxLen and self.isFile(child.fname):
                self.maxLen = pathLen

        return currLen

    def lengthLongestPath(self, input):
        """
        :type input: str
        :rtype: int
        """

        currentLevel = 0
        parent = None
        lastNodeByLevel = {}
        
        while True:
            if len(input) <= 0:
                break
            
            fname = ''
            char = input[0]
            
            if char == '\n':
                input = input[1:]
                currentLevel = 0
            elif char == '\t':
                input = input[1:]
                currentLevel = currentLevel + 1
                parent = lastNodeByLevel[currentLevel - 1]
            else:
                if char == ' ' and len(input) >= 4:
                    if input[:4] == '    ' and currentLevel in lastNodeByLevel:
                        # treat like \t
                        currentLevel = currentLevel + 1
                        parent = lastNodeByLevel[currentLevel - 1]
#                        print input
                        input = input[4:]
#                        print input
                        char = input[0]

                while char != '\n' and char != '\t':
                    fname = fname + char
                    if len(input) > 1:
                        input = input[1:]
                        char = input[0]
                    else:
                        input = input[1:]
                        break

                newNode = Node(fname)

                if parent and currentLevel != 0:
                    parent.addChild(newNode)
                else:
                    parent = newNode
                    self.roots.append(newNode)

                lastNodeByLevel[currentLevel] = newNode

        for root in self.roots:
            self.getMaximumLength(root, 0)

        return self.maxLen
