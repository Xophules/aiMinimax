#!/usr/bin/env python3

import math, random
from ...lib.game import discrete_soccer, connect_four



def soccer(state, player_id):
	# TODO: Implement this function!
	#
	# The soccer evaluation function *must* look into the game state
	# when running. It will then return a number, where the larger the
	# number, the better the expected reward (or lower bound reward)
	# will be.
	#
	# For a good evaluation function, you will need to
	# SoccerState-specific information. The file
	# `src/lib/game/discrete_soccer.py` provides a description of all
	# useful SoccerState properties.


	if not isinstance(state, discrete_soccer.SoccerState):
		raise ValueError("Evaluation function incompatible with game type.")


	pos = (state.players[player_id]['x'], state.players[player_id]['y'])
	total  = 10 - state.dist_to_goal(pos, player_id)

	'''if state.players[player_id]['has_ball']:
		total = total + 100

	if pos[0] == 0 or pos[0] == 12:
		total = total - 1000

	if pos[1] == 0 or pos[0] == 18:
		total = total - 1000'''

	#elif not state.ball['on_field']:
	#	total = total - 10

	return total


def connect_four(state, player_id):

	if not isinstance(state, connect_four.Connect4State):
		raise ValueError("Evaluation function incompatible with game type.")
	return random.random()