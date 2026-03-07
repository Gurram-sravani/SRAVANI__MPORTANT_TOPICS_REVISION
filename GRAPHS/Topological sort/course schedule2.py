class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj_list=defaultdict(list)
        indegree=[0 for i in range(numCourses)]
        visited=set()
        output=[]
        for a,b in prerequisites:
            adj_list[b].append(a)
            indegree[a]+=1
        queue=deque()
        for i in range(len(indegree)):
            if indegree[i]==0:
                queue.append(i)
        while queue:
            course=queue.popleft()
            output.append(course)
            if course not in visited:
                visited.add(course)
                for nei in adj_list[course]:
                    indegree[nei]-=1
                    if indegree[nei]==0 and nei not in visited:
                        queue.append(nei)
        if len(output)==numCourses:
            return output
        else:
            return []

