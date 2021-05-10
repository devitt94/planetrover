class Planet:

    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height

    def position_is_valid(self, x: int, y: int) -> bool:
        return 0 <= x <= self.width and 0 <= y <= self.height
