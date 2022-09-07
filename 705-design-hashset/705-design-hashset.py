class MyHashSet(object):

    def __init__(self):
        self.size=1000
        self.bucket=[None]*self.size
    def hash1(self,key):
        return key%self.size 
    
    def hash2(self,key): 
        return key//self.size

    def add(self, key):
        """
        :type key: int
        :rtype: None
        """
        hi = self.hash1(key)
        dhi = self.hash2(key)
        if not self.bucket[hi] and hi==0: 
            self.bucket[hi]= [False]*(self.size+1)
        elif not self.bucket[hi]: 
            self.bucket[hi]=[False]*(self.size)
        self.bucket[hi][dhi]= True 
        

    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        hi= self.hash1(key)
        dhi = self.hash2(key)
        if self.bucket[hi]: 
            self.bucket[hi][dhi]= False 
        
        

    def contains(self, key):
        """
        :type key: int
        :rtype: bool
        """
        hi = self.hash1(key)
        dhi = self.hash2(key)
        if self.bucket[hi]:
            return self.bucket[hi][dhi]
        