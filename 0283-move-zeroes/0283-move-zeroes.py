class Solution(object):
    def moveZeroes(self, nums):
        empty=[]
        i=0
        while i < len(nums):
            if nums[i]==0:
                empty.append(0)
                nums.pop(i)
            else:
                i+=1
        nums.extend(empty)
