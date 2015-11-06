'''
To check a sudoku board is valid or not.
'''
class Solution:
    def isValidSudoku(self, board):
        colums = [[row[i] for row in board] for i in range(9)]

        blocks = [[board[i+k][j+l] for i in range(3) for j in range(3)]
                  for k in range(0,9,3) for l in range(0,9,3)]

        def isvalid(parts):
            flag = 0
            for part in parts:
                part_num = [item for item in part if item != '.']
                part_valid = set(part_num)
                if len(part_num) == len(part_valid):
                    flag += 1
                else:
                    flag += 0
            return True if flag == len(part) else False
        return isvalid(board) and isvalid(colums) and isvalid(blocks)

# sefl test
if __name__ == '__main__':
    board = [[5, 3, '.', '.', 7, '.', '.', '.', '.'],
         [6, '.', '.', 1, 9, 5, '.', '.', '.'],
         ['.', 9, 8, '.', '.', '.', '.', 6, '.'],
         [8, '.', '.', '.', 6, '.', '.', '.', 3],
         [4, '.', '.', 8, '.', 3, '.', '.', 1],
         [7, '.', '.', '.', 2, '.', '.', '.', 6],
         ['.', 6, '.', '.', '.', '.', 2, 8, '.'],
         ['.', '.', '.', 4, 1, 9, '.', '.', 5],
         ['.', '.', '.', '.', 8, '.', '.', 7, 9]
         ]

    instance = Solution()
    test = instance.isValidSudoku(board)
    print(test)






