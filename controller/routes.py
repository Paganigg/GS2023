from flask import * 
from .medico_controller import get_medicos, registrar_medico
app = Flask(__name__)  


@app.route("/")
def index():
    return "Index Page" 


@app.route("/pacientes", methods=['GET']) 
def pacientes():
    pass


@app.route("/registro_paciente", methods=['POST']) 
def registro():
    request.method == 'POST'

    
@app.route("/registro_medico", methods=['POST'])
def registro_medico():
    if request.method == 'POST':
        medico = request.get_json()
        registrar_medico(medico)
        return jsonify(medico)


@app.route("/pacientes/<id>",methods=['PUT'])
def editar():
    pass


@app.route("/medicos",methods=['GET'])
def medicos():
    if request.method == 'GET':
        return jsonify(get_medicos())

