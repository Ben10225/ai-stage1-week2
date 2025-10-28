# import sys
# import os

# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import unittest
from task1 import Point, Line, Circle, Polygon
import math


class TestPoint(unittest.TestCase):
    def test_distance(self):
        p1 = Point(x=0, y=0)
        p2 = Point(x=3, y=4)
        self.assertEqual(p1.distance_to(p2), 5.0)

        p3 = Point(x=-1, y=-1)
        self.assertEqual(p1.distance_to(p3), math.sqrt(2))


class TestLine(unittest.TestCase):
    def setUp(self):
        p1 = Point(x=0, y=0)
        p2 = Point(x=3, y=4)
        self.line1 = Line(start=p1, end=p2)

        p3 = Point(x=3, y=0)
        p4 = Point(x=6, y=4)
        self.line2 = Line(start=p3, end=p4)

        p5 = Point(x=0, y=0)
        p6 = Point(x=3, y=0)
        self.line3 = Line(start=p5, end=p6)

        p7 = Point(x=0, y=0)
        p8 = Point(x=0, y=4)
        self.line4 = Line(start=p7, end=p8)

        p9 = Point(x=0, y=6)
        p10 = Point(x=0, y=6)
        self.line5 = Line(start=p9, end=p10)

    def test_line_is_valid(self):
        self.assertTrue(self.line1.is_valid_line())
        self.assertTrue(self.line2.is_valid_line())
        self.assertTrue(self.line3.is_valid_line())
        self.assertTrue(self.line4.is_valid_line())
        self.assertFalse(self.line5.is_valid_line())

    def test_line_vertor(self):
        self.assertEqual(self.line1.vector(), (3, 4))
        self.assertEqual(self.line2.vector(), (3, 4))
        self.assertEqual(self.line3.vector(), (3, 0))
        self.assertEqual(self.line4.vector(), (0, 4))
        self.assertEqual(self.line5.vector(), (0, 0))

    def test_line_parallel(self):
        self.assertTrue(self.line1.is_parallel_to(self.line2))
        self.assertFalse(self.line3.is_parallel_to(self.line4))
        # 測試無效線段
        self.assertFalse(self.line3.is_parallel_to(self.line5))

    def test_line_perpendicular(self):
        self.assertFalse(self.line1.is_perpendicular_to(self.line2))
        self.assertTrue(self.line3.is_perpendicular_to(self.line4))
        # 測試無效線段
        self.assertFalse(self.line3.is_perpendicular_to(self.line5))


class TestCircle(unittest.TestCase):
    def test_area_and_intersection(self):
        center1 = Point(x=0, y=0)
        circle1 = Circle(center=center1, radius=3)

        center2 = Point(x=5, y=0)
        circle2 = Circle(center=center2, radius=3)

        center3 = Point(x=10, y=0)
        circle3 = Circle(center=center3, radius=3)

        self.assertAlmostEqual(circle1.get_area(), math.pi * 9)
        self.assertTrue(circle1.is_intersecting_with(circle2))
        self.assertFalse(circle1.is_intersecting_with(circle3))


class TestPolygon(unittest.TestCase):
    def test_perimeter(self):
        vertices = [
            Point(x=0, y=0),
            Point(x=3, y=0),
            Point(x=3, y=4),
            Point(x=0, y=4),
        ]
        polygon = Polygon(vertices=vertices)
        self.assertEqual(polygon.get_perimeter(), 14.0)


if __name__ == "__main__":
    unittest.main()
