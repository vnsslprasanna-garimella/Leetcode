class Solution:
    def isValid(self, s: str) -> bool:
        st=[]
        d={')':'(','}':'{',']':'['}
        for c in s:
            if c in d:
                if not st or st[-1]!=d[c]:
                    return False
                st.pop()
            else:
                st.append(c)
        return len(st)==0