#!/usr/bin/env python3
### Triangle Total ###
import sys

# read + transform the input
lines = [list(map(int, line.split())) for line in sys.stdin.readlines()]

# starting from the bottom of the pyramid
for i in range(len(lines) - 2, -1, -1):
    for j in range(len(lines[i])):
        # this value plus the maximum of its two children
        lines[i][j] = lines[i][j] + max(lines[i + 1][j], lines[i + 1][j + 1])

# the value at the top of the pyramid is the maximum sum path
print(lines[0][0])
