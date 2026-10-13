class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        count=defaultdict(int)
        res,countMax=0,0

        for num in nums:
            count[num]+=1
            res=num if count[num]>countMax else res
            countMax=max(count[num],countMax)
        
        return res