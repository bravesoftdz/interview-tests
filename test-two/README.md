A implementação descrita no teste foi possível ser feita da [seguinte forma](https://github.com/johnidm/interview-tests/blob/master/test-two/src/main.py).

Ao acessar o atributo `X` através de uma instância da classe `D`, é invocado a implementação do atributo `X` da classe `A`, pois a implementaçao desse atributo existe somente na classe `A`.

No teste proposto, da forma com entendi, não está exigindo o uso de polimorfismo pois os atributos, `X`, `Y`, `Z`  possuem uma "única forma" implementada nas classes. Veja o "esquema" que eu entendi: 

* Classe `A` possui o atributo `X`.
* Classe `B` possui o atributo `Y` e estende a classe `A`.
* Classe `C` possui o atributo `Z` e estende a classe `A`.
* Classe `D` **não** possui atributos e estende a classe `B` e `C`.

Apesar da clase `D` herdar as classes `B` e `C`, `B` e `C` herdam a clase `A`, somente uma instancia de `A` é criada na herança.

O comando abaixo mostra esse comportamento, execute:

```
python3.4 src/tests.py -d
```

Baseado na execução do algoritmo do arquivo [virtual_table.py](https://github.com/johnidm/interview-tests/blob/master/test-two/src/virtual_table.py), `python3.4 src/virtual_table.py`, cheguei a na conclusão desenhada no diagrama abaixo.

![](imagens/vt.png)

Para acompanhar o comportamento de cada classe, execute:

```
python3.4 src/tests.py -a -b -c -d
```

> Utilizei o método construtor `__init__` apenas para informar quando a classe esta sendo criada.

Referências:
* http://en.wikipedia.org/wiki/Virtual_method_table
* http://stackoverflow.com/questions/4714136/python-how-to-implement-virtual-methods
* http://legacy.python.org/workshops/1998-11/proceedings/papers/lowis/lowis.html
* http://www.johnidouglas.com.br/vinculacao-de-metodos-em-delphi/
* http://stackoverflow.com/questions/15416733/what-is-the-difference-between-dynamic-and-virtual-methods/
* http://pages.cs.wisc.edu/~rkennedy/vmt
