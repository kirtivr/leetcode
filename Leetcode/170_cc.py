class TwoSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.tb = {}

    def add(self, number):
        """
        Add the number to an internal data structure..
        :type number: int
        :rtype: void
        """

        if number in self.tb:
            self.tb[number] += 1
        else:
            self.tb[number] = 1

    def find(self, value):
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        :type value: int
        :rtype: bool
        """

        for num, count in self.tb.items():
            if value - num == num and count >= 2:
                return True
            elif self.tb.get(value - num, 0) > 0:
                return True
        return False


# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)
