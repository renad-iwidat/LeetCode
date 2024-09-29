class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        # Dictionary to store the last index of each element
        index_map = {}

        for current_index in range(len(nums)):
            current_value = nums[current_index]
            
            if current_value in index_map:
                if current_index - index_map[current_value] <= k:
                    return True
            
            # Update the last seen index of the current value
            index_map[current_value] = current_index
        
        # If no such pair, return False
        return False