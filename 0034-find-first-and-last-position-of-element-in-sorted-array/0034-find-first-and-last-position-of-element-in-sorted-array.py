class Solution(object):
    def searchRange(self, nums, target):
        li=[]
        for i in range(len(nums)):
            if nums[i]==target:
                li.append(i)
        if (len(li))==0:
            return [-1,-1]
        s=max(li)
        n=min(li)
        return  [n,s]
        