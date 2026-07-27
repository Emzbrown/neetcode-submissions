class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights)-1
        container= min(heights[l],heights[r])*(r-l)
        while l<r:
            container= max(min(heights[l], heights[r])*(r-l), container)
            if heights[l] < heights[r]:
                l+=1
            else:
                r-=1
        return container 