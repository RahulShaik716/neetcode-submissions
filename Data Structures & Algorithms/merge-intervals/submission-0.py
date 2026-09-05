class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        sorted_intervals = sorted(intervals,key = lambda x:x[0])
        merged = []
        for i in sorted_intervals:
            if not merged or i[0] > merged[-1][1]:
                merged.append(i)
            else:
                merged[-1][1] = max(i[1],merged[-1][1])
        return merged
            