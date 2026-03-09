Use prefix sum approach by checking tank=gas[i]-cost[i]+tank => whenever you get tank value negative it means that from the start index to current index - you cannot start  
"net = [1,1,1,1,1,1,1,1,-10] // gas[i]-cost[i]
Greedy scan:
start=0
tank accumulates until index 8
at index 8 → tank becomes negative
Now GREEDY says:
👉 If start=0 failed at index 8
👉 then start=1,2,3,4,5,6,7,8 will ALSO fail

Why?
Because starting later gives less accumulated gas before reaching index 8.
So greedy skips all those starts and jumps directly to:
start = 9"


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


Optimized approach:

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas)<sum(cost):
            return -1
        tank=0
        start=0
        s=0
        while s<len(gas):
            tank=tank+gas[s]-cost[s]
            if tank<0:
                start=s+1
                tank=0
            s+=1
        return start

# Time Complexity:O(n) 

