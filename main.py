from os import sep
from tkinter import Tk
from tkinter.filedialog import askopenfilename
import msvcrt
import webbrowser


global lista_con_ordenes
global titulo, num_a_buscar, resultado_busqueda, lista_ordenadas__enteros


lista_numeros_int = []
lista_ordenadas__enteros = []
resultado_busqueda = 0
num_a_buscar = 0
lista_con_ordenes = []
contador_ordenar = []
lista_numeros_sin_ordenar = []
identificador_ordenar = 0
titulo = []
nombre = []
numeros = []
lista_numeros = []
cadena = []
orden = []



def crearReporte():

    f = open('Reporte.html', 'w')
    f.write('<!DOCTYPE HTML>\n')
    f.write('<html>\n')
    f.write('<head>\n')
    f.write('<title>Reporte Practica Uno</title>\n')
    f.write('<meta charset="utf-8" />\n')
    f.write('<meta name="viewport" content="width=device-width, initial-scale=1" />\n')
    f.write('<link rel="stylesheet" href="assets/css/main.css" />\n')
    f.write('</head>\n')
    f.write('<body>\n')
    f.write('<header id="header">\n')
    f.write('<div class="inner">\n')
    f.write('<a href="Reporte.html" class="logo">Lenguajes Formales y de Programacion</a>\n')
    f.write('<nav id="nav">\n')
    f.write('<a href="Reporte.html">Inicio</a>\n')
    f.write('</nav>\n')
    f.write('<a href="#navPanel" class="navPanelToggle"><span class="fa fa-bars"></span></a>\n')
    f.write('</div>\n')
    f.write('</header>\n')
    #BANER
    f.write('<section id="banner">\n')
    f.write('<h1>Reporte Practica Uno</h1>\n')
    f.write('<p>Curso: Lenguajes Formales y de Programacion.</p>\n')
    f.write('</section>\n')
    #SECCIÓN
    f.write('<section id="one" class="wrapper">\n')
    f.write('<div class="inner">\n')
    f.write('<header class="align-center">\n')

    f.write('<h3>Los datos generados son:</h3>\n')
    f.write('<pre><code>\n')
    contador = 0
    for i in lista_con_ordenes:
        lista_numeros[contador] = list(map(int, lista_numeros[contador]))
        if 'ORDENAR' in i:
            f.write(str('{}: {} | Resultado de ordenar: {}'.format(titulo[contador], lista_numeros_sin_ordenar[contador], lista_numeros[contador]) + '\n'))
        contador += 1

    contador_busquedas = 0

    for i in lista_con_ordenes:
        if 'BUSCAR' in i:
            for j in i:
                if j.isdigit():
                    num_a_buscar = j
                    lista_para_ordenar = []
                    indice = []
                    for i in range(len(lista_numeros_sin_ordenar[contador_busquedas])):
                            if lista_numeros_sin_ordenar[contador_busquedas][i] == num_a_buscar:
                                indice.append(i + 1)
                    if indice:
                        f.write(str('{}: {} | valor buscado: {} | encontrado en: {}'.format(titulo[contador_busquedas], 
                        lista_numeros_sin_ordenar[contador_busquedas], num_a_buscar, indice)) + '\n')
                    else:
                        f.write(str('{}: {} | valor buscado: {} | No encontrado'.format(titulo[contador_busquedas], 
                        lista_numeros_sin_ordenar[contador_busquedas], num_a_buscar)) + '\n')
        contador_busquedas += 1
    f.write('</code></pre>\n')
    f.write('</header>\n')
    #FOOTER
    f.write('<footer id="footer">\n')
    f.write('<div class="inner">\n')
    f.write('<div class="flex">\n')
    f.write('<div class="copyright">\n')
    f.write('&copy; Rodrigo Antonio Poron De Leon | Laboratorio LFP\n')
    f.write('</div>\n')
    f.write('</div>\n')
    f.write('</div>\n')
    f.write('</footer>\n')
    #SCRIPTS
    f.write('<script src="assets/js/jquery.min.js"></script>\n')
    f.write('<script src="assets/js/skel.min.js"></script>\n')
    f.write('<script src="assets/js/util.js"></script>\n')
    f.write('<script src="assets/js/main.js"></script>\n')
    f.write('</body>\n')
    f.write('</html>\n')
    
    f.close()
    webbrowser.open_new_tab('Reporte.html')

def verificarNumero():
 
    correcto = False
    num = 0
    while(not correcto):
        try:
            num = int(input("Seleccione una opción: "))
            correcto=True
        except ValueError:
            print('Error, introduce un numero entero')
     
    return num

def ordenamientoBurbuja(unaLista):
    for numPasada in range(len(unaLista)-1,0,-1):
        for i in range(numPasada):
            if unaLista[i]>unaLista[i+1]:
                temp = unaLista[i]
                unaLista[i] = unaLista[i+1]
                unaLista[i+1] = temp
 

def leerArchivo():
    print ("Cargar archivo de entrada")
    root = Tk()
    root.withdraw()
    root.update()
    root.attributes("-topmost", True)
    pathString = askopenfilename(filetypes=[("Text files","*.txt")])
    return pathString

 
salir = False
opcion = 0
 
while not salir:
 
    print ("1. Cargar archivo de entrada")
    print ("2. Desplegar listas ordenadas")
    print ("3. Desplegar búsquedas")
    print ("4. Desplegar todas")
    print ("5. Desplegar HTML")
    print ("6. Salir")
 
    opcion = verificarNumero()


    
    if opcion == 1:

        ruta = leerArchivo()
        archivo = open(ruta, "r")
        contador_split = 0
        for linea in archivo.readlines():
            lista_numeros_int = []
            nombre = linea.split('=')
            titulo.append(nombre[0])
            numeros = nombre[1].split(' ')
            
            lista_unica = numeros[0].split(',')
            
            for num in lista_unica:
                a = int(num)
                lista_numeros_int.append(a)
            
            print(lista_numeros_int)
            lista_numeros.append(lista_numeros_int)
            lista_numeros_sin_ordenar.append(numeros[0].split(','))
            numeros[len(cadena) - 1] = numeros[len(cadena) - 1].rstrip('\n')
            orden = ",".join(numeros[1:]).split(',')
            lista_con_ordenes.append(orden)
            ordenamientoBurbuja(lista_numeros[contador_split])
            contador_split += 1
                

    elif opcion == 2:
        print ("Desplegar listas ordenadas:")

        contador = 0
        

        for i in lista_con_ordenes:
            lista_numeros[contador] = list(map(int, lista_numeros[contador]))
            if 'ORDENAR' in i:
                print('{}: {} | Resultado de ordenar: {}'.format(titulo[contador], lista_numeros_sin_ordenar[contador], lista_numeros[contador]))
            contador += 1


    elif opcion == 3:
        print("Desplegar búsquedas:")
        contador_busquedas = 0

        for i in lista_con_ordenes:
            if 'BUSCAR' in i:
                for j in i:
                    if j.isdigit():
                        num_a_buscar = j
                        lista_para_ordenar = []
                        indice = []
                        #indice = [x for x, k in enumerate(lista_numeros_sin_ordenar[contador]) if k == num_a_buscar]
                        for i in range(len(lista_numeros_sin_ordenar[contador_busquedas])):
                            if lista_numeros_sin_ordenar[contador_busquedas][i] == num_a_buscar:
                                indice.append(i + 1)
                        if indice:
                            print('{}: {} | valor buscado: {} | encontrado en: {}'.format(titulo[contador_busquedas], 
                            lista_numeros_sin_ordenar[contador_busquedas], num_a_buscar, indice))
                        else:
                            print('{}: {} | valor buscado: {} | No encontrado'.format(titulo[contador_busquedas], 
                            lista_numeros_sin_ordenar[contador_busquedas], num_a_buscar))
            contador_busquedas += 1


    elif opcion == 4:
        print('Desplegar todas:')
        contador = 0
        for i in lista_con_ordenes:
            lista_numeros[contador] = list(map(int, lista_numeros[contador]))
            if 'ORDENAR' in i:
                print('{}: {} | Resultado de ordenar: {}'.format(titulo[contador], lista_numeros_sin_ordenar[contador], lista_numeros[contador]))
            contador += 1

        contador_busquedas = 0

        for i in lista_con_ordenes:
            if 'BUSCAR' in i:
                for j in i:
                    if j.isdigit():
                        num_a_buscar = j
                        lista_para_ordenar = []
                        indice = []
                        #indice = [x for x, k in enumerate(lista_numeros_sin_ordenar[contador]) if k == num_a_buscar]
                        for i in range(len(lista_numeros_sin_ordenar[contador_busquedas])):
                            if lista_numeros_sin_ordenar[contador_busquedas][i] == num_a_buscar:
                                indice.append(i + 1)
                        if indice:
                            print('{}: {} | valor buscado: {} | encontrado en: {}'.format(titulo[contador_busquedas], 
                            lista_numeros_sin_ordenar[contador_busquedas], num_a_buscar, indice))
                        else:
                            print('{}: {} | valor buscado: {} | No encontrado'.format(titulo[contador_busquedas], 
                            lista_numeros_sin_ordenar[contador_busquedas], num_a_buscar))
            contador_busquedas += 1
        

    elif opcion == 5:
        crearReporte()
    elif opcion == 6:
        print("201902781")
        print("Rodrigo Antonio Porón De León")
        print("rodriporon2@gmail.com")
        print("Lenguajes Formales y de Programación")
        msvcrt.getch()
        salir = True
    else:
        print ("Introduzca un numero entre 1 y 6")



