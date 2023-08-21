class Solution:
    def mergeSort(self, nums: List[int]):
        if len(nums) < 2:
           return nums
        middle = len(nums)//2
        left = nums[:middle]
        right = nums[middle:]
        
        self.mergeSort(left)
        self.mergeSort(right)
        
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                nums[k] = left[i]
                i += 1
            else:
                nums[k] = right[j]
                j += 1
            k += 1
        
        while i < len(left):
            nums[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            nums[k] = right[j]
            j += 1
            k += 1
        
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        self.mergeSort(nums)
        return [[]]
