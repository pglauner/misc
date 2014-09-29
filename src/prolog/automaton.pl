final(s3).

trans(s1, a, s1).
trans(s1, a, s2).
trans(s1, b, s1).
trans(s2, b, s3).
trans(s3, b, s4).

silent(s1, s3).
silent(s2, s4).
silent(s3, s1).

accepts(S, []) :- final(S).
accepts(S, [X|Rest]) :- trans(S, X, S1), accepts(S1, Rest).
accepts(S, String) :- silent(S, S1), accepts(S1, String).

accepts1(S, [], _) :- final(S).
accepts1(S, [X|Rest], Max_moves) :- N1 is Max_moves - 1, N1 >= 0, trans(S, X, S1), accepts1(S1, Rest, N1).
accepts1(S, String, Max_moves) :- N1 is Max_moves - 1, N1 >= 0, silent(S, S1), accepts1(S1, String, N1).