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
        for j in range(len(nums)-1,0,-1):
            sum=rightsum[len(rightsum)-1]+nums[j]
            rightsum.append(sum)
        length=len(rightsum)
        for k in range(len(nums)):
            result=leftsum[k]-rightsum[length-1]
            length=length-1
            resultarr.append(abs(result))
        return resultarr

obj1 = Solution()
print(obj1.leftRigthDifference([10,4,8,3]))
print(obj1.leftRigthDifference([1]))