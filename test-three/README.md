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

Nos testes de performance, a cada execução é recomendado reiniciar o serviço do Postgre para não comprometer a resultado das consultas.

```
sudo /etc/init.d/postgresql restart 
```

Para criar os objetos no DB, execute: 
```bash
python3.4 src/main.py --initdb
``` 
> Nota: esse comando demora alguns minutos para executar, ele cria toda a estrura de testes e popula a tabela `users` com 4.194.304 registros.

Para rodar a consulta SQL exigida no teste, execute:
```bash
python3.4 main.py --runquery
``` 

### Resultado

#### Consulta executada

Esse consulta foi a exigida no teste.
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

