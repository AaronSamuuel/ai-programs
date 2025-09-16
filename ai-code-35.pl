% Define the possible fruits and their colors
fruit(apple, red).
fruit(banana, yellow).
fruit(grape, purple).
fruit(orange, orange).
fruit(watermelon, green).
% Define a predicate to match a fruit with its color
match_fruit_color(Fruit, Color) :-
 fruit(Fruit, Color).
% Define a predicate to find all fruits with a certain color
% Note: The color argument is expressed as a variable to enable backtracking
fruits_with_color(FruitList, Color) :-
 findall(Fruit, match_fruit_color(Fruit, Color), FruitList).
 % Sample queries and expected outputs
%
% Query: match_fruit_color(apple, Color).
% Expected output: Color = red.
%
% Query: match_fruit_color(banana, Color).
% Expected output: Color = yellow.
%
% Query: match_fruit_color(pear, Color).
% Expected output: false.
%
% Query: fruits_with_color(FruitList, red).
% Expected output: FruitList = [apple].
%
% Query: fruits_with_color(FruitList, green).
% Expected output: FruitList = [watermelon].
%
% Query: fruits_with_color(FruitList, purple).
% Expected output: FruitList = [grape].