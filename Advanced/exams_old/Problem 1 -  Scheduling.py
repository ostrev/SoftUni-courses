import sys
from collections import deque as dq

jobs = [int(s) for s in input().split(', ')]
index_num = int(input())

count = 0
current_index = None

while True:
    min_job = sys.maxsize
    for job in jobs:
        try:
            if job < min_job:
                min_job = job
        except TypeError:
            continue
    count += min_job
    current_index = jobs.index(min_job)
    jobs[current_index] = 'P'
    if current_index == index_num:
        break

print(count)