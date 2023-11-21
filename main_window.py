from model.medico import medico_model
from model.paciente import paciente_model
from view.pasta_medico import medicos_menu

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
            medicos_menu.criar_registro(medico_model)

        case "2":
            pass

        case "3":
            pass

        case "4":
            medicos_menu.criar_registro(paciente_model)

        case "5":
            pass

        case "6":
            pass

        case "0":
            break

        case _:
            print("Digite uma escolha válida")