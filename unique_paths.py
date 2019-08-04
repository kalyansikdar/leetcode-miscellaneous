class Solution(object):
"""
Algorithm:
The concept is that from every square, you can go right or down. But you can reach the squares in the first row in only 1 way.
Same case for the squares in the first column. Then rest of the squares need to be calculated. Ways to reach rest each squares
can be counted by adding the value for the squares just left and top of the current square.

Steps:
1. Fill squares in first row with value 1, because only one way these squares can be reached
2. Fill squares in first column with value 1, because only one way these squares can be reached
3. Fill rest of the squares with adding the value for the squares just left and top of the current square.
4. Return the value of the square in question([n-1],[m-1])

"""
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        dp = [[0]*m for i in range(n)]      # Create mxn 2d list
        
        for i in range(m):
            dp[0][i] = 1
            
        for i in range(n):
            dp[i][0] = 1
        
        for i in range(1, n):
            for j in range(1, m):
                print (i, j)
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
                
        return dp[n-1][m-1]
