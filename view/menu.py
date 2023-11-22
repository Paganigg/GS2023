import random

def print_menu():
    print('''
    Projeto Global Solution 2023
    
    1 - Registrar um médico
    2 - Editar médico
    3 - Visualizar médicos
    4 - Registrar Paciente
    5 - Editar paciente
    6 - Visualizar pacientes
    0 - Sair
    ''')


def criar_registro(modelo: dict) -> dict:
    novo_registro = modelo.copy()
    for k, v in novo_registro.items():
        while type(v) != int and (v == '' or v.isspace()):
            v = input(f"{k.capitalize()}: ").capitalize()
            novo_registro[k] = v
            
            if v == '':
                print("Campo em branco, digite algo!")

    id = random.randrange(0, 100000)
    novo_registro['id'] = id

    return novo_registro


def editar(modelo: dict) -> dict:
    edicao = input('Digite o id da pessoa que deseja editar: ')
    novo = criar_registro(modelo)
    novo['id'] = edicao

    return novo


def visualizar(lista: list):
    print(lista)
