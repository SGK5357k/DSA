def product_except_itself(nums):
    
    res=[1]*len(nums)
    for i in range(1,len(nums)):
        res[i]=res[i-1]*nums[i-1]
    ans=1
    for i in range(len(nums)-1,-1,-1):
        res[i]*=ans
        ans*=nums[i]
    return res
print(product_except_itself([1,2,3,4]))
print(product_except_itself([-1,1,0,-3,3]))
print(product_except_itself([2,3,4,5]))