class Solution(object):
    def mergeSort(self, left, right, nums):
        # sortedlist = []
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                # sortedlist.append(left[i])
                nums[k] = left[i]
                i += 1
                k += 1
            else:
                # sortedlist.append(right[j])
                nums[k] = right[j]
                j += 1
                k += 1

        while i < len(left):
            # sortedlist.append(left[i])
            nums[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            # sortedlist.append(right[j])
            nums[k] = right[j]
            j += 1
            k += 1
        return nums

    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if len(nums) <= 1:
            return nums
        # sorted_list = []
        mid = len(nums) // 2
        right = nums[mid:]
        left = nums[:mid]
        self.sortArray(left)
        self.sortArray(right)
        return self.mergeSort(left, right, nums)

obj1 = Solution()
print(obj1.sortArray([5,2,3,1]))
print(obj1.sortArray([5,1,1,2,0,0]))