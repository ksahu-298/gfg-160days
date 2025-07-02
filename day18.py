#Given two strings, one is a text string txt and the other is a pattern string pat. The task is to print the indexes of all the occurrences of the pattern string in the text string. Use 0-based indexing while returning the indices. 
# Note: Return an empty list in case of no occurrences of pattern.
#User function Template for python3
def constructLps(pat,lps):
    len_ = 0
    m = len(pat)
    
    lps[0] = 0
    i=1
    while i<m:
        if pat[i] == pat[len_]:
            len_+=1
            lps[i]=len_
            i+=1
        else:
            if len_ != 0:
                len_ = lps[len_-1]
            else:
                lps[i] = 0
                i+=1


class Solution:
    def search(self, pat, txt):
        n= len(txt)
        m = len(pat)
        
        lps = [0]*m
        res = []
        
        constructLps(pat,lps)
        
        i=0
        j=0
        while i<n:
            
            if txt[i] == pat[j]:
                i+=1
                j+=1
                
            if j==m:
                res.append(i-j)
                j=lps[j-1]
                
            elif i<n and txt[i]!=pat[j]:
                
                if j!=0:
                    j=lps[j-1]
                else:
                    i+=1
        
        return res