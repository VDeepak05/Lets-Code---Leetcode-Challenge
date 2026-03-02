class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        arr=[]
        for i in range(0,len(nums), 2):
            min1=min(nums)
            nums.remove(min1)
            min2=min(nums)
            nums.remove(min2)
            arr.append(min2)
            arr.append(min1)
        return arr
