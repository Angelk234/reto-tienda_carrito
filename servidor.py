# Servidor del servicio Carrito · Reto de integración · Unidad II
# Contrato: carrito.proto · Puerto: 50057
# Antes de correrlo: bash compilar.sh
import time
import grpc
from concurrent import futures

import carrito_pb2
import carrito_pb2_grpc

# Datos de ejemplo (no hace falta base de datos)
PRECIOS = {"P001": 1299900, "P002": 29900, "P003": 89900, "P004": 119900, "P005": 69900, "P006": 329900}
CARRITOS = {
    "ana": [("P001", 1), ("P002", 1)],
    "luis": [("P003", 1), ("P005", 2)],
}


class CarritoServicio(carrito_pb2_grpc.CarritoServicer):

    def TotalCarrito(self, request, context):
        if request.usuario not in CARRITOS :
            context.abort(grpc.StatusCode.NOT_FOUND, "El usuario no tiene carrito")

        articulos =  CARRITOS[request.usuario]
        total = sum(
            PRECIOS[clave] * cantidad
            for clave, cantidad in articulos
        )
        cantidad_articulos = sum(
            cantidad for clave, cantidad in articulos
        )
        return carrito_pb2.Total(
            usuario=request.usuario,
            total_centavos=total,
            articulos=cantidad_articulos
        )

    def VerArticulos(self, request, context):
        if request.usuario not in CARRITOS :
            context.abort(grpc.StatusCode.NOT_FOUND, "El usuario no tiene carrito")
        for clave, cantidad in CARRITOS [request.usuario]:
            time.sleep(0.5)

            yield carrito_pb2.Articulo(
                clave = clave,
                cantidad = cantidad,
                subtotal_centavos= PRECIOS[clave] * cantidad
            )



servidor = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
carrito_pb2_grpc.add_CarritoServicer_to_server(CarritoServicio(), servidor)
servidor.add_insecure_port("[::]:50057")
servidor.start()
print("Servidor de Carrito escuchando en el puerto 50057...")
servidor.wait_for_termination()
