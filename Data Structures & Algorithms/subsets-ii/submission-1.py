class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        n, res = len(nums), []
        nums.sort()

        def helper(i,sol):
            if i == n:
                res.append(sol[:])
                return
                
           
            sol.append(nums[i])
            helper(i+1,sol)
            sol.pop()

            while i +1 < n and nums[i] == nums[i+1]:
                i += 1
            helper(i +1, sol)
        

        helper(0, [])
        return res
