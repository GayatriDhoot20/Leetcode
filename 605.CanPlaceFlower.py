class Solution(object):
    def canPlaceFlower(self, flowered, n):
        f = [0] + flowered + [0]
        for i in range(1,len(f)-1):
            if f[i-1]==0 and f[i]==0 and f[i+1]==0:
                f[i] = 0
                n=n-1
        return n<=0

obj1 = Solution()
print(obj1.canPlaceFlower(flowered = [1,0,0,0,1], n = 1))
print(obj1.canPlaceFlower(flowered = [1,0,0,0,1], n = 2))
