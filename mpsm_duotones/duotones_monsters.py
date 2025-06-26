#!/usr/bin/env python3
############################################ mpsm : MyPiSensehatMonsters
#
#	LAFONTAINE Cedric Camille 2025
#	contact@codelibre.fr
#
#           _        _ _ _             ___
#  ___ ___ _| |___   | |_| |_ ___ ___  |  _|___
# |  _| . | . | -_|  | | | . |  _| -_|_|  _|  _|
# |___|___|___|___|  |_|_|___|_| |___|_|_| |_|
#
# ASCII art generator: http://patorjk.com/software/taag/
#
#################################################################################
# dependency for python script mpsm - MyPiSensehatMonsters
#################################################################################
import random

O = 'O'
X = 'X'
Y = 'Y'

### OFTEN MONSTERS RANDOM COLORS ARE WONDERFUL! ENJOY!

def Duotonation(bg,fg,other):
	O = bg
	X = fg
	Y = other
	# DEBUG print(f"X:{X} Y:{Y} O:{O}")
	# DEBUG print(f"nombre de monstres: {len(monstres)}")
	monstre = random.choice(monstres)
	# DEBUG print(f"{monstre} shape")
		
	zebebete = []
	for item in monstre:
		if item == 'X':
			zebebete.append(X)
		elif item == 'Y':
			zebebete.append(Y)
		elif item == 'O':
			zebebete.append(O)
		elif isinstance(item, tuple):
			zebebete.append(item)  # Keep tuples as they are, if ever.
		else:
			return None

	# DEBUG print(f"{zebebete} colored")
	return zebebete

monstres = [
	[
	X, O, O, X, X, O, O, X,
	X, O, X, X, X, X, O, X,
	O, X, Y, X, X, Y, X, O,
	O, X, X, X, X, X, X, O,
	O, X, O, O, O, O, X, O,
	O, O, X, X, X, X, O, O,
	X, X, O, X, X, O, X, X,
	X, O, O, O, O, O, O, X
	],
	[
	O, O, X, O, O, X, O, O,
	O, O, X, X, X, X, O, O,
	O, O, X, X, X, X, O, O,
	O, X, O, X, X, O, X, O,
	X, O, X, X, X, X, O, X,
	O, O, X, X, X, X, O, O,
	X, X, O, X, X, O, X, X,
	X, O, O, O, O, O, O, X
	],
	[
	O, O, X, X, X, X, O, O,
	O, X, X, X, X, X, X, O,
	X, X, Y, X, X, Y, X, X,
	X, X, X, X, X, X, X, X,
	X, X, X, X, X, X, X, X,
	O, X, O, O, O, O, X, O,
	O, X, O, O, O, O, X, O,
	O, X, O, O, O, O, X, O
	],
	[
	O, O, O, O, O, O, O, O,
	O, X, X, X, X, X, X, O,
	O, X, O, O, O, O, X, O,
	O, X, Y, O, O, Y, X, O,
	O, X, O, O, O, O, X, O,
	O, X, X, X, X, X, X, O,
	X, X, O, O, O, O, X, X,
	O, X, O, O, O, O, X, O
	],
	[
	O, O, X, O, O, O, X, O,
	O, O, X, X, X, X, X, O,
	O, O, X, Y, X, Y, X, O,
	O, O, X, X, X, X, X, O,
	O, O, X, X, X, X, X, O,
	O, O, X, X, X, X, X, O,
	O, X, O, X, O, X, O, O,
	X, O, X, O, X, O, X, O
	],
	[
	X, O, O, O, O, O, O, X,
	X, X, X, X, X, X, X, X,
	X, O, Y, O, O, Y, O, X,
	X, O, O, O, O, O, O, X,
	X, X, X, X, X, X, X, X,
	O, O, O, X, X, O, O, O,
	O, O, X, X, X, X, O, O,
	O, X, O, O, O, O, X, O
	],
	[
	O, X, O, O, O, O, X, O,
	O, O, X, O, O, X, O, O,
	O, X, Y, X, X, Y, X, O,
	O, X, X, X, X, X, X, O,
	O, X, O, X, X, O, X, O,
	O, O, X, O, O, X, O, O,
	O, O, X, X, X, X, O, O,
	O, O, O, X, X, O, O, O
	],
	[
	X, O, O, O, O, O, O, X,
	O, X, O, O, O, O, X, O,
	X, O, X, O, O, X, O, X,
	O, X, Y, X, X, Y, X, O,
	O, O, X, O, O, X, O, O,
	O, X, O, O, O, O, X, O,
	X, X, O, O, O, O, X, X,
	O, X, O, X, X, O, X, O
	],
	[
	O, X, X, X, X, X, X, O,
	O, X, Y, X, X, Y, X, O,
	O, X, X, X, X, X, X, O,
	O, X, O, X, X, O, X, O,
	X, O, O, X, X, O, O, X,
	O, O, O, X, X, O, O, O,
	O, O, O, X, X, O, O, O,
	O, O, X, O, O, X, O, O
	],
	[
	O, X, X, X, X, X, X, O,
	O, O, Y, X, X, Y, O, O,
	O, O, X, X, X, X, O, O,
	O, X, O, X, X, O, X, O,
	X, O, O, X, X, O, O, X,
	O, O, O, X, X, O, O, O,
	O, O, O, X, X, O, O, O,
	O, O, X, Y, Y, X, O, O
	],
	[
	O, O, O, O, O, O, O, O,
	X, X, X, O, O, X, X, X,
	O, O, X, O, O, X, O, O,
	X, X, X, X, X, X, X, X,
	O, X, Y, X, X, Y, X, O,
	O, X, X, O, O, X, X, O,
	O, X, O, O, O, O, X, O,
	X, X, O, O, O, O, X, X
	],
	[
	O, X, X, O, O, X, X, O,
	O, X, Y, O, O, Y, X, O,
	O, O, X, O, O, X, O, O,
	O, O, X, O, O, X, O, O,
	O, X, X, X, X, X, X, O,
	X, O, X, O, O, X, O, X,
	O, O, O, X, X, O, O, O,
	O, O, X, O, O, X, O, O
	]
]
