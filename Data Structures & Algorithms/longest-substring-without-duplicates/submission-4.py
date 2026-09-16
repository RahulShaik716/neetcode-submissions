class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        maxLength = 0 
        start = 0 
        hash = {}
        for end in range(len(s)):
              hash[s[end]] = 1 + hash.get(s[end],0)

              while hash[s[end]] > 1:
                hash[s[start]] -= 1
                if hash[s[start]] == 0:
                    del hash[s[start]]
                start = start + 1
              maxLength = max(maxLength,end-start+1)
        return maxLength 