from graph import Graph
import random

def create_random_graph(n: int, m: int) -> Graph:
    g = Graph()
    grid = [[None for _ in range(m)] for _ in range(n)]
    label = 1
    for i, row in enumerate(grid):
        for j, _ in enumerate(row):
            grid[i][j] = g.add_vertex(label)
            label += 1

    for i, row in enumerate(grid):
        for j, _ in enumerate(row):
            try:
                g.add_edge(grid[i][j], grid[i+1][j], random.randint(1, max(n,m)//2))
            except IndexError as _:
                pass
            try:
                g.add_edge(grid[i][j], grid[i][j+1], random.randint(1, max(n,m)//2))
            except IndexError as _:
                pass
    return g

def main() -> None:
    n = int(input("Enter n: "))
    m = int(input("Enter m: "))
    create_random_graph(n, m)

if __name__=="__main__":
    main()
