class Solution(object):
    def countPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        ans=0
        for i in range(0,len(nums)-1):
            for j in range(i+1,len(nums)):
                if nums[i]==nums[j] and (i*j)%k==0:
                    ans+=1
        return ans