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
from ADT import list as lt
from ADT import graph as g
from ADT import map as map
from ADT import list as lt
from ADT import orderedmap as tree
from DataStructures import listiterator as it
from datetime import datetime
from DataStructures import dijkstra as dj
from datetime import datetime
from Sorting import mergesort as mg
"""
Se define la estructura de un catálogo de libros.
El catálogo tendrá tres listas, una para libros, otra para autores 
y otra para géneros
"""

# Construccion de modelos

def newCatalog():
    """
    Inicializa el catálogo y retorna el catalogo inicializado.
    """
    Tripgraph = g.newGraph(325117 ,compareByKey,directed=True)
    Bikemap= map.newMap(numelements=50,maptype="PROBING",comparefunction=compareByKey)
    TripTree= tree.newMap()
    Stations=map.newMap(comparefunction=compareByKey)
    Lista=lt.newList("ARRAY_LIST")
    catalog = {'TripGraph':Tripgraph,  "BikesMap":Bikemap, "TripTree": TripTree, "Stations": Stations, "List":Lista}
    #rgraph = g.newGraph(5500,compareByKey)
    fgraph = g.newGraph(111353,compareByKey)
    #catalog['reviewGraph'] = rgraph
    catalog['flightGraph'] = fgraph
    return catalog

def NewCity(catalog, row):
    values={"stations": lt.newList("ARRAY_LIST"), "capacidadmax": lt.newList("ARRAY_LIST") }
    lt.addLast(values["stations"], row["name"]) 
    lt.addLast(values["capacidadmax"], {"ciudad":row["name"],"value": int(row["dock_count"])})
    #lt.addLast(values["capacidadmax"], (row["name"], row["dock_count"]) )
    map.put(catalog["BikesMap"], row["city"], values)  

def NewStation(catalog, row):
    values={"stations": lt.newList("ARRAY_LIST")}
    lt.addLast(values["stations"], row["city"]) 
    map.put(catalog["Stations"], row["id"], values) 

def newTripDate(catalog, row):
    formato= '%Y/%m/%d'
    trip = { "Date": strToDate(row["start_date"].split(" ")[0],formato), "City": None, "Citylist": None}
    trip["Citylist"]= lt.newList("ARRAY_LIST")
    trip["City"]= map.newMap(comparefunction=compareByKey)
    City= map.get(catalog["Stations"], row["start_station_id"])["value"]
    map.put(trip["City"], City["stations"]["elements"][0], 1)
    lt.addLast(trip['Citylist'],row['id'])
    return trip

def addWeather(catalog, row):
    formato= '%Y/%m/%d'
    lt.addLast(catalog["List"], {"Date":row["date"].split("-")[0]+row["date"].split("-")[1]+row["date"].split("-")[2], "value": row["mean_temperature_f"]} )

def addTripDate (catalog, row):
    """
    Adiciona libro al map con key=title
    """
    #catalog['booksTree'] = map.put(catalog['booksTree'], int(book['book_id']), book, greater)
    formato= '%Y/%m/%d'
    Trips= catalog['TripTree']
    Exist=tree.get(Trips,strToDate(row["start_date"].split(" ")[0],formato), greater)
    if Exist:
        lt.addLast(Exist['Citylist'],row['id'])
        City= map.get(catalog["Stations"], row["start_station_id"])
        Nuevovalor= map.get(Exist["City"], City["value"]["stations"]["elements"][0])
        if Nuevovalor:
            Nuevovalor["value"] +=1
            map.put(Exist["City"], City["value"]["stations"]["elements"][0], Nuevovalor["value"])
        else:
            map.put(Exist["City"], City["value"]["stations"]["elements"][0], 1)
        tree.put(catalog['TripTree'],strToDate(row["start_date"].split(" ")[0],formato),Exist, greater)    
        #director['sum_average_rating'] += float(row['vote_average'])
       
    else:
        Trip= newTripDate(catalog, row)
        catalog['TripTree']  = tree.put(Trips , Trip["Date"], Trip, greater)
        #tree.put(Accidents, Accident['Date'], Accident, greater)

def AddCity(catalog, row):
    city= map.get(catalog["BikesMap"], row["city"])
    station= map.get(catalog["BikesMap"], row["name"])
    if not city:
        NewCity(catalog, row)
    else: 
        lt.addLast(city["value"]["stations"], row["name"]) 
        lt.addLast(city["value"]["capacidadmax"], {"ciudad":row["name"],"value": int(row["dock_count"])})
        mg.mergesort(city["value"]["capacidadmax"], comparemayor)
    if not station:
        NewStation(catalog, row)
    else: 
        lt.addLast(city["value"]["stations"], row["city"]) 



def addLibraryNode (catalog, row):
    """
    Adiciona un nodo para almacenar una biblioteca
    """
    if not g.containsVertex(catalog['librariesGraph'], row['ID_src']):
        g.insertVertex (catalog['librariesGraph'], row['ID_src'])
    if not g.containsVertex(catalog['librariesGraph'], row['ID_dst']):
        g.insertVertex (catalog['librariesGraph'], row['ID_dst'])

def addLibraryEdge  (catalog, row):
    """
    Adiciona un enlace entre bibliotecas
    """
    g.addEdge (catalog['librariesGraph'], row['ID_src'], row['ID_dst'], float(row['dist']))

def addTripNode(catalog, row):
    """
    Adiciona un nodo para almacenar un vuelo. 
    """
    if not g.containsVertex(catalog['TripGraph'], row['src']):
        g.insertVertex (catalog['TripGraph'], row['src'])

def addTripEdge (catalog, row):
    """
    Adiciona un enlace para conectar dos vuelos
    """
    g.addEdge (catalog['TripGraph'], row['src'], row['dst'], float(row['duration']))

def Requerimiento1(catalog, city):
    Map=catalog["BikesMap"]
    cities= map.get(Map, city)
    i= 0
    resul= lt.newList("ARRAY_LIST")
    while i < 3:
        lt.addLast(resul, cities["value"]["capacidadmax"]["elements"][i] )
        i+=1
    return resul 
def Requerimiento2(catalog, date1, date2):
    formato= '%Y/%m/%d'
    Map=catalog["TripTree"]
    cities= tree.valueRange(Map, strToDate(date1,formato),strToDate(date2,formato) , greater)
    resul= lt.newList("ARRAY_LIST")
    contador= 0
    res=""
    ciudades= map.newMap(comparefunction=compareByKey)
    if cities:
        for Año in cities["elements"]:
            Ci= map.keySet(Año["City"])
            iterator=it.newIterator(Ci)
            contador+= lt.size(Año["Citylist"])
            while it.hasNext(iterator):
                SevKey = it.next(iterator)
                Valor = map.get(Año["City"],SevKey)
                Está= map.get(ciudades, SevKey)
                if Está:       
                    Está["value"]["value"] +=Valor["value"]
                    map.put(ciudades,SevKey, Está)
                else:
                    map.put(ciudades, SevKey, Valor)
        res+= HacerRespuesta(ciudades)
        res+= "El total de viajes entre las fechas " + str(date1) + " y " + str(date2)+ " fue "+ str(contador)+ "\n"
    return res
def Requerimiento22(catalog, date1, date2):
    formato= '%Y/%m/%d'
    Map=catalog["TripTree"]
    cities= tree.valueRange(Map, date1, date2, greater)
    resul= lt.newList("ARRAY_LIST")
    contador= 0
    res=""
    ciudades= map.newMap(comparefunction=compareByKey)
    if cities:
        for Año in cities["elements"]:
            Ci= map.keySet(Año["City"])
            iterator=it.newIterator(Ci)
            contador+= lt.size(Año["Citylist"])
            while it.hasNext(iterator):
                SevKey = it.next(iterator)
                Valor = map.get(Año["City"],SevKey)
                Está= map.get(ciudades, SevKey)
                if Está:       
                    Está["value"]["value"] +=Valor["value"]
                    map.put(ciudades,SevKey, Está)
                else:
                    map.put(ciudades, SevKey, Valor)
        res+= HacerRespuesta1(ciudades)
        res+= "El total de viajes entre las fechas " + str(date1) + " y " + str(date2)+ " fue "+ str(contador)+ "\n"
    return res
def Requerimiento3(catalog, N):
    Map=catalog["List"]
    Tree=catalog["TripTree"]
    lista= lt.newList("ARRAY_LIST")
    res=""

    for i in range(0, N):
        lt.addLast(lista, Map["elements"][i])
    for i in range(lt.size(lista)-N-1, lt.size(lista)):
        lt.addLast(lista, Map["elements"][i])

    for i in lista["elements"]: 
        res+= "Día: "+ str(i["Date"])
        res+="Temperatura promedio: "+ str(i["value"])
        res+= Requerimiento22(catalog, i["Date"], i["Date"])
    
    return res
         


    
def HacerRespuesta(Dic):
    res=""
    Severidades= map.keySet(Dic)
    iterator=it.newIterator(Severidades)
    while it.hasNext(iterator):
        SevKey = it.next(iterator)
        res += 'Ciudad '+ SevKey + ' : ' + str(map.get(Dic,SevKey)["value"]["value"]["value"] ) + '\n'
    return res

def HacerRespuesta1(Dic):
    res=""
    Severidades= map.keySet(Dic)
    iterator=it.newIterator(Severidades)
    while it.hasNext(iterator):
        SevKey = it.next(iterator)
        res += 'Ciudad '+ SevKey + ' : ' + str(map.get(Dic,SevKey) ) + '\n'
    return res
def getShortestPath (catalog, source, dst):
    """
    Retorna el camino de menor costo entre vertice origen y destino, si existe 
    """
    print("vertices: ",source,", ",dst)

    dijkstra= dj.newDijkstra(catalog['TripGraph'], source)

    Path= dj.pathTo(dijkstra, dst)
    # ejecutar Dijkstra desde source
    # obtener el camino hasta dst
    # retornar el camino
    return Path
    
# Funciones de comparacion

def compareByKey (key, element):
    return  (key == element['key'] )  

def comparemayor (elem1, elem2):
    return ( float(elem1['value']) > float(elem2['value']))


def greater (key1, key2):
    if ( key1 == key2):
        return 0
    elif (key1 < key2):
        return -1
    else:
        return 1

def strToDate(date_string, format):

    nume= date_string.split("/")
    res=""
    if len(nume[0])<2 and len(nume[1])<2:
        res= nume[2]+"0"+nume[0]+"0"+nume[1]
    elif len(nume[0])<2:
        res= nume[2]+"0"+nume[0]+nume[1]
    elif len(nume[1])<2:
        res= nume[2]+nume[0]+"0"+nume[1]
    else:
        res= nume[2]+nume[0]+nume[1]

    return res
    """
    formato= '%Y/%m/%d %H:%M:%S'
    try:
        # date_string = '2016/05/18 13:55:26' -> format = '%Y/%m/%d %H:%M:%S')
        return datetime.strptime(date_string,formato)
    except:
        return datetime.strptime('1900', '%Y')
    """