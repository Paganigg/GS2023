from repository.medico_repository import get, registrar


def get_medicos():
    return get()


def registrar_medico(medico):
    registrar(medico)
