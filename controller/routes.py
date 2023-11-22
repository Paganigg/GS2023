from flask import * 
from .medico_controller import get_medicos, registrar_medico, get_medico_by_id
from .paciente_controller import get_pacientes, registrar_paciente
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
        TODO: Alterar o retorno.
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
        controller.paciente_controller.editar_paciente(paciente)
        return jsonify(paciente)
    

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
        TODO: Alterar o retorno.
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
        TODO: Alterar o retorno.
    """
    if request.method == 'PUT':
        medico = request.get_json()
        controller.medico_controller.editar_medico(medico)
        return jsonify(medico)


@app.route("/medico/<id>", methods=['GET'])
def get_medico(id):
    if request.method == 'GET':
        return jsonify(get_medico_by_id(id))