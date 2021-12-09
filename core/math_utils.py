from __future__ import annotations
import math
from core.dto import Position, Node


def calculate_euclidean_distance(p1: Position, p2: Position) -> float:
    dx = p1.x - p2.x
    dy = p1.y - p2.y
    return math.hypot(dx, dy)


def calculate_distance_and_angle() -> tuple[float, float]:
    ...
