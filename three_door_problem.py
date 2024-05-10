import functools
import random
from typing import Callable, TypeAlias

StrategyFunc: TypeAlias = Callable[[int, int], int]


def stay_strategy(your_choice: int, remaining_choice: int) -> int:
    return your_choice


def switch_strategy(your_choice: int, remaining_choice: int) -> int:
    return remaining_choice


def random_choice(your_choice: int, remaining_choice: int, weight: float) -> int:
    return your_choice if random.random() < weight else remaining_choice


def random_choice_func(weight: float) -> StrategyFunc:
    return functools.partial(random_choice, weight=weight)


def open_door(choices, your_choice, winning_choice) -> int:
    if your_choice != winning_choice:
        return next(c for c in choices if c not in [your_choice, winning_choice])
    weights = [0.5 if x != your_choice else 0 for x in choices]
    return random.choices(choices, weights=weights, k=1)[0]


def simulate(strategy: StrategyFunc) -> bool:
    choices = list(range(3))
    winning_choice = random.choice(choices)
    your_choice = random.choice(choices)
    open = open_door(choices, your_choice, winning_choice)

    remaining_choice = [d for d in choices if d not in [your_choice, open]][0]

    new_choice = strategy(your_choice, remaining_choice)
    return new_choice == winning_choice


def main():
    num_sims = 10000

    win_count = 0
    for _ in range(num_sims):
        win_count += int(simulate(stay_strategy))
    print(f"Stay strategy success rate: {(100 * (win_count / num_sims)):.3f}%")

    win_count = 0
    for _ in range(num_sims):
        win_count += int(simulate(switch_strategy))
    print(f"Switch strategy success rate: {(100 * (win_count / num_sims)):.3f}%")

    win_count = 0
    for _ in range(num_sims):
        win_count += int(simulate(random_choice_func(0.5)))
    print(
        f"Random strategy success rate with a 0.5 weight: {(100 * (win_count / num_sims)):.3f}%"
    )


if __name__ == "__main__":
    main()
