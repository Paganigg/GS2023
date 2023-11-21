from model.medico import medico_model
from model.paciente import paciente_model
from view import menu

while True:
    '''
    Projeto Global Solution 2023
    
    1 - Registrar um médico
    2 - Editar médico
    3 - Visualizar médicos
    4 - Registrar Paciente
    5 - Editar paciente
    6 - Visualizar pacientes
    0 - Sair
    
    '''

    escolha = input('Escolha: ')

    match escolha:
        case "1":
            menu.criar_registro(medico_model)
            print('Médico cadastrado')

        case "2":
            menu.editar(medico_model)
            print("Médico editado")

        case "3":
            pass

        case "4":
            menu.criar_registro(paciente_model)
            print("Paciente cadastrado")

        case "5":
            menu.editar(paciente_model)
            print("Paciente editado")

        case "6":
            pass

        case "0":
            break

        case _:
            print("Digite uma escolha válida")