class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        ans,zero = 1,0
        for i in nums:
            if i:
                ans *= i
            else: 
                zero +=1
        if zero > 1:
            return [0]*len(nums)
        elif zero == 1:
            for j in nums:
                if j:
                    res.append(0)
                else:
                    res.append(ans)
        else:
            for x in nums:
                res.append(ans//x)
        

        return res
        