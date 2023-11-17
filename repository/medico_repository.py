import json
from model import medico

MEDICOS = "medicos.json"


def get() -> list:
    """
    Obtém a lista de médicos do arquivo JSON.

    Retorna:
        list: Lista de médicos.
    """
    try:
        with open(MEDICOS, "r", encoding="utf-8") as arquivo_medicos: 
            medicos = json.load(arquivo_medicos)
            return medicos
    except FileNotFoundError:
        print("Arquivo não encontrado")
        return []
    except:
        print("Erro desconhecido")
        return []


def registrar(medico) -> None:
    """
    Registra um novo médico no arquivo JSON.

    Args:
        medico (dict): Informações do médico a serem registradas.

    Retorna:
        None
    """
    medicos = get()
    medicos.append(medico)
    try:
        with open(MEDICOS, "w+", encoding="utf-8") as arquivo_medicos: 
            json.dump(medicos, arquivo_medicos, indent=4)
    except FileNotFoundError:
        print("Arquivo não encontrado")
    except:
        print("Erro desconhecido")


def editar(medico) -> None:
    """
    Edita as informações de um médico (TODO).

    Args:
        medico (dict): Médico a ter seus registros alterados.

    Retorna:
        None
    """
    pass
