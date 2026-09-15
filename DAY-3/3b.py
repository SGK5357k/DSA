def max_product_subarray(nums):
        mx=nums[0]
        mn=nums[0]
        gmx=nums[0]
        for i in range(1,len(nums)):
            cmx=mx
            mx=max(nums[i],nums[i]*cmx,nums[i]*mn)
            mn=min(nums[i],nums[i]*cmx,nums[i]*mn)
            gmx=max(gmx,mx)
        return gmx
print(max_product_subarray([2,3,-2,4]))
print(max_product_subarray([-2,0,-1]))
print(max_product_subarray([-4,-3,-2]))
