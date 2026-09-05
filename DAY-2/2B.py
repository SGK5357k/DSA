def longestconseq(nums):
    s=set()
    for i in nums:
        s.add(i)
    c=1
    mx=c
    for i in s:
        if i-1 not in s:
            while i+1 in s:
                c+=1
                i+=1
            mx=max(c,mx)
            c=1
    return mx

print(longestconseq([100,4,200,1,3,2]))
print(longestconseq([0,3,7,2,5,8,4,6,0,1]))
print(longestconseq([1,0,1,2]))
        