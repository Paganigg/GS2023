import random

def print_menu():
    print('''
    Projeto Global Solution 2023
    
    1 - Registrar um médico
    2 - Editar médico
    3 - Visualizar médicos
    4 - Encontrar médico pelo ID      
    5 - Registrar Paciente
    6 - Editar paciente
    7 - Visualizar pacientes
    8 - Encontrar paciente pelo ID     
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
    id = int(input('Digite o id da pessoa que deseja editar: '))
    novo = criar_registro(modelo)
    novo['id'] = id

    return novo


def visualizar_elemento(dicionario: dict):
    print(f"id = {dicionario['id']}")
    print(f"Nome = {dicionario['nome']}")
    print(f"Email = {dicionario['email']}")


def visualizar_dicionario(dicionario: dict):
    for k,v in dicionario.items():
        print(f'{k} = {v}')


def visualizar(lista: list):
    for e in lista:
        print()
        visualizar_elemento(e)
