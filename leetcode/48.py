

#48


class Solution:
    def rotate(self, matrix):
        """
        Do not return anything, modify matrix in-place instead.
        """
        # print(matrix[1][1])

        for i,c in enumerate(matrix):
            print(c)



s=Solution()
matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(s.rotate(matrix))
