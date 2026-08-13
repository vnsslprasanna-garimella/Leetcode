class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        i=len(num1)-1
        j=len(num2)-1
        c=0
        res=[]
        while i>=0 or j>=0 or c:
            d1=ord(num1[i])-48 if i>=0 else 0
            d2=ord(num2[j])-48 if j>=0 else 0
            s=d1+d2+c
            c=s//10
            res.append(str(s%10))
            i-=1
            j-=1
        return "".join(res[::-1])
