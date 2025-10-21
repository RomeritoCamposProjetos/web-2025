# Avaliação

## Problema

Você é desenvolver da empresa *Sonhos* e foi indicado para realizar atualizações no sistema da empresa. O sistema atualmente conta com o SQLAlchemy como framework para mapeamento objeto-relacional. O sistema também conta com login e cadastro de usuários já implmentados com Flask-Login.

Alguns requisitos importantes já foram implementados como: hash de senhas, cadastro de livros e login, logout e cadastro de usuários. 

A empresa notou que está acontecendo recorrentes pedidos para incrementar funcionalidades da aplicação. Os clientes desajam que os livros tenham mais de um autor e que os usuários (autores) possam ter também mais de um livro.

Para executar a aplicação, basta:

```bash
python app.py
```

Você deve implementar os requisitos abaixo:

## Requisitos

- (25 pontos) Implementar relacionamento N:N entre usuários e livros nos modelos
- (25 pontos) Permitr a associação de mais de um usuário por livro
- (25 pontos) Atualizar dados básicos de livro
- (25 pontos) Operações de banco de dados utilizando sessões SQLAlchemy corretamente, sem erros