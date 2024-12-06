import os
import requests

YEAR = 2023
DAY = 5
COOKIES = os.getenv('AOC_SESSION')


def generate():
    folder = os.path.dirname(os.path.abspath(__file__))
    parent_folder = os.path.dirname(folder) 
    year_folder = os.path.join(parent_folder, str(YEAR))
    day_folder = os.path.join(year_folder, "day"+str(DAY))
    os.makedirs(day_folder, exist_ok=True)
    
    day_txt = os.path.join(folder, "day.py")
    time_txt = os.path.join(folder, "timetaken.txt")
    
    with open(day_txt, 'r') as file:
        day_content = file.read().replace('%year%', str(YEAR)).replace('%day%', str(DAY))
        day_content = day_content.replace('Day', 'Day'+str(DAY))
        with open(os.path.join(day_folder, "day"+str(DAY)+".py"), 'w') as day_file:
            day_file.write(day_content)
    
    with open(time_txt, 'r') as file:
        time_content = file.read().replace('%year%', str(YEAR)).replace('%day%', str(DAY))
        with open(os.path.join(day_folder, "timetaken.txt"), 'w') as time_file:
            time_file.write(time_content)
            
    with open(os.path.join(day_folder, "input.txt"), 'w') as input_file:
        input_data = input()
        input_file.write(input_data)
    
    with open(os.path.join(day_folder, "test.txt"), 'w') as test_file:
        pass


def input():
    url = f"https://adventofcode.com/{YEAR}/day/{DAY}/input"
    headers = {
        "cookie": f"{COOKIES}"
    }
    
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        input_data = response.text.strip()
        return input_data
    else:
        print("Failed to fetch input from Advent of Code website")



generate()
