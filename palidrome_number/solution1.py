class Solution:
    def isPalindrome(self, x: int) -> bool:
        number = x
        reversedNumber = 0;
        while number > 0:
            reversedNumber = reversedNumber * 10 + number % 10
            number = number // 10
        return True if reversedNumber == x else False;


solution = Solution()
z = 121

print(solution.isPalindrome(z))