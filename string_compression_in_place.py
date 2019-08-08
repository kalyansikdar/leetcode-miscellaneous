class Solution:
    def compress(self, chars: List[str]) -> int:
        """
        Explanation: Two indices have been used. i is for general counter, resultIdx is for
        maintaining where to insert the character and it's count. 
        
        In the inside while loop, next character is checked. If it's same, counter and count
        increases. If not, at the resultIdx, character is inserted and increased, then, count
        is inserted and increased.
        
        @return: resultIdx - which represents how many characters needed to represent the
        string after compression.
        
        """
        i = 0
        resultIdx = 0
        
        while i < len(chars):
            ch = chars[i]
            count = 1
            
            while (i+1) < len(chars) and chars[i+1] == ch:
                i += 1
                count += 1
            
            i += 1
            
            chars[resultIdx] = ch
            resultIdx += 1
            
            if count == 1:
                continue
            else:
                for c in str(count):
                    chars[resultIdx] = c
                    resultIdx += 1
            
        return resultIdx
