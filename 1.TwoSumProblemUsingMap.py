class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashmap = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashmap:
                return [i, hashmap[complement]]
            hashmap[nums[i]] = i


obj1 = Solution()
print(obj1.twoSum([2, 7, 11, 15], 9))
print(obj1.twoSum([3, 2, 4], 6))
print(obj1.twoSum([3, 3], 6))

# Time Complexity is O(n)
# Space Complexity is O(n)

