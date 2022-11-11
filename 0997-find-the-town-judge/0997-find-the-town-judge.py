class Solution(object):
    def findJudge(self, n, trust):
        """
        :type n: int
        :type trust: List[List[int]]
        :rtype: int
        """
        lst=[0 for i in range(n)]
        for i in trust:
            lst[i[0]-1]-=1
            lst[i[1]-1]+=1
        
        if (n-1) in lst:
            return lst.index(n-1)+1 
        else:
            return -1 
        