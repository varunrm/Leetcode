class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        n=len(temperatures)
        stck=[]
        output=[0]*n
        for curr_day, curr_temp in enumerate(temperatures):
            
            while stck and temperatures[stck[-1]] < curr_temp:
                prev_day = stck.pop()
                output[prev_day]=curr_day-prev_day
            stck.append(curr_day)
        return output