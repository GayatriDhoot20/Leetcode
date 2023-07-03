class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        temp_num=x
        rev=0
        while (temp_num > 0):
            temp = temp_num % 10
            rev = rev *10 +temp
            temp_num = temp_num//10
        if rev == x:
            return True
        else:
            return False
obj1 = Solution()
print(obj1.isPalindrome(121))
print(obj1.isPalindrome(-121))
print(obj1.isPalindrome(10))