class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        for i in range(len(numns)):
            for j in range(i+1):
                if numns[i] == nums[j]:
                    return True
                return False