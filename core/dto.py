from __future__ import annotations

from dataclasses import dataclass
from typing import Optional


@dataclass(frozen=True)
class Position:
    x: int
    y: int


@dataclass(frozen=True)
class SquareArea:
    min_val: int
    max_val: int


class Node:
    def __init__(self, position: Position):
        self.position: Position = position
        self.path: list[Position] = []
        self.parent: Optional[Node] = None
