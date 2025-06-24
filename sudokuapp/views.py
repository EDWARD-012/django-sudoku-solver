from django.shortcuts import render
import copy

def is_valid(board, row, col, ch):
    for i in range(9):
        if board[row][i] == ch or board[i][col] == ch:
            return False
        if board[3*(row//3) + i//3][3*(col//3) + i%3] == ch:
            return False
    return True

def solve_sudoku(board, solutions, row=0, col=0, limit=10):
    if len(solutions) >= limit:
        return

    if row == 9:
        solutions.append(copy.deepcopy(board))
        return

    next_row, next_col = (row, col+1) if col < 8 else (row+1, 0)

    if board[row][col] != '':
        solve_sudoku(board, solutions, next_row, next_col, limit)
    else:
        for ch in map(str, range(1, 10)):
            if is_valid(board, row, col, ch):
                board[row][col] = ch
                solve_sudoku(board, solutions, next_row, next_col, limit)
                board[row][col] = ''

def home(request):
    return render(request, 'index.html')

def solve(request):
    solutions = []
    board = [['' for _ in range(9)] for _ in range(9)]

    if request.method == 'POST':
        for i in range(9):
            for j in range(9):
                val = request.POST.get(f'cell{i}{j}', '').strip()
                board[i][j] = val if val in '123456789' else ''
        solve_sudoku(board, solutions, limit=10)

    return render(request, 'result.html', {
        'input_board': board,
        'solutions': solutions,
        'num_solutions': len(solutions),
    })
