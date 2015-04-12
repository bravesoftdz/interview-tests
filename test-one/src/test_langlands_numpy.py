import unittest

from langlands_numpy import LanglandsNumPy

class TestLanglandsNumPy(unittest.TestCase):
	
	def test_delta_lista_fixa(self):	
		lista = [1, 3, 6]			
		self.assertEqual(LanglandsNumPy.delta(lista), [2, 3])

	def test_densidade_repeticao_lista_fixa(self):	
		lista = [1, 4, 7, 9, 14, 21, 24, 25, 29, 30, 35, 38]
		delta = LanglandsNumPy.delta(lista)	
		self.assertListEqual(LanglandsNumPy.densidade_repetição(delta), 
			[ (1, 2),
			  (2, 1),
			  (3, 4), 			   
			  (4, 1),
			  (5, 2), 
			  (7, 1), ])

if __name__ == '__main__':
    unittest.main()