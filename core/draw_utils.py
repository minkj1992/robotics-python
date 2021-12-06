from __future__ import annotations
import math
from typing import Optional
import matplotlib.pyplot as plt
import numpy as np

from core.dto import Node, Position


def draw_graph(start: Position,
               goal: Position,
               tree: list[Node],
               obstacles: list[] = [],
               rnd: Optional[Position] = None):
    plt.clf()
    # 멈출려면 ESC 키를 누르시면 됩니다.
    plt.gcf().canvas.mpl_connect('key_release_event',
                                 lambda event: [exit(0) if event.key == 'escape' else None])

    # 랜덤 노드(랜덤 목표점)를 그립니다. 검은색 별
    if rnd:
        plt.plot(rnd.x, rnd.y, "*k")

    # path를 그리는 함수입니다. 초록색 선
    for node in tree:
        if node.parent:
            plt.plot(node.position.x, node.position.y, 'ob')
            plt.plot(node.path.x, node.path.y, "-g")

    for (ox, oy, size) in obstacles:
        plot_circle(ox, oy, size)
    # 출발점과 도착점을 그려주고
    plt.plot(start.x, start.y, "xr")
    plt.plot(goal.x, goal.y, "Dr")
    plt.axis("equal")
    plt.axis([-10, 20, -10, 20])
  #  plt.grid(True)
    plt.pause(0.001)


def plot_circle(x, y, size, color="-b"):  # pragma: no cover
    deg = list(range(0, 360, 5))
    deg.append(0)
    xl = [x + size * math.cos(np.deg2rad(d)) for d in deg]
    yl = [y + size * math.sin(np.deg2rad(d)) for d in deg]
    plt.plot(xl, yl, color)
