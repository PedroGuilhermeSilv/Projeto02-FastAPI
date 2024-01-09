# Projeto 02 - FastAPI
O prejeto será referente a produtos e catergorias, onde poderemos adicionar , atualizar, deletar e listar produtos.

# Modelagem
![](https://github.com/PedroGuilhermeSilv/Projeto02-FastAPI/blob/main/img/proeto2-models.png)

- Temos duas classes: User e Product. Elas possuem uma relação entre si de 1 para N.
### db/models.py
- Será informado as entidades da nossa aplicação.

# Rotas Category
![](https://github.com/PedroGuilhermeSilv/Projeto02-FastAPI/blob/main/img/projeto2-rotas.png)

# Rotas Products 
![](https://github.com/PedroGuilhermeSilv/Projeto02-FastAPI/blob/main/img/projeto2-rotas2.png)
# TDD
![](https://github.com/PedroGuilhermeSilv/Projeto02-FastAPI/blob/main/img/tdd.png)

## Bibliotecas utilizadas:
- Fastapi
- Uvicorn
- sqlalchemy
- psycopg2-binary
- pytest
- alembic
- pyhon-decouple

## Anotações

### db/base.py
- A variável chamada de Base serve para fazera a conexão das entidades com o orm.

### db/connection.py
- Será ressponsável por fazer a uma sessão no banco de dados.

### Alembic
- O alembic ficará responsável por fazer as migrações para nosso banco de dados, ou seja, para cada alteração de nossas entidades ele irá alterar no banco.
1. Rode o comando `alembic init migrations`. Este comando irá gerar as pastas iniciais para geração das migrações.
2. Altere os seguintes arquivos: migrations/env.py e alembic.ini
3. Remova o valor de sqlalchemy.url do arquivo alembic.ini
4. Faça as seguintes alterações no env.py
```
from app.db.models import Base
from decouple import config as config_decouple
TEST_MODE = config_decouple('TEST_MODE',default=False,cast=bool)
DB_URL=config_decouple('DB_URL_TEST') if TEST_MODE else config_decouple('DB_URL')

config = context.config
config.set_main_option('sqlalchemy.url',DB_URL)


target_metadata = Base.metadata
```

