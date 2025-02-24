from hash_resize import LinearProbingHashTable, ChainingHashTable
import config

def setup_table(cls):
    config.initialize()
    table = cls()
    table.insert("Los Angeles", "LAX")
    table.insert("Chicago", "ORD")
    table.insert("Dallas", "DAL")
    return table

def test_insert_search_linear():
    lpht = setup_table(LinearProbingHashTable)
    assert lpht.search("Chicago") == "ORD"
    assert lpht.search("Tokyo") is None

def test_remove_linear():
    lpht = setup_table(LinearProbingHashTable)
    assert lpht.remove("Chicago") is True
    assert lpht.search("Chicago") is None

def test_insert_search_chaining():
    cht = setup_table(ChainingHashTable)
    assert cht.seach("Dallas") == "DAL"
    assert cht.search("Miami") is None

def test_remove_chaining():
    cht = setup_table(ChainingHashTable)
    assert cht.remove("Los Angeles") is True
    assert cht.search("Los Angeles") is None
