import requests
url = "https://dolarapi.com/v1/dolares/blue"
respuesta =requests.get(url)
datos = respuesta.json()
precio_dolar= datos ["venta"]
print("1-Pesos a Dolares")
print("2-Dolares a Pesos")
print("3. Salir")
opcion = input("que queres hacer?:")
if opcion == "1":
    pesos = input("Ingresa el monto en pesos: ")
    pesos=pesos.replace(".", "").replace("," , "")
    resultado= float(pesos) / precio_dolar  
    print(f"tenes {resultado:,.2f}dolares")
elif opcion == "2":
    dolares=input("Ingresa el monto en dolares: ")
    resultado= float(dolares) * precio_dolar
    print(f"tenes {resultado:,.2f} pesos")
elif opcion == "3":
    print("Chau!3")
    