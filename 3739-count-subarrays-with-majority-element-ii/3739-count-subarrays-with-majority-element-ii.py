from typing import List
from bisect import bisect_left

class Fenwick:
    def __init__(self, n):
        self.bit = [0] * (n + 1)

    def update(self, idx, val):
        while idx <= len(self.bit) - 1:
            self.bit[idx] += val
            idx += idx & -idx

    def query(self, idx):
        s = 0
        while idx > 0:
            s += self.bit[idx]
            idx -= idx & -idx
        return s


class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        prefix = [0]
        cur = 0

        # Transform the array
        for x in nums:
            if x == target:
                cur += 1
            else:
                cur -= 1
            prefix.append(cur)

        # Coordinate compression
        values = sorted(set(prefix))

        bit = Fenwick(len(values))

        ans = 0

        for p in prefix:
            idx = bisect_left(values, p) + 1  # 1-based index
            ans += bit.query(idx - 1)         # Count smaller prefix sums
            bit.update(idx, 1)

        return ans