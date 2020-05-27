"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad de Los Andes
 * 
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 """

import config as cf
import sys
import controller 
import csv
from ADT import list as lt
from ADT import stack as stk
from ADT import orderedmap as map
from DataStructures import listiterator as it

import sys


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""


def printMenu():
    print("Bienvenido al Proyecto Final")
    print("1- Cargar información")
    print("2- Rquerimiento 1 ")
    print("3- Requerimiento 2")
    print("4- Requerimiento 3")
    print("5- Requeimiento 4")
    print("0- Salir")


def initCatalog ():
    """
    Inicializa el catalogo
    """
    return controller.initCatalog()


def loadData (catalog):
    """
    Carga las bibliotecas en la estructura de datos
    """
    controller.loadData(catalog)


"""
Menu principal 
""" 
def main():
    while True: 
        printMenu()
        inputs =input("Seleccione una opción para continuar\n")
        if int(inputs[0])==1:
            print("Cargando información de los archivos ....")
            catalog = initCatalog ()
            loadData (catalog)
        elif int(inputs[0])==2:
            city=input("Digite la ciudad que desea buscar: ")
            controller.Requerimiento1(catalog, city)
        elif int(inputs[0])==3:
            date1=input("Digite la fecha de inicio que desea buscar: ")
            date2= input("Digite la fecha de finalización que desea buscar: ")
            controller.Requerimiento2(catalog, date1, date2)
        elif int(inputs[0])==4:
            n=input("Digite el N que desea buscar: ")
            controller.Requerimiento3(catalog, n)

        elif int(inputs[0])==5:
            vertices =input("Ingrese el vertice origen y destino\n")
            try:
                path = controller.getShortestPath(catalog,vertices)
                print("El camino de menor costo entre los vertices es:")
                totalDist = 0
                while not stk.isEmpty (path): 
                    step = stk.pop(path)
                    totalDist += step['weight']
                    print (step['vertexA'] + "-->" + step['vertexB'] + " costo: " + str(step['weight']))
                    print("Total: " + str (totalDist))
            except:
                print("No existe un camino entre los dos vértices")
            
        else:
            sys.exit(0)
    sys.exit(0)

if __name__ == "__main__":
    main()