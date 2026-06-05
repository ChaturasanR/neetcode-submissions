class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0 and target != 0:
            return [-1, -1]

        visited_num_idx_map = dict()
        for i, num in enumerate(nums):
            second_num = target - num
            if second_num in visited_num_idx_map:
                return [visited_num_idx_map[second_num], i]
            
            visited_num_idx_map[num] = i
        
        return [-1, -1]
        