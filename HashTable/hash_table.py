#Base class for a hash table that supports insert, remove, and search operations

class HashTable:
    #Returns a non-negative hash code for the specified key.
    def hashKey(self,key):
        return abs(hash(key))
    
    #Inserts the key/value pait. If key exists, update value.
    #Return True if inserted/updated, False if not.
    def insert(self, key, value):
        pass

    #Removed the key/value pait if found. Return True if removed, False if not.
    def remove(self,key):
        pass

    #Returns value if key is found, none if not.
    def search(self,key):
        pass