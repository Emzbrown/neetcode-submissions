class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = 1
        numbers.sort
        while l < len(numbers):
            if numbers[l]!= numbers[r] and numbers[l] + numbers [r] == target:
                return [l+1,r+1]
            elif r == len(numbers)-1:
                l+=1
                r=l+1

            elif numbers[l]+numbers[r] > target:
                l+=1
                r= l+1
            else:
                r +=1
            

                