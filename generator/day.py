import os
import requests
from datetime import datetime

class GridUtils:
    @staticmethod
    def cardinal_directions():
        return [(1, 0), (-1, 0), (0, 1), (0, -1)]

    @staticmethod
    def diagonal_directions():
        return [(1, 1), (-1, -1), (1, -1), (-1, 1)]

    @staticmethod
    def all_directions():
        return GridUtils.cardinal_directions() + GridUtils.diagonal_directions()

    @staticmethod
    def find_in_grid(grid, element):
        for y, row in enumerate(grid):
            for x, cell in enumerate(row):
                if cell == element:
                    return (x, y)
        return None

    @staticmethod
    def count_elements_in_grid(grid, element):
        return sum(row.count(element) for row in grid)

class AocUtils:
    def __init__(self, year, day):
        self.year = year
        self.day = day
        self.session_cookie = os.getenv("AOC_SESSION")
        self.input_path = os.path.join(os.getcwd(), str(self.year), "day" + str(self.day), "test.txt")

    def load_input(self):
        with open(self.input_path, "r") as f:
            self.input_content = f.read().strip()

    def submit(self, part, result):
        url = f"https://adventofcode.com/{self.year}/day/{self.day}/answer"
        data = {"level": part, "answer": str(result)}
        headers = {"Cookie": f"session={self.session_cookie}"}
        response = requests.post(url, data=data, headers=headers)

        if response.status_code == 200:
            if "<article><p>" in response.text:
                start_index = response.text.index("<article><p>") + len("<article><p>")
                end_index = response.text.index("</p></article>")
                feedback = response.text[start_index:end_index]
                print(f"Part {part} answer submission feedback: {feedback}")
            else:
                print(f"Part {part} answer submitted successfully!")
        else:
            print(f"Error submitting Part {part} answer. Status code: {response.status_code}")

class Day:
    def __init__(self, aoc_utils):
        self.aoc_utils = aoc_utils
        self.grid = None

    def load_grid(self):
        self.aoc_utils.load_input()
        self.grid = [[c for c in line] for line in self.aoc_utils.input_content.split("\n")]

    def pretty_print_grid(self):
        for line in self.grid:
            print("".join(line))

    def solve_part1(self):
        self.load_grid()
        self.pretty_print_grid()
        
        res = 0
        
        
        return res

    def solve_part2(self):
        res = 0
        return res

if __name__ == "__main__":
    year = int("%year%")
    day = int("%day%")

    aoc_utils = AocUtils(year, day)
    solver = Day(aoc_utils)

    solver.load_grid()
    solver.pretty_print_grid()

    part1_result = solver.solve_part1()
    print("Solution to Part 1:", part1_result)

    part2_result = solver.solve_part2()
    print("Solution to Part 2:", part2_result)

# Access grid-related utility methods
print(GridUtils.cardinal_directions())
print(GridUtils.find_in_grid(solver.grid, 'x'))