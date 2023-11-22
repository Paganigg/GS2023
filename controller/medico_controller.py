from repository.medico_repository import get, registrar, editar, get_by_id
from .validator import validar_keys
from model.medico import medico_model

def get_medicos() -> list:
    """
    Obtém a lista de médicos do repository.

    Retorna:
        list: Lista de médicos.
    """
    return get()


def get_medico_by_id(id: int) -> dict:
    return get_by_id(id)


def registrar_medico(medico: dict) -> None:
    """
    Registra um novo médico no repository.

    Args:
        medico (dict): Informações do médico a serem registradas.

    Retorna:
        None
    """
    registrar(medico)


def editar_medico(medico: dict) -> int:
    """
    Edita um médico no repository.

    Args:
        medico (dict): Informações do médico a serem editadas.
    
    Retorna:
        int
    """
    if not validar_keys(medico, medico_model):
        return 400
    
    return editar(medico)