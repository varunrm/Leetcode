class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        rows=len(matrix)
        col=len(matrix[0])
        sq=[[0 for c in range(col+1)] for r in range(rows+1) ]
        ans=0
        for r in range(rows):
            for c in range(col):
                if matrix[r][c]=='0':
                    sq[r+1][c+1]=0
                else:
                    sq[r+1][c+1]=1+min((sq[r][c+1]),(sq[r][c]),(sq[r+1][c]))
                ans= max(ans,sq[r+1][c+1])
        return ans**2
                        