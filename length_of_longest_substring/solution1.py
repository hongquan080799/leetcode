class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLenght, left = 0, 0
        charSet = set()
        for right, char in enumerate(s):
            if char in charSet:
                while s[left] in charSet:
                    charSet.remove(s[left])
                    left += 1
            else:
                charSet.add(char)
                maxLenght = max(maxLenght, right - left + 1)
        return maxLenght
    

solution = Solution()

print(solution.lengthOfLongestSubstring("abcabcbb"))