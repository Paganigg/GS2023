from repository.paciente_repository import get, registrar


def get_pacientes():
    return get()


def registrar_paciente(paciente):
    registrar(paciente)
