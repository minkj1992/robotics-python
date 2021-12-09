# RRT

```pseudo
Pseudo Code RRT
    Input: Initial configuration qinit, number of vertices(꼭지점) in RRT K, incremental distance Δq
    Output: RRT graph G

    G.init(qinit)
    for k = 1 to K do
        qrand ← RAND_CONF()
        qnear ← NEAREST_VERTEX(qrand, G)
        qnew ← NEW_CONF(qnear, qrand, Δq)
        G.add_vertex(qnew)
        G.add_edge(qnear, qnew)
    return G
```

- refs
  - https://en.wikipedia.org/wiki/Rapidly-exploring_random_tree
  - https://github.com/AtsushiSakai/PythonRobotics/blob/master/PathPlanning/RRT/rrt.py
  - https://msc9533.github.io/irl-study-2020/algorithm/2020/04/24/RRT_RRTstar.html
