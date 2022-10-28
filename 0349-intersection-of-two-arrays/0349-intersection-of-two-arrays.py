class Solution(object):
    def intersection(self, nums1, nums2):
        if len(nums1)==0 or len(nums2)==0:
            return []
        n1=len(nums1)
        n2=len(nums2)
        
        if(n2<n1):
            nums2,nums1=nums1,nums2
        nums1.sort()
        nums2.sort()
        result=[]
        for i in range(len(nums1)):
            tmp = nums1[i]
            l,r=0,len(nums2)-1
            while l<=r:
                mid = (l+r)//2
                if nums2[mid]==tmp:
                    result.append(tmp)
                if nums2[mid] < tmp:
                    l = mid+1
                else:
                    r = mid-1
        return list(set(result))
