import json
def abrirarchivo(miJson):
    miJson=[]
    with open("info.json",encoding="utl-8")in miarchivo:
        miJson=json.load(miarchivo)



def guardarArchivo(miJson):
    with open("info.json","w") in miarchivo:
        miJson=json.dump(miarchivo)
   
def menuprincipal():
    print(":::::::::::::: MENU PRINCIPAL :::::::::::::::::\n"
    "1 MODULO DE USUARIO\n"
    "2 MODULO DE SERVICIO\n"
    "3 MODULO DE REPORTES\n"
    "4 MODULO DE CLIENTES LEALES\n"
    "5 FINALIZAR PROGRAMA\n"
    "::::::::::::::::::::::::::::::::::::::::::::::::::::::\n")
def menuusuario():
    print(":::::::::::MENU DE USUARIO (ADMINISTRATIVO)::::::::::\n"
    "1 Regitro y gestion de usuario\n"
    "2 Seguimiento de historial de uasuarios\n"
    "3 Personalizacion de servicios\n"
    "4 Gestion de la fidelizacion del cliente\n"
    "5 Finalizar")
def menuregistroygestion():
    print(":::::::Registro  y gestion :::::::\n"
    "1 actualizar datos\n"
    "2 ingresar nuevo usuario\n"
    "::::::::::::::::::::::::::::::::::::::::::\n")
def menuhistorial():
    print("::::::: menu historial ::::::::::\n"
    "1 servicios utilizados\n"
    "2 consultas, reclamaciones y sugerencias\n")
miarchivo=[]
bool=True
while bool==True:
    print("")
    print("===========BIENVENIDO A GESTION DE USUARIO=============")
    menuprincipal()
  
    opc=int(input("ingrese su opcion por favor: "))
    if opc==1:
        menuregistroygestion()
        dupu=True
        while dupu==True:
            try: 
                opci=int(input("ingrese una opcion: "))
                if opci==1:
                    print("tipos de clientes","1 leales","2 regulares", "3 nuevos")
                    opc=int(input("ingrese la opcion del grupo en donde va a actualizar: "))
                    if opc==1:
                        print(":::::::::::actualizar datos::::::::::::")
                        print("::::menu::::\n","1 nombre\n","2 apellido \n","3 direccion\n","4 telefono\n","5 edad\n","6 finalizar\n")
                        tuelijes=int(input("ingrese una opcion:"))
                        if tuelijes==1:
                            nomnew=input("ingrese el nuevo nombre: ")
                            for i in miJson[0]["usuarios"]:
                                for a in i[" clientes leales"]:
                                    a["nombre"]=nomnew
                        if  tuelijes==2:
                            apenew=input("ingrese el nuevo appellido: ")
                            for i in miJson[0]["usuarios"]:
                                for a in i[" clientes leales"]:
                                    a["apellido"]=apenew
                        if  tuelijes==3:
                            dirnew=input("ingrese la nueva direccion: ")
                            for i in miJson[0]["usuarios"]:
                                for a in i[" clientes leales"]:
                                    a["direccion"]=dirnew
                        if  tuelijes==4:
                            telnew=input("ingrese el nuevo numero: ")
                            for i in miJson[0]["usuarios"]:
                                for a in i[" clientes leales"]:
                                    a["telefono"]=telnew
                        if tuelijes==5:
                            edanew=input("ingrese la nueva edad: ")
                            for i in miJson[0]["usuarios"]:
                                for a in i[" clientes leales"]:
                                    a["edad"]=edanew
                        if tuelijes==6:
                            dupu=False
                            du=input("deseas seguir actualizando en otro grupo si o no(presiona enter):")
                            if du!="si":
                                dupu=False

                    if opc==2:
                        print(":::::::::::actualizar datos::::::::::::")
                        print("::::menu::::\n","1 nombre\n","2 apellido \n","3 direccion\n","4 telefono\n","5 edad\n","6 finalizar\n")
                        tuelijes=int(input("ingrese una opcion:"))
                        if tuelijes==1:
                            nomnew=input("ingrese el nuevo nombre: ")
                            for i in miJson[0]["usuarios"]:
                                for a in i[" clientes regulares"]:
                                    a["nombre"]=nomnew
                        if  tuelijes==2:
                            apenew=input("ingrese el nuevo appellido: ")
                            for i in miJson[0]["usuarios"]:
                                for a in i[" clientes regulares"]:
                                    a["apellido"]=apenew
                        if  tuelijes==3:
                            dirnew=input("ingrese la nueva direccion: ")
                            for i in miJson[0]["usuarios"]:
                                for a in i[" clientes regulares"]:
                                    a["direccion"]=dirnew
                        if  tuelijes==4:
                            telnew=input("ingrese el nuevo numero: ")
                            for i in miJson[0]["usuarios"]:
                                for a in i["clientes regulares"]:
                                    a["telefono"]=telnew
                        if tuelijes==5:
                            edanew=input("ingrese la nueva edad: ")
                            for i in miJson[0]["usuarios"]:
                                for a in i["clientes regulares"]:
                                    a["edad"]=edanew
                        if tuelijes==6:
                            dupu=False
                            du=input("deseas seguir actualizando en otro grupo si o no(presiona enter):")
                            if du!="si":
                                dupu=False
                    if opc==3:
                        print(":::::::::::actualizar datos::::::::::::")
                        print("::::menu::::\n","1 nombre\n","2 apellido \n","3 direccion\n","4 telefono\n","5 edad\n","6 finalizar\n")
                        tuelijes=int(input("ingrese una opcion:"))
                        if tuelijes==1:
                            nomnew=input("ingrese el nuevo nombre: ")
                            for i in miJson[0]["usuarios"]:
                                for a in i[" clientes nuevos"]:
                                    a["nombre"]=nomnew
                        if  tuelijes==2:
                            apenew=input("ingrese el nuevo appellido: ")
                            for i in miJson[0]["usuarios"]:
                                for a in i[" clientes nuevos"]:
                                    a["apellido"]=apenew
                        if  tuelijes==3:
                            dirnew=input("ingrese la nueva direccion: ")
                            for i in miJson[0]["usuarios"]:
                                for a in i[" clientes nuevos"]:
                                    a["direccion"]=dirnew
                        if  tuelijes==4:
                            telnew=input("ingrese el nuevo numero: ")
                            for i in miJson[0]["usuarios"]:
                                for a in i["clientes nuevos"]:
                                    a["telefono"]=telnew
                        if tuelijes==5:
                            edanew=input("ingrese la nueva edad: ")
                            for i in miJson[0]["usuarios"]:
                                for a in i["clientes nuevos"]:
                                    a["edad"]=edanew
                        if tuelijes==6:
                            dupu=False
                            du=input("deseas seguir actualizando en otro grupo si o no(presiona enter):")
                            if du!="si":
                                dupu=False
                if opci==2:
                    print ("::::::: ingresar nuevo usuario::::::::")  
                    iD=input("ingrese laid del nuevo usuario: ")
                    nomb=input("ingrese el nombre de nuevo usuario: ")
                    apell=input("ingrese el apellido del nuevo usuario: ")
                    dire=input("ingrese la direccion de nuevo usuario: ")
                    try:
                        telefono=int(input("ingrese el numero te telefono del nuevo usuario: "))
                    except ValueError:
                        print("ingrese una opcion valida")
                    edad=input("ingrese la edad del usuario: ")

                    #for i in miarchivo[0]["usuarios"]:
                        #i.append("nombre":nomb,"apellido":ape,"direccion":dire,"telefono":telefono,"edad":edad)


    
            except ValueError:
                print("ingrese una i¿opcion valida")
           
        
      

#desarrollado por yurley botello t.i 1066085539

 