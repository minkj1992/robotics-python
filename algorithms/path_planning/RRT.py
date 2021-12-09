from __future__ import annotations
import math
import random

from core import math_utils
from core.dto import Node, Position, SquareArea

from typing import Optional
from dataclasses import dataclass

SHOW_ANIMATION = True

# TODO abstract tree data structure

# animation drawer을 여기에 주입시켜주어야 한다.


class RRT:
    """Rapidly-exploring random tree Strategy """

    def __init__(self,
                 start: Position,
                 goal: Position,
                 obstacles: tuple[Position, ...],
                 area: SquareArea,
                 expand_distance: float = 3.0,
                 path_resolution: float = 0.5,
                 goal_sample_rate: int = 5,
                 max_iter: int = 500) -> None:

        self.start: Node = Node(start)
        self.goal: Node = Node(goal)
        self.obstacles: tuple[Position, ...] = obstacles
        self.area: SquareArea = area

        # TODO: simulation 관련된 인자들은 분리
        self.expand_distance: float = expand_distance
        self.path_resolution: float = path_resolution
        self.goal_sample_rate: float = goal_sample_rate
        self.max_iter: int = max_iter

        # TODO: abstract tree
        self.tree: list[Node] = [self.start, ]

    def planning(self):
        for i in range(self.max_iter):
            random_node = self.get_random_node()
            nearest_node = self.get_nearest_node(random_node)
            new_node = self.steer(from_node=nearest_node, to_node=random_node)

            # TODO: 2
            # obstacles이 없다면
            self.add_node(new_node)
            self.add_edge(nearest_node, new_node)
            if is_arrived():
                return "FINISHED"

    def get_random_node(self) -> Node:
        # Why?
        if random.randint(0, 100) > self.goal_sample_rate:
            return Node(Position(
                x=random.uniform(self.area.min_val, self.area.min_val),
                y=random.uniform(self.area.min_val, self.area.min_val)))
        return Node(self.goal.position)

    def get_nearest_node(self, target_node: Node) -> Node:
        distances = [math_utils.calculate_euclidean_distance(node.position, target_node.position)
                     for node in self.tree]
        nearest_node_index = distances.index(min(distances))
        return self.tree[nearest_node_index]

    def steer(self, from_node: Node, to_node: Node):
        distance, theta = math_utils.calculate_distance_and_angle(
            from_node.position, to_node.position)

        extend_length: float = min(self.expand_distance, distance)
        num_of_sampling_path_node: int = math.floor(
            extend_length / self.path_resolution)
        return self.create_new_node(from_node,
                                    to_node,
                                    theta,
                                    num_of_sampling_path_node)

    def create_new_node(self, from_node: Node, to_node: Node, theta: float, iter_num: int):
        x = from_node.position.x
        y = from_node.position.y
        path_history = [from_node.position, ]

        for _ in range(iter_num):
            x += self.path_resolution * math.cos(theta)
            y += self.path_resolution * math.sin(theta)
            path_history.append(Position(x, y))

        # TODO: 1
        # 반올림하느라 짤린 거리도 path에 추가해줍니다.
        distance, _ = self.calc_distance_and_angle(new_node, to_node)
        if d <= self.path_resolution:
            new_node.path_x.append(to_node.x)
            new_node.path_y.append(to_node.y)

        # 트리 구조여서 parent 지정, 마지막에 Goal을 찾았을 때 트리 구조가 유용하게 쓰입니다.
        new_node.parent = from_node
        return new_node

    def generate_final_course(self, goal_ind):
        pass

    @ staticmethod
    def check_collision(node, obstacleList):
        pass
