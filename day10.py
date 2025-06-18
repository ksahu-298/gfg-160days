#Given an integer array arr[]. You need to find the maximum sum of a subarray.
#Kadane's Algorithm
class Solution:
    def maxSubArraySum(self, arr):
        res = arr[0]
        maxEnding = arr[0]
        
        for i in range (1, len(arr)):
            maxEnding = max(maxEnding + arr[i] , arr[i])
            res = max(res, maxEnding)
        return res