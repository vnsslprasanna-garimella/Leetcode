from typing import List

class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[bool]:
        # Assign component IDs
        comp = [0] * n
        component = 0

        for i in range(1, n):
            if nums[i] - nums[i - 1] > maxDiff:
                component += 1
            comp[i] = component

        # Answer queries
        return [comp[u] == comp[v] for u, v in queries]