"""
-----------------------------------------------------------------------------------------------
Título: Entrega 1
Fecha: 11 de mayo
Autor:  Jonathan Lucas Cáceres
        Tomas Villamil
        Francisco Pasta
        Santino Godoy
        Tomas Biglia

Descripción: Entrega del programa 

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
def titular (mensaje):
    '''
    -Imprime un titulo para los encabezados de las opciones
    
    -Parametros:
        mensaje (str): Mensaje que se desea aplicar el formato
    -Retorno:
        (print) Mensaje en formato de encabezado
    '''
    print("=" * 90)
    print(mensaje.center(90))
    print("=" * 90)
    print()

def validarNumero(num):
    '''
    -Valida que el dato ingresado pueda ser convertido en un entero

    -Parametros:
        num (str): Valor a verificar
    -Retorno:
        (int) : valor ingresado convertido en (int)
    '''
    while True:
        if not num.isdigit():
            print("Entrada no valida. Por favor ingrese un número entero")
        else:
            return int(num)
        num = input("   Tiene que ser un número entero: ")

def validarSiNo(opcion): #Valida que la entrada sea S, N, True o False con sus variantes
    '''
    -Valida que el valor ingresado por el usuario (Si o No) en sus variantes sea reconocido como True or False

    -Paramtros:
        opcion (str): valor a verificar
    -Rertorno:
        (bool) : True si ingreso S o sus variantes / False caso contrario
    '''
    while True:
        if opcion not in ["S", "N", "n", "s", "True", "False"]:
            print("Valor no válido. Ingrese S o N.")
        elif opcion in ["S", "s", "True"]:
            return True
        elif opcion in ["N", "n", "False"]:
            return False
        opcion = input("¿Desea generar una nueva lista? (S/N): ")

def validacionNumMayor2(num):
    '''
    -Valida que el dato ingresado pueda ser convertido en un entero y mayor a 2

    -Parametros:
        num (str): Valor a verificar entero y mayor a dos
    -Retorno:
        (int) : valor ingresado convertido en (int)
    '''
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
    '''
    Asigna a la lista valores de 1,3,5 digitos de forma aleatoria con igual probabilidad de ocurrencia
    Tres valores al azar: el primero de 1 digido, el segundo de 3 digitos y el tercero de 5 digitos
    Elije uno de los 3 al azar y lo agrega a la lista
    Repite hasta que el tamaño de la lista deje de ser menor que la cantidad de valores deseada

    -Parametros: 
        lista (list): Lista a la cual se le agregaran los valores
        canValores (int): Cantidad de valores que se le agregara a la lista
    -Retorno:
        (None): Agrega los valores a la lista 
    '''
    while len(lista) < cantValores:

        valor1 = random.randint(0, 9) 
        valor2 = random.randint(100, 999)
        valor3 = random.randint(10000,99999)
        valores = valor1, valor2, valor3
        valor = random.choice(valores)
        lista.append(valor) # Agrega el valor a la lista

def generarValores(cantValores,lista):
    ''' 
    -Si ya existia una lista generada anteriormente, informa y solicita confirmacion antes de reemplazarla.
    Y si es la primera vez, genera los valores de la lista, usa la funcion anterior listarRandom()

    -Parametros:
        cantValores (int): Cantidad de valores a agregar a la lista
        lista (list): Lista a evaluar si ya existia o no, y que sera modificada
    -Retorno:
        (list): lista modificada o no segun eleccion
        (print): En el caso de Error, o si no se elige modificar una lista ya creada
    '''
    if lista:
        eleccion =validarSiNo(input("Lista ya creada anteriormente, desea generar una nueva lista? (S/N): "))
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
        if lista: print("Lista creada correctamente.")
        else: print("ERROR al crear la lista")

    return lista

#   TAREA 2
Letras=["A","B","C","D","E","F","G","H","I","J"]

def mostrarValores(miLista, titulo):
    '''
    -Presenta los valores en formato de tabla encolumnada y cerrada, con 10 valores por fila, repetando el formato de la consigna

    -Parametros:
        miLista (list): Lista a dar formato
        titulo (str): Mensaje personalisado para usarlo en otros puntos
    -Retorno:
        (print): Imprime la tabla en formato de la consigna
    '''
    filas=0

    if len(miLista) == 0: #Cambiar segun funcion 1
        print("No hay valores generados.")
    else:

        print("*" * 90)
        print(f"VALORES DEL JUEGO DE DATOS ({titulo})")
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
    '''
    - Genera y muestra una nueva lista a partir de la original, eliminando los valores duplicados
    conservando el orden de primera aparición de cada valor, informando tambien cuantos valores fueron eliminados

    -Parametros:
        lista (list): Lista a eliminar valores repetidos
    -Retorno:
        (list) resultado: lista nueva sin los valores repetidos
        (int) contadorRepetidos: Cantidad de valores repetidos y eliminados
    '''
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
    '''
    -Realiza un filtrado segun criterio seleccionado por el usuario: "mayores que", "menores que", "en Rango", "pares", "impares"

    -Parametros:
        miLista (list): Lista que se toma de referencia para realizar los criterios de filtrado
    -Retorno:
        (list) listaResultado = Lista filtrada segun criterio
        (str) mensaje = Mensaje personalizado segun criterio elegido
    '''

    lista = miLista[:]
    listaResultado = []
    if len(lista) == 0:
        return [], "SIN DATOS"
    criterio = input("Ingrese el criterio de filtrado [M=Mayores que | E=Menores que | R=En rango | P=Pares | I=Impares]: ")
    criterio = criterio.upper()
    while criterio != "M" and criterio != "E" and criterio != "R" and criterio != "P" and criterio != "I":
        print("Error! criterio incorrecto")
        criterio = input("Ingrese el criterio de filtrado [M=Mayores que | E=Menores que | R=En rango | P=Pares | I=Impares]: ")
        criterio = criterio.upper()
    
    if criterio == "M":
        num = validarNumero(input("Criterio de filtrado: Mayores que: "))
        for valor in lista:
            if valor > num:
                listaResultado.append(valor)
        mensaje = f"MAYORES QUE {num}"
        return listaResultado, mensaje

    elif criterio == "E":
        num = validarNumero(input("Criterio de filtrado: Menores que:  "))
        for valor in lista:
            if valor < num:
                listaResultado.append(valor)
        mensaje = f"MENORES QUE {num}"
        return listaResultado, mensaje
    elif criterio == "R":
        desde = validarNumero(input("Criterio de filtrado: En rango \nIngrese el limite inferior: "))
        hasta = validarNumero(input("Ingrese el limite superior: "))
        while hasta < desde:
            print("El limite superior debe ser mayor")
            hasta = validarNumero(input("Ingrese nuevamente un limite superior: "))
        for valor in lista:
            if valor >= desde and valor <= hasta:
                listaResultado.append(valor)
        mensaje = f"VALORES ENTRE {desde} y {hasta}"
        return listaResultado, mensaje 
    
    elif criterio == "P":
        for valor in lista:
            if valor % 2 == 0:
                listaResultado.append(valor)
        mensaje = f"VALORES PARES"
        return listaResultado, mensaje
    elif criterio == "I":
        for valor in lista:
            if valor % 2 == 1:
                listaResultado.append(valor)
        mensaje = f"VALORES IMPARES"
        return listaResultado, mensaje
    
#   TAREA 5 DESDOBLAR VALORES
def desdoblarValores(miLista):
    """
    Función que a partir de la lista ingresada, pregunta al usuario mediante qué criterios quiere desdoblarla
    Valida la entrada del usuario y crea varias listas a partir de la original según el criterio elegido
    retorna las listas segun criterio seleccionado

    -Parametros: 
        miLista (list): Lista que se toma de referencia para realizar los criterios de desdoblamiento de listas
    -Retorno:
        (list): Lista de listas desdobladas segun criterio 
        (list): Lista con mensajes personalizados para cada listas de las primera
    """
    lista = miLista[:]
    lista1 = []
    lista2 = []
    lista3 = []

    if len(lista) == 0:
        return [], []
       
    criterio = input("Ingrese el criterio de desdoblamiento [P=Pares/Impares | C=Por cantidad de cifras | U=Por valor umbral]: ")
    criterio = criterio.upper()
    while criterio != "P" and criterio != "C" and criterio != "U":  #criterio not in ["P,"C","U"]
        print("Valor inválido ingresado, intente de nuevo")
        criterio = input("Ingrese el criterio de desdoblamiento [P=Pares/Impares | C=Por cantidad de cifras | U=Por valor umbral]: ")
        criterio = criterio.upper()
        
    #Validación del umbral
    if criterio == "U":
        umbral = (input("Elija el valor umbral para desdoblar las listas: "))
        while not umbral.isdigit() or int(umbral) <= 0:
            print("Valor inválido, intente de nuevo")
            umbral = (input("Elija el valor umbral para desdoblar las listas: "))
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
        return [lista1, lista2], ["PARES", "IMPARES"]
    
    #Separación de listas por umbral
    elif criterio == "U":
        pos = 0
        while pos < len(lista):
            if (lista[pos]) > umbral:
                lista1.append(lista[pos])
            pos = pos + 1
        pos = 0
        while pos < len(lista):
            if (lista[pos]) <= umbral:
                lista2.append(lista[pos])
            pos = pos + 1
        return [lista2, lista1], [f"VALORES HASTA {umbral}", f"MAYORES QUE {umbral}"]        
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
        return [lista1, lista2, lista3], ["UNA CIFRA", "TRES CIFRAS", "CINCO CIFRAS"]        
#   TAREA 6 VALORES TOP N
def valoresTop(miLista):
    '''
    -Presenta un ranking de los N valores mas altos unicos de la lista.
    N es la cantidad de valores a rankear, validado para que no sea mayor a la lista sin repetidos

    -Parametros:
        miLista (list): Lista a la cual se le eliminaran los repetidos y se rankeara
    -Retorno:
        (None): Imprime la lista rankeada de N valores
    '''
    listaTop = miLista[:]
    listaTop, cant = eliminarRepetidos(listaTop)
    ranking = []
    if len(listaTop) == 0:
        print("No hay valores generados. Use la opción [1] primero.")
        return
    
    n = validarNumero(input("Ingrese la cantidad N para el ranking (top N): "))
    if n > len(listaTop):
        n = len(listaTop)
        print(f"Hay menos valores únicos que N. Se muestran los {n} disponibles.")

    for cont in range(0, n):
        aux = 0
        for elem in listaTop:
            if elem > aux:
                aux = elem
        ranking.append(aux)
        for i, elem in enumerate(listaTop):
            if aux == elem:
                del listaTop[i]

    separador = "*" * 90
    print()
    print(separador)
    print("VALORES DEL JUEGO DE DATOS (DATOS TOP N)")
    print(separador)

    for i, elem in enumerate(ranking):
        print (f"{i+1}- {elem}")

    fecha_hora = time.strftime("%d-%m-%Y %H:%M:%S")
    print("FIN DEL LISTADO (" + fecha_hora + ") " + "*" * 51)

#      TAREA 7 MAXIMOS Y MINIMOS
def Valores_Maximos_Y_Minimos(miLista):
    '''
    -Encuentra los valores maximo y minimo de la lista

    -Parametro:
        miLista (list): lista donde se busca los valores maximo y minimo
    -Retorno:
        (float) maximo: el maximo de la lista
        (float) minimo: el minimo de la lista
    '''
    maximo = float("-inf")
    minimo = float("+inf") 
    
    for numero in miLista:
        if numero > maximo: 
            maximo = numero 

        if numero<minimo:
            minimo=numero

    return maximo,minimo
    

def mostrarMaximosMinimos(miLista,titulo):
    '''
    -Identifica el valor maximo y minimo de la lista y los destaca segun [max] (min) <igual>
    y los imprime en formato tabla del punto 2

    -Parametros:
        miLista (list): lista de la cual se identifica los valores solicitados
        titulo (str): Titulo personalizado que detalla VALORES MAXIMOS Y MINIMOS
    -Retorno:
        (None): Imprime en formato tabla destacando los valores solicitados
    '''
    filas = 0

    if len(miLista) == 0: #Cambiar segun funcion 1
        print("No hay valores generados.")
    else:

        print("*" * 90)
        print(F"VALORES DEL JUEGO DE DATOS ({titulo})")
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
            print("[6] Valores Top N")
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
            titular("[1] Generar valores")
            cantValores = input("Ingrese la cantidad de valores a generar: ")
            cantValores = validacionNumMayor2(cantValores)
            miLista = generarValores(cantValores,miLista)
            
         
        elif opcion == "2":   # Opción 2
            titular("[2] Mostrar valores")
            mostrarValores(miLista, "TODOS LOS DATOS")

        elif opcion == "3":   # Opción 3
            titular("[3] Eliminar valores repetidos")
            sinRep, contRepetidos = eliminarRepetidos(miLista)
            mostrarValores(sinRep, "DATOS SIN REPETIDOS")
            print (f"\nCANTIDAD DE REPETIDOS ELIMINADOS = {contRepetidos}")

        elif opcion == "4":   # Opción 4
            titular("[4] Filtrar Valores")
            listaFiltrada, mensaje = criterioFiltro(miLista)
            print()
            mostrarValores(listaFiltrada, mensaje)
        elif opcion == "5":   # Opción 5
            titular("[5] Desdoblar Valores")
            listas, mensajes = desdoblarValores(miLista)
            print()
            if len(listas) == 0:
                mostrarValores(listas, mensajes)
            else:
                for i, lista in enumerate(listas):
                    mensaje = mensajes[i]
                    mostrarValores(lista, mensaje)
                    print()

        elif opcion == "6":   # Opción 6
            titular("[6] Valores TOP N")
            listaTop, cont = eliminarRepetidos(miLista)
            valoresTop(listaTop)

        elif opcion == "7":   # Opción 7
            titular("[7] Valores máximos y mínimos")
            mostrarMaximosMinimos(miLista, f"DATOS MÁXIMOS Y MÍNIMOS [máx] (mín) <máx/mín>")


        input("\nPresione ENTER para volver al menú.")
        print("\n\n")


# Punto de entrada al programa
main()