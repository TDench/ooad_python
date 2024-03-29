import pytest

from Inventory import Inventory
from Guitar import Guitar, GuitarSpec


def test_add_guitar():
    inventory = Inventory()
    guitar = Guitar(1000, "G-001", GuitarSpec("Gibson", "Rosewood", None))
    inventory.addGuitar(guitar)
    assert len(inventory.guitars) == 1
    assert inventory.guitars[0] == guitar


class TestInventory:
    @pytest.fixture
    def inventory_with_guitars(self):
        inventory = Inventory()
        guitars = [
            Guitar(1000, "G-001", GuitarSpec("Gibson", "Rosewood", None)),
            Guitar(1500, "G-002", GuitarSpec("Fender", "Maple", None)),
            Guitar(800, "G-003", GuitarSpec("Martin", "Mahogany", None)),
            Guitar(1200, "G-004", GuitarSpec("Taylor", "Koa", None)),
            Guitar(2000, "G-005", GuitarSpec("Gretsch", "Walnut", "5")),
        ]
        for guitar in guitars:
            inventory.addGuitar(guitar)
        return inventory

    def test_get_guitar(self, inventory_with_guitars: Inventory):
        guitar = inventory_with_guitars.get_guitar("G-005")
        assert guitar.get_price() == 2000

    def test_inventory_length(self, inventory_with_guitars):
        assert len(inventory_with_guitars.guitars) == 5

    def test_search_guitar(self, inventory_with_guitars):
        wanted_guitar = GuitarSpec("Taylor", "Koa", None)
        search_result = inventory_with_guitars.search(wanted_guitar)
        assert len(search_result) == 1
        assert search_result[0].get_id() == "G-004"

    def test_search_string(self, inventory_with_guitars):
        wanted_guitar = GuitarSpec(None, None, "5")
        search_result = inventory_with_guitars.search(wanted_guitar)
        assert len(search_result) == 1
        assert search_result[0].get_id() == "G-005"


if __name__ == "__main__":
    pytest.main()
