class Solution(object):
    def climbStairs(self, n):
        if n <= 1:
            return 1
        
        dp = [-1] * (n + 1)
        return self.climbStairsHelper(n, dp)
    
    def climbStairsHelper(self, n, dp):
        if n <= 1:
            return 1
        if dp[n] != -1:
            return dp[n]
        
        dp[n] = self.climbStairsHelper(n - 1, dp) + self.climbStairsHelper(n - 2, dp)
        return dp[n]