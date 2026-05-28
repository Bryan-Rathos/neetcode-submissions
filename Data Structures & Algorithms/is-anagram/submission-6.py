from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False

        dict1 = defaultdict(int)
        dict2 = defaultdict(int)

        for valS, valT in zip(s,t):
            dict1[valS] += 1
            dict2[valT] += 1

        isEqual = dict1 == dict2

        return isEqual