"""
-----------------------------------------------------------------------------------------------
Título: Entrega 1
Fecha: 11 de mayo
Autor: Jonathan Lucas Cáceres 

Descripción:

Pendientes:
-----------------------------------------------------------------------------------------------
"""

#----------------------------------------------------------------------------------------------
# MÓDULOS
#----------------------------------------------------------------------------------------------
import time, random


#----------------------------------------------------------------------------------------------
# FUNCIONES
#----------------------------------------------------------------------------------------------

#VALIDACIONES

def validarNumero(num):
    while True:
        if not num.isdigit():
            print("Entrada no valida. Por favor ingrese un número entero")
        else:
            return int(num)
        num = input("   Tiene que ser un número entero: ")

def validarSiNo(opcion): #Valida que la entrada sea S, N, True o False con sus variantes
    while True:
        if opcion not in ["S", "N", "n", "s", "True", "False"]:
            print("Valor no válido. Ingrese S o N.")
        elif opcion in ["S", "s", "True"]:
            return True
        elif opcion in ["N", "n", "False"]:
            return False
        opcion = input("¿Desea generar una nueva lista? (S/N): ")

def validacionNumMayor2(num):
    while True:
        if not num.isdigit():
            mensaje = "Entrada inválida. Por favor, ingrese un número entero."
            print(mensaje.center(120, "="))
        
        # 2. Validar que el valor numérico sea mayor o igual a 2
        elif int(num) < 2:
            mensaje = "La cantidad de valores debe ser al menos 2."
            print(mensaje.center(120, "="))
        
        # 3. Si pasa ambas validaciones, el número es correcto
        else:
            return int(num)
            
        # Solicitar nueva entrada solo si falló alguna validación
        num = input("\nIngrese la cantidad de valores a generar: ")

#   TAREA 1
def listarRandom(lista, cantValores):
    while len(lista) < cantValores:

        valor1 = random.randint(0, 9) 
        valor2 = random.randint(100, 999)
        valor3 = random.randint(10000,99999)
        valores = valor1, valor2, valor3
        valor = random.choice(valores)
        lista.append(valor) # Agrega el valor a la lista

def generarValores(cantValores,lista):
    ''' 
    docstring
    '''
    if lista:
        eleccion =validarSiNo(input("Lista ya creada anteriormente, desea generar una nueva lista? (S/N): \n"))
        if eleccion:
            listaNuevaVacia = [] # Crea una nueva lista
            listarRandom(listaNuevaVacia, cantValores)
            lista = listaNuevaVacia # Asigna la nueva lista a la variable original
        else:
            print("No se generará una nueva lista.") 
    else:
        print("Primera vez que se crea la lista")
        print()
        listarRandom(lista, cantValores)
    return lista

#   TAREA 2
Letras=["A","B","C","D","E","F","G","H","I","J"]

def mostrarValores(miLista, titulo):
    filas=0

    if len(miLista) == 0: #Cambiar segun funcion 1
        print("No hay valores generados.")
    else:

        print("*" * 90)
        print(titulo)
        print("*" * 90)

        guion="="*7

        for letra in Letras:
            print(letra.center(9), end="")

        print()

        for i in range(10):
            print(guion.center(9),end="")

        print()

        for numero in miLista:
            print(str(numero).center(9), end="")
            filas=filas+1

            if filas==10:
                print()
                filas=0

        print()

        fechaHora = time.strftime("%d-%m-%Y %H:%M:%S")
        print("FIN DEL LISTADO (" + fechaHora + ") " + "*" * 52)

#   TAREA 3 ELIMINAR VALORES REPETIDOS
def eliminarRepetidos(lista):
    lista3 = lista[:]
    resultado = []
    contadorRepetidos = 0
    for valor in lista3:
        if valor not in resultado:
            resultado.append(valor)
        else:
            contadorRepetidos += 1
    return resultado, contadorRepetidos

#   TAREA 4 FILTRAR VALORES
def criterioFiltro(miLista):
    lista = miLista[:]
    listaResultado = []
    criterio = input("Ingrese el criterio de filtrado [M=Mayores que | E=Menores que | R=En rango | P=Pares | I=Impares]: ")
    while True:
        if criterio in ["M", "m"]:
            valor = validarNumero(input("Criterio de filtrado: Mayores que:  "))
            for elem in lista:
                if elem > valor:
                    listaResultado.append(elem)
            return mostrarValores(listaResultado, f"VALORES DEL JUEGO DE DATOS (Mayores que {valor})")

        elif criterio in ["E", "e"]:
            valor = validarNumero(input("Criterio de filtrado: Menores que:  "))
            for elem in lista:
                if elem < valor:
                    listaResultado.append(elem)
            return mostrarValores(listaResultado, f"VALORES DEL JUEGO DE DATOS (Menores que {valor})")
        
        elif criterio in ["R", "r"]:
            limInferior = validarNumero(input("Criterio de filtrado: En rango.\nIngrese el limite inferior:  "))
            limSuperior = validarNumero(input("Ingrese el limite superior: "))

            for elem in lista:
                if elem > limInferior and elem < limSuperior:
                    listaResultado.append(elem)
            return mostrarValores(listaResultado, f"VALORES DEL JUEGO DE DATOS (VALORES ENTRE {limInferior} y {limSuperior})")
        
        elif criterio in ["P", "p"]:
            print("Criterio de filtrado: Valores Pares")
            for elem in lista:
                if elem % 2 == 0:
                    listaResultado.append(elem)
            return mostrarValores(listaResultado, f"VALORES DEL JUEGO DE DATOS (VALORES PARES)")

        elif criterio in ["I", "i"]:
            print("Criterio de filtrado: Valores Impares")
            for elem in lista:
                if elem % 2 == 1:
                    listaResultado.append(elem)
            return mostrarValores(listaResultado, f"VALORES DEL JUEGO DE DATOS (VALORES IMPARES)")

        
        criterio = input("Valor ingresado incorreco.\nIngrese el criterio de filtrado [M=Mayores que | E=Menores que | R=En rango | P=Pares | I=Impares]: ")

#   TAREA 5 DESDOBLAR VALORES
'''
def desdoblarValores(miLista):
    lista = miLista [:]
    letra = input("Ingrese el criterio de desdoblamiento [P=Pares/Impares | C=Por cantidad de cifras | U=Por valor umbral]: ")
    while True:
        if letra in ["P", "p"]:
            print("Generando dos listas, una de valores pares y otra de impares: \n")
            listaPar = [] 
            listaImpar = []
            for elem in lista:
                if elem % 2 == 0:
                    listaPar.append(elem)
                else:
                    listaImpar.append(elem)
            return mostrarValores(listaPar, f"VALORES DEL JUEGO DE DATOS (PARES)"),print("\n"), mostrarValores(listaImpar, f"VALORES DEL JUEGO DE DATOS (IMPARES)")
        elif letra in ["C", "c"]:
            print("Generando tres listas, una con valores de una cifra, la segunda de tres cifras y la tercera de cinco cifras: \n")
            listaC1 = []
            listaC3 = []
            listaC5 = []
            for elem in lista:
                if elem >= 0 and elem <=9:
                    listaC1.append(elem)
                elif elem >= 100 and elem <= 999:
                    listaC3.append(elem)
                elif elem >= 10000 and elem <= 99999:
                    listaC5.append(elem)
            return mostrarValores(listaC1, f"VALORES DEL JUEGO DE DATOS (UNA CIFRA)"),print("\n"), mostrarValores(listaC3, f"VALORES DEL JUEGO DE DATOS (TRES CIFRAS)"), print("\n"), mostrarValores(listaC5, "VALORES DEL JUEGO DE DATOS (CINCO CIFRAS)")
        elif letra in ["U", "u"]:
            uInferior = []
            uSuperior = []
            umbral = validarNumero(input("Ingresar el valor umbral que generará una lista con valores por debajo y otra por encima: "))
            for elem in lista:
                if elem > umbral:
                    uSuperior.append(elem)
                else:
                    uInferior.append(elem)
            return mostrarValores(uInferior, f"VALORES DEL JUEGO DE DATOS (MENORES QUE {umbral})"),print("\n"), mostrarValores(uSuperior, f"VALORES DEL JUEGO DE DATOS (MAYORES QUE ({umbral})")
'''
def desdoblarValores(miLista):
        """
        Función que a partir de la lista ingresada, pregunta al usuario mediante qué criterios quiere desdoblarla
        Valida la entrada del usuario y crea varias listas a partir de la original según el criterio elegido
        retorna las listas segun criterio seleccionado
        """
        lista = miLista[:]
        lista1 = []
        lista2 = []
        lista3 = []
        
        criterio = input("Ingrese el criterio de desdoblamiento [P=Pares/Impares | C=Por cantidad de cifras | U=Por valor umbral]: ")
        criterio = criterio.upper()
        while criterio != "P" and criterio != "C" and criterio != "U":  #criterio not in ["P,"C","U"]
            print("Valor inválido ingresado, intente de nuevo")
            criterio = input("Ingrese el criterio de desdoblamiento [P=Pares/Impares | C=Por cantidad de cifras | U=Por valor umbral]: ")
            criterio = criterio.upper()
            
        #Validación del umbral
        if criterio == "U":
            umbral = (input("Elija el valor umbral para desdoblar las listas: "))
            print()
            while not umbral.isdigit() or int(umbral) <= 0:
                print("Valor inválido, intente de nuevo")
                umbral = (input("Elija el valor umbral para desdoblar las listas: "))
                print()
            umbral = int(umbral)
            
                
        #Separación de listas por par/impar
        if criterio == "P":
            pos = 0
            while pos < len(lista):
                if lista[pos] % 2 == 0:
                    lista1.append(lista[pos])
                pos = pos + 1
        
            pos = 0
            while pos < len(lista):
                if lista[pos] % 2 != 0:
                    lista2.append(lista[pos])
                pos = pos + 1
            return mostrarValores(lista1, f"VALORES DEL JUEGO DE DATOS (PARES)"),print("\n"), mostrarValores(lista2, f"VALORES DEL JUEGO DE DATOS (IMPARES)")
        
        #Separación de listas por umbral
        elif criterio == "U":
            pos = 0
            while pos < len(lista):
                if (lista[pos]) > umbral:
                    lista1.append(lista[pos])
                pos = pos + 1
            pos = 0
            while pos < len(lista):
                if (lista[pos]) < umbral:
                    lista2.append(lista[pos])
                pos = pos + 1
            return mostrarValores(lista2, f"VALORES DEL JUEGO DE DATOS (MENORES QUE {umbral})"),print("\n"), mostrarValores(lista1, f"VALORES DEL JUEGO DE DATOS (MAYORES QUE {umbral})")
            
        #Separación de listas por cifras
        elif criterio == "C":
            pos = 0
            while pos < len(lista):
                if len(str(lista[pos])) == 1:
                    lista1.append(lista[pos])
                pos = pos + 1
            pos = 0
            while pos < len(lista):
                if len(str(lista[pos])) == 3:   # == 3
                    lista2.append(lista[pos])
                pos = pos + 1
            pos = 0
            while pos < len(lista):
                if len(str(lista[pos])) == 5:   # == 5
                    lista3.append(lista[pos])
                pos = pos + 1
            return mostrarValores(lista1, f"VALORES DEL JUEGO DE DATOS (UNA CIFRA)"),print("\n"), mostrarValores(lista2, f"VALORES DEL JUEGO DE DATOS (TRES CIFRAS)"), print("\n"), mostrarValores(lista3, "VALORES DEL JUEGO DE DATOS (CINCO CIFRAS)")
            
#   TAREA 6 VALORES TOP N
def valoresTop(miLista):
    listaTop = miLista[:]
    listaTop, cant = eliminarRepetidos(listaTop)
    ranking = []
    n = validarNumero(input("Ingrese cantidad de valores mas altos que desea ver: "))
    if n > len(listaTop):
        n = len(listaTop)
        print(f"El valor ingresado es mayor al tamaño de la lista, se cambia el valor ingresado por {n} ")

    for cont in range(0, n):
        aux = 0
        for elem in listaTop:
            if elem > aux:
                aux = elem
        ranking.append(aux)
        for i, elem in enumerate(listaTop):
            if aux == elem:
                del listaTop[i]
        
    for i, elem in enumerate(ranking):
        print (f"{i+1}- {elem}")

#      TAREA 7 MAXIMOS Y MINIMOS
def Valores_Maximos_Y_Minimos(miLista):
 
    maximo = float("-inf")
    minimo = float("+inf") 
    
    for numero in miLista:
        if numero > maximo: 
            maximo = numero 

        if numero<minimo:
            minimo=numero

    return maximo,minimo
    

def mostrarMaximosMinimos(miLista,titulo):
    filas=0

    if len(miLista) == 0: #Cambiar segun funcion 1
        print("No hay valores generados.")
    else:

        print("*" * 90)
        print(titulo)
        print("*" * 90)

        guion="="*7

        for letra in Letras:
            print(letra.center(9), end="")

        print()

        for i in range(10):
            print(guion.center(9),end="")

        print()

        maximo,minimo=Valores_Maximos_Y_Minimos(miLista)

        for numero in miLista:
            if maximo==minimo:
                texto="<" + str(numero).center(5) + ">"

            elif numero == maximo:
                texto = "[" + str(numero).center(5) + "]"

            elif numero == minimo:
                texto = "(" + str(numero).center(5) + ")"


            else:
                texto = str(numero)

            print(texto.center(9), end="")

            filas=filas+1

            if filas==10:
                print()
                filas=0

        print()

        fechaHora = time.strftime("%d-%m-%Y %H:%M:%S")
        print("FIN DEL LISTADO (" + fechaHora + ") " + "*" * 52) 

            




#----------------------------------------------------------------------------------------------
# CUERPO PRINCIPAL
#----------------------------------------------------------------------------------------------
def main():
    #-------------------------------------------------
    # Inicialización de variables
    #----------------------------------------------------------------------------------------------
    miLista = []


    #-------------------------------------------------
    # Bloque de menú
    #----------------------------------------------------------------------------------------------
    while True:
        while True:
            opciones = 7
            print()
            print("---------------------------")
            print("MENÚ DEL PROGRAMA           ")
            print("---------------------------")
            print("[1] Generar Valores")
            print("[2] Mostrar Valores")
            print("[3] Eliminar Valores Repetidos")
            print("[4] Filtrar Valores")
            print("[5] Desdoblar Valores")
            print("[6] valores Top N")
            print("[7] Valores Máximos y Mínimos")
            print("---------------------------")
            print("[0] Salir del programa")
            print("---------------------------")
            print()
            
            opcion = input("Seleccione una opción: ")
            if opcion in [str(i) for i in range(0, opciones + 1)]: # Sólo continua si se elije una opcion de menú válida
                break
            else:
                input("Opción inválida. Presione ENTER para volver a seleccionar.")
        print()

        if opcion == "0": # Opción salir del programa
            exit() # También puede ser sys.exit() para lo cual hay que importar el módulo sys

        elif opcion == "1":   # Opción 1
            
            print("[1] Generar valores\n")
            cantValores = input("Ingrese la cantidad de valores a generar: ")
            cantValores = validacionNumMayor2(cantValores)
            miLista = generarValores(cantValores,miLista)

            print(miLista)

            
         
        elif opcion == "2":   # Opción 2
            print("[2] Mostrar valores\n")
            mostrarValores(miLista, "VALORES DEL JUEGO DE DATOS (TODOS LOS DATOS)")
            ...
        elif opcion == "3":   # Opción 3
            print("[3] Eliminar valores repetidos\n")
            sinRep, contRepetidos = eliminarRepetidos(miLista)
            mostrarValores(sinRep, "VALORES DEL JUEGO DE DATOS (DATOS SIN REPETIDOS)")
            print (f"\nCANTIDAD DE REPETIDOS ELIMINADOS = {contRepetidos}")
            ...
        elif opcion == "4":   # Opción 4
            print("[4] Filtrar Valores\n")
            criterioFiltro(miLista)
        elif opcion == "5":   # Opción 5
            print("[5] Desdoblar Valores\n")
            desdoblarValores(miLista)
        elif opcion == "6":   # Opción 6
            listaTop, cont = eliminarRepetidos(miLista)
            valoresTop(listaTop)
        elif opcion == "7":   # Opción 7
            mostrarMaximosMinimos(miLista, f"VALORES MAXIMOS Y MINIMOS")


        input("\nPresione ENTER para volver al menú.")
        print("\n\n")


# Punto de entrada al programa
main()