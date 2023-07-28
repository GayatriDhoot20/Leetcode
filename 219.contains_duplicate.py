class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        data1={}
        for i in range(len(nums)):
            if nums[i] in data1 and abs(i-data1[nums[i]])<=k:
                return True
            else:
                data1[nums[i]]=i
        return False

obj1 = Solution()
print(obj1.containsNearbyDuplicate(nums = [1,2,3,1], k = 3))
print(obj1.containsNearbyDuplicate(nums = [1,0,1,1], k = 1))
print(obj1.containsNearbyDuplicate(nums = [1,2,3,1,2,3], k = 2))