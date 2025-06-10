#You are given an array arr[] of non-negative integers. Your task is to move all the zeros in the array to the right end while maintaining the relative order of the non-zero elements. The operation must be performed in place, meaning you should not use extra space for another array.


class Solution:
	def pushZerosToEnd(self,arr):
                count = 0
                for i in range (len(arr)):
                    if arr[i] != 0:
                        arr[i], arr[count] = arr[count],arr[i]
                        count += 1