NEW PATTERN - SPEND TIME AND UNDERSTAND THE CONCEPT - CUSTOM COMPRATOR

Python's sort asks your comparator ONE question:

"Hey comparator, I have element A and element B.
 Should A go before B, after B, or are they equal?
 Tell me with a NUMBER:
    negative = A before B
    zero     = equal
    positive = B before A"
###The comparator is a TRAFFIC COP 🚦
Cars A and B arrive at intersection.
Cop must signal: "A go first" or "B go first"
CORRECT cop:  raises hand signal (-1 or 1)
YOUR cop:     throws car A or car B at Python 😂
Python receives a CAR instead of a SIGNAL → confusion!

''' 
# Sorting ["9", "34"]
# Python calls: comparator("9", "34")
# YOUR CODE:
def wrong(a, b):          # a="9", b="34"
    if a+b > b+a:         # "934" > "349" → TRUE
        return a          # returns "9"
# Python receives "9"
# Python converts to number for comparison: 
#   bool("9") = True = 1 = POSITIVE
#   Positive means "b goes first"
# So Python puts "34" first → "349" ❌  (should be "934")
'''

''' # ANOTHER example: comparator("34", "3")
def wrong(a, b):           # a="34", b="3"
    if a+b > b+a:          # "343" > "334" → TRUE
        return a           # returns "34"
# Python receives "34"
# bool("34") = True = 1 = POSITIVE = "b goes first"
# Puts "3" first → "334" ❌  (should be "343")
'''

bool("9")    # True  → 1 → POSITIVE → "b first"
bool("34")   # True  → 1 → POSITIVE → "b first"
bool("0")    # True  → 1 → POSITIVE → "b first"
bool("")     # False → 0 → ZERO     → "equal"


from functools import cmp_to_key
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        for i in range(len(nums)):
            nums[i]=str(nums[i])
        nums.sort(key=cmp_to_key(self.custom_sorting))
        if nums[0] == "0":
            return "0"
        return "".join(nums)
    def custom_sorting(self, a,b):
        if a+b > b+a:
            return -1
        elif b+a> a+b:
            return 1
        else:
            return 0
    
# So returning ANY non-empty string always means "b goes first"
# Your comparator ALWAYS puts b first — it never puts a first!
# The sort becomes completely meaningless!
