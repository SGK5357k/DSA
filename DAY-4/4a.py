def threesum(nums):
    nums = sorted(nums)
    res = []
    for i in range(len(nums)-2):
        if i > 0 and nums[i]==nums[i-1]:
            continue
        if nums[i]>0:
            break
        l=i+1
        r=len(nums)-1
        while l<r:
            t=nums[i]+nums[l]+nums[r]
            if t==0:
                res.append([nums[i],nums[l],nums[r]])
                l+=1
                while l<r and nums[l]==nums[l-1]:
                    l+=1
                while l<r and nums[r]==nums[r-1]:
                    r-=1
                
            elif t<0:
                l+=1
            else:
                r-=1
    return res
print(threesum([-1,0,1,2,-1,-4]))
print(threesum([0,1,1]))
print(threesum([0,0,0]))