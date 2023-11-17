import json
from model import paciente

PACIENTES = "pacientes.json"


def get() -> list:
    """
    Obtém a lista de pacientes do arquivo JSON.

    Retorna:
        list: Lista de pacientes.
    """
    try:
        with open(PACIENTES, "r", encoding="utf-8") as arquivo_pacientes: 
            pacientes = json.load(arquivo_pacientes)
            return pacientes
    except FileNotFoundError:
        print("Arquivo não encontrado")
        return []
    except:
        print("Erro desconhecido")
        return []


def registrar(paciente) -> None:
    """
    Registra um novo paciente no arquivo JSON.

    Args:
        paciente (dict): Informações do paciente a serem registradas.

    Retorna:
        None
    """
    pacientes = get()
    pacientes.append(paciente)
    try:
        with open(PACIENTES, "w+", encoding="utf-8") as arquivo_pacientes: 
            json.dump(pacientes, arquivo_pacientes, indent=4)
    except FileNotFoundError:
        print("Arquivo não encontrado")
    except:
        print("Erro desconhecido")


def editar(paciente) -> None:
    """
    Edita as informações de um paciente (TODO).

    Args:
        paciente (dict): Paciente a ter seus registros alterados.
    
    Retorna:
        None
    """
    pass
