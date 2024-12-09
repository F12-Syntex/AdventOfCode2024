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

class Day9:
    def __init__(self, aoc_utils):
        self.aoc_utils = aoc_utils
        self.grid = None
        self.aoc_utils.load_input("test")
        self.input_content = self.aoc_utils.input_content

    def load_grid(self):
        self.grid = [list(line) for line in self.input_content.split("\n")]

    def pretty_print_grid(self):
        for line in self.grid:
            print("".join(line))

    def get_files(self):
        line = self.input_content.split("\n")[0]
        files = []
        id = 0
        for i in range(0, len(line), 2):
            files.append((int(line[i]), id))
            if i + 1 < len(line):
                files.append(int(line[i + 1]))
            id += 1
        files.append(0)
        return files

    def get_word(self, files):
        parts = []
        for file in files:
            if isinstance(file, int):
                parts.append('.' * file)
            else:
                parts.append(str(file[1]) * file[0])
        return ''.join(parts)
    
    def find_first_empty_space(self, word):
        try:
            return word.index('.')
        except ValueError:
            return -1
        
    
    def left_shift(self, word_list):
        for i in range(len(word_list) - 2, -1, -1):
            if word_list[i] != '.':
                id = word_list[i]
                start_index = i
                
                #find end of segment
                end_index = start_index
                while end_index < len(word_list) and word_list[end_index] == id:
                    end_index += 1
                end_index -= 1
                
                #find first empty space
                empty_space = self.find_first_empty_space(word_list)
                
                #shift segment
                segment_length = end_index - start_index + 1
                for j in range(segment_length):
                    word_list[empty_space + j] = id
                    word_list[start_index + j] = '.'
                
                break
        
        return ''.join(word_list)

    def defragmented(self, word):
        stripped = word.rstrip('.')
        return '.' not in stripped


    def find_required_defragmentation(self, word):
        chains = 0
        chain = False
        
        for i in range(len(word)):
            if word[i] == '.':
                if not chain:
                    chains += 1
                    chain = True
            else:
                chain = False
                
        return chains

    def solve_part1(self):
        files = self.get_files()
        word = self.get_word(files)
        word_list = list(word)

        chains = self.find_required_defragmentation(word)
        c = 0
        while not self.defragmented(word):
            word = self.left_shift(word_list)
            word_list = list(word)
            c+=1
            if c % 1000 == 0:
                print(c, chains)
        
        checksum = 0
        for i, char in enumerate(word):
            if char == '.':
                break
            checksum += i * int(char)
        
        return checksum

    def solve_part2(self):
        return 0

if __name__ == "__main__":
    year = int("2024")
    day = int("9")

    aoc_utils = AocUtils(year, day)
    solver = Day9(aoc_utils)

    stopwatch = Stopwatch()

    part1_result = solver.solve_part1()
    print("Solution to Part 1:", part1_result, "(", round(stopwatch.mark()), "ms )")

    part2_result = solver.solve_part2()
    print("Solution to Part 2:", part2_result, "(", round(stopwatch.mark()), "ms )")