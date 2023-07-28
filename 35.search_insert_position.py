class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        low=0
        high=len(nums)-1
        if target > nums[high]:
            return high+1
        if target < nums[low]:
            return low
        while (low<=high):
            mid=(low+high)//2
            if target == nums[mid] or nums[mid]>target and nums[mid-1]<target:
                return mid
            elif target < nums[mid]:
                high = mid-1
            elif target > nums[mid]:
                low = mid+1
        return -1

obj1 = Solution()
print(obj1.searchInsert(nums = [1,3,5,6], target = 5))
print(obj1.searchInsert(nums = [1,3,5,6], target = 2))
print(obj1.searchInsert(nums = [1,3,5,6], target = 7))