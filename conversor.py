import requests
url = "https://dolarapi.com/v1/dolares/blue"
respuesta =requests.get(url)
datos = respuesta.json()
precio_dolar= datos ["venta"]
pesos=input("cuantos pesos tenes guardados ahora?")
resultado= float(pesos) / precio_dolar
print(f"Tenes {resultado:.2f} dolares")