# a minor amendment from pascatriangle1
class Solution:
    # @param {integer} numRows
    # @return {integer[][]}
    def getRow(self, rowIndex):
        numRows = rowIndex + 1
        if numRows == 0:
            res = [1]
        elif numRows == 1:
            res = [[1]]
        else:
            res = [[1],[1,1]]
            numRows += 1
            while numRows > 2:
                cur = []
                last = res[-1]
                cur.append(1)
                for i in range(len(last)-1):
                    cur.append(last[i] + last[i+1])                
                cur.append(1)
                res.append(cur)
                numRows -= 1            
        return res[rowIndex]




# an approach with less space
class Solution:
    # @return a list of lists of integers
    def getRow(self, numRows):
        if numRows < 0:
            return []

        prev_row = [1]
        for i in range(0,numRows):
            row = [1]
            for j in range(1,i+1):
                print('prev_row1', prev_row)
                row.append(prev_row[j-1] + prev_row[j])
                print('prev_row2', prev_row)
                print('##', prev_row[j-1], ',', prev_row[j])
                print('about J', j-1, j)
                print('#', row)

            row.append(1)
            prev_row = row

        return prev_row

    

