def maxarea(nums):
    l=0
    r=len(nums)-1
    mxarea=0
    while l<r:
        ar=(r-l) * min(nums[l],nums[r])
        mxarea=max(ar,mxarea)
        if nums[l]<nums[r]:
            l+=1
        else:
            r-=1
    return mxarea
print(maxarea([1,8,6,2,5,4,8,3,7]))
print(maxarea([1,1]))
