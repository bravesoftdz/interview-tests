Código fonte utilizado nesse teste está no diretório `/src`

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

Nos testes de performance, a cada execução é recomendado reiniciar o serviço do Postgre para não comprometer o resultado das consultas.

```
sudo /etc/init.d/postgresql restart 
```

Para criar os objetos no DB, execute: 
```bash
python3.4 src/main.py --initdb
``` 
> Nota: esse comando demora alguns minutos para executar, ele cria toda a estrura do DB e popula a tabela `users` com 4.194.304 registros.

Para rodar a consulta SQL exigida no teste, execute:
```bash
python3.4 src/main.py --runquery
``` 

### Resultado

#### Consulta executada

Comando SQL utilizado no teste.
```
EXPLAIN SELECT name, email FROM users WHERE email LIKE '@gmail.com%' GROUP BY name, email
```

#### Índice com melhor desempenho

O índice abaixo permitiu que a consulta fosse executada com um tempo de **6186 ms** com cerca de **4194304** registros.

```
CREATE INDEX idx_email ON users USING btree (email varchar_pattern_ops);
```

O índice que apresentou o melhor resultado utiliza o algoritmo de busca [B-Tree](http://www.postgresql.org/docs/9.2/static/indexes-types.html) com o operador de classe [varchar_pattern_ops](http://www.postgresql.org/docs/9.3/static/indexes-opclass.html) que é indicado para os casos em que o “curinga” em uma busca textual esta no final da texto.

##### Outros índices usados no teste

```
CREATE EXTENSION pg_trgm;
```

###### Índice um

```
CREATE INDEX idx_email ON users USING btree (email)
```

###### Índice dois

```
CREATE INDEX idx_email ON users USING gist (email gist_trgm_ops);
```

###### Índice três
```
CREATE INDEX idx_email ON users USING gin (email gin_trgm_ops);
```

Descartei outras possibilidade de testes por entender que a melhor performace já foi obtida;

