class Solution:
    def maxArea(self, height: List[int]) -> int:
        l=0
        r=len(height)-1
        mxarea = 0
        while l < r:
            ar = (r-l) * min(height[l],height[r])
            mxarea = max(ar,mxarea)
            if height[l]<height[r]:
                l+=1
            else:
                r-=1
        return mxarea