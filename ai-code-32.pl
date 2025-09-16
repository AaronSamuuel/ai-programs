% Facts about the family members
female(pam).
female(liz).
female(ann).
female(pat).
male(tom).
male(bob).
male(jim).
% Parent relations
parent(tom, liz).
parent(tom, bob).
parent(pam, liz).
parent(pam, bob).
parent(bob, ann).
parent(bob, pat).
parent(liz, jim).
% Mother relation
mother(X, Y) :-
 female(X),
 parent(X, Y).
% Father relation
father(X, Y) :-
 male(X),
 parent(X, Y).
% Grandmother relation
grandmother(X, Y) :-
 female(X),
 parent(X, Z),
 parent(Z, Y).
% Grandfather relation
grandfather(X, Y) :-
 male(X),
 parent(X, Z),
 parent(Z, Y).
% Sister relation
sister(X, Y) :-
 female(X),
 parent(Z, X),
 parent(Z, Y),
 X \= Y.
% Brother relation
brother(X, Y) :-
 male(X),
 parent(Z, X),
 parent(Z, Y),
 X \= Y.
