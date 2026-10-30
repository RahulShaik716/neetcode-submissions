class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # #naive
        # grouped = {}

        # for s in strs:
        #     key = "".join(sorted(s))
        #     if key not in grouped:
        #         grouped[key] = []
            
        #     grouped[key].append(s)
        
        # return list(grouped.values())
        # #n - len of strings , m - len of each string. 
        # #time - O(nlogm) , space - O(n)

        #i will try to use hashmap to count the frequency of characters, lower case english would be a-z , 
        # use that as the key . 

        output = {}

        for s in strs:
            count = [0] * 26 
            for c in s:
                count[ord(c)-ord("a")] += 1
            
            #as key should be immutable in a dictionary, convert list to tuple. 
            key = tuple(count)
            if key not in output:
                output[key] = []
            output[key].append(s)

        return list(output.values())