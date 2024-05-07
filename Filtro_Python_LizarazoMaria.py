import json
from os import system

with open("MiJson.json", encoding="utf-8") as archivo:
    info = json.load(archivo)

sel=0
while sel!=3:
    system("cls")
    print("------------------- BIENVENIDO AL MENÚ -------------------\n")
    print("""
    1. Usuario
    2. Administración
    3. Salir
    """)
    inicio=int(input("¿Usted es?\n"))

    if inicio==1:
        sel1=0
        while sel1!=2:
            print("Bienvenido al modulo del usuario.")
            print("""
                1. Ver mis planes
                2. Salir
                """)
            haga=int(input("Que desea hacer:\n"))

            if haga==1:
                for i in range (0,len(info[1]["Planes"])):
                    print(info[1]["Planes"][i]["Movistar"])
                    print("---------------------------------------------------")
                input("Para volver al menú de usuario, presione ENTER.")
                system("cls")
                
            else:
                print("Gracias por ingresar al menú de usuario.")
                input("Presione ENTER para regresar al menú principal.")
                break


    if inicio==2:
        sel2=0
        while sel2!=4:
            print("Bienvenido, Administrador")
            print(""" ¿Que desea hacer?\n
                1. Ver los clientes
                2. Registrar un cliente
                3. Salir
                """)
            hacer=int(input("Que desea hacer:\n"))

            if hacer==1:
                contador=0
                for i in range (0,len(info[0]["Usuarios"])):
                    contador+=1
                    print("Identificador:", contador)
                    print("Nombres: ", info[0]["Usuarios"][i]["Nombres"])
                    print("Apellidos: ", info[0]["Usuarios"][i]["Apellidos"])
                    print("Telefono: ", info[0]["Usuarios"][i]["Telefono"])
                    print("Fijo: ", info[0]["Usuarios"][i]["Fijo"])
                    print("Direccion: ", info[0]["Usuarios"][i]["Direccion"])
                    print("---------------------------------------------------")
                input("Para volver al menú, presione ENTER.")
                system("cls")

            if hacer==2:
                for i in range (0,len(info[0]["Usuarios"])):
                    iden=(input("Ingrese un identificador para el nuevo cliente.\n"))
                    nom=(input("Ingrese el nombre del nuevo cliente.\n"))
                    ape=(input("Ingrese el apellido del nuevo cliente.\n"))
                    tel=(input("Ingrese el número de telefono del nuevo cliente.\n"))
                    fijo=(input("Ingrese el fijo del nuevo cliente.\n"))
                    dir=(input("Ingrese la Direccion del nuevo cliente.\n"))
                    break
                info[0]["Usuarios"].append(
                    {
                        "Identificador" : iden,
                        "Nombres" : nom,
                        "Apellidos" : ape,
                        "Telefono" : tel,
                        "Fijo" : fijo,
                        "Direccion" : dir
                    }
                )
                with open("MiJson.json", "w") as file:
                    json.dump(info,file)
                print("El nuevo cliente ha sido guardado exitosamente.")
                input("Presione ENTER para continuar al menú")
                system("cls")

            else:
                print("Saliendo del modulo administrador")
                input("Presieno ENTER para regresar al menú")
                break              

    else:
        print("Gracias por visitarnos")
        input("Presieno ENTER para finalizar el programa")
        break

# Realizado por María Lizarazo 
# Pdta; Se hizo lo que se pudo profe, no nos ande tan duro :V PFV :'(