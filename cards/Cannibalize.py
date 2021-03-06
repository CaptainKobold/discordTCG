#!/user/bin/env python

from cardList import addCard
import tcgpowers, mechanics

#Simple variables
NAME = "Cannibalize"
COST = 1
RARITY = 'C'
DESC = "Heal 10 lifeforce. Lose 5 Hunger."
TARGETS = None
TYPE = "PlyInteraction"

#What happens when you play it
def playFunc(ply, enemy, target):
	yield from mechanics.heal( ply, 10 )
	ply.hunger -= 5
	
addCard( NAME, COST, RARITY, DESC, TARGETS, TYPE, playFunc )

