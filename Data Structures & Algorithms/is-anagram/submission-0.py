class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict1,dict2={},{}
        for e in s:
            dict1[e]=dict1.get(e,0)+1
        for e in t:
            dict2[e]=dict2.get(e,0)+1
        if dict1 != dict2: return False
        return True