import numpy as np


ROW_COUNT = 6
COLUMN_COUNT = 7

def create_board():
	board = np.zeros((ROW_COUNT, COLUMN_COUNT))
	return board


def drop_piece(board, row, column, piece):
	board[row][column] = piece


def is_valid_location(board, column):
	return board[ROW_COUNT -1][column] == 0


def get_next_open_row(board, column):
	for row in range(ROW_COUNT):
		if board[row][column] == 0:
			return row

def print_board(board):
	#print(np.flip(board, 0))
	print(board)


def winning_move(board, piece):
	# Check horizontal locations
	for column in range(COLUMN_COUNT -3):
		for row in range(ROW_COUNT):
			if board[row][column] == piece and board[row][column +1] == piece and board[row][column +2] == piece and board[row][column +3] == piece:
				return True

	#Check vertical locations for win




board = create_board()
print_board(board)
game_over = False
turn = 0

while not game_over:
	# Ask for Player 1 input
	if turn == 0:
		column = int(input("Player 1 Make your Selection (0-6):"))

		if is_valid_location(board, column):
			row = get_next_open_row(board, column)
			drop_piece(board, row, column, 1)

			if winning_move(board, 1):
				print("PLAYER 1 WINS!")
				game_over = True



	# Ask for Player 2 input
	else:
		column = int(input("Player 2 Make your Selection (0-6):"))

		if is_valid_location(board, column):
			row = get_next_open_row(board, column)
			drop_piece(board, row, column, 1)
	print_board(board)

	turn += 1
	turn = turn % 2







