from random import randint
import time
weapon_inv = [['Beginner Sword', 1, 12, 'warrior'], ['Beginner Staff', 1, 12, 'mage'], ['Beginner Bow', 1, 12, 'archer']]
weapon = ['name', 1]
print weapon_inv
weapon_inv.pop(1)
print weapon_inv
while False:
    listn = []
    print "Weapon Equiped:  %s: %s" % (weapon[0], weapon[1])
    for list in weapons_inv:
       print "%s: Class = %s, Damage = %s, $%s" % (list[0], list[3], list[1], list[2])
       listn.append([list[0], list[1]])

    equip = raw_input("Type what you would like to equip or hit enter: ")
    equip = equip.lower()
    for list in listn:
        z = list[0].lower()
        if equip == z:
            weapon[0] = list[0]
            weapon[1] = list[1]
            print "You have equipped a '%s'" % weapon[0]
            print ""

while False:
    num = 0
    weapon_class = randint(1, 3)
    if weapon_class == 1:
       cl = 'warrior'
       names = ['Adze', 'Apprentice Broad Axe', 'Arch Axe', 'Arreat Axe', 'Balestarius', 'Battle Axe', 'Broad Axe', 'Bullova', 'Chopper', 'Cresent Axe', 'Double Axe', 'Exalted Galraki', 'Galraki', 'Grand Master Ono', 'Hand Axe', 'Hatchet', 'Heavy Axe', 'Journeyman Heavy Axe', 'Marauder Axe', 'Masakari', 'Master Soldier Axe', 'Ono', 'Reaver', 'Soldier Axe', 'Tomahawk', 'Ancient Sword', 'Bastard Sword', 'Battle Sword', 'Broadsword', 'Conquest Sword', 'Cutlass', 'Dao', 'Exalted Conquest Sword', 'Falchion', 'Gladius', 'Illustrious Raid Sword', 'King Blade', 'Knight Sword', 'Longsword', 'Master Bastard Sword', 'Pirate Sword', 'Raid Sword', 'Resplendent Strong Sword', 'Rune Sword', 'Sabre', 'Saif']
    elif weapon_class == 2:
       cl = 'mage'
       names = ['Adept Hunting Bow', 'Battle Bow', 'Composite Bow', 'Daikyu', 'Exalted phantom Bow', 'Glorius Sniper Bow', 'Grand Master Siege Bow', 'Hankyu', 'Higoyumi', 'Hunting Bow', 'Long Bow', 'Longshot Bow', 'Magnificient Higoyumi', 'Maruki', 'Phantom Bow', 'Ranger Bow', 'Recurve Bow', 'Revenant Bow', 'Short Bow', 'Siege Bow', 'Sniper Bow', 'Warden Bow', 'Yumi', 'Apprentice Light Crossbow', 'Arbalest', 'Chokonu', 'Cranequin', 'Crossbow', 'Doomcaster', 'Dread Crossbow', 'Exalted Doomcaster', 'Heavy Crossbow', 'Heavy Siege Crossbow', 'Hellion Crossbow', 'Lian Nu', 'Light Crossbow', 'Nayin', 'Porcupine', 'Quarrelbow', 'Scorpian', 'Siege Crossbow', 'Slingbow', 'Stonebow', 'War Caster', 'War Crossbow', 'Windlass']
    elif weapon_class == 3:
       cl = 'archer'
       names = ['Adept Enchanter Wand', 'Apprentice Lesser Wand', 'Apprentice\'s Wand', 'Archmage Wand', 'Battle Wand', 'Desolator Wand', 'Divination Wand', 'Duelist Wand', 'Enchanter Wand', 'Exalted Strike Wand', 'Glorious Arch Mage Wand', 'Greater Wand', 'Grim Wand', 'Guardian', 'Jade Wand', 'Journeyman Steel Wand', 'Lesser Wand', 'Magnificent Greater Wand', 'Magus Wand', 'Master Grim Wand', 'Mentor Wand', 'Oak Wand', 'Petrified Wand', 'Silversteel Wand', 'Sorcery Wand', 'Arcane Staff', 'Archaic Staff', 'Battle Staff', 'Bone Staff', 'Conquest Staff', 'Elder Staff', 'Exalted Mythical Staff', 'Gnarled Staff', 'High Priest Staff', 'Hyperion Staff', 'Long Staff', 'Master War Staff', 'Mentor Staff', 'Mythical Staff', 'Obsidian Staff', 'Petrified Staff', 'Primordial Staff', 'Shamanic Staff', 'Short Staff', 'Sovereign Staff', 'Styfian Staff']
    weapon_name = names[randint(0,45)]
    for list in weapon_inv:
       if weapon_name in list[0]:
           num += 1
       print list
    if num > 0:
        weapon_name = '%s(%s)' % (weapon_name, num)
    weapon_damage = int(1 / 0.5)
    weapon_value = 20 / 0.5
    weapon_class = 'archer'
    new_weapon = [weapon_name, weapon_damage, weapon_value, weapon_class]
    weapon_inv.append(new_weapon)
    time.sleep(1)
    print ""
