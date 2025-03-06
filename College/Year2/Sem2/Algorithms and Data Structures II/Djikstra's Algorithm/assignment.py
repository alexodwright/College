from graphreader import graphreader
from djikstra import djikstra
from gen_rand_graph import create_random_graph
from time_func import time_func
from apq import APQUL, APQBH

def part_1() -> None:
    graph = graphreader("simplegraph2-2.txt")
    s = graph.get_vertex_by_label(14)
    res = djikstra(s, graph, APQUL)
    print("Unordered List: ")
    for k, v in res.items():
        print(f"Target: {k.__str__()}:, Cost: {res[k][0]}, Predecessor: {res[k][1].__str__()}")

    print("Min Heap: ")
    res = djikstra(s, graph, APQBH)
    for k, v in res.items():
        print(f"Target: {k.__str__()}:, Cost: {res[k][0]}, Predecessor: {res[k][1].__str__()}")

def part_2() -> None:
    n = int(input("Enter n: "))
    m = int(input("Enter m: "))
    graph = create_random_graph(n, m)
    s = graph.get_vertex_by_label(1)
    res = djikstra(s, graph, APQUL)
    for k, v in res.items():
        print(f"Target: {k.__str__()}:, Cost: {res[k][0]}, Predecessor: {res[k][1].__str__()}")
    # print([f"Target: {res[k].__str__()}:, Cost: {res[k][0]}, Predecessor: {res[k][1].__str__()}" for k in res])

def part_3() -> None:
    for i in range(1, 11):
        graph = create_random_graph(i, i)
        s = graph.get_vertex_by_label(1)
        res = time_func(djikstra, s, graph, APQUL)
        k = graph.get_vertex_by_label(i*i)
        print(f"Target: {k.__str__()}:, Cost: {res[k][0]}, Predecessor: {res[k][1].__str__()}")

def main() -> None:
    part_1()
    # part_2()
    # part_3()


if __name__=="__main__":
    main()
