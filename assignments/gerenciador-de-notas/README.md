# 📘 Atividade: Gerenciador de Notas

## 🎯 Objetivo

Construa um gerenciador de notas escolares que salva os dados em um arquivo JSON, lida com erros sem travar e é verificado por testes automatizados. Você vai praticar arquivos, tratamento de exceções com `try/except` e seus primeiros testes com `pytest`, habilidades essenciais para criar APIs mais adiante!

## 📝 Tarefas

### 🛠️	Cadastrar Alunos e Calcular Médias

#### Descrição
Use o arquivo `notas.py` como ponto de partida. Implemente as funções que adicionam notas a um dicionário de alunos e calculam a média de cada aluno. Essa primeira parte é rápida e prepara a base para o resto da atividade.

#### Requisitos
O programa concluído deve:

- Implementar `adicionar_nota(dados, aluno, nota)`, que adiciona a nota à lista do aluno (criando a lista se o aluno ainda não existir)
- Implementar `calcular_media(notas)`, que retorna a média de uma lista de notas arredondada para 2 casas decimais
- Retornar `0.0` em `calcular_media` quando a lista estiver vazia
- Exibir no menu a média de cada aluno cadastrado

```
Aluno: Ana
Nota: 8.5
Nota adicionada!

--- Médias ---
Ana: 8.50
```


### 🛠️	Salvar e Carregar Dados em JSON

#### Descrição
Hoje os dados somem quando o programa fecha. Use o módulo `json` para salvar as notas em `notas.json` e carregá-las de volta quando o programa abrir.

#### Requisitos
O programa concluído deve:

- Implementar `salvar_dados(dados, caminho)`, que grava o dicionário no arquivo JSON
- Implementar `carregar_dados(caminho)`, que lê o arquivo e retorna o dicionário
- Carregar os dados automaticamente ao iniciar e salvá-los ao escolher "Sair"
- Manter as notas cadastradas depois de fechar e abrir o programa novamente


### 🛠️	Tratar Erros com try/except

#### Descrição
Usuários cometem erros, e um bom programa não trava por causa disso! Use `try/except` para lidar com entradas inválidas e com problemas no arquivo.

#### Requisitos
O programa concluído deve:

- Implementar `validar_nota(texto)`, que converte o texto em `float` e lança `ValueError` se não for um número ou se estiver fora do intervalo de 0 a 10
- Mostrar uma mensagem amigável quando a nota for inválida, sem encerrar o programa
- Fazer `carregar_dados` retornar um dicionário vazio quando `notas.json` não existir (`FileNotFoundError`)
- Fazer `carregar_dados` retornar um dicionário vazio e avisar o usuário quando o arquivo estiver corrompido (`json.JSONDecodeError`)

```
Nota: dez
❌ Nota inválida: digite um número entre 0 e 10.
Nota: 11
❌ Nota inválida: digite um número entre 0 e 10.
```


### 🛠️	Escrever Testes com pytest

#### Descrição
Como saber se suas funções continuam funcionando depois de uma mudança? Com testes automatizados! Complete o arquivo `test_notas.py` e rode os testes com o comando `pytest`.

#### Requisitos
O programa concluído deve:

- Ter pelo menos 2 testes para `calcular_media`, incluindo o caso da lista vazia
- Ter pelo menos 3 testes para `validar_nota`, incluindo uma nota válida, um texto que não é número e uma nota fora do intervalo (use `pytest.raises`)
- Ter 1 teste que salva e carrega dados de um arquivo temporário (use o fixture `tmp_path`) e confere que os dados são iguais
- Passar em todos os testes ao rodar `pytest`

```
$ pytest
======== 6 passed in 0.02s ========
```
