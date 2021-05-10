import dataclasses
import traceback
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

    def __str__(self):
        return self.s


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
        new_xpos = (self.__xpos + xmove) % self.planet.width
        new_ypos = (self.__ypos + ymove) % self.planet.height
        if self.planet.position_is_valid(new_xpos, new_ypos):
            self.__xpos, self.__ypos = new_xpos, new_ypos
        else:
            print(f"Error: cannot move to {new_xpos, new_ypos}")

    def __str__(self):
        return f"Rover at x={self.__xpos} y={self.__ypos}, facing {self.direction.s}\n{self.planet}"


if __name__ == "__main__":

    rover = None
    while rover is None:
        try:
            width, height = map(int, input("Enter Planet width and height: ").split())
            planet = Planet(width, height)

            x, y, direction = input("Enter initial rover position e.g. '0 0 E': ").split()
            x, y = int(x), int(y)
            d = direction.upper()
            if d == str(EAST):
                dir_index = COMPASS.index(EAST)
            elif d == str(NORTH):
                dir_index = COMPASS.index(NORTH)
            elif d == str(WEST):
                dir_index = COMPASS.index(WEST)
            elif d == str(SOUTH):
                dir_index = COMPASS.index(SOUTH)
            else:
                raise Exception(f"Invalid direction {direction}")

        except Exception:
            print("Error parsing input")
            print(traceback.format_exc())
        else:
            rover = Rover(planet, x, y, dir_index)

    while True:
        print(rover)
        instruction = input("Enter next instruction: ").upper()
        if instruction == FORWARD:
            rover.move_forward()
        elif instruction == BACKWARD:
            rover.move_backward()
        elif instruction == RIGHT:
            rover.rotate_clockwise()
        elif instruction == LEFT:
            rover.rotate_anticlockwise()
        else:
            print(f"Could not interpret instruction: {instruction}")

