# Revisión del conversor (estilo profesor)

## 1. ¿Qué hace cada parte del código?

### Imports y URL (líneas 1-4)
- **`from datetime import datetime`**: Importas solo la clase `datetime` para obtener fecha y hora al guardar en el historial.
- **`import requests`**: Librería para hacer peticiones HTTP (en tu caso, GET a la API del dólar).
- **`url`**: La dirección de la API que devuelve las cotizaciones en JSON.

### Obtención de datos (líneas 5-14)
- **`requests.get(url)`**: Pide los datos al servidor. No garantiza que la respuesta sea correcta (puede ser 404, 500, sin internet, etc.).
- **`respuesta.raise_for_status()`**: Si el servidor respondió con error (ej. 404), lanza una excepción. Así evitas seguir con datos inválidos.
- **`respuesta.json()`**: Convierte el cuerpo de la respuesta (texto JSON) en una lista/diccionario de Python.
- **`try/except`**: Si algo falla (red, JSON mal formado), mostrás un mensaje y salís con `exit(1)` en lugar de que el programa crashee sin explicación.

### Mostrar cotizaciones y elegir el blue (líneas 16-24)
- **`for dolar in datos`**: Recorrés cada elemento de la lista (cada “casa” de cambio: oficial, blue, etc.) y mostrás nombre, compra y venta.
- **`next(item for item in datos if item["casa"] == "blue")`**: Buscás el primer elemento cuya clave `"casa"` sea `"blue"` y lo guardás en `blue`. Si no hay ninguno, `next()` lanza `StopIteration`.
- **`precio_dolar = blue["venta"]`**: Te quedás con el precio de venta del blue para usarlo en las conversiones.

### Bucle principal (líneas 26-60)
- **`while True`**: El menú se repite hasta que el usuario elija salir.
- **Menú**: Mostrás las 3 opciones y leés la elección con `input()`.
- **Opción 1**: Pedís pesos, quitás puntos y comas para poder hacer `float(pesos)`, dividís por `precio_dolar`, mostrás el resultado y guardás en `historial.txt` con fecha/hora.
- **Opción 2**: Igual pero al revés: pedís dólares, multiplicás por `precio_dolar`, mostrás y guardás.
- **Opción 3**: Imprimís "Chau!" y `break` sale del `while`, por lo que el programa termina.
- **`else`**: Cualquier otra tecla muestra "Opción no válida." y el bucle vuelve a mostrar el menú.

---

## 2. Errores o malas prácticas

| Qué | Dónde | Problema |
|-----|--------|----------|
| **No limpiar el input** | `opcion`, `pesos`, `dolares` | Si el usuario pone espacios o Enter de más (ej. `"  1  "` o `"3\n"`), la comparación `opcion == "1"` puede fallar. Conviene usar `.strip()` para quitar espacios y saltos de línea. |
| **División sin validar** | `float(pesos) / precio_dolar` | Si la API devolviera `venta: 0`, tendrías `ZeroDivisionError`. No es común, pero es buena práctica comprobar que `precio_dolar > 0` antes de dividir. |
| **Precio fijo en el tiempo** | Todo el programa | La cotización se pide solo al inicio. Si dejás el programa abierto mucho rato, el valor del dólar puede quedar desactualizado. No es un “error”, pero es una limitación que conviene tener clara. |
| **`exit(1)`** | Líneas 11, 13, 23 | En un script chico está bien. En programas más grandes suele preferirse no usar `exit()` dentro de funciones y en su lugar devolver un código de error o lanzar una excepción para que quien llame decida qué hacer. |

No hay errores graves; el código es legible y la lógica es correcta.

---

## 3. Mejoras sugeridas (sin reescribir todo)

1. **Usar `.strip()` en todos los `input()`**  
   Así aceptás `"1"`, `"  1  "` y evitas problemas con espacios o Enter accidental.

2. **Validar que `precio_dolar` sea mayor que 0**  
   Después de obtener `precio_dolar`, si es `0` o `None`, mostrar un mensaje y salir (o no usar ese valor). Así evitás un posible `ZeroDivisionError` o resultados absurdos.

3. **Opcional para más adelante**  
   - Añadir una opción tipo “4. Actualizar cotización” que vuelva a llamar a la API y actualice `precio_dolar`.  
   - O mostrar la fecha de actualización que trae la API (`fechaActualizacion`) para que el usuario sepa qué tan viejo es el precio.

---

## 4. Cambios que voy a hacer en el código (y por qué)

Voy a aplicar solo dos cosas en el archivo:

1. **Agregar `.strip()` a los `input()`**  
   - En la opción elegida en el menú.  
   - En el monto en pesos.  
   - En el monto en dólares.  
   Así, si el usuario escribe `"  2  "` o `" 1000 "`, el programa sigue funcionando bien.

2. **Comprobar que `precio_dolar` sea válido**  
   Después de `precio_dolar = blue["venta"]`, si es `None` o menor o igual a 0, mostramos un mensaje y salimos. Así no se divide por cero ni se multiplica por un valor raro.

No voy a tocar la estructura del programa ni reescribir el resto.

---

## 5. Preguntas para ver si entendiste el código

**Pregunta 1:** Si en la opción 1 el usuario escribe `1.500,50` (mil quinientos con coma decimal), ¿qué hace tu código antes de hacer `float(pesos)`? ¿Qué string queda en `pesos` después de los `replace` y por qué con eso `float()` puede funcionar?

**Pregunta 2:** ¿Por qué usamos `break` en la opción 3 y no `exit(0)`? ¿Qué pasaría si en lugar de `break` pusieras `exit(0)`? (Pensá en si el programa hace algo más después del `while`.)
