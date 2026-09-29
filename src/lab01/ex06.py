print("in_1: ", end="")
n = int(input())
lines = []
online = 0
offline = 0
for i in range(n):
    line = input().strip()
    parts = line.split()
    if parts[-1] == "True": online += 1
    else: offline += 1
print(online, offline)