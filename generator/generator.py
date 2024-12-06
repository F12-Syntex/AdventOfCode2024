import os
import requests
import calendar

COOKIES = os.getenv('AOC_SESSION')


def generate(year = calendar.datetime.datetime.now().year, day = calendar.datetime.datetime.now().day):
        
    folder = os.path.dirname(os.path.abspath(__file__))
    parent_folder = os.path.dirname(folder) 
    
    year_folder = os.path.join(parent_folder, str(year))
    day_folder = os.path.join(year_folder, "day"+str(day))
    
    if os.path.exists(day_folder):
        print(f"Day {day} already exists")
        return
    
    os.makedirs(day_folder, exist_ok=True)
    
    day_txt = os.path.join(folder, "day.py")
    time_txt = os.path.join(folder, "timetaken.txt")    
    
    with open(day_txt, 'r') as file:
        print(f"Generating Day {day} for Year {year}")
        day_content = file.read().replace('%year%', str(year)).replace('%day%', str(day)).replace('%cookies%', COOKIES)
        day_content = day_content.replace('Day', 'Day'+str(day))
        with open(os.path.join(day_folder, "day"+str(day)+".py"), 'w') as day_file:
            day_file.write(day_content)
    
    with open(time_txt, 'r') as file:
        print(f"Generating timetaken.txt for Day {day} in Year {year}")
        time_content = file.read().replace('%year%', str(year)).replace('%day%', str(day))
        with open(os.path.join(day_folder, "timetaken.txt"), 'w') as time_file:
            time_file.write(time_content)
            
    with open(os.path.join(day_folder, "input.txt"), 'w') as input_file:
        print(f"Fetching input for Day {day} in Year {year}")
        input_data = input(year, day)
        input_file.write(input_data)
    
    with open(os.path.join(day_folder, "test.txt"), 'w') as test_file:
        print(f"Fetching test input for Day {day} in Year {year}")
        test_data = testInput(year, day)
        test_file.write(test_data)

def testInput(year = calendar.datetime.datetime.now().year, day = calendar.datetime.datetime.now().day):
    url = f"https://adventofcode.com/{year}/day/{day}"
    headers = {
        "cookie": f"{COOKIES}"
    }
    
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        test_data = response.text
        test_data = test_data[test_data.find('For example'):]
        test_data = test_data[test_data.find('<code>')+6:test_data.find('</code>')]
        return test_data
    else:
        print("Failed to fetch test input from Advent of Code website")
    

def input(year = calendar.datetime.datetime.now().year, day = calendar.datetime.datetime.now().day):
    url = f"https://adventofcode.com/{year}/day/{day}/input"
    headers = {
        "cookie": f"{COOKIES}"
    }
    
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        input_data = response.text.strip()
        return input_data
    else:
        print("Failed to fetch input from Advent of Code website")


generate(year=2018, day=6)
