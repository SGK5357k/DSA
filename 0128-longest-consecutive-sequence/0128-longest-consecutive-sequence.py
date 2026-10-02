class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s=set()
        for i in nums:
            s.add(i)
        mc =0
        for i in s:
            c=1
            if i-1 not in s:
                while i+1  in s:
                    c+=1
                    i=i+1
                mc=max(c,mc)
                    
                
        return mc