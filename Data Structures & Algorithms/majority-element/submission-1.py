class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        # count=defaultdict(int)
        # res,countMax=0,0

        # for num in nums:
        #     count[num]+=1
        #     res=num if count[num]>countMax else res
        #     countMax=max(count[num],countMax)
        
        # return res

        res=0
        count=0

        for n in nums:
            if count==0: res=n
            count+= (1 if n==res else -1)
        return res


        
