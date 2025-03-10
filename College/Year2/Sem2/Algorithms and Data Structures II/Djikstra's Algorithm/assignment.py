from graphreader import graphreader
from djikstra import djikstra
from gen_rand_graph import create_random_graph
from time_func import time_func
from apq import APQUL, APQBH

def part_1() -> None:
    graph = graphreader("simplegraph2-2.txt")
    s = graph.get_vertex_by_label(14)
    res = djikstra(s, graph, APQBH)
    path(graph.get_vertex_by_label(5), res)

def part_2() -> None:
    n = int(input("Enter n: "))
    m = int(input("Enter m: "))
    graph = create_random_graph(n, m)
    s = graph.get_vertex_by_label(1)
    res = djikstra(s, graph, APQBH)

def part_3() -> None:
    for i in range(1, 11):
        graph = create_random_graph(i, i)
        s = graph.get_vertex_by_label(1)
        exec_time, res = time_func(djikstra, s, graph, APQBH)
        print(f"Djikstra took {exec_time:.8f}s to execute with a {i}x{i} random graph.")
        print(f"Shortest path from node 1 to node {i*i} is ", end="")
        path(graph.get_vertex_by_label(i*i), res)

def main() -> None:
    # part_1()
    # part_2()
    part_3()

def path(end, closed):
    pred = end
    output = [end.element()]
    while pred is not None:
        if closed[pred][1] is not None:
            output.append(closed[pred][1].element())
        pred = closed[pred][1]
    output = "->".join(map(str, output[::-1]))
    print(output)
    
if __name__=="__main__":
    main()
