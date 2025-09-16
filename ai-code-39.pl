% Define the facts and rules
bird(penguin) :- cannot_fly.
bird(eagle) :- can_fly.
cannot_fly.
can_fly :- has_wings.
has_wings.
% Define the forward chaining rule
infer(X) :- bird(X).
% Example queries
?- infer(penguin).
?- infer(eagle)
?- infer(crow).
Result: Hence its proved
Exp 39 : Write a Prolog Program for backward Chaining. Incorporate required queries.
Aim: backward chainiag incorporative requird queries
Program:
% Define the facts and rules
bird(penguin) :- cannot_fly.
bird(eagle) :- can_fly.
cannot_fly.
can_fly :- has_wings.
has_wings.
% Define the backward chaining rules
infer(X) :- bird(X).
infer(X) :- can_fly, X = eagle.
infer(X) :- cannot_fly, X = penguin.
% Example queries
?- infer(crow).
?- infer(X).
