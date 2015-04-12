import numpy

class LanglandsNumPy:

	@staticmethod
	def delta(lista):	
		arr = numpy.array(lista)		
		return numpy.diff(arr).tolist()
	
	@staticmethod
	def densidade_repetição(delta):
		número, repetição = numpy.unique(delta, return_counts=True)
		return list(zip(número, repetição))
		
