class Solution(object):
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j]:
                    count = count + 1

        return count

obj1 = Solution()
print(obj1.numIdenticalPairs([1,2,3,1,1,3]))
print(obj1.numIdenticalPairs([1,1,1,1]))
print(obj1.numIdenticalPairs([1,2,3]))