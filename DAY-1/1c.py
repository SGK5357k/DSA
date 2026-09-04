def bttbass(l):
    minprice=l[0]
    maxprofit=0
    for i in l:
        minprice=min(minprice,i)
        maxprofit=max(maxprofit,i-minprice)
    return maxprofit
print(bttbass([7,1,5,3,6,4]))
print(bttbass([7,6,4,3,1]))
print(bttbass([2,4,1]))