% Facts
fever.
cough.

% Rules
flu :-
    fever,
    cough.

medicine :-
    flu.

cold :-
    cough.

syrup :-
    cold.

% Main Predicate
start :-
    write('Checking whether medicine is required...'), nl,
    (medicine ->
        write('Goal Achieved: Medicine is required.'), nl
    ;
        write('Goal Failed: Medicine is not required.'), nl
    ).