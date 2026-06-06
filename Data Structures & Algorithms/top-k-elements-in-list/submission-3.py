class Solution:
    # T.C: O(NlogK), S.C: O(N + K) ~ O(2N) ~ O(N), small correct in T.C from last time as
    # max of K elements will be there in the heap
    # Idea is to use min heap
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Calculate freq of each num
        freq_map = defaultdict(int)
        for num in nums:
            freq_map[num] += 1

        # if k is greater the nums array
        if len(nums) <= k:
            return list(freq_map.keys())

        # Maintain top most k frequent numbers using min heap
        min_heap = []
        for num, freq in freq_map.items():
            heapq.heappush(min_heap, (freq, num))

            # Heap size exceed the limit intended
            if len(min_heap) > k:
                heapq.heappop(min_heap)
        
        return [num for freq, num in min_heap]
        