def validar_keys(json_validar: dict, model: dict) -> bool:
    """
    Função que valida os campos do JSON.
    
    Args:
        json_validar (dict): Dicionário a ser validado. 
        model (dict): DTO que representa o modelo JSON a ser seguido.

    Retorno:
        bool
    """
    if json_validar.keys() != model.keys():
        print("Erro")
        return False
    return True
