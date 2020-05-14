import unittest
import teampredictor

class Testteampredictor(unittest.TestCase):
	def test_printDefaultPokemons(self):
		result= teampredictor.predictor('Pikachu')
		self.assertEqual(result, 'Abra, Kadabra')

