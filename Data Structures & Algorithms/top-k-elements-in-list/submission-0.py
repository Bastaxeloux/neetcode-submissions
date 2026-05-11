class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = dict()
        for num in nums:
            freq[num] = freq.get(num,0) + 1
        top_k = sorted(freq, key = freq.get, reverse=True)[:k]
        return top_k