my_member(X, [X|_]).  
my_member(X, [_|T]) :- my_member(X, T).

my_conc([], L, L).
my_conc([X|L1], L2, [X|L3]) :- my_conc(L1, L2, L3).

my_last1(Item, List) :- my_conc(_, [Item], List).

my_last2(Item, [Item]).
my_last2(Item, [_|Rest]) :- my_last2(Item, Rest).

my_add(X, L, [X | L]).

my_del(X, [X|Tail], Tail).
my_del(X, [Y|Tail], [Y|Tail1]) :- my_del(X, Tail, Tail1).

my_insert(X, List, BiggerList) :- my_del(X, BiggerList, List).

my_member2(X, List) :- my_del(X, List, _).

my_sublist(S, L) :- my_conc(_, L2, L), my_conc(S, _, L2).


my_permutation([], []).
my_permutation([X|L], P) :- my_permutation(L, L1), my_insert(X, L1, P).

my_permutation2([], []).
my_permutation2(L, [X|P]) :- my_del(X, L, L1), my_permutation2(L1, P).

my_evenlength([]).
my_evenlength([_|Y]) :- my_oddlength(Y).
my_oddlength([_]).
my_oddlength([_|Y]) :- my_evenlength(Y).

my_reverse([], []).
my_reverse([X|Y], Reversed) :- my_reverse(Y, ReversedList), my_conc(ReversedList, [X], Reversed).

my_shift([X|Y], List2) :- my_conc(Y, [X], List2).

my_palindrome(X) :- my_reverse(X, X).

my_means(0, zero).
my_means(1, one).
my_means(2, two).
my_means(3, three).
my_means(4, four).
my_means(5, five).
my_means(6, six).
my_means(7, seven).
my_means(8, eight).
my_means(9, nine).

my_translate([], []).
my_translate([H|T], [H1|T1]) :- my_means(H, H1), my_translate(T, T1).

my_length([], 0).
my_length([_|Tail], N) :- my_length(Tail, N1), N is 1 + N1.

my_length1([], 0).
my_length1([_|Tail], N) :- N = 1 + N1, my_length1(Tail, N1).

my_max(X, Y, Max) :- X >= Y, Max = X; X < Y, Max = Y.

my_maxlist([X], X).
my_maxlist([X, Y|T], Max) :- my_maxlist([Y|T], MaxRest), my_max(X, MaxRest, Max).

my_sum([], 0).
my_sum([H|T], Sum) :- my_sum(T, Sum1), Sum is H + Sum1.

my_ordered([_]).
my_ordered([X, Y|T]) :- X =< Y, my_ordered([Y|T]).