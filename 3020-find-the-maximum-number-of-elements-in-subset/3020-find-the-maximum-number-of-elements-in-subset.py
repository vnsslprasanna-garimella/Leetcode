from collections import Counter

class Solution:
    def maximumLength(self, nums):
        cnt = Counter(nums)
        ans = 1

        # Handle value 1 separately
        if 1 in cnt:
            if cnt[1] % 2 == 0:
                ans = max(ans, cnt[1] - 1)
            else:
                ans = max(ans, cnt[1])

        for x in list(cnt.keys()):
            if x == 1:
                continue

            cur = x
            length = 1

            while cnt.get(cur, 0) >= 2:
                nxt = cur * cur
                if nxt not in cnt:
                    break

                length += 2
                cur = nxt

            ans = max(ans, length)

        return ans
        