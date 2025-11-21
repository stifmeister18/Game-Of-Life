#--------------------
# Modules
#--------------------
import random


#--------------------
# Global Variables
#--------------------
ALIVE = 1
DEAD = 0
OFFSET = {'up' : (-1,0),
		'down' : (1,0),
		'left' : (0,-1),
		'right' : (0,1),
		'uplft' : (-1,-1),
		'uprgt' : (-1,1),
		'dwnlft' : (1,-1),
		'dwnrgt' : (1,1)}

#--------------------
# Functions
#--------------------


def death_state(height: int, width: int) -> list[list[int]]:
	grid = []

	for y in range(height):
		row = []
		for x in range(width):
			row.append(DEAD)
		grid.append(row)

	return grid


def random_state(grid: list[list[int]]) -> list[list[int]]:

	for y in range(len(grid)):
		for x in range(len(grid[0])):
			if random.random() > 0.64:
				grid[y][x] = ALIVE
			else:
				grid[y][x] = DEAD

	return grid


def next_board_state(board):
	final_board = death_state(len(board), len(board[0]))

	for y in range(len(board)):
		for x in range(len(board[0])):
			counter = 0
			for v in OFFSET.values():
				new_y = y + v[0]
				new_x = x + v[1]
				if 0 <= new_y < len(board) and 0 <= new_x < len(board[0]):
					if board[new_y][new_x] == ALIVE:
						counter += 1

			cell = board[y][x]
			if cell == ALIVE:
				if counter == 2 or counter == 3:
					final_board[y][x] = ALIVE
			else:
				if counter == 3:
					final_board[y][x] = ALIVE

	return final_board