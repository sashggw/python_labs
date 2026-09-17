print("in_1: ", end="")
n = int(input())
lines = []
online = 0
offline = 0
for i in range(n):
    print(f"in_{i + 2}: ", end="")
    lines.append(input())
for line in lines:
    parts = line.split()
    if parts[-1] == "True": online += 1
    else: offline += 1
print(f"out: {online} {offline}")
