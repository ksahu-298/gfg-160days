#Given an array of integers arr[] in a circular fashion. Find the maximum subarray sum that we can get if we assume the array to be circular.
class Solution:
    def circularSubarraySum(self, arr):
            totalSum = 0
            currMaxSum = 0
            currMinSum = 0
            maxSum = arr[0]
            minSum = arr[0]
            
            for i in range(len(arr)):
                currMaxSum = max(currMaxSum + arr[i], arr[i])
                maxSum = max(maxSum , currMaxSum)
                
                currMinSum = min(currMinSum + arr[i], arr[i])
                minSum = min(minSum, currMinSum)
                
                totalSum += arr[i]
            
            normalSum = maxSum
            circularSum = totalSum - minSum
            
            if minSum == totalSum:
                return normalSum
                
            return max(normalSum, circularSum)