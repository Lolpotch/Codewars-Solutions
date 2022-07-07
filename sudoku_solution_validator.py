#Solution for "Sudoku Solution Validator" in Codewars

def is_arr_duplicate(arr):
    for i in enumerate(arr):
        v = [j for j in arr]
        v.pop(i[0])
        if i[1] in v:
            return True
            
    return False

def valid_solution(board):
    length = len(board)

    #Validate horizontal
    for bar in board:
        if is_arr_duplicate(bar) or 0 in bar:
            return False
            break
    
    #Validate vertical
    for i in range(length):
        a = []
        for j in range(length):
            a.append(board[j][i])
        
        if is_arr_duplicate(a) or 0 in a:
            return False
            break
    
    #Validate square
    for h in range(1,4):
        for v in range(1,4):
            a = []
            for i in range(3*(h-1),3*h):
                for j in range(3*(v-1),3*v):
                    a.append(board[i][j])
            if is_arr_duplicate(a) or 0 in a:
                return False

    #Return true if no validation return false
    return True

board = [[5, 3, 4, 6, 7, 8, 9, 1, 2], 
         [6, 7, 2, 1, 9, 5, 3, 4, 8],
         [1, 9, 8, 3, 4, 2, 5, 6, 7],
         [8, 5, 9, 7, 6, 1, 4, 2, 3],
         [4, 2, 6, 8, 5, 3, 7, 9, 1],
         [7, 1, 3, 9, 2, 4, 8, 5, 6],
         [9, 6, 1, 5, 3, 7, 2, 8, 4],
         [2, 8, 7, 4, 1, 9, 6, 3, 5],
         [3, 4, 5, 2, 8, 6, 1, 7, 9]]

valid_solution(board)
