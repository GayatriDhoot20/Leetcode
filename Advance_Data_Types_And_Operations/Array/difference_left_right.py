class Solution(object):
    def leftRigthDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        leftsum=[]
        rightsum=[]
        leftsum.append(0)
        rightsum.insert(0,0)
        # rightsum.insert(1,nums[len(nums)-1])
        resultarr=[]
        for i in range(len(nums)-1):
            sum=leftsum[len(leftsum)-1]+nums[i]
            leftsum.append(sum)
        for j in nums[-1:0:-1]:
            sum=rightsum[0]+j
            rightsum.insert(0,sum)
        for k in range(len(nums)):
            result=leftsum[k]-rightsum[k]
            resultarr.append(abs(result))
        return resultarr


obj1=Solution()
obj1.leftRigthDifference([10,4,8,3])


