from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

clientes = {}

#Resource es par traer todas las configuraciones de Apis pre-hechas
class HelloWorld(Resource):
    #El self es para obtener un metodo
    def get(self, cliente_id):
        return {'cliente': clientes[cliente_id]}
    def put(self, cliente_id):
        clientes[cliente_id] = request.get_json()
    def delete(self, cliente_id):
        clientes.pop(cliente_id);
        
class HelloWorldSinId(Resource):
    def get(self):
        return clientes
    def post(self):
        json = request.get_json()
        clientes[json["id"]] = json
        return json["id"]

#Los parametros te pide algo que sea un Resource, en este caso, HelloWorld, despues te pide insertar la ruta o url.
api.add_resource(HelloWorld, '/<string:cliente_id>')
api.add_resource(HelloWorldSinId, '/')

#Esto es si el archivo se llama main, la aplicación corre con modo debug.
if __name__ == '__main__':
    app.run(debug=True)