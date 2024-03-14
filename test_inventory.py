import pytest

from Inventory import Guitar, Inventory


def test_add_guitar():
    inventory = Inventory()
    guitar = Guitar(1000, "G-001", "Gibson", "Rosewood")
    inventory.addGuitar(guitar)
    assert len(inventory.guitars) == 1
    assert inventory.guitars[0] == guitar


class TestInventory:
    @pytest.fixture
    def inventory_with_guitars(self):
        inventory = Inventory()
        guitars = [
            Guitar(1000, "G-001", "Gibson", "Rosewood"),
            Guitar(1500, "G-002", "Fender", "Maple"),
            Guitar(800, "G-003", "Martin", "Mahogany"),
            Guitar(1200, "G-004", "Taylor", "Koa"),
            Guitar(2000, "G-005", "Gretsch", "Walnut"),
        ]
        for guitar in guitars:
            inventory.addGuitar(guitar)
        return inventory

    def test_get_guitar(self, inventory_with_guitars: Inventory):
        guitar = inventory_with_guitars.get_guitar("G-005")
        assert guitar.get_manufacturer() == "Gretsch"

    def test_inventory_length(self, inventory_with_guitars):
        assert len(inventory_with_guitars.guitars) == 5

    def test_search_guitar(self, inventory_with_guitars):
        wanted_guitar = Guitar(None, None, "Taylor", "Koa")
        search_result = inventory_with_guitars.search(wanted_guitar)
        assert len(search_result) == 1
        assert search_result[0].get_manufacturer() == "Taylor"


if __name__ == "__main__":
    pytest.main()
