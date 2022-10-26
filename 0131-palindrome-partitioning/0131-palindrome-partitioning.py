class Solution:
    def partition(self, s):
        
        final = []
        
        def backtrack(path,length,i):
            if length == len(s):
                final.append(path[:])
                
            for j in range(i+1,len(s)+1):
                word = s[i:j]
				
                if word == word[::-1]:
                    path.append(word)
                    backtrack(path,length+len(word),i+len(word))
                    path.pop()
        
        backtrack([],0,0)
        return final