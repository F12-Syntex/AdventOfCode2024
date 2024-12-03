import os

class Day:
    def __init__(self):
        self.input_content = None

    def solve_part1(self):
        self.loadGrid()
        
        t1 = []
        t2 = []
        
        for row in self.grid:
            row = "".join(row).strip().split(" ")
            row = [x for x in row if x]
            t1.append(int(row[0]))
            t2.append(int(row[1]))
        
        sorted_t1 = sorted(t1)
        sorted_t2 = sorted(t2)
        
        
        s1 = 0
        for i in range(len(t1)):
            s1 += abs(sorted_t1[i] - sorted_t2[i])
        
        return s1
        
    def solve_part2(self):
        self.loadGrid()
        
        t1 = []
        t2 = []
        
        for row in self.grid:
            row = "".join(row).strip().split(" ")
            row = [x for x in row if x]
            t1.append(int(row[0]))
            t2.append(int(row[1]))
        
        score = 0
        for i in range(len(t1)):
            number = t1[i]
            similarity = t2.count(number)
            score += number * similarity
        
        return score

    def loadInputFiles(self):
        inputPath = os.path.join(os.getcwd(), "2024", "day1", "input.txt")
        with open(inputPath, "r") as f:
            self.input_content = f.read()
            
    def loadGrid(self):
        self.grid = [[c for c in line] for line in self.input_content.split("\n")]
        
    def prettyPrintGrid(self):
        for line in self.grid:
            print(line)

solver = Day()
solver.loadInputFiles()

part1_result = solver.solve_part1()
print("Solution to Part 1:", part1_result)

part2_result = solver.solve_part2()
print("Solution to Part 2:", part2_result)
