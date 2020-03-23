weapon_inv = [['Beginner Sword', 1, 0,'warrior'], ['Beginner Staff', 1, 0,'mage'], ['Beginner Bow', 1, 0,'archer']]
wep = []
save = open('saveWep.txt', 'w')
for list in  weapon_inv:
    s = '%s,%s,%s,%s' % (list[0], list[1], list[2], list[3])
    save.write(str(s)+"\n")

save.close()

save = open('saveWep.txt', 'r')

load = []

for line in save:
     name, damage, cost, classs = line.strip().split(',')
     new_weapon = [name, int(damage), int(cost), classs]
     load.append(new_weapon)

print load
save.close()
