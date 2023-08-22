class Solution:
    def mergeSort(self, nums):
        if len(nums) == 1:
            return nums
        middle = len(nums)//2
        left = nums[:middle]
        right = nums[middle:]
        
        self.mergeSort(left)
        self.mergeSort(right)
        
        i, j, k = 0, 0, 0
        
        while i < len(left) and j < len(right):
            if (left[i] < right[j]):
                nums[k] = left[i]
                i += 1
            else:
                nums[k] = right[j]
                j += 1
            k += 1
        
        while(i < len(left)):
            nums[k] = left[i]
            k += 1
            i += 1
        
        while(j < len(right)):
            nums[k] = right[j]
            k += 1
            j += 1    
            
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        self.mergeSort(nums)
        res = []
        for i, a in enumerate(nums):
            if i > 0 and a == nums[i - 1]:
                continue
            j = i + 1
            k = len(nums) - 1
            while j < k:
                sum = nums[i] + nums[j] + nums[k]
                if sum > 0:
                    k = k - 1
                elif sum < 0:
                    j = j + 1
                else:
                    res.append([nums[i], nums[j], nums[k]])
                    j = j + 1
                    while nums[j] == nums[j-1] and j < k:
                        j = j + 1
        return res
