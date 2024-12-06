import os

class Day5:
    def __init__(self):
        self.input_content = None

    def solve_part1(self):
    
        rules, updates = self.parseInput()

        sum = 0

        for order in updates:
            if self.verifyOrderIsCorrect(rules, order):
                sum += order[len(order) // 2]
            
        
        return sum
    
    
    def fixOrdering(self, rules, order): 
        rulesMap = dict()
        
        keys = set()
        for rule in rules:
            keys.add(rule[0])
            keys.add(rule[1])
        
        for key in keys:
            after = [rule[1] for rule in rules if rule[0] == key]
            rulesMap[key] = after
        
        for i in range(len(order)):
            for j in range(i+1, len(order)):
                if order[j] in rulesMap[order[i]]:
                    order[i], order[j] = order[j], order[i]
        
        return order
    
    def verifyOrderIsCorrect(self, rules, order):  
        for rule in rules:
            before, after = rule
            
            if before not in order or after not in order:
                continue
  
            if order.index(before) > order.index(after):
                return False
            
        return True
        
    
    def parseInput(self):
        sections = self.input_content.split("\n\n")
        
        rules = []
        updates = []
        
        for line in sections[0].split('\n'):
            if line:
                x, y = map(int, line.split('|'))
                rules.append((int(x), int(y)))    
        
        for line in sections[1].split('\n'):
            values = line.split(',')
            values = [int(x) for x in values]
            updates.append(values)
        
        return rules, updates
    
    def solve_part2(self):
        rules, updates = self.parseInput()

        sum = 0

        for order in updates:
            if not self.verifyOrderIsCorrect(rules, order):
                order = self.fixOrdering(rules, order)
                sum += order[len(order) // 2]
            
        return sum

    def loadInputFiles(self):
        inputPath = os.path.join(os.getcwd(), "2024", "day5", "input.txt")
        with open(inputPath, "r") as f:
            self.input_content = f.read()
            
    def loadGrid(self):
        self.grid = [[c for c in line] for line in self.input_content.split("\n")]
        
    def prettyPrintGrid(self):
        for line in self.grid:
            print(line)

solver = Day5()
solver.loadInputFiles()

part1_result = solver.solve_part1()
print("Solution to Part 1:", part1_result)

part2_result = solver.solve_part2()
print("Solution to Part 2:", part2_result)
