# Controle de Insumos
Sistema de controle de insumos desenvolvido em Python como projeto de estudo, com foco em lógica de programação, organização de código, persistência de dados e evolução para desenvolvimento backend.

## Sobre o projeto
O sistema funciona pelo terminal e permite cadastrar, consultar e controlar a quantidade de insumos em estoque.
O projeto está sendo desenvolvido por versões, adicionando novos conceitos e tecnologias conforme avanço nos estudos.
Na versão atual, os dados são armazenados em um arquivo JSON e carregados automaticamente ao iniciar o programa.

## Funcionalidades
- Cadastro de insumos
- Listagem de insumos
- Registro de entrada
- Registro de saída
- Consulta por código
- Verificação de estoque baixo
- Persistência dos dados em JSON
- Carregamento automático dos dados
- Salvamento dos dados após alterações válidas

Cada insumo possui:
- Código
- Nome
- Quantidade
- Unidade de medida
- Estoque mínimo

## Tecnologias
- Python
- JSON
- pathlib
- Git
- GitHub

## Estrutura do projeto
```text
controle-insumos/

    controle_insumos.py
    .gitignore
    README.md
```

O arquivo `insumos.json` é criado durante a execução do programa e não é versionado pelo Git.

## Persistência de dados
Na versão atual, os dados são armazenados em um arquivo JSON. Ao iniciar o programa, os dados existentes são carregados automaticamente. Sempre que ocorre uma alteração válida, como cadastro, entrada ou saída de estoque, os dados são salvos novamente no arquivo, e caso o arquivo ainda não exista ou esteja vazio ou inválido, o programa inicia com uma lista vazia.O caminho do arquivo é definido com `pathlib`, garantindo que o `insumos.json` fique na pasta do projeto.

## Versões
### v1.0.0
Primeira versão funcional do projeto.

Principais funcionalidades:
- Cadastro de insumos
- Listagem de insumos
- Entrada de estoque
- Saída de estoque
- Consulta por código
- Verificação de estoque baixo
- Dados armazenados apenas em memória

### v1.1.0
Adição de persistência de dados e organização do código.

Principais mudanças:
- Organização das funcionalidades em funções
- Criação de função auxiliar para exibição dos insumos
- Persistência dos dados com JSON
- Carregamento automático dos dados
- Salvamento após alterações válidas
- Tratamento de arquivo inexistente
- Tratamento de JSON inválido ou vazio
- Uso de `pathlib` para definir o caminho do arquivo
- Adição do `insumos.json` ao `.gitignore`

## Objetivo
Usar o projeto para aplicar na prática os conceitos estudados e acompanhar minha evolução desde os fundamentos de Python até o desenvolvimento de aplicações backend mais completas.

## Autor
Gustavo José Santos Medeiros