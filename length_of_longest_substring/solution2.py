class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLenght, left = 0, 0
        mapChar = {}
        for right, char in enumerate(s):
            if char in mapChar:
               left = mapChar[char]  + 1
            else:
                maxLenght = max(maxLenght, right - left + 1)
            mapChar[char] = right
        return maxLenght
    

solution = Solution()

print(solution.lengthOfLongestSubstring("abcabcbb"))