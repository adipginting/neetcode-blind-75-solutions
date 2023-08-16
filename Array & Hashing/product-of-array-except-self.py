class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
      num: int = 1
      answer: List[int] = [1] * len(nums)
      for i in range (len(nums)):
        if (i == 0):
          num = num * 1
        else:
          num = num * nums[i - 1]
        answer[i] = num
      
      num = 1
      for i in range (len(nums) - 1, -1, -1):
        if (i == len(nums) - 1):
          num = num * 1
        else:
          num = num * nums[i + 1]
        answer[i] = answer[i] * num
      return answer
