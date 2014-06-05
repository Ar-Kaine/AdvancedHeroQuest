import ahq

table_race = ahq.import_table("Modules/Standard/races.csv")
table_class = ahq.import_table("Modules/Standard/classes.csv")

class Character(object):
    """An AHQ Character"""


    def __init__(self):
        self.name = "Unknown"
        self.aclass = "Unknown"
        self.stats = {}
        
        created = False
        while not created:
            self.race = input("What race is this character?\n")
            if self.race in table_race.keys():
                created = True
            else:
                print("That is not an option.")
                print("Select from:")
                print(table_race.keys())
                      
    def roll_character(self):
        '''Rolls a character. Race should be full subject from table_race'''
        
        self.ws = max(d(1,6),d(1,6))+self.race['ws']
        self.bs = max(d(1,6),d(1,6))+self.race['bs']
        self.st = max(d(1,4),d(1,4))+self.race['st']
        self.to = max(d(1,4),d(1,4))+self.race['to']
        self.sp = max(d(1,6),d(1,6))+self.race['sp']
        self.br = max(d(1,8),d(1,8))+self.race['br']
        self.iq = max(d(1,8),d(1,8))+self.race['iq']
        self.wo = max(d(1,4),d(1,4))+self.race['wo']
        self.fp = self.race['fp']
        self.tr = self.race['tr'] #This needs ammending to work as  alist


    def assign_class(self):
        assigned = False
        while not assigned:
            self.aclass = input("What class is this character?\n")
            if self.aclass in table_class.keys():
                assigned = True
                self.ws += table_class[aclass]['ws']
                self.bs += table_class[aclass]['bs']
                self.st += table_class[aclass]['st']
                self.to += table_class[aclass]['to']
                self.sp += table_class[aclass]['sp']
                self.br += table_class[aclass]['br']
                self.iq += table_class[aclass]['iq']
                self.wo += table_class[aclass]['wo']
                self.fp += table_class[aclass]['fp']
                self.tr += table_class[aclass]['tr'] #this needs ammending to work as a list
                
            else:
                print("That is not an option.")
                print("Select from:")
                print(table_class.keys())
                    
                    

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
        self.fp += table_class[aclass]['fp']
        self.tr += table_class[aclass]['tr']



garth = Character()
garth.roll_character()
garth.print_character()
garth.assign_class()
garth.print_character()
