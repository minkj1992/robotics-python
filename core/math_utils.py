import math

from core.dto import Position


def calculate_euclidean_distance(p1: Position, p2: Position) -> float:
    dx = p1.x - p2.x
    dy = p1.y - p2.y
    return math.hypot(dx, dy)
