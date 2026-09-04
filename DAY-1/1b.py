def containsduplicate(l):
    s=set()
    for i in l:
        if i in s:
            return True
        s.add(i)
    return False
print(containsduplicate([1,2,3,1]))
print(containsduplicate([1,2,3,4]))
print(containsduplicate([1,1,1,3,3,4,3,2,4,2]))

