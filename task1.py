from __future__ import annotations
from typing import Tuple
import math


class Point:
    def __init__(self, *, x: int, y: int) -> None:
        self.x = x
        self.y = y

    def distance_to(self, other: Point) -> float:
        return math.sqrt((other.x - self.x) ** 2 + (other.y - self.y) ** 2)


class Line:
    def __init__(self, *, start: Point, end: Point) -> None:
        self.x1, self.y1 = start.x, start.y
        self.x2, self.y2 = end.x, end.y

    def vector(self) -> Tuple[int, int]:
        return (self.x2 - self.x1, self.y2 - self.y1)

    # 如果線段的起點和終點相同，則不是有效線段，會讓平行和垂直的判斷失效
    def is_valid_line(self) -> bool:
        return not (self.x1 == self.x2 and self.y1 == self.y2)

    def is_parallel_to(self, other: Line) -> bool:
        if not self.is_valid_line() or not other.is_valid_line():
            return False  # 其中一條不是有效線段

        v1 = self.vector()
        v2 = other.vector()

        # 叉積為 0 即平行 # 兩向量 (x1, y1) 和 (x2, y2) 平行的條件是 x1 * y2 == y1 * x2
        return v1[0] * v2[1] == v1[1] * v2[0]

    def is_perpendicular_to(self, other: Line) -> bool:
        if not self.is_valid_line() or not other.is_valid_line():
            return False  # 其中一條不是有效線段

        v1 = self.vector()
        v2 = other.vector()

        # 點積為 0 即垂直 # 兩向量 (x1, y1) 和 (x2, y2) 垂直的條件是 x1 * x2 + y1 * y2 == 0
        return v1[0] * v2[0] + v1[1] * v2[1] == 0


class Circle:
    def __init__(self, *, center: Point, radius: int) -> None:
        self.cx, self.cy = center.x, center.y
        self.radius = radius

    def get_area(self) -> float:
        return math.pi * (self.radius**2)

    def is_intersecting_with(self, other: Circle) -> bool:
        distance_squared = (self.cx - other.cx) ** 2 + (self.cy - other.cy) ** 2
        radius_sum = self.radius + other.radius
        return distance_squared <= radius_sum**2


class Polygon:
    def __init__(self, *, vertices: list[Point]) -> None:
        self.vertices = vertices

    def get_perimeter(self) -> float:
        perimeter = 0.0
        num_vertices = len(self.vertices)
        for i in range(num_vertices):
            j = (i + 1) % num_vertices
            perimeter += self.vertices[i].distance_to(self.vertices[j])
        return perimeter


def main() -> None:

    # Line
    point_line_a1 = Point(x=-6, y=1)
    point_line_a2 = Point(x=2, y=4)

    point_line_b1 = Point(x=-6, y=-1)
    point_line_b2 = Point(x=2, y=2)

    point_line_c1 = Point(x=-4, y=-4)
    point_line_c2 = Point(x=-1, y=6)

    lineA = Line(start=point_line_a1, end=point_line_a2)
    lineB = Line(start=point_line_b1, end=point_line_b2)
    lineC = Line(start=point_line_c1, end=point_line_c2)

    # Circle
    point_circle_a = Point(x=6, y=3)
    point_circle_b = Point(x=8, y=1)
    circleA = Circle(center=point_circle_a, radius=2)
    circleB = Circle(center=point_circle_b, radius=1)

    # Polygon
    point_polygon_a1 = Point(x=2, y=0)
    point_polygon_a2 = Point(x=5, y=-1)
    point_polygon_a3 = Point(x=4, y=-4)
    point_polygon_a4 = Point(x=-1, y=-2)
    polygonA = Polygon(
        vertices=[
            point_polygon_a1,
            point_polygon_a2,
            point_polygon_a3,
            point_polygon_a4,
        ]
    )

    print("Are Line A and Line B parallel?", lineA.is_parallel_to(lineB))
    print("Are Line C and Line A perpendicular?", lineC.is_perpendicular_to(lineA))
    print("Print the area of Circle A.", circleA.get_area())
    print("Do Circle A and Circle B intersect?", circleA.is_intersecting_with(circleB))
    print("Print the perimeter of Polygon A.", polygonA.get_perimeter())


if __name__ == "__main__":
    main()
