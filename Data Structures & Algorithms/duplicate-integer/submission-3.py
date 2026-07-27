class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        output = False
        emzy = sorted(nums)
        store = "a"
        for i in emzy:
            if i == store:
                output = True
            store = i
        return output
            