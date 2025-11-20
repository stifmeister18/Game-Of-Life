leggenda = {0:' · ',
			1:' O ',
			'w':' - ',
			'h':' | '}

def renderizza(grid):
	board = '-' + leggenda['w'] * len(grid[0]) + '-\n'

	for y in grid:
		board+= '|'
		for x in y:
			board+= leggenda[x]
		board += '|\n'
	board += '-' + leggenda['w'] * len(grid[0]) + '-'
	return board