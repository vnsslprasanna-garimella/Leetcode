class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        ans=0
        l=0
        d={}
        for r in range(len(s)):
            d[s[r]]=d.get(s[r],0)+1
            while d[s[r]]>2:
                d[s[l]]-=1
                l+=1
            if r-l+1>ans:
                ans=r-l+1
        return ans
