from collections import deque

# Maze from the image (manual transcription from image)
maze_str = """
_______________________________
|_U_    |    ___|___    |    ___|
|    ___    |       |   ____    |
|___|   |_______|___________|   |
|           |       |   ________|
#.####..##.#.##.....#.##...####..
..###.#.####.#..#.#.#..#.. .###.#
.#.###.#.#.#..#.#.....##.#.....#.
...##...###.#..##..###.#.#######
"""

# Convert to a list of lists
maze = [list(line) for line in maze_str.strip().split('\n')]

def find_position(maze, symbol):
    for r, row in enumerate(maze):
        for c, val in enumerate(row):
            if val == symbol:
                return r, c
    return None

def solve_maze(maze):
    directions = {'w': (-1, 0), 's': (1, 0), 'a': (0, -1), 'd': (0, 1)}
    start = find_position(maze, 'U')
    if not start:
        return None
    queue = deque([(start, [])])
    visited = set([start])

    while queue:
        (r, c), path = queue.popleft()
        # Exit condition: reach outside bottom row or rightmost column with a path cell
        if r >= len(maze) - 1 or c >= len(maze[0]) - 1:
            if maze[r][c] == '.':
                return path

        for move, (dr, dc) in directions.items():
            nr, nc = r + dr, c + dc
            if 0 <= nr < len(maze) and 0 <= nc < len(maze[0]):
                if maze[nr][nc] == '.' and (nr, nc) not in visited:
                    visited.add((nr, nc))
                    queue.append(((nr, nc), path + [move]))
    return None

# Run the solver
move_sequence = solve_maze(maze)
move_sequence

