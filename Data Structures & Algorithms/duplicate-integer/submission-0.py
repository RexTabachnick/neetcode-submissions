class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # create a dict
        seen = set()
        
        for val in nums:
            seen.add(val)
        
        if len(seen) == len(nums):
            return False
        
        return True