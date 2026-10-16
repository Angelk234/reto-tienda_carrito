# Cliente del servicio Catálogo (equipo vecino) · Reto de integración
# Contrato del vecino: catalogo.proto · Qué hace y con qué datos probar: servicios/catalogo/README.md
# Antes de correrlo, el servidor del vecino debe estar corriendo (README.md, paso 5).
import grpc
import sys
import os

ruta_vecino = os.path.abspath('../vecino/reto-tienda')
sys.path.append(ruta_vecino)

# 2. Importa los módulos directamente por su nombre, sin la ruta ni el ".py"
import catalogo_pb2
import catalogo_pb2_grpc

canal = grpc.insecure_channel("localhost:50051")
stub = catalogo_pb2_grpc.CatalogoStub(canal)

print("=== Parte 1 · ObtenerProducto con un dato válido ===")
# TODO: arma la petición con un dato que funcione (tabla "Datos para probar" del README del vecino),
#       llama a stub.ObtenerProducto(...) e imprime los campos de la respuesta.
try:
    peticion=catalogo_pb2.ProductoRequest(clave = "P001")
    respuesta= stub.ObtenerProducto(peticion)
    print(f"¡Producto encontrado!")
    print(f"  - Clave: {respuesta.clave}")
    print(f"  - Nombre: {respuesta.nombre}")
    print(f"  - Precio (centavos): {respuesta.precio_centavos}")
    print(f"  - Categoría: {respuesta.categoria}")
except grpc.RpcError as e:
    print(f"Error inesperado: {e.code()} - {e.details()}")

print("=== Parte 2 · ObtenerProducto con un dato que provoca error ===")
# TODO: llama con un dato que provoque error, dentro de try/except grpc.RpcError,
#       e imprime e.code() y e.details(). El programa NO debe tronar.
try:
    # Usamos una clave que no exista para forzar un error gRPC
    peticion_error = catalogo_pb2.ProductoRequest(clave="CLAVE_INEXISTENTE")
    stub.ObtenerProducto(peticion_error)
except grpc.RpcError as e:
    print(f"Código de error: {e.code()}, {e.details}")

print("=== Parte 3 · ListarCategoria (streaming) ===")
# TODO: recorre stub.ListarCategoria(...) con for e imprime cada caja en cuanto llegue.
#       Ponlo también dentro de try/except por si el servidor regresa un error.
try:
    peticion_cat = catalogo_pb2.CategoriaRequest(categoria="bebidas")
    print("Recibiendo productos de la categoría...")
    for producto in stub.ListarCategoria(peticion_cat):
        print(f" -> [{producto.clave}] {producto.nombre} | ${producto.precio_centavos} centavos")
except grpc.RpcError as e:
    print(f"Error en el streaming: {e.code()} - {e.details()}")