from random import randint
import time
while True:
    weapon_class = randint(1, 3)
    if weapon_class == 1:
        names = ['Adze', 'Apprentice Broad Axe', 'Arch Axe', 'Arreat Axe', 'Balestarius', 'Battle Axe', 'Broad Axe', 'Bullova', 'Chopper', 'Cresent Axe', 'Double Axe', 'Exalted Galraki', 'Galraki', 'Grand Master Ono', 'Hand Axe', 'Hatchet', 'Heavy Axe', 'Journeyman Heavy Axe', 'Marauder Axe', 'Masakari', 'Master Soldier Axe', 'Ono', 'Reaver', 'Soldier Axe', 'Tomahawk', 'Ancient Sword', 'Bastard Sword', 'Battle Sword', 'Broadsword', 'Conquest Sword', 'Cutlass', 'Dao', 'Exalted Conquest Sword', 'Falchion', 'Gladius', 'Illustrious Raid Sword', 'King Blade', 'Knight Sword', 'Longsword', 'Master Bastard Sword', 'Pirate Sword', 'Raid Sword', 'Resplendent Strong Sword', 'Rune Sword', 'Sabre', 'Saif']
    elif weapon_class == 2:
        names = ['Adept Hunting Bow', 'Battle Bow', 'Composite Bow', 'Daikyu', 'Exalted phantom Bow', 'Glorius Sniper Bow', 'Grand Master Siege Bow', 'Hankyu', 'Higoyumi', 'Hunting Bow', 'Long Bow', 'Longshot Bow', 'Magnificient Higoyumi', 'Maruki', 'Phantom Bow', 'Ranger Bow', 'Recurve Bow', 'Revenant Bow', 'Short Bow', 'Siege Bow', 'Sniper Bow', 'Warden Bow', 'Yumi', 'Apprentice Light Crossbow', 'Arbalest', 'Chokonu', 'Cranequin', 'Crossbow', 'Doomcaster', 'Dread Crossbow', 'Exalted Doomcaster', 'Heavy Crossbow', 'Heavy Siege Crossbow', 'Hellion Crossbow', 'Lian Nu', 'Light Crossbow', 'Nayin', 'Porcupine', 'Quarrelbow', 'Scorpian', 'Siege Crossbow', 'Slingbow', 'Stonebow', 'War Caster', 'War Crossbow', 'Windlass']
    elif weapon_class == 3:
        names = ['Adept Enchanter Wand', 'Apprentice Lesser Wand', 'Apprentice\'s Wand', 'Archmage Wand', 'Battle Wand', 'Desolator Wand', 'Divination Wand', 'Duelist Wand', 'Enchanter Wand', 'Exalted Strike Wand', 'Glorious Arch Mage Wand', 'Greater Wand', 'Grim Wand', 'Guardian', 'Jade Wand', 'Journeyman Steel Wand', 'Lesser Wand', 'Magnificent Greater Wand', 'Magus Wand', 'Master Grim Wand', 'Mentor Wand', 'Oak Wand', 'Petrified Wand', 'Silversteel Wand', 'Sorcery Wand', 'Arcane Staff', 'Archaic Staff', 'Battle Staff', 'Bone Staff', 'Conquest Staff', 'Elder Staff', 'Exalted Mythical Staff', 'Gnarled Staff', 'High Priest Staff', 'Hyperion Staff', 'Long Staff', 'Master War Staff', 'Mentor Staff', 'Mythical Staff', 'Obsidian Staff', 'Petrified Staff', 'Primordial Staff', 'Shamanic Staff', 'Short Staff', 'Sovereign Staff', 'Styfian Staff']
    weapon = names[randint(0,45)]
    print weapon
    lvl = randint(1, 6)
    print lvl
    weapon_damage = lvl / 2
    print weapon_damage
    time.sleep(1)
