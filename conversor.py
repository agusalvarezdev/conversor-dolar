from datetime import datetime
import requests

url = "https://dolarapi.com/v1/dolares"
try:
    respuesta = requests.get(url)
    respuesta.raise_for_status()
    datos = respuesta.json()
except requests.RequestException as e:
    print("Error al obtener cotizaciones:", e)
    exit(1)
except ValueError:
    print("Error: la API no devolvió datos válidos.")
    exit(1)

def obtener_precio_blue():
    """Pide la API y devuelve (precio_venta, fecha_actualizacion). Si falla, devuelve (None, None)."""
    try:
        resp = requests.get(url)
        resp.raise_for_status()
        datos = resp.json()
        blue = next(item for item in datos if item["casa"] == "blue")
        precio = blue["venta"]
        fecha = blue.get("fechaActualizacion", "?")
        return precio, fecha
    except (requests.RequestException, ValueError, StopIteration):
        return None, None


try:
    blue = next(item for item in datos if item["casa"] == "blue")
    precio_dolar = blue["venta"]
    fecha_actualizacion = blue.get("fechaActualizacion", "?")
except StopIteration:
    print("No se encontró cotización del dólar blue.")
    exit(1)

if precio_dolar is None or precio_dolar <= 0:
    print("La cotización del dólar blue no es válida (vacía o cero).")
    exit(1)

while True:
    print("\n--- Dólar blue (venta):", precio_dolar, "| Actualizado:", (fecha_actualizacion[:16] if fecha_actualizacion else "?"))
    print("1 - Pesos a Dolares")
    print("2 - Dolares a Pesos")
    print("3 - Actualizar cotización")
    print("4 - Ver historial")
    print("5 - Salir")
    opcion = input("Que queres hacer?: ").strip()

    if opcion == "1":
        pesos = input("Ingresa el monto en pesos: ").strip()
        pesos = pesos.replace(".", "").replace(",", "")
        try:
            valor = float(pesos)
            if valor <= 0:
                print("El monto tiene que ser mayor que cero.")
            else:
                resultado = valor / precio_dolar
                print(f"tenes {resultado:,.2f} dolares")
                ahora = datetime.now().strftime("%d/%m/%Y %H:%M")
                with open("historial.txt", "a") as archivo:
                    archivo.write(f"{ahora} - Pesos a dolares: {pesos} pesos = {resultado:.2f} dolares\n")
        except ValueError:
            print("Monto inválido. Ingresá solo números.")

    elif opcion == "2":
        dolares = input("Ingresa el monto en dolares: ").strip()
        dolares = dolares.replace(",", "").replace(".", "")
        try:
            valor = float(dolares)
            if valor <= 0:
                print("El monto tiene que ser mayor que cero.")
            else:
                resultado = valor * precio_dolar
                print(f"tenes {resultado:,.2f} pesos")
                ahora = datetime.now().strftime("%d/%m/%Y %H:%M")
                with open("historial.txt", "a") as archivo:
                    archivo.write(f"{ahora} - Dolares a pesos: {dolares} dolares = {resultado:.2f} pesos\n")
        except ValueError:
            print("Monto inválido. Ingresá solo números.")
    elif opcion == "3":
        print("Actualizando cotización...")
        nuevo_precio, nueva_fecha = obtener_precio_blue()
        if nuevo_precio and nuevo_precio > 0:
            precio_dolar = nuevo_precio
            fecha_actualizacion = nueva_fecha if nueva_fecha else fecha_actualizacion
            print("Listo. Nuevo precio de venta:", precio_dolar)
        else:
            print("No se pudo actualizar. Se sigue usando el precio anterior.")

    elif opcion == "4":
        try:
            with open("historial.txt", "r") as archivo:
                lineas = archivo.readlines()
            if not lineas:
                print("Aún no hay historial.")
            else:
                print("\n--- Últimas operaciones ---")
                for linea in lineas[-10:]:
                    print(linea.rstrip())
        except FileNotFoundError:
            print("Aún no hay historial.")

    elif opcion == "6":
        for dato in datos:
            print(f"{dato['nombre']}: compra {dato['compra']} - venta {dato['venta']}")

    elif opcion == "5":
        print("seguro que queres salir?")
        print("1-si")
        print("2-no")
        opcion = input("Que queres hacer?: ").strip()
        if opcion == "1":
            print("Chau!")
            break
        elif opcion == "2":
            print("Ok, continuamos.")
        
    else:
        print("Opción no válida.")

        