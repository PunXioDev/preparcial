from datetime import datetime

# fecha
now = datetime.now()
fichos = []
options = 1
numeroDeFicho = 0

def findFicho(numeroFicho):
    for ficho in fichos:
        if(ficho['numero'] == numeroFicho):
            print(f"Ficho")
            print(f'Numero:',ficho['numero'])
            print(f'Nombre:',ficho['nombre'])
            print(f'Fecha:',ficho['fecha'])
            print(f"**")

def findFichos():
    for ficho in fichos:
        if(ficho):
            print(f"Ficho")
            print(f'Numero:',ficho['numero'])
            print(f'Nombre:',ficho['nombre'])
            print(f'Fecha:',ficho['fecha'])
            print(f"**")
        else:
            print(f"No hay fichos")

def findFichosReverse():
    for ficho in reversed(fichos):
        print(f"Ficho")
        print(f'Numero:',ficho['numero'])
        print(f'Nombre:',ficho['nombre'])
        print(f'Fecha:',ficho['fecha'])
        print(f"**")

# arreglar funcion
# def deleteFicho(numeroFicho):
#     for ficho in fichos:
#         if(ficho['numero'] == numeroFicho):
#             indice = fichos.index(ficho['numero'])
#             fichos.pop(indice)

while options != 0:
    print(f"*****")
    print(f"*Opcion 1: Registrar ficho*")
    print(f"*Opcion 2: Modificar dueño del ficho*")
    print(f"*Opcion 3: ver fichos*")
    print(f"*Opcion 4: ver fichos al reves*")
    print(f"*Opcion 5: eliminar TODOS los fichos*")
    print(f"*Presiona 0 para cerrar.*")
    print(f"*****")
    options = int(input("Digite una opción: "))
    print(f"*****")

    if(options == 1):
        print(f"*****")
        print(f"Estas registrando un ficho")
        print(f"*****")

        numeroDeFicho = numeroDeFicho + 1
        ficho = {}

        ficho['numero'] = numeroDeFicho
        ficho['nombre'] = input(f"Digite el nombre de la persona que solicita el ficho {ficho['numero']}: ")
        ficho['fecha'] = now

        for fichoForCreate in fichos:
            if(fichoForCreate['numero'] == ficho['numero']):
                print(f"El ficho ya existe. El dueno es: {fichoForCreate['nombre']}")
                options = 1
            else:
                pass

        if(ficho):
            fichos.append(ficho)

    elif (options == 2):
        print(f"*****")
        print(f"Estas registrando un ficho")
        print(f"*****")

        fichoUpdate = int(input("Digite el numero del ficho que quiere actualizar: "))

        for fichoForUpdate in fichos:
            if (fichoForUpdate['numero'] == fichoUpdate):
                print(f"El ficho {fichoUpdate} esta registrado para {fichoForUpdate['nombre']}")
                findFicho(fichoUpdate)
            else:
                pass
        fichoForUpdate['nombre'] = input(f"Digite el nuevo dueño del ficho {fichoUpdate}: ")
        fichoForUpdate['fecha'] = now

        findFichos()

    # arreglar eliminar un solo elemento
    # elif (options == 2):
    #     print(f"*****")
    #     print(f"Estas eliminando un ficho")
    #     print(f"*****")

    #     numFicho = int(input(f'Digite el numero de la boleta a eliminar: '))
    #     delete = input(f'¿Seguro que quieres eliminar el ficho {numFicho}? (S/n) ')
    #     if (delete == 's' or delete == 'S'):
    #         deleteFicho(numFicho)
    #         print('Se elimino el ficho. Los fichos actuales son:')
    #         findFichos()
    #     elif (delete == 'n' or delete == 'N'):
    #         options = int(input("Digite una opción (entre 1 a 2): "))

    elif (options == 3):
        print(f"*****")
        print(f"Estas viendo los fichos")
        findFichos()
        print(f"*****")
    elif (options == 4):
        print(f"*****")
        print(f"Todos los fichos al reves")
        findFichosReverse()
        print(f"*****")
    elif (options == 5):
        print(f"*****")
        fichos.clear()
        numeroDeFicho = 0
        print(f"Se elimino todos los fichos")
        print(f"*****")
        findFichos()
    else:
        print(f"*****")
        options = int(input("Digite una opción (entre 1 y 5, excepto el 2.): "))
        print(f"*****")