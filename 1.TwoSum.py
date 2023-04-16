class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums) - 1):
            for j in range(1, len(nums)):
                if nums[j] == target - nums[i]:
                    return [i, j]


obj1 = Solution()
print(obj1.twoSum([2, 7, 11, 15], 9))
print(obj1.twoSum([3, 2, 4], 6))
print(obj1.twoSum([3, 3], 6))
