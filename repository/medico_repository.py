import json

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


def get_by_id(id: int) -> dict:
    medicos = get()

    for i in medicos:
        if i["id"] == id:
            return i
    return {"Erro": "ID não encontrado"}
    

def registrar(medico: dict) -> None:
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


def editar(medico: dict) -> int:
    """
    Edita as informações de um médico.

    Args:
        medico (dict): Médico a ter seus registros alterados.

    Retorna:
        int
    """
    id = medico["id"]
    medicos = get()

    medico_existe = False
    for i in medicos:
        if i["id"] == id:
            n_medico = medico.copy()
            indice = medicos.index(i)
            medicos[indice] = n_medico
            medico_existe = True
            break

    if not medico_existe:
        return 400
    
    try:
        with open(MEDICOS, "w+", encoding="utf-8") as arquivo_medicos: 
            json.dump(medicos, arquivo_medicos, indent=4)
    except FileNotFoundError:
        print("Arquivo não encontrado")
    except:
        print("Erro desconhecido")

    return 200

