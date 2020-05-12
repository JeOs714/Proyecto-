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

"""
Estructura que contiene la información de una cola de prioridad indexada, orientada a menor
"""

def newIndexMinPQ (capacity, cmpFunction):
  
  priorities = [0]*(capacity+1)
  pq = [0]*(capacity+1)
  qp = [-1]*(capacity+1)
  minPQ = {'priorities':priorities, 'pq':pq, 'qp':qp, 'maxCapacity':capacity,'size':0, 'cmpFunction':cmpFunction}

  return minPQ


def isEmpty(minPQ):
    return minPQ['size'] == 0

def contains(minPQ, i):
    return minPQ['qp'][i] != -1

def size(minPQ):
    return minPQ['size']

def minIndex(minPQ):
    return minPQ['pq'][1]

def minPriority(minPQ):
    minIdx=minPQ['pq'][1]
    return minPQ['priorities'][minIdx]

def delMin(minPQ):
    minIdx = minPQ['pq'][1]
    n = minPQ['size']
    exch(minPQ, 1, n)
    minPQ['size'] = n-1
    sink(minPQ, 1)
    minPQ['qp'][minIdx] = -1            # delete
    minPQ['priorities'][minIdx] = None  # to help with garbage collection
    minPQ['pq'][n] = -1                 # not needed
    return minIdx
    

def decreasePriority(minPQ, i, priority):
    minPQ['priorities'][i] = priority
    swim(minPQ, minPQ['qp'][i])

def increasePriority(minPQ, i, priority):
    minPQ['priorities'][i] = priority
    sink(minPQ, minPQ['qp'][i])


def exch(minPQ, i, j):
    swap = minPQ['pq'][i]
    minPQ['pq'][i] = minPQ['pq'][j]
    minPQ['pq'][j] = swap
    minPQ['qp'][minPQ['pq'][i]] = i
    minPQ['qp'][minPQ['pq'][j]] = j


def insert(minPQ, i, priority):
    if contains(minPQ, i):
        raise Exception('index is already in the priority queue')
    n = minPQ['size']+1
    minPQ['size']=n
    minPQ['qp'][i] = n
    minPQ['pq'][n] = i
    minPQ['priorities'][i] = priority
    swim(minPQ, n)


def greater(minPQ, i, j):
    i_element = minPQ['priorities'][minPQ['pq'][i]]
    j_element = minPQ['priorities'][minPQ['pq'][j]]
    cmpFunction = minPQ['cmpFunction']
    return cmpFunction(i_element, j_element) > 0


def swim(minPQ , k):
    while k > 1 and greater(minPQ, int(k/2), k):
        exch(minPQ, k, int(k/2))
        k = int(k/2)
    

def sink(minPQ, k):
    n = minPQ['size']
    while 2*k <= n:
        j = 2*k
        if j < n and greater(minPQ, j, j+1):
            j+=1
        if not greater(minPQ, k, j):
            break
        exch(minPQ, k, j)
        k = j