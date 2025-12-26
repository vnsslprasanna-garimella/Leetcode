class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0 

        # max_so_far: overall maximum sum
        max_so_far = nums[0]
        
        # max_ending_here: max sum of subarray ending at current position
        max_ending_here = nums[0]

        for i in range(1, len(nums)):
            # Core decision: start new or extend previous
            max_ending_here = max(nums[i], max_ending_here + nums[i])

            # Update overall maximum
            max_so_far = max(max_so_far, max_ending_here)

        return max_so_far