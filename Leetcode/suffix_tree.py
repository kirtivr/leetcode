class SuffixNode:
    def __init__(self, input):
        self.matched_string = input
        self.connections = {}

    def findNextNode(self, input):
        connection_key = self.getConnectionKeyFromInput(input)
        i_sz = len(connection_key)

        for k, node in self.connections.values():
            k_sz = len(k)
            if k_sz > i_sz:
                continue

            overlap = connection_key[:k_sz]
            if k == overlap:
                return node
        return None

    def matchStrings(self, input, overlap):
        N = len(input)
        i = 0
        while i < N:
            if input[i] != overlap[i]:
                break
            i += 1
        return i

    def findLongestPartialMatch(self, input):
        i_sz = len(input)
        longest_match = ''
        for k, node in self.connections.values():
            n_sz = len(k)
            overlap = k[:min(i_sz, n_sz)]

            match_len = self.matchStrings(input, overlap)
            if match_len > len(longest_match):
                longest_match = input[:match_len]

        return longest_match

    def findMatchInNode(self, input):
        string_to_find = self.getConnectionKeyFromInput(input)
        matched_prefix = input[: len(input) - len(string_to_find)]
        partial_match = self.findLongestPartialMatch(string_to_find)
        return matched_prefix + partial_match

    def findMatchInTree(self, input):
        # Traverse the tree until we find a node that matches completely.
        prev_node = self
        while True:
            curr = prev_node.findNextNode(input)
            if curr == None:
                break
            prev_node = curr

        return prev_node.findMatchInNode(input)

    def getConnectionKeyFromInput(self, input):
        # What should the key of 'connections' be?
        string_to_add = ''
        if len(input) > len(self.matched_string):
            if input[:len(self.matched_string)] != self.matched_string:
                print('Invariant violated: Input string {} and Matched string {} do not have a common prefix', input, self.matched_string)
                return
            string_to_add = input[len(self.matched_string):]
        else:
            print('Invariant violated: Input string {} and Matched string {} do not have a common prefix', input, self.matched_string)
        return string_to_add

    def addStringToNode(self, input):
        string_to_add = self.getConnectionKeyFromInput(input)
        if string_to_add in self.connections:
            print("Invariant violated: {} is already in connections", string_to_add)
            return
        self.connections[string_to_add] = SuffixNode(input)
        return

    def addStringToSuffixTree(self, input):
        # Traverse the tree until we find a node to add to.
        prev_node = self
        while True:
            curr = prev_node.findNextNode(input)
            if curr == None:
                break
            prev_node = curr

        prev_node.addStringToNode(input)
        return