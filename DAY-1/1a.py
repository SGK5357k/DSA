def twosum(l,tar):
    d={}
    for i in range(len(l)):
        res=tar-l[i]
        if res in d:
            return [d[res],i]
        d[l[i]]=i
print(twosum([2,7,11,15],9))
print(twosum([3,2,4],6))
print(twosum([3,3],6))