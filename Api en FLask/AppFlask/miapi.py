from flask import Flask, request

app = Flask(__name__)

lista = ["Lista de Clientes"]

@app.route("/clientes")
def getClientes():
    return lista

@app.get("/cliente/<int:id>")
def getCliente(id):
    return lista.index(id)

@app.post("/cliente")
def postCliente():
    json = request.get_json()

    cliente = {
        "id": json["id"],
        "nombre": json["nombre"],
        "rut": json["rut"],
        "direccion": json["direccion"]
    }
    print(cliente)

    lista.append(cliente)
    return "Cliente agregado con éxito"

@app.put("/cliente/<int:id>")
def putCliente(id):
    json = request.get_json()

    cliente = {
        "id": json["id"],
        "nombre": json["nombre"],
        "rut": json["rut"],
        "direccion": json["direccion"]
    }
    lista.pop(id)
    lista.append(cliente)
    return "Cliente actualizado!"

@app.delete("/cliente/<int:id>")
def deleteCliente(id):
    lista.pop(id)
    return "Cliente borrado con éxito"

#INSERTAR CLIENTES POR URL
#@app.route("/cliente/<nombre>/<id>", methods=['POST'])
#def postCliente(nombre, id):

#    clienteNuevo = f"{nombre}, {id}\n"

#    lista.append(clienteNuevo)

#    return "Cliente agregado con éxito"
