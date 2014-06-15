#AHQ Helper - Henchman
#Current Features:

#Dice Roller
#Treasure Chest Generator (no contents)
#Character generator
#(Primitive) Corridor Generator
#(Primitive) Room generator

import random
import csv

#Enabling - consider moving to module

def d(number, sides, modifier = 0):
    result = modifier
    for d in range(number):
        result += random.randint(1, sides)
    return result

def import_table(filename):
    '''Imports a csv table to dictionary items
       Resulting table will consist of dicts with
       key:key:value = Table Name : Sub Table : Results '''
    table_output = {} 
    with open(filename, 'r') as t:
        table_import = csv.reader(t)
        headings = next(table_import)
        
        for row in table_import:
            table_sub = {}
            num = 1
              
            for e in row[1:]: #Constructs a sub table
                try:
                    key = int(headings[num])
                except:
                    key = headings[num]
                
                if e == '':
                    table_sub[key] = None
                else:
                    try:
                        table_sub[key] = int(e)
                    except:
                        try:
                            table_sub[key] = float(e)
                        except:
                            table_sub[key] = e
                num += 1
                
            table_output[row[0]] = table_sub #assigns sub table to main table
    t.close()
    return table_output


#Rooms/Exploration

class Door(object):
    '''Door - defaults to roomdoor = False Special = False'''

    def __init__(self, roomdoor = False, special = False, opened = False):
        self.toroom = True
        self.opened = opened
        self.special = special
        self.special_feature = []
        self.roomdoor = roomdoor        

        if random.randint(1,2) == 1 and self.roomdoor == True:
            self.toroom = False
            
        if special:
            self.feature = table_specialdoors["Special Doors"][d(1,12)]
            self.special_feature.append(self.feature)
            
            #Enhanced doors have 2 features
            if self.feature == "Enhanced": 
                self.feature1 = table_specialdoors["Special Doors"][d(1,12)]
                self.feature2 = table_specialdoors["Special Doors"][d(1,12)]
                
                #2nd roll of enhanced creates a dimension door
                if self.feature1 == "Enhanced" or self.feature2 == "Enhanced":
                    self.feature1 = "Dimension Door"
                    self.feature2 = table_specialdoors["Dimension Doors"][d(1,12)]
                
                self.special_feature.append(self.feature1)
                self.special_feature.append(self.feature2)

        
    def __str__(self):
        if self.opened:
            special = " "
            if len(self.special_feature) != 0:
                special += self.special_feature[0]                
                try:
                    for x in self.special_feature[1:]:
                        special += ", "
                        special += x
                        
                except:
                    special += " "

                special += " "
            
            return "An open"+special+ "door"

        elif "Double" in self.special_feature:
            return "A closed double door"
        else:
            return "A closed door"
        


class Section(object):
    def __init__self():
        print("Hi!")
    

class Room(Section):

    total = 0
    
    def __init__(self):

        Room.total += 1
        
        roll = d(1,12)+Room.total
        if roll > 24:
            roll = 24
            
        self.size = table_rooms["Size"][roll]
        self.furniture = [] 
        self.features = []
        self.questroom = table_rooms["Quest"][roll] == True
        self.doors = table_rooms["# Doors"][d(1,12)]
        
        feature_number = table_rooms["# Features"][roll]
        furniture_number = table_rooms["# Furniture"][roll]

        # Creates Furniture
        while furniture_number > 0:            
            furniture_roll = table_rooms["Furniture"][d(2,12)]
            if furniture_roll == "Roll Twice":
                furniture_number += 2
            else:
                self.furniture.append(furniture_roll)
                furniture_number -= 1

        # Creates features/hazards
        for h in range(feature_number):
            self.features.append(table_rooms["Features"][d(1,24)])

        #Creates monsters. 
        monstertype = table_rooms["Monsters"][roll]

        try:
            monsterroll = d(1,12)+counters_monster
            if monsterroll > 12:
                monsterroll = 12
            self.monsters = (table_monsters[monstertype][monsterroll]) * playerlevel
        except:
            self.monsters = 0    
                                
    def __str__(self):

        description  = "Size: "+self.size+"\n"
        description += "Doors: "+str(self.doors)+"\n" 
        description += "Features: "+", ".join(self.features)+"\n"
        description += "Furniture: "+", ".join(self.furniture)+"\n"
        description += "Monsters: "+str(self.monsters)+"\n"
        description += "Quest: "+str(self.questroom)+"\n"

        return description


def roll_corridor():
    roll = d(2,12)
    
    section = table_corridors["Sections"][d(1,12)]
    ends = table_corridors["End"][d(2,12)]
    doors = table_corridors["Doors"][roll]
    special = table_corridors["Special Feature"][roll]
    trap = table_corridors["Trap"][roll]
    specialdoor = table_corridors["Special Doors"][roll]
    monster = table_corridors["Monster"][roll]
    print('Sections:',section)
    print('Ends in:', ends)
    print('Doors:', doors)
    print('Special Doors:', specialdoor)
    print('Special:', special)
    print('Monster:', monster)




def roll_treasure(monsters, level=1):
    chest = {}
    for table in table_treasure.keys():
        roll = d(1,12,level-1 + int(monsters/25))
        if roll > 15:
            roll = 15

        #Gold can either be another role or a fixed number
        #If it requires an additional roll, the value will be of type str
        #This string will be in the format '1,12,10' meaning 1d12*10
        if table == 'Gold' and isinstance(table_treasure[table][roll],str):
            dice = [int(d) for d in table_treasure[table][roll].split(',')]
            chest[table] = d(dice[0],dice[1])*dice[2]           
        else:
            #Ammendments Needed:
            #Add ability to roll on sub tables
            #Try: roll for range(table)
            #Except: as below
            chest[table] = table_treasure[table][roll]
    return chest
        
class Character(object):
    """An AHQ Character"""


    def __init__(self, name="Unknown"):
        #Ammendments needed:
        #Add race and class as potential inputs with defaults to unknown
        #Remove all input needed in the text
        
        self.name = name
        self.aclass = "Unknown"
        self.stats = {}
        
        created = False
        while not created:
            self.race = input("What race is this character?\n")
            if self.race in table_races.keys():
                created = True
            else:
                print("That is not an option.")
                print("Select from:")
                print(table_races.keys())

        #Ammendments Needed
        #This should be convereted to a dict called stats
                
        self.ws = max(d(1,6),d(1,6))+table_races[self.race]['ws']
        self.bs = max(d(1,6),d(1,6))+table_races[self.race]['bs']
        self.st = max(d(1,4),d(1,4))+table_races[self.race]['st']
        self.to = max(d(1,4),d(1,4))+table_races[self.race]['to']
        self.sp = max(d(1,6),d(1,6))+table_races[self.race]['sp']
        self.br = max(d(1,8),d(1,8))+table_races[self.race]['br']
        self.iq = max(d(1,8),d(1,8))+table_races[self.race]['iq']
        self.wo = max(d(1,4),d(1,4))+table_races[self.race]['wo']
        self.fp = table_races[self.race]['fp']
        self.tr = table_races[self.race]['tr'] #This needs ammending to work as a list

    def __str__(self):
        return self.name+", "+self.race+" "+self.aclass
    


    def assign_class(self):
        #Ammendments needed:
        #Remove need for input
        #Make it allow a class to be input as a variable
        #Separate out the part asking for class and assigning class effect
        assigned = False
        while not assigned:
            self.aclass = input("What class is this character?\n")
            if self.aclass in table_classes.keys():
                assigned = True
                self.ws += table_classes[self.aclass]['ws']
                self.bs += table_classes[self.aclass]['bs']
                self.st += table_classes[self.aclass]['st']
                self.to += table_classes[self.aclass]['to']
                self.sp += table_classes[self.aclass]['sp']
                self.br += table_classes[self.aclass]['br']
                self.iq += table_classes[self.aclass]['iq']
                self.wo += table_classes[self.aclass]['wo']
                self.fp += table_classes[self.aclass]['fp']
                self.tr += table_classes[self.aclass]['tr'] #this needs ammending to work as a list
                
            else:
                print("That is not an option.")
                print("Select from:")
                print(table_classes.keys())
                    
    def print_character(self):
        print("Name:",self.name)
        print("Race:",self.race)
        print('  WS:',self.ws)
        print('  BS:',self.bs)
        print('  ST:',self.st)
        print('  TO:',self.to)
        print('  SP:',self.sp)
        print('  BR:',self.br)
        print('  IQ:',self.iq)
        print('  WO:',self.wo)
        print('  FP:',self.fp)
        print('  TR:',self.tr) #This needs ammending to work as  alist

    def list_character(self):
        return [self.name, self.race, self.ws, self.bs, self.st, self.to,
                self.sp, self.br, self.iq, self.wo, self.fp, self.tr]
                
    
       
#AHQ Helper - Henchman
        

#Dungeon settings
dungeon_level = 1
rooms = 0
playerlevel = 0
module = "Standard"

#Counter pool
counters_monster = 0
counters_ambush  = 0
counters_trap    = 0
counters_fate    = 0



#Tables
table_treasure      = import_table('Modules/'+module+'/treasure.csv')
table_races         = import_table('Modules/'+module+'/races.csv')
table_corridors     = import_table('Modules/'+module+'/corridors.csv')
table_specialdoors  = import_table('Modules/'+module+'/specialdoors.csv')
table_rooms         = import_table('Modules/'+module+'/rooms.csv')
table_classes       = import_table('Modules/'+module+'/classes.csv')
table_monsters      = import_table('Modules/'+module+'/monsters.csv')

#main




while True:
    print("\n\nDungeon Level:", dungeon_level)
    print("Rooms:", rooms)
    print("Player Level:", playerlevel)
    option = input("\n[R]oom, [C]orridor, [T]reasure, [D]ungeon\n")
    if option == "r":
        print(Room())
        rooms += 1
    elif option == "c":
        print(roll_corridor())
    elif option == "t":
        monsters = int(input("Monsters:"))
        print(roll_treasure(monsters, dungeon_level))
    elif option == "d":
        dungeon_level = int(input("Dungeon Level"))
        rooms = int(input("Rooms"))
        playerlevel = int(input("Player Level"))
    else:
        print("Not an option (r, c, t, d)\n")






    


    
    


