def validar_keys(json_validar: dict, model: dict) -> bool:
    if json_validar.keys() != model.keys():
        print("Erro")
        return False
    return True