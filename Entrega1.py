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
            print("Ingresar el valor ")
            




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
            criterioFiltro(miLista)
        elif opcion == "5":   # Opción 5
            desdoblarValores(miLista)
        elif opcion == "6":   # Opción 6
            ...
        elif opcion == "7":   # Opción 7
            ...

        input("\nPresione ENTER para volver al menú.")
        print("\n\n")


# Punto de entrada al programa
main()