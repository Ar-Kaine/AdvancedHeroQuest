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
        

def roll_character(race):
    '''Rolls a character. Race should be full subject from table_race'''
    character = {}
    character['ws'] = max(d(1,6),d(1,6))+race['ws']
    character['bs'] = max(d(1,6),d(1,6))+race['bs']
    character['st'] = max(d(1,4),d(1,4))+race['st']
    character['to'] = max(d(1,4),d(1,4))+race['to']
    character['sp'] = max(d(1,6),d(1,6))+race['sp']
    character['br'] = max(d(1,8),d(1,8))+race['br']
    character['iq'] = max(d(1,8),d(1,8))+race['iq']
    character['wo'] = max(d(1,4),d(1,4))+race['wo']
    character['fp'] = race['fp']
    character['tr'] = race['tr']

    return character

def roll_room(count):
    


