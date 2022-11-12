class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l=0
        lw=0
        rw=0
        r=len(height)-1
        result=0
        while l<=r:
            if (lw<=rw):
                if (height[l]<lw):
                    result=result+(lw-height[l])
                else:
                    lw=height[l]
                l+=1
            else:
                if (height[r]<rw):
                    result=result+(rw-height[r])
                else:
                    rw=height[r]
                r-=1
        return result 
                    