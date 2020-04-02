

init -999 python:



    class Item(object):
        def __init__(self, objname, type, name, imgname, cost, consumable, description):
            self.objname = objname
            self.type = type
            self.name = name
            self.fullimg = "Database/Items/{}_full.png".format(imgname)
            self.oosimg = "None"
            
            if renpy.loadable("Database/Items/{}_oos.png".format(imgname)):
                self.oosimg = "Database/Items/{}_oos.png".format(imgname)
            self.cost = int(cost)
            self.consumable = consumable
            self.description = description           







    class Equipment(object):
        def __init__(self, objname, type, name, spriteimg, itemimg, cost, atk, pdef, mdef, skill, description):
            self.objname = objname
            self.type = type
            self.name = name
            self.spriteimg = spriteimg
            self.fullimg = "Database/{}/{}_full.png".format(type,itemimg)
            self.oosimg = "None"
            
            if renpy.loadable("Database/{}/{}_oos.png".format(type,itemimg)):
                self.oosimg = "Database/{}/{}_oos.png".format(type,itemimg)
            self.cost = int(cost)
            self.atk = int(atk)
            self.pdef = int(pdef)
            self.mdef = int(mdef)
            self.skill = "None"
            if skill != "None":
                self.skill = globals()[skill]
            self.description = description







    class Recipe(object):
        def __init__(self, objname, type, name, imgname, cost, description, output, category, *components):
            self.objname = objname
            self.type = type
            self.name = name
            self.fullimg = "Database/Items/{}_full.png".format(imgname)
            self.oosimg = "None"
            
            if renpy.loadable("Database/Items/{}_oos.png".format(imgname)):
                self.oosimg = "Database/Items/{}_oos.png".format(imgname)
            self.cost = int(cost)
            self.description = description
            self.output = globals()[output]
            self.category = category
            self.components = []
            for i in range(0,len(components)):
                self.components.append([globals()[components[i].split(",")[0]], int(components[i].split(",")[1])])



    class TroopEquip(object):
        def __init__(self, objname, name, imgname, type, consumable, combat, defense, raid, diplomacy, siege, magic, tagadd, tagsub, description):
            self.objname = objname
            self.name = name
            self.img = "Database/Troops/Equips/{}.png".format(imgname)
            self.type = type
            self.consumable = consumable
            self.combat = int(combat)
            self.defense = int(defense)
            self.raid = int(raid)
            self.diplomacy = int(diplomacy)
            self.siege = int(siege)
            self.magic = int(magic)
            
            self.tagadd = []
            for i in range(0,len(tagadd.split(","))):
                if tagadd.split(",")[i].strip() == "":
                    break
                self.tagadd.append(tagadd.split(",")[i].strip())
            
            self.tagsub = []
            for i in range(0,len(tagsub.split(","))):
                if tagsub.split(",")[i].strip() == "":
                    break
                self.tagsub.append(tagsub.split(",")[i].strip())
            
            self.description = description






    def startitems(filename):
        with renpy.file(filename) as itemslist:
            for line in itemslist:
                line = line.decode("utf-8")
                data = line.rstrip().split("\t")
                if data == "" or data[0][0] == "#": continue
                try: 
                    globals()[data[0]]
                except KeyError: 
                    globals()[data[0]] = Item(*data)
                else: 
                    globals()[data[0]].type = data[1]
                    globals()[data[0]].name = data[2]
                    globals()[data[0]].fullimg = "Database/Items/{}_full.png".format(data[3])
                    globals()[data[0]].oosimg = "None"
                    if renpy.loadable("Database/Items/{}_oos.png".format(data[3])):
                        globals()[data[0]].oosimg = "Database/Items/{}_oos.png".format(data[3])
                    globals()[data[0]].cost = int(data[4])
                    globals()[data[0]].consumable = data[5]
                    globals()[data[0]].description = data[6]


    def startequipments(filename):
        with renpy.file(filename) as equipslist:
            for line in equipslist:
                line = line.decode("utf-8")
                data = line.rstrip().split("\t")
                if data == "" or data[0][0] == "#": continue
                try: 
                    globals()[data[0]]
                except KeyError: 
                    globals()[data[0]] = Equipment(*data)
                else: 
                    globals()[data[0]].type = data[1]
                    globals()[data[0]].name = data[2]
                    globals()[data[0]].spriteimg = data[3]
                    globals()[data[0]].fullimg = "Database/{}/{}_full.png".format(data[1],data[4])
                    globals()[data[0]].oosimg = "None"
                    if renpy.loadable("Database/{}/{}_oos.png".format(data[1],data[4])):
                        globals()[data[0]].oosimg = "Database/{}/{}_oos.png".format(data[1],data[4])
                    globals()[data[0]].cost = int(data[5])
                    globals()[data[0]].atk = int(data[6])
                    globals()[data[0]].pdef = int(data[7])
                    globals()[data[0]].mdef = int(data[8])
                    globals()[data[0]].skill = "None"
                    if data[9] != "None":
                        globals()[data[0]].skill = globals()[data[9]]
                    globals()[data[0]].description = data[10]


    def startrecipes(filename):
        with renpy.file(filename) as recipeslist:
            for line in recipeslist:
                line = line.decode("utf-8")
                data = line.rstrip().split("\t")
                if data == "" or data[0][0] == "#": continue
                try: 
                    globals()[data[0]]
                except KeyError: 
                    globals()[data[0]] = Recipe(*data)
                else: 
                    globals()[data[0]].type = data[1]
                    globals()[data[0]].name = data[2]
                    globals()[data[0]].fullimg = "Database/Items/{}_full.png".format(data[3])
                    globals()[data[0]].oosimg = "None"
                    if renpy.loadable("Database/Items/{}_oos.png".format(data[3])):
                        globals()[data[0]].oosimg = "Database/Items/{}_oos.png".format(data[3])
                    globals()[data[0]].cost = int(data[4])
                    globals()[data[0]].description = data[5]
                    globals()[data[0]].output = globals()[data[6]]
                    globals()[data[0]].category = data[7]
                    globals()[data[0]].components = []
                    for i in range(0,len(data[8:])):
                        globals()[data[0]].components.append([globals()[data[8:][i].split(",")[0]], int(data[8:][i].split(",")[1])])


    def starttroopequips(filename):
        with renpy.file(filename) as troopequips:
            for line in troopequips:
                line = line.decode("utf-8")
                data = line.rstrip().split("\t")
                if data == "" or data[0][0] == "#": continue
                try: 
                    globals()[data[0]]
                except KeyError: 
                    globals()[data[0]] = TroopEquip(*data)
                else: 
                    globals()[data[0]].name = data[1]
                    globals()[data[0]].img = "Database/Troops/Equips/{}.png".format(data[2])
                    globals()[data[0]].type = data[3]
                    globals()[data[0]].consumable = data[4]                
                    globals()[data[0]].combat = int(data[5])
                    globals()[data[0]].defense = int(data[6])
                    globals()[data[0]].raid = int(data[7])
                    globals()[data[0]].diplomacy = int(data[8])
                    globals()[data[0]].siege = int(data[9])
                    globals()[data[0]].magic = int(data[10])
                    globals()[data[0]].tagadd = []
                    for i in range(0,len(data[11].split(","))):
                        if data[11].split(",")[i].strip() == "":
                            break
                        globals()[data[0]].tagadd.append(data[11].split(",")[i].strip())
                    globals()[data[0]].tagsub = []
                    for i in range(0,len(data[12].split(","))):
                        if data[12].split(",")[i].strip() == "":
                            break
                        globals()[data[0]].tagsub.append(data[12].split(",")[i].strip())
                    globals()[data[0]].description = data[13]
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
