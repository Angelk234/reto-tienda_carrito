# Script para probar el servicio Carrito (puerto 50057) con el usuario 'ana'
import grpc

import carrito_pb2
import carrito_pb2_grpc

def probar_ana():
    # Conexión al servidor local de Carrito
    canal = grpc.insecure_channel("localhost:50057")
    stub = carrito_pb2_grpc.CarritoStub(canal)

    print("=== Probando TotalCarrito para 'ana' ===")
    try:
        peticion = carrito_pb2.CarritoRequest(usuario="ana")
        respuesta = stub.TotalCarrito(peticion)
        
        print(f"Usuario: {respuesta.usuario}")
        print(f"Total centavos: {respuesta.total_centavos} (${respuesta.total_centavos / 100:.2f} MXN)")
        print(f"Cantidad de artículos: {respuesta.articulos}")
        print(f"Envío gratis: {respuesta.envio_gratis}")
        
    except grpc.RpcError as e:
        print(f"Error al llamar a TotalCarrito [{e.code()}]: {e.details()}")

    print("\n=== Probando VerArticulos (streaming) para 'ana' ===")
    try:
        peticion = carrito_pb2.CarritoRequest(usuario="ana")
        stream_articulos = stub.VerArticulos(peticion)
        
        for articulo in stream_articulos:
            print(f"  -> Clave: {articulo.clave} | Cantidad: {articulo.cantidad} | Subtotal: ${articulo.subtotal_centavos / 100:.2f}")
    except grpc.RpcError as e:
        print(f"Error en streaming [{e.code()}]: {e.details()}")

if __name__ == "__main__":
    probar_ana()