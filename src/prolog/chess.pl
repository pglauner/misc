jump(X/Y, X1/Y1) :-
  (X1 is X + 1, Y1 is Y + 2;
   X1 is X + 2, Y1 is Y + 1;
   X1 is X + 2, Y1 is Y - 1;
   X1 is X + 1, Y1 is Y - 2;
   X1 is X - 1, Y1 is Y - 2;
   X1 is X - 2, Y1 is Y - 1;
   X1 is X - 2, Y1 is Y + 1;
   X1 is X - 1, Y1 is Y + 2
  ),
  ValidCoords = [1,2,3,4,5,6,7,8],
  member(X1, ValidCoords),
  member(Y1, ValidCoords).

knightpath([_]).
knightpath([A, B|Rest]) :-
  jump(A, B),
  knightpath([B|Rest]).