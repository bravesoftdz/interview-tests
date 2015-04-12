import timeit

def lista_sequencia_continua():
	return [ item for item in range(1, 1000000, 2) ]

def lista_de_repeticoes():
	listas = [
		[2]*2, 
		[5]*3,
		[10]*5,
		[4]*5,
		[5]*3,
		[8]*9,
		[2]*8,
		[3]*10,
		[4]*6,
		[5]*8, ]

	return sum(listas, [])


diff_1 = lambda lista : [lista[item]-lista[item-1] for item in range(1,len(lista))] 
diff_2 = lambda lista : [lista[item+1]-lista[item] for item in range(len(lista)-1)]	
diff_3 = lambda lista : [j-i for i, j in zip(lista[:-1], lista[1:])] 

count_1 = lambda lista : [ (i, lista.count(i)) for i in set(lista) ]
count_2 = lambda lista : { (i, lista.count(i)) for i in (lista) }


def teste_diff_1_sequencia_continua():
	return diff_1(lista_sequencia_continua())	

def teste_diff_2_sequencia_continua():
	return diff_2(lista_sequencia_continua())

def teste_diff_3_sequencia_continua():	
	return diff_3(lista_sequencia_continua())

def teste_count_1_sequencia_continua():
	return count_1(lista_de_repeticoes())

def teste_count_2_sequencia_continua():
	return count_2(lista_de_repeticoes())

print("|-- Início Teste Diff 1 ")	
print(timeit.Timer(teste_diff_1_sequencia_continua).timeit(number=1))
print("|-- Fim Teste Diff 1 ")

print("------------------------")

print("|-- Início Teste Diff 2 ")	
print(timeit.Timer(teste_diff_2_sequencia_continua).timeit(number=1))
print("|-- Fim Teste Diff 2 ")

print("------------------------")

print("|-- Início Teste Diff 3 ")	
print(timeit.Timer(teste_diff_3_sequencia_continua).timeit(number=1))
print("|-- Fim Teste Diff 3 ")

print("------------------------")

print("|-- Início Teste Count 1 ")	
print(timeit.Timer(teste_count_1_sequencia_continua).timeit(number=1))
print("|-- Fim Teste Count 1 ")

print("------------------------")

print("|-- Início Teste Count 2 ")	
print(timeit.Timer(teste_count_2_sequencia_continua).timeit(number=1))
print("|-- Fim Teste Count 2 ")

print("------------------------")

