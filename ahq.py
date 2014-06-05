#AHQ Helper - Henchman
#Current Features:

#Dice Roller
#Treasure Chest Generator (no contents)
#Character generator


import random
import csv

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
                        table_sub[key] = e
                num += 1
            table_output[row[0]] = table_sub #assigns sub table to main table
    t.close()
    return table_output


##def roll_corridor():
##    section = d(1,12)
##    floor_feature = d(2,12)
##    ends = d(2,12)
##    special = d(2,12)
##    monster = d(1,12)
##    print('Section:',section)
##    print('Floor Feature:', floor_feature)
##    print('Ends in:', ends)
##    print('Special:', special)
##    print('Monster:', monster)
##    print('\n\n')
##
##
##def roll_room():
##    rooms = int(input('rooms so far'))    
##    room_type = d(1,12)+rooms
##    furnishings1 = d(2,12)
##    furnishings2 = d(2,12)
##    hazard = d(1,24)
##    doors = d(1,12)
##    print('Doors:',doors)
##    print('Type:', room_type)
##    print('furnishings 1:',furnishings1)
##    print('furnishings 2:',furnishings2)
##    print('Hazard:',hazard)
##    print('Monsters:', d(1,12))
##    print('\n\n')

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
            chest[table] = table_treasure[table][roll]
    return chest
        
class Character(object):
    """An AHQ Character"""


    def __init__(self, name="Unknown"):
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
                      
        self.ws = max(d(1,6),d(1,6))+table_races[self.race]['ws']
        self.bs = max(d(1,6),d(1,6))+table_races[self.race]['bs']
        self.st = max(d(1,4),d(1,4))+table_races[self.race]['st']
        self.to = max(d(1,4),d(1,4))+table_races[self.race]['to']
        self.sp = max(d(1,6),d(1,6))+table_races[self.race]['sp']
        self.br = max(d(1,8),d(1,8))+table_races[self.race]['br']
        self.iq = max(d(1,8),d(1,8))+table_races[self.race]['iq']
        self.wo = max(d(1,4),d(1,4))+table_races[self.race]['wo']
        self.fp = table_races[self.race]['fp']
        self.tr = table_races[self.race]['tr'] #This needs ammending to work as  alist

    def __str__(self):
        return self.name+", "+self.race+" "+self.aclass
    


    def assign_class(self):
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
       
#AHQ Helper - Henchman
        

#Dungeon settings
dungeon_level = 1
rooms = 0
module = "Standard"


#Tables
table_treasure      = import_table('Modules/'+module+'/treasure.csv')
table_races         = import_table('Modules/'+module+'/races.csv')
table_corridors     = import_table('Modules/'+module+'/corridors.csv')
table_specialdoors  = import_table('Modules/'+module+'/specialdoors.csv')
table_rooms         = import_table('Modules/'+module+'/rooms.csv')
table_classes       = import_table('Modules/'+module+'/classes.csv')


#main

print(roll_treasure(25))

