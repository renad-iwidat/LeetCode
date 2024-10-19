class Solution(object):
    def canJump(self, nums):
        """
        Determines if it is possible to reach the last index of the array from the first index.
        
        :type nums: List[int]
        :rtype: bool
        """
        # To keep track of the furthest index we can reach
        max_reachable_index = 0
        
        # Loop
        for current_index in range(len(nums)):
            # If the current index is greater than the furthest index we can reach
            if current_index > max_reachable_index:
                return False
            
            # Update the max_reachable_index based on the current position and jump length
            max_reachable_index = max(max_reachable_index, current_index + nums[current_index])
            
            # If we can reach or surpass the last index
            if max_reachable_index >= len(nums) - 1:
                return True
        
        return True
