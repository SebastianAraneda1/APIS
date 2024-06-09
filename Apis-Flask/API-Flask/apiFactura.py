from flask import Flask, request
from flask_restful import Api, Resource
import requests
from flask_cors import cross_origin
from flask_cors import CORS

app = Flask(__name__)
api = Api(app)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

url_cliente = "http://localhost:22435/api/cliente"

url_producto = "http://localhost:22435/api/producto"

## POST localhost:port/api/boleta 
## > body: json > { id_producto, cantidad, id_cliente }
## new Factura() -> #3ag32g45 --> Factura{ }
class Factura(Resource):
    @cross_origin()
    def post(self):
        # definimos un objeto para la respuesta de la boleta
        objRespuesta = {
            "id_cliente": 0,
            "nombre_cliente": "",
            "direccion_cliente": "",
            "id_producto": 0,
            "cantidad": 0,
            "precio": 0,
            "total_venta": 0,
            "tipo_entrega": 0
        }
        print(objRespuesta)

        # capturamos el json que nos llega
        json = request.get_json()

        print("PASE")
        print(json)
        # generamos una nueva consulta hacia el api de cliente
        cliente_response = requests.get(url_cliente+"/"+ str(json["id_cliente"]))
        producto_response = requests.get(url_producto + "/" + str(json["id_producto"]))

        print("Estado de respuesta cliente: " + str(cliente_response.status_code))
        print("Estado de respuesta producto: " + str(producto_response.status_code))
        print("")

        if(cliente_response.status_code == 200 and producto_response.status_code == 200):
            cliente_json = cliente_response.json()
            producto_json = producto_response.json()
            envio = "Retiro" if json["tipo_entrega"] == "1" else "Despacho"
            cantidad = int(json["cantidad"])

            if(cantidad > int(producto_json["cantidad"])):
                print("STOCK INSUFICIENTE")
                return objRespuesta
            else:

                objRespuesta["id_cliente"] = cliente_json["id"]
                objRespuesta["nombre_cliente"] = cliente_json["nombre"]
                objRespuesta["direccion_cliente"] = cliente_json["direccion"]
                objRespuesta["id_producto"] = producto_json["id"]
                objRespuesta["nombre_producto"] = producto_json["nombre"]
                objRespuesta["cantidad"] = cantidad
                objRespuesta["precio"] = producto_json["precio"]
                objRespuesta["total_venta"] = producto_json["precio"] * cantidad
                objRespuesta["tipo_entrega"] = envio 

                return objRespuesta
    
api.add_resource(Factura, "/api/boleta")

app.run(debug=True, port=5001)