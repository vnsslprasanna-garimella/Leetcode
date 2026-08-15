class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        ans=0
        c=0
        for i in nums:
            if c==0:
                ans=i
            if i==ans:
                c+=1
            else:
                c-=1
        return ans
