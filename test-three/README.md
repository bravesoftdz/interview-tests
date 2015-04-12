Código fonte utilizado está no diretório `/src`

O DB utilizado foi o Postgresql.

#### Requisitos

Instalação da [libpq](http://www.postgresql.org/docs/9.4/static/libpq.html) e das bibliotecas Python.

```
sudo apt-get install libpq-dev python3-dev
```

Biblioteca [Psycopg](http://initd.org/psycopg/) utilizada na comunicação com o Postgresql

```
sudo pip install psycopg2
```

Nos testes de performance é recomendado reiniciar o serviço do Postgre para evitar que os dados fiquem em cache e comprometam a contagem de tempo.

```
sudo /etc/init.d/postgresql restart 
```

Para criar os objetos no DB:
```bash
python3.4 main.py --initdb
``` 

Para rodar a query no DB:
```bash
python3.4 main.py --runquery
``` 


### Resultado

#### Consulta executada

```
SELECT email FROM users WHERE email LIKE '@gmail.com%' GROUP BY email
```

#### Índice com melhor desempenho

O índice abaixo executou a consulta eentre **20 ms** a **60 ms** com cerca de **4194304** registros.

```
CREATE INDEX idx_email ON users USING btree (email varchar_pattern_ops);
```

O índice que apresentou o melhor resultado utiliza o algoritmo de busca B-Tree com a extenção `varchar_pattern_ops` melhor indicado para os casos em que o “curinga” da busca textual fica no final da texto.

##### Outros índices usados no teste

CREATE EXTENSION pg_trgm;

###### Índice um

3110 ms com 4194304 registros 
```
CREATE INDEX idx_email ON users USING btree (email ASC)
```

###### Índice dois

26228 ms com 4194304 registros 
```
CREATE INDEX idx_email ON users USING gist (email gist_trgm_ops);
```

12308 ms com 4194304 registros 
###### Índice três
CREATE INDEX idx_email ON users USING gin (email gin_trgm_ops);

Descartei outras possibilidade de testes por entender que a melhor performace já foi obtida;

