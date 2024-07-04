from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = ''
        minWord, maxWord = max(strs), min(strs)
        for i in range(len(minWord)):
            if minWord[i] == maxWord[i]:
                result += minWord[i]
        return result
    

solution = Solution()

strs = ["flower", "flow", "flight"]

print(solution.longestCommonPrefix(strs))  # Output: "fl"
        