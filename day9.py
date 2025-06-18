#Given an array arr[] denoting heights of N towers and a positive integer K.
# For each tower, you must perform exactly one of the following operations exactly once.
# Increase the height of the tower by K
# Decrease the height of the tower by K
# Find out the minimum possible difference between the height of the shortest and tallest towers after you have modified each tower
#User function Template for python3

class Solution:
    def getMinDiff(self,arr,k):
        n= len(arr)
        arr.sort()
        res = arr[n-1] - arr[0]
        
        for i in range (1, len(arr)):
          if arr[i] - k < 0:
              continue
          minH = min(arr[0]+k , arr[i]-k)
          maxH = max(arr[i-1]+k , arr[n-1]-k)
          
          res = min(res, maxH-minH)
          
        return res
    