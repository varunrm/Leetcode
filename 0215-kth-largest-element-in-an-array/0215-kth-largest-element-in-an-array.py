class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        pq = []
        for x in nums:
            if len(pq)<k:
                heapq.heappush(pq,x)
            else:
                smallest_in_heap = heappop(pq)
                if smallest_in_heap < x:
                    heappush(pq, x)
                else:
                    heappush(pq, smallest_in_heap)
        return pq[0]