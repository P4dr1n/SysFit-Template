# main.py
from aluno import *
from entrada import *
from navegabilidade import *

# variáveis de controle dos dados na memória
id = 1 
""" número do id de autoincremento
"""
alunos = []  
""" lista de dicionários que armazena as abstrações de alunos
"""

while True:
    imprimir_cabecalho()
    exibir_menu()
    opc = ler_inteiro("Opção: ")

    # navegabilidade
    if opc == 1:
        # cadastrar aluno
        aluno = cadastrar_aluno(id)
        alunos.append(aluno)
        id += 1 
        print("Aluno cadastrado com sucesso!")
    elif opc == 2:
        # Imprimir cadastros
        imprimir_alunos(alunos)
    elif opc == 3:
        # Buscar aluno por id
        id_busca = ler_inteiro("Digite o ID do aluno: ")
        aluno_encontrado = next((aluno for aluno in alunos if aluno['id'] == id_busca), None)
        if aluno_encontrado:
            print(f"ID: {aluno_encontrado['id']}, Nome: {aluno_encontrado['nome']}, Peso: {aluno_encontrado['peso']}kg, Altura: {aluno_encontrado['altura']}m, IMC: {aluno_encontrado['imc']:.2f}")
        else:
            print("Aluno não encontrado.")
    elif opc == 4:
        # Filtrar alunos por IMC
        imc_min = ler_real("Digite o IMC mínimo: ")
        imc_max = ler_real("Digite o IMC máximo: ")

        alunos_filtrados = [aluno for aluno in alunos if imc_min <= aluno['imc'] <= imc_max]
        
        if alunos_filtrados:
            print("Alunos filtrados por IMC:")
            imprimir_alunos(alunos_filtrados)
        else:
            print("Nenhum aluno encontrado com o IMC especificado.")
    elif opc == 5:
        # Salvar os dados e pergunta se deseja sair do programa
        print("Dados salvos. Saindo do programa...")
        break
    else:
        print("Opção inválida!")

    limpar_tela()