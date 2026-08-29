class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        n=len(nums)
        a=sorted([(nums[i],i) for i in range(0,n)])
        res=[0]*n
        v=[]
        p=[]
        for i in range(0,n):
            if not v or a[i][0]-v[-1]<=limit:
                v.append(a[i][0])
                p.append(a[i][1])
            else:
                p.sort()
                for j in range(0,len(v)):
                    res[p[j]]=v[j]
                v=[a[i][0]]
                p=[a[i][1]]
        p.sort()
        for j in range(0,len(v)):
            res[p[j]]=v[j]
        return res
