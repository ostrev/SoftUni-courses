import math

centuries = int(input())

print(f'{centuries} centuries = {centuries * 100} years = {math.trunc(36524.22 * centuries)} days = {(math.trunc(36524.22 * centuries)) * 24} hours = {(math.trunc(36524.22 * centuries)) * 24 * 60} minutes')