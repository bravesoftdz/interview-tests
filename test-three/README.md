Código fonte utilizado nesse teste está no diretório [/src](https://github.com/johnidm/interview-tests/tree/master/test-three/src)

DB utilizado foi o [Postgresql](http://www.postgresql.org/).

#### Requisitos

Instalação da [libpq](http://www.postgresql.org/docs/9.4/static/libpq.html) e de algumas bibliotecas Python.

```
sudo apt-get install libpq-dev python3-dev
```

Instalação da biblioteca [Psycopg](http://initd.org/psycopg/) utilizada na comunicação com o Postgresql

```
sudo pip install psycopg2
```

Nos testes de performance a cada execução é recomendado reiniciar o serviço do Postgre para não comprometer o resultado das consultas.

```
sudo /etc/init.d/postgresql restart 
```

Para criar os objetos no DB, execute: 
```bash
python3.4 src/main.py --initdb
```
> Nota: esse comando demora alguns minutos para executar, ele cria toda a estrutura do DB e popula a tabela `users` com 4.194.304 registros.


Criando índices no DB:
```
python3.4 src/main.py --createindex "<statement>"
```
> onde **statement** é o comando SQL utilizado para criar o índice.

Para rodar a consulta SQL exigida no teste, execute:
```bash
python3.4 src/main.py --runquery
``` 

### Resultado

#### Consulta executada

Comando SQL utilizado no teste.
```
EXPLAIN ANALYZE SELECT name, email FROM users WHERE email LIKE '@gmail.com%' GROUP BY name, email
```

#### Índice com melhor desempenho

O índice abaixo permitiu que a consulta fosse executada com um tempo de **6186 ms** com cerca de **4194304** registros.

```
CREATE INDEX idx_email ON users USING btree (email varchar_pattern_ops);
```

O índice que apresentou o melhor resultado utiliza o algoritmo de busca [B-Tree](http://www.postgresql.org/docs/9.2/static/indexes-types.html) com o operador de classe [varchar_pattern_ops](http://www.postgresql.org/docs/9.3/static/indexes-opclass.html).

##### Outros índices usados no teste e que também apresentaram bons resultados

```
CREATE EXTENSION pg_trgm;
```

###### Índice um

```
CREATE INDEX idx_email ON users USING gist (email gist_trgm_ops);
```

###### Índice dois

```
CREATE INDEX idx_email ON users USING gin (email gin_trgm_ops);
```

Referencias:
* http://www.johnidouglas.com.br/dicas-para-melhorar-a-performance-em-comandos-sql-parte-1/
* http://stackoverflow.com/questions/1566717/postgresql-like-query-performance-variations
* http://blog.2ndquadrant.com/text-search-strategies-in-postgresql/
* http://www.postgresonline.com/journal/archives/212-PostgreSQL-9.1-Trigrams-teaching-LIKE-and-ILIKE-new-tricks.html/
* http://dba.stackexchange.com/questions/10694/pattern-matching-with-like-similar-to-or-regular-expressions-in-postgresql
