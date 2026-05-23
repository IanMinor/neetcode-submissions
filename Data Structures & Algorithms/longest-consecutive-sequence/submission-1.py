class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: return 0
        ord_nums = sorted(set(nums))
        act = 1
        longest = 1

        for i in range(1, len(ord_nums)):
            if ord_nums[i] == ord_nums[i-1] + 1:
                act += 1
            else:
                act = 1
            longest = max(longest, act)
        return longest