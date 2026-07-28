import heapq

class Node:
    def __init__(self, position, parent=None, h=0):
        self.position = position   # (x, y)
        self.parent = parent       # link to previous node
        self.h = h                 # heuristic (Manhattan distance)

    def __lt__(self, other):
        return self.h < other.h    # priority queue based on heuristic only


def heuristic(a, b):
    # Manhattan distance
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def greedy_best_first_search(grid, start, goal):
    open_list = []
    closed_set = set()

    start_node = Node(start, None, heuristic(start, goal))
    heapq.heappush(open_list, start_node)

    while open_list:
        current = heapq.heappop(open_list)

        if current.position == goal:
            # reconstruct path
            path = []
            while current:
                path.append(current.position)
                current = current.parent
            return path[::-1]

        closed_set.add(current.position)

        # explore neighbors (4 directions)
        for dx, dy in [(0,1),(1,0),(0,-1),(-1,0)]:
            neighbor_pos = (current.position[0] + dx, current.position[1] + dy)

            if (0 <= neighbor_pos[0] < len(grid) and
                0 <= neighbor_pos[1] < len(grid[0]) and
                grid[neighbor_pos[0]][neighbor_pos[1]] == 0 and
                neighbor_pos not in closed_set):

                h = heuristic(neighbor_pos, goal)
                neighbor_node = Node(neighbor_pos, current, h)

                if not any(n.position == neighbor_pos and n.h <= neighbor_node.h for n in open_list):
                    heapq.heappush(open_list, neighbor_node)

    return None  # no path found


# Example usage
grid = [
    [0,0,0,0,0],
    [1,1,0,1,0],
    [0,0,0,0,0],
    [0,1,1,1,0],
    [0,0,0,0,0]
]

start = (0,0)
goal = (4,4)

path = greedy_best_first_search(grid, start, goal)
print("Path found:", path)
