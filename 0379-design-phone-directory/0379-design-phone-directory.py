class PhoneDirectory(object):

    def __init__(self, maxNumbers):
        """
        :type maxNumbers: int
        """
        self.dic = [i for i in range(maxNumbers)]
            
    def get(self):
        """
        :rtype: int
        """
        if len(self.dic)==0:
            return -1
        else:
            return self.dic.pop(0)

    def check(self, number):
        """
        :type number: int
        :rtype: bool
        """
        return True if number in self.dic else False
        

    def release(self, number):
        """
        :type number: int
        :rtype: None
        """
        if number not in self.dic:
            self.dic.append(number)
        


# Your PhoneDirectory object will be instantiated and called as such:
# obj = PhoneDirectory(maxNumbers)
# param_1 = obj.get()
# param_2 = obj.check(number)
# obj.release(number)