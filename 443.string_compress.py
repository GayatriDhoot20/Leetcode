# class Solution(object):
#     def compress(self, chars):
#         """
#         :type chars: List[str]
#         :rtype: int
#         """
#         count=1
#         new_str=''
#         for i in range(0,len(chars)-1):
#             if chars[i] == chars[i+1]:
#                 count=count+1
#             else:
#                 new_str=new_str+chars[i]+str(count)
#                 count = 1
#         new_str = new_str + chars[-1] + str(count)
#         return list(new_str)
#
# obj1 = Solution()
# print(obj1.compress(["a","a","b","b","c","c","c"]))


class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        k=i=0
        while i<len(chars):
            temp=chars[i]
            count=0
            while i<len(chars) and chars[i]==temp:
                count+=1
                i+=1
            chars[k]=temp
            k+=1
            if count>1:
                count_str=str(count)
                for l in range(len(count_str)):
                    chars[k]=count_str[l]
                    k+=1
        return k

obj1 = Solution()
print(obj1.compress(["a","a","b","b","c","c","c"]))
print(obj1.compress(["a","b","b","b","b","b","b","b","b","b","b","b","b"]))