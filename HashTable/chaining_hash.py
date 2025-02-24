from hash_table import HashTable
import config

config.initialize() #Access hashTableSize

class ChainingHashTable(HashTable):
    def __init__(self):
        self.size = config.hashTableSize
        self.table = [None] * self.size
        self.count = 0

    def insert(self,key,value):
        #Implement Chaining
        pass

    def remove(self, key):
        #Return ture if removed
        pass

    def search(self,key):
        #Return airport if found
        pass