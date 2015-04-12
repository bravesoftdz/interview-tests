import unittest
from langlands_custom import LanglandsCustom

class TestLanglandsCustom(unittest.TestCase):
	
	def test_delta_lista_fixa(self):	
		lista = [5, 7, 12]	
		self.assertEqual(LanglandsCustom.delta(lista), [2, 5])						
			
	def test_densidade_repeticao_lista_fixa(self):	
		lista = [5, 9, 14, 59, 64, 98, 100, 102, 109, 119, 124]
		delta = LanglandsCustom.delta(lista)	
		self.assertListEqual(LanglandsCustom.densidade_repetição(delta), 
			[ (2, 2),
			  (4, 1),
			  (5, 3), 			   
			  (7, 1),
			  (10, 1),
			  (34, 1), 
			  (45, 1), ])			  

if __name__ == '__main__':
    unittest.main()