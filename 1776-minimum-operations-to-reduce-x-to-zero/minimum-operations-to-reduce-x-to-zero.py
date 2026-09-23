class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
        target=sum(nums)-x
        if target<0:
            return -1
        if target==0:
            return len(nums)
        n=len(nums)
        cur=0
        left=0
        max_len=-1
        for right in range(n):
            cur+=nums[right]
            while cur>target and left<=right:
                cur-=nums[left]
                left+=1
            if cur==target:
                max_len=max(max_len,right-left+1)
        return n-max_len if max_len!=-1 else -1