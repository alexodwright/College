## Question 3

For question 3, I generated random graphs of increasing grid size from 10x10 to 100x100 in increments of 10 each time. I ran Djikstra's Algorithm 10 times for each grid size and computed the average runtime for each grid size. I ran Djikstra's Algorithm to compute the shortest path from the Vertex at (n//2, m//2) to the Vertex at (0, 0). The output of my program was as as follows, showing the shortest path length for each iteration and after 10 iterations of a graph size, the average runtime for Djikstra's Algorithm on that grid size:
```
Final path length for graph size 10x10, iteration 1: 13
Final path length for graph size 10x10, iteration 2: 15
Final path length for graph size 10x10, iteration 3: 11
Final path length for graph size 10x10, iteration 4: 15
Final path length for graph size 10x10, iteration 5: 10
Final path length for graph size 10x10, iteration 6: 14
Final path length for graph size 10x10, iteration 7: 11
Final path length for graph size 10x10, iteration 8: 10
Final path length for graph size 10x10, iteration 9: 15
Final path length for graph size 10x10, iteration 10: 13
Average time for a 10x10 grid graph is 0.00021648s
Final path length for graph size 20x20, iteration 1: 82
Final path length for graph size 20x20, iteration 2: 86
Final path length for graph size 20x20, iteration 3: 86
Final path length for graph size 20x20, iteration 4: 98
Final path length for graph size 20x20, iteration 5: 78
Final path length for graph size 20x20, iteration 6: 73
Final path length for graph size 20x20, iteration 7: 81
Final path length for graph size 20x20, iteration 8: 88
Final path length for graph size 20x20, iteration 9: 78
Final path length for graph size 20x20, iteration 10: 98
Average time for a 20x20 grid graph is 0.00099028s
Final path length for graph size 30x30, iteration 1: 81
Final path length for graph size 30x30, iteration 2: 98
Final path length for graph size 30x30, iteration 3: 114
Final path length for graph size 30x30, iteration 4: 91
Final path length for graph size 30x30, iteration 5: 103
Final path length for graph size 30x30, iteration 6: 93
Final path length for graph size 30x30, iteration 7: 108
Final path length for graph size 30x30, iteration 8: 119
Final path length for graph size 30x30, iteration 9: 107
Final path length for graph size 30x30, iteration 10: 96
Average time for a 30x30 grid graph is 0.00263807s
Final path length for graph size 40x40, iteration 1: 292
Final path length for graph size 40x40, iteration 2: 263
Final path length for graph size 40x40, iteration 3: 311
Final path length for graph size 40x40, iteration 4: 332
Final path length for graph size 40x40, iteration 5: 356
Final path length for graph size 40x40, iteration 6: 324
Final path length for graph size 40x40, iteration 7: 330
Final path length for graph size 40x40, iteration 8: 304
Final path length for graph size 40x40, iteration 9: 281
Final path length for graph size 40x40, iteration 10: 312
Average time for a 40x40 grid graph is 0.00483160s
Final path length for graph size 50x50, iteration 1: 251
Final path length for graph size 50x50, iteration 2: 270
Final path length for graph size 50x50, iteration 3: 272
Final path length for graph size 50x50, iteration 4: 232
Final path length for graph size 50x50, iteration 5: 306
Final path length for graph size 50x50, iteration 6: 266
Final path length for graph size 50x50, iteration 7: 261
Final path length for graph size 50x50, iteration 8: 271
Final path length for graph size 50x50, iteration 9: 263
Final path length for graph size 50x50, iteration 10: 278
Average time for a 50x50 grid graph is 0.00897557s
Final path length for graph size 60x60, iteration 1: 675
Final path length for graph size 60x60, iteration 2: 687
Final path length for graph size 60x60, iteration 3: 668
Final path length for graph size 60x60, iteration 4: 639
Final path length for graph size 60x60, iteration 5: 682
Final path length for graph size 60x60, iteration 6: 672
Final path length for graph size 60x60, iteration 7: 634
Final path length for graph size 60x60, iteration 8: 624
Final path length for graph size 60x60, iteration 9: 668
Final path length for graph size 60x60, iteration 10: 694
Average time for a 60x60 grid graph is 0.01741086s
Final path length for graph size 70x70, iteration 1: 489
Final path length for graph size 70x70, iteration 2: 528
Final path length for graph size 70x70, iteration 3: 507
Final path length for graph size 70x70, iteration 4: 513
Final path length for graph size 70x70, iteration 5: 496
Final path length for graph size 70x70, iteration 6: 436
Final path length for graph size 70x70, iteration 7: 476
Final path length for graph size 70x70, iteration 8: 483
Final path length for graph size 70x70, iteration 9: 484
Final path length for graph size 70x70, iteration 10: 447
Average time for a 70x70 grid graph is 0.02189442s
Final path length for graph size 80x80, iteration 1: 1118
Final path length for graph size 80x80, iteration 2: 1156
Final path length for graph size 80x80, iteration 3: 1127
Final path length for graph size 80x80, iteration 4: 1171
Final path length for graph size 80x80, iteration 5: 1134
Final path length for graph size 80x80, iteration 6: 1108
Final path length for graph size 80x80, iteration 7: 1167
Final path length for graph size 80x80, iteration 8: 1164
Final path length for graph size 80x80, iteration 9: 1174
Final path length for graph size 80x80, iteration 10: 1151
Average time for a 80x80 grid graph is 0.04035554s
Final path length for graph size 90x90, iteration 1: 818
Final path length for graph size 90x90, iteration 2: 819
Final path length for graph size 90x90, iteration 3: 857
Final path length for graph size 90x90, iteration 4: 802
Final path length for graph size 90x90, iteration 5: 848
Final path length for graph size 90x90, iteration 6: 827
Final path length for graph size 90x90, iteration 7: 823
Final path length for graph size 90x90, iteration 8: 886
Final path length for graph size 90x90, iteration 9: 868
Final path length for graph size 90x90, iteration 10: 845
Average time for a 90x90 grid graph is 0.04515075s
Final path length for graph size 100x100, iteration 1: 1778
Final path length for graph size 100x100, iteration 2: 1897
Final path length for graph size 100x100, iteration 3: 1854
Final path length for graph size 100x100, iteration 4: 1782
Final path length for graph size 100x100, iteration 5: 1839
Final path length for graph size 100x100, iteration 6: 1810
Final path length for graph size 100x100, iteration 7: 1874
Final path length for graph size 100x100, iteration 8: 1829
Final path length for graph size 100x100, iteration 9: 1781
Final path length for graph size 100x100, iteration 10: 1718
Average time for a 100x100 grid graph is 0.04707526s
```
### Average Execution Time vs Grid Size

![[Part3 1.png]]

From the graph we can see that the execution time is proportional to the grid size of the randomly generated graph. The runtime of Djikstra's Algorithm is O($(V + E)\log{V}$) where V is the number of vertices in the graph and E is the number of edges in the graph. This is because in the binary heap implementation of the APQ, each time we call add(), remove_min(), and update_key() it is an O($\log{n}$) operation (where n is the number of nodes in the graph). As the graph size increases we must call each of these three operations an increasing number of times (proportional to n), which in turn increases the overall execution time.