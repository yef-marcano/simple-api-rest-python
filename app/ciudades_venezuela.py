from flask import Flask,jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost:3306/bdpython'
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False

db = SQLAlchemy(app)
mash = Marshmallow(app)

class Ciudades (db.Model):
    id_estado = db.Column(db.Integer,primary_key=True)
    estado = db.Column(db.String(250))

    def __init__(self,id_estado,estado):
        self.id_estado = id_estado
        self.estado = estado


db.create_all()

class EstadosSchema(mash.Schema):
    class Meta:
        fields = ('id_estado','estado')


#Una sola respuesta
estado_schema = EstadosSchema()

#Varias respuestas
estados_schema = EstadosSchema(many=True)

@app.route('/estados',methods=['GET'])
def get_estados():
    all_estados = Ciudades.query.all()
    result = estados_schema.dump(all_estados)
    return jsonify(result)