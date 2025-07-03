# Given a string s, the task is to find the minimum characters to be added at the front to make the string palindrome.

# Note: A palindrome string is a sequence of characters that reads the same forward and backward.
def computeLPSArray(pat):
    n= len(pat)
    lps = [0]*n
    len_lps = 0
    i = 1
    while i<n:
        if pat[i] == pat[len_lps]:
            len_lps += 1
            lps[i] = len_lps
            i+=1
        else:
            if len_lps != 0:
                len_lps = lps[len_lps-1]
            else:
                lps[i] = 0
                i+= 1
    return lps
class Solution:
    def minChar(self, s):
        n = len(s)
        rev = s[:: -1]
        
        s= s + "$" + rev
        lps = computeLPSArray(s)
        
        return n-lps[-1]
