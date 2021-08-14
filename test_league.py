#!/usr/bin/env python3

import unittest
import league

class TestLeague(unittest.TestCase):
	def setUp(self):
		self.table1 = league.LeagueTable(['Bob', 'Joe', 'Jim'])
		self.table2 = league.LeagueTable([])

	def populate(self):
		self.table1.add_result('Bob', 23)
		self.table1.add_result('Joe', 15)
		self.table1.add_result('Jim', 39)

	def test_init(self):
		self.assertEqual(self.table1.players, {'Bob': 0, 'Joe': 0, 'Jim': 0})
		self.assertEqual(self.table2.players, {})
		table3 = league.LeagueTable(['Bob', 'Bob', 'Joe', 'Jim'])
		self.assertEqual(table3.players, {'Bob': 0, 'Joe': 0, 'Jim': 0})
		with self.assertRaises(TypeError):
			verror1 = league.LeagueTable([1, 2, 3])
			verror2 = league.LeagueTable([['Adam', 'Bob', 'Carl'], ['Dave', 'Ed']])
			verror3 = league.LeagueTable(['Adam', None])
			verror4 = league.LeagueTable('Adam')
			verror5 = league.LeagueTable({})
	
	def test_add(self):
		self.populate()
		self.assertEqual(self.table1.players, {'Bob': 23, 'Joe': 15, 'Jim': 39})
		self.table1.add_result('Bob', 99)
		self.assertEqual(self.table1.players, {'Bob': 99, 'Joe': 15, 'Jim': 39})
		self.table2.add_result('Jim', 39)
		self.assertEqual(self.table2.players, {'Jim': 39})
		self.table2.add_result(99, 99)
		self.assertEqual(self.table2.players, {'Jim': 39})
		self.table2.add_result('Jim', 'xx')
		self.assertEqual(self.table2.players, {'Jim': 0})
		self.table2.add_result('Jack')
		self.assertEqual(self.table2.players, {'Jim': 0, 'Jack': 0})

	def test_get_score(self):
		self.assertEqual(self.table1.get_scores('Jim'), 0)
		self.populate()
		self.assertEqual(self.table1.get_scores('Bob'), 23)
		self.assertEqual(self.table1.get_scores('Max'), None)
		self.assertEqual(self.table1.get_scores(23), None)
		self.assertEqual(self.table2.get_scores('Bob'), None)

	def test_get_rank(self):
		self.assertEqual(self.table1.get_player_by_rank(1), 'Bob')	
		self.assertEqual(self.table1.get_player_by_rank(2), 'Joe')	
		self.assertEqual(self.table1.get_player_by_rank(3), 'Jim')	
		self.populate()
		self.assertEqual(self.table1.get_player_by_rank(1), 'Jim')	
		self.assertEqual(self.table1.get_player_by_rank(2), 'Bob')	
		self.assertEqual(self.table1.get_player_by_rank(3), 'Joe')	
		self.assertEqual(self.table1.get_player_by_rank(4), None)	
		self.assertEqual(self.table1.get_player_by_rank(0), None)	
		self.assertEqual(self.table1.get_player_by_rank(-1), None)
		self.assertEqual(self.table2.get_player_by_rank(1), None)	
		self.assertEqual(self.table1.get_player_by_rank('x'), None)
		self.table1.add_result('Max', 99)	
		self.assertEqual(self.table1.get_player_by_rank(1), 'Max')	
		self.assertEqual(self.table1.get_player_by_rank(2), 'Jim')	

if __name__ == '__main__':
	unittest.main()
