#!/usr/bin/env python3
############################################ mpsm : MyPiSensehatMonsters
#
#	LAFONTAINE Cédric Camille 2025
#	contact@codelibre.fr
#
#           _        _ _ _             ___
#  ___ ___ _| |___   | |_| |_ ___ ___  |  _|___
# |  _| . | . | -_|  | | | . |  _| -_|_|  _|  _|
# |___|___|___|___|  |_|_|___|_| |___|_|_| |_|
#
# ASCII art generator: http://patorjk.com/software/taag/
#
########################################################################
# USAGE EXAMPLE:
# from sense_hat import SenseHat
# from mpsm import *
#
# sense = SenseHat()
# DisplayOneRandomMonster(sense)
# ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# >>> to add a random-colored background:
# DisplayOneRandomMonster(sense, True)
# ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# FOR A NON RANDOM-COLORED:
#
#		rouge = (255,0,0)
#		blanc = (255,255,255)
#		vide = (0,0,0)
#		DisplayOneRandomMonsterWithMyColors(sense, rouge, blanc, vide)
########################################################################

from mpsm_duotones import duotones_monsters
from random import randint

def OneRandomRGBColor():
  random_red = randint(0, 255)
  random_green = randint(0, 255)
  random_blue = randint(0, 255)
  return (random_red, random_green, random_blue)

def TupleOuPas(inconnue):
    return (
        isinstance(inconnue, tuple) and
        len(inconnue) == 3 and
        all(isinstance(i, int) for i in inconnue)
    )

def DisplayOneRandomMonster(sense, colored_background=False):
	# Check if SenseHat is connected
	if sense:
		bg = (0,0,0)
		if (colored_background):
			bg = OneRandomRGBColor()
		# random foreground color
		fg = OneRandomRGBColor()
		# I use other for the eyes
		other = OneRandomRGBColor()
		# random a monster!
		monstre = duotones_monsters.Duotonation(bg, fg, other)
		if (monstre):
			print("+++ [SENSEHAT] has a new monster.")
			sense.set_pixels(monstre)
	else:
		print("----[ERROR] sensehat not found")

def DisplayOneRandomMonsterWithMyColors(sense, bg, fg, other):
	# Check if SenseHat is connected
	if sense:
		if ((TupleOuPas(bg) == True) and (TupleOuPas(fg) == True) and (TupleOuPas(other) == True)):
			monstre = duotones_monsters.Duotonation(bg, fg, other)
			if (monstre):
				print("+++ [SENSEHAT] has a new monster with your colors.")
				sense.set_pixels(monstre)
		else:
			print("--- [ERROR] wrong RGB tuples")
	else:
		print("----[ERROR] sensehat not found")
