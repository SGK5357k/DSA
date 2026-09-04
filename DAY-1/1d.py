def anagram(s1,s2):
    if len(s1)!=len(s2):
        return False
    d1={}
    d2={}
    for i in s1:
        d1[i]=d1.get(i,0)+1
    for j in s2:
        d2[j]=d2.get(j,0)+1
    return d1==d2
print(anagram("anagram","nagaram")) 
print(anagram("rat","car")) 
print(anagram("silent","listsn")) 