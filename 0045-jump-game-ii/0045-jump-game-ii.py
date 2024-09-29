class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        if length == 1:
            return 0  
        
        total_jumps = 0
        jump_limit = 0
        max_reach = 0
        
        for idx in range(length - 1): 
            max_reach = max(max_reach, idx + nums[idx])
           
            if idx == jump_limit:
                total_jumps += 1
                jump_limit = max_reach
                
                if jump_limit >= length - 1:
                    break
        
        return total_jumps