#!/user/bin/env python

from cardList import addCard
import tcgpowers, mechanics

#Simple variables
NAME = "Energy Inversion"
COST = 4
RARITY = 'R'
DESC = "Your opponent gains lifeforce equal to your total energy (counts negative numbers)."
TARGETS = None
TYPE = "PlyInteraction"

#What happens when you play it
def playFunc(ply, enemy, target):
	enemy.lifeforce = enemy.lifeforce + ply.energy
	
addCard( NAME, COST, RARITY, DESC, TARGETS, TYPE, playFunc )
