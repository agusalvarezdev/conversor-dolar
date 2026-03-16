gastos = []
while True: 
    print("1-Agregar gasto")
    print("2-Ver todos los gastos")
    print("3-Ver total")
    print("4-salir")
    opcion=input("Que opcion elegis?:")
    if opcion == "1":
       nombre = input("nombre del gasto")
       monto = input("monto: ")
       gastos.append({"nombre": nombre,"monto": float(monto)})
        

    elif opcion == "4":
        print("chau!")   
        break
    elif opcion == "2":
        for gasto in gastos:
            print(gasto["nombre"], gasto["monto"])        
    elif opcion == "3":
        total= 0
        for gasto in gastos:
            total = total + gasto["monto"]
        print(f"total: {total}")    
