from flask import * 
app = Flask(__name__)  


@app.route("/")
def index():
    return "Index Page" 


@app.route("/pacientes", methods=['GET']) 
def pacientes():
    pass


@app.route("/registro", methods=['POST']) 
def registro():
    request.method == 'POST'
    

@app.route("/pacientes/<id>",methods=['PUT'])
def editar():
    pass



if __name__ == "__main__":
    app.run(debug=True)
    app.run(host='0.0.0.0')
