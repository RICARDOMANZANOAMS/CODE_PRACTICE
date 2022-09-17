class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count_all=0
        for i in nums:
            string=str(i)
            count=0
            for j in string:
                count+=1
            if count%2==0:
                count_all+=1
        return count_all
                
        
