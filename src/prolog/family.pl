different(X,X) :- !,fail.
different(_,_).

parent(pam, bob).
parent(tom, bob).
parent(tom, liz).
parent(bob, ann).
parent(bob, pat).
parent(pat, jim).

female(pam).
female(liz).
female(pat).
female(ann).
male(tom).
male(bob).
male(jim).

offspring(Y, X) :- parent(X, Y).

mother(X, Y) :-
  parent(X, Y),
  female(X).

grandparent(X, Z) :-
  parent(X, Y),
  parent(Y, Z).

sister(X, Y) :-
  parent(Z, X),
  parent(Z, Y),
  female(X),
  different(X, Y).

happy(X) :- parent(X, _Y).

hastwochildren(X) :-
  parent(X, Y),
  sister(_Z, Y).


grandchild(X, Y) :- grandparent(Y, X).

aunt(X, Y) :-
  parent(Z, Y),
  sister(X, Z).

predecessor(X, Z) :- parent(X, Z).

predecessor(X, Z) :-
  parent(X, Y),
  predecessor(Y, Z).
