import os

class Day12:
    def __init__(self):
        self.input_content = None

    def solve_part1(self):
        self.loadGrid()
        self.prettyPrintGrid()
        
        return 0
    
    def solve_part2(self):
        return 0

    def loadInputFiles(self):
        inputPath = os.path.join(os.getcwd(), "2023", "day12", "test.txt")
        with open(inputPath, "r") as f:
            self.input_content = f.read()
            
    def loadGrid(self):
        self.grid = [[c for c in line] for line in self.input_content.split("\n")]
        
    def prettyPrintGrid(self):
        for line in self.grid:
            print(line)

solver = Day12()
solver.loadInputFiles()

part1_result = solver.solve_part1()
print("Solution to Part 1:", part1_result)

part2_result = solver.solve_part2()
print("Solution to Part 2:", part2_result)
