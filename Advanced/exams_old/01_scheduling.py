# jobs = [int(i) for i in input().split(', ')]
# copy_jobs = jobs.copy()
#
# index = int(input())
# biggest = jobs[index]
#
# total_jobs = 0
#
# found = False
#
# while True:
#     min_num = min(jobs)
#     min_num_index = jobs.index(min_num)
#     for i in range(len(jobs)):
#         if min_num == biggest and i == index:
#             found = True
#             total_jobs += jobs[i]
#             break
#         if jobs[i] <= biggest and jobs[i] == min_num:
#             total_jobs += jobs[i]
#             jobs[i] = 99999999999999
#             break
#
#     if found:
#         break
#
# print(total_jobs)
#
# #
# # a = 5
#
# # 3, 2, 1, 10, 1, 2
# # 0
# #
# # 4, 10, 10, 6, 2, 99
# # 2

from collections import deque as dq
jobs = dq([int(x) for x in input().split(', ')])
job_index = int(input())

target_job = jobs[job_index]
jobs_before_target = [x for x in jobs if x <= target_job]
cycles = sum(jobs_before_target)

print(cycles)