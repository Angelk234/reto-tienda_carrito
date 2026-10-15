# Cliente del servicio Catálogo (equipo vecino) · Reto de integración
# Contrato del vecino: catalogo.proto · Qué hace y con qué datos probar: servicios/catalogo/README.md
# Antes de correrlo, el servidor del vecino debe estar corriendo (README.md, paso 5).
import grpc

import catalogo_pb2
import catalogo_pb2_grpc

canal = grpc.insecure_channel("localhost:50051")
stub = catalogo_pb2_grpc.CatalogoStub(canal)

print("=== Parte 1 · ObtenerProducto con un dato válido ===")
# TODO: arma la petición con un dato que funcione (tabla "Datos para probar" del README del vecino),
#       llama a stub.ObtenerProducto(...) e imprime los campos de la respuesta.

print("=== Parte 2 · ObtenerProducto con un dato que provoca error ===")
# TODO: llama con un dato que provoque error, dentro de try/except grpc.RpcError,
#       e imprime e.code() y e.details(). El programa NO debe tronar.

print("=== Parte 3 · ListarCategoria (streaming) ===")
# TODO: recorre stub.ListarCategoria(...) con for e imprime cada caja en cuanto llegue.
#       Ponlo también dentro de try/except por si el servidor regresa un error.
