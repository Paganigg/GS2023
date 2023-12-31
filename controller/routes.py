from flask import * 
from .medico_controller import get_medicos, registrar_medico, get_medico_by_id
from .paciente_controller import get_pacientes, registrar_paciente, get_paciente_by_id
import controller.paciente_controller
import controller.medico_controller

app = Flask(__name__)  


@app.route("/pacientes", methods=['GET']) 
def pacientes():
    """
    Endpoint para carregar a lista de pacientes.

    Retorna:
        Response: Resposta JSON contendo a lista de pacientes.
    """
    if request.method == 'GET':
        return jsonify(get_pacientes())


@app.route("/registrar_paciente", methods=['POST']) 
def registro():
    """
    Endpoint para cadastrar um novo paciente.

    Retorna:
        Response: Resposta JSON que ecoa os dados registrados.
    """
    if request.method == 'POST':
        paciente = request.get_json()
        registrar_paciente(paciente)
        return jsonify(paciente)


@app.route("/editar_paciente", methods=['PUT'])
def edita_paciente():
    """
    Endpoint para edição de um paciente existente.
    
    Retorna:
        Response: Resposta JSON que modifica os dados já registrados
    """
    if request.method == 'PUT':
        paciente = request.get_json()
        status = controller.paciente_controller.editar_paciente(paciente)
        resposta = Response(paciente, mimetype="application/json")
        resposta.status_code = status
        return resposta
    

@app.route("/medicos", methods=['GET'])
def medicos():
    """
    Endpoint para carregar a lista de médicos.

    Retorna:
        Response: Resposta JSON contendo a lista de médicos.
    """
    if request.method == 'GET':
        return jsonify(get_medicos())


@app.route("/registrar_medico", methods=['POST'])
def registro_medico():
    """
    Endpoint para registrar um novo médico.

    Retorna:
        Response: Resposta JSON que ecoa os dados registrados.
    """
    if request.method == 'POST':
        medico = request.get_json()
        registrar_medico(medico)
        return jsonify(medico)
    

@app.route("/editar_medico", methods=['PUT'])
def edita_medico():
    """
    Endpoint para editar um médico já existente.

    Retorna:
        Response: Resposta JSON que ecoa os dados registrados.
    """
    if request.method == 'PUT':
        medico = request.get_json()
        status = controller.medico_controller.editar_medico(medico)
        resposta = Response(medico, mimetype="application/json")
        resposta.status_code = status
        return resposta


@app.route("/medico/<id>", methods=['GET'])
def get_medico(id: int):
    if request.method == 'GET':
        return jsonify(get_medico_by_id(int(id)))


@app.route("/paciente/<id>", methods=['GET'])
def get_paciente(id: int):
    if request.method == 'GET':
        return jsonify(get_paciente_by_id(int(id)))