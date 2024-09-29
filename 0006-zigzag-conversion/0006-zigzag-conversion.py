class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
     #If numRows is 1, return the string as no zigzag
        if numRows == 1:
            return s
        
        # Array to store the characters for each row
        zigzag_rows = [''] * min(numRows, len(s))
        current_position = 0
        moving_down = False
        
        for character in s:
            zigzag_rows[current_position] += character  
            
            # Change direction when we hit the top or bottom row
            if current_position == 0 or current_position == numRows - 1:
                moving_down = not moving_down
            
            # Move up or down based on the current direction
            current_position += 1 if moving_down else -1
        
        # Combine all rows to form the final zigzag string
        return ''.join(zigzag_rows)
        