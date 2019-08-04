class Solution(object):
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        AB, CD = {}, {}
        count = 0
        
        for a in A:
            for b in B:
                val = a + b
                if val not in AB:
                    AB[val] = 1
                else:
                    AB[val] += 1
        
        # check if -(c+d) is available in AB map, then get the frequency and increase it
        for c in C:
            for d in D:
                val = -(c + d)
                if val in AB:
                    count += AB[val]
                    
        return count
