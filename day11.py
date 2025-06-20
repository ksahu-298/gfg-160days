#Given an array arr[] that contains positive and negative integers (may contain 0 as well). Find the maximum product that we can get in a subarray of arr[].

#Note: It is guaranteed that the output fits in a 32-bit integer.

class Solution:
	def maxProduct(self,arr):
            n = len(arr)
            currMax= arr[0]
            currMin = arr[0]
            maxProd = arr[0]
            
            for i in range (1,n):
                temp = max(arr[i], arr[i]*currMax, arr[i]*currMin)
                currMin = min(arr[i], arr[i]*currMax, arr[i]*currMin)
                currMax = temp
                
                maxProd = max(maxProd, currMax)
            return maxProd