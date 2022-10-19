class Logger(object):

    def __init__(self):
        
        self.dic={}
       
    def shouldPrintMessage(self, timestamp, message):
        """
        :type timestamp: int
        :type message: str
        :rtype: bool
        """
        if message in self.dic:
            if (self.dic[message][-1]+10)<=timestamp:
                self.dic[message].append(timestamp)
                return True
            
            else:
                return False
        else:
            self.dic[message]=[timestamp]
            return True
        


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)