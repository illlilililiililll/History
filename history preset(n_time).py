import sys
from pprint import pprint
input = sys.stdin.readline

n_time = []
while True:
    year = input().strip().strip(",").strip("'")
    if not year:
        break
    try:
        y, m, d = year.split(' ')
    except ValueError:
        y, m = year.split(' ')
    n_year = y+' '+m
    n_time.append(n_year)

print('n_time = ', end='')
pprint(n_time)

print(len(n_time))