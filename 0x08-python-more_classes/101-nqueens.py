#!/usr/bin/python3
"""Solves the N-queens puzzle.

Determines all possible solutions for placing N non-attacking
queens on an NxN chessboard.

Usage:
    $ ./101-nqueens.py N

N must be an integer greater than or equal to 4.

Attributes:
    board (list): A list of lists representing the chessboard.
    solutions (list): A list of lists containing solutions.

Solutions are represented in the format [[r, c], [r, c], [r, c], [r, c]]
where `r` and `c` represent the row and column, respectively, where a queen
must be placed on the chessboard.
"""
import sys


def initialize_board(n):
    """Initialize an `n`x`n` sized chessboard with empty spaces."""
    board = [[" " for _ in range(n)] for _ in range(n)]
    return board


def deepcopy_board(board):
    """Return a deep copy of a chessboard."""
    return [row.copy() for row in board]


def get_solution(board):
    """Return the list of lists representation of a solved chessboard."""
    solution = []
    for r in range(len(board)):
        for c in range(len(board)):
            if board[r][c] == "Q":
                solution.append([r, c])
    return solution


def mark_attacked_spots(board, row, col):
    """Mark non-attacking spots on a chessboard as 'x'."""
    n = len(board)
    for c in range(col + 1, n):
        board[row][c] = "x"
    for c in range(col - 1, -1, -1):
        board[row][c] = "x"
    for r in range(row + 1, n):
        board[r][col] = "x"
    for r in range(row - 1, -1, -1):
        board[r][col] = "x"
    r, c = row + 1, col + 1
    while r < n and c < n:
        board[r][c] = "x"
        r += 1
        c += 1
    r, c = row - 1, col - 1
    while r >= 0 and c >= 0:
        board[r][c] = "x"
        r -= 1
        c -= 1
    r, c = row - 1, col + 1
    while r >= 0 and c < n:
        board[r][c] = "x"
        r -= 1
        c += 1
    r, c = row + 1, col - 1
    while r < n and c >= 0:
        board[r][c] = "x"
        r += 1
        c -= 1


def recursive_solve(board, row, queens, solutions):
    """Recursively solve the N-queens puzzle.

    Args:
        board (list): The current working chessboard.
        row (int): The current working row.
        queens (int): The current number of placed queens.
        solutions (list): A list of lists of solutions.
    Returns:
        solutions (list): A list of lists containing solutions.
    """
    n = len(board)
    if queens == n:
        solutions.append(get_solution(board))
        return solutions

    for col in range(n):
        if board[row][col] == " ":
            tmp_board = deepcopy_board(board)
            tmp_board[row][col] = "Q"
            mark_attacked_spots(tmp_board, row, col)
            solutions = recursive_solve(tmp_board, row + 1,
                                        queens + 1, solutions)

    return solutions


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if not sys.argv[1].isdigit():
        print("N must be a number")
        sys.exit(1)
    n = int(sys.argv[1])
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = initialize_board(n)
    solutions = recursive_solve(board, 0, 0, [])
    for solution in solutions:
        print(solution)
