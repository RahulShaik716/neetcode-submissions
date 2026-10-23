class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        #input : array of intervals [start,end]
        #imagine a number line, intervals would occupy bars on the number 
        #sort by start_time
        #then if the start_time of next is less than end_time of current , we need to merge. 
        #else we push as is . 
        #initialize merged array 
        #edge cases : empty array  return empty, single element - single element, duplicate elements - #would be merged . 

        merged = []
        intervals.sort(key=lambda x:x[0])

        for interval in intervals:
            if merged and interval[0] <= merged[-1][1]:
                merged[-1][1] = max(interval[1],merged[-1][1])
            else:
                merged.append(interval)
        
        return merged
