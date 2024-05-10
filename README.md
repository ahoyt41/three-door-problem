# three-door-problem
A demonstration of the three door problem in python

## Description

The Monty Hall, or three door problem is a probability puzzle in which
you are presented with three doors. Behind one of the doors is a prize. Each door
is equally probable. After you chose a door, one of the two doors you didnt choose
is opened revealing no prize. You are then allowed to choose either to stay with your
initial guess or to switch to a new door. The question then is it better to stay
with your current guess or should you switch.

The naive assumption assumption would be that both doors are equally likely since you
now have two options. However, it is always more likely in this situation the the door
you did not initially choose is correct.

## Explanation

The way to think about this problem is this. Once you have made the first choice,
you split the doors into two groups. The first in which you are correct with 1/3
chance containing only the door that you picked. The second in which you are wrong
with a 2/3 chance, containing the two doors you did not pick. If you assume you are wrong,
then there is a 50/50 chance that it is either door you did not pick. Therefore the overall
odds it is either is door you did not pick is (1/2) * (2 / 3) = 1 / 3. Once a door is opened.
We know that the odds of that door being correct are 0 but the odds that you are wrong
stay the same. Therefore the odds of the unopned door being correct become (1) * (2/3) = 2/3.
The odds that you are correct do not change once the door is opened, therefore
the odds that your first guess is correct is (1/3) * (1) = 1/3.

## Code

This repo is a simple python script that simulates different strategies that could
be employed, demonstrating the probabilities described above. It uses only modules
from the standard library. To run the simulation simply run.

```bash
python3 three_door_problem.py
```

## Sources

[1] [Monty Hall Problem](https://en.wikipedia.org/wiki/Monty_Hall_problem)


