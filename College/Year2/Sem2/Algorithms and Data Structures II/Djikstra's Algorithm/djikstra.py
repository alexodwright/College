from apq import APQUL, APQBH
from graph import Vertex, Edge, Graph

def djikstra(s: Vertex, g: Graph, apq):
    open = apq() # cost as the key and the vertex as the value
    closed: dict = {} # destination vertex as the key and the value is (cost to get there, preceeding vertex)
    locs: dict = {} # vertex as a key, location in open as the value
    preds: dict = {s: None} # vertex as the key and preceeding vertex as the value

    # add s with APQ key 0 to open, and add s:(elt returned from APQ) to locs
    locs[s] = open.add(0, s)

    # while open is not empty
    while open.length() > 0:
        # remove the min element v and its cost (key) from open
        cost = open.get_key(open.minimum())
        v = open.remove_min().get_value()
        # remove the entry for v from locs
        del locs[v]
        # and preds which returns the predecessor
        pred = preds.pop(v)
        # add an entry for v:(cost, predecessor) into closed
        closed[v] = (cost, pred)
        # for each edge e from v
        for e in g.get_edges(v):
            # w is the opposite vertex to v in e
            w = e.opposite(v)
            if w not in closed:
                #new_cost is v's key plus e's cost
                new_cost = cost + e.element()
                if w not in locs:
                    # add w:v to preds
                    preds[w] = v
                    # add w:new_cost to open
                    locs[w] = open.add(new_cost, w)
                # if new_cost is better than w's old cost
                elif new_cost < open.get_key(locs[w]):
                    # update w:v in preds
                    preds[w] = v
                    # update w's cost in open to new_cost
                    open.update_key(locs[w], new_cost)
    # return closed
    return closed
