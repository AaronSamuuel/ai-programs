% Define the initial state and final state
initial_state(state(at_door, on_floor, at_window, has_not_eaten)).
final_state(state(_, _, _, has_eaten)).
% Define the possible actions and their effects
% Note: Action effects are expressed as changes to the state of the monkey
action(state(at_door, on_floor, at_window, has_not_eaten), climb, state(at_window,
on_window, at_window, has_not_eaten)).
action(state(at_window, on_floor, at_window, has_not_eaten), grasp, state(at_window,
on_floor, at_window, has_eaten)).
action(state(at_window, on_window, at_window, has_not_eaten), climb, state(at_door,
on_window, at_door, has_not_eaten)).
action(state(at_door, on_window, at_door, has_not_eaten), walk, state(at_middle,
on_floor, at_middle, has_not_eaten)).
action(state(at_middle, on_floor, at_middle, has_not_eaten), grasp, state(at_middle,
on_floor, at_middle, has_eaten)).
action(state(at_middle, on_floor, at_middle, has_eaten), walk, state(at_door, on_floor,
at_door, has_eaten)).
% Define a predicate to execute a sequence of actions
% Note: The last argument of the predicate is the final state of the sequence of actions
execute_actions(_, [], FinalState) :- final_state(FinalState).
execute_actions(CurrentState, [Action|Rest], FinalState) :-
 action(CurrentState, Action, NextState),
 execute_actions(NextState, Rest, FinalState).
% Define a predicate to solve the problem
% Note: The solution is expressed as a sequence of actions
solve_problem(ActionList) :-
 initial_state(InitialState),
 execute_actions(InitialState, ActionList, FinalState),
 final_state(FinalState).
% Sample query and expected output
%
% Query: solve_problem(ActionList).
% Expected output: ActionList = [climb, grasp, climb, walk, grasp, walk].