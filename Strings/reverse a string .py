class Solution:
    def reverseWords(self, s: str) -> str:
        s.strip()  # This throws an error because STRINGS are immutable 
        l=s.split()  # It automatically ignores leading/trailing whitespace, treats multiple spaces/tabs/newlines as one separator
        print(l)
        new_s=' '.join(l[::-1])  # creates a new string because strings are immutable
        return snew_s
# Time cOmplexity: n = length of the string(total characters) k = number of words. split(): creates O(n) Scans entire string once + 
                             # join() : Creates a new string with all characters → O(n) + Reverses list of words → O(k) where k = #words  => O(n)
#Space Complexity: O(n) -> creating a list where n is number of words  + O(n) Extra space to create a new string => O(n)
