class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        #m-rows
        #n-colmns
        dp=[[1 for c in range(n) ]for r in range(m)]
        for r in range(1,m):
            for c in range(1,n):
                dp[r][c]=dp[r-1][c]+dp[r][c-1]
                
        return dp[m-1][n-1]
                