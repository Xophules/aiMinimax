#!/usr/bin/env python3

import math, random
from ...lib.game import discrete_soccer, connect_four
#from ...lib import ddqn
from .agent import MinimaxAgent


def soccer(state, player_id, ag = None):
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

	total = 0
	posBall = (state.ball['x'], state.ball['y'])
	posP = (state.players[player_id]['x'], state.players[player_id]['y'])
	distToBall = math.hypot(posBall[0] - posP[0], posBall[1] - posP[1])

	total = total + 2 - distToBall / 13
	if state.players[player_id]['has_ball']:
		print("Player", player_id, "Ball:", state.players[player_id]['has_ball'], state.players[player_id].team)
		print("Player", (player_id + 1) % 2, "Ball:", state.players[(player_id + 1) % 2]['has_ball'],
			  state.players[(player_id + 1) % 2].team)
		print(state)
		total = total + 3

	print("total:", total)

	return total

	#return MinimaxAgent.predictMinmax(ag, state, player_id)


def cf(state, player_id):
	if not isinstance(state, connect_four.Connect4State):
		raise ValueError("Evaluation function incompatible with game type.")
	if state.is_terminal:

		return state.reward(player_id)

	return random.random()
