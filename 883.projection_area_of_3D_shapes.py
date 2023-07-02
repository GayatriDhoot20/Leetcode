class Solution(object):
    def projectionArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        import numpy as np
        grid = np.array(grid)
        if len(grid)==1:
            max1=len(grid)
        else:
            non_zero = grid[np.where(grid!=0)]
            max1 = len(non_zero)
        raw1 = np.amax(grid, axis = 1)
        raw2 = np.amax(grid, axis = 0)
        max2 = np.sum(raw1)
        max3 = np.sum(raw2)
        return max1+max2+max3

obj1 = Solution()
print(obj1.projectionArea([[1,2],[3,4]]))
print(obj1.projectionArea([[2]]))
print(obj1.projectionArea([[1,0],[0,2]]))
