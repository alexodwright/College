
For an undirected connected simple graph G = =(V, E), a spanning tree is a subgraph of G that is a tree and which contains every vertex in V.

If the graph G has numerical weights on each edge, then a minimum spanning tree is a spanning tree which has the lowest sum of weights of the selected edges.

## Prim's Algorithm

```
Input: Connnected undirected graph G = (V, E) with edge weights and n verticies
Output: the edges S of a spanning tree (V, S) for G

T := [v], where v is any vertex in V
S := []
for each i from 2 to n
	e := {w, y} an edge with minimum weight in E such that w is in T and Y is not in T
	add e into S
	add y into T
return S
```

```
prim()

create an APQ pq which will contain costs and (vertex, edge) pairs
create an empty dictionary locs for locations of vertices in pq
for each v in G
	add (infinity, (v, None)) into pq and store location in locs[v]
create an empty list tree, which will be the output (the edges in the tree)
while pq is not empty
	remove c:(v, e), the minimum element, from pq
	remove v from locs
	if e is not None, append e to tree
	for each edge d incident on v
	w == d's opposite vertex from v
	if w is in locs # and so it is not yet in the tree
		cost = d's cost
		if cost is cheaper than w's entry in pq
			replace ?:(w, ?) in pq with cost: (w, d)
return tree
```

### Unsorted List APQ

O(n) for first loop

n times round loop each time O(1) to remove from locs and add to tree, O(n) to find and remove from pq, so for the loop without edge updates O($n^2$).

Internal loop for d edges, where d is max degree of any vertex, but overall there are m edges, so m times round that loop. Each time O(1) to update pq, so O(m).

### Heap APQ

O(n log n)

n times round loop each time O(1) to remove from locs and add to tree. O(log n ) to remove from pq, so for loop without edge updates O(n log n).

Internal loop for d edges, where d is max degree of any vertex but overall there are m edges, so m times round that loop. Each time O(log n) to update pq. So O(m log n).
