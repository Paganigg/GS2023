def criar_registro(modelo: dict) -> dict:
    novo_registro = modelo.copy()
    for k,v in novo_registro.items():
        while type(v) != int and (v == '' or v.isspace()):
            v = input(f"{k.capitalize()}: ").capitalize()
            if v == '':
                print("Campo em branco, digite algo!")

    return novo_registro



