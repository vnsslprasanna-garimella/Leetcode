class Solution:
    def minimumCost(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:
        shared_need = min(need1, need2)
        rem1 = need1 - shared_need
        rem2 = need2 - shared_need
        
        return (
            shared_need * min(costBoth, cost1 + cost2) 
            + rem1 * min(cost1, costBoth) 
            + rem2 * min(cost2, costBoth)
        )
