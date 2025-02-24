#The packet does not mention anything about hash_implementaitons except for right here.

from hash_implementations import LinearProbingHashTable, ChainingHashTable
import config

config.initialize()
airport_data = [
    ("Lose Angeles", "LAX"), ("Houston", "IAH"), ("Chicago", "ORD"),
]

def demo():
    print("Linear Probing Demo:")
    lpht = LinearProbingHashTable()
    for city, code in airport_data[:15]:
        lpht.insert(city, code)
    print(lpht.search("Tokyo"))
    lpht.remove("Chicago")
    print(lpht.search("Chicago"))

    print("\nChaining Demo:")
    cht = ChainingHashTable()
    for city, code in airport_data:
        cht.insert(city,code)
    print(cht.search("Dallas"))
    cht.remove("New York")
    print(chr.search("New York"))

if __name__ == "__main__":
    demo()