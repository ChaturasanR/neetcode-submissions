# Brute force would be for each number, multiply remaining numbers
# T.C: O(N^2), S.C: O(N), Auxilary S.C: O(1)
# Better way is to store prefix and suffix multiplications for each number
# And finally do the product of suffix and prefix values
# 3 iterations of the arrays. T.C: O(N), Auxilary and S.C: O(N)
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if not nums:
            return []

        n = len(nums)
        prefix = []
        for i in range(n):
            if i == 0:
                prefix.append(1)
                continue
            
            prefix.append(prefix[i-1] * nums[i-1])
            

        suffix = []
        for i in range(n-1, -1, -1):
            if i == n-1:
                suffix.append(1)
                continue

            suffix.append(nums[i+1] * suffix[n-2-i])
        
        product = []
        for i in range(n):
            product.append(prefix[i] * suffix[n-i-1])
        
        return product
        

        