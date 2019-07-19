class Solution(object):
    def _helper(self, n, s, open, result):
        close = len(s) - open
        
        if len(s) == 2*n:
            result.append(s)
        if open < n:
            self._helper(n, s+"(", open+1, result)
        if close < open:
            self._helper(n, s+")", open, result)
        
        
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        open = 0
        result = []
        s = ""
        if n < 1:
            return []
        else:
            self._helper(n, s, open, result)
            return result
