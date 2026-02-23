Store list → must use path.copy()
Store string built from list → join already gives a safe snapshot, no copy needed


class Solution:
  def letterCombinations(digits):
    path=[]
    output=[]
    index=0
    phone = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz"
    }
if digits:
  self.backtrack(path,index,otuput)
  return output
def backtrack(self,path,index,output):
  if index>=len(digits):
    return output.append("".join(path))
  
  for letter in mapping[digits[index]]:
    path.append(letter)
    self.backtrack(path,index+1,output)
    path.pop()

sol=Solution()
print(sol.letterCombinations("23"))

''' 
Why "".join(path) solves the "copy" problemIn Python, strings are immutable. 
When you run "".join(path), Python takes all the characters currently in your list and creates a brand new string object in memory.
Step 1: path is ['a', 'd'].
Step 2: "".join(path) creates a new string "ad".
Step 3: You append that string "ad" to your output list.
Step 4: You path.pop(), so path becomes ['a'].
Because "ad" is a completely separate object from the path list, it doesn't care that the list changed!
If we were storing lists (The "Copy" Rule)If the problem asked for a list of lists (like [['a', 'd'], ['a', 'e']]), 
then you would be 100% correct. You would have to use .copy().
Actionpath (The List)   output     (The Result)
At Base Case['a', 'd']  ["ad"]      (New string created)
Backtrack['a']         ["ad"]       (String remains unchanged)
Next Move['a', 'e']   ["ad", "ae"]      (Another new string)
The List (path): We keep this as one single object in memory and move characters in and out of it to save space (this is the "Backtracking" part).
The Result (output): We only put "snapshots" of the path into the result. By converting the list to a string, we are effectively taking a permanent snapshot that won't change when the list does.
