'''
Given an input binary as form a string and integer k. 
Find the number of valid '1,0' combination can be made from the each subsequence after applying 'operation x', which is optional, to get k number of such combinations.
operation x: add bit 1 or 0 until k number of '1,0' combinations are made.
'''

class Solution(object):
    def findValidBin(self,bin,k):
        result = 0
        value = 0
        noOfOnes = 0
        for i in bin:
            if i == "1":
                noOfOnes +=1
            if i == "0":
                value += noOfOnes
            
            if k < value + noOfOnes:
                return result
            else:
                result +=1
        return result
    
print(Solution().findValidBin("100",1))