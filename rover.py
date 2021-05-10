import dataclasses

from planet import Planet

# Movement constants
FORWARD = "F"
BACKWARD = "B"
LEFT = "L"
RIGHT = "R"


@dataclasses.dataclass(frozen=True)
class Direction:
    x: int
    y: int
    s: str


EAST = Direction(1, 0, "E")
NORTH = Direction(0, 1, "N")
WEST = Direction(-1, 0, "W")
SOUTH = Direction(0, -1, "S")
COMPASS = [EAST, SOUTH, WEST, NORTH]
NDIRS = len(COMPASS)


class Rover:

    def __init__(self, planet: Planet, dir_index: int):
        self.planet = planet
        self.__dir_index = dir_index

    def rotate_clockwise(self):
        self.__dir_index = (self.__dir_index + 1) % NDIRS

    def rotate_anticlockwise(self):
        self.__dir_index = (self.__dir_index - 1) % NDIRS

    def move_forward(self):
        pass

    def move_backward(self):
        pass

