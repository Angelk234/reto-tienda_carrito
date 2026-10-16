# Nuestro equipo

- **Nuestro servicio:** Carrito · puerto 50057 · contrato `carrito.proto`
- **Servicio que consumimos (vecino):** Catálogo · puerto 50051 · contrato `catalogo.proto`
- **Repositorio del equipo vecino:** ([pega aquí la URL](https://github.com/Elias735/reto-tienda))

| Integrante | Matrícula | Rol |
|---|---|---|
|alex santos gutierrez | 20205341 | Servidor |
|luis fernando aviña martinez | 20205295| Cliente |
|jesus angel aguilar vazquez |20204845 | Integración (README, issues y prueba cruzada) |

## Prueba cruzada

Corran `python cliente_vecino.py` contra el servidor **real** del equipo vecino (el que clonaron en `../vecino`)
y peguen aquí todo lo que imprimió:

```
=== Parte 1 · ObtenerProducto con un dato válido ===
¡Producto encontrado!
  - Clave: P001
  - Nombre: Laptop 14 pulgadas
  - Precio (centavos): 1299900
  - Categoría: computo
=== Parte 2 · ObtenerProducto con un dato que provoca error ===
Código de error: StatusCode.NOT_FOUND, <bound method _InactiveRpcError.details of <_InactiveRpcError of RPC that terminated with:
        status = StatusCode.NOT_FOUND
        details = "No existe el producto CLAVE_INEXISTENTE"
        debug_error_string = "NOT_FOUND:No existe el producto CLAVE_INEXISTENTE"
>>
=== Parte 3 · ListarCategoria (streaming) ===
Recibiendo productos de la categoría...
Error en el streaming: StatusCode.NOT_FOUND - No existen productos de la categoría bebidas
```

## Issues

Enlaces a los issues que abrieron en el repositorio del vecino o que les abrieron a ustedes (si hubo):

-

## Uso de IA (Acuerdo No. 23/2024 UdeC)

¿Usaron IA? ¿Cuál, quién y para qué? (por ejemplo: "Copilot para el for de la parte 3; lo revisamos línea por línea").

- si, se uso gemini para depurar errores 
