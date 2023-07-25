class Solution(object):
    def maxIncreaseKeepingSkyline(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        import numpy as np
        max_value_twod_row = np.amax(grid, axis = 1)
        max_value_twod_col = np.amax(grid, axis = 0)
        total_value=0
        for i in range(len(grid)):
            for j in range(len(grid)):
                value=min(max_value_twod_col[i],max_value_twod_row[j])-grid[i][j]
                total_value+=value
        return total_value

obj1 = Solution()
print(obj1.maxIncreaseKeepingSkyline([[3,0,8,4],[2,4,5,7],[9,2,6,3],[0,3,1,0]]))
print(obj1.maxIncreaseKeepingSkyline(([[0,0,0],[0,0,0],[0,0,0]])))