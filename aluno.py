# aluno.py
from entrada import *

def cadastrar_aluno(id):
    """
    Cadastra um aluno e retorna um dicionário com os dados do aluno.

    Parâmetros:
      - id: ID do aluno a ser cadastrado.

    Retorno:
      - Dicionário com os dados do aluno.
    """
    nome = input("Nome do aluno: ")
    peso = ler_real("Peso (kg): ", pos=True)
    altura = ler_real("Altura (m): ", pos=True)
    
    imc = peso / (altura ** 2)

    aluno = {
        'id': id,
        'nome': nome,
        'peso': peso,
        'altura': altura,
        'imc': imc
    }
    
    return aluno

def imprimir_alunos(alunos):
    """
    Imprime todos os alunos cadastrados.

    Parâmetros:
      - alunos: Lista de dicionários com os dados dos alunos.
    """
    if not alunos:
        print("Nenhum aluno cadastrado.")
        return

    for aluno in alunos:
        print(f"ID: {aluno['id']}, Nome: {aluno['nome']}, Peso: {aluno['peso']}kg, Altura: {aluno['altura']}m, IMC: {aluno['imc']:.2f}")