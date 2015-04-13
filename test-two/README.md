A implementação desse teste esta no arquivo [main.py](https://github.com/johnidm/interview-tests/blob/master/test-two/src/main.py).

A forma que implementei não está usando polimorfismo. Os atributos `X`, `Y`, `Z` possuem uma "única forma" implementada nas classes. Segue o "esquema":

* Classe `A` possui o atributo `X`.
* Classe `B` possui o atributo `Y` e estende a classe `A`.
* Classe `C` possui o atributo `Z` e estende a classe `A`.
* Classe `D` **não** possui atributos e estende as classes `B` e `C`.

Ao acessar o atributo `X` através de uma instância da classe `D`, é invocado a implementação do atributo `X` da classe `A`, pois a implementação desse atributo existe somente na classe `A`.

O comando abaixo exibe esse comportamento:

```
python3.4 src/tests.py -d
```

Baseado na execução do algoritmo do arquivo [virtual_table.py](https://github.com/johnidm/interview-tests/blob/master/test-two/src/virtual_table.py), `python3.4 src/virtual_table.py`, referente a tabela virtual, chega-se a conclusão representada no diagrama abaixo:

![](https://raw.githubusercontent.com/johnidm/interview-tests/master/test-two/images/vt.png)

> A classe `D` herda as classes `B` e `C`. As classes `B` e `C` herdam a classe `A`. Somente uma instância de `A` é criada nas heranças da classe `D`.

Para ver o comportamento de cada classe, execute:

```
python3.4 src/tests.py -a -b -c -d
```

Referências:
* http://en.wikipedia.org/wiki/Virtual_method_table
* http://stackoverflow.com/questions/4714136/python-how-to-implement-virtual-methods
* http://legacy.python.org/workshops/1998-11/proceedings/papers/lowis/lowis.html
* http://www.johnidouglas.com.br/vinculacao-de-metodos-em-delphi/
* http://stackoverflow.com/questions/15416733/what-is-the-difference-between-dynamic-and-virtual-methods/
* http://pages.cs.wisc.edu/~rkennedy/vmt
