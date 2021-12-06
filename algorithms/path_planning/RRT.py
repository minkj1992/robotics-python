from __future__ import annotations

import random

from core.dto import Node, Position, SquareArea

from typing import Optional
from dataclasses import dataclass

SHOW_ANIMATION = True

# TODO abstract tree data structure


class RRT:
    """Rapidly-exploring random tree Strategy """

    def __init__(self,
                 start: Position,
                 goal: Position,
                 obstacles: tuple[Position, ...],
                 area: SquareArea,
                 expand_distance: float = 1.0,
                 path_resolution: float = 0.5,
                 goal_sample_rate: float = 1.0,
                 max_iter: int = 1500) -> None:
        self.start: Node = Node(start)
        self.goal: Node = Node(goal)
        self.obstacles: tuple[Position, ...] = obstacles
        self.area: SquareArea = area

        # TODO: simulation 관련된 인자들은 분리
        self.expand_distance: float = expand_distance
        self.path_resolution: float = path_resolution
        self.goal_sample_rate: float = goal_sample_rate
        self.max_iter: int = max_iter

        self.tree: list[Node] = []

    def planning(self, animation=True):
        pass

    def steer(self, from_: Node, to_: Node):  # to use keyworld as variable pep-008
        pass

    def generate_final_course(self, goal_ind):
        pass

    def get_random_node(self) -> Node:
        pass

    # 랜덤 목표 지점으로부터 가장 가까이에 있는 노드를 찾는 함수입니다.
    @staticmethod
    def get_nearest_node_index(tree, rnd_node):
        pass

    # 랜덤 목표 지점으로부터 가장 가까이에 있는 노드를 찾는 함수입니다.
    @staticmethod
    def check_collision(node, obstacleList):
        pass

    # 거리, 각도 계산
    @staticmethod
    def calc_distance_and_angle(from_node, to_node):
        pass
