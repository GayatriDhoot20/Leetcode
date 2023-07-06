class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        arr=[]
        for i in accounts:
            arr.append(sum(i))
        return max(arr)

obj1 = Solution()
print(obj1.maximumWealth([[1,2,3],[3,2,1]]))
print(obj1.maximumWealth([[1,5],[7,3],[3,5]]))
print(obj1.maximumWealth([[2,8,7],[7,1,3],[1,9,5]]))