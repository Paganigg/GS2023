import json

PACIENTES = "pacientes.json"


def get() -> list:
    """
    Obtém a lista de pacientes do arquivo JSON.

    Retorna:
        list: Lista de pacientes.
    """
    try:
        with open(PACIENTES, "r", encoding="utf-8") as arquivo_pacientes: 
            pacientes = json.load(arquivo_pacientes)
            return pacientes
    except FileNotFoundError:
        print("Arquivo não encontrado")
        return []
    except:
        print("Erro desconhecido")
        return []


def get_by_id(id: int) -> dict:
    pacientes = get()
    for i in pacientes:
        if i["id"] == id:
            return i
    return {"Erro": "ID não encontrado"}


def registrar(paciente: dict) -> None:
    """
    Registra um novo paciente no arquivo JSON.

    Args:
        paciente (dict): Informações do paciente a serem registradas.

    Retorna:
        None
    """
    pacientes = get()
    pacientes.append(paciente)
    
    try:
        with open(PACIENTES, "w+", encoding="utf-8") as arquivo_pacientes: 
            json.dump(pacientes, arquivo_pacientes, indent=4)
    except FileNotFoundError:
        print("Arquivo não encontrado")
    except:
        print("Erro desconhecido")


def editar(paciente: dict) -> int:
    """
    Edita as informações de um paciente.

    Args:
        paciente (dict): Paciente a ter seus registros alterados.
    
    Retorna:
        int
    """
    id = paciente["id"]
    pacientes = get()

    paciente_existe = False
    for i in pacientes:
        if i["id"] == id:
            paciente_editado = paciente.copy()
            indice =  pacientes.index(i)  
            pacientes[indice] = paciente_editado
            paciente_existe = True
            break

    if not paciente_existe:
        return 400

    try:
        with open(PACIENTES, "w+", encoding="utf-8") as arquivo_pacientes: 
            json.dump(pacientes, arquivo_pacientes, indent=4)
    except FileNotFoundError:
        print("Arquivo não encontrado")
    except:
        print("Erro desconhecido")

    return 200


    
    
    
    
    


