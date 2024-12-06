import os
import requests
from datetime import datetime

class AocUtils:
    def __init__(self, year, day):
        self.year = year
        self.day = day
        self.session_cookie = os.getenv("AOC_SESSION")
        self.input_path = os.path.join(os.getcwd(), ""+str(self.year), "day"+str(self.day), "test.txt")

    def load_input(self):
        with open(self.input_path, "r") as f:
            self.input_content = f.read().strip()
            
    def load_grid(self):
        self.grid = [[c for c in line] for line in self.input_content.split("\n")]

    def pretty_print_grid(self):
        for line in self.grid:
            print("".join(line))

class Day:
    def __init__(self, aoc_utils):
        self.aoc_utils = aoc_utils

    def solve_part1(self):
        self.aoc_utils.load_input()
        self.aoc_utils.load_grid()
        self.aoc_utils.pretty_print_grid()

        res = 0
        return res

    def solve_part2(self):
        self.aoc_utils.load_input()
        self.aoc_utils.load_grid()
        
        
        res = 0
        return res

if __name__ == "__main__":
    year = int("%year%")
    day = int("%day%")

    aoc_utils = AocUtils(year, day)
    solver = Day(aoc_utils)

    part1_result = solver.solve_part1()
    print("Solution to Part 1:", part1_result)

    part2_result = solver.solve_part2()
    print("Solution to Part 2:", part2_result)