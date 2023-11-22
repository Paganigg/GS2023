from repository.paciente_repository import get, registrar, editar, get_by_id
from .validator import validar_keys
from model.paciente import paciente_model

def get_pacientes() -> list:
    """
    Obtém a lista de pacientes do repository.

    Retorna:
        list: Lista de pacientes.
    """
    return get()


def get_paciente_by_id(id: int) -> dict:
    return get_by_id(id)


def registrar_paciente(paciente: dict) -> None:
    """
    Cadastra um novo paciente no repository.

    Args:
        paciente (dict): Informações do paciente a serem cadastradas.

    Retorna:
        None
    """
    registrar(paciente)


def editar_paciente(paciente: dict) -> bool:
    """
    Edita um paciente no repository.

    Args:
        paciente (dict): Informações do paciente a serem editadas.
    
    Retorna:
        bool
    """
    if not validar_keys(paciente, paciente_model):
        return False
    
    return editar(paciente)
     
    

