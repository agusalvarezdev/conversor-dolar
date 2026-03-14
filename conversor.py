import requests
url = "https://dolarapi.com/v1/dolares"
respuesta =requests.get(url)
datos = respuesta.json()
for dolar in datos:
    print(f"{dolar['nombre']}: compra{dolar['compra']} - venta {dolar['venta']}")
blue = next(item for item in datos if item["casa"]== "blue")
precio_dolar = blue["venta"]
print("1-Pesos a Dolares")
print("2-Dolares a Pesos")
print("3. Salir")
opcion = input("que queres hacer?:")
if opcion == "1":
    pesos = input("Ingresa el monto en pesos: ")
    pesos=pesos.replace(".", "").replace("," , "")
    resultado= float(pesos) / precio_dolar  
    print(f"tenes {resultado:,.2f}dolares")
    with open("historial.txt" , "a") as archivo:
        archivo.write(f"Pesos a dolares: {pesos} pesos={resultado:.2f} dolares\n")
elif opcion == "2":
    dolares=input("Ingresa el monto en dolares: ")
    dolares= dolares.replace("," , "").replace("," , "")
    resultado= float(dolares) * precio_dolar
    print(f"tenes {resultado:,.2f} pesos")
    with open("historial.txt" , "a") as archivo:
        archivo.write(f"dolares a pesos: {dolares} dolares={resultado:.2f} pesos\n")
elif opcion == "3":
    print("Chau!3")
        