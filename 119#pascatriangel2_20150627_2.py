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

if __name__ == '__main__':
    test = Solution()
    print(test.getRow(5))
    
# an approach with less space
