# Camalheia

Aplicação web em Flask para gestão de um catálogo de cidades — com fotografias, pesquisa, autenticação de utilizadores e permissões por nível de acesso.

> "Um homem precisa viajar. Por sua conta, não por meio de histórias, imagens, livros ou TV." — Amyr Klink

## Funcionalidades

- **Listagem e detalhe de cidades**, incluindo galeria de fotografias
- **Pesquisa** de cidades por nome, país ou descrição (com destaque do termo pesquisado)
- **Autenticação** de utilizadores (login/logout) com passwords em hash
- **Permissões por nível de utilizador**:
  - Utilizador autenticado: adicionar e atualizar cidades
  - Utilizador de nível 1 (admin): também eliminar cidades e gerir fotografias
- **CRUD de cidades**: adicionar, atualizar, eliminar
- **Gestão de fotografias**: upload e eliminação, associadas a uma cidade

## Arquitetura

O projeto segue uma arquitetura em três camadas:

```
app/
├── __init__.py
├── db_config.py                # ligação à base de dados (pymysql)
├── routes/                     # camada de rotas (Blueprints Flask)
│   ├── rt_autenticacao.py
│   └── rt_cidades.py
├── services/                   # camada de lógica de negócio
│   ├── srv_autenticacao.py
│   ├── srv_cidades.py
│   ├── srv_fotos.py
│   └── srv_utilizadores.py
├── models/                     # camada de acesso a dados (queries SQL)
│   ├── rep_autenticacao.py
│   ├── rep_cidades.py
│   ├── rep_fotos.py
│   └── rep_utilizadores.py
├── utils/
│   └── decorators.py           # login_required, login_nivel_1_required
├── static/
│   ├── css/, js/, img/cidades/
└── templates/                  # templates Jinja2
    ├── base.html
    ├── home.html
    ├── detalhes.html
    ├── adicionar.html
    ├── atualizar_1.html
    ├── atualizar_2.html
    ├── eliminar.html
    ├── pesquisa.html
    └── ad_foto.html
```

**Fluxo típico de um pedido:** `rota (rt_*)` → `serviço (srv_*)` → `repositório (rep_*)` → base de dados.

## Modelo de dados

### `utilizadores`
| Campo | Descrição |
|---|---|
| `id_u` | Identificador |
| `nome_u` | Nome de utilizador |
| `ppass_u` | Password (hash, `werkzeug.security`) |
| `nivel_u` | Nível de permissões (`1` = administrador) |

### `cidades`
| Campo | Descrição |
|---|---|
| `id_c` | Identificador |
| `nome_c` | Nome da cidade |
| `dataf_c` | Ano de fundação (negativo = a.C.) |
| `pais_c` | País |
| `habitantes_c` | Número de habitantes |
| `desc_c` | Descrição |

### `fotos`
| Campo | Descrição |
|---|---|
| `id_f` | Identificador |
| `img_f` | Nome do ficheiro de imagem |
| `cidade_f` | Cidade associada (FK para `cidades.id_c`) |
| `desc_f` | Descrição da fotografia |

## Rotas principais

| Método | Rota | Descrição | Acesso |
|---|---|---|---|
| GET | `/` | Página inicial (lista de cidades) | Público |
| GET | `/detalhes/<id>` | Detalhe de uma cidade | Público |
| POST | `/pesquisa` | Pesquisa de cidades | Público |
| GET/POST | `/adicionar` | Adicionar cidade | Autenticado |
| GET | `/listar` | Lista de cidades para atualizar | Autenticado |
| GET/POST | `/atualizar/<id>` | Atualizar cidade | Autenticado |
| GET | `/eliminar` | Lista de cidades para eliminar | Nível 1 |
| GET | `/eliminar_2/<id>` | Eliminar cidade | Nível 1 |
| GET/POST | `/adicionar_foto` | Adicionar fotografia | Nível 1 |
| GET | `/eliminar_foto/<id>` | Eliminar fotografia | Nível 1 |
| POST | `/autenticacao/login` | Login | Público |
| GET | `/autenticacao/logout` | Logout | Público |

## Tecnologias

- **Flask** — framework web e sistema de Blueprints
- **PyMySQL** — ligação à base de dados MySQL
- **Werkzeug Security** — hashing de passwords
- **itsdangerous** — geração de tokens seguros
- **Jinja2** — motor de templates

## Instalação

1. Clonar o repositório e criar um ambiente virtual:
   ```bash
   python -m venv venv
   source venv/bin/activate   # Windows: venv\Scripts\activate
   ```

2. Instalar dependências:
   ```bash
   pip install flask pymysql werkzeug itsdangerous
   ```

3. Configurar a ligação à base de dados em `app/db_config.py` (host, utilizador, password, nome da base de dados) e criar as tabelas `utilizadores`, `cidades` e `fotos`.

4. Criar a pasta de upload de imagens, se ainda não existir:
   ```bash
   mkdir -p app/static/img/cidades
   ```

5. Executar a aplicação:
   ```bash
   flask --app app run --debug
   ```

## Notas

- As passwords são armazenadas com hash (`generate_password_hash` / `check_password_hash` do Werkzeug); nunca em texto simples.
- O upload de fotografias grava o ficheiro em `app/static/img/cidades` com um nome único baseado em timestamp, e regista o registo correspondente na tabela `fotos`.
- A pesquisa de cidades destaca o termo pesquisado a negrito (`<strong>`) na descrição apresentada.
