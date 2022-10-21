class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result=[]
       
        def helper(target,comb,index):
            #path=[]
            if target==0:
                result.append(list(comb))
                return
            elif target<0:
                return
            for i in range(index,len(candidates)):
                comb.append(candidates[i])
                helper(target-candidates[i],comb,i)
                comb.pop()
        helper(target,[],0)
        return result
    