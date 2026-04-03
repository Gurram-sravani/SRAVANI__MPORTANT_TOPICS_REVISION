In an undirected graph:

while visiting neighbors
if neighbor is not visited → continue DFS/BFS
if neighbor is visited and neighbor != parent → cycle
if neighbor is visited and neighbor == parent → ignore

def bfs(self, V,E,EDGES):
    self.adj_list={i:[] for i in range(V)}
    visited=set()
    for u ,v in edges:
        self.adj_list[u].append(v)
        self.adj_list[v].append(u)
    for n in range(V):
        if n  not in visited:
            visited.add(n)
            self.queue=deque([(n,-1)])
        while self.queue:
            node,parent=self.queue.popleft()
            for nei in self.adj_list[node]:
                if nei not in visited:
                    visited.add(nei)
                    self.queue.append((nei,node))
                elif nei!=parent:
                    return True
        return False 

I’m using a tuple because (node, parent) is a fixed pair that doesn’t need modification. Tuples are immutable and better represent structured data, whereas lists are typically used for mutable collections.
DFS: 
def graph(self,V,e,edges):
    self.adj_list={i:[] for i in range(v)}
    visited=set()
    parent=-1
    for u,v in edges:
        self.adj_list[u].append(v)
        self.adj_list[v].append(u)
    for node in range(v):
        if node not in visited:
            if self.dfs(visited,node,parent):
                return True
    return False
def dfs(self,visited,node,parent):
    if node in visited:
        return
    visited.add(node)
    for nei in self.adj_list[node]:
        if nei not in visited:
            visited.add(nei)
            self.dfs(visited,nei,node)
        elif nei!=parent:
            return True
    return False
