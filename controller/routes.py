from flask import * 
from .medico_controller import get_medicos, registrar_medico
from .paciente_controller import get_pacientes, registrar_paciente

app = Flask(__name__)  


@app.route("/")
def index():
    return "Index Page" 


@app.route("/pacientes", methods=['GET']) 
def pacientes():
    if request.method == 'GET':
        return jsonify(get_pacientes())


@app.route("/registrar_paciente", methods=['POST']) 
def registro():
    if request.method == 'POST':
        paciente = request.get_json()
        registrar_paciente(paciente)
        return jsonify(paciente)


@app.route("/medicos", methods=['GET'])
def medicos():
    if request.method == 'GET':
        return jsonify(get_medicos())


@app.route("/registrar_medico", methods=['POST'])
def registro_medico():
    if request.method == 'POST':
        medico = request.get_json()
        registrar_medico(medico)
        return jsonify(medico)
