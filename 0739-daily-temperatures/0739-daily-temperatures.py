class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        n=len(temperatures)
        stack=[]
        output=[0]*n
        for i in range(n):
            while stack and temperatures[i]>temperatures[stack[-1]]:
                p_day=stack.pop()
                output[p_day]=i-p_day
            stack.append(i)
        return output