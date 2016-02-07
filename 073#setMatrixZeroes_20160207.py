# 73 setMatrixZeroes.py
class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        zrows, zcols = [], []
        row = len(matrix)
        col = len(matrix[0])
        for i in range(row):
            for j in range(col):
                if matrix[i][j] == 0:
                    zrows.append(i)
                    zcols.append(j)
        for r in zrows:
            matrix[r] = [0] * col
        for c in zcols:
            for t in range(row):
                matrix[t][c] = 0
if __name__ == "__main__":
    m = [[1,2,3],
         [0,3,4],
         [1,1,1],
         [2,0,5]]
    print(m)
    test = Solution()
    test.setZeroes(m)
    print(m)
