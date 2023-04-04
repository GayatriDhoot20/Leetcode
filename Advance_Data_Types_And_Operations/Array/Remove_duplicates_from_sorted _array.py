class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        k = 1
        count=0
        for i in range(1, len(nums)):
            if nums[i - 1] != nums[i]:

                nums[k] = nums[i]
                k = k + 1
            else:
                count = count + 1
        print(count)
        result=len(nums)-count
        return nums[:result]

obj1=Solution()
print(obj1.removeDuplicates([0,0,1,1,1,2,2,3,3,4]))