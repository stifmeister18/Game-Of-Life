#--------------------
#Librerie
#--------------------
import board
import render
import time

#--------------------
#Main
#--------------------

print("\033[2J\033[H", end="")
print("Benvenuto.\n" + 
	"Premi Ctrl + C per interrompere in qualsiasi momento.\n")

# altezza = int(input('Inserisci l\'altezza della board:\n'))
# larghezza = int(input('Inserisci la larghezza della board:\n'))

try:
	input("Premi enter per continuare")
except TypeError:
	print("TypeError")


altezza = 28
larghezza = 36
griglia = board.random_state(board.death_state(altezza, larghezza)) #Initialize board

try:
	while True:
		output_griglia = render.renderizza(griglia)
		print (output_griglia)
		next = board.next_board_state(griglia)
		griglia = next
		time.sleep(0.15)

		linee_da_risalire = output_griglia.count("\n") + 1
		print(f"\033[{linee_da_risalire}A", end="")

except KeyboardInterrupt:
	print(f"\033[{altezza+3}B", end="")
	print("\nGioco interrotto.\nA presto!")