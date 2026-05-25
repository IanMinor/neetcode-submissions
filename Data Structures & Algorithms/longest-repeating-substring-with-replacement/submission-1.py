class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        longest = 0
        frequencies = {}
        n = len(s)

        for r in range(n):
            frequencies[s[r]] = frequencies.get(s[r], 0) + 1
            w_length = (r - l + 1)
            max_f = max(frequencies.values())

            while (r - l + 1) - max(frequencies.values()) > k:
                frequencies[s[l]] -= 1
                l += 1

            longest = max(longest, r - l + 1)
            
        return longest