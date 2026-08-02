class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left)//2
            mid_elem = nums[mid]
            if target == mid_elem:
                return mid
            
            if target > mid_elem:
                left = mid + 1
            else:
                right = mid - 1
        
        return -1
            
        