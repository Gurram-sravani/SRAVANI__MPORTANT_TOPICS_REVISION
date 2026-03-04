class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source==target:
            return 0
        adj_list=defaultdict(list)
        for bus,stop in enumerate(routes):
            for s in stop:
                adj_list[s].append(bus)
        print(adj_list)
        if source not in adj_list:
            return -1
        queue=deque()
        visited=set()
        for bus in adj_list[source]:
            queue.append((bus,1))
        while queue:
            bus,size=queue.popleft()
            visited.add(bus)
            for nxt_stop in routes[bus]:
                if nxt_stop==target:
                    return size
                for nxt_bus in adj_list[nxt_stop]:
                    if nxt_bus not in visited:
                        visited.add(nxt_bus)
                        queue.append([nxt_bus,size+1])
        return -1

# let n be the total numbe rof buses and k be the total stops
# Time Complexity: creating adj_list O(k) + while Loop O(n) => O(n+k) 
# Space Complexity: adj_list O(k) + visited O(n)+ queue O(n) =>O(n+k)
