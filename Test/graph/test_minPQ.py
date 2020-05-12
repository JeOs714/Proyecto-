import unittest
import config
from DataStructures import indexMinPQ as pq
from DataStructures import mapMinPQ as mapq



class GraphTest (unittest.TestCase):

    def setUp (self):
        pass

    def tearDown (self):
        pass

    def comparenames (self, searchname, element):
        return (searchname == element['key'])


    def greater (self, el1, el2):
        return el1 > el2


    def test_indexMinPQ (self):
        minPQ = pq.newIndexMinPQ(11,self.greater)
        pq.insert(minPQ, 5, 13)
        pq.insert(minPQ, 6, 14)
        pq.insert(minPQ, 7, 12)
        print(pq.delMin(minPQ))
        pq.insert(minPQ, 8, 11)
        pq.insert(minPQ, 9, 10)
        pq.decreasePriority(minPQ, 6, 10)
        print("minIdx",pq.minIndex(minPQ))
        while not pq.isEmpty(minPQ):
              print(pq.delMin(minPQ))


    def test_mapMinPQ (self):
        minPQ = mapq.newMapMinPQ(11,self.comparenames)
        mapq.insert(minPQ, '5', 13)
        mapq.insert(minPQ, '6', 14)
        mapq.insert(minPQ, '7', 12)
        print(mapq.delMin(minPQ))
        mapq.insert(minPQ, '8', 11)
        mapq.insert(minPQ, '9', 10)
        mapq.decreasePriority(minPQ, '6', 10)
        print("minIdx",mapq.minIndex(minPQ))
        while not mapq.isEmpty(minPQ):
              print(mapq.delMin(minPQ))



if __name__ == "__main__":
    unittest.main()
