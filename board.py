#--------------------
# Modules
#--------------------
import random
import os
from time import sleep


#--------------------
# Global Variables
#--------------------
ALIVE = 1
DEAD = 0
SURVIVAL_RATE = 0.62

OFFSET = {
		'up' : (-1,0),
		'down' : (1,0),
		'left' : (0,-1),
		'right' : (0,1),
		'uplft' : (-1,-1),
		'uprgt' : (-1,1),
		'dwnlft' : (1,-1),
		'dwnrgt' : (1,1)
		}

legend = {
			0 : ' · ',
			1 : ' O ',
			'w' : ' - ',
			'h' : ' | '
			}


#--------------------
# Functions
#--------------------


def welcome():
	print("\033[2J\033[H", end="")
	print("Benvenuto.")
	print("Questo è Game of Life, premi:")
	print("ENTER\t per utilizzare i parametri di default.")
	print("-o\t per modificare i parametri.")
	print("Ctrl+C\t per interrompere il gioco in qualsiasi momento.")


def check_choice():
	"""
    Gestisce l'input iniziale e restituisce SEMPRE una griglia pronta.
    """

	choice = input()
	if choice == '-o':
		return settings()
	elif choice == '':
		h = get_height()
		w = get_width()
		return random_state(h, w)
	else:
		print("Scelta non valida")
		return check_choice()


def settings():
	print("\nSeleziona una delle opzioni:")
	options = {
			1 : 'Change Survival Rate',
			2 : 'Change Board Size',
			3 : 'Load a specific Life Pattern'
		}

	for k, v in options.items():
		print(f"{k}.\t{v}")

	while True:
		try:
			choice = int(input("Opzione:\t"))
			if choice == 1:
				set_survival_rate()
				return random_state(get_height(), get_width())
			elif choice == 2:
				h, w = set_board_size()
				return random_state(h, w)
			elif choice == 3:
				return choose_pattern()
			else:
				print("Numero non valido, riprova.\n")
		except ValueError:
			print("Errore, puoi inserire solo numeri interi.")


def set_board_size():
	while True:
		try:
			print("Inserisci il numero di righe (minimo 2):\t")
			h = int(input())
			print("Inserisci il numero di colonne (minimo 2):\t")
			w = int(input())
			if h >= 2 and w >= 2:
				return [h, w]
			print("Dimensioni troppo piccole per avviare il gioco.")

		except ValueError:
			print("Errore.\nInserisci solo numeri interi")


def get_height(height = 24) -> int:
	return height


def get_width(width: int = 30) -> int:
	return width


def set_survival_rate():
	global SURVIVAL_RATE
	while True:
		try:
			dummy = float(input("Inserisci un valore compreso tra 0.0 e 1.0:\t"))
			if 0.0 <= dummy <= 1.0:
				SURVIVAL_RATE = dummy
				h = get_height()
				w = get_width()
				return (h, w)
			else:
				print("Il numero inserito non rientra nell'intervallo corretto.")

		except ValueError:
			print("Input non valido")

		except TypeError:
			print("Il numero inserito non è corretto.")

	
def death_state(height: int, width: int) -> list[list[int]]:
	"""
	Generates a board with no living cells.

	Args:
		height (int): The number of board rows.
		width (int): The number of board columns.

	Returns:
		list[list[int]]: A board of of size Height x Width containing only 0s.
	"""
	grid = []

	for y in range(height):
		row = [DEAD for _ in range(width)]
		grid.append(row)

	return grid


def random_state(height: int, width: int) -> list[list[int]]:
	"""
	Generates a board populated by cells based on a survival rate.

	Args:
		height (int): The number of board rows.
		width (int): The number of board columns.

	Returns:
		list[list[int]]: A board of of size Height x Width containing 0s and 1s.
	"""
	grid = []

	for y in range(height):
		row = []
		for x in range(width):
			if random.random() < SURVIVAL_RATE:
				row.append(ALIVE)
			else:
				row.append(DEAD)
		grid.append(row)

	return grid


def next_board_state(board: list[list[int]]) -> list[list[int]]:
	"""
	Generates a new board from an existing one,
	updating the state of all cells according to the game's rules.

	Args:
		board(list[list[int]]):

	Returns:
		list[list[int]]: A board of of size Height x Width containing 0s and 1s.
	"""
	h = len(board)
	w = len(board[0])
	final_board = death_state(h, w)

	for y in range(h):
		for x in range(w):

			counter = 0
			for v in OFFSET.values():	# Taking the offsets to calculate
				new_y = y + v[0]		# the neighbour's coordinates.
				new_x = x + v[1]		# Checking boundaries and counting liveliness.

				if 0 <= new_y < h and 0 <= new_x < w:
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


def choose_pattern():
	folder = "LifePatterns"
	current_directory = os.getcwd()
	full_path = os.path.join(current_directory, folder)

	if not os.path.exists(full_path):
		print("Non sono presenti Life Patterns nella cartella di riferimento.")
		print("Il gioco inizierà normalmente.")
		return random_state(get_height(), get_width())

	files = [f for f in os.listdir(full_path) if f.endswith('.txt')]
	if not files:
		print("Non sono presenti Life Patterns nella cartella di riferimento.")
		print("Il gioco inizierà normalmente.")
		return random_state(get_height(), get_width())

	for file in files:
		print(file[:-4])
	while True:
		choice = input("\nInserisci il nome del pattern da avviare (ad esempio glider):\t")
		choice += '.txt'
		if choice in files:
			return load_pattern(os.path.join(full_path, choice))
		else:
			print("File non trovato. Riprova")


def load_pattern(file: str):
	pattern = []
	with open(file, mode='r', encoding='utf-8') as T:
		for row in T:
			row_container = []
			for digit in row:
				if digit == "0":
					row_container.append(0)
				if digit == "1":
					row_container.append(1)
			pattern.append(row_container)
	return pattern


def render(grid):
	board = '-' + legend['w'] * len(grid[0]) + '-\n'

	for y in grid:
		board+= '|'
		for x in y:
			board+= legend[x]
		board += '|\n'
	board += '-' + legend['w'] * len(grid[0]) + '-'
	return board


def run_life(grid):
	try:		
		while True:
			output_grid = render(grid)
			print(output_grid)

			grid = next_board_state(grid)
			sleep(0.15)

			climb_spaces = output_grid.count("\n") + 1
			print(f"\033[{climb_spaces}A", end="")
	except KeyboardInterrupt:
		rows_to_go_down = len(grid) + 2
		print(f"\033[{rows_to_go_down}B", end="")
		print("Gioco interrotto.")