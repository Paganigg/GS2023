import json
from model import medico
MEDICOS = "repository\medicos.json"


def get() -> list: 
    try:
        with open (MEDICOS,"r", encoding = "utf-8") as arquivo_medicos: 
            medicos = json.load(arquivo_medicos)
            return medicos
    except FileNotFoundError:
        print ("Arquivo não encontrado")
        return []
    except:
        print ("Erro desconhecido")
        return []


def registrar(medico) -> None:
    medicos = get()
    medicos.append(medico)
    try:
        with open (MEDICOS,"w+", encoding = "utf-8") as arquivo_medicos: 
            json.dump(medicos, arquivo_medicos, indent=4)
    except FileNotFoundError:
        print ("Arquivo não encontrado")
    except:
        print ("Erro desconhecido")


def editar(medico) -> None:
    pass