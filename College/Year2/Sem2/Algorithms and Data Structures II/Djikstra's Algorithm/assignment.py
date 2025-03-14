# imports from other files
from graphreader import graphreader
from djikstra import djikstra, djikstra_question_4, djikstra_question_6
from gen_rand_graph import create_random_graph
from time_func import time_func
from apq import APQUL, APQBH
from plot import plot_times

###################################################
# To run each question/part simply
# uncomment the function name in main()
# and run the program
###################################################

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
    return output

# function to get vertex in the grid graph given it's row and column
def get_vertex_by_row_col(width, row, col, graph):
    return graph.get_vertex_by_label((width*row)+col+1)

def part_1() -> None:
    # Compute the shortest path for simplegraph1-2 and simplegraph2-2
    graph = graphreader("simplegraph1-2.txt")
    # starting at v1
    s = graph.get_vertex_by_label(1)
    res = djikstra(s, graph, APQBH)
    # destination is v4
    print(path(graph.get_vertex_by_label(4), res))

    graph = graphreader("simplegraph2-2.txt")
    # starting at v14
    s = graph.get_vertex_by_label(14)
    res = djikstra(s, graph, APQBH)
    # destination is v5
    print(path(graph.get_vertex_by_label(5), res))

def part_2() -> None:
    # create a 1x1, 2x2, 3x3, ..., 10x10 random graph and compute the shortest path and output the final cost
    for i in range(4, 11):
        graph = create_random_graph(i, i)
        s = graph.get_vertex_by_label(1)
        res = djikstra(s, graph, APQBH)
        print(path(graph.get_vertex_by_label(i*i), res))

def part_3() -> None:
    # create a 10x10, 20x20, 30x30, ..., 100x100 random graph and compute the shortest path's cost also compute the average time over 10 iterations
    exec_times = []
    for i in range(10, 101, 10):
        e = []
        for _ in range(10):
            graph = create_random_graph(i, i)
            source = get_vertex_by_row_col(i, i//2, i//2, graph)
            exec_time, res = time_func(djikstra, source, graph, APQBH)
            e.append(exec_time)
            print(f"Path length for graph size {i}x{i}: ", end="")
            print(len(path(get_vertex_by_row_col(i, 0, 0, graph), res).split("->")))
        print(f"Average time for {i}x{i} grid is: {(sum(e)/len(e)):.8f}s")
        print()
        exec_times.append(e)
    plot_times("Grid Size", "Execution Time (s)", "Grid Size vs Execution Time", [i for i in range(10, 101, 10)], *exec_times)
        

def part_4() -> None:
    # with a random graph size of 500x500, compute the shortest path to a node increasingly further away from the source
    # test this scenario against the original version of djikstra and then against the modified djikstra
    # in which we check if the node removed from the heap is the destination node
    original_djikstra_times = []
    modified_djikstra_times = []
    distances = []
    width = 500
    graph = create_random_graph(width, width)
    # get the centre vertex
    source = get_vertex_by_row_col(width, width//2, width//2, graph)
    for i in range(1, 101):
        # the destination is i rows down and i colums across from the source vertex
        destination = get_vertex_by_row_col(width, (width//2)+i, (width//2)+i, graph)
        print(f"Going to vertex {(width//2)+i}")
        original_exec_time, _ = time_func(djikstra, source, graph, APQBH)
        modified_exec_time, _ = time_func(djikstra_question_4, source, destination, graph, APQBH)
        original_djikstra_times.append(original_exec_time)
        modified_djikstra_times.append(modified_exec_time)
        distances.append(i)
    plot_times("Distance from source", "Execution Time (s)", "Specific-Node vs All-Node Djikstra's Algorithm", distances, original_djikstra_times, modified_djikstra_times)
    
def part_5() -> None:
    ul_times = []
    bh_times = []
    sizes = []
    # generate graphs from size 10 to size 500 in increments of 10
    for i in range(10, 501, 10):
        print(i)
        graph = create_random_graph(i, i)
        # get the first vertex
        source = get_vertex_by_row_col(i, 0, 0, graph)
        # compute the times for the unordered list apq and binary heap apq
        ul_time, _ = time_func(djikstra, source, graph, APQUL)
        bh_time, _ = time_func(djikstra, source, graph, APQBH)
        # add these times to the respective list of times
        ul_times.append(ul_time)
        bh_times.append(bh_time)
        # add the grid size to the list of grid sizes
        sizes.append(i)
    plot_times("Grid Size", "Execution Time (s)", "Unordered List vs Binary Heap APQ Implementations", sizes, ul_times, bh_times)
    
def part_6() -> None:
    # basically the same as question 4, but this time comparing the specific-node version to the specific-node simpler apq version
    original_djikstra_times = []
    modified_djikstra_times = []
    distances = []
    width = 500
    graph = create_random_graph(width, width)
    source = get_vertex_by_row_col(width, width//2, width//2, graph)
    for i in range(1, 101):
        destination = get_vertex_by_row_col(width, (width//2)+i, (width//2)+i, graph)
        print(f"Going to vertex {(width//2)+i}")
        # specific-node from q4
        original_exec_time, _ = time_func(djikstra_question_4, source, destination, graph, APQBH)
        # specific-node and simpler apq
        modified_exec_time, _ = time_func(djikstra_question_6, source, destination, graph, APQBH)
        original_djikstra_times.append(original_exec_time)
        modified_djikstra_times.append(modified_exec_time)
        distances.append(i)
    plot_times("Distance from source", "Execution Time (s)", "Original vs Simpler APQ", distances, original_djikstra_times, modified_djikstra_times)

def main() -> None:
    part_1()
    # part_2()
    # part_3()
    # part_4()
    # part_5()
    # part_6()


if __name__=="__main__":
    main()
