from repository.paciente_repository import get, registrar, editar
from .validator import validar_keys


def get_pacientes() -> list:
    """
    Obtém a lista de pacientes do repository.

    Retorna:
        list: Lista de pacientes.
    """
    return get()


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
    if not validar_keys:
        return False
    
    return editar(paciente)
     
    

