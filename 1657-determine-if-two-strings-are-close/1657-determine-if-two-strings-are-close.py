from collections import Counter

class Solution(object):
    def closeStrings(self, word1, word2):
        """
        Determines if two strings are considered close by using the allowed operations.
        
        :type word1: str
        :type word2: str
        :rtype: bool
        """
        # If the lengths of the two strings are the same
        if len(word1) != len(word2):
            return False
        
        # Count character frequencies for both strings
        freq_word1 = Counter(word1)
        freq_word2 = Counter(word2)
        
        # If both words have the same set of characters
        if set(freq_word1.keys()) != set(freq_word2.keys()):
            return False
        
        # If both words have the same frequency distribution of characters
        if Counter(freq_word1.values()) != Counter(freq_word2.values()):
            return False
        
        return True
