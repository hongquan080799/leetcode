from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []
        m = len(matrix[0])
        n = len(matrix)
        top, bottom = 0, n
        left, right = 0, m
        while left < right and top < bottom:
            for i in range(left, right):
                result.append(matrix[top][i])
            top += 1
            for i in range(top, bottom):
                result.append(matrix[i][right - 1])
            right -= 1
            if not (left < right and top < bottom):
                break
            for i in range(right - 1, left - 1, -1):
                result.append(matrix[bottom - 1][i])
            bottom -= 1
            
            for i in range(bottom - 1, top - 1, - 1):
                result.append(matrix[i][left])
            left += 1
        return result
            
solution = Solution()

print(solution.spiralOrder([[1,2,3,4]]))
# [[1,2,3,4],
#  [5,6,7,8],
#  [9,10,11,12]]