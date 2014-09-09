my_member(X, [X|_]).  
my_member(X, [_|T]) :- member(X, T).

my_conc([], L, L).
my_conc([X|L1], L2, [X|L3]) :- my_conc(L1, L2, L3).