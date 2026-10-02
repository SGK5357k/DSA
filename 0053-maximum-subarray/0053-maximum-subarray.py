class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        csum = nums[0]
        msum = csum
        for i in range(1,len(nums)):
            csum = max(csum+nums[i],nums[i])
            msum = max(csum,msum)
        return msum