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
import model
import csv
from ADT import list as lt
from ADT import map as map


from DataStructures import listiterator as it
from Sorting import mergesort as sort
from time import process_time


"""
El controlador se encarga de mediar entre la vista y el modelo.
"""


# Funcionaes utilitarias

def printList (lst):
    iterator = it.newIterator(lst)
    while  it.hasNext(iterator):
        element = it.next(iterator)
        result = "".join(str(key) + ": " + str(value) + ",  " for key, value in element.items())
        print (result)


# Funciones para la carga de datos 

def loadLibraries (catalog, sep=','):
    """
    Carga las bibliotecas del archivo.
    Por cada para de bibliotecas, se almacena la distancia en kilometros entre ellas.
    """
    t1_start = process_time() #tiempo inicial
    libsFile = cf.data_dir + 'GoodReads/libraries_edges.csv'
    dialect = csv.excel()
    dialect.delimiter=sep
    with open(libsFile, encoding="utf-8-sig") as csvfile:
        spamreader = csv.DictReader(csvfile, dialect=dialect)
        for row in spamreader:
            model.addLibraryNode (catalog, row)
            model.addLibraryEdge (catalog, row)
    t1_stop = process_time() #tiempo final
    print("Tiempo de ejecución carga de grafo de bibliotecas:",t1_stop-t1_start," segundos")   

def loadCities(catalog, sep=","):
    t1_start = process_time() #tiempo inicial
    BikeFile = cf.data_dir + 'bikes_data1/station.csv'
    dialect = csv.excel()
    dialect.delimiter=sep

    with open(BikeFile, encoding="utf-8-sig") as csvfile:
        spamreader= csv.DictReader(csvfile, dialect=dialect)
        for row in spamreader:
            AddCity(catalog, row)
    t1_stop = process_time() #tiempo final
    print("Tiempo de ejecución carga de la información fue: ",t1_stop-t1_start," segundos")   
def loadArbol(catalog, sep=","):
    t1_start = process_time() #tiempo inicial
    BikeFile = cf.data_dir + 'bikes_data/trip.csv'
    dialect = csv.excel()
    dialect.delimiter=sep

    with open(BikeFile, encoding="utf-8-sig") as csvfile:
        spamreader= csv.DictReader(csvfile, dialect=dialect)
        for row in spamreader:
            addTripDate(catalog, row)
    t1_stop = process_time() #tiempo final
    print("Tiempo de ejecución carga de la información del árbol : ",t1_stop-t1_start," segundos")

def loadWeather(catalog,sep= "," ):
    t1 = process_time() #tiempo inicial
    flightsfile = cf.data_dir + 'bikes_data1/weather.csv'
    dialect = csv.excel()
    dialect.delimiter=sep
    with open(flightsfile, encoding="utf-8-sig") as csvfile:
        spamreader = csv.DictReader(csvfile, dialect=dialect)
        for row in spamreader:
            addWeather(catalog, row)
    t2 = process_time() #tiempo final para vértices
    print("Tiempo de ejecución carga del archivo del clima fue :",t2-t1," segundos") 
def loadTrips (catalog, sep=';'):
    """
    Carga los vuelos del archivo.
    """
    t1 = process_time() #tiempo inicial
    flightsfile = cf.data_dir + 'tripxday_edges1/tripday_edges.csv'
    dialect = csv.excel()
    dialect.delimiter=sep
    with open(flightsfile, encoding="utf-8-sig") as csvfile:
        spamreader = csv.DictReader(csvfile, dialect=dialect)
        for row in spamreader:
            addTripNode(catalog, row)
    t2 = process_time() #tiempo final para vértices
    print("Tiempo de ejecución carga de vértices en el grafo de viajes:",t2-t1," segundos") 

    t3 = process_time() #tiempo inicial para arcos
    flightsfile = cf.data_dir + 'tripxday_edges1/tripday_edges.csv'
    dialect = csv.excel()
    dialect.delimiter=sep
    with open(flightsfile, encoding="utf-8-sig") as csvfile:
        spamreader = csv.DictReader(csvfile, dialect=dialect)
        for row in spamreader:
            addTripEdge(catalog, row)
    t4 = process_time() #tiempo final para carga de vértices y arcos
    print("Tiempo de ejecución carga de arcos en el grafo de viajes:",t4-t3," segundos")

    print("Tiempo de ejecución total para carga del grafo de viajes:",t4-t1," segundos")


def initCatalog ():
    """
    Llama la funcion de inicializacion del catalogo del modelo.
    """
    catalog = model.newCatalog()
    return catalog



def loadData (catalog):
    """
    Carga los datos de los archivos en la estructura de datos
    """
    #loadLibraries(catalog)
    loadCities(catalog)
    loadArbol(catalog)
    #loadTrips(catalog)
    #loadWeather(catalog)
    sort.mergesort(catalog["List"], comparemayor)

# Funciones llamadas desde la vista y enviadas al modelo


def countNodesEdges(catalog):
    t1_start = process_time() #tiempo inicial
    nodes, edges = model.countNodesEdges(catalog)
    t1_stop = process_time() #tiempo final
    print("Tiempo de ejecución de conteo de componentes conectados:",t1_stop-t1_start," segundos")
    return nodes, edges


def getShortestPath(catalog, vertices):
    t1_start = process_time() #tiempo inicial
    source=vertices.split(" ")[0]
    dst=vertices.split(" ")[1]
    path = model.getShortestPath(catalog, source, dst)
    t1_stop = process_time() #tiempo final
    print("Tiempo de ejecución de dijkstra: ",t1_stop-t1_start," segundos")
    return path

def addTripNode(catalog, row):
    return model.addTripNode(catalog, row)

def addTripEdge (catalog, row):
    return model.addTripEdge(catalog, row)

def addTripDate(catalog, row):
    return model.addTripDate(catalog, row)
def AddCity(catalog, row):
    return model.AddCity(catalog, row)
def addWeather(catalog, row):
    return model.addWeather(catalog, row)

def comparemayor (elem1, elem2):
    return ( float(elem1['value']) > float(elem2['value']))

def Requerimiento1(catalog, city):
    return printList( model.Requerimiento1(catalog, city)) 
def Requerimiento2(catalog, date1, date2):
    return model.Requerimiento2(catalog, date1, date2)
def Requerimiento3(catalog, N):
    return model.Requerimiento3(catalog, N)