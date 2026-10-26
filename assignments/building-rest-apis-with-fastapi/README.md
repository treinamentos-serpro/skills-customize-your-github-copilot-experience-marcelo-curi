# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Construa uma API REST para gerenciar tarefas usando FastAPI. Você praticará a criação de endpoints, validação de dados, códigos de status HTTP e testes de comportamento da API.

## 📝 Tasks

### 🛠️ Create the FastAPI application

#### Descrição
Configure uma aplicação FastAPI e crie os primeiros endpoints para consultar e cadastrar tarefas. Cada tarefa deve ter um identificador, um título e um indicador de conclusão.

#### Requisitos
O programa concluído deve:

- Instalar FastAPI e Uvicorn e iniciar a aplicação com `uvicorn app:app --reload`
- Definir modelos Pydantic para os dados de entrada e de saída de uma tarefa
- Implementar `GET /tasks` para listar tarefas e `POST /tasks` para cadastrar uma tarefa
- Retornar `201 Created` ao cadastrar uma tarefa e documentar pelo menos um exemplo de requisição


### 🛠️ Implement task management endpoints

#### Descrição
Expanda a API para que os clientes possam consultar, atualizar e remover uma tarefa específica pelo identificador.

#### Requisitos
O programa concluído deve:

- Implementar `GET /tasks/{task_id}` para consultar uma tarefa
- Implementar `PUT /tasks/{task_id}` para atualizar o título e o estado de conclusão
- Implementar `DELETE /tasks/{task_id}` e retornar `204 No Content` quando a remoção for concluída
- Retornar `404 Not Found` quando o identificador solicitado não existir


### 🛠️ Validate and test the API

#### Descrição
Adicione regras de validação aos dados recebidos e testes automatizados para verificar os principais comportamentos da API.

#### Requisitos
O programa concluído deve:

- Rejeitar títulos vazios e títulos maiores que 100 caracteres usando validação Pydantic
- Definir o estado de conclusão como `false` quando ele não for informado na criação
- Criar testes que cubram o cadastro, a consulta, a atualização e a remoção de tarefas
- Verificar nos testes os códigos de status para sucesso, dados inválidos e identificadores inexistentes
