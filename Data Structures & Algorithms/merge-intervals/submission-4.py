class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        #input : array of intervals [start,end]
        #imagine a number line, intervals would occupy bars on the number 
        #sort by start_time
        #then if the start_time of next is less than end_time of current , we need to merge. 
        #else we push as is . 
        #initialize merged array 
        #edge cases : empty array  return empty, single element - single element, duplicate elements - #would be merged . 

        # merged = []
        # intervals.sort(key=lambda x:x[0]) #O(nlogn)

        # for interval in intervals:
        #     if merged and interval[0] <= merged[-1][1]:
        #         merged[-1][1] = max(interval[1],merged[-1][1])
        #     else:
        #         merged.append(interval)
        
        # return merged 
        #time - O(nlogn) , space - O(1) heapsort, O(n) - timsort 

        #next approach , get the max start time of all the intervals . 
        max_start = max(interval[0] for interval in intervals)
        mp = [0] * (max_start + 1)

        for start,end in intervals:
            mp[start] = max(end+1,mp[start])
        
        res = []
        interval_start = -1
        have = -1 

        for i in range(len(mp)):
            if mp[i]!=0:
                if interval_start == -1:
                    interval_start = i 
                have = max(mp[i]-1,have)
            #we have reached the end of interval
            if have == i:
                res.append([interval_start,have])
                interval_start = -1
                have = -1
        if interval_start!=-1:
            res.append([interval_start,have])
        return res