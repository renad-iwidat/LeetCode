class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        # Split the string into words
        words = s.split()
        
        # If the number of pattern characters and words are not the same, return False
        if len(pattern) != len(words):
            return False
        
        # Create two dictionaries for bijection
        pat_to_word = {}
        word_to_pat = {}
        
        # Iterate over both pattern characters and words
        for p, w in zip(pattern, words):
            # If pattern character is already mapped but not to the current word
            if p in pat_to_word and pat_to_word[p] != w:
                return False
            # If word is already mapped but not to the current pattern character
            if w in word_to_pat and word_to_pat[w] != p:
                return False
            
            # Create the mapping
            pat_to_word[p] = w
            word_to_pat[w] = p
        
        # If no conflicts are found, return True
        return True