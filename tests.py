import unittest

from rover import Rover
from planet import Planet


class TestRover(unittest.TestCase):

    def setUp(self) -> None:
        planet = Planet(10, 10)
        self.rover = Rover(planet, 0, 0, 0)

    def test_rotate_clockwise(self):
        for expected_direction in ("S", "W", "N", "E"):
            self.rover.rotate_clockwise()
            self.assertEqual(self.rover.direction.s, expected_direction)

    def test_rotate_anticlockwise(self):
        for expected_direction in ("N", "W", "S", "E"):
            self.rover.rotate_anticlockwise()
            self.assertEqual(self.rover.direction.s, expected_direction)

    def test_move_forward(self):
        self.rover.move_forward()
        self.assertEqual(self.rover.location, (1, 0))

        self.rover.rotate_clockwise()
        self.rover.move_forward()
        self.assertEqual(self.rover.location, (1, -1))

        self.rover.rotate_anticlockwise()
        self.rover.move_forward()
        self.assertEqual(self.rover.location, (2, -1))

    def test_move_backward(self):
        self.rover.move_backward()
        self.assertEqual(self.rover.location, (-1, 0))

        self.rover.rotate_clockwise()
        self.rover.move_backward()
        self.assertEqual(self.rover.location, (-1, 1))

        self.rover.rotate_anticlockwise()
        self.rover.move_backward()
        self.assertEqual(self.rover.location, (-2, 1))


unittest.main()
