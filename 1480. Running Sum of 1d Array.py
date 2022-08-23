class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        print(nums)
        sum_all=0
        final=[]
        for i in nums:
            sum_all=sum_all+i
            final.append(sum_all)
        return final