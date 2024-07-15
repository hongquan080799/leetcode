class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLenght, left = 0, 0
        arrayChar = [-1] * 128 # init array with size 128 with each item equal to -1
        for right, char in enumerate(s):
            if arrayChar[ord(char)] >= left:
               left = arrayChar[ord(char)]  + 1
            else:
                maxLenght = max(maxLenght, right - left + 1)
            arrayChar[ord(char)] = right
        return maxLenght
    

solution = Solution()

print(solution.lengthOfLongestSubstring("pwwkew"))