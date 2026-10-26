# Código Inicial para a Tarefa Gerenciador de Notas

import json

ARQUIVO_DADOS = "notas.json"


# Tarefa 1: Cadastrar Alunos e Calcular Médias

def adicionar_nota(dados, aluno, nota):
    """Adiciona a nota à lista de notas do aluno no dicionário `dados`."""
    pass


def calcular_media(notas):
    """Retorna a média da lista de notas (2 casas decimais) ou 0.0 se estiver vazia."""
    pass


# Tarefa 2: Salvar e Carregar Dados em JSON
# Tarefa 3: Trate FileNotFoundError e json.JSONDecodeError em carregar_dados

def salvar_dados(dados, caminho=ARQUIVO_DADOS):
    """Grava o dicionário `dados` no arquivo JSON indicado."""
    pass


def carregar_dados(caminho=ARQUIVO_DADOS):
    """Lê o arquivo JSON e retorna o dicionário de notas."""
    pass


# Tarefa 3: Tratar Erros com try/except

def validar_nota(texto):
    """Converte o texto em float e lança ValueError se for inválido ou fora de 0 a 10."""
    pass


def menu():
    dados = carregar_dados()

    while True:
        print("\n1 - Adicionar nota")
        print("2 - Ver médias")
        print("3 - Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            aluno = input("Aluno: ")
            texto = input("Nota: ")
            # Use validar_nota e try/except para tratar notas inválidas
            pass
        elif opcao == "2":
            print("\n--- Médias ---")
            # Mostre a média de cada aluno usando calcular_media
            pass
        elif opcao == "3":
            salvar_dados(dados)
            print("Dados salvos. Até logo!")
            break
        else:
            print("Opção inválida, tente novamente.")


if __name__ == "__main__":
    menu()
