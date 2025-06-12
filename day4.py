#Given an array arr[]. Rotate the array to the left (counter-clockwise direction) by d steps, where d is a positive integer. Do the mentioned change in the array in place.


class Solution:
   
    def rotateArr(self, arr, d):
        n = len(arr)
        d = d%n
        
        #REVERSING ALGORITHM
            
        rev(arr,0,d-1)
        rev(arr,d,n-1)
        rev(arr,0,n-1)
        
def rev(arr,start,end):
    while start < end :
        arr[start] , arr[end] = arr[end], arr[start]
        start += 1
        end -= 1