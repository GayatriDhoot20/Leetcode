class Solution(object):
    def numberOfSteps(self, num):
        """
        :type num: int
        :rtype: int
        """
        temp = num
        steps = 0
        while (temp > 0):
            if temp % 2 == 0:
                steps += 1
                temp = temp / 2
            else:
                temp -= 1
                steps += 1

        return steps

obj1=Solution()
print(obj1.numberOfSteps(14))
print(obj1.numberOfSteps(8))
print(obj1.numberOfSteps(0))
