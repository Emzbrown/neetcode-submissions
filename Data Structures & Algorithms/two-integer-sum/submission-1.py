class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        i = 0
        while i < len(nums):
                complement= target - nums[i]
                if complement in seen:
                        return [seen[complement], i]
                seen[nums[i]] = i
                i+=1