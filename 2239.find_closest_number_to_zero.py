class Solution(object):
    def findClosestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        pos=[]
        neg=[]
        for i in range(len(nums)):
            if nums[i]<0:
                neg.append(nums[i])
            else:
                pos.append(nums[i])
        if neg:
            max_val=max(neg)
        if pos:
            min_val=min(pos)
        if pos and neg:
            if abs(max_val) >= min_val:
                return min_val
            else:
                return max_val
        elif pos:
            return min_val
        else:
            return max_val

obj1 = Solution()
print(obj1.findClosestNumber([-4,-2,1,4,8]))
print(obj1.findClosestNumber([2,-1,1]))