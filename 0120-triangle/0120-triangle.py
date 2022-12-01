class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        
        l=len(triangle)
        if l==0:
            return 0
        for i in range(l-2,-1,-1):
            for j in range(i+1):
                triangle[i][j]+=min(triangle[i+1][j],triangle[i+1][j+1])
                
        return triangle[0][0]