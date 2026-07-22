class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows = len(matrix)
        cols = len(matrix[0])

        firstRowZero = False
        firstColZero = False

        # Check first row
        for j in range(cols):
            if matrix[0][j] == 0:
                firstRowZero = True

        # Check first column
        for i in range(rows):
            if matrix[i][0] == 0:
                firstColZero = True

        # Use first row and column as markers
        for i in range(1, rows):
            for j in range(1, cols):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        # Set cells using markers
        for i in range(1, rows):
            for j in range(1, cols):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        # Zero first row
        if firstRowZero:
            for j in range(cols):
                matrix[0][j] = 0

        # Zero first column
        if firstColZero:
            for i in range(rows):
                matrix[i][0] = 0
        