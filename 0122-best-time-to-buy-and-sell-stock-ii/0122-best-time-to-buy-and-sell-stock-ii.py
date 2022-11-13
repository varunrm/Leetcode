class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        ptr1=0
        ptr2=1
        profit=0
        
        if len(prices)==0:
            return 
        while ptr2<len(prices):
            diff=prices[ptr2]-prices[ptr1]
            if diff>=0:
                profit+=diff
            ptr1+=1
            ptr2+=1
        return profit
            
        