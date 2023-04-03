print("Ex.5.1")
import glob
import os

def find_pdf_size(top):
    pdf_files = glob.glob(os.path.join(top, '**/*.pdf'), recursive=True)
    total_size = sum(os.path.getsize(file_path) for file_path in pdf_files)
    return total_size

print(find_pdf_size('.'))

print("Ex.5.2")

import datetime

def print_working_days(date1, date2):
    start_date = datetime.datetime.strptime(date1, '%Y-%m-%d')
    end_date = datetime.datetime.strptime(date2, '%Y-%m-%d')

    for current_date in (start_date + datetime.timedelta(n) for n in range((end_date - start_date).days)):
        if current_date.weekday() < 5:
            print(current_date.strftime('%Y-%m-%d'))

print_working_days('2023-03-28', '2023-04-05')

print("Ex.5.3")

import random
from itertools import accumulate

def random_walk(start):
    steps = (random.choice([-1, 1]) for _ in range(100))
    positions = accumulate(steps, initial=start)
    return positions

final_positions = list(map(lambda start: list(random_walk(start))[-1], range(3)))
print(final_positions)


