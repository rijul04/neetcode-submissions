class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # First do for same number in same row        
        for row in board:
            row = [value for value in row if value != "."]
            row_len = len(row)
            set_len = len(set(row))

            if row_len != set_len:
                # print(row)
                return False

        # Second do for same number is same column
        for i in range(len(board)):
            col = []
            for j in range(len(board[i])):
                if board[j][i] != ".":
                    col.append(board[j][i])
            set_len = len(set(col))
            col_len = len(col)

            if len(set(col)) != col_len:
                return False


        # third do each square
        # print("square")

        for i in range(3, len(board), 3):
            for j in range(3, len(board), 3):
            # if i == 3:
            #     square = [row[0:i] for row in board[0:i]]
            #     square_flatten = [value for row in square for value in row if value != "."]
            #     square_len = len(square_flatten)
            #     set_len = len(set(square_flatten))


            #     if square_len != set_len:
            #         print("1")
            #         return False
            #     continue

                square = [row[i-3 if i != 3 else 0:i] for row in board[j-3 if j != 3 else 0:j]]
                square_flatten = [value for row in square for value in row if value != "."]
                square_len = len(square_flatten)
                set_len = len(set(square_flatten))

                print(square)

                if square_len != set_len:
                    print(square)
                    print(square_flatten)
                    print(i)
                    return False
            
        return True
        
