class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums = sorted(nums)
        res = []
        for i in range(len(nums)):
            if i>0 and nums[i]==nums[i-1]:
                continue
            if nums[i]>0:
                return res
            l=i+1
            r=len(nums)-1
            while l<r:
                t = nums[i] + nums[r] + nums[l]
                if t==0:
                    res.append([nums[l],nums[i],nums[r]])
                    l+=1
                    r-=1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1

                    while l < r and nums[r] == nums[r+1]:
                        r -= 1
                    
                elif t<0:
                    l+=1
                else:
                    r-=1
        return res
        
                    