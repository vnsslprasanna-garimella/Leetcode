class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        if not head or not head.next or not head.next.next:
            return [-1, -1]
        
        # To store positions of critical points
        critical_positions = []
        
        # Previous, current, and next nodes to identify critical points
        prev = head
        curr = head.next
        pos = 1  # Start with the position of the second node
        
        while curr.next:
            next_node = curr.next
            if (curr.val > prev.val and curr.val > next_node.val) or (curr.val < prev.val and curr.val < next_node.val):
                critical_positions.append(pos)
            
            prev = curr
            curr = next_node
            pos += 1
        
        # If fewer than two critical points, return [-1, -1]
        if len(critical_positions) < 2:
            return [-1, -1]
        
        # Calculate the minimum and maximum distances
        min_distance = float('inf')
        max_distance = critical_positions[-1] - critical_positions[0]
        
        for i in range(1, len(critical_positions)):
            min_distance = min(min_distance, critical_positions[i] - critical_positions[i - 1])
        
        return [min_distance, max_distance]
        