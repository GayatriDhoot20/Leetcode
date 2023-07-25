class Solution(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        array3=[]
        for i in range(len(nums)/2):
            array3.append(nums[i])
            array3.append(nums[i+n])
        return array3

obj1 = Solution()
print(obj1.shuffle(nums = [2,5,1,3,4,7], n = 3))
print(obj1.shuffle(nums = [1,1,2,2], n = 2))