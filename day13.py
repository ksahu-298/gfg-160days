#You are given an integer array arr[]. Your task is to find the smallest positive number missing from the array.
#User function Template for python3

class Solution:
    
    #Function to find the smallest positive number missing from the array.
    def missingNumber(self,arr):
        n= len(arr)
        
        for i in range (n):
            while 1<= arr[i]<= n and arr[i]!= arr[arr[i]-1]:
                temp = arr[i]
                arr[i]= arr[arr[i]-1]
                arr[temp-1] = temp
        
        for i in range (1,n+1):
            if i != arr[i-1]:
                return i
                
        
        return n+1