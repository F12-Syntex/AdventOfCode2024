import os

class Day4:
    def __init__(self):
        self.input_content = None
        self.grid = None
        self.rows = 0
        self.cols = 0

    def solve_part1(self):
        self.loadGrid()
        
        directions = [
            (0, 1),  
            (1, 0),   
            (1, 1),  
            (1, -1),  
            (-1, 1),  
            (-1, -1),
            (-1, 0), 
            (0, -1)  
        ]
        
        return self.count_xmas_occurrences(directions, "XMAS")
    
    def solve_part2(self):
        self.loadGrid()
        count = 0
        
        for row in range(1, self.rows - 1):
            for col in range(1, self.cols - 1):
                if self.grid[row][col] != 'A':
                    continue
                    
                TopLeft = self.grid[row-1][col-1]
                TopRight = self.grid[row-1][col+1]
                BottomLeft = self.grid[row+1][col-1]
                BottomRight = self.grid[row+1][col+1]
                
                word = TopLeft + BottomRight + TopRight + BottomLeft
                
                if word == "MSMS" or word == "SMSM" or word == "MSSM" or word == "SMMS":
                    count += 1
                
        return count

    def loadInputFiles(self):
        inputPath = os.path.join(os.getcwd(), "2024", "day4", "test.txt")
        with open(inputPath, "r") as f:
            self.input_content = f.read().strip()
            
    def loadGrid(self):
        self.grid = [[c for c in line] for line in self.input_content.split("\n")]
        self.rows = len(self.grid)
        self.cols = len(self.grid[0]) if self.rows > 0 else 0

    def check_direction(self, row, col, dx, dy, target):
        length = len(target)
        if (0 <= row + (length - 1)*dx < self.rows and 
            0 <= col + (length - 1)*dy < self.cols):
            word = ""
            for i in range(len(target)):
                word += self.grid[row + i*dx][col + i*dy]
            return word == target
        return False

    def count_xmas_occurrences(self, directions, target):
        count = 0
        for row in range(self.rows):
            for col in range(self.cols):
                for dx, dy in directions:
                    if self.check_direction(row, col, dx, dy, target):
                        count += 1
        return count

solver = Day4()
solver.loadInputFiles()

part1_result = solver.solve_part1()
print("Solution to Part 1:", part1_result)

part2_result = solver.solve_part2()
print("Solution to Part 2:", part2_result)