import os

class Day:
    def __init__(self):
        self.input_content = None

    def solve_part1(self):
        self.loadGrid()
        self.grid = [[int(c) for c in line] for line in self.grid]
        safe = 0 
        for i in self.grid:
            multiplier = self.checkMultiplier(i)
            check = self.checkValidRow(i, multiplier)
            safe += 1 if check == -1 else 0
            
        return safe
    
    def solve_part2(self):
        self.loadGrid()
        self.grid = [[int(c) for c in line] for line in self.grid]
        safe = 0 
        
        for row in self.grid:
            multiplier = self.checkMultiplier(row)
            if self.checkValidRow(row, multiplier) == -1:
                safe += 1
                continue
                
            isSafe = False
            for i in range(len(row)):
                testRow = row[:i] + row[i+1:]
                if len(testRow) < 2: 
                    continue
                    
                multiplier = self.checkMultiplier(testRow)
                if self.checkValidRow(testRow, multiplier) == -1:
                    isSafe = True
                    break
                    
            safe += 1 if isSafe else 0
                
        return safe
    
    def checkValidRow(self, row, multiplier):
        prev = row[0]
        row = row[1:]
        
        if len(row) < 2:
            return -1
        
        for j in range(len(row)):
            element = row[j]
            difference = (prev - element) * multiplier
            if difference < 1 or difference > 3:
                return j
            prev = element
        
        return -1
    
    def checkMultiplier(self, row):
        return 1 if row[0] - row[1] > 0 else -1

    def loadInputFiles(self):
        inputPath = os.path.join(os.getcwd(), "2024", "day2", "input.txt")
        with open(inputPath, "r") as f:
            self.input_content = f.read()
            
    def loadGrid(self):
        self.grid = [[c for c in line.split(' ')] for line in self.input_content.split("\n")]
        
    def prettyPrintGrid(self):
        for line in self.grid:
            print(line)

solver = Day()
solver.loadInputFiles()

part1_result = solver.solve_part1()
print("Solution to Part 1:", part1_result)

part2_result = solver.solve_part2()
print("Solution to Part 2:", part2_result)