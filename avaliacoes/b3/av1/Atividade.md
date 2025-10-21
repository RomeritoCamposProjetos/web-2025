# Avaliação

## Problema

Você é desenvolver da emprasa *Sonhos* e foi eleito como lider de um projeto. A tarefa do projeto é incluir o SQLAlchemy como framework ORM oficial do produto da empresa. Atualmente, eles usam a versão básica do Sqlite3.

Seu papel é incluir o sqlalchemy, configurar o banco (MySQL ou SQLite3), incluir sessões e definir um modelo `User` que seja um adequado ao SQLAlchemy.

O projeto está funcional e realiza três operações básicas: cadastro, *login* e *logout* de usuários.

Para executar a aplicação, basta:

```bash
python app.py
```


## Requisitos

- (25 pontos) Configuração correta do SQLAlchemy 	
- (25 pontos) Modelo User implementado e funcionalcom base no SQLAlchemy
- (25 pontos) Rotas `/register` e `/login` adaptadas 	
- (25 pontos) Sessões do banco funcionando sem erros