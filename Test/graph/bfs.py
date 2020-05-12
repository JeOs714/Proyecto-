import config
import math
from DataStructures import adjlist as g
from DataStructures import listiterator as it
from ADT import queue as q
from ADT import map as map
from DataStructures import edge as e
from ADT import stack as stk
from ADT import list as lt


def bfs (search, source):
    queue = q.newQueue()
    q.enqueue(queue, source)
    while not (q.isEmpty(queue)):
        v = q.dequeue (queue)
        visited_v = map.get(search['visitedMap'], v)['value']
        # Loop v's adjacent vertices with w
        # If w has not visited 
        # Visit w 
        # Enqueue w

def hasPathTo(search, v):
    # Has v been visited?
    return False



def pathTo(search, v):
    if hasPathTo(search, v)==False:
        return None
    path= stk.newStack()
    # Loop through previous vertices (edgeTo) until source vertex:
    # Add each previous vertex to the path
    # At the end of the loop, add the source vertex to the path
    return path



# Function to return the smallest  
# prime number greater than N 
# # This code is contributed by Sanjit_Prasad  

def isPrime(n): 
      
    # Corner cases  
    if(n <= 1): 
        return False
    if(n <= 3): 
        return True
      
    # This is checked so that we can skip  
    # middle five numbers in below loop  
    if(n % 2 == 0 or n % 3 == 0): 
        return False
      
    for i in range(5,int(math.sqrt(n) + 1), 6):  
        if(n % i == 0 or n % (i + 2) == 0): 
            return False
      
    return True

def nextPrime(N): 
  
    # Base case  
    if (N <= 1): 
        return 2
  
    prime = N 
    found = False
  
    # Loop continuously until isPrime returns  
    # True for a number greater than n  
    while(not found): 
        prime = prime + 1
  
        if(isPrime(prime) == True): 
            found = True
  
    return prime 


def comparenames (searchname, element):
    return (searchname == element['key'])