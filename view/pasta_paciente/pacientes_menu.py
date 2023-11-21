def criar_paciente(modelo: dict) -> dict:
    novo_paciente = modelo.copy()
    for k,v in novo_paciente.items():
        while type(v) != int and (v == '' or v.isspace()):
            v = input(f"{k.capitalize()}: ").capitalize()
            if v == '':
                print("Campo em branco, digite algo!")

    return novo_paciente