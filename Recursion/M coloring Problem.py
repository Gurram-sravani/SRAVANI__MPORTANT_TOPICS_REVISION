class Solution:
    def m_coloring(self, m, n, edges, E=None):
        # Build adjacency list from edges
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        color = [-1] * n  # -1 means "uncolored"

        return self.backtrack(m, n, adj, color, 0)

    def isSafe(self, node, chosen_color, adj, color):
        # check all neighbors of 'node'
        for nei in adj[node]:
            if color[nei] == chosen_color:
                return False
        return True

    def backtrack(self, m, n, adj, color, node):
        # base case: all nodes colored
        if node == n:
            return True

        # try all colors for this node
        for c in range(m):
            if self.isSafe(node, c, adj, color):
                color[node] = c
                if self.backtrack(m, n, adj, color, node + 1):
                    return True
                color[node] = -1  # undo (backtrack)

        return False

Time Complexity: O(m^n)
Space Complexity: O(n) color list + O(n) recursion Depth 
