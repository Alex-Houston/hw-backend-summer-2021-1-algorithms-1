from typing import Any

__all__ = (
    'Node',
    'Graph'
)


class Node:
    def __init__(self, value: Any):
        self.value = value

        self.outbound = []
        self.inbound = []

    def point_to(self, other: 'Node'):
        self.outbound.append(other)
        other.inbound.append(self)

    def __str__(self):
        return f'Node({repr(self.value)})'

    __repr__ = __str__


class Graph:
    def __init__(self, root: Node):
        self._root = root

    
    def dfs(self) -> list[Node]:
        stack, path = [self._root], []
        
        while stack:
            vertex = stack.pop()
            if vertex in path:
                continue
            path.append(vertex)
            for neighbor in vertex.outbound:
                stack.append(neighbor)

        return path

    def bfs(self) -> list[Node]:
        visited = []
        queue = []
        visited.append(self._root)
        queue.append(self._root)
    
        while queue:
            s = queue.pop(0) 

            for neighbor in s.outbound:
                if neighbor not in visited:
                    visited.append(neighbor)
                    queue.append(neighbor)
        
        return visited
        

