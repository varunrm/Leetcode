class Solution(object):
    def rob(self, nums):
        count_no=0
        count_run=nums[0]
        
        for i in range(1,len(nums)):
            temp=count_no
            count_no=max(count_no,count_run)
            count_run=temp+nums[i]
        return max(count_no,count_run)