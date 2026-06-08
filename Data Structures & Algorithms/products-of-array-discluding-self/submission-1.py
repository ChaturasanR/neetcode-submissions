# Brute force would be for each number, multiply remaining numbers
# T.C: O(N^2), S.C: O(N), Auxilary S.C: O(1)
# Better way is to calculate running prefix and suffix values for each num
# T.C: O(N), auxilary S.C: O(1)
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if not nums:
            return []

        n = len(nums)
        res = [1] * n

        prefix = suffix = 1
        for i in range(n):
            res[i] *= prefix
            prefix *= nums[i]

            res[n-i-1] *= suffix
            suffix *= nums[n-i-1]
        
        return res
            

       
        

        