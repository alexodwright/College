from graphreader import graphreader
from djikstra import djikstra, djikstra_question_4
from gen_rand_graph import create_random_graph
from time_func import time_func
from apq import APQUL, APQBH
from plot import plot_times

def path(end, closed):
    # string representation of the shortest path from the source vertex in the closed dictionary to the 'end' vertex
    pred = end
    output = [end.element()]
    while pred is not None:
        if closed[pred][1] is not None:
            output.append(closed[pred][1].element())
        pred = closed[pred][1]
    output = "->".join(map(str, output[::-1]))
    output += f" : With a total cost of {closed[end][0]}"
    print(output)
    print(len(output))

def part_1() -> None:
    # Compute the shortest path for simplegraph1-2 and simplegraph2-2
    graph = graphreader("simplegraph1-2.txt")
    # starting at v1
    s = graph.get_vertex_by_label(1)
    res = djikstra(s, graph, APQBH)
    # destination is v4
    path(graph.get_vertex_by_label(4), res)

    graph = graphreader("simplegraph2-2.txt")
    # starting at v14
    s = graph.get_vertex_by_label(14)
    res = djikstra(s, graph, APQBH)
    # destination is v5
    path(graph.get_vertex_by_label(5), res)

def part_2() -> None:
    # create a 1x1, 2x2, 3x3, ..., 10x10 random graph and compute the shortest path and output the final cost
    for i in range(1, 11):
        graph = create_random_graph(i, i)
        s = graph.get_vertex_by_label(1)
        res = djikstra(s, graph, APQBH)
        path(graph.get_vertex_by_label(i*i), res)

def part_3() -> None:
    # create a 10x10, 20x20, 30x30, ..., 100x100 random graph and compute the shortest path's cost also compute the average time over 10 iterations
    gridsizes = []
    execution_times = []
    for i in range(10, 101, 10):
        total = 0
        gridsizes.append(i)
        for j in range(10):
            graph = create_random_graph(i, i)
            source = graph.get_vertex_by_label(1)
            exec_time, res = time_func(djikstra, source, graph, APQBH)
            total += exec_time
            # get the final path cost from [n//2][m//2] to [0][0]
            print(f"Final path length for graph size {i}x{i}, iteration {j+1}: {res[graph.get_vertex_by_label((i//2)*(i//2))][0]}")
        print(f"Average time for a {i}x{i} grid graph is {(total/10):.8f}s")
        execution_times.append(total/10)
    plot_times(gridsizes, execution_times, "Average Execution Time vs Grid Size")

def part_4() -> None:
    # with a random graph size of 500x500, compute the shortest path to a node increasingly further away from the source
    # test this scenario against the original version of djikstra and then against the modified djikstra
    # in which we check if the node removed from the heap is the destination node
    original_djikstra_times = []
    modified_djikstra_times = []
    for i in range(1, 1000):
        graph = create_random_graph(500, 500)
        source = graph.get_vertex_by_label(250)
        destination = graph.get_vertex_by_label(250+(i*i//10))
        path(destination, djikstra(source, graph, APQBH))
        print(f"Going to vertex {250+(i*i//10)}")
        exec_time, _ = time_func(djikstra, source, graph, APQBH)
        exec_time2, _ = time_func(djikstra_question_4, source, destination, graph, APQBH)
        original_djikstra_times.append(exec_time)
        modified_djikstra_times.append(exec_time2)
        print(f"The execution time for the normal djikstra was {exec_time}s")
        print(f"The execution time for the modified djikstra was {exec_time2}s")
    plot_times([i for i in range(1, 10)], "Impact of finding shortest path to all other nodes", original_djikstra_times, modified_djikstra_times)

def part_5() -> None:
    # check the unordered list implementation against the binary heap implementation with the same scenario as question 2
    print("Unordered List Implementation: ")
    for i in range(10, 101, 10):
        total = 0
        for j in range(10):
            graph = create_random_graph(i, i)
            source = graph.get_vertex_by_label(1)
            exec_time, res = time_func(djikstra, source, graph, APQUL)
            total += exec_time
            print(f"Final path cost for graph size {i}x{i}, iteration {j+1}: {res[graph.get_vertex_by_label((i//2)*(i//2))][0]}")
        print(f"Average time for a {i}x{i} grid graph is {(total/10):.8f}s")

    print("Binary Heap Implementation: ")
    for i in range(10, 101, 10):
        total = 0
        for j in range(10):
            graph = create_random_graph(i, i)
            source = graph.get_vertex_by_label(1)
            exec_time, res = time_func(djikstra, source, graph, APQBH)
            total += exec_time
            print(f"Final path cost for graph size {i}x{i}, iteration {j+1}: {res[graph.get_vertex_by_label((i//2)*(i//2))][0]}")
        print(f"Average time for a {i}x{i} grid graph is {(total/10):.8f}s")

def main() -> None:
    # part_1()
    # part_2()
    # part_3()
    part_4()
    # part_5()


if __name__=="__main__":
    main()
