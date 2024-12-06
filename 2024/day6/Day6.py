import os
import time

class Day6:
    def __init__(self):
        self.input_content = None

    def solve_part1(self):
        self.loadGrid()
        
        guard = self.locateGuard()
        direction = (-1, 0)
        
        locations = set()
        locations.add(guard) 
        
        while True:
            next = (guard[0] + direction[0], guard[1] + direction[1])
            
            if not self.inRange(next[0], next[1]):
                break
                
            if self.grid[next[0]][next[1]] == "#":
                direction = self.turnRight(direction)
                continue
            
            guard = next
            locations.add(guard)
            
        return len(locations)
    
    def causesLoop(self, i, j):
        guard = self.locateGuard()
        direction = (-1, 0)
        
        visited = set()
        
        while True:
            state = (guard, direction)
            
            if state in visited:
                return True
            
            visited.add(state)
            
            next = (guard[0] + direction[0], guard[1] + direction[1])
            
            if not self.inRange(next[0], next[1]):
                return False
                
            if self.grid[next[0]][next[1]] == "#" or (next[0] == i and next[1] == j):
                direction = self.turnRight(direction)
                continue
            
            guard = next
            
            if len(visited) > len(self.grid) * len(self.grid[0]) * 4:
                return False
    
    def inRange(self, i, j):
        return i >= 0 and i < len(self.grid) and j >= 0 and j < len(self.grid[0])
    
    def turnRight(self, direction):
        if direction == (-1, 0):    
            return (0, 1)
        elif direction == (0, 1):   
            return (1, 0)
        elif direction == (1, 0):   
            return (0, -1)
        elif direction == (0, -1):   
            return (-1, 0)
    
    def locateGuard(self):
        for i, row in enumerate(self.grid):
            for j, cell in enumerate(row):
                if cell == "^":
                    return (i, j)
        return None
    
    def solve_part2(self):
        self.loadGrid()
        
        guard = self.locateGuard()
        loop_count = 0

        for i in range(len(self.grid)):
            for j in range(len(self.grid[i])):
                if self.grid[i][j] == "." and (i, j) != guard:
                    if self.causesLoop(i, j):
                        loop_count += 1

        return loop_count

    def loadInputFiles(self):
        inputPath = os.path.join(os.getcwd(), "2024", "day6", "input.txt")
        with open(inputPath, "r") as f:
            self.input_content = f.read().strip()
            
    def loadGrid(self):
        self.grid = [[c for c in line] for line in self.input_content.split("\n")]
        
    def prettyPrintGrid(self):
        for line in self.grid:
            print(''.join(line))

solver = Day6()
solver.loadInputFiles()

startTime = int(round(time.time() * 1000))

part1_result = solver.solve_part1()
endTime = int(round(time.time() * 1000))
print("Solution to Part 1:", part1_result, "Time:", endTime - startTime, "ms")

startTime = int(round(time.time() * 1000))

part2_result = solver.solve_part2()
endTime = int(round(time.time() * 1000))
print("Solution to Part 2:", part2_result, "Time:", endTime - startTime, "ms")