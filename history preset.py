import sys
from pprint import pprint
input = sys.stdin.readline

event = []
time = []

while True:
    line = input().strip()
    if not line:
        break
    t, e = line.split(') ')
    t = t[:(t.index('('))]
    for _ in ['년', '월', '일']:
        t = t.replace(_, '')
    time.append(t)
    if e[-1] == '.':
        e = e[:-1]
    event.append(e)

pprint(event)
print()
pprint(time)

print(len(time), len(event))