class LanglandsCustom:

	@staticmethod
	def delta(lista):
		δ = lambda lista : [j-i for i, j in zip(lista[:-1], lista[1:])] 
		return δ(lista)
	
	@staticmethod
	def densidade_repetição(δ):		
		β = lambda lista : { (item, lista.count(item)) for item in (lista) }
		return list( sorted( β(δ) ) )

# teste de performance disponíveis no arquivo "performance_langlands_custom.py"