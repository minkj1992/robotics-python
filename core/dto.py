from __future__ import annotations

from dataclasses import dataclass
from typing import Optional


@dataclass(frozen=True)
class Position:
    x: float
    y: float


@dataclass(frozen=True)
class SquareArea:
    min_val: int
    max_val: int


@dataclass
class Node:
    def __init__(self, position: Position) -> None:
        self.position: Position = position
        self.path: list[Position] = [position, ]
        self.parent: Optional[Node] = None

    def add_path(self, pos: Position) -> None:
        self.path.append(pos)
