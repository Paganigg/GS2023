from repository.medico_repository import get, registrar


def get_medicos() -> list:
    """
    Obtém a lista de médicos do repository.

    Retorna:
        list: Lista de médicos.
    """
    return get()


def registrar_medico(medico: dict) -> None:
    """
    Registra um novo médico no repository.

    Args:
        medico (dict): Informações do médico a serem registradas.

    Retorna:
        None
    """
    registrar(medico)
