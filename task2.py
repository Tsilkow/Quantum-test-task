#!/usr/bin/env python3

# Task 2
# Counting Islands
# ---
# You have a matrix MxN that represents a map. There are 2 possible states on the map: 1 - islands,
# 0 - ocean. Your task is to calculate the number of islands in the most effective way. Please
# write code in Python 3.


from typing import List
from collections import deque


NEIGHBORHOOD = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def mark_island(input_map, visited_tiles, island) -> None:
    to_visit = deque([island])

    while to_visit:
        curr = to_visit.pop()
        visited_tiles.add(curr)
        for direction in NEIGHBORHOOD:
            neighbor = (curr[0]+direction[0], curr[1]+direction[1])
            if (neighbor not in visited_tiles and
                (0 <= neighbor[0] and neighbor[0] < len(input_map[0])) and
                (0 <= neighbor[1] and neighbor[1] < len(input_map)) and
                    input_map[neighbor[1]][neighbor[0]] == 1):
                # Check only unvisited, valid coordinates that are not an ocean
                to_visit.appendleft(neighbor)
                visited_tiles.add(neighbor)


def count_islands(input_map: List[List[int]]) -> int:
    island_count = 0
    visited_tiles = set()

    for y, row in enumerate(input_map):
        for x, cell in enumerate(row):
            if (x, y) in visited_tiles:
                # If tile is alread assigned to island, don't search
                continue
            if cell == 1:
                # Start search only from land
                mark_island(input_map, visited_tiles, (x, y))
                island_count += 1
    return island_count


if __name__ == '__main__':
    input_map = []
    N, M = [int(x) for x in input('>').split(' ')]
    for y in range(N):
        input_map.append([int(x) for x in input('>').split(' ')])

    print(count_islands(input_map))
