class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        return [(candy+extraCandies) >= max(candies) for candy in candies]

obj1 = Solution()
print(obj1.kidsWithCandies(candies = [2,3,5,1,3], extraCandies = 3))
print(obj1.kidsWithCandies(candies = [4,2,1,1,2], extraCandies = 1))
print(obj1.kidsWithCandies(candies = [12,1,12], extraCandies = 10))