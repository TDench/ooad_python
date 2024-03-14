import pytest

from Inventory import Guitar, Inventory

def test_add_guitar():
    inventory = Inventory()
    guitar = Guitar(1000, "G-001", "Gibson", "Rosewood")
    inventory.addGuitar(guitar)
    assert len(inventory.guitars) == 1
    assert inventory.guitars[0] == guitar

def test_search_guitar():
    inventory = Inventory()
    guitar1 = Guitar(1000, "G-001", "Gibson", "Rosewood")
    guitar2 = Guitar(1500, "G-002", "Fender", "Maple")
    inventory.addGuitar(guitar1)
    inventory.addGuitar(guitar2)

    search_guitar = Guitar(None, None, "Gibson", "Rosewood")
    search_result = inventory.search(search_guitar)
    assert len(search_result) == 1
    assert search_result[0] == guitar1

if __name__ == "__main__":
    pytest.main()

if __name__ == "__main__":
    pytest.main()