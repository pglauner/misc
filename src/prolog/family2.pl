different(X,X) :- !,fail.
different(_,_).

male(john).
father(peter, john).
father(peter, maria).
mother(liz, john).
mother(liz, maria).


brother(X, Y) :-
    male(X),
    father(F, X),
    mother(M, X),
    father(F, Y),
    mother(M, Y),
    different(X, Y).