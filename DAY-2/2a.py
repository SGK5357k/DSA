def maxsubarray(l):
    if len(l)==0:
        return 0
    if len(l)==1:
        return l[0]
    mxsum=l[0]
    crsum=mxsum
    for i in range(1,len(l)):
        crsum=max(crsum+l[i],l[i])
        mxsum=max(mxsum,crsum)
    return mxsum
print(maxsubarray([-2,1,-3,4,-1,2,1,-5,4]))
print(maxsubarray([1]))
print(maxsubarray([5,4,-1,7,8]))