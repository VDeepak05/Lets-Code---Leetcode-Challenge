class Solution(object):
    def averageValue(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum=0
        count=0
        L=[]
        for i in nums:
            if i%6==0:
                L.append(i)
        for i in L:
            sum+=i
            count+=1
        if count==0:
            return 0
        else:
            return sum//count
