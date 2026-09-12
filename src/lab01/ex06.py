n = int(input())
online = 0
offline = 0
for i in range(n):
    line = input().strip()
    parts = line.split()
    format_type = parts[-1]
    if format_type == "True": online += 1
    else: offline += 1
print(online, offline)