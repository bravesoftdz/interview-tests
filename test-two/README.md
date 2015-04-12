A implementação descrita no teste é possível, [exemplo de implementação](https://github.com/johnidm/interview-tests/blob/master/test-two/src/main.py), ao acessar o atributo `X` através de uma instancia da classe `D` é invocado a implementação do atributo `X` da classe `A`.

No teste proposto, da forma com entendi, de certa forma não está exigindo o uso de polimorfismo pois os atributos possuem uma única forma em cada classe.

Como eu etendi o problema proposto:

* Classe `A` possui o atributo `X`.
* Classe `B` possui o atributo `Y` e estende a classe `A`.
* Classe `C` possui o atributo `Z` e estende a classe `A`.
* Classe `D` **não** possui atributos e estende a classe `B` e `C`.

Para rodas os testes e acompanhas o comportamento de cada classe execute:
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
