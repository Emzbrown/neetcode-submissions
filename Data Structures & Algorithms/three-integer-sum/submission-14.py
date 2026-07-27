class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        i =0
        r = len(nums)-1
        l =1
        sum = nums[l]+ nums[i] + nums[r]
        emzy = []
        while i < len(nums)-2:
            r = len(nums)-1
            l =i+1
            while l < r:
                if nums[l]+ nums[i] + nums[r] == 0:
                    emzy.append([nums[l], nums[i], nums[r]])
                    l+=1
                    while nums[l]==nums[l-1] and l <r:
                        l+=1
                    r-=1
                    while nums[r] == nums[r+1] and l < r:
                        r-=1
                if nums[l]+ nums[i] + nums[r] < 0:
                    l +=1
                    while nums[l]==nums[l-1] and l <r:
                        l+=1
                elif nums[l]+ nums[i] + nums[r] > 0:
                    r-=1
                    while nums[r] == nums[r+1] and l < r:
                        r-=1
            i+=1
            
            while nums[i] == nums[i-1] and i < len(nums)-2:
                i+=1

        return emzy