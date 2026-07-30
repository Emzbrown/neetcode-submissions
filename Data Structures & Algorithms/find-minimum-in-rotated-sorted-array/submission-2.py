class Solution:
    def findMin(self, nums: List[int]) -> int:
      l = 0
      r = len(nums)-1
      res = nums[l]
      while l <= r:
        m = (l+r)//2
        if nums [m] > nums[l]:
            res= min(nums[l],res)
            l = m+1
        elif nums[m] == nums [l]:
          return min(nums[l],nums[r],res)
        else: 
            res = min(nums[m], res)
            r = m-1
      return res
