from hash_table import HashTable
import config

config.initialize() #Access hashTableSize

class LinearProbingHashTable(HashTable):
    def __init__(self):
        self.size = config.hashTableSize
        self.table = [None] * self.size
        self.count = 0

    def insert(self,key,value):
        #Implement linear probing
        pass

    def remove(self, key):
        #Use "DELETED" marker
        pass

    def search(self,key):
        #Handle "DELETED" marker
        pass