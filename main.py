#--------------------
# Modules
#--------------------
import board
import sys
#--------------------
try:
	board.welcome()
	grid = board.check_choice()
	
	if grid is not None:
		input("Premi ENTER per avviare il gioco.")
		board.run_life(grid)
	
	else:
		print("Errore nella generazione della griglia di gioco.")
		sys.exit()

except KeyboardInterrupt:
	print("\nGioco interrotto.\nA presto!")
	sys.exit()