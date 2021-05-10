from typing import List, Tuple

NO_OBSTACLE = 0
OBSTACLE = 1


class Planet:

    def __init__(self, width: int, height: int, obstacles: List[Tuple[int, int]]):
        assert width > 0 and height > 0, "Height and with must be positive integers"
        self.width = width
        self.height = height

        grid = []
        for i in range(height):
            row = []
            for j in range(width):
                val = OBSTACLE if (i, j) in obstacles else NO_OBSTACLE
                row.append(val)
            grid.append(row)

        self.__grid = grid

    def position_is_valid(self, x: int, y: int) -> bool:
        if not (0 <= x <= self.width and 0 <= y <= self.height):
            return False
        elif self.__grid[x][y] == OBSTACLE:
            return False
        else:
            return True

    def __str__(self):
        row_strs = reversed([" ".join(str(cell) for cell in row) for row in self.__grid])
        return "\n".join(row_strs)
