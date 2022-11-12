class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if len(nums)==0 or len(nums)==k:
            return 
        k=k%len(nums)
        def reverse(array,left,right):
            while left<right:
                array[left],array[right]=array[right],array[left]
                left+=1
                right-=1
                
        reverse(nums,0,len(nums)-1)
        reverse(nums,0,k-1)
        reverse(nums,k,len(nums)-1)
        return nums