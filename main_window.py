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
            menu.editar(medico_model)
            print("Médico editado")

        case "3":
            medicos = requests.get(f"{API}/medicos").json()
            menu.visualizar(medicos)

        case "4":
            novo_paciente = menu.criar_registro(medico_model)
            requests.post(f"{API}/registrar_paciente", data=json.dumps(novo_paciente), headers=HEADERS)
            print('Paciente cadastrado')

        case "5":
            menu.editar(paciente_model)
            print("Paciente editado")

        case "6":
            pacientes = requests.get(f"{API}/pacientes").json()
            menu.visualizar(pacientes)

        case "0":
            break

        case _:
            print("Digite uma escolha válida")
