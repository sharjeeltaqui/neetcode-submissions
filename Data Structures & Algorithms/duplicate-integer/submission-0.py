class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        h_map={}
        for i,n in enumerate(nums):
            if n in h_map: return True
            h_map[n]=i
        return False
