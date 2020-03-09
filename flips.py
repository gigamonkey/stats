#!/usr/bin/env python

import random


def model(flips_left, heads_so_far=0, tails_so_far=0, iters=100_000):

    majority_heads = 0

    flips = flips_left + heads_so_far + tails_so_far

    for i in range(iters):
        heads = sum(random.randrange(2) for _ in range(flips_left)) + heads_so_far
        if heads > round(flips / 2):
            majority_heads += 1

    return majority_heads / iters


def prediction(flips, heads):
    half = round(flips / 2)
    chance = model(flips - heads, heads_so_far=heads)
    so_far = f", having gotten {heads} heads so far" if heads != 0 else ""
    print(
        f"Chance of getting more than {half} heads in {flips} flips{so_far}: {chance:.0%}"
    )


if __name__ == "__main__":

    prediction(10, 0)
    prediction(10, 4)
