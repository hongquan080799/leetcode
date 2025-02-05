from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        m = len(matrix)
        n = len(matrix[0])

        for i in range(m):
            for j in range(i + 1,n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        # reveres rows
        for i in range(m):
            matrix[i].reverse()
        print(matrix)
solution = Solution()
result = solution.rotate([[1,2,3],[4,5,6],[7,8,9]])
