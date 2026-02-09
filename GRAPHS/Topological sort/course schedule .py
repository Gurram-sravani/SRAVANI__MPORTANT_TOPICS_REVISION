''' Empty queue + unprocessed nodes ⇒ cycle
Empty queue + all nodes processed ⇒ no cycle '''

from collections import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj_list={n:[] for n in range(numCourses)}
        self.count=0
        indegree=[0]*numCourses  # if you create []*n =>[], Multiplying an empty list by anything still gives an single empty list. []*5=>[]
        for u,v in prerequisites:
            adj_list[u].append(v)
            indegree[v]+=1
        print(adj_list)
        queue=deque()
        for i in range(numCourses):
            if indegree[i]==0:
                queue.append(i)
        while queue:
            self.count+=1
            node=queue.popleft()
            for nei in adj_list[node]:
                indegree[nei]-=1  
                if indegree[nei]==0:
                    queue.append(nei)
        #print(self.count)
        if self.count==numCourses:  
            return True
        
        else:
            return False

# time Complexity: O(n+E) adj_list + indegree O(E) + bfs Traversal O(n+E) => O(n+E)
# Space Complexity : O(n+E) +O(n) (adj_list+Indegree) + Queue O(n) Worst case =>O(n+E)

In Kahns algorithm, you dont need self.visited to check if there is a cycle. 

BFS STEPS:
1.Create a Adj_list
2.Create indegree
3. if indegree==0 , insert all nodes into the Queue if indegree is zero
4. make a count  of processings in queue
5. In processing, Take them out of Queue and make indegree 0 (decrement the indegree until the node becomes 0 and if it 0 add into the Queue).

After BFS finishes:
If processed == number of nodes → No cycle → return True
Else → Cycle exists → return False

* “In BFS topological sort, indegree allows us to know in O(1) time which nodes become sources after removing a node. 
Without indegree, we’d have to repeatedly scan edges to find nodes with no incoming edges, which increases the time complexity.” *****
