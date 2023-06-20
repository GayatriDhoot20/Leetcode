class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        str1 = ""
        for i in digits:
            str1 = str1 + str(i)
        str1 = int(str1) + 1
        return [int(x) for x in str(str1)]

obj1 = Solution()
print(obj1.plusOne([1,2,3]))