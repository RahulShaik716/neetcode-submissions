class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        min_stack = []
        results = [0] * len(temperatures)
        for index,value in enumerate(temperatures):
            while min_stack and value > temperatures[min_stack[-1]]:
                    idx = min_stack.pop()
                    results[idx] = index-idx
            min_stack.append(index)
        return results 

        