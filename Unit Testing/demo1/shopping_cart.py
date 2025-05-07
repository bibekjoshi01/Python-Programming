from typing import List


class ShoppingCart:
    def __init__(self, max_size: int):
        self.items: List[str] = []
        self.max_size = max_size

    def add_item(self, item: str) -> None:
        if self.get_size() == self.max_size:
            raise OverflowError("Cannot add more items to the cart.")
        self.items.append(item)

    def remove_item(self, item: str) -> None:
        if item in self.items:
            self.items.remove(item)

    def get_items(self) -> List[str]:
        return self.items

    def get_size(self) -> int:
        return len(self.items)

    def get_total_price(self, price_map):
        total_price = 0.0
        for item in self.get_items():
            total_price += price_map.get(item)
        return total_price
