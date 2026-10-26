# Testes para a Tarefa Gerenciador de Notas
# Rode com: pytest

import pytest

from notas import calcular_media, carregar_dados, salvar_dados, validar_nota


# Tarefa 4: Escrever Testes com pytest

def test_calcular_media_com_notas():
    assert calcular_media([8, 9, 10]) == 9.0


def test_calcular_media_lista_vazia():
    # Complete: a média de uma lista vazia deve ser 0.0
    pass


def test_validar_nota_valida():
    # Complete: validar_nota("7.5") deve retornar 7.5
    pass


def test_validar_nota_texto_invalido():
    with pytest.raises(ValueError):
        validar_nota("dez")


def test_validar_nota_fora_do_intervalo():
    # Complete: use pytest.raises para uma nota maior que 10
    pass


def test_salvar_e_carregar_dados(tmp_path):
    caminho = tmp_path / "notas.json"
    # Complete: salve um dicionário, carregue de volta e compare
    pass
