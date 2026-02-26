class Solution(object):
    def returnToBoundaryCount(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum=0
        count=0
        for i in nums:
            sum+=i
            if sum==0:
                count+=1
        return count
