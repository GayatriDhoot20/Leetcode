class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        for j in range(len(t)):
            if s:
                if t[j] == s[0]:
                    s=s[1:]
        if not s:
            return True
        return False

obj1 = Solution()
print(obj1.isSubsequence(s = "abc", t = "ahbgdc"))