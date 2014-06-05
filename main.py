#AHQ Helper - Henchman
#Current Features:

import ahq


#Dungeon settings
dungeon_level = 1
rooms = 0
module = "Standard"

table_treasure = ahq.import_table('Modules/'+module+'/treasure.csv')
table_race = ahq.import_table('Modules/'+module+'/races.csv')
table_corridor = ahq.import_table('Modules/'+module+'/corridors.csv')
table_specialdoors = ahq.import_table('Modules/'+module+'/specialdoors.csv')
table_doors = ahq.import_table('Modules/'+module+'/rooms.csv')
table_classes = ahq.import_table('Modules/'+module+'/classes.csv')

garth = ahq.Character()
garth.roll_character()
garth.print_character()
garth.assign_class()
garth.print_character()  
                               




    




                

        
