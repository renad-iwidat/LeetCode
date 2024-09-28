class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        #Making Mapping 
        roman_to_int_map = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50,
            'C': 100, 'D': 500, 'M': 1000
        }
        
        result = 0
        
        #Repeat over the string
        for index in range(len(s)):
            # If the current value is smaller than the next one, subtract it
            if index < len(s) - 1 and roman_to_int_map[s[index]] < roman_to_int_map[s[index + 1]]:
                result -= roman_to_int_map[s[index]]
            else:
                #Another case, add value.
                result += roman_to_int_map[s[index]]
        
        return result