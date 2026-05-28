class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        uSet = set()

        for val in nums:
            if val in uSet:
                return True
            uSet.add(val)
        
        return False
        