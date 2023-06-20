class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        dictionary1 = {"a": ".-", "b": "-...", "c": "-.-.", "d": "-..", "e": ".", "f": "..-.", "g": "--.", "h": "....",
                       "i": "..", "j": ".---", "k": "-.-", "l": ".-..", "m": "--", "n": "-.", "o": "---", "p": ".--.",
                       "q": "--.-", "r": ".-.", "s": "...", "t": "-", "u": "..-", "v": "...-", "w": ".--", "x": "-..-",
                       "y": "-.--", "z": "--.."}

        all_words = set()
        for i in range(len(words)):
            make_word = ''
            for j in words[i]:
                if j in dictionary1:
                    make_word = make_word + "".join(dictionary1[j])
                else:
                    return "Not Found"
            all_words.add(make_word)
        return len(all_words)


obj1 = Solution()
print(obj1.uniqueMorseRepresentations(["gin", "zen", "gig", "msg"]))
print(obj1.uniqueMorseRepresentations(["a"]))

# Time complexity is O(n^2)
