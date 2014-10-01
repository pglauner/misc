% directed connection of node 1 and node 2 through edge 1
c(n1, n2, e1).
c(n1, n3, e2).
c(n1, n4, e3).
c(n1, n5, e4).
c(n2, n3, e5).
c(n2, n4, e6).
c(n3, n4, e7).
c(n4, n5, e8).

% undirected connection
connected(Node1, Node2, Edge) :-
  c(Node1, Node2, Edge);
  c(Node2, Node1, Edge).  

path(_, [], _).

path(Start, Edges, [Edge|Path]) :- 
  connected(Start, Succ, Edge),
  select(Edge, Edges, NewEdges),
  path(Succ, NewEdges, Path).

res(Start, Path) :-
  Edges = [e1, e2, e3, e4, e5, e6, e7, e8],
  path(Start, Edges, Path).