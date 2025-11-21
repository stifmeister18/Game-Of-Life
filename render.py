legend = {0:' · ',
			1:' O ',
			'w':' - ',
			'h':' | '}

def render(grid):
	board = '-' + legend['w'] * len(grid[0]) + '-\n'

	for y in grid:
		board+= '|'
		for x in y:
			board+= legend[x]
		board += '|\n'
	board += '-' + legend['w'] * len(grid[0]) + '-'
	return board