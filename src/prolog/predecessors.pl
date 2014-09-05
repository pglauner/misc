parent(pam, bob).
parent(tom, bob).
parent(tom, liz).
parent(bob, ann).
parent(bob, pat).
parent(pat, jim).

pred1(X, Z) :-
    parent(X, Z).

pred1(X, Z) :-
    parent(X, Y),
    pred1(Y, Z).


pred2(X, Z) :-
    parent(X, Y),
    pred2(Y, Z).

pred2(X, Z) :-
    parent(X, Z).


pred3(X, Z) :-
    parent(X, Z).

pred3(X, Z) :-
    pred3(X, Y),
    parent(Y, Z).


pred4(X, Z) :-
    pred4(X, Y),
    parent(Y, Z).

pred4(X, Z) :-
    parent(X, Z).