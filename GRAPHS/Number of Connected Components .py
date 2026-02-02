'''Make sure you will write or create adjacency list from u-v,v-u because it is undirected Graph , 
becaue if you a graph like 1-0 if you create adjacency list for 0 node it is empty and one dfs call for 0 + another dfs call for Node 1 which is wrong 
and the total components count will become 2 '''
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        self.visited=set()
        self.no_of_connected_Components=0
        self.adjacency_list={i:[] for i in range(n)}
        for u,v in edges:
            self.adjacency_list[u].append(v)
            self.adjacency_list[v].append(u)
        print(self.adjacency_list)
        for node in self.adjacency_list.keys():
            if node not in self.visited:
                self.no_of_connected_Components+=1
                self.dfs(node)
        return self.no_of_connected_Components
    def dfs(self,node):
        if  node in self.visited:
            return
        self.visited.add(node)
        for v in self.adjacency_list[node]:
            if v not in self.visited:
                self.dfs(v)

# Time complexity : O(n+2e)creating and adding edges in adjacency list + Dfs calls O(n) +scanning adjacency lists: O(2e) -> for v in adj[node]:  => O(n+e)
# Space Complexity : Adjacency list: Stores all nodes and edges -> Space = O(n + e) + Visited set: Stores up to n nodes ->Space = O(n) + Recursion stack (DFS) :Worst case (graph is a chain): depth = n -> Space = O(n) =>O(n+e)
