class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        # import ipdb
        # ipdb.set_trace()
        i = 0
        n = len(nums)
        count=0
        while (i < n):
            if nums[i] == val:
                count=count+1
                if nums[i] != nums[n-1]:
                    nums[i] = nums[n - 1]
                    n = n - 1
                else:
                    n=n-1
            else:
                i = i + 1
        result=len(nums)-count
        return nums[0:result]

obj1=Solution()
print(obj1.removeElement([0,1,2,2,3,0,4,2],2))
