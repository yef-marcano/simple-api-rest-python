from flask import Flask,jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app = Flask(__name__)
#root = usuario : pass = empy : ruta y puerto / base de datos
#doc = docs.sqlalchemy.org/en/14/dialects/mysql.html
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost:3306/bdpython'
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False

db = SQLAlchemy(app)
mash = Marshmallow(app)

#clase y modelo que contiene los datos internos de la base para la creacion de una tabla con sus datos y tipos de datos
class Categoria (db.Model):
    cat_id = db.Column(db.Integer,primary_key=True)
    cat_nombre = db.Column(db.String(100))
    cat_descripcion = db.Column(db.String(100))

    def __init__(self,cat_nombre,cat_descripcion):
        self.cat_nombre = cat_nombre
        self.cat_descripcion = cat_descripcion

#crea todas las tablas declaradas
db.create_all()


#esquema 
class CategoriaSchema(mash.Schema):
    class Meta:
        fields = ('cat_id','cat_nombre','cat_descripcion')

#Una sola respuesta
categoria_schema = CategoriaSchema()

#Varias respuestas
categorias_schema = CategoriaSchema(many=True)

@app.route('/categoria',methods=['GET'])
def get_categoria():
    all_categorias = Categoria.query.all()
    result = categorias_schema.dump(all_categorias)
    return jsonify(result)


@app.route('/',methods=['GET'])

#mensaje de bienvenida
def index():
    return jsonify({'Mensaje':'Hola, Bienvenido a la API'})

if __name__ =="__main__":
    app.run(debug=True)
