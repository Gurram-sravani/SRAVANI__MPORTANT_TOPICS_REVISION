class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        left=0
        right=0
        basket={}
        max_count=0
        while right<len(fruits):
            print('r',right)
            basket[fruits[right]]=basket.get(fruits[right],0)+1
            #print(basket)
            if len(basket)>2:   # Always use while here because if you if condition to check it only shrinks one time (Shrinks only one position,Window may still be invalid) so using "while" Shrinks as much as needed - Guarantees window validity before moving right
                basket[fruits[left]]-=1
                if basket[fruits[left]]==0:
                    del basket[fruits[left]]
                left+=1
            max_count=max(max_count,(right-left+1))
            right+=1
        return max_count
    
# Time Complexity: O(n) left moves+ O(n) right Moves => O(2n) => O(n)
# Space complexity: O(n)# Space complexity: O(n)
