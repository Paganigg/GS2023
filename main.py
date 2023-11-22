import requests
import json
from model.medico import medico_model
from model.paciente import paciente_model
from view import menu

API = "http://localhost:5000"
HEADERS = {
    'Content-type':'application/json', 
    'Accept':'application/json'
}

while True:
    menu.print_menu()

    escolha = input('Escolha: ')

    match escolha:
        case "1":
            novo_medico = menu.criar_registro(medico_model)
            requests.post(f"{API}/registrar_medico", data=json.dumps(novo_medico), headers=HEADERS)
            print('Médico cadastrado')

        case "2":
            editar_medico = menu.editar(medico_model)
            response = requests.put(f"{API}/editar_medico", data=json.dumps(editar_medico), headers=HEADERS)

            if response.status_code != 200:
                print("ID inválido")
            else:    
                print("Médico editado")

        case "3":
            medicos = requests.get(f"{API}/medicos").json()
            menu.visualizar(medicos)
            if medicos == []:
                print("Nenhum registro encontrado")

        case "4":
            id = int(input("Digite o ID do médico a ser encontrado: "))
            medico = requests.get(f"{API}/medico/{id}").json()
            menu.visualizar_dicionario(medico)

        case "5":
            novo_paciente = menu.criar_registro(paciente_model)
            requests.post(f"{API}/registrar_paciente", data=json.dumps(novo_paciente), headers=HEADERS)
            print('Paciente cadastrado')

        case "6":
            editar_paciente = menu.editar(paciente_model)
            response = requests.put(f"{API}/editar_paciente", data=json.dumps(editar_paciente), headers=HEADERS)

            if response.status_code != 200:
                print("ID inválido")
            else:
                print("Paciente editado")

        case "7":
            pacientes = requests.get(f"{API}/pacientes").json()
            menu.visualizar(pacientes)
            if pacientes == []:
                print("Nenhum registro encontrado")

        case "8":
            id = int(input("Digite o ID do paciente a ser encontrado: "))
            paciente = requests.get(f"{API}/paciente/{id}").json()
            menu.visualizar_dicionario(paciente)
            
        case "0":
            break

        case _:
            print("Digite uma escolha válida")
    input("Digite qualquer tecla para continuar: ")