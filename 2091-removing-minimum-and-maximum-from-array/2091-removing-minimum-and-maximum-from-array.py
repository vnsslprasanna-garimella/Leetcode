class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        n=len(nums)
        a=nums.index(min(nums))
        b=nums.index(max(nums))
        
        if a>b:
            a,b=b,a
            
        c1=b+1
        c2=n-a
        c3=(a+1)+(n-b)
        
        return min(c1,c2,c3)
