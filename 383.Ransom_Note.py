class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazine = list(magazine)
        for i in range(len(ransomNote)):
            if ransomNote[i] in magazine:
                magazine.remove(ransomNote[i])
            else:
                return False
        return True


obj1 = Solution()
print(obj1.canConstruct(ransomNote="a", magazine="b"))
print(obj1.canConstruct(ransomNote="aa", magazine="ab"))
print(obj1.canConstruct(ransomNote="aa", magazine="aab"))
