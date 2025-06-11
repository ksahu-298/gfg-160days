#You are given an array of integers arr[]. Your task is to reverse the given array.

# Note: Modify the array in place.
class Solution:
    def reverseArray(self, arr):
        l = 0
        r = len(arr)-1
        
        while l<r:
            arr[l], arr[r] = arr[r], arr[l]
            l += 1
            r -= 1
            
            
        
        
        