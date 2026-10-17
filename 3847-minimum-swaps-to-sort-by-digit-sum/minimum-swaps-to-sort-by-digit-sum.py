class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        n=len(nums)
        s_idx=sorted(range(n),key=lambda i:(sum(map(int,str(nums[i]))),nums[i]))
        pos=[0]*n
        for idx,orig in enumerate(s_idx):
            pos[orig]=idx
        vis=[False]*n
        ans=0
        for i in range(n):
            if vis[i] or pos[i]==i:
                continue
            sz=0
            curr=i
            while not vis[curr]:
                vis[curr]=True
                curr=pos[curr]
                sz+=1
            ans+=sz-1
        return ans