class Solution:
    def romanToInt(self, s: str) -> int:
        mapNum = {
                    "I": 1,
                    "V": 5,
                    "X": 10,
                    "L": 50,
                    "C": 100,
                    "D": 500,
                    "M": 1000
                }
        num = 0
        i = 0
        while i != len(s):
            if i+1 < len(s) and mapNum[s[i]] < mapNum[s[i+1]]:
                num += mapNum[s[i+1]] - mapNum[s[i]]
                i +=2
            else:
                num += mapNum[s[i]]
                i += 1
        return num
        

solution = Solution()

print(solution.romanToInt("III"))
print(solution.romanToInt("LVIII"))
print(solution.romanToInt("MCMXCIV"))