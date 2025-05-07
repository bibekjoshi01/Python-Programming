class ItemDB:
    def __init__(self) -> None:
        self.price_map = {
            "apple": 0.5,
            "banana": 0.25,
            "orange": 0.75,
            "grape": 1.0,
            "watermelon": 1.5,
        }

    def get(self) -> dict:
        pass