#--------------------
#Librerie
#--------------------
import random


#--------------------
#Variabili Globali
#--------------------
ALIVE = 1
DEAD = 0

#--------------------
#Funzioni
#--------------------


def death_state(height:int, width:int) -> list[list[int]]:
	grid = []

	for y in range(height):
		L= list()
		for x in range(width):
			L.append(DEAD)
		grid.append(L)

	return grid


def random_state(grid: list[list[int]]) -> list[list[int]]:

	for y in range(len(grid)):
		for x in range(len(grid[0])):
			if random.random() > 0.64:
				grid[y][x] = ALIVE
			else: grid[y][x] = DEAD

	return grid

def next_board_state(board):
	final_board = death_state(len(board), len(board[0]))
	offset = {'su':(-1,0),
			'giu':(1,0),
			'sx':(0,-1),
			'dx':(0,1),
			'susx':(-1,-1),
			'sudx':(-1,1),
			'giusx':(1,-1),
			'giudx':(1,1)}

	for y in range(len(board)):
		for x in range(len(board[0])):
			cell = board [y][x]

			if cell == DEAD:
				conta = 0
				for v in offset.values():
					Y = y + v[0]
					X= x+ v[1]
					if 0 <= Y < len(board) and 0 <= X < len(board[0]):
						if board[Y][X] == ALIVE:
							conta += 1
				if conta == 3:
					final_board[y][x] = ALIVE

			elif cell == ALIVE:
				conta = 0
				for v in offset.values():
					Y = y + v[0]
					X= x+ v[1]
					if 0 <= Y < len(board) and 0 <= X < len(board[0]):
						if board[Y][X] == ALIVE:
							conta += 1
				if conta <= 1:
					final_board[y][x] = DEAD
				elif conta < 4:
					final_board[y][x] = ALIVE
				elif conta >= 4:
					final_board[y][x] = DEAD


	return final_board