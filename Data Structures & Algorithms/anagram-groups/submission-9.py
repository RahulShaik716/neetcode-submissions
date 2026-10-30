class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #naive
        grouped = {}

        for s in strs:
            key = "".join(sorted(s))
            if key not in grouped:
                grouped[key] = []
            
            grouped[key].append(s)
        
        return list(grouped.values())