class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        n_c=len(citations)
        low=0
        high=n_c
        while low<high:
            
            mid=low+(high-low)//2
            if (citations[mid]==n_c-mid):
                return n_c-mid
            elif citations[mid]>=n_c-mid:
                high=mid
            else:
                low=mid+1
        return n_c-low