class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        arr=[]
        arr.append(0)
        for i in range(len(gain)):
            arr.append(arr[i]+gain[i])

        return max(arr)

obj=Solution()
print(obj.largestAltitude([-5,1,5,0,-7]))
print(obj.largestAltitude([-4,-3,-2,-1,4,3,2]))