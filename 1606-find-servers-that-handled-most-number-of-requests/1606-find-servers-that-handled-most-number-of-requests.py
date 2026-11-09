
from sortedcontainers import SortedList
import heapq

class Solution:
    def busiestServers(self, k: int, arrival: List[int], load: List[int]) -> List[int]:

        available = SortedList(range(k))
        busy = []
        count = [0] * k

        for i in range(len(arrival)):

            # Free servers whose requests are completed
            while busy and busy[0][0] <= arrival[i]:
                end, server = heapq.heappop(busy)
                available.add(server)

            # If no server is available, drop request
            if not available:
                continue

            # Find the next available server
            idx = available.bisect_left(i % k)

            if idx == len(available):
                idx = 0

            server = available.pop(idx)

            # Assign request
            count[server] += 1
            heapq.heappush(busy, (arrival[i] + load[i], server))

        # Find maximum requests handled
        maximum = max(count)

        return [i for i in range(k) if count[i] == maximum]
