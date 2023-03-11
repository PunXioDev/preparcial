options = 1
empanadas = []

while options != 0:
    print(f"*Empanada pa ti*")
    print(f"*Opcion 1:*")
    print(f"*Opcion 2:*")
    print(f"*Opcion 3:*")
    print(f"*Opcion 4:*")
    print(f"*Opcion 5:*")
    print(f"*Presiona 0 para cerrar.*")
    options = int(input("Digite una opción: "))

    if (options == 0):
        pass
    elif (options == 1):
        empanada = {}
        empanada["id"] = int(input(f"Digite la identificacion de la empanada: "))
        empanada["nombre"] = input(f"Digite el nombre de la empanada: ")
        empanada["precio"] = float(input(f"Digite el precio de la empanada: "))
        empanada["popularidad"] = int(input(f"Digite la popularidad de la empanada: "))
        empanada["fechaVencimiento"] = input(f"Digite la fecha de vencimiento de la empanada: ")

        empanadas.append(empanada)
        print(f"Empanada registrada")

    elif (options == 2):
        if (empanadas):
            for empanada in empanadas:
                print(empanada)
        else:
            print("No hay empanadas")

    elif (options == 3):
        buscarEmpanada = int(input("Digite el id de la empanada que quiere buscar: "))
        for empanada in empanadas:
            if (empanada["id"] == buscarEmpanada):
                print(f"La empanada {buscarEmpanada} es {empanada}")
            else:
                print(f"La empanada {buscarEmpanada} no existe.")
    elif (options == 4):
        buscarEmpanada = int(input("Digite el id de la empanada que quiere actualizar: "))
        for empanada in empanadas:
            if (empanada["id"] == buscarEmpanada):
                print(f"La empanada {buscarEmpanada} es {empanada} y su precio es {empanada['precio']}")
                empanada["precio"] = float(input(f"Digite el nuevo precio de {empanada}: "))
            else:
                print(f"La empanada {buscarEmpanada} no existe.")
    elif (options == 5):
        pass
    else:
        print(f"Digite una opcion entre 0 y 5")
