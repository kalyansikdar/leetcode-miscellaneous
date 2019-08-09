class Solution(object):
    def checkPrime(self, n):
        for i in range(2, n):
            if n%i == 0:
                return False
        return True
    
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        for i in range(2, n):
            if self.checkPrime(i):
                count += 1
                
        return count
