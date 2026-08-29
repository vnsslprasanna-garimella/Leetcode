class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res=[]
        def solve(i,t,path):
            if t==0:
                res.append(list(path))
                return
            for j in range(i,len(candidates)):
                if candidates[j]>t:
                    break
                path.append(candidates[j])
                solve(j,t-candidates[j],path)
                path.pop()
        solve(0,target,[])
        return res
