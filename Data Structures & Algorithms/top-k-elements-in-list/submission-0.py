class Solution:
    # T.C: O(NlogN), S.C: O(N)
    # Idea is to use min heap
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Calculate freq of each num
        freq_map = defaultdict(int)
        for num in nums:
            freq_map[num] += 1

        # Maintain top most k frequent numbers using min heap
        min_heap = []
        for num, freq in freq_map.items():
            heapq.heappush(min_heap, (freq, num))

            # Heap size exceed the limit intended
            if len(min_heap) > k:
                heapq.heappop(min_heap)
        
        return [num for freq, num in min_heap]
        