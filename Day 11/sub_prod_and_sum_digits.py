class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        s=str(n)
        sum,prod=0,1
        for i in s:
             sum+=int(i)
             prod*=int(i)
        return prod-sum
