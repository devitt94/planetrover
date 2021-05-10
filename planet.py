class Planet:

    def __init__(self, width: int, height: int):
        assert width > 0 and height > 0, "Height and with must be positive integers"
        self.width = width
        self.height = height

    def position_is_valid(self, x: int, y: int) -> bool:
        return 0 <= x <= self.width and 0 <= y <= self.height

    def __str__(self):
        return f"Planet width={self.width} height={self.height}"
