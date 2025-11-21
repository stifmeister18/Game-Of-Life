#--------------------
# Modules
#--------------------
import board
import render
import time

#--------------------
# Main
#--------------------

print("\033[2J\033[H", end="")
print("Benvenuto.\n" + 
	"Premi Ctrl + C per interrompere in qualsiasi momento.\n")

input("Premi un tasto per continuare.")

# Per modificare le dimensioni della griglia modifica i commenti
# height = int(input('Inserisci l\'height della board:\n'))
# width = int(input('Inserisci la width della board:\n'))
height = 28
width = 36
grid = board.random_state(board.death_state(height, width)) #Initialize board

try:
	while True:
		output_grid = render.render(grid)
		print(output_grid)
		next_grid = board.next_board_state(grid)
		grid = next_grid
		time.sleep(0.15)

		climb_spaces = output_grid.count("\n") + 1
		print(f"\033[{climb_spaces}A", end="")

except KeyboardInterrupt:
	print(f"\033[{height+3}B", end="")
	print("\nGioco interrotto.\nA presto!")