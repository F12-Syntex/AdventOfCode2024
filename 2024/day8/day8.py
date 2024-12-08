import os
import requests
import time

class Stopwatch:
    def __init__(self):
        self.start_time = time.time() * 1000 
    
    def mark(self):
        current_time = time.time() * 1000 
        elapsed_time = current_time - self.start_time 
        self.start_time = current_time 
        return elapsed_time 

class AocUtils:
    def __init__(self, year, day):
        self.year = year
        self.day = day
        self.session_cookie = os.getenv("AOC_SESSION")
        
    def load_input(self, file):
        self.input_path = os.path.join(os.getcwd(), str(self.year), "day" + str(self.day), file+".txt")
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

class Day8:
    def __init__(self, aoc_utils):
        self.aoc_utils = aoc_utils
        self.grid = None
        self.aoc_utils.load_input("input")
        self.input_content = self.aoc_utils.input_content

    def load_grid(self):
        self.grid = [[c for c in line] for line in self.input_content.split("\n")]

    def pretty_print_grid(self):
        for line in self.grid:
            print("".join(line))

    def solve_part1(self):
        self.load_grid()
        antinodes = set()
        
        for _, locations in self.find_frequencies().items():
            for i, (x1, y1) in enumerate(locations):
                for _, (x2, y2) in enumerate(locations[i+1:], i+1):
                    antinodes.update(self.find_antinodes_part1(x1, y1, x2, y2))

        return len(antinodes)
        
    def find_antinodes_part1(self, x1, y1, x2, y2):
        dx = x2 - x1
        dy = y2 - y1
        distance = ((dx * dx + dy * dy) ** 0.5)
        
        if distance == 0:
            return []
        
        ratio = 2
        ax1 = x2 + (x2 - x1) / (ratio - 1)
        ay1 = y2 + (y2 - y1) / (ratio - 1)
        
        ax2 = x1 - (x2 - x1) / (ratio - 1)
        ay2 = y1 - (y2 - y1) / (ratio - 1)
        
        antinodes = []
        
        if (0 <= round(ax1) < len(self.grid[0]) and 
            0 <= round(ay1) < len(self.grid)):
            antinodes.append((round(ax1), round(ay1)))
            
        if (0 <= round(ax2) < len(self.grid[0]) and 
            0 <= round(ay2) < len(self.grid)):
            antinodes.append((round(ax2), round(ay2)))
        
        return antinodes

    def find_antinodes_part2(self, x1, y1, x2, y2):
        antinodes = set()
        antinodes.add((x1, y1))
        antinodes.add((x2, y2))
        
        for y in range(len(self.grid)):
            for x in range(len(self.grid[0])):
                if (x, y) == (x1, y1) or (x, y) == (x2, y2):
                    continue
                if (x2 - x1) * (y - y1) == (y2 - y1) * (x - x1):
                    antinodes.add((x, y))
        
        
        return antinodes

    def find_frequencies(self):
        frequencies = {}
        for y, row in enumerate(self.grid):
            for x, cell in enumerate(row):
                if cell != ".":
                    if cell not in frequencies:
                        frequencies[cell] = []
                    frequencies[cell].append((x, y))
        return frequencies

    def solve_part2(self):
        self.load_grid()
        antinodes = set()
        
        for _, locations in self.find_frequencies().items():
            for x, y in locations:
                antinodes.add((x, y))
            
            for i, (x1, y1) in enumerate(locations):
                for _, (x2, y2) in enumerate(locations[i+1:], i+1):
                    found = self.find_antinodes_part2(x1, y1, x2, y2)
                    antinodes.update(found)

        return len(antinodes)

if __name__ == "__main__":
    year = int("2024")
    day = int("8")

    aoc_utils = AocUtils(year, day)
    solver = Day8(aoc_utils)

    stopwatch = Stopwatch()

    part1_result = solver.solve_part1()
    print("Solution to Part 1:", part1_result, "(", round(stopwatch.mark()), "ms )")

    part2_result = solver.solve_part2()
    print("Solution to Part 2:", part2_result, "(", round(stopwatch.mark()), "ms )")