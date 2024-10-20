# prime-grid-labeling
Generate an NxM 2d matrix such that all orthogonal neighbors are coprime.

*this is a testing version of the [PrimeGridLabeling project]*(https://github.com/GanschowJosh/PrimeGridLabeling)

# Goal
Our team's goal is to build an efficient algorithm that generates a matrix of a prime labeled graph. Ideally, we would be able to generate a 90x90 matrix in under a minute (that's a grid with 8100 prime-labeled vertices!).

Read [this paper](https://www.rroij.com/open-access/some-prime-labeling-of-graph.pdf) to learn more about prime labeling.

# Building on an Old Approach
The goal right now is to use a stack that attempts to use most heavily-factored numbers first. See v4.py. Tested for 10x10 grid.
This algorithm is deterministic since it does not use randomness, but instead, a high-factor-biased list to try to attempt to use the 'worst' numbers first.