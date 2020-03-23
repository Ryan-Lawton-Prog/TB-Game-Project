save = open('save.txt', 'r')
load = []

for line in save:
 line = line.strip()
 load.append(line)
print load
