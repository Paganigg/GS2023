import json
from model import medico


def get_medicos() -> list: 
    try:
        with open ("medicos.json","r", enconding = "utf-8") as arquivo_medicos: 
            medicos = json.loads(arquivo_medicos) 
            return medicos
    except FileNotFoundError:
        print ("Arquivo não encontrado")
        return []
    except:
        print ("Erro desconhecido")
        return []


def registrar_medico(medico) -> None:
    pass


def editar_medico(medico) -> None:
    pass