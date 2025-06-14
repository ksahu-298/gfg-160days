#You are given an array of integer arr[] where each number represents a vote to a candidate. Return the candidates that have votes greater than one-third of the total votes, If there's not a majority vote, return an empty array. 

#Note: The answer should be returned in an increasing format.
class Solution:
    # Function to find the majority elements in the array
    def findMajority(self, arr):
        n = len(arr)
        ele1 , ele2 = -1, -1
        count1 , count2 = 0, 0
        
        for ele in arr:
            if ele1 == ele:
                count1 +=1
            elif ele2 == ele:
                count2 += 2
            elif count1 == 0:
                ele1 = ele
                count1 +=1
            elif count2 == 0:
                ele2 = ele
                count2 +=1
            else:
                count1 -=1
                count2 -=1
        
        res=[]
        count1 , count2 = 0,0
        
        for ele in arr:
            if ele1 == ele:
                count1 +=1
            if ele2 == ele:
                count2 +=1
        
        if count1 > n/3:
            res.append(ele1)
        if count2 > n/3 and ele1 != ele2:
            res.append(ele2)
        
        if len(res) == 2 and res[0] > res[1]:
            res[0] , res[1] = res[1] , res[0]
        
        return res