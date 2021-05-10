import dataclasses
from typing import Tuple

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

    def __init__(self, planet: Planet, xpos: int, ypos: int, dir_index: int):
        self.planet = planet
        self.__xpos = xpos
        self.__ypos = ypos
        self.__dir_index = dir_index

    def rotate_clockwise(self):
        self.__dir_index = (self.__dir_index + 1) % NDIRS

    def rotate_anticlockwise(self):
        self.__dir_index = (self.__dir_index - 1) % NDIRS

    def move_forward(self):
        self._make_move(self.direction.x, self.direction.y)

    def move_backward(self):
        self._make_move(self.direction.x * -1, self.direction.y * -1)

    @property
    def direction(self) -> Direction:
        return COMPASS[self.__dir_index]

    @property
    def location(self) -> Tuple[int, int]:
        return self.__xpos, self.__ypos

    def _make_move(self, xmove: int, ymove: int):
        new_xpos = self.__xpos + xmove
        new_ypos = self.__ypos + ymove
        if self.planet.position_is_valid(new_xpos, new_ypos):
            self.__xpos, self.__ypos = new_xpos, new_ypos
        else:
            print(f"Error: cannot move to {new_xpos, new_ypos}")


