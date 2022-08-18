class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        xor,nor=0,0
        for i in nums:
            xor^=i
        for j in range(0,len(nums)+1):
            nor^=j
        return (xor^nor)