#https://github.com/coni-escobar/equipos.git

import csv
lista=[]

def conf_cambio():
    op=input("¿Esta seguro de realizar el cambio?")
    if op=="si":
        return 1
    elif op=="no":
        return 0
    else:
        print("Ingrese una opción válida")
        
def cont_puntos():
    if Puntos <0 and Puntos >151:
        return print("Ingrese un puntaje valido. (0 a 150)")
    elif Puntos >=0 and Puntos <=150:
        return ("Añadido correctamente")
def estadisticas():
    cont=0
    acum=0
    Punto=0
    for x in lista:
        cont=cont+1
        acum=int(acum+x[2])
    prom=acum/cont
    return print("El promedio de puntos es de = ",prom)
    for x in lista:
        p=x[2]
        return print("El puntaje mas alto fue= ",Punto)

while True:
    print("- - - - - - -")
    print("- - - menú - - - ")
    print("")
    print("1.- Agregar equipo")
    print("2.- Listar equipo")
    print("3.- Actualizar nombre de equipo por ID")
    print("4.- Generar BBDD")
    print("5.- Cargar BBDD")
    print("6.- Estadisticas")
    print("0.- Salir")
    print("")
    op=int(input("Seleccione una opción: "))
    print("")

    if op==1:
        print("")
        ID=int(input("Ingrese el ID del equipo: "))
        Nombre=input("Ingrese el nombre del equipo: ")
        Puntos=int(input("Ingrese los puntos del equipo: "))
        cont_puntos()
        if Puntos >=0 and Puntos <=40:
            categoria="Amateur"
        elif Puntos >=41 and Puntos <=80:
            categoria="Principiante"
        elif Puntos >=81 and Puntos <120:
            categoria = "Avanzado"
        elif Puntos>120 and Puntos<=150:
            categoria = "Idolos"
        else:
            print("Ingresa puntaje valido (0-150)")
            
        listaequipo=[ID,Nombre,Puntos,categoria]
        lista.append(listaequipo)
                          
    elif op==2:
        print("")
        print("Listar equipo")
        print("")
        for x in lista:
            print("ID del equipo: ",x[0],"Nombre: ",x[1],"Puntos: ",x[2],"categoria: ",x[3])
            print("- - - - - - - - - - - - ")
    elif op==3:
        print("")
        print("Actualizar nombre de equipo por ID")
        print("")
        encontrado=False
        ID=int(input("Ingrese la ID del equipo a modificar : "))
        op1=conf_cambio()
        if op1==1:
            for x in lista:
                if ID==x[0]:
                    print("Equipo existente")
                    print("ID: ",x[0],"Nombre: ",x[1],"Puntos: ",x[2],"categoria: ",x[3])
                    nuevo_id=int(input("Ingrese el nuevo ID: "))
                    x[0]=nuevo_id
                    print("ID actualizado")
                    encontrado=True
                    print("")
            if encontrado==False:
                            print("El equipo que ingresó no existe")
        if op1==0:
                print("ID no modificado")
                           
        elif op==4:
            print("")
            print("Generar BBDD")
            print("")
            with open('bbdd_equipos.csv','w',newline='') as bbdd_equipos:
                escritor_csv=csv.writer(bbdd_equipos)
                escritor_csv.writerows(['ID','NOMBRE','PUNTOS','CATEGORIA'])
                escritor_csv.writerows(lista)
                print("BBDD generado correctamente")
            
        elif op==5:
            print("")
            print("Cargar BBDD")
            print("")
            with open('bbdd_equipos.csv','r',newline='')as bbdd_equipos:
                lector_csv=csv.reader(bbdd_equipos)
                for x in lector_csv:
                    lista.append(x)
                print("csv cargado con exito")
            
        elif op==6:
            estadisticas()
        elif op==0:
            print("")
            print("adio")
            break
        else:
            print("")
            print("ERROR")
            print("Ingrese una opcion valida.")
           
           
