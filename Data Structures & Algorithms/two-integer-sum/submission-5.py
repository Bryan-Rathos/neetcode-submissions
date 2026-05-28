class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numIdxDict = {}

        for idx, val in enumerate(nums):
            diff = target - val
            if diff in numIdxDict:
                return [numIdxDict[diff], idx]
            numIdxDict[val] = idx