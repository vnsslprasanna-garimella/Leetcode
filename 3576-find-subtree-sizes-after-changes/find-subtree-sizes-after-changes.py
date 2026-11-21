class Solution:
    def findSubtreeSizes(self, parent: List[int], s: str) -> List[int]:
        n = len(parent)
        
        # Build original tree
        children = [[] for _ in range(n)]
        for i in range(1, n):
            children[parent[i]].append(i)
            
        new_parent = [-1] * n
        # stacks[char] stores the path of nodes with that character from root to current node
        stacks = [[] for _ in range(26)]
        
        def dfs_build(node: int):
            c = ord(s[node]) - ord('a')
            # Closest ancestor with same char is the top of its stack
            if stacks[c]:
                new_parent[node] = stacks[c][-1]
            else:
                new_parent[node] = parent[node]
                
            stacks[c].append(node)
            for child in children[node]:
                dfs_build(child)
            stacks[c].pop()
            
        dfs_build(0)
        
        # Build new tree and calculate sizes
        new_children = [[] for _ in range(n)]
        for i in range(1, n):
            new_children[new_parent[i]].append(i)
            
        ans = [0] * n
        def dfs_size(node: int) -> int:
            size = 1
            for child in new_children[node]:
                size += dfs_size(child)
            ans[node] = size
            return size
            
        dfs_size(0)
        return ans
