class Solution:
    def isPalindrome(self, x: int) -> bool:
        number = x
        reversedNumber = 0;
        while number > reversedNumber:
            reversedNumber = reversedNumber * 10 + number % 10
            number = number // 10
        return True if reversedNumber == number or reversedNumber == number / 10 else False;


solution = Solution()
z = 121

print(solution.isPalindrome(z))