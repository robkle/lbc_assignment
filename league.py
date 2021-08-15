class LeagueTable:
	def __init__(self, lst):
		if not type(lst) is list:
			raise TypeError("Only an empty list or list of type str is allowed.")
		self.players = {}
		for i in lst:
			if not type(i) is str:
				raise TypeError("Only type str allowed.")
			self.players[i] = 0
	
	def add_result(self, player, score = 0):
		if type(player) is str:
			self.players[player] = score if type(score) is int else 0

	def get_scores(self, player):
		return self.players[player] if (player in self.players) else None
	
	def get_player_by_rank(self, rank):
		if type(rank) is int:
			s = sorted(self.players.items(), key=lambda x: x[1], reverse=True)
			return s[rank - 1][0] if (rank <= len(s) and rank > 0) else None
		else:
			return None
