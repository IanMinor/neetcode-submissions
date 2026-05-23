class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix, sufix = [1] * n, [1] * n
        output = []

        for i in range(1, n):
            prefix[i] = prefix[i - 1] * nums[i - 1]

        for j in range(n - 2, -1, -1):
            sufix[j] = sufix[j + 1] * nums[j + 1]

        for k in range(n):
            output.append(prefix[k] * sufix[k]) 
        return output