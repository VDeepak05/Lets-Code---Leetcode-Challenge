class Solution(object):
    def maxDepth(self, s):
        """
        :type s: str
        :rtype: int
        """
        count=0
        m=0
        for i in s:
            if i=='(':
                count+=1
                m=max(m, count)
            elif i==')':
                count-=1
        return m
