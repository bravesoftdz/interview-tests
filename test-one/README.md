### Nesse teste foi proposto duas soluções:

#### Primeira solução.

Utilizei a biblioteca [NumPy](http://www.numpy.org/).

Para instalar a biblioteca execute:

```
sudo pip install numpy
```

Para rodar os testes, execute:

```
python3.4 src/test_langlands_custom.py
```

Código fonte da implementação [langlands_numpy.py](https://github.com/johnidm/interview-tests/blob/master/test-one/src/langlands_numpy.py).


#### Segunda solução

Desenvolvi um algoritmo utilizando [list comprehension](https://docs.python.org/2/tutorial/datastructures.html#list-comprehensions) e [dicionary compressions]( https://docs.python.org/2/tutorial/datastructures.html#dictionaries).

Para rodar os testes, execute:

```
python3.4 src/test_langlands_custom.py
```

Código fonte da implementação [langlands_custom.py](https://github.com/johnidm/interview-tests/blob/master/test-one/src/langlands_custom.py).

O prefixo `Langlands` utilizado nas classes e arquivos é uma referência a [Robert Langlands](http://en.wikipedia.org/wiki/Robert_Langlands) professor de matemática responsável pelo [Programa de Langlands](http://en.wikipedia.org/wiki/Langlands_program).

Referência: [Amor a Matemática - Edward Frenkel](http://www.casadapalavra.com.br/livros/602/Amor+e+matematica).
