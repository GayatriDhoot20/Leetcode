class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        result = ''
        final_result = ''
        i = j = 0
        while i < len(word1) or j < len(word2):
            if i < len(word1) and j < len(word2):
                result = word1[i] + word2[j]
            elif i < len(word1):
                result = word1[i]
            elif j < len(word2):
                result = word2[j]
            i = i + 1
            j = j + 1
            final_result = final_result + result
        return final_result


obj1 = Solution()
print(obj1.mergeAlternately("abc", "pqr"))
print(obj1.mergeAlternately("ab", "pqrs"))
