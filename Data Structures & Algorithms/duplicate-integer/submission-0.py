class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dict={}
        for e in nums:
            dict[e] = dict.get(e,0) + 1
        for e in dict:
            if dict[e]!=1:
                return True
        return False