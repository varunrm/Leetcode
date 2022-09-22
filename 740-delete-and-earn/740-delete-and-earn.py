class Solution(object):
    def deleteAndEarn(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxi=max(nums)
        dp=[0]*(maxi+1)
        for i in range(len(nums)):
            idx=nums[i]
            dp[idx] += nums[i]
        skip=0
        take=dp[0]
        for i in range(0,maxi+1):
            temp=skip
            skip=max(skip,take)
            take=temp+dp[i]
        return max(skip,take)
        