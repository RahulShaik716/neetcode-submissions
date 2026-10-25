class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #input : list of strings , 
        #output : list of list of strings , list -> grouped strings , 
        #anagram : two strings having the same characters . 
        # we can have 10000 strings, each string can have utmost 100 characters, 10000 * 100 -> 10^6 , characters . 
        #they are made up of only lowercase english letters. 

        #naive approach , i can think of is , 
        #sort the string , make it a key for a dictionary , append the string to that array of that key. 
        # grouped = {}
        # for s in strs:
        #     key = "".join(sorted(s)) #O(klogk) k <=100 
        #     if key not in grouped:
        #         grouped[key] = []
        #     grouped[key].append(s)
        # #entire loop is O(n)
        # return list(grouped.values())

        #time - O(n) + O(klogk) , space - O(n) -> worst case every string is unique ,

        # i can optimizing the key , instead of sorting we can use character count in a string to be the key . 
        # lowercase english alphabets are 26, we can take a list with 26 length that represent english alphabets and take the count of the characters. 
        res = {}
        for word in strs:
            count = [0] * 26 
            for character in word:
                count[ord(character) - ord("a")] += 1
            
            key = tuple(count)
            if key not in res:
                res[key] = []
            res[key].append(word)
        
        return list(res.values())

