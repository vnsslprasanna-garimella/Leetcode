class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        n=len(img1)
        a=[]
        b=[]
        for i in range(n):
            for j in range(n):
                if img1[i][j]==1:
                    a.append((i,j))
                if img2[i][j]==1:
                    b.append((i,j))
        d={}
        ans=0
        for r1,c1 in a:
            for r2,c2 in b:
                v=(r1-r2,c1-c2)
                d[v]=d.get(v,0)+1
                if d[v]>ans:
                    ans=d[v]
        return ans
