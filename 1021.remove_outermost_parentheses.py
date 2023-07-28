class Solution(object):
    def removeOuterParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack=[]
        final_result=[]
        count=0
        for i in s:
            if i == '(':
                count=count+1
                stack.append(i)
            if i == ')':
                count=count-1
                stack.append(i)
            if count==0:
                final_result=final_result+stack[1:-1]
                stack=[]
        return "".join(final_result)

obj1 = Solution()
print(obj1.removeOuterParentheses(s = "(()())(())"))
print(obj1.removeOuterParentheses(s = "(()())(())(()(()))"))
print(obj1.removeOuterParentheses(s = "()()"))