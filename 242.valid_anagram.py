class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        test_dict1={}
        for i in range(len(s)):
            if s[i] in test_dict1:
                test_dict1[s[i]]=test_dict1[s[i]]+1
            else:
                test_dict1[s[i]]=1
        for j in range(len(t)):
            if t[j] in test_dict1:
                test_dict1[t[j]]=test_dict1[t[j]]-1
            else:
                return False
        print(test_dict1)
        flag = all(value == 0 for value in test_dict1.values())
        if flag:
            return True
        else:
            return False

obj1 = Solution()
print(obj1.isAnagram(s = "anagram", t = "nagaram"))
print(obj1.isAnagram("rat","car"))
