class Solution:
    # Brute force - picking pair O(N^2), S.C: O(1)
    # HashMap - Use hashmap to store visit numbers, T.C: O(N), S.C: O(N)
    # Two pointer - use left and right pointers pointing to other ends of the array and move them based
    # on conditions. T.C: O(N), S.C: O(1)
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        if not numbers:
            return [-1, -1]
        
        left, right = 0, len(numbers) - 1
        while left < right:
            sum_val = numbers[left] + numbers[right]
            if sum_val == target:
                return [left + 1, right + 1]
            elif sum_val < target:
                left += 1
            else:
                right -= 1
        return [-1, -1] 