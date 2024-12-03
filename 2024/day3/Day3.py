import os

class Day:
    def __init__(self):
        self.input_content = None

    def solve_part1(self):

        sum = 0

        for mul in self.input_content.split("mul("):
            if ")" not in mul:
                continue
            
            mul = mul.split(")")[0].split(",")
            mul = [int(x) for x in mul if x.isdigit()]
            
            if len(mul) != 2:
                continue
            
            mul = mul[0] * mul[1]
            sum += mul

        return sum
    
    def solve_part2(self):

        mul = [i for i in range(len(self.input_content)) if self.input_content.startswith("mul(", i)]
        do = [i for i in range(len(self.input_content)) if self.input_content.startswith("do()", i)]
        dont = [i for i in range(len(self.input_content)) if self.input_content.startswith("don't()", i)]
        
        sum = 0
        
        state = True
        
        for i in range(len(mul)):
            index = mul[i]
            mul[i] = self.input_content[mul[i]:].split(")")[0] + ")"
            
            lastDo = do[0] if len(do) > 0 else -1
            lastDont = dont[0] if len(dont) > 0 else -1
            
            if lastDo < index and lastDo != -1:
                state = True
                do.pop(0)
            
            if lastDont < index and lastDont != -1:
                state = False
                dont.pop(0)
                
            if state:
                sum += self.compute(mul[i])

        
        return sum
    
    
    def compute(self, mul):
        mul = mul.split("mul(")[1].split(")")[0].split(",")
        
        numbers = [int(x) for x in mul if x.lstrip("-").isdigit()]
        
        if len(numbers) >= 2:
            return numbers[0] * numbers[1]
        else:
            return 0  

    
    def validate(self, mul):
        if not mul.startswith("mul("):
            return False
        if not mul.endswith(")"):
            return False
        if "," not in mul:
            return False
        
        mul = mul.split("(")[1].split(')')[0].split(",")
        
        if len(mul) != 2:
            return False
        
        for m in mul:
            if not m.isdigit():
                return False
            
        return True
    
    def loadInputFiles(self):
        inputPath = os.path.join(os.getcwd(), "2024", "day3", "test.txt")
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
