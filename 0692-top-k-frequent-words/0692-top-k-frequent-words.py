from collections import Counter

class Solution:
    def topKFrequent(self, words, k):
        count = Counter(words)
        
        # sort by (-frequency, word)
        sorted_words = sorted(count.keys(), key=lambda x: (-count[x], x))
        
        return sorted_words[:k]