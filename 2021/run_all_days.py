import time
import os

last_day = max([int(file.split('.')[0][3:].split('_')[0]) for file in os.listdir() if file[0:3] == 'day'])
for day in range(1, last_day + 1):
    print(f'--- Day {day} ---')
    file_name = 'day' + str(day) + '.py'
    exec(open(file_name).read())
    print()