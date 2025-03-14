from apq import APQUL, APQBH
from graph import Vertex, Graph

def djikstra(s: Vertex, g: Graph, apq):
    open_apq = apq() # cost as the key and the vertex as the value
    closed: dict = {} # destination vertex as the key and the value is (cost to get there, preceeding vertex)
    locs: dict = {} # vertex as a key, location in open as the value
    preds: dict = {s: None} # vertex as the key and preceeding vertex as the value

    # add s with APQ key 0 to open, and add s:(elt returned from APQ) to locs
    locs[s] = open_apq.add(0, s)

    # while open is not empty
    while open_apq.length() > 0:
        v = open_apq.remove_min()
        cost = open_apq.get_key(v)
        v = v.get_value() 
        del locs[v]
        pred = preds.pop(v)
        closed[v] = (cost, pred)
        for e in g.get_edges(v):
            w = e.opposite(v)
            if w not in closed:
                new_cost = cost + e.element()
                if w not in locs:
                    preds[w] = v
                    locs[w] = open_apq.add(new_cost, w)
                elif new_cost < open_apq.get_key(locs[w]):
                    preds[w] = v
                    open_apq.update_key(locs[w], new_cost)
    return closed

def djikstra_question_4(s: Vertex, d: Vertex, g: Graph, apq):
    open_apq = apq() # cost as the key and the vertex as the value
    closed: dict = {} # destination vertex as the key and the value is (cost to get there, preceeding vertex)
    locs: dict = {} # vertex as a key, location in open as the value
    preds: dict = {s: None} # vertex as the key and preceeding vertex as the value

    locs[s] = open_apq.add(0, s)

    while open_apq.length() > 0:
        # remove the min element v and its cost (key) from open
        v = open_apq.remove_min()
        cost = open_apq.get_key(v)
        v = v.get_value() 
        del locs[v]
        pred = preds.pop(v)
        closed[v] = (cost, pred)

        # if the node being removed from the heap is the destination, break out of the loop and return the current tree
        if v == d:
            return closed

        for e in g.get_edges(v):
            w = e.opposite(v)
            if w not in closed:
                new_cost = cost + e.element()
                if w not in locs:
                    preds[w] = v
                    locs[w] = open_apq.add(new_cost, w)
                elif new_cost < open_apq.get_key(locs[w]):
                    preds[w] = v
                    open_apq.update_key(locs[w], new_cost)
    return closed

def djikstra_question_6(s: Vertex, d: Vertex, g: Graph, apq):
    open_apq = apq() # cost as the key and the vertex as the value
    closed: dict = {} # destination vertex as the key and the value is (cost to get there, preceeding vertex)

    # add (s, None) into open with key (priority) 0
    open_apq.add(0, (s, None))

    while open_apq.length() > 0:

        # remove the minimum element, and get it's cost, vertex, and pred
        x = open_apq.remove_min()
        cost = open_apq.get_key(x)
        v = x.get_value()[0]
        if v == d:
            return closed
        pred = x.get_value()[1]

        if v not in closed:
            closed[v] = (cost, pred)
            for e in g.get_edges(v):
                w = e.opposite(v)
                if w not in closed:
                    new_cost = cost + e.element()
                    open_apq.add(new_cost, (w, v))
    return closed