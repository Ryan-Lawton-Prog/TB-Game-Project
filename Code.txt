# importing randint from random module
from random import randint
from random import random
from random import uniform
# importing math module
import math
# iompoerting time module
import time

#==================================================================
#= Player ==========================================================
#==================================================================
class Player(object):
   
   # Players Stats
   def __init__(self, name="", max_hp=50, lvl=1, xp=0, strength=0, dexterity=0, vitality=0, x=0,y=0,intelligence=0, script=[], quests=[], drp_ch=0, max_xp=20, money=50, max_mana=20, lessar_potion=5, intro_done=False, potion=0, greater_potion=0, rift_visit=False, rift_first=False, lessar_mana_potion=0, mana_potion=0, first_tavern=False, first_battle=False, greater_mana_potion=0, silver_horn=0, work_bench=0, ocean_gem=0, junk_metal=0, wood=0, iron=0, bronze=0, silver=0, gold=0, steel=0, dragon_blood=0, defence_up=0, weapon=['unknown', 0, 0, 0, 0, 0, 0], weapon_inv=[], plan_rusty_sword=0, plan_wooden_bow=0, plan_wooden_staff=0, companion=False):
      self.name = name
      self.max_hp = max_hp
      self.hp = self.max_hp
      self.lvl = lvl
      self.xp = xp
      self.max_xp = max_xp
      self.money = money
      self.max_mana = max_mana
      self.mana = self.max_mana
      self.lessar_potion = lessar_potion
      self.potion = potion
      self.greater_potion = greater_potion
      self.lessar_mana_potion = lessar_mana_potion
      self.mana_potion = mana_potion
      self.greater_mana_potion = greater_mana_potion
      self.silver_horn = silver_horn
      self.work_bench = work_bench
      self.ocean_gem = ocean_gem
      self.junk_metal = junk_metal
      self.wood = wood
      self.bronze = bronze
      self.iron = iron
      self.steel = steel
      self.silver = silver
      self.gold = gold
      self.dragon_blood = dragon_blood
      self.defence_up = defence_up
      self.weapon = weapon
      self.weapon_inv = weapon_inv
      self.plan_rusty_sword = plan_rusty_sword
      self.plan_wooden_bow = plan_wooden_bow
      self.plan_wooden_staff = plan_wooden_staff
      self.companion = companion
      self.str = strength
      self.int = intelligence
      self.dex = dexterity
      self.vit = vitality
      self.drop = drp_ch
      self.quests = quests
      self.script = script
      self.first_battle = first_battle
      self.rift_first = rift_first
      self.first_tavern = first_tavern
      self.rift_visit = rift_visit
      self.intro_done = intro_done
      self.x = x
      self.y = y
   
   # Options Module
   def get_stats(self):
      message = "\nName: %s\nLevel: %d\nHP: %s / %s\nMP: %s / %s\nXP: %s / %s\n\nQuests:\n" % (self.name, self.lvl, self.hp, self.max_hp, self.mana, self.max_mana, self.xp, self.max_xp)
      for list in self.quests:
         message = '%sName: %s, \n\tDescription:%s\n\tCompletion: %s / %s\nRewards: %s\n' % (message, list[0], list[1], list[2], list[3], list[5])
      return message

   # Mob Encounter Module
   def encounter(self):
      chance = randint(1,2)
      if chance == 1:
         return True
      else:
         return False

   # Level Up Module
   def level_up(self):
      if self.xp >= self.max_xp and self.lvl < 100:
         print "\n*Congragulations! You've leveled up!*\n"
         self.lvl += 1
         if self.lvl == 5:
            if classes == 'warrior':
               print "You have learned the ability: Blind"
            if classes == 'mage':
               print "You have learned the ability: Bubble Shield"
            if classes == 'archer':
               print "You have learned the ability: Multi Shot"
         if self.lvl == 10:
            if classes == 'warrior':
               print "You have learned the ability: Bleed"
            if classes == 'mage':
               print "You have learned the ability: Burn"
            if classes == 'archer':
               print "You have learned the ability: Pierce"
         self.max_hp += randint(5, 10)
         self.hp = self.max_hp
         self.max_mana += 10 * self.lvl- 10
         self.mana = self.max_mana
         self.max_xp += 10 * (self.lvl + (1 / 10 * self.lvl))
         self.xp = 0
      
#==================================================================
#= Enemy ===========================================================
#==================================================================
class Enemy(object):

   # Global Enemy Stats
   def __init__(self, name, max_hp, lvl, xp_given, id_val):
      self.name = name
      self.max_hp = max_hp
      self.hp = self.max_hp
      self.lvl = lvl
      self.xp_given = xp_given
      self.id_val = id_val

#==================================================================
#= Companion =======================================================
#==================================================================
class Companion(object):

   #Companion Stats (Future Update)
   def __init__(self, name="", max_hp=70, lvl=6):
      self.name = name
      self.max_hp = max_hp
      self.hp = self.max_hp
      self.lvl = lvl

#==================================================================
#= Random_Enemy ====================================================
#==================================================================
class Renemy(object):

    def __init__(self, player):
        self.renemy = {
            }
        self.player = player

    # Mob finding Module (For Arcade)
    def mob(self):
         # Mob finder
         mob = randint(0, 10)
         # List of Mobs
         enm = ["Vespoid", "Giant Moth", "Giant Bee", "Bear", "The Eye", "Pegasus", "Soul Eater", "Flame Spitter", "Illusionist", "Python", "Spamirificano" ]
         # Finding Mob name from list via random number from variable mob
         name = enm[mob]
         # base lvl finder
         lvl_one = self.player.lvl - 1
         # max enemy lvl compared to player lvl
         lvl_two = self.player.lvl
         # finding lvl Randomely
         level = randint(lvl_one, lvl_two)
         # Making sure lvl isnt below 1
         if level <= 0:
            level = 1
         # finding base xp to grant
         xp_one = 5 * level - 5
         # finding max xp to grant
         xp_two = 7 * level - 7
         # adding base xp to standard xp
         x_one = 5 + xp_one
         # adding max xp to standard xp
         x_two = 8 + xp_two
         # finding base health multiplier
         plus_one = 4 * level - 4
         # finding max health multiplier
         plus_two = 5 * level - 5
         # finding base hp
         health_one = 15 + plus_one
         # finding max hp
         health_two = 20 + plus_two
         # assigining found values to the Enemy
         enemy = Enemy(name, randint(health_one, health_two), level, randint(x_one, x_two))
         # finding players skills
         skills = Skills(player, enemy)
         # assigning enemy battle formula
         enemy_battle = Battle(player, enemy, skills, False)
         # Entering battle stage
         return enemy_battle

    #Mob fining module for areas 1, 2 and 3
    def area_1_2_3(self, rare):
         enm = [["Vespoid",0], ["Giant Moth",1], ["Giant Bee",2], ["Bear",3], ["The Eye",4], ["Pegasus",5], ["Soul Eater",6], ["Flame Spitter",7], ["Illusionist",8], ["Python",9], ["Spamirificano",10]]
         name_len = len(enm)
         mob = randint(0, name_len-1)
         names = enm[mob]
         name = names[0]
         id_val = names[1]
         lvl_one = self.player.lvl - 1
         lvl_two = self.player.lvl
         level = randint(lvl_one, lvl_two)
         if level <= 0:
            level = 1
         if level > 4:
            level = 4
         xp_one = 3 * level - 3
         xp_two = 4 * level - 4
         x_one = 5 + xp_one
         x_two = 6 + xp_two
         plus_one = 4 * level - 4
         plus_two = 5 * level - 5
         health_one = 15 + plus_one
         health_two = 20 + plus_two
         boss = False
         if rare == 'rare':
            boss = True
            name = "Rare Monster: %s" % name
            health_one += plus_one * 2
            health_two += plus_two * 2
            x_one += xp_one * 2
            x_two += xp_two * 2
         enemy = Enemy(name, randint(health_one, health_two), level, randint(x_one, x_two), id_val)
         skills = Skills(player, enemy)
         enemy_battle = Battle(player, enemy, skills, boss)
         return enemy_battle
		 
    def area_forest(self, bosss):
         enm = [['Slime',11]]
         name_len = len(enm)
         mob = randint(0, name_len-1)
         names = enm[mob]
         name = names[0]
         id_val = names[1]
         lvl_one = self.player.lvl - 1
         lvl_two = self.player.lvl
         level = randint(lvl_one, lvl_two)
         if level <= 6:
            level = 7
         if level > 8:
            level = 8
         xp_one = 3 * level - 3
         xp_two = 4 * level - 4
         x_one = 5 + xp_one
         x_two = 6 + xp_two
         plus_one = 4 * level - 4
         plus_two = 5 * level - 5
         health_one = 15 + plus_one
         health_two = 20 + plus_two
         boss = False
         if bosss == 'rare':
            boss = True
            name = "Giant %s" % name
            health_one += plus_one * 2
            health_two += plus_two * 2
            x_one += xp_one * 2
            x_two += xp_two * 2
         enemy = Enemy(name, randint(health_one, health_two), level, randint(x_one, x_two), id_val)
         skills = Skills(player, enemy)
         enemy_battle = Battle(player, enemy, skills, boss)
         return enemy_battle
		 
    def area_four_boss(self):
       enm = [["Chuck Testa",1000], ["Giant Chicken",1001], ["The Pumpkin King",1002], ["Bob",1003], ["\"YOUR MUM\"",1004], ["DEATH",1005], ["Jython",1006], ["Chris's evil twin",1007], ["Gigantic Turkey",1008], ["....",1009], ["A group of angry Vogons",1010]]
       name_len = len(enm)
       boss = randint(0, name_len-1)
       names = enm[boss]
       name = names[0]
       id_val = names[1]
       level = 6
       plus_h = 7 * level - 7
       health_one = 40 + plus_h
       health_two = 50 + plus_h
       xp = 8 * level - 8
       x_one = 17 + xp
       x_two = 21 + xp
       opponent = Enemy(name, randint(health_one, health_two), level, randint(x_one, x_two), id_val)
       skills = Skills(player, opponent)
       opponent_battle = Battle(player, opponent, skills, True)
       return opponent_battle


#==================================================================
#= Skills ==========================================================
#==================================================================
class Skills(object):

   def __init__(self, player, enemy):
      self.player = player
      self.enemy = enemy

   def warrior(self):
      if self.player.lvl >= 1:
         print "[Sword Slash] Cost: %s MP" % (8 + (self.player.lvl * 3) - 3)
      if self.player.lvl >= 5:
         print "[Blind] Cost: %s MP" % (20 + (self.player.lvl * 3) - 3)
      if self.player.lvl >= 10:
         print "[Bleed] Cost: %s MP" % (15 + (self.player.lvl * 3) - 3)

   def mage(self):
      if self.player.lvl >= 1:
         print "[Fire Ball] Cost: %s MP" % (8 + (self.player.lvl * 3) - 3)
      if self.player.lvl >= 5:
         print "[Bubble Shield] Cost: %s MP" % (20 + (self.player.lvl * 3) - 3)
      if self.player.lvl >= 10:
         print "[Burn] Cost: %s MP" % (15 + (self.player.lvl * 3) - 3)

   def archer(self):
      if self.player.lvl >= 1:
         print "[Charged Shot] Cost: %s MP" % (8 + (self.player.lvl * 3) - 3)
      if self.player.lvl >= 5:
         print "[Multi Shot] Cost: %s MP" % (20 + (self.player.lvl * 3) - 3)
      if self.player.lvl >= 10:
         print "[Pierce] Cost: %s MP" % (15 + (self.player.lvl * 3) - 3)
      
#==================================================================
#= Battle ==========================================================
#==================================================================
class Battle(object):

   def __init__(self, player, enemy, skills, boss):
      self.player = player
      self.enemy = enemy
      self.skills = skills
      self.dodge = False
      self.boss = boss
   
   def sys_battle(self):
      print "\nYou've encountered a Level %d %s!" % (self.enemy.lvl,self.enemy.name)
      raw_input("Press ENTER to continue.")
      print "\nType one of the following commands below to attempt an action.\n"
      enemy_defence = self.enemy.lvl / 1.5 + 1 + (self.enemy.lvl / 3)
      player_defence = self.player.lvl / 1.5
      enemy_attack = self.enemy.lvl
      if self.boss == True:
         enemy_attack = enemy_attack * 1.5
         enemy_defence = enemy_defence * 1.5
      player_attack = self.player.lvl + self.player.weapon[1]
      player_fear = 0.2
      turn_bubble = 0
      turn_pot = 0
      blind = 0
      blind_delay = 0
      bleed = 0
      if classes == "warrior":
         player_defence += 0.5
         player_attack += (self.player.str / 2)
      if classes == "mage":
         player_fear += 0.2
         player_attack += 0.2
         player_attack += (self.player.int / 2)
      if classes == "archer":
         player_attack += 0.5
         player_attack += (self.player.dex / 2)
      battle = True
      while self.enemy.hp > 0 and self.player.hp > 0 and battle:
         print "[Attack]"
         print "[Fear]"
         if classes == 'mage':
            self.skills.mage()
         if classes == 'warrior':
            self.skills.warrior()
         if classes == 'archer':
            self.skills.archer()
         print "[Inventory]"
         if self.boss == False:
            print "[Run]"
         print "\nHP: %s / %s\nMP: %s / %s\n" % (self.player.hp, self.player.max_hp, self.player.mana, self.player.max_mana)
         turn_bubble -= 1
         turn_pot -= 1
         blind -= 1
         blind_delay -= 1
         bleed -= 1
         if turn_bubble <= 0:
            turn_bubble = 0
            player_defence = self.player.lvl / 1.5
         if turn_bubble > 0:
            print "%s Turns till Bubble Shield can be used." % turn_bubble
         if turn_pot > 0:
            print "%s Turns till you can take a pot." % turn_pot
         if blind_delay > 0:
            print "%s Turns till you can use blind." % blind_delay
         if turn_bubble < 0:
            turn_buble = 0
         if turn_pot < 0:
            turn_pot = 0
         if blind < 0:
            blind = 0
         if blind_delay < 0:
            blind_delay = 0
         if bleed < 0:
            bleed = 0
         action = raw_input(">>> ")
         action = action.lower()
         
         # Normal attack.
         if action == "attack":
            self.enemy.hp -= math.ceil((player_attack * (randint(11.0,15.0) / 10.0) * 2.0) - (enemy_defence * randint(10.0,14.0) / 10.0))
            if self.enemy.hp > self.enemy.max_hp:
               self.enemy.hp = self.enemy.max_hp
            if self.enemy.hp < 0:
               self.enemy.hp = 0
            if classes == 'warrior':
               attack = "\nYou swing your sword leaving minor cuts! [%s HP: %d / %d]" % (self.enemy.name, self.enemy.hp, self.enemy.max_hp)

            if classes == 'mage':
               attack = "\nYou You wack your opponent with your Staff! [%s HP: %d / %d]" % (self.enemy.name, self.enemy.hp, self.enemy.max_hp)

            if classes == 'archer':
               attack = "\nYou shoot an arrow leaving a minor wound! [%s HP: %d / %d]" % (self.enemy.name, self.enemy.hp, self.enemy.max_hp)
               
            print attack
            if blind <= 0:
               self.player.hp -= math.ceil((enemy_attack * (randint(11.0,15.0) / 10.0) * 2.0) - (player_defence * randint(10.0,14.0) / 10.0))
               if self.player.hp > self.player.max_hp:
                  self.player.hp = self.player.max_hp
               if self.player.hp < 0:
                  self.player.hp = 0
               message = "It attacks back and hurts you! [%s's HP: %d / %d]\n" % (self.player.name, self.player.hp, self.player.max_hp)
               if self.enemy.hp <= 0:
                  message = "In the %s's Dying Breath he attacks back and hurts you! [%s's HP: %d / %d]\n" % (self.enemy.name, self.player.name, self.player.hp, self.player.max_hp)
               print message
               self.dodge = False
            if blind > 0:
               print "Your opponent is blinded and unable to move."
            if bleed > 0:
               if classes == 'mage':
                  print "Your opponent has major burns and takes damage."
                  self.enemy.hp -= 6 + (self.player.lvl * 3)
               if classes == 'warrior':
                  print "Your opponent is heavily bleeding dealing damage."
                  self.enemy.hp -= 6 + (self.player.lvl * 3)
               if classes == 'archer':
                  print "Your opponent is heavily bleeding dealing damage."
                  self.enemy.hp -= 6 + (self.player.lvl * 3)

         # Reduce Opponents Defence.
         elif action == "fear":
            fear = 0.2 * self.enemy.lvl
            if enemy_defence > fear:
               print "You scare your opponent and his defence is weakened."
               enemy_defence -= player_fear
               if blind <= 0:
                  self.player.hp -= math.ceil((enemy_attack * (randint(11.0,15.0) / 10.0) * 2.0) - (player_defence * randint(10.0,14.0) / 10.0))
                  if self.player.hp > self.player.max_hp:
                     self.player.hp = self.player.max_hp
                  if self.player.hp < 0:
                     self.player.hp = 0
                  print "It attacks back and hurts you! [%s's HP: %d / %d]\n" % (self.player.name, self.player.hp, self.player.max_hp)
                  self.dodge = False
               if blind > 0:
                  print "Your opponent is blinded and unable to move."
               if bleed > 0:
                  if classes == 'mage':
                     print "Your opponent has major burns and takes damage."
                     self.enemy.hp -= 6 + (self.player.lvl * 3)
                  if classes == 'warrior':
                     print "Your opponent is heavily bleeding dealing damage."
                     self.enemy.hp -= 6 + (self.player.lvl * 3)
                  if classes == 'archer':
                     print "Your opponent is heavily bleeding dealing damage."
                     self.enemy.hp -= 6 + (self.player.lvl * 3)
            elif enemy_defence <= fear:
               print "Your opponent has become Immune to fear."
               enemy_defence = fear
               turn_bubble += 1
               turn_pot += 1
               blind += 1
               blind_dealy += 1
               bleed += 1

         elif action == "inventory":
            inventory = True
            while inventory:
               print "Lesser Potion: %s" % self.player.lessar_potion
               print "Potion: %s" % self.player.potion
               print "Greater Potion: %s" % self.player.greater_potion
               print "Lesser Mana Potion: %s" % self.player.lessar_mana_potion
               print "Mana Potion: %s" % self.player.mana_potion
               print "Greater Mana Potion: %s" % self.player.greater_mana_potion
               select = raw_input("Type what item you want to Use or hit Enter: ")
               select = select.lower()
               if select == 'lesser potion':
                  if turn_pot <= 0:
                     if self.player.lessar_potion <= 0:
                        print "You do not have any Lesser Potions left"
                     elif self.player.lessar_potion > 0:
                        turn_pot += 6
                        print "You use a Lesser potion"
                        self.player.hp += 100
                        self.player.lessar_potion -= 1
                        print "You heal 100 hp"
                        if self.player.hp > self.player.max_hp:
                           self.player.hp = self.player.max_hp
                        print "You now have: %s / %s" % (self.player.hp, self.player.max_hp)
                        if blind <= 0:
                           self.player.hp -= math.ceil((enemy_attack * (randint(11.0,15.0) / 10.0) * 2.0) - (player_defence * randint(10.0,14.0) / 10.0))
                           if self.player.hp > self.player.max_hp:
                              self.player.hp = self.player.max_hp
                           if self.player.hp < 0:
                              self.player.hp = 0
                           print "%s Don't like pot heads, " % self.enemy.name
                           print "It get angry and attacks back! [%s's HP: %d / %d]\n" % (self.player.name, self.player.hp, self.player.max_hp)
                           self.dodge = False
                           inventory = False
                        if blind > 0:
                           print "Your opponent is blinded and unable to move."
                        if bleed > 0:
                           if classes == 'mage':
                              print "Your opponent has major burns and takes damage."
                              self.enemy.hp -= 6 + (self.player.lvl * 3)
                           if classes == 'warrior':
                              print "Your opponent is heavily bleeding dealing damage."
                              self.enemy.hp -= 6 + (self.player.lvl * 3)
                           if classes == 'archer':
                              print "Your opponent is heavily bleeding dealing damage."
                              self.enemy.hp -= 6 + (self.player.lvl * 3)
                  else:
                     print "You can't use pots for another %s turns" % turn_pot
               elif select == 'potion':
                  if turn_pot <= 0:
                     if self.player.potion <= 0:
                        print "You do not have any Potions left"
                     elif self.player.potion > 0:
                        turn_pot += 6
                        print "You use a potion"
                        self.player.hp += 200
                        self.player.potion -= 1
                        print "You heal 200 hp"
                        if self.player.hp > self.player.max_hp:
                           self.player.hp = self.player.max_hp
                        print "You now have: %s / %s" % (self.player.hp, self.player.max_hp)
                        if blind <= 0:
                           self.player.hp -= math.ceil((enemy_attack * (randint(11.0,15.0) / 10.0) * 2.0) - (player_defence * randint(10.0,14.0) / 10.0))
                           if self.player.hp > self.player.max_hp:
                              self.player.hp = self.player.max_hp
                           if self.player.hp < 0:
                              self.player.hp = 0
                           print "%s Don't like pot heads, " % self.enemy.name
                           print "It get angry and attacks back! [%s's HP: %d / %d]\n" % (self.player.name, self.player.hp, self.player.max_hp)
                           self.dodge = False
                           inventory = False
                        if blind > 0:
                           print "Your opponent is blinded and unable to move."
                        self.dodge = False
                        inventory = False
                        if bleed > 0:
                           if classes == 'mage':
                              print "Your opponent has major burns and takes damage."
                              self.enemy.hp -= 6 + (self.player.lvl * 3)
                           if classes == 'warrior':
                              print "Your opponent is heavily bleeding dealing damage."
                              self.enemy.hp -= 6 + (self.player.lvl * 3)
                           if classes == 'archer':
                              print "Your opponent is heavily bleeding dealing damage."
                              self.enemy.hp -= 6 + (self.player.lvl * 3)
                  else:
                     print "You can't use pots for another %s turns" % turn_pot
               elif select == 'greater potion':
                  if turn_pot <= 0:
                     if self.player.greater_potion <= 0:
                        print "You do not have any Greater Potions left"
                     elif self.player.greater_potion > 0:
                        turn_pot += 6
                        print "You use a Greater potion"
                        self.player.hp += 300
                        self.player.greater_potion -= 1
                        print "You heal 300 hp"
                        if self.player.hp > self.player.max_hp:
                           self.player.hp = self.player.max_hp
                        print "You now have: %s / %s" % (self.player.hp, self.player.max_hp)
                        if blind <= 0:
                           self.player.hp -= math.ceil((enemy_attack * (randint(11.0,15.0) / 10.0) * 2.0) - (player_defence * randint(10.0,14.0) / 10.0))
                           if self.player.hp > self.player.max_hp:
                              self.player.hp = self.player.max_hp
                           if self.player.hp < 0:
                              self.player.hp = 0
                           print "%s Don't like pot heads, " % self.enemy.name
                           print "It get angry and attacks back! [%s's HP: %d / %d]\n" % (self.player.name, self.player.hp, self.player.max_hp)
                           self.dodge = False
                           inventory = False
                        if blind > 0:
                           print "Your opponent is blinded and unable to move."
                        self.dodge = False
                        inventory = False
                        if bleed > 0:
                           if classes == 'mage':
                              print "Your opponent has major burns and takes damage."
                              self.enemy.hp -= 6 + (self.player.lvl * 3)
                           if classes == 'warrior':
                              print "Your opponent is heavily bleeding dealing damage."
                              self.enemy.hp -= 6 + (self.player.lvl * 3)
                           if classes == 'archer':
                              print "Your opponent is heavily bleeding dealing damage."
                              self.enemy.hp -= 6 + (self.player.lvl * 3)
                  else:
                     print "You can't use pots for another %s turns" % turn_pot
               elif select == 'lesser mana potion':
                  if turn_pot <= 0:
                     if self.player.lessar_mana_potion <= 0:
                        print "You do not have any Lesser Mana Potions left"
                     elif self.player.lessar_mana_potion > 0:
                        turn_pot += 6
                        print "You use a lesser mana potion"
                        self.player.mana += 100
                        self.player.lessar_mana_potion -= 1
                        print "You gain 100 mana"
                        if self.player.mana > self.player.max_mana:
                           self.player.mana = self.player.max_mana
                        print "You now have: %s / %s" % (self.player.mana, self.player.max_mana)
                        if blind <= 0:
                           self.player.hp -= math.ceil((enemy_attack * (randint(11.0,15.0) / 10.0) * 2.0) - (player_defence * randint(10.0,14.0) / 10.0))
                           if self.player.hp > self.player.max_hp:
                              self.player.hp = self.player.max_hp
                           if self.player.hp < 0:
                              self.player.hp = 0
                           print "%s Don't like pot heads, " % self.enemy.name
                           print "It get angry and attacks back! [%s's HP: %d / %d]\n" % (self.player.name, self.player.hp, self.player.max_hp)
                           self.dodge = False
                           inventory = False
                        if blind > 0:
                           print "Your opponent is blinded and unable to move."
                        self.dodge = False
                        inventory = False
                        if bleed > 0:
                           if classes == 'mage':
                              print "Your opponent has major burns and takes damage."
                              self.enemy.hp -= 6 + (self.player.lvl * 3)
                           if classes == 'warrior':
                              print "Your opponent is heavily bleeding dealing damage."
                              self.enemy.hp -= 6 + (self.player.lvl * 3)
                           if classes == 'archer':
                              print "Your opponent is heavily bleeding dealing damage."
                              self.enemy.hp -= 6 + (self.player.lvl * 3)
                  else:
                     print "You can't use pots for another %s turns" % turn_pot
               elif select == 'mana potion':
                  if turn_pot <= 0:
                     if self.player.mana_potion <= 0:
                        print "You do not have any Mana Potions left"
                     elif self.player.mana_potion > 0:
                        turn_pot += 6
                        print "You use a mana potion"
                        self.player.mana += 200
                        self.player.mana_potion -= 1
                        print "You gain 200 mana"
                        if self.player.mana > self.player.max_mana:
                           self.player.mana = self.player.max_mana
                        print "You now have: %s / %s" % (self.player.mana, self.player.max_mana)
                        if blind <= 0:
                           self.player.hp -= math.ceil((enemy_attack * (randint(11.0,15.0) / 10.0) * 2.0) - (player_defence * randint(10.0,14.0) / 10.0))
                           if self.player.hp > self.player.max_hp:
                              self.player.hp = self.player.max_hp
                           if self.player.hp < 0:
                              self.player.hp = 0
                           print "%s Don't like pot heads, " % self.enemy.name
                           print "It get angry and attacks back! [%s's HP: %d / %d]\n" % (self.player.name, self.player.hp, self.player.max_hp)
                           self.dodge = False
                           inventory = False
                        if blind > 0:
                           print "Your opponent is blinded and unable to move."
                        self.dodge = False
                        inventory = False
                        if bleed > 0:
                           if classes == 'mage':
                              print "Your opponent has major burns and takes damage."
                              self.enemy.hp -= 6 + (self.player.lvl * 3)
                           if classes == 'warrior':
                              print "Your opponent is heavily bleeding dealing damage."
                              self.enemy.hp -= 6 + (self.player.lvl * 3)
                           if classes == 'archer':
                              print "Your opponent is heavily bleeding dealing damage."
                              self.enemy.hp -= 6 + (self.player.lvl * 3)
                  else:
                     print "You can't use pots for another %s turns" % turn_pot
               elif select == 'greater mana potion':
                  if turn_pot <= 0:
                     if self.player.greater_mana_potion <= 0:
                        print "You do not have any Greater Mana Potions left"
                     elif self.player.greater_mana_potion > 0:
                        turn_pot += 6
                        print "You use a greater mana potion"
                        self.player.mana += 300
                        self.player.greater_mana_potion -= 1
                        print "You gain 300 mana"
                        if self.player.mana > self.player.max_mana:
                           self.player.mana = self.player.max_mana
                        print "You now have: %s / %s" % (self.player.mana, self.player.max_mana)
                        if blind <= 0:
                           self.player.hp -= math.ceil((enemy_attack * (randint(11.0,15.0) / 10.0) * 2.0) - (player_defence * randint(10.0,14.0) / 10.0))
                           if self.player.hp > self.player.max_hp:
                              self.player.hp = self.player.max_hp
                           if self.player.hp < 0:
                              self.player.hp = 0
                           print "%s Don't like pot heads, " % self.enemy.name
                           print "It get angry and attacks back! [%s's HP: %d / %d]\n" % (self.player.name, self.player.hp, self.player.max_hp)
                           self.dodge = False
                           inventory = False
                        if blind > 0:
                           print "Your opponent is blinded and unable to move."
                        self.dodge = False
                        inventory = False
                        if bleed > 0:
                           if classes == 'mage':
                              print "Your opponent has major burns and takes damage."
                              self.enemy.hp -= 6 + (self.player.lvl * 3)
                           if classes == 'warrior':
                              print "Your opponent is heavily bleeding dealing damage."
                              self.enemy.hp -= 6 + (self.player.lvl * 3)
                           if classes == 'archer':
                              print "Your opponent is heavily bleeding dealing damage."
                              self.enemy.hp -= 6 + (self.player.lvl * 3)
                  else:
                     print "You can't use pots for another %s turns" % turn_pot
               else:
                  inventory = False
                  turn_bubble += 1
                  turn_pot += 1
                  blind += 1
                  blind_delay += 1
                  bleed += 1

         elif action == 'run' and self.boss == False:
            run = randint(0, 2)
            if run == 0:
               print "You fail in running away"
               self.player.hp -= math.ceil((enemy_attack * (randint(11.0,15.0) / 10.0) * 2.0) - (player_defence * randint(10.0,14.0) / 10.0))
               if self.player.hp > self.player.max_hp:
                  self.player.hp = self.player.max_hp
               if self.player.hp < 0:
                  self.player.hp = 0
               message = "It attacks your back and hurts you! [%s's HP: %d / %d]\n" % (self.player.name, self.player.hp, self.player.max_hp)
               print message
               
            elif run >= 1:
               print "You escape from your opponent."
               battle = False

         elif classes == 'warrior':
            if action == 'sword slash' and self.player.lvl >= 1:
               if self.player.mana >= 5 + (self.player.lvl * 3):
                  self.player.mana -= 5 + (self.player.lvl * 3)
                  self.enemy.hp -= math.ceil((player_attack * (randint(16.0,20.0) / 10.0) * 2.0) - (enemy_defence * randint(10.0,14.0) / 10.0))
                  if self.enemy.hp > self.enemy.max_hp:
                     self.enemy.hp = self.enemy.max_hp
                  if self.enemy.hp < 0:
                     self.enemy.hp = 0
                  attack = "\nYour Rage Overflows into your weapon unleashing a devastating strike! [%s HP: %d / %d]" % (self.enemy.name, self.enemy.hp, self.enemy.max_hp)
                  print attack
                  if blind <= 0:
                     self.player.hp -= math.ceil((enemy_attack * (randint(11.0,15.0) / 10.0) * 2.0) - (player_defence * randint(10.0,14.0) / 10.0))
                     if self.player.hp > self.player.max_hp:
                        self.player.hp = self.player.max_hp
                     if self.player.hp < 0:
                        self.player.hp = 0
                     message = "It attacks back and hurts you! [%s's HP: %d / %d]\n" % (self.player.name, self.player.hp, self.player.max_hp)
                     if self.enemy.hp <= 0:
                        message = "In the %s's Dying Breath he attacks back and hurts you! [%s's HP: %d / %d]\n" % (self.enemy.name, self.player.name, self.player.hp, self.player.max_hp)
                     print message
                     self.dodge = False
                  if blind > 0:
                     print "Your opponent is blinded and unable to move."
                  if bleed > 0:
                     print "Your opponent is heavily bleeding dealing damage."
                     self.enemy.hp -= 6 + (self.player.lvl * 3)
               else:
                  print "You don't have enough MP."
                  turn_pot += 1
                  blind += 1
                  blind_delay += 1
                  bleed += 1

            elif action == 'blind' and self.player.lvl >= 5:
               if self.player.mana >= 20 + ((self.player.lvl * 3) - 3):
                  if blind_delay <= 0:
                     self.player.mana -= 20 + ((self.player.lvl * 3) - 3)
                     print "You engulf your blade in holy light blinding your opponent for 2 turns."
                     blind_delay += 11
                     blind += 3
                     if bleed > 0:
                        if classes == 'mage':
                           print "Your opponent has major burns and takes damage."
                           self.enemy.hp -= 6 + (self.player.lvl * 3)
                        if classes == 'warrior':
                           print "Your opponent is heavily bleeding dealing damage."
                           self.enemy.hp -= 6 + (self.player.lvl * 3)
                  else:
                     print "You can't use blind for another %s Turns." % blind_delay
                     turn_pot += 1
                     blind += 1
                     blind_delay += 1
                     bleed += 1
               else:
                  print "You don't have enough MP."
                  turn_pot += 1
                  blind += 1
                  blind_delay += 1
                  bleed += 1

            elif action == 'bleed' and self.player.lvl >= 10:
               if self.player.mana >= 15 + ((self.player.lvl * 3) - 3):
                  self.player.mana -= 15 + ((self.player.lvl * 3) - 3)
                  print "You quickly slash you opponent creating a severe wound dealing damage for 4 turns!"
                  bleed += 5
                  if blind <= 0:
                     self.player.hp -= math.ceil((enemy_attack * (randint(11.0,15.0) / 10.0) * 2.0) - (player_defence * randint(10.0,14.0) / 10.0))
                     if self.player.hp > self.player.max_hp:
                        self.player.hp = self.player.max_hp
                     if self.player.hp < 0:
                        self.player.hp = 0
                     message = "It attacks back and hurts you! [%s's HP: %d / %d]\n" % (self.player.name, self.player.hp, self.player.max_hp)
                     if self.enemy.hp <= 0:
                        message = "In the %s's Dying Breath he attacks back and hurts you! [%s's HP: %d / %d]\n" % (self.enemy.name, self.player.name, self.player.hp, self.player.max_hp)
                     print message
                     if blind > 0:
                        print "Your opponent is blinded and unable to move."
                     if bleed > 0:
                        if classes == 'mage':
                           print "Your opponent has major burns and takes damage."
                           self.enemy.hp -= 6 + (self.player.lvl * 3)
                        if classes == 'warrior':
                           print "Your opponent is heavily bleeding dealing damage."
                           self.enemy.hp -= 6 + (self.player.lvl * 3)
               else:
                  print "You don't have enough MP."
                  turn_pot += 1
                  blind += 1
                  blind_delay += 1
                  bleed += 1

            else:
               print "\nPlease enter a real command!\n"
               turn_bubble += 1
               turn_pot += 1
               blind += 1
               blind_delay += 1
               bleed += 1

         elif classes == 'mage':
            if action == 'fire ball' and self.player.lvl >= 1:
               if self.player.mana >= 5 + ((self.player.lvl * 3) - 3):
                  self.player.mana -= 5 + ((self.player.lvl * 3) - 3)
                  self.enemy.hp -= math.ceil((player_attack * (randint(16.0,20.0) / 10.0) * 2.0) - (enemy_defence * randint(10.0,14.0) / 10.0))
                  if self.enemy.hp > self.enemy.max_hp:
                     self.enemy.hp = self.enemy.max_hp
                  if self.enemy.hp < 0:
                     self.enemy.hp = 0
                  attack = "\nYour cast a fire ball at your opponent giving minor burns! [%s HP: %d / %d]" % (self.enemy.name, self.enemy.hp, self.enemy.max_hp)
                  print attack
                  self.player.hp -= math.ceil((enemy_attack * (randint(11.0,15.0) / 10.0) * 2.0) - (player_defence * randint(10.0,14.0) / 10.0))
                  if self.player.hp > self.player.max_hp:
                     self.player.hp = self.player.max_hp
                  if self.player.hp < 0:
                     self.player.hp = 0
                  message = "It attacks back and hurts you! [%s's HP: %d / %d]\n" % (self.player.name, self.player.hp, self.player.max_hp)
                  if self.enemy.hp <= 0:
                     message = "In the %s's Dying Breath he attacks back and hurts you! [%s's HP: %d / %d]\n" % (self.enemy.name, self.player.name, self.player.hp, self.player.max_hp)
                  print message
                  self.dodge = False
                  if bleed > 0:
                     if classes == 'mage':
                        print "Your opponent has major burns and takes damage."
                        self.enemy.hp -= 6 + (self.player.lvl * 3)
                     if classes == 'warrior':
                        print "Your opponent is heavily bleeding dealing damage."
                        self.enemy.hp -= 6 + (self.player.lvl * 3)
               else:
                  print "You don't have enough MP."
                  turn_bubble += 1
                  turn_pot += 1
                  blind += 1
                  blind_delay += 1
                  bleed += 1
                  
            if action == 'bubble shield' and self.player.lvl >= 5:
               if self.player.mana >= 20 + ((self.player.lvl * 3) - 3):
                  if turn_bubble <= 0:
                     self.player.mana -= 20 + ((self.player.lvl * 3) - 3)
                     turn_bubble += 6
                     print "You engulf yourself in a bubble shield protecting you for 5 turns."
                     if turn_bubble > 0:
                        player_defence += 0.2
                     self.player.hp -= math.ceil((enemy_attack * (randint(11.0,15.0) / 10.0) * 2.0) - (player_defence * randint(10.0,14.0) / 10.0))
                     if self.player.hp > self.player.max_hp:
                        self.player.hp = self.player.max_hp
                     if self.player.hp < 0:
                        self.player.hp = 0
                     message = "It attacks back and hurts you! [%s's HP: %d / %d]\n" % (self.player.name, self.player.hp, self.player.max_hp)
                     print message
                     self.dodge = False
                  elif turn_bubble > 0:
                     print "You cant use bubble shield for another %s Turns" % _bubble
                     turn_bubble += 1
                     turn_pot += 1
                     blind += 1
                     blind_delay += 1
                     bleed += 1
               else:
                  print "You don't have enough MP."
                  turn_bubble += 1
                  turn_pot += 1
                  blind += 1
                  blind_delay += 1
                  bleed += 1

            elif action == 'burn' and self.player.lvl >= 10:
               if self.player.mana >= 15 + ((self.player.lvl * 3) - 3):
                  self.player.mana -= 15 + ((self.player.lvl * 3) - 3)
                  print "You Inflict Heavy burns on your opponent causing damage for 4 turns!"
                  bleed += 5
                  if blind <= 0:
                     self.player.hp -= math.ceil((enemy_attack * (randint(11.0,15.0) / 10.0) * 2.0) - (player_defence * randint(10.0,14.0) / 10.0))
                     if self.player.hp > self.player.max_hp:
                        self.player.hp = self.player.max_hp
                     if self.player.hp < 0:
                        self.player.hp = 0
                     message = "It attacks back and hurts you! [%s's HP: %d / %d]\n" % (self.player.name, self.player.hp, self.player.max_hp)
                     if self.enemy.hp <= 0:
                        message = "In the %s's Dying Breath he attacks back and hurts you! [%s's HP: %d / %d]\n" % (self.enemy.name, self.player.name, self.player.hp, self.player.max_hp)
                     print message
                     if blind > 0:
                        print "Your opponent is blinded and unable to move."
                     if bleed > 0:
                        if classes == 'mage':
                           print "Your opponent has major burns and takes damage."
                           self.enemy.hp -= 6 + (self.player.lvl * 3)
                        if classes == 'warrior':
                           print "Your opponent is heavily bleeding dealing damage."
                           self.enemy.hp -= 6 + (self.player.lvl * 3)
               else:
                  print "You don't have enough MP."
                  turn_bubble += 1
                  turn_pot += 1
                  blind += 1
                  blind_delay += 1
                  bleed += 1
                  
            else:
               print "\nPlease enter a real command!\n"
               turn_bubble += 1
               turn_pot += 1
               blind += 1
               blind_delay += 1
               bleed += 1

         elif classes == 'archer':
            if action == 'charged shot' and self.player.lvl >= 1:
               if self.player.mana >= 5 + ((self.player.lvl * 3) - 3):
                  self.player.mana -= 5 + ((self.player.lvl * 3) - 3)
                  self.enemy.hp -= math.ceil((player_attack * (randint(16.0,20.0) / 10.0) * 2.0) - (enemy_defence * randint(10.0,14.0) / 10.0))
                  if self.enemy.hp > self.enemy.max_hp:
                     self.enemy.hp = self.enemy.max_hp
                  if self.enemy.hp < 0:
                     self.enemy.hp = 0
                  attack = "\nYour Energy flows into your arrow dealing massive damage against your opponent! [%s HP: %d / %d]" % (self.enemy.name, self.enemy.hp, self.enemy.max_hp)
                  print attack
                  self.player.hp -= math.ceil((enemy_attack * (randint(11.0,15.0) / 10.0) * 2.0) - (player_defence * randint(10.0,14.0) / 10.0))
                  if self.player.hp > self.player.max_hp:
                     self.player.hp = self.player.max_hp
                  if self.player.hp < 0:
                     self.player.hp = 0
                  message = "It attacks back and hurts you! [%s's HP: %d / %d]\n" % (self.player.name, self.player.hp, self.player.max_hp)
                  if self.enemy.hp <= 0:
                     message = "In the %s's Dying Breath he attacks back and hurts you! [%s's HP: %d / %d]\n" % (self.enemy.name, self.player.name, self.player.hp, self.player.max_hp)
                  print message
                  self.dodge = False
                  if bleed > 0:
                     print "Your opponent is heavily bleeding dealing damage."
                     self.enemy.hp -= 6 + (self.player.lvl * 3)
               else:
                  print "You don't have enough MP."
                  turn_pot += 1
                  blind += 1
                  blind_delay += 1
                  bleed += 1

            elif action == 'multi shot' and self.player.lvl >= 5:
               if self.player.mana >= 20 + ((self.player.lvl * 3) - 3):
                     self.player.mana -= 20 + ((self.player.lvl * 3) - 3)
                     self.enemy.hp -= math.ceil((player_attack * (randint(6.0,10.0) / 10.0) * 2.0) - (enemy_defence * randint(10.0,14.0) / 10.0))
                     self.enemy.hp -= math.ceil((player_attack * (randint(6.0,10.0) / 10.0) * 2.0) - (enemy_defence * randint(10.0,14.0) / 10.0))
                     self.enemy.hp -= math.ceil((player_attack * (randint(6.0,10.0) / 10.0) * 2.0) - (enemy_defence * randint(10.0,14.0) / 10.0))
                     if self.enemy.hp > self.enemy.max_hp:
                        self.enemy.hp = self.enemy.max_hp
                     if self.enemy.hp < 0:
                        self.enemy.hp = 0
                     attack = "\nYou shoot three arrows simultaneously.! [%s HP: %d / %d]" % (self.enemy.name, self.enemy.hp, self.enemy.max_hp)
                     print attack
                     self.player.hp -= math.ceil((enemy_attack * (randint(11.0,15.0) / 10.0) * 2.0) - (player_defence * randint(10.0,14.0) / 10.0))
                     if self.player.hp > self.player.max_hp:
                        self.player.hp = self.player.max_hp
                     if self.player.hp < 0:
                        self.player.hp = 0
                     message = "It attacks back and hurts you! [%s's HP: %d / %d]\n" % (self.player.name, self.player.hp, self.player.max_hp)
                     if self.enemy.hp <= 0:
                        message = "In the %s's Dying Breath he attacks back and hurts you! [%s's HP: %d / %d]\n" % (self.enemy.name, self.player.name, self.player.hp, self.player.max_hp)
                     print message
                     if bleed > 0:
                        if classes == 'mage':
                           print "Your opponent has major burns and takes damage."
                           self.enemy.hp -= 6 + (self.player.lvl * 3)
                        if classes == 'warrior':
                           print "Your opponent is heavily bleeding dealing damage."
                           self.enemy.hp -= 6 + (self.player.lvl * 3)
                        if classes == 'archer':
                           print "Your opponent is heavily bleeding dealing damage."
                           self.enemy.hp -= 6 + (self.player.lvl * 3)
               else:
                  print "You don't have enough MP."
                  turn_pot += 1
                  blind += 1
                  blind_delay += 1
                  bleed += 1

            elif action == 'pierce' and self.player.lvl >= 10:
               if self.player.mana >= 15 + ((self.player.lvl * 3) - 3):
                  self.player.mana -= 15 + ((self.player.lvl * 3) - 3)
                  print "You pierce your opponent causing him to heavily bleed for 4 Turns!"
                  bleed += 5
                  if blind <= 0:
                     self.player.hp -= math.ceil((enemy_attack * (randint(11.0,15.0) / 10.0) * 2.0) - (player_defence * randint(10.0,14.0) / 10.0))
                     if self.player.hp > self.player.max_hp:
                        self.player.hp = self.player.max_hp
                     if self.player.hp < 0:
                        self.player.hp = 0
                     message = "It attacks back and hurts you! [%s's HP: %d / %d]\n" % (self.player.name, self.player.hp, self.player.max_hp)
                     if self.enemy.hp <= 0:
                        message = "In the %s's Dying Breath he attacks back and hurts you! [%s's HP: %d / %d]\n" % (self.enemy.name, self.player.name, self.player.hp, self.player.max_hp)
                     print message
                     if blind > 0:
                        print "Your opponent is blinded and unable to move."
                     if bleed > 0:
                        if classes == 'mage':
                           print "Your opponent has major burns and takes damage."
                           self.enemy.hp -= 6 + (self.player.lvl * 3)
                        if classes == 'warrior':
                           print "Your opponent is heavily bleeding dealing damage."
                           self.enemy.hp -= 6 + (self.player.lvl * 3)
               else:
                  print "You don't have enough MP."
                  turn_pot += 1
                  blind += 1
                  blind_delay += 1
                  bleed += 1

            else:
               print "\nPlease enter a real command!\n"
               turn_bubble += 1
               turn_pot += 1
               blind += 1
               blind_delay += 1
               bleed += 1
         
         # Not a valid command.
         else:
            print "\nPlease enter a real command!\n"
            turn_bubble += 1
            turn_pot += 1
            blind += 1
            blind_delay += 1
            bleed += 1

      if self.enemy.hp <= 0 and self.player.hp > 0:
         print "You've killed a Level %d %s!" % (self.enemy.lvl, self.enemy.name)
         if self.player.lvl < 100:
            self.player.xp += self.enemy.xp_given
            self.enemy.hp = self.enemy.max_hp
            print "You Gain %s XP" % (self.enemy.xp_given)
            self.player.level_up()
            print "%s / %s till next LvL" % (self.player.xp, self.player.max_xp)
         for list in self.player.quests:
            if list[4] == self.enemy.id_val and 'kill' in list[1].lower():
               list[2] += 1
               print 'You kill a %s' % list[6]
            elif list[4] == self.enemy.id_val and 'aquire' in list[1].lower():
               chance = randint (1,2)
               if chance == 1:
                  print 'You Obtain a %s' % list[6]
                  list[2] += 1
         drop_count = 0
         drop_limit = 1
         if self.boss == True:
            drop_limit = 3
         while drop_count < drop_limit:
            # [prefix,base,suffix]
            prefixes = ['Dangerous', 'Exciting', 'Mysterious', 'Interesting', 'Exalted', 'Battle', 'Perculiar', 'Unsightly', 'Faithful', 'Thundering', 'Colossal', 'Long', 'Strong', 'Sticky', 'The Famous']
            suffixes = [' of Power', ' of a King', ' of Death', ' of Misfortune', ' of Destiny', ' of Madness', ' of Orpheus', ' of The Elements', ' of Greed']
            warrior_c = [' Sword', ' Axe']
            mage_c = [' Wand', ' Staff']
            archer_c = [' Bow', ' Cross-Bow']
            name = ['','','']
            strength = 0
            dexterity = 0
            intelligence = 0
            vitality = 0
            increase_drop = 0
            prelist = len(prefixes) - 1
            chance = randint(0,prelist)
            name[0] = prefixes[chance]
            drop_rare = 850 - (2 * self.player.drop)
            drop_legend = 999 - self.player.drop
            if self.boss == True:
               drop_rare -= 100
               drop_legend -= 50
            chance_c = randint(1, 1000)
            chance = randint(0, 2)
            if chance == 0:
               chancef = randint(0,1)
               name[1] = mage_c[chancef]
               cl = 'mage'
            if chance == 1:
               chancef = randint(0,1)
               name[1] = warrior_c[chancef]
               cl = 'warrior'
            if chance == 2:
               chancef = randint(0,1)
               name[1] = archer_c[chancef]
               cl = 'archer'
            weapon_damage = int(self.enemy.lvl / randint(1,3))
            if weapon_damage < 1:
               weapon_damage = 1
            weapon_value = int(self.enemy.max_hp / 2)
            if chance_c >= drop_rare:
               suflist = len(suffixes) - 1
               chance = randint(0,suflist)
               name[2] = suffixes[chance]
               if chance_c < drop_legend:
                  weapon_damage = int(self.enemy.lvl / uniform(0.5,1))
                  if weapon_damage < 1:
                     weapon_damage = 1
                  weapon_value = int(self.enemy.max_hp / 1)
                  rep_stats_1 = randint(0,4)
                  rep_stats_2 = randint(0,4)
                  while rep_stats_1 == rep_stats_2:
                     rep_stats_2 = randint(0,4)
                  if rep_stats_1 == 0 or rep_stats_2 == 0:
                     str_mark = self.enemy.lvl * 3
                     strength = randint(str_mark-(2*self.player.lvl), str_mark)
                  if rep_stats_1 == 1 or rep_stats_2 == 1:
                     dex_mark = self.enemy.lvl * 3
                     dexterity = randint(dex_mark-(2*self.player.lvl), dex_mark)
                  if rep_stats_1 == 2 or rep_stats_2 == 2:
                     int_mark = self.enemy.lvl * 3
                     intelligence = randint(int_mark-(2*self.player.lvl), int_mark)
                  if rep_stats_1 == 3 or rep_stats_2 == 3:
                     vit_mark = self.enemy.lvl * 3
                     vitality = randint(vit_mark-(2*self.player.lvl), vit_mark)
                  if rep_stats_1 == 4 or rep_stats_2 == 4:
                     drp_mark = self.enemy.lvl * 5
                     increase_drop = randint(drp_mark-(3*self.player.lvl), drp_mark)
               
            weapon_name = ''.join(name)
            if chance_c >= drop_legend:
               weapon_name = 'Legendary: %s' % weapon_name
               weapon_damage = int(self.enemy.lvl / uniform(0.3,0.6))
               if weapon_damage < 1:
                  weapon_damage = 1
               weapon_value = int(self.enemy.max_hp / 0.5)
               rep_stats_1 = randint(0,4)
               rep_stats_2 = randint(0,4)
               rep_stats_3 = randint(0,4)
               while rep_stats_1 == rep_stats_2 or rep_stats_1 == rep_stats_3:
                  rep_stats_1 = randint(0,4)
               while rep_stats_2 == rep_stats_1 or rep_stats_2 == rep_stats_3:
                  rep_stats_2 = randint(0,4)
               if rep_stats_1 == 0 or rep_stats_2 == 0 or rep_stats_3 == 0:
                  str_mark = self.enemy.lvl * 4
                  strength = randint(str_mark-(2*self.player.lvl), str_mark)
               if rep_stats_1 == 1 or rep_stats_2 == 1 or rep_stats_3 == 1:
                  dex_mark = self.enemy.lvl * 4
                  dexterity = randint(dex_mark-(2*self.player.lvl), dex_mark)
               if rep_stats_1 == 2 or rep_stats_2 == 2 or rep_stats_3 == 2:
                  int_mark = self.enemy.lvl * 4
                  intelligence = randint(int_mark-(2*self.player.lvl), int_mark)
               if rep_stats_1 == 3 or rep_stats_2 == 3 or rep_stats_3 == 3:
                  vit_mark = self.enemy.lvl * 4
                  vitality = randint(vit_mark-(2*self.player.lvl), vit_mark)
               if rep_stats_1 == 4 or rep_stats_2 == 4 or rep_stats_3 == 4:
                  drp_mark = self.enemy.lvl * 7
                  increase_drop = randint(drp_mark-(4*self.player.lvl), drp_mark)
            weapon_class = cl
            new_weapon = [weapon_name, weapon_damage, weapon_value, weapon_class, strength, dexterity, intelligence, vitality, increase_drop]
            self.player.weapon_inv.append(new_weapon)
            print 'You Aquire a "%s"' % weapon_name
            drop_count += 1
            
         if self.enemy.lvl < 10:
            interger = randint(0, 6)
            if interger > 5:
               number = 1
            if interger <= 5:
               number = 0
            if number > 0:
               self.player.lessar_potion += number
               print "You Aquire %s Lessar Potion" % number
            raw_input("Press ENTER to exit the battle scene.")
         
         elif self.enemy.lvl < 20 and self.enemy.lvl >= 10:
            interger = randint(0, 6)
            if interger > 5:
               number = 1
            if interger <= 5:
               number = 0
            if number > 0:
               self.player.potion += number
               print "You Aquire %s Potion" % number
            raw_input("Press ENTER to exit the battle scene.")
         
         elif self.enemy.lvl < 30 and self.enemy.lvl >= 20:
            interger = randint(0, 6)
            if interger > 5:
               number = 1
            if interger <= 5:
               number = 0
            if number > 0:
               self.player.greater_potion += number
               print "You Aquire %s Greater Potion" % number
            raw_input("Press ENTER to exit the battle scene.")
            
      elif self.player.hp <= 0 and self.enemy.hp > 0:
         print "You've been killed by a Level %d %s!" % (self.enemy.lvl, self.enemy.name)
         cred = Credits()
         cred.cred()

      elif self.player.hp <= 0 and self.enemy.hp <= 0:
         print "You've been killed by a Level %d %s!" % (self.enemy.lvl, self.enemy.name)
         cred = Credits()
         cred.cred()

#==================================================================
#= Game ============================================================
#==================================================================
class GameStory(object):
   
   def __init__(self, player, start, renemy):
      self.player = player
      self.start = start
      self.renemy = renemy
      # Variable for toggling the game intro.
      self.intro_done = False
      self.first_battle = False
      self.rift_first = False
   
   # Engine for playing the game.
   def play(self, x, y):
      next_area = self.start
      while True:
         room = getattr(self, next_area)
         next_area = room(x, y)

   def load(self, room, data):
      if data == 'save1':
         save = open('save1.txt', 'r')
         wep = open('save_wep1.txt', 'r')
         quest = open('save_quest1.txt', 'r')
      
      elif data == 'save2':
         save = open('save2.txt', 'r')
         wep = open('save_wep2.txt', 'r')
         quest = open('save_quest2.txt', 'r')
      
      elif data == 'save3':
         save = open('save3.txt', 'r')
         wep = open('save_wep3.txt', 'r')
         quest = open('save_quest3.txt', 'r')

      load = []

      for line in save:
         line = line.strip()
         load.append(line)
      
      self.player.lvl = int(load[0])
      self.player.hp = float(load[1])
      self.player.max_hp = int(load[2])
      self.player.xp = int(load[3])
      self.player.max_xp = int(load[4])
      self.player.mana = int(load[7])
      self.player.max_mana = int(load[8])
      self.player.money = int(load[9])
      self.player.junk_metal = int(load[10])
      self.player.lessar_potion = int(load[11])
      self.player.potion = int(load[12])
      self.player.greater_potion = int(load[13])
      self.player.lessar_mana_potion = int(load[14])
      self.player.mana_potion = int(load[15])
      self.player.greater_mana_potion = int(load[16])
      self.player.ocean_gem = int(load[17])
      self.player.defence_up = int(load[18])
      self.player.silver_horn = int(load[19])
      self.player.weapon[0] = str(load[22])
      self.player.weapon[1] = int(load[23])
      self.player.plan_rusty_sword = int(load[24])
      self.player.plan_wooden_staff = int(load[25])
      self.player.plan_wooden_bow = int(load[26])
      self.player.work_bench = int(load[27])
      self.player.wood = int(load[28])
      self.player.bronze = int(load[29])
      self.player.iron = int(load[30])
      self.player.steel = int(load[31])
      self.player.gold = int(load[32])
      self.player.silver = int(load[33])
      self.player.dragon_blood = int(load[34])
      self.player.str = int(load[36])
      self.player.dex = int(load[37])
      self.player.int = int(load[38])
      self.player.vit = int(load[39])
      self.player.drop = int(load[40])
      if load[35] == 'True':
         self.player.rift_first = True
      if load[35] == 'False':
         self.player.rift_first = False
      if load[21] == 'True':
          self.player.first_battle = True
      if load[21] == 'False':
          self.player.first_battle = False
      if load[43] == 'True':
          self.player.first_tavern = True
      if load[43] == 'False':
          self.player.first_tavern = False
      print "Your Save file has loaded"
      raw_input('Press ENTER to continue')
      self.intro_done = True

      for line in wep:
         name, damage, cost, classs, strength, dexterity, intelligence, vitality, drop = line.strip().split(',')
         new_weapon = [name, int(damage), int(cost), classs, int(strength), int(dexterity), int(intelligence), int(vitality), int(drop)]
         self.player.weapon_inv.append(new_weapon)

      for line in quest:
         a, b, c, d, e, f, g = line.strip().split(',')
         loading_quests = [a, b, int(c), int(d), int(e), f, g]
         self.player.quests.append(loading_quests)
      
      save.close()
      wep.close()
      quest.close()

      return room

   def save(self, room, x, y):
      print '[Save 1]'
      print '[Save 2]'
      print '[Save 3]'
      saving = raw_input(">>> ")
      saving = saving.lower()
      if saving == 'save 1':
         save = open('save1.txt', 'w')
         wep = open('save_wep1.txt', 'w')
         quest = open('save_quest1.txt', 'w')

      elif saving == 'save 2':
         save = open('save2.txt', 'w')
         wep = open('save_wep2.txt', 'w')
         quest = open('save_quest2.txt', 'w')

      elif saving == 'save 3':
         save = open('save3.txt', 'w')
         wep = open('save_wep3.txt', 'w')
         quest = open('save_quest3.txt', 'w')
         
      try:
         save.write(str(self.player.lvl)+"\n")
         save.write(str(self.player.hp)+"\n")
         save.write(str(self.player.max_hp)+"\n")
         save.write(str(self.player.xp)+"\n")
         save.write(str(self.player.max_xp)+"\n")
         save.write(str(self.player.name)+"\n")
         save.write(str(room)+"\n")
         save.write(str(self.player.mana)+"\n")
         save.write(str(self.player.max_mana)+"\n")
         save.write(str(self.player.money)+"\n")
         save.write(str(self.player.junk_metal)+"\n")
         save.write(str(self.player.lessar_potion)+"\n")
         save.write(str(self.player.potion)+"\n")
         save.write(str(self.player.greater_potion)+"\n")
         save.write(str(self.player.lessar_mana_potion)+"\n")
         save.write(str(self.player.mana_potion)+"\n")
         save.write(str(self.player.greater_mana_potion)+"\n")
         save.write(str(self.player.ocean_gem)+"\n")
         save.write(str(self.player.defence_up)+"\n")
         save.write(str(self.player.silver_horn)+"\n")
         save.write(str(classes)+"\n")
         save.write(str(self.player.first_battle)+"\n")
         save.write(str(self.player.weapon[0])+"\n")
         save.write(str(self.player.weapon[1])+"\n")
         save.write(str(self.player.plan_rusty_sword)+"\n")
         save.write(str(self.player.plan_wooden_staff)+"\n")
         save.write(str(self.player.plan_wooden_bow)+"\n")
         save.write(str(self.player.work_bench)+"\n")
         save.write(str(self.player.wood)+"\n")
         save.write(str(self.player.bronze)+"\n")
         save.write(str(self.player.iron)+"\n")
         save.write(str(self.player.steel)+"\n")
         save.write(str(self.player.gold)+"\n")
         save.write(str(self.player.silver)+"\n")
         save.write(str(self.player.dragon_blood)+"\n")
         save.write(str(self.player.rift_first)+"\n")
         save.write(str(self.player.str)+"\n")
         save.write(str(self.player.dex)+"\n")
         save.write(str(self.player.int)+"\n")
         save.write(str(self.player.vit)+"\n")
         save.write(str(self.player.drop)+"\n")
         save.write(str(self.player.x)+"\n")
         save.write(str(self.player.y)+"\n")
         save.write(str(self.player.first_tavern)+"\n")
         # save.write(str()+"\n")

         for list in self.player.weapon_inv:
            s = '%s,%s,%s,%s,%s,%s,%s,%s,%s' % (list[0], list[1], list[2], list[3], list[4], list[5], list[6], list[7], list[8])
            wep.write(str(s)+"\n")

         for list in self.player.quests:
            s = '%s,%s,%s,%s,%s,%s,%s' % (list[0], list[1], list[2], list[3], list[4], list[5], list[6])
            quest.write(str(s)+"\n")

         save.close()
         wep.close()
         quest.close()
         print "Game Saved...."
         raw_input ("Press ENTER to continue")
      except:
         print "Error saving file to '%s'" % saving
         raw_input ("Press ENTER to continue")
      return room

   def shop(self, room, x, y):
       shop = True
       while shop:
          print "[Buy]"
          print "[Sell]"
          print "[Exit]"
          option = raw_input(">>> ")
          option = option.lower()
          if option == 'exit':
              shop = False
              return room
          elif option == 'buy':
              buy = True
              while buy:
                 print "[Pots]"
                 print "[Mats]"
                 print "[Exit]"
                 choosing = raw_input(">>> ")
                 choosing = choosing.lower()
                 if choosing == 'exit':
                    buy = False
                 elif choosing == 'pots':
                    pots = True
                    while pots:
                       print "You have $%s" % self.player.money
                       print "1 Lesser Potion = $25"
                       print "1 Potion = $100"
                       print "1 Greater Potion= $200"
                       print "1 Lesser Mana Potion = $25"
                       print "1 Mana Potion = $100"
                       print "1 Greater Mana Potion = $200"
                       print "[Exit]"
                       pot = raw_input("What would you like to buy: ")
                       pot = pot.lower()
                       if pot == "exit":
                          pots = False 
                       elif pot == "lesser potion":
                          amount = int(raw_input("How many pots would you like to buy? "))
                          money = self.player.money / 25
                          if amount > money:
                             print "You don't have enough money"
                          elif amount <= money:
                             print "You bought %s pots" % amount
                             minus = amount * 25
                             self.player.money -= minus
                             self.player.lessar_potion += amount
                       elif pot == "potion":
                          amount = int(raw_input("How many pots would you like to buy? "))
                          money = self.player.money / 100
                          if amount > money:
                             print "You don't have enough money"
                          elif amount <= money:
                             print "You bought %s pots" % amount
                             minus = amount * 100
                             self.player.money -= minus
                             self.player.potion += amount
                       elif pot == "greater potion":
                          amount = int(raw_input("How many pots would you like to buy? "))
                          money = self.player.money / 200
                          if amount > money:
                             print "You don't have enough money"
                          elif amount <= money:
                             print "You bought %s pots" % amount
                             minus = amount * 200
                             self.player.money -= minus
                             self.player.greater_potion += amount
                       elif pot == "lesser mana potion":
                          amount = int(raw_input("How many pots would you like to buy? "))
                          money = self.player.money / 25
                          if amount > money:
                             print "You don't have enough money"
                          elif amount <= money:
                             print "You bought %s pots" % amount
                             minus = amount * 25
                             self.player.money -= minus
                             self.player.lessar_mana_potion += amount
                       elif pot == "mana potion":
                          amount = int(raw_input("How many pots would you like to buy? "))
                          money = self.player.money / 100
                          if amount > money:
                             print "You don't have enough money"
                          elif amount <= money:
                             print "You bought %s pots" % amount
                             minus = amount * 100
                             self.player.money -= minus
                             self.player.mana_potion += amount
                       elif pot == "greater mana potion":
                          amount = int(raw_input("How many pots would you like to buy? "))
                          money = self.player.money / 200
                          if amount > money:
                             print "You don't have enough money"
                          elif amount <= money:
                             print "You bought %s pots" % amount
                             minus = amount * 200
                             self.player.money -= minus
                             self.player.greater_mana_potion += amount
                       else:
                          "Invalid Syntax"
                 elif choosing == "mats":
                    mats = True
                    while mats:
                       print '1 Scrap Metal = $5'
                       print '1 Wood = $5'
                       if classes == 'warrior':
                          print 'Plan: Rusty Sword = $30'
                       if classes == 'mage':
                          print 'Plan: Wooden Staff = $30'
                       if classes == 'archer':
                          print 'Plan: Wooden Bow = $30'
                       print '[Exit]'
                       mat = raw_input("What would you like to buy: ")
                       mat = mat.lower()
                       if mat == "exit":
                          mats = False
                       elif mat == "junk metal":
                          amount = int(raw_input("How many would you like to buy? "))
                          money = self.player.money / 5
                          if amount > money:
                             print "You don't have enough money"
                          elif amount <= money:
                             print "You bought %s" % amount
                             minus = amount * 5
                             self.player.money -= minus
                             self.player.junk_metal += amount
                       elif mat == "wood":
                          amount = int(raw_input("How many would you like to buy? "))
                          money = self.player.money / 5
                          if amount > money:
                             print "You don't have enough money"
                          elif amount <= money:
                             print "You bought %s" % amount
                             minus = amount * 5
                             self.player.money -= minus
                             self.player.wood += amount
                       elif 'wooden bow' in mat and classes == 'archer':
                          if self.player.money < 30:
                             print "You don't have enough money"
                          elif self.player.money >= 30:
                             print "You bought 1 Plan"
                             minus = 30
                             self.player.money -= minus
                             self.player.plan_wooden_bow += 1
                       elif 'wooden staff' in mat and classes == 'mage':
                          if self.player.money < 30:
                             print "You don't have enough money"
                          elif self.player.money >= 30:
                             print "You bought 1 Plan"
                             minus = 30
                             self.player.money -= minus
                             self.player.plan_wooden_staff += 1
                       elif 'rusty sword' in mat and classes == 'warrior':
                          if self.player.money < 30:
                             print "You don't have enough money"
                          elif self.player.money >= 30:
                             print "You bought 1 Plan"
                             minus = 30
                             self.player.money -= minus
                             self.player.plan_rusty_sword += 1
                       else:
                          "Invalid Syntax"
                       
                 else:
                    "Invalid Syntax"
           
          elif option == 'sell':
             sell = True
             while sell:
                 print "[Pots]"
                 print "[Mats]"
                 print "[Equipment]"
                 print "[Exit]"
                 choosing = raw_input(">>> ")
                 choosing = choosing.lower()
                 if choosing == 'exit':
                    sell = False
                 elif choosing == 'pots':
                    pots = True
                    while pots:
                       print "You have $%s" % self.player.money
                       print "Lesser Potion = %s" % self.player.lessar_potion
                       print "Potion = %s" % self.player.potion
                       print "Greater Potion = %s" % self.player.greater_potion
                       print "Lesser Mana Potion = %s" % self.player.lessar_mana_potion
                       print "Mana Potion = %s" % self.player.mana_potion
                       print "Greater Mana Potion = %s" % self.player.greater_mana_potion
                       print "exit"
                       pot = raw_input("What would you like to sell: ")
                       pot = pot.lower()
                       if pot == "exit":
                          pots = False 
                       elif pot == "lesser potion":
                          amount = int(raw_input("How many pots would you like to sell? "))
                          if amount > self.player.lessar_potion:
                             print "You don't have enough pots"
                          elif amount <= self.player.lessar_potion:
                             print "You sold %s pots" % amount
                             money = amount * 75
                             print "You recieve $%s" % money
                             self.player.money += money
                             self.player.lessar_potion -= amount
                       elif pot == "potion":
                          amount = int(raw_input("How many pots would you like to sell? "))
                          if amount > self.player.potion:
                             print "You don't have enough pots"
                          elif amount <= self.player.potion:
                             print "You sold %s pots" % amount
                             money = amount * 200
                             print "You recieve $%s" % money
                             self.player.money += money
                             self.player.potion -= amount
                       elif pot == "greater potion":
                          amount = int(raw_input("How many pots would you like to sell? "))
                          if amount > self.player.greater_potion:
                             print "You don't have enough pots"
                          elif amount <= self.player.greater_potion:
                             print "You sold %s pots" % amount
                             money = amount * 350
                             print "You recieve $%s" % money
                             self.player.money += money
                             self.player.greater_potion -= amount
                       elif pot == "lesser mana potion":
                          amount = int(raw_input("How many pots would you like to sell? "))
                          if amount > self.player.lessar_mana_potion:
                             print "You don't have enough pots"
                          elif amount <= self.player.lessar_mana_potion:
                             print "You sold %s pots" % amount
                             money = amount * 75
                             print "You recieve $%s" % money
                             self.player.money += money
                             self.player.lessar_mana_potion -= amount
                       elif pot == "mana potion":
                          amount = int(raw_input("How many pots would you like to sell? "))
                          if amount > self.player.mana_potion:
                             print "You don't have enough pots"
                          elif amount <= self.player.mana_potion:
                             print "You sold %s pots" % amount
                             money = amount * 200
                             print "You recieve $%s" % money
                             self.player.money += money
                             self.player.mana_potion -= amount
                       elif pot == "greater mana potion":
                          amount = int(raw_input("How many pots would you like to sell? "))
                          if amount > self.player.greater_mana_potion:
                             print "You don't have enough pots"
                          elif amount <= self.player.greater_mana_potion:
                             print "You sold %s pots" % amount
                             money = amount * 350
                             print "You recieve $%s" % money
                             self.player.money += money
                             self.player.greater_mana_potion -= amount
                       else:
                           print "Invalid Syntax"
                 elif choosing == "mats":
                    mats = True
                    while mats:
                       print "Junk Metal = %s" % self.player.junk_metal
                       print '[Exit]'
                       mat = raw_input("What would you like to sell: ")
                       mat = mat.lower()
                       if mat == "exit":
                          mats = False
                       elif mat == "junk metal":
                          amount = int(raw_input("How much much junk metal do you want to sell? "))
                          if amount > self.player.junk_metal:
                             print "You don't have enough junk metal"
                          elif amount <= self.player.junk_metal:
                             print "You sold %s junk metal" % amount
                             money = amount * 5
                             print "You recieve $%s" % money
                             self.player.money += money
                             self.player.junk_metal -= amount
                       elif mat == "wood":
                          amount = int(raw_input("How much much junk metal do you want to sell? "))
                          if amount > self.player.wood:
                             print "You don't have enough Wood"
                          elif amount <= self.player.wood:
                             print "You sold %s Wood" % amount
                             money = amount * 5
                             print "You recieve $%s" % money
                             self.player.money += money
                             self.player.wood -= amount
                       else:
                           print "Invalid Syntax"
                 elif choosing == "equipment":
                    while True:
                       listn = []
                       print "You Have $%s" % self.player.money
                       print "Weapon Equiped: %s Damage: %s, Str = %s, Dex = %s, Int = %s, Vit = %s, Drop+ = %s" % (self.player.weapon[0], self.player.weapon[1], self.player.str, self.player.dex, self.player.int, self.player.vit, self.player.drop)
                       side_format = 0
                       number_check = 0
                       for list in self.player.weapon_inv:
                          if len(list[0]) > side_format:
                             side_format = len(list[0])
                       for list in self.player.weapon_inv:
                          l0 = list[0].rjust(side_format)
                          l3 = list[3].rjust(7)
                          print "%s(%s): Class = %s, Damage = %s, Str = %s, Dex = %s, Int = %s, Vit = %s, Drop+ = %s, $%s" % (l0, number_check, l3, list[1], list[4], list[5], list[6], list[7], list[8], list[2])
                          listn.append([list[0], list[2], list[3], number_check])
                          number_check += 1
                       print '[Exit]'
                       eq = raw_input("Type what you would like to sell: ")
                       eq = eq.lower()
                       if eq == 'exit':
                          break
                       num = 0
                       try:
                          c = classes.lower()
                          for list in listn:
                             z = list[0].lower()
                             h = list[2].lower()
                             if int(eq) == list[3]:
                                 if list[0] == self.player.weapon[0]:
                                    print 'Can\'t sell Equiped items!!!'
                                 else:
                                    self.player.money += list[1]
                                    self.player.weapon_inv.pop(num)
                                    print 'Item Sold for $%s' % list[1]
                                    print 'You know have $%s' % self.player.money
                                    print ""
                             num += 1
                       except:
                          print 'Invalid ID Value'
                 else:
                    print 'Invalid Syntax'
          
        
          else:
             print "Invalid Syntax"

   def inv(self, room, x, y):
      inventory = True
      while inventory:
         print "[Pots]"
         print "[Items]"
         print "[Equipment]"
         if self.player.work_bench > 0:
            print "[Crafting]"
         game_inv = raw_input(">>> ")
         game_inv = game_inv.lower()
         if game_inv == 'items':
            items = True
            while items:
               print "Scrap Metal: %s" % self.player.junk_metal
               print "Wood: %s" % self.player.wood
               print "Bronze: %s" % self.player.bronze
               print "Iron: %s" % self.player.iron
               print "Steel: %s" % self.player.steel
               print "Silver: %s" % self.player.silver
               print "Gold: %s" % self.player.gold
               if self.player.dragon_blood > 0:
                  print "Dragon Blood: %s" % self.player.junk_metal
               if self.player.ocean_gem > 0:
                  print "Ocean Gem: %s" % self.player.ocean_gem
               if self.player.silver_horn > 0:
                  print "Silver Horn: Aquired"
               print "Type 'Descripton' to find out what items do....."
               select = raw_input("Type what item you want to 'Use' or hit Enter to leave: ")
               select = select.lower()
               if select  == 'description':
                  print "Scrap Metal: Used to sell for money or crafting (Future Update)"
                  if self.player.ocean_gem > 0:
                     print "Ocean Gem: A magical gem but is unknown what it does."
                  if self.player.silver_horn > 0:
                     print "Silver Horn: A Mythical horn known to open a hall of riches."
                  raw_input("Press ENTER to continue")
               elif select == 'silver horn':
                  print 'You blow through the horn and it\'s sound echos through the mountains.'
                  raw_input("Press ENTER to continue")
               elif select == 'ocean gem':
                  print 'The gem shines in the sunlight'
                  raw_input("Press ENTER to continue")
               elif select == 'junk metal':
                  print "(Place Holder) Will be used for future crafting"
                  raw_input("Press ENTER to continue")
               else:
                  items = False
         elif game_inv == 'pots':
            pots = True
            while pots:
               print "Lesser Potion: %s" % self.player.lessar_potion
               print "Potion: %s" % self.player.potion
               print "Greater Potion: %s" % self.player.greater_potion
               print "Lesser Mana Potion: %s" % self.player.lessar_mana_potion
               print "Mana Potion: %s" % self.player.mana_potion
               print "Greater Mana Potion: %s" % self.player.greater_mana_potion
               print "Type 'Descripton' to find out what items do....."
               select = raw_input("Type what item you want to 'Use' or hit Enter to leave: ")
               select = select.lower()
               if select  == 'description':
                  print "Lesser Potion: Heals 100 HP"
                  print "Potion: Heals 200 HP"
                  print "Greater Potion: Heals 300 HP"
                  print "Lesser Mana Potion: Gives 100 MP"
                  print "Mana Potion: Gives 200 MP"
                  print "Greater Mana Potion: Gives 300 MP"
               elif select == 'lesser potion':
                  if self.player.lessar_potion <= 0:
                     print "You do not have any Lesser Potions left"
                  elif self.player.lessar_potion > 0:
                     print "You use a potion"
                     self.player.hp += 100
                     self.player.lessar_potion -= 1
                     print "You heal 100 hp"
                     if self.player.hp > self.player.max_hp:
                        self.player.hp = self.player.max_hp
                     print "You now have: %s / %s" % (self.player.hp, self.player.max_hp)
               elif select == 'potion':
                  if self.player.potion <= 0:
                     print "You do not have any Potions left"
                  elif self.player.potion > 0:
                     print "You use a potion"
                     self.player.hp += 200
                     self.player.potion -= 1
                     print "You heal 200 hp"
                     if self.player.hp > self.player.max_hp:
                        self.player.hp = self.player.max_hp
                     print "You now have: %s / %s" % (self.player.hp, self.player.max_hp)
               elif select == 'greater potion':
                  if self.player.greater_potion <= 0:
                     print "You do not have any Greater Potions left"
                  elif self.player.greater_potion > 0:
                     print "You use a potion"
                     self.player.hp += 300
                     self.player.greater_potion -= 1
                     print "You heal 300 hp"
                     if self.player.hp > self.player.max_hp:
                        self.player.hp = self.player.max_hp
                     print "You now have: %s / %s" % (self.player.hp, self.player.max_hp)
               elif select == 'lesser mana potion':
                  if self.player.lessar_mana_potion <= 0:
                     print "You do not have any Lesser Mana Potions left"
                  elif self.player.lessar_mana_potion > 0:
                     print "You use a lessar mana potion"
                     self.player.mana += 100
                     self.player.lessar_mana_potion -= 1
                     print "You gain 100 mana"
                     if self.player.mana > self.player.max_mana:
                        self.player.mana = self.player.max_mana
                     print "You now have: %s / %s" % (self.player.mana, self.player.max_mana)
               elif select == 'mana potion':
                  if self.player.mana_potion <= 0:
                     print "You do not have any Mana Potions left"
                  elif self.player.mana_potion > 0:
                     print "You use a mana potion"
                     self.player.mana += 200
                     self.player.mana_potion -= 1
                     print "You gain 200 mana"
                     if self.player.mana > self.player.max_mana:
                        self.player.mana = self.player.max_mana
                     print "You now have: %s / %s" % (self.player.mana, self.player.max_mana)
               elif select == 'greater mana potion':
                  if self.player.greater_mana_potion <= 0:
                     print "You do not have any Greater Mana Potions left"
                  elif self.player.greater_mana_potion > 0:
                     print "You use a greater mana potion"
                     self.player.mana += 300
                     self.player.greater_mana_potion -= 1
                     print "You heal 300 hp"
                     if self.player.mana > self.player.max_mana:
                        self.player.mana = self.player.max_mana
                     print "You now have: %s / %s" % (self.player.mana, self.player.max_mana)
               else:
                  pots = False
         elif game_inv == 'equipment':
            while True:
                listn = []
                print "Weapon Equiped: %s Damage: %s, Str = %s, Dex = %s, Int = %s, Vit = %s, Drop+ = %s" % (self.player.weapon[0], self.player.weapon[1], self.player.str, self.player.dex, self.player.int, self.player.vit, self.player.drop)
                side_format = 0
                number_checker_thing = 0
                for list in self.player.weapon_inv:
                   if len(list[0]) > side_format:
                      side_format = len(list[0])
                for list in self.player.weapon_inv:
                   l0 = list[0].rjust(side_format)
                   l3 = list[3].rjust(7)
                   print "%s(%s): Class = %s, Damage = %s, Str = %s, Dex = %s, Int = %s, Vit = %s, Drop+ = %s, $%s" % (l0, number_checker_thing, l3, list[1], list[4], list[5], list[6], list[7], list[8], list[2])
                   listn.append([list[0], list[1], list[3], number_checker_thing, list[4], list[5], list[6], list[7], list[8]])
                   number_checker_thing += 1

                equip = raw_input("Type what you would like to equip or hit enter: ")
                equip = equip.lower()
                if equip == "":
                   break
                try:
                   for list in listn:
                       if int(equip) == list[3]:
                           if list[2] == classes:
                               self.player.weapon[0] = list[0]
                               self.player.weapon[1] = list[1]
                               self.player.str = list[4]
                               self.player.dex = list[5]
                               self.player.int = list[6]
                               self.player.max_hp -= (self.player.vit * 2)
                               if self.player.hp > self.player.max_hp:
                                  self.player.hp = self.player.max_hp
                               self.player.vit = list[7]
                               self.player.max_hp += (self.player.vit * 2)
                               self.player.drop = list[8]
                               print "You have equipped a '%s'" % self.player.weapon[0]
                               print ""
                           else:
                               print 'Can\'t Equip %s Weapons' % list[2]
                               print ""
                except:
                   print "Invalid ID Value"
                        
         elif game_inv == 'crafting' and self.player.work_bench > 0:
            while True:
               if self.player.plan_rusty_sword > 0:
                  print 'Rusty Sword: 5 Scrap metal, 2 Wood'
               if self.player.plan_wooden_staff > 0:
                  print 'Wooden Staff: 7 Wood'
               if self.player.plan_wooden_bow > 0:
                  print 'Wooden Bow: 7 Wood'
               plan = raw_input("Enter what you want to build or type [Exit] to go back>>> ")
               plan = plan.lower()
               if plan == 'exit':
                  break
               elif plan == 'rusty sword' and self.player.plan_rusty_sword > 0:
                  if self.player.junk_metal >= 5 and self.player.wood >= 2:
                     self.player.junk_metal -= 5
                     self.player.wood -= 2
                     print 'You have made a Rusty Sword...'
                     self.player.weapon_inv.append('Rusty Sword', 2, 30, 'warrior', 0, 0, 0, 0, 0)
               elif plan == 'wooden staff' and self.player.plan_wooden_staff > 0:
                  if self.player.wood >= 7:
                     self.player.wood -= 7
                     print 'You have made a Wooden Staff...'
                     self.player.weapon_inv.append('Wooden Staff', 2, 30, 'mage', 0, 0, 0, 0, 0)
               elif plan == 'wooden bow' and self.player.plan_wooden_staff > 0:
                  if self.player.wood >= 7:
                     self.player.wood -= 7
                     print 'You have made a Wooden Bow...'
                     self.player.weapon_inv.append('Wooden Bow', 2, 30, 'archer', 0, 0, 0, 0, 0)
               else:
                  print 'Invalid Syntax'
         else:
            inventory = False
            return room, x, y

   def area_one(self, x, y):
      # Plays the intro if this is the first time starting.
      if not self.player.intro_done:
         print "\n{Text}You are about to stumble into a strange world."
         print "{Text}With it comes vicious creatures."
         print "{Text}At any time you can type 'options' display your current stats."
         print "{Text}Type 'Save' to save your game status."
         print '''
{Text}!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
{Text}!                                                !
{Text}! Type the following keys to move around the map !
{Text}!                --------------                  !
{Text}!               |    W = Up    |                 !
{Text}!    -----------------------------------------   !
{Text}!   | A = Left  |   S = Down   |   D = Right  |  !
{Text}!    -----------------------------------------   !
{Text}!                                                !
{Text}!               # = Out of Bounds                !
{Text}!                                                !
{Text}!     E = Enemy | R =  Rare Enemy | B = Boss     !
{Text}!                                                !
{Text}!               | = Entrance/Exit                !
{Text}!                                                !
{Text}!               ]/[ = Closed Door                !
{Text}!                                                !
{Text}!                   * = Player                   !
{Text}!                                                !
{Text}!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
'''
         raw_input("Press ENTER to continue.")
         print "\n{Text}Your caravan finally comes to a stop."
         if classes == 'warrior':
            new_weapon = ['Beginner Sword', 1, 0, 'warrior', 0, 0, 0, 0, 0]
            self.player.weapon_inv.append(new_weapon)
            self.player.weapon[0] = 'Beginner Sword'
            self.player.weapon[1] = 1
         if classes == 'mage':
            new_weapon = ['Beginner Staff', 1, 0, 'mage', 0, 0, 0, 0, 0]
            self.player.weapon_inv.append(new_weapon)
            self.player.weapon[0] = 'Beginner Staff'
            self.player.weapon[1] = 1
         if classes == 'archer':
            new_weapon = ['Beginner Bow', 1, 0, 'archer', 0, 0, 0, 0, 0]
            self.player.weapon_inv.append(new_weapon)
            self.player.weapon[0] = 'Beginner Bow'
            self.player.weapon[1] = 1
         # Changes intro_done so it plays through only this one time.
         self.player.intro_done = True
		 
      print "\n{Text}You arrive in AREA 1..."
      print "{Text}There are two passable roads in front of you."
      f01 = ['##############',1]
      f02 = ['#          E #',2]
      f03 = [' ####        #',3]
      f04 = [' ####   #    #',4]
      f05 = ['#      ###   |',5]
      f06 = ['#       #R   #',6]
      f07 = ['# E          #',7]
      f08 = ['######|#######',8]
      default = [f01,f02,f03,f04,f05,f06,f07,f08]
      map_layout = default
      x = int(x)
      y = int(y)
      num = -1
      movenment = ''
      while True:
          while num <= len(default)-2:
              num += 1
              holder = map_layout[num]
              printable = holder[0]
              if num == y-1:
                  replacment = list(holder[0])
                  replacment[x - 1] = '*'
                  replacment = ''.join(replacment)
                  printable = replacment
              print printable
          num = -1
          movenment = raw_input('>>> ')
          if movenment == 'a':
              place_holder = map_layout[y-1]
              string = list(place_holder[0])
              if string[x-2] == '#':
                  print '[Can\'t Move There]'
              else:
                  x -= 1
              if string[x-1] == 'E':
                  string[x-1] = ' '
                  string = ''.join(string)
                  place_holder[0] = string
                  u = self.renemy.area_1_2_3('normal')
                  u.sys_battle()
              if string[x-1] == 'R':
                  string[x-1] = ' '
                  string = ''.join(string)
                  place_holder[0] = string
                  u = self.renemy.area_1_2_3('rare')
                  u.sys_battle()
          elif movenment == 's':
              place_holder = map_layout[y]
              string = list(place_holder[0])
              if string[x-1] == '|' and x-1 == 6 and y ==7:
                  inv = GameStory(player, 'area_three', renemy)
                  inv.play(6, 2)
              if string[x-1] == '#':
                  print '[Can\'t Move There]'
              else:
                  y += 1
              if string[x-1] == 'E':
                  string[x-1] = ' '
                  string = ''.join(string)
                  place_holder[0] = string
                  u = self.renemy.area_1_2_3('normal')
                  u.sys_battle()
              if string[x-1] == 'R':
                  string[x-1] = ' '
                  string = ''.join(string)
                  place_holder[0] = string
                  u = self.renemy.area_1_2_3('rare')
                  u.sys_battle()
          elif movenment == 'd':
              place_holder = map_layout[y-1]
              string = list(place_holder[0])
              if string[x] == '|' and x == 13 and y-1 == 4:
                  inv = GameStory(player, 'area_two', renemy)
                  inv.play(2, 5)
              if string[x] == '#':
                  print '[Can\'t Move There]'
              else:
                  x += 1
              if string[x-1] == 'E':
                  string[x-1] = ' '
                  string = ''.join(string)
                  place_holder[0] = string
                  u = self.renemy.area_1_2_3('normal')
                  u.sys_battle()
              if string[x-1] == 'R':
                  string[x-1] = ' '
                  string = ''.join(string)
                  place_holder[0] = string
                  u = self.renemy.area_1_2_3('rare')
                  u.sys_battle()
          elif movenment == 'w':
              place_holder = map_layout[y-2]
              string = list(place_holder[0])
              if string[x-1] == '#':
                  print '[Can\'t Move There]'
              else:
                  y -= 1
              if string[x-1] == 'E':
                  string[x-1] = ' '
                  string = ''.join(string)
                  place_holder[0] = string
                  u = self.renemy.area_1_2_3('normal')
                  u.sys_battle()
              if string[x-1] == 'R':
                  string[x-1] = ' '
                  string = ''.join(string)
                  place_holder[0] = string
                  u = self.renemy.area_1_2_3('rare')
                  u.sys_battle()
          elif movenment == "options":
               print self.player.get_stats()
               raw_input("Press ENTER to go back.")
          elif movenment == "inventory":
               inv = GameStory(player, 'area_two', renemy)
               inv.inv('area_two', x, y)
          elif movenment == "save":
               self.player.x = x
               self.player.y = y
               save = GameStory(player, 'area_two', renemy)
               save.save('area_two', x, y)
         
   def area_two(self, x, y):
      print "\n{Text}You arrive in AREA 2..."
      print "{Text}Seems like a relatively peaceful place."
      print "{Text}Looks like we got a couple clear paths ahead of us."
      f01 = ['######|######',1]
      f02 = ['#         E #',2]
      f03 = ['#  E    #   #',3]
      f04 = ['#           #',4]
      f05 = ['|   # R     #',5]
      f06 = ['#  ###   #  #',6]
      f07 = ['#   #   E   #',7]
      f08 = ['#           |',8]
      f09 = ['#############',9]
      default = [f01,f02,f03,f04,f05,f06,f07,f08,f09]
      map_layout = default
      x = int(x)
      y = int(y)
      num = -1
      movenment = ''
      while True:
          while num <= len(default)-2:
              num += 1
              holder = map_layout[num]
              printable = holder[0]
              if num == y-1:
                  replacment = list(holder[0])
                  replacment[x - 1] = '*'
                  replacment = ''.join(replacment)
                  printable = replacment
              print printable
          num = -1
          movenment = raw_input('>>> ')
          if movenment == 'a':
              place_holder = map_layout[y-1]
              string = list(place_holder[0])
              if string[x-2] == '|' and x -2 == 0 and y -1 == 4:
                  inv = GameStory(player, 'area_one', renemy)
                  inv.play(13, 5)
              if string[x-2] == '#':
                  print '[Can\'t Move There]'
              else:
                  x -= 1
              if string[x-1] == 'E':
                  string[x-1] = ' '
                  string = ''.join(string)
                  place_holder[0] = string
                  u = self.renemy.area_1_2_3('normal')
                  u.sys_battle()
              if string[x-1] == 'R':
                  string[x-1] = ' '
                  string = ''.join(string)
                  place_holder[0] = string
                  u = self.renemy.area_1_2_3('rare')
                  u.sys_battle()
          elif movenment == 's':
              place_holder = map_layout[y]
              string = list(place_holder[0])
              if string[x-1] == '#':
                  print '[Can\'t Move There]'
              else:
                  y += 1
              if string[x-1] == 'E':
                  string[x-1] = ' '
                  string = ''.join(string)
                  place_holder[0] = string
                  u = self.renemy.area_1_2_3('normal')
                  u.sys_battle()
              if string[x-1] == 'R':
                  string[x-1] = ' '
                  string = ''.join(string)
                  place_holder[0] = string
                  u = self.renemy.area_1_2_3('rare')
                  u.sys_battle()
          elif movenment == 'd':
              place_holder = map_layout[y-1]
              string = list(place_holder[0])
              if string[x] == '|' and x == 12 and y-1 == 7:
                  inv = GameStory(player, 'cave1', renemy)
                  inv.play(8, 11)
              if string[x] == '#':
                  print '[Can\'t Move There]'
              else:
                  x += 1
              if string[x-1] == 'E':
                  string[x-1] = ' '
                  string = ''.join(string)
                  place_holder[0] = string
                  u = self.renemy.area_1_2_3('normal')
                  u.sys_battle()
              if string[x-1] == 'R':
                  string[x-1] = ' '
                  string = ''.join(string)
                  place_holder[0] = string
                  u = self.renemy.area_1_2_3('rare')
                  u.sys_battle()
          elif movenment == 'w':
              place_holder = map_layout[y-2]
              string = list(place_holder[0])
              if string[x-1] == '|' and x - 1== 6 and y - 2 == 0:
                  inv = GameStory(player, 'area_five', renemy)
                  inv.play(5, 9)
              if string[x-1] == '#':
                  print '[Can\'t Move There]'
              else:
                  y -= 1
              if string[x-1] == 'E':
                  string[x-1] = ' '
                  string = ''.join(string)
                  place_holder[0] = string
                  u = self.renemy.area_1_2_3('normal')
                  u.sys_battle()
              if string[x-1] == 'R':
                  string[x-1] = ' '
                  string = ''.join(string)
                  place_holder[0] = string
                  u = self.renemy.area_1_2_3('rare')
                  u.sys_battle()
          elif movenment == "options":
               print self.player.get_stats()
               raw_input("Press ENTER to go back.")
          elif movenment == "inventory":
               inv = GameStory(player, 'area_two', renemy)
               inv.inv('area_two', x, y)
          elif movenment == "save":
               self.player.x = x
               self.player.y = y
               save = GameStory(player, 'area_two', renemy)
               save.save('area_two', x, y)
   
   def area_three(self, x, y):
      if self.player.ocean_gem > 4 and self.player.silver_horn == 1:
         print "{Text}A strange rift opens up infront of you."
         f01 = ['#####|#######',1]
         f02 = ['#  E        #',2]
         f03 = ['#      E    #',3]
         f04 = ['# #       # #',4]
         f05 = ['#  # EO  # E#',5]
         f06 = ['## E#####  ##',6]
         f07 = ['###       ###',7]
         f08 = ['#############',8]
      elif self.player.ocean_gem > 4 and self.player.silver_horn == 0:
         print "{Text}A strange rift opens up infront of you."
         f01 = ['#####|#######',1]
         f02 = ['#  E        #',2]
         f03 = ['#      E    #',3]
         f04 = ['# #       # #',4]
         f05 = ['#  # EO  # E#',5]
         f06 = ['## E#####  ##',6]
         f07 = ['###   !   ###',7]
         f08 = ['#############',8]
      elif self.player.silver_horn == 1:
         f01 = ['#####|#######',1]
         f02 = ['#  E        #',2]
         f03 = ['#      E    #',3]
         f04 = ['# #       # #',4]
         f05 = ['#  # E   # E#',5]
         f06 = ['## E#####  ##',6]
         f07 = ['###       ###',7]
         f08 = ['#############',8]
      else:
         f01 = ['#####|#######',1]
         f02 = ['#  E        #',2]
         f03 = ['#      E    #',3]
         f04 = ['# #       # #',4]
         f05 = ['#  # E   # E#',5]
         f06 = ['## E#####  ##',6]
         f07 = ['###   !   ###',7]
         f08 = ['#############',8]
      default = [f01,f02,f03,f04,f05,f06,f07,f08]
      map_layout = default
      x = int(x)
      y = int(y)
      num = -1
      movenment = ''
      while True:
          while num <= len(default)-2:
              num += 1
              holder = map_layout[num]
              printable = holder[0]
              if num == y-1:
                  replacment = list(holder[0])
                  replacment[x - 1] = '*'
                  replacment = ''.join(replacment)
                  printable = replacment
              print printable
          num = -1
          movenment = raw_input('>>> ')
          if movenment == 'a':
              place_holder = map_layout[y-1]
              string = list(place_holder[0])
              if string[x-2] == 'O' and x - 2== 6 and y - 1 ==4:
                  inv = GameStory(player, 'rift', renemy)
                  inv.play(2, 11)
              if string[x-2] == '!' and x-2== 6 and y - 1 == 6:
                  print "\n{Text}This might be of some use."
                  print "\n{Text}*Silver Horn Obtained*"
                  self.player.silver_horn = 1
                  string[x-2] = ' '
                  string = ''.join(string)
                  place_holder[0] = string
              if string[x-2] == '#':
                  print '[Can\'t Move There]'
              else:
                  x -= 1
              if string[x-1] == 'E':
                  string[x-1] = ' '
                  string = ''.join(string)
                  place_holder[0] = string
                  u = self.renemy.area_1_2_3('normal')
                  u.sys_battle()
              if string[x-1] == 'R':
                  string[x-1] = ' '
                  string = ''.join(string)
                  place_holder[0] = string
                  u = self.renemy.area_1_2_3('rare')
                  u.sys_battle()
          elif movenment == 's':
              place_holder = map_layout[y]
              string = list(place_holder[0])
              if string[x-1] == 'O' and x - 1== 6 and y ==4:
                  inv = GameStory(player, 'rift', renemy)
                  inv.play(2, 11)
              if string[x-1] == '#':
                  print '[Can\'t Move There]'
              else:
                  y += 1
              if string[x-1] == 'E':
                  string[x-1] = ' '
                  string = ''.join(string)
                  place_holder[0] = string
                  u = self.renemy.area_1_2_3('normal')
                  u.sys_battle()
              if string[x-1] == 'R':
                  string[x-1] = ' '
                  string = ''.join(string)
                  place_holder[0] = string
                  u = self.renemy.area_1_2_3('rare')
                  u.sys_battle()
          elif movenment == 'd':
              place_holder = map_layout[y-1]
              string = list(place_holder[0])
              if string[x] == 'O' and x == 6 and y - 1 ==4:
                  inv = GameStory(player, 'rift', renemy)
                  inv.play(2, 11)
              if string[x] == '!' and x== 6 and y - 1 == 6:
                  print "\n{Text}This might be of some use."
                  print "\n{Text}*Silver Horn Obtained*"
                  self.player.silver_horn = 1
                  string[x-2] = ' '
                  string = ''.join(string)
                  place_holder[0] = string
              if string[x] == '#':
                  print '[Can\'t Move There]'
              else:
                  x += 1
              if string[x-1] == 'E':
                  string[x-1] = ' '
                  string = ''.join(string)
                  place_holder[0] = string
                  u = self.renemy.area_1_2_3('normal')
                  u.sys_battle()
              if string[x-1] == 'R':
                  string[x-1] = ' '
                  string = ''.join(string)
                  place_holder[0] = string
                  u = self.renemy.area_1_2_3('rare')
                  u.sys_battle()
          elif movenment == 'w':
              place_holder = map_layout[y-2]
              string = list(place_holder[0])
              if string[x-1] == '|' and x - 1== 5 and y - 2 == 0:
                  inv = GameStory(player, 'area_one', renemy)
                  inv.play(7, 7)
              if string[x-1] == '#':
                  print '[Can\'t Move There]'
              else:
                  y -= 1
              if string[x-1] == 'E':
                  string[x-1] = ' '
                  string = ''.join(string)
                  place_holder[0] = string
                  u = self.renemy.area_1_2_3('normal')
                  u.sys_battle()
              if string[x-1] == 'R':
                  string[x-1] = ' '
                  string = ''.join(string)
                  place_holder[0] = string
                  u = self.renemy.area_1_2_3('rare')
                  u.sys_battle()
          elif movenment == "options":
               print self.player.get_stats()
               raw_input("Press ENTER to go back.")
          elif movenment == "inventory":
               inv = GameStory(player, 'area_three', renemy)
               inv.inv('area_three', x, y)
          elif movenment == "save":
               self.player.x = x
               self.player.y = y
               save = GameStory(player, 'area_three', renemy)
               save.save('area_three', x, y)
         
   def cave1(self, x, y):
      if self.player.first_battle:
         f01 = ['      ###      ',1]
         f02 = ['  ####!# ####  ',2]
         f03 = [' #         ! # ',3]
         f04 = ['##  #######  ##',4]
         f05 = ['###  #####  ###',5]
         f06 = ['####  ###  ####',6]
         f07 = ['#####  #  #####',7]
         f08 = ['#      !   !  #',8]
         f09 = ['#  !          #',9]
         f10 = [' #           # ',10]
         f11 = ['  ####  !####  ',11]
         f12 = ['      #|#      ',12]

      else:
         f01 = ['      ###      ',1]
         f02 = ['  #### # ####  ',2]
         f03 = [' #     B     # ',3]
         f04 = ['##  #######  ##',4]
         f05 = ['###  #####  ###',5]
         f06 = ['####  ###  ####',6]
         f07 = ['#####  #  #####',7]
         f08 = ['#             #',8]
         f09 = ['#             #',9]
         f10 = [' #           # ',10]
         f11 = ['  ####   ####  ',11]
         f12 = ['      #|#      ',12]
      default = [f01,f02,f03,f04,f05,f06,f07,f08,f09,f10,f11,f12]
      map_layout = default
      x = int(x)
      y = int(y)
      num = -1
      movenment = ''
      while True:
          while num <= len(default)-2:
              num += 1
              holder = map_layout[num]
              printable = holder[0]
              if num == y-1:
                  replacment = list(holder[0])
                  replacment[x - 1] = '*'
                  replacment = ''.join(replacment)
                  printable = replacment
              print printable
          num = -1
          movenment = raw_input('>>> ')
          if movenment == 'a':
              place_holder = map_layout[y-1]
              string = list(place_holder[0])
              if string[x-2] == 'B' and x - 2== 7 and y - 1 <=2:
                  string[x-2] = ' '
                  string = ''.join(string)
                  place_holder[0] = string
                  u = self.renemy.area_four_boss()
                  u.sys_battle()
                  self.player.first_battle = True
                  inv = GameStory(player, 'cave1', renemy)
                  inv.play(8, 3)
              if string[x-2] == '#':
                  print '[Can\'t Move There]'
              else:
                  x -= 1
              if string[x-1] == 'E':
                  string[x-1] = ' '
                  string = ''.join(string)
                  place_holder[0] = string
                  u = self.renemy.area_1_2_3()
                  u.sys_battle()
              if string[x-1] == 'R':
                  string[x-1] = ' '
                  string = ''.join(string)
                  place_holder[0] = string
                  u = self.renemy.area_1_2_3()
                  u.sys_battle()
              if string[x-1] == '!':
                  string[x-1] = ' '
                  string = ''.join(string)
                  place_holder[0] = string
                  if self.player.ocean_gem < 5:
                     print 'You find some Ocean Gems and Pick them Up!'
                     self.player.ocean_gem += 1
                  else:
                     print 'You have enough Ocean Gems Already!'
          elif movenment == 's':
              place_holder = map_layout[y]
              string = list(place_holder[0])
              if string[x-1] == '|' and x - 1== 7 and y ==11:
                  inv = GameStory(player, 'area_two', renemy)
                  inv.play(12, 8)
              if string[x-1] == '#':
                  print '[Can\'t Move There]'
              else:
                  y += 1
              if string[x-1] == 'E':
                  string[x-1] = ' '
                  string = ''.join(string)
                  place_holder[0] = string
                  u = self.renemy.area_1_2_3()
                  u.sys_battle()
              if string[x-1] == 'R':
                  string[x-1] = ' '
                  string = ''.join(string)
                  place_holder[0] = string
                  u = self.renemy.area_1_2_3()
                  u.sys_battle()
              if string[x-1] == '!':
                  string[x-1] = ' '
                  string = ''.join(string)
                  place_holder[0] = string
                  if self.player.ocean_gem < 5:
                     print 'You find some Ocean Gems and Pick them Up!'
                     self.player.ocean_gem += 1
                  else:
                     print 'You have enough Ocean Gems Already!'
          elif movenment == 'd':
              place_holder = map_layout[y-1]
              string = list(place_holder[0])
              if string[x] == 'B' and x== 7 and y - 1 <=2:
                  string[x] = ' '
                  string = ''.join(string)
                  place_holder[0] = string
                  u = self.renemy.area_four_boss()
                  u.sys_battle()
                  self.player.first_battle = True
                  inv = GameStory(player, 'cave1', renemy)
                  inv.play(8, 3)
              if string[x] == '#':
                  print '[Can\'t Move There]'
              else:
                  x += 1
              if string[x-1] == 'E':
                  string[x-1] = ' '
                  string = ''.join(string)
                  place_holder[0] = string
                  u = self.renemy.area_1_2_3()
                  u.sys_battle()
              if string[x-1] == 'R':
                  string[x-1] = ' '
                  string = ''.join(string)
                  place_holder[0] = string
                  u = self.renemy.area_1_2_3()
                  u.sys_battle()
              if string[x-1] == '!':
                  string[x-1] = ' '
                  string = ''.join(string)
                  place_holder[0] = string
                  if self.player.ocean_gem < 5:
                     print 'You find some Ocean Gems and Pick them Up!'
                     self.player.ocean_gem += 1
                  else:
                     print 'You have enough Ocean Gems Already!'
          elif movenment == 'w':
              place_holder = map_layout[y-2]
              string = list(place_holder[0])
              if string[x-1] == '|' and x - 1== 4 and y - 2 == 7 and self.player.silver_horn == 1:
                  print 'You enter the Shack and see a Mall'
                  shop = GameStory(player, 'area_five', renemy)
                  shop.shop('area_five')
              if string[x-1] == '|' and x - 1== 4 and y - 2 == 7 and self.player.silver_horn == 0:
                  print 'You enter the shack and find nothing interesting!'
              if string[x-1] == '#':
                  print '[Can\'t Move There]'
              else:
                  y -= 1
              if string[x-1] == 'E':
                  string[x-1] = ' '
                  string = ''.join(string)
                  place_holder[0] = string
                  u = self.renemy.area_1_2_3()
                  u.sys_battle()
              if string[x-1] == 'R':
                  string[x-1] = ' '
                  string = ''.join(string)
                  place_holder[0] = string
                  u = self.renemy.area_1_2_3()
                  u.sys_battle()
              if string[x-1] == '!':
                  string[x-1] = ' '
                  string = ''.join(string)
                  place_holder[0] = string
                  if self.player.ocean_gem < 5:
                     print 'You find some Ocean Gems and Pick them Up!'
                     self.player.ocean_gem += 1
                  else:
                     print 'You have enough Ocean Gems Already!'
          elif movenment == "options":
               print self.player.get_stats()
               raw_input("Press ENTER to go back.")
          elif movenment == "inventory":
               inv = GameStory(player, 'cave1', renemy)
               inv.inv('cave1', x, y)
          elif movenment == "save":
               self.player.x = x
               self.player.y = y
               save = GameStory(player, 'cave1', renemy)
               save.save('cave1', x, y)

   def area_five(self, x, y):
      print "{Text}You see an old shack infront of you."
      f01 = ['#########',1]
      f02 = ['##     ##',2]
      f03 = ['#       #',3]
      f04 = ['#  ###  #',4]
      f05 = ['# ##### #',5]
      f06 = ['# ##### #',6]
      f07 = ['# ##### #',7]
      f08 = ['#  #|#  #',8]
      f09 = ['#       #',9]
      f10 = ['####|####',10]
      default = [f01,f02,f03,f04,f05,f06,f07,f08,f09,f10]
      map_layout = default
      x = int(x)
      y = int(y)
      num = -1
      movenment = ''
      while True:
          while num <= len(default)-2:
              num += 1
              holder = map_layout[num]
              printable = holder[0]
              if num == y-1:
                  replacment = list(holder[0])
                  replacment[x - 1] = '*'
                  replacment = ''.join(replacment)
                  printable = replacment
              print printable
          num = -1
          movenment = raw_input('>>> ')
          if movenment == 'a':
              place_holder = map_layout[y-1]
              string = list(place_holder[0])
              if string[x-2] == '#':
                  print '[Can\'t Move There]'
              else:
                  x -= 1
              if string[x-1] == 'E':
                  string[x-1] = ' '
                  string = ''.join(string)
                  place_holder[0] = string
                  u = self.renemy.area_1_2_3()
                  u.sys_battle()
              if string[x-1] == 'R':
                  string[x-1] = ' '
                  string = ''.join(string)
                  place_holder[0] = string
                  u = self.renemy.area_1_2_3()
                  u.sys_battle()
          elif movenment == 's':
              place_holder = map_layout[y]
              string = list(place_holder[0])
              if string[x-1] == '|' and x - 1== 4 and y ==9:
                  inv = GameStory(player, 'area_two', renemy)
                  inv.play(7, 2)
              if string[x-1] == '#':
                  print '[Can\'t Move There]'
              else:
                  y += 1
              if string[x-1] == 'E':
                  string[x-1] = ' '
                  string = ''.join(string)
                  place_holder[0] = string
                  u = self.renemy.area_1_2_3()
                  u.sys_battle()
              if string[x-1] == 'R':
                  string[x-1] = ' '
                  string = ''.join(string)
                  place_holder[0] = string
                  u = self.renemy.area_1_2_3()
                  u.sys_battle()
          elif movenment == 'd':
              place_holder = map_layout[y-1]
              string = list(place_holder[0])
              if string[x] == '#':
                  print '[Can\'t Move There]'
              else:
                  x += 1
              if string[x-1] == 'E':
                  string[x-1] = ' '
                  string = ''.join(string)
                  place_holder[0] = string
                  u = self.renemy.area_1_2_3()
                  u.sys_battle()
              if string[x-1] == 'R':
                  string[x-1] = ' '
                  string = ''.join(string)
                  place_holder[0] = string
                  u = self.renemy.area_1_2_3()
                  u.sys_battle()
          elif movenment == 'w':
              place_holder = map_layout[y-2]
              string = list(place_holder[0])
              if string[x-1] == '|' and x - 1== 4 and y - 2 == 7 and self.player.silver_horn == 1:
                  print 'You enter the Shack and see a Mall'
                  shop = GameStory(player, 'area_five', renemy)
                  shop.shop('area_five', 5, 9)
              if string[x-1] == '|' and x - 1== 4 and y - 2 == 7 and self.player.silver_horn == 0:
                  print 'You enter the shack and find nothing interesting!'
              if string[x-1] == '#':
                  print '[Can\'t Move There]'
              else:
                  y -= 1
              if string[x-1] == 'E':
                  string[x-1] = ' '
                  string = ''.join(string)
                  place_holder[0] = string
                  u = self.renemy.area_1_2_3()
                  u.sys_battle()
              if string[x-1] == 'R':
                  string[x-1] = ' '
                  string = ''.join(string)
                  place_holder[0] = string
                  u = self.renemy.area_1_2_3()
                  u.sys_battle()
          elif movenment == "options":
               print self.player.get_stats()
               raw_input("Press ENTER to go back.")
          elif movenment == "inventory":
               inv = GameStory(player, 'area_five', renemy)
               inv.inv('area_five', x, y)
          elif movenment == "save":
               self.player.x = x
               self.player.y = y
               save = GameStory(player, 'area_five', renemy)
               save.save('area_five', x, y)

   def rift(self, x, y):
      if not self.player.rift_first:
         print "{Text}As you go through the rift you hear a voice..."
         print "{Text}'Go see Professer Niru'"
         print "{Text}As you regain consciousness, you notice your in a alley way."
         print "{Text}As you go and explore your surroundings you notice your in a Small Town."
         print "{Text}It's Getting Dark though so you are thinking to go to:\n"
         print "{Location}Bob and Bill's General Store"
         print "{Location}The Rushmanov Beer Hall\n"
         self.player.rift_first = True
      f01 = ['###################',1]
      f02 = ['#                 #',2]
      f03 = ['#       ###   ### #',3]
      f04 = ['#      #####  N## #',4]
      f05 = ['|      #####    # #',5]
      f06 = ['|       #|#       #',6]
      f07 = ['|                 #',7]
      f08 = ['#####             #',8]
      f09 = ['####]   # #       #',9]
      f10 = ['#####  #####  ### #',10]
      f11 = ['#O      # #   ### #',11]
      f12 = ['#####  #####  ### #',12]
      f13 = ['####]   # #   |## #',13]
      f14 = ['#####         ### #',14]
      f15 = ['#                 #',15]
      f16 = ['# # #   # #   # # #',16]
      f17 = ['#                 #',17]
      f18 = ['# # #   # #   # # #',18]
      f19 = ['#                 #',19]
      f20 = ['###################',20]
      default = [f01,f02,f03,f04,f05,f06,f07,f08,f09,f10,f11,f12,f13,f14,f15,f16,f17,f18,f19,f20]
      map_layout = default
      x = int(x)
      y = int(y)
      num = -1
      movenment = ''
      while True:
          while num <= len(default)-2:
              num += 1
              holder = map_layout[num]
              printable = holder[0]
              if num == y-1:
                  replacment = list(holder[0])
                  replacment[x - 1] = '*'
                  replacment = ''.join(replacment)
                  printable = replacment
              print printable
          num = -1
          movenment = raw_input('>>> ')
          if movenment == 'a':
              place_holder = map_layout[y-1]
              string = list(place_holder[0])
              if string[x-2] == '|' and x - 2== 0 and y - 1 <=6 and y-1 >=4:
                  inv = GameStory(player, 'forest', renemy)
                  inv.play(15, 11)
              if string[x-2] == 'O' and x - 2== 1 and y - 1 <=10:
                  inv = GameStory(player, 'area_three', renemy)
                  inv.play(7 , 4)
              if string[x-2] == '#':
                  print '[Can\'t Move There]'
              else:
                  x -= 1
              if string[x-1] == 'E':
                  string[x-1] = ' '
                  string = ''.join(string)
                  place_holder[0] = string
                  u = self.renemy.area_forest('normal')
                  u.sys_battle()
              if string[x-1] == 'R':
                  string[x-1] = ' '
                  string = ''.join(string)
                  place_holder[0] = string
                  u = self.renemy.area_forest('rare')
                  u.sys_battle()
          elif movenment == 's':
              place_holder = map_layout[y]
              string = list(place_holder[0])
              if string[x-1] == '|' and x - 1== 0 and y <=6 and y >=4:
                  return 'forest'
              if string[x-1] == '#':
                  print '[Can\'t Move Their]'
              else:
                  y += 1
              if string[x-1] == 'E':
                  string[x-1] = ' '
                  string = ''.join(string)
                  place_holder[0] = string
                  u = self.renemy.area_forest('normal')
                  u.sys_battle()
              if string[x-1] == 'R':
                  string[x-1] = ' '
                  string = ''.join(string)
                  place_holder[0] = string
                  u = self.renemy.area_forest('rare')
                  u.sys_battle()
          elif movenment == 'd':
              place_holder = map_layout[y-1]
              string = list(place_holder[0])
              if string[x] == '|' and x == 14 and y - 1 ==12:
                  inv = GameStory(player, 'rushmanov', renemy)
                  inv.play(2, 6)
              if string[x] == 'N' and x== 14 and y - 1 == 3:
                  print 'Hello %s' % self.player.name
                  print 'I\'m the Blacksmith Here'
                  print 'What would you like to buy?'
                  shop = GameStory(player, 'rift', renemy)
                  shop.shop('rift', x, y)
                  x -= 1
              if string[x] == '#':
                  print '[Can\'t Move Their]'
              else:
                  x += 1
              if string[x-1] == 'E':
                  string[x-1] = ' '
                  string = ''.join(string)
                  place_holder[0] = string
                  u = self.renemy.area_forest('normal')
                  u.sys_battle()
              if string[x-1] == 'R':
                  string[x-1] = ' '
                  string = ''.join(string)
                  place_holder[0] = string
                  u = self.renemy.area_forest('rare')
                  u.sys_battle()
          elif movenment == 'w':
              place_holder = map_layout[y-2]
              string = list(place_holder[0])
              if string[x-1] == '|' and x - 1== 9 and y - 2 == 5:
                  inv = GameStory(player, 'alchemist', renemy)
                  inv.play(4, 6)
              if string[x-1] == 'N' and x - 1== 14 and y - 2 == 3:
                  print 'Hello %s' % self.player.name
                  print 'I\'m the Blacksmith Here'
                  print 'What would you like to buy?'
                  shop = GameStory(player, 'rift', renemy)
                  shop.shop('rift', x, y)
                  y += 1
              if string[x-1] == '#':
                  print '[Can\'t Move Their]'
              else:
                  y -= 1
              if string[x-1] == 'E':
                  string[x-1] = ' '
                  string = ''.join(string)
                  place_holder[0] = string
                  u = self.renemy.area_forest('normal')
                  u.sys_battle()
              if string[x-1] == 'R':
                  string[x-1] = ' '
                  string = ''.join(string)
                  place_holder[0] = string
                  u = self.renemy.area_forest('rare')
                  u.sys_battle()
          elif movenment == "options":
               print self.player.get_stats()
               raw_input("Press ENTER to go back.")
          elif movenment == "inventory":
               inv = GameStory(player, 'rift', renemy)
               inv.inv('rift', x, y)
          elif movenment == "save":
               self.player.x = x
               self.player.y = y
               save = GameStory(player, 'rift', renemy)
               save.save('rift', x, y)

   def alchemist(self, x, y):
      f01 = [' ##### ',1]
      f02 = ['#     #',2]
      f03 = ['# # # #',3]
      f04 = ['#  N  #',4]
      f05 = ['# # # #',5]
      f06 = ['#     #',6]
      f07 = [' ##|## ',7]
      default = [f01,f02,f03,f04,f05,f06,f07]
      map_layout = default
      x = int(x)
      y = int(y)
      num = -1
      movenment = ''
      while True:
          while num <= len(default)-2:
              num += 1
              holder = map_layout[num]
              printable = holder[0]
              if num == y-1:
                  replacment = list(holder[0])
                  replacment[x - 1] = '*'
                  replacment = ''.join(replacment)
                  printable = replacment
              print printable
          num = -1
          movenment = raw_input('>>> ')
          if movenment == 'a':
              place_holder = map_layout[y-1]
              string = list(place_holder[0])
              if string[x-2] == 'N' and x - 2== 3 and y - 1 ==3:
                  print 'What would you like %s' % self.player.name
                  shop = GameStory(player, 'alchemist', renemy)
                  shop.shop('alchemist', x, y)
                  x += 1
              if string[x-2] == '#':
                  print '[Can\'t Move There]'
              else:
                  x -= 1
              if string[x-1] == 'E':
                  string[x-1] = ' '
                  string = ''.join(string)
                  place_holder[0] = string
                  u = self.renemy.area_forest('normal')
                  u.sys_battle()
              if string[x-1] == 'R':
                  string[x-1] = ' '
                  string = ''.join(string)
                  place_holder[0] = string
                  u = self.renemy.area_forest('rare')
                  u.sys_battle()
          elif movenment == 's':
              place_holder = map_layout[y]
              string = list(place_holder[0])
              if string[x-1] == '|' and x - 1== 3 and y ==6:
                  inv = GameStory(player, 'rift', renemy)
                  inv.play(10, 7)
              if string[x-1] == 'N' and x - 1== 3 and y ==3:
                  print 'What would you like %s' % self.player.name
                  shop = GameStory(player, 'alchemist', renemy)
                  shop.shop('alchemist', x, y)
                  y -= 1
              if string[x-1] == '#':
                  print '[Can\'t Move Their]'
              else:
                  y += 1
              if string[x-1] == 'E':
                  string[x-1] = ' '
                  string = ''.join(string)
                  place_holder[0] = string
                  u = self.renemy.area_forest('normal')
                  u.sys_battle()
              if string[x-1] == 'R':
                  string[x-1] = ' '
                  string = ''.join(string)
                  place_holder[0] = string
                  u = self.renemy.area_forest('rare')
                  u.sys_battle()
          elif movenment == 'd':
              place_holder = map_layout[y-1]
              string = list(place_holder[0])
              if string[x] == 'N' and x== 3 and y - 1 ==3:
                  print 'What would you like %s' % self.player.name
                  shop = GameStory(player, 'alchemist', renemy)
                  shop.shop('alchemist', x, y)
                  x -=1
              if string[x] == '#':
                  print '[Can\'t Move Their]'
              else:
                  x += 1
              if string[x-1] == 'E':
                  string[x-1] = ' '
                  string = ''.join(string)
                  place_holder[0] = string
                  u = self.renemy.area_forest('normal')
                  u.sys_battle()
              if string[x-1] == 'R':
                  string[x-1] = ' '
                  string = ''.join(string)
                  place_holder[0] = string
                  u = self.renemy.area_forest('rare')
                  u.sys_battle()
          elif movenment == 'w':
              place_holder = map_layout[y-2]
              string = list(place_holder[0])
              if string[x-1] == 'N' and x - 1 == 3 and y - 2 ==3:
                  print 'What would you like %s' % self.player.name
                  shop = GameStory(player, 'alchemist', renemy)
                  shop.shop('alchemist', x, y)
                  y += 1
              if string[x-1] == '#':
                  print '[Can\'t Move Their]'
              else:
                  y -= 1
              if string[x-1] == 'E':
                  string[x-1] = ' '
                  string = ''.join(string)
                  place_holder[0] = string
                  u = self.renemy.area_forest('normal')
                  u.sys_battle()
              if string[x-1] == 'R':
                  string[x-1] = ' '
                  string = ''.join(string)
                  place_holder[0] = string
                  u = self.renemy.area_forest('rare')
                  u.sys_battle()
          elif movenment == "options":
               print self.player.get_stats()
               raw_input("Press ENTER to go back.")
          elif movenment == "inventory":
               inv = GameStory(player, 'alchemist', renemy)
               inv.inv('alchemist', x, y)
          elif movenment == "save":
               self.player.x = x
               self.player.y = y
               save = GameStory(player, 'alchemist', renemy)
               save.save('alchemist', x, y)
               
   def rushmanov(self, x, y):
      if not self.player.first_tavern:
         print "{Text}As you enter the Tavern you are approached by an old man in a Robe"
         print "{Text}Old man 'Are you %s?'" % self.player.name
         reply = raw_input("Yes or No...>>> ")
         reply = reply.lower()
         if reply == 'yes':
             print "\n{Text}Well %s, Welcome to the Rift." % self.player.name
             print "{Text}Here's a complamentary Work bench so you can Craft Weapons."
             print "{Text}Aquired *Work bench*\n"
             self.player.work_bench = 1
             print "{Text}Well now please head to the forest outside of town,"
             print "{Text}And kill 5 slimes"
             print "{Text}Aquired Quest 'Slimes, Gotta Hate'\n"
             quest = ['Slimes; Gotta Hate','Kill 5 Slimes then head back to Professor Niru',0,6,11,'200xp. $250', 'Slime']
             self.player.quests.append(quest)
             raw_input("press ENTER to continue\n")
         else:
             print "{Text}I never liked liers..."
             print "{Text}Well %s, Welcome to the Rift." % self.player.name
             print "{Text}Here's a complamentary Work bench so you can Craft Weapons."
             print "Aquired *Work bench*\n"
             self.player.work_bench = 1
             print "{Text}Well now please head to the forest outside of town,"
             print "{Text}And kill 5 slimes"
             print "{Text}Aquired Quest 'Slimes, Gotta Hate'\n"
             quest = ['Slimes; Gotta Hate','Kill 5 Slimes then head back to Professor Niru',0,6,11,'200xp. $250', 'Slime']
             self.player.quests.append(quest)
             raw_input("press ENTER to continue\n")
         self.player.first_tavern = True
      f01 = ['#####',1]
      f02 = ['#N  #',2]
      f03 = ['### #',3]
      f04 = ['#   #',4]
      f05 = ['#   #',5]
      f06 = ['|  N#',6]
      f07 = ['#####',7]
      default = [f01,f02,f03,f04,f05,f06,f07]
      map_layout = default
      x = int(x)
      y = int(y)
      num = -1
      movenment = ''
      while True:
          while num <= len(default)-2:
              num += 1
              holder = map_layout[num]
              printable = holder[0]
              if num == y-1:
                  replacment = list(holder[0])
                  replacment[x - 1] = '*'
                  replacment = ''.join(replacment)
                  printable = replacment
              print printable
          num = -1
          movenment = raw_input('>>> ')
          if movenment == 'a':
              place_holder = map_layout[y-1]
              string = list(place_holder[0])
              if string[x-2] == '|' and x - 2== 0 and y - 1 ==5:
                  inv = GameStory(player, 'rift', renemy)
                  inv.play(14, 13)
              if string[x-2] == 'N' and x - 2== 1 and y - 1 ==1:
                  print "I'm Bob and I own the Rushmanov Beer Hall,"
                  print "Welcome %s" % self.player.name
                  x += 1
              if string[x-2] == '#':
                  print '[Can\'t Move There]'
              else:
                  x -= 1
              if string[x-1] == 'E':
                  string[x-1] = ' '
                  string = ''.join(string)
                  place_holder[0] = string
                  u = self.renemy.area_forest('normal')
                  u.sys_battle()
              if string[x-1] == 'R':
                  string[x-1] = ' '
                  string = ''.join(string)
                  place_holder[0] = string
                  u = self.renemy.area_forest('rare')
                  u.sys_battle()
          elif movenment == 's':
              place_holder = map_layout[y]
              string = list(place_holder[0])
              if string[x-1] == 'N' and x - 1== 3 and y ==5:
                  for i in self.player.quests:
                     print i[4], i[2]
                     if i[4] == 11 and i[2] >= 6:
                        print 'I see you have killed 6 slimes.'
                        print 'Congradulations, Here\'s your Reward:'
                        print '200xp'
                        self.player.xp += 200
                        self.player.level_up()
                        print '$250'
                        self.player.money += 250
                  print 'Hello again %s' % self.player.name
                  print 'I\'m Professor Niru'
                  y -= 1
              if string[x-1] == '#':
                  print '[Can\'t Move Their]'
              else:
                  y += 1
              if string[x-1] == 'E':
                  string[x-1] = ' '
                  string = ''.join(string)
                  place_holder[0] = string
                  u = self.renemy.area_forest('normal')
                  u.sys_battle()
              if string[x-1] == 'R':
                  string[x-1] = ' '
                  string = ''.join(string)
                  place_holder[0] = string
                  u = self.renemy.area_forest('rare')
                  u.sys_battle()
          elif movenment == 'd':
              place_holder = map_layout[y-1]
              string = list(place_holder[0])
              if string[x] == 'N' and x == 3 and y - 1 ==5:
                  for i in self.player.quests:
                     print i[4], i[2]
                     if i[4] == 11 and i[2] >= 6:
                        print 'I see you have killed 6 slimes.'
                        print 'Congradulations, Here\'s your Reward:'
                        print '200xp'
                        self.player.xp += 200
                        self.player.level_up()
                        print '$250'
                        self.player.money += 250
                  print 'Hello again %s' % self.player.name
                  print 'I\'m Professor Niru'
                  x -= 1
              if string[x] == '#':
                  print '[Can\'t Move Their]'
              else:
                  x += 1
              if string[x-1] == 'E':
                  string[x-1] = ' '
                  string = ''.join(string)
                  place_holder[0] = string
                  u = self.renemy.area_forest('normal')
                  u.sys_battle()
              if string[x-1] == 'R':
                  string[x-1] = ' '
                  string = ''.join(string)
                  place_holder[0] = string
                  u = self.renemy.area_forest('rare')
                  u.sys_battle()
          elif movenment == 'w':
              place_holder = map_layout[y-2]
              string = list(place_holder[0])
              if string[x-1] == '#':
                  print '[Can\'t Move Their]'
              else:
                  y -= 1
              if string[x-1] == 'E':
                  string[x-1] = ' '
                  string = ''.join(string)
                  place_holder[0] = string
                  u = self.renemy.area_forest('normal')
                  u.sys_battle()
              if string[x-1] == 'R':
                  string[x-1] = ' '
                  string = ''.join(string)
                  place_holder[0] = string
                  u = self.renemy.area_forest('rare')
                  u.sys_battle()
          elif movenment == "options":
               print self.player.get_stats()
               raw_input("Press ENTER to go back.")
          elif movenment == "inventory":
               inv = GameStory(player, 'rushmanov', renemy)
               inv.inv('rushmanov', x, y)
          elif movenment == "save":
               self.player.x = x
               self.player.y = y
               save = GameStory(player, 'rushmanov', renemy)
               save.save('rushmanov', x, y)
			
   def forest(self, x, y):
      print '{Text}You smell the scent of flowers in the air'
      print '{Text}and the wind blowing past your head...'
      f01 = ['################',1]
      f02 = ['#              #',2]
      f03 = ['#  # E     #   #',3]
      f04 = ['# ###          #',4]
      f05 = ['#  #   R    E  #',5]
      f06 = ['#    #         #',6]
      f07 = ['#   ###   #    #',7]
      f08 = ['#    #         #',8]
      f09 = ['#  E #  E      #',9]
      f10 = ['#   ###     #  #',10]
      f11 = ['#  #####       |',11]
      f12 = ['#   ###   E    #',12]
      f13 = ['#    #       # #',13]
      f14 = ['#        #  ####',14]
      f15 = ['#   E        # #',15]
      f16 = ['################',16]
      default = [f01,f02,f03,f04,f05,f06,f07,f08,f09,f10,f11,f12,f13,f14,f15,f16]
      map_layout = default
      x = int(x)
      y = int(y)
      num = -1
      movenment = ''
      while True:
          while num <= 14:
              num += 1
              holder = map_layout[num]
              printable = holder[0]
              if num == y-1:
                  replacment = list(holder[0])
                  replacment[x - 1] = '*'
                  replacment = ''.join(replacment)
                  printable = replacment
              print printable
          num = -1
          movenment = raw_input('>>> ')
          if movenment == 'a':
              place_holder = map_layout[y-1]
              string = list(place_holder[0])
              if string[x-2] == '#':
                  print '[Can\'t Move Their]'
              elif string[x-2] == '|':
                  inv = GameStory(player, 'rift', renemy)
                  inv.play(2, 6)
              else:
                  x -= 1
              if string[x-1] == 'E':
                  string[x-1] = ' '
                  string = ''.join(string)
                  place_holder[0] = string
                  u = self.renemy.area_forest('normal')
                  u.sys_battle()
              if string[x-1] == 'R':
                  string[x-1] = ' '
                  string = ''.join(string)
                  place_holder[0] = string
                  u = self.renemy.area_forest('rare')
                  u.sys_battle()
          elif movenment == 's':
              place_holder = map_layout[y]
              string = list(place_holder[0])
              if string[x-1] == '#':
                  print '[Can\'t Move Their]'
              elif string[x-1] == '|':
                  inv = GameStory(player, 'rift', renemy)
                  inv.play(2, 6)
              else:
                  y += 1
              if string[x-1] == 'E':
                  string[x-1] = ' '
                  string = ''.join(string)
                  place_holder[0] = string
                  u = self.renemy.area_forest('normal')
                  u.sys_battle()
              if string[x-1] == 'R':
                  string[x-1] = ' '
                  string = ''.join(string)
                  place_holder[0] = string
                  u = self.renemy.area_forest('rare')
                  u.sys_battle()
          elif movenment == 'd':
              place_holder = map_layout[y-1]
              string = list(place_holder[0])
              if string[x] == '#':
                  print '[Can\'t Move Their]'
              elif string[x] == '|':
                  inv = GameStory(player, 'rift', renemy)
                  inv.play(2, 6)
              else:
                  x += 1
              if string[x-1] == 'E':
                  string[x-1] = ' '
                  string = ''.join(string)
                  place_holder[0] = string
                  u = self.renemy.area_forest('normal')
                  u.sys_battle()
              if string[x-1] == 'R':
                  string[x-1] = ' '
                  string = ''.join(string)
                  place_holder[0] = string
                  u = self.renemy.area_forest('rare')
                  u.sys_battle()
          elif movenment == 'w':
              place_holder = map_layout[y-2]
              string = list(place_holder[0])
              if string[x-1] == '#':
                  print '[Can\'t Move Their]'
              elif string[x-1] == '|':
                  inv = GameStory(player, 'rift', renemy)
                  inv.play(2, 6)
              else:
                  y -= 1
              if string[x-1] == 'E':
                  string[x-1] = ' '
                  string = ''.join(string)
                  place_holder[0] = string
                  u = self.renemy.area_forest('normal')
                  u.sys_battle()
              if string[x-1] == 'R':
                  string[x-1] = ' '
                  string = ''.join(string)
                  place_holder[0] = string
                  u = self.renemy.area_forest('rare')
                  u.sys_battle()
          elif movenment == "options":
               print self.player.get_stats()
               raw_input("Press ENTER to go back.")
          elif movenment == "inventory":
               inv = GameStory(player, 'forest', renemy)
               inv.inv('forest', x, y)
          elif movenment == "save":
               self.player.x = x
               self.player.y = y
               save = GameStory(player, 'forest', renemy)
               save.save('forest', x, y)


#==================================================================
#= Game ============================================================
#==================================================================
class GameArcade(object):
   
   def __init__(self, player, renemy):
      self.player = player
      self.renemy = renemy
      self.arcade_intro = False

   def arcade(self):
      # Plays the Arcade intro if this is the first time starting.
      if not self.arcade_intro:
         print "\nWelcome to Arcade Mode."
         print "Arcade mode is what you would call a Training System."
         print "Come here whenever you want or need to lvl."
         print "After each battle you can type 'options' to display your current stats."
         print "After each battle you can type 'inventory' to display your inventory."
         raw_input("Press ENTER to continue.")
         # Changes intro_done so it plays through only this one time.
         self.arcade_intro = True
      round_num = 0
      arcade_mode = True
      while arcade_mode:
         round_num += 1
         print "ROUND %s......... FIGHT!!!!" % round_num
         u = self.renemy.mob()
         u.sys_battle()
         print "Press Enter to Find a NEW opponent or type 'leave'to go back to your adventure"
         ch = raw_input(">>> ")
         ch = ch.lower()
         if ch == 'leave':
            arcade_mode = False
         if ch == 'options':
            print self.player.get_stats()
            raw_input("Press ENTER to go back")
         if ch == 'inventory':
            inventory = True
            while inventory:
               print "[Pots]"
               print "[Items]"
               print "[Equipment]"
               game_inv = raw_input(">>> ")
               game_inv = game_inv.lower()
               if game_inv == 'items':
                  items = True
                  while items:
                     print "Scrap Metal: %s" % self.player.junk_metal
                     if self.player.ocean_gem > 0:
                        print "Ocean Gem: %s" % self.player.ocean_gem
                     if self.player.silver_horn > 0:
                        print "Silver Horn: Aquired"
                     print "Type 'Descripton' to find out what items do....."
                     select = raw_input("Type what item you want to 'Use' or hit Enter to leave: ")
                     select = select.lower()
                     if select  == 'description':
                        print "Scrap Metal: Used to sell for money or crafting (Future Update)"
                        if self.player.ocean_gem > 0:
                           print "Ocean Gem: A magical gem but is unknown what it does."
                        if self.player.silver_horn > 0:
                           print "Silver Horn: A Mythical horn known to open a hall of riches."
                        raw_input("Press ENTER to continue")
                     elif select == 'silver horn':
                        print 'You blow through the horn and it\'s sound echos through the mountains.'
                        raw_input("Press ENTER to continue")
                     elif select == 'ocean gem':
                        print 'The gem shines in the sunlight'
                        raw_input("Press ENTER to continue")
                     elif select == 'junk metal':
                        print "(Place Holder) Will be used for future crafting"
                        raw_input("Press ENTER to continue")
                     else:
                        items = False
               if game_inv == 'pots':
                  pots = True
                  while pots:
                     print "Lessar Potion: %s" % self.player.lessar_potion
                     print "Potion: %s" % self.player.potion
                     print "Greater Potion: %s" % self.player.greater_potion
                     print "Type 'Descripton' to find out what items do....."
                     select = raw_input("Type what item you want to 'Use' or hit Enter to leave: ")
                     select = select.lower()
                     if select  == 'description':
                        print "Lessar Potion: Heals 100 HP"
                        print "Potion: Heals 200 HP"
                        print "Greater Potion: Heals 300 HP"
                     elif select == 'lessar potion':
                        if self.player.lessar_potion <= 0:
                           print "You do not have any Lessar Potions left"
                        elif self.player.lessar_potion > 0:
                           print "You use a potion"
                           self.player.hp += 100
                           self.player.lessar_potion -= 1
                           print "You heal 100 hp"
                           if self.player.hp > self.player.max_hp:
                              self.player.hp = self.player.max_hp
                           print "You now have: %s / %s" % (self.player.hp, self.player.max_hp)
                     elif select == 'potion':
                        if self.player.potion <= 0:
                           print "You do not have any Potions left"
                        elif self.player.potion > 0:
                           print "You use a potion"
                           self.player.hp += 200
                           self.player.potion -= 1
                           print "You heal 200 hp"
                           if self.player.hp > self.player.max_hp:
                              self.player.hp = self.player.max_hp
                           print "You now have: %s / %s" % (self.player.hp, self.player.max_hp)
                     elif select == 'greater potion':
                        if self.player.greater_potion <= 0:
                           print "You do not have any Greater Potions left"
                        elif self.player.greater_potion > 0:
                           print "You use a potion"
                           self.player.hp += 300
                           self.player.greater_potion -= 1
                           print "You heal 300 hp"
                           if self.player.hp > self.player.max_hp:
                              self.player.hp = self.player.max_hp
                           print "You now have: %s / %s" % (self.player.hp, self.player.max_hp)
                     else:
                        pots = False

#==================================================================
#= Credits =========================================================
#==================================================================
class Credits(object):
   def __init__(self):
      self.credits = '1'

   def cred(self):
      print "YOU LOSE"
      raw_input("Hit ENTER to see the Credits")
      print "CREDITS"
      time.sleep(1.0)
      print "Project Manager: "
      time.sleep(1.0)
      print "\t*Ryan Lawton"
      print ""
      time.sleep(1.0)
      print "Lead Programmer: "
      time.sleep(1.0)
      print "\t*Ryan Lawton"
      print ""
      time.sleep(1.0)
      print "Lead Art Designer: "
      time.sleep(1.0)
      print "\t* Ryan Lawton"
      print ""
      time.sleep(1.0)
      print "Story Board Designer: "
      time.sleep(1.0)
      print "\t* Ryan Lawton"
      print ""
      time.sleep(1.0)
      print "Music and Sounds: "
      time.sleep(1.0)
      print "\t* Ryan Lawton"
      print ""
      time.sleep(1.0)
      print "Producer: "
      time.sleep(1.0)
      print '\t* Ryan Lawton'
      time.sleep(1.0)
      print ""
      time.sleep(1.0)
      print ""
      time.sleep(1.0)
      print ""
      time.sleep(1.0)
      print ""
      time.sleep(1.0)
      print ""
      time.sleep(1.0)
      print ""
      time.sleep(1.0)
      print ""
      time.sleep(1.0)
      print ""
      print 'THE END'
      while True:
          raw_input()
                     
         
# Setting up the game.
rmp = True
while rmp:
   print "Welcome To Battle's By Ryan L."
   print ("[Story Mode]")
   print ("[Arcade]")
   run = raw_input(">>> ")
   run = run.lower()
   if run == 'story mode':
      print '[New Game]'
      print '[Load Game]'
      g = raw_input('>>> ')
      g = g.lower()
      if g == 'new game':
         x = raw_input("\n-\nWhat is your name, traveler? ")
         player = Player(x)
         if x == "Cheat Mode":
            fun = True
            while fun:
               print """
Welcome to Cheat mode!!!
Here you  can access many cheats available!
[Change Log]
         """
               cheat = raw_input("Cheat>>> ")
               cheat = cheat.lower()
               if cheat == 'weapon ultimo':
                  print "You aquire the ultimate weapon of destruction,"
                  print "Access it in your inventory."

               elif cheat == 'change log':
                  print """

Version 1.0.0 - 8th August 2012:
\t* Basic game code layout made based off first Py Game.

Version 1.0.1 - 9th August 2012:
\t* First Inventory system placed in-game and mob gen coded in.

Version 1.0.2 - 10th August 2012:
\t* Changed mob gen code to implement a variety of enemies an bosses.

Version 1.0.3 - 11th August 2012:
\t* Added Potions (Worn't Working) to the game.
\t* Added Fear Ability.

Version 1.1.0 - 12th August 2012:
\t* Changed Inventory System completly to allow functionality of
\tPotions.
\t* Mobs level up with you to allow higher ends of challenge.

Version 1.1.1 - 13th August 2012:
\t* Took out code for Defence and Dodge abilities even though visible
\tchoices not there.
\t* Bosses now level with you but the Boss at area 4 will always be
\tlvl 5 until you hit that level to allow a block for progression.
\t* Added cheat menu to view Change Log In-Game + Small Challenges.
\t* Added access to inventory mid Battle.
\t* Fixed Lower or Upper Case Specific Commands to Accept Anything.

Version 1.1.2 - 14th August 2012:
\t* Added Money system.
\t* Added Shop system to sell your junk and buy extra pots.
\t* Added Junk Metal used for shop system(AND PLACEHOLDER FOR CRAFTING MATS).
\t* Added area 5 as access to shop.

Version 1.1.3 - 15th August 2012:
\t* Need Silver Horn to access the Shop.
\t* Shortened Mob Code for the Randemizer.
\t* Took out old Inventory System that wasn't doing anything.
\t* Added new death sentences.
\t* Added Credits when you die.

Version 1.1.4 - 16th August 2012:
\t* Added new mobs
\t* Fixed Enemy Lvl's to max 4 for areas 1-3.
\t* Fixed boss fight lvling.
\t* Fixed some minor code.
\t* Added Arcade Mode SEPERATE from the story line.
\t* Increased xp to lvl.
\t* Improved inventory to reduce coding.
\t* Added Item descriptions in Inventory.
\t* Added a place holder for Companions.
\t* Added the next stage of the story line, the Rift.
\t* Mages now do more damage not as much as the archer but also has a new ability.

Version 1.1.5 - 17th August 2012:
\t* Added in-battle potion debuff timer.
\t* Increased pot healing effects.
\t* Increased price for pots.
\t* Improved shop system.
\t* Improved inventory system ready for new systems (Equipment and Crafting).
\t* Changed Mr Anderson to a new mob name.
\t* Added escape feature during battle.
\t* Added support for Weaponry.
\t* New attack messages based on classes.

Version 1.2.0 - 19th August 2012:
\t* Added NEW ABILITIES for Warrior and Mage (Archer In Progress).
\t* Added Mana System to cast abilities.
\t* Required specific lvl's to cast the new abilities.
\t* Added new text for Mage's version of bleed, burn.
\t* Added Archers new abilities.
\t* Fixed some loop holes.
\t* Increased starter health.
\t* Added 3 Tiers of mana potions.
\t* Changed the spelling of lessar to lesser.
\t* Added Mana Cost next to abilities.
\t* Increased Mob HP.
\t* Increased Required lvl before higher tier pots drop from mobs.
\t* Added 5 Lesser Potions when you start a new game.

Version 1.2.1 - 23rd August 2012:
\t* Added Credits module to reduce code length.
\t* Added XP in Options Menu.
\t* Added MP in Options Menu.
\t* Added XP Reward Message after each battle.
\t* Took out bonus games.

Version 2.0.0 - 28th August 2012:
\t* Changed the Layout of initial starting screen.
\t* Added a Save function when playing and can be loaded at anytime.
\t* Fixed Rift Ignore Error.
\t* Added Secret Testing Weapon to 1 hit any mob(For testing Purposes).
\t* Added 3 Save Slots in Total.
\t* Fixed Saving and or Loading ERRORS.

Version 2.0.1 - 5th September 2012:
\t* Added new Mats in (Gold, Wood, Iron etc.)
\t* Added new weapons.
\t* Added Plans to make weapons.
\t* Added damage level of weapons in Equipment.
\t* Updated Save function for new Items.
\t* Updated the RIFT for more Story line.
\t* Added crafting system requireing a Work bench.
\t* Added ability to buy mats for new weps.
\t* Updated look of Shop.

Version 2.0.2 - 9th September 2012:
\t* Revamped Weapon system to Add over 200 new weapons to the game.
\t* Weapons are dropped from enmies with a chance of them being rare or even legendary.
\t* Fixed Saving\\Loading System to Accompany the Numerous new Weapons.
\t* Changed XP system to make it more of a FARM.
\t* New Equipment Section in the Selling part of the shop to sell weapons.
\t* Fixed Weapon Name problem if weapon is already in bag.

Version 2.0.3 - 8th October 2012:
\t* Changed Weapon Naming System.
\t* Added Weapon Stats (Strength, Dexterity, Intelligence, Vitality and Drop Chance).
\t* Save System chnaged for new weapon system (Old saves will not be usable).
\t* Chnaged Drop Chances.
\t* Added new Rare enemy mobs that give higher drop chance for better weapons but are alot tougher to defeat.
\t* Bosses now get buffs.
\t* Added number beside names for easier Usage.
            """

               else:
                  print "Invalid Option (restart game to play normaly)"
               
         renemy = Renemy(player)
         print "{Text}Please Type in Your Selected Class"
         print "{Class}Warrior"
         print "{Class}Mage"
         print "{Class}Archer"
         print "{Text}More Info"
         classes = raw_input(">>> ")
         classes = classes.lower()
         if classes == "more info":
            print "{Text}Warrior's have higher defence so they take less damage."
            print "{Text}Mage's are scary and when fear their opponent, there defence is weakened even further."
            print "{Text}Archer's are deadly and deal more damage to their foes."
            raw_input("Press ENTER to go back")
            print "{Text}Please Type in Your Selected Class"
            print "{Class}Warrior"
            print "{Class}Mage"
            print "{Class}Archer"
            classes = raw_input(">>> ")
         game = GameStory(player, "area_one", renemy)
         arcade = GameArcade(player, renemy)
         game.play(4, 5)
      elif g == 'load game':
         print "[Save 1]"
         print "[Save 2]"
         print "[Save 3]"
         data = raw_input(">>> ")
         data = data.lower()
         if data == 'save 1':
            try:
               save = open('save1.txt', 'r')
               s = []
               sav = 'save1'

            except:
               print "Invalid Save File"

         elif data == 'save 2':
            try:
               save = open('save2.txt', 'r')
               s = []
               sav = 'save2'

            except:
               print "Invalid Save File"

         elif data == 'save 3':
            try:
               save = open('save3.txt', 'r')
               s = []
               sav = 'save3'
               
            except:
               print "Invalid Save File"
               
         try:
            for line in save:
               line = line.strip()
               s.append(line)
            classes = s[20]
            name = s[5]
            room = s[6]
            save.close()
            player = Player(name)
            renemy = Renemy(player)
            game = GameStory(player, room, renemy)
            game.load(room, sav)
         except:
            print "Error Opening '%s'" % data
         game.play(s[41],s[42])
         
   elif run == 'arcade':
      arcade = GameArcade(player, renemy)
      arcade.arcade()
