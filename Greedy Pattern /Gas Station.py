class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas)<sum(cost):
            return -1
        net=[]
        tank=0
        tank_size=0
        for i in range(len(gas)):
            net.append(gas[i]-cost[i])
        for start in range(len(gas)):
            tank=0
            tank=tank+net[start]
            if tank>=0 and gas[start] >= cost[start]:
                if self.circuit_once_check(gas, cost, tank_size,start) == False:
                     continue
                else:
                    return start

    def circuit_once_check(self,gas,cost,tank_size,start):
        n=len(gas)
        for moves in range(n):
            index=(start+moves)%n
            tank_size=tank_size+gas[index]-cost[index]
            if tank_size<0:
                return False
                break
        return True
# Time Complexity: O(n^2) => n (starts) * n (moves per start) = n²
