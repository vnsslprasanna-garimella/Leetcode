class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        match = {}
        # Step 1: Map matching parentheses indices
        for i, char in enumerate(s):
            if char == '(':
                stack.append(i)
            elif char == ')':
                j = stack.pop()
                match[i] = j
                match[j] = i
        
        res = []
        i = 0
        direction = 1  # 1 for right, -1 for left
        # Step 2: Traverse with direction changes
        while i < len(s):
            if s[i] == '(' or s[i] == ')':
                i = match[i]          # Jump to matching bracket
                direction *= -1       # Reverse direction
            else:
                res.append(s[i])      # Collect normal characters
            i += direction            # Move to next index based on direction
            
        return ''.join(res)