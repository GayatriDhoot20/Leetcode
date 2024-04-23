class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        dict1 = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        sum = 0
        for i in range(len(s)):
            if s[i] in dict1:
                sum = sum + dict1[s[i]]
                if i>0:
                    if s[i] == "V" and s[i - 1] == "I":
                        sum = sum - 2
                    if s[i] == "X" and s[i - 1] == "I":
                        sum = sum - 2
                    if s[i] == "L" and s[i - 1] == "X":
                        sum = sum - 20
                    if s[i] == "C" and s[i - 1] == "X":
                        sum = sum - 20
                    if s[i] == "D" and s[i - 1] == "C":
                        sum = sum - 200
                    if s[i] == "M" and s[i - 1] == "C":
                        sum = sum - 200

        return sum


obj1 = Solution()
print(obj1.romanToInt("MMMCDXC"))
print(obj1.romanToInt("III"))
print(obj1.romanToInt("LVIII"))
print(obj1.romanToInt("MCMXCIV"))
