class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r

        while l <= r:
            k = (l + r) // 2
            total_h = 0

            for pile in piles:
                total_h += math.ceil(pile / k)
            if total_h <= h:
                res = k
                r = k - 1
            else:
                l = k + 1
        return res
