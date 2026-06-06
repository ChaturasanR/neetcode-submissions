class Solution:
    # Bucket sort - Max freq that can occur is the nums size
    # Create an list with size of nums + 1 (to start frequency from 1)
    # Store list of numbers for each freq
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = defaultdict(int)
        for num in nums:
            freq_map[num] += 1

        freq_buckets = [[] for _ in range(len(nums) + 1)]
        print(freq_map)
        for num, freq in freq_map.items():
            freq_buckets[freq].append(num)

        
        res = list()
        for freq in range(len(nums), 0, -1):
            if len(freq_buckets[freq]) != 0:
                res.extend(freq_buckets[freq])

            if len(res) == k:
                return res

        return []       