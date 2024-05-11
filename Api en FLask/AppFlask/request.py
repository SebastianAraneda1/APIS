import requests

url = "http://localhost:5000/"

post_response = requests.post(url, json = {"id": "5", "nombre": "Sebastian"})
print(post_response.status_code)

google_response = requests.get(url)
print(google_response.content)

#Realizar una api de un Carrito de compras que a traves de un request pueda consumirse.

#EL CARRITO SERA EL REQUEST Y HAY QUE CONSUMIR EL API DE C#
#El carrito debe pedir el id del producto (que ya traerá el precio y nombre etc.), el id del cliente (tambien trae el nombre y etc.) y la cantidad de los productos
#El total se multiplica por la cantidad de productos