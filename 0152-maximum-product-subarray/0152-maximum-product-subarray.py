class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        mx = nums[0]
        mn = nums[0]
        gmx =mx
        for i in range(1,len(nums)):
            cmx = mx
            cmn =mn
            mx = max(mx*nums[i],cmn*nums[i],nums[i])
            mn = min(cmx*nums[i],mn*nums[i],nums[i])
            
            gmx = max(mn,mx,gmx)
        return gmx