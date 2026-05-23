class Solution:
    def isPalindrome(self, s: str) -> bool:
        a = [c for c in s if c.isalnum()]
        alnum_string = "".join(a).lower()

        l, r = 0, len(alnum_string) - 1

        while l <= r:
            if alnum_string[l] == alnum_string[r]:
                l += 1
                r -= 1
            else:
                return False
        return True