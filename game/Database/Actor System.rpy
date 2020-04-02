


init -1:
    default activeparty = []

init -999 python:



    class Actor(object):
        def __init__(self, objname, name, affection, level, xp, stamina, hp, ep, str, con, res, skills, weapon, armor, acc, *args):
            self.objname = objname
            self.name = name
            self.face = "normal"
            self.blush = False
            self.affection = int(affection)
            self.level = int(level)
            self.xp = int(xp)
            self.nextxp = (2 ** (self.level -1)) * 5
            self.stamina = int(stamina)
            self.maxstamina = int(stamina)
            self.hp = int(hp)
            self.maxhp = int(hp)
            self.ep = 0
            self.maxep = int(ep)
            self.str = int(str)
            self.atk = self.str
            self.con = int(con)
            self.pdef = self.con
            self.res = int(res)
            self.mdef = self.res
            
            self.actives = []
            self.passives = []
            for i in range(0,len(skills.split(","))):
                if skills.split(",")[i] == "None":
                    break
                elif globals()[skills.split(",")[i]].stype == "Active":
                    self.actives.append(globals()[skills.split(",")[i]])
                elif globals()[skills.split(",")[i]].stype == "Passive":
                    self.passives.append(globals()[skills.split(",")[i]])
            
            self.weapon = "None"
            if weapon != "None":
                self.equip(globals()[weapon])
            
            self.armor = "None"
            if armor != "None":
                self.equip(globals()[armor])
            
            self.acc = "None"
            if acc != "None":
                self.equip(globals()[acc])
            
            self.extras = []
            if args:
                for i in range(0,len(args)):
                    self.extras.append(args[i])
            
            self.stance = "Normal"
            self.buffs = []
            self.debuffs = []
        
        
        
        def set_str(self, value):
            self.str = value
            self.atk = value
            if self.weapon != "None": self.atk += self.weapon.atk
            if self.armor != "None": self.atk += self.armor.atk
            if self.acc != "None": self.atk += self.acc.atk
        
        
        def add_str(self, value):
            self.str += value
            self.atk += value
        
        
        def set_con(self, value):
            self.con = value
            self.pdef = value
            if self.weapon != "None": self.pdef += self.weapon.pdef
            if self.armor != "None": self.pdef += self.armor.pdef
            if self.acc != "None": self.pdef += self.acc.pdef
        
        
        def add_con(self, value):
            self.con += value
            self.pdef += value
        
        
        def set_res(self, value):
            self.res = value
            self.mdef = value
            if self.weapon != "None": self.mdef += self.weapon.mdef
            if self.armor != "None": self.mdef += self.armor.mdef
            if self.acc != "None": self.mdef += self.acc.mdef
        
        
        def add_res(self, value):
            self.res += value
            self.mdef += value
        
        
        
        def equip(self, what, inventory="no"):
            if what == "None":
                return
            if what.type == "Weapon" and self.weapon != "None": 
                self.unequip(self.weapon, inventory=inventory)
            elif what.type == "Armor" and self.armor != "None":
                self.unequip(self.armor, inventory=inventory)
            elif what.type == "Accessory" and self.acc != "None":
                self.unequip(self.acc, inventory=inventory)
            if what.type == "Weapon": self.weapon = what
            if what.type == "Armor": self.armor = what
            if what.type == "Accessory": self.acc = what
            self.atk += what.atk
            self.pdef += what.pdef
            self.mdef += what.mdef
            if what.skill != "None":
                if what.skill.stype == "Active":
                    self.actives.append(what.skill)
                elif what.skill.stype == "Passive":
                    self.passives.append(what.skill)
            if inventory == "yes":
                actorequipment(item=what, do="equip")
        
        
        
        def unequip(self, what, inventory="no"):
            if what == "None":
                return
            if what.type == "Weapon": 
                if self.weapon == "None":
                    return
                else:
                    self.weapon = "None"
            elif what.type == "Armor": 
                if self.armor == "None":
                    return
                else:
                    self.armor = "None"
            elif what.type == "Accessory": 
                if self.acc == "None":
                    return
                else:
                    self.acc = "None"
            self.atk -= what.atk
            self.pdef -= what.pdef
            self.mdef -= what.mdef
            if what.skill != "None":
                if what.skill.stype == "Active":
                    self.actives.remove(what.skill)
                elif what.skill.stype == "Passive":
                    self.passives.remove(what.skill)
            if inventory == "yes":
                actorequipment(item=what, do="unequip")
        
        def recoverhp(self, amount="full"):
            if amount == "full":
                self.hp = self.maxhp
            else:
                self.hp += amount
                if self.hp > self.maxhp:
                    self.hp = self.maxhp
        
        def rest(self):
            self.hp = self.maxhp
            self.ep = 0
            self.stamina += (self.maxstamina / 2)
            if self.stamina > self.maxstamina:
                self.stamina = self.maxstamina
            if self.xp >= self.nextxp:
                self.level += 1
                self.xp -= self.nextxp
                self.nextxp = (2 ** (self.level -1)) * 5
                self.stamina = self.stamina + 10
                self.maxstamina = self.maxstamina + 10
                self.maxhp += 25
                self.hp = self.maxhp
                renpy.say(None, "{} gained a level! (Current: {})".format(self.name, self.level))
        
        
        
        def indexbuff(self, buff):
            for i in range(0,len(self.buffs)):
                if self.buffs[i][0] == buff: return(i)
        
        def has_buff(self,buff):
            if not any(e[0] == buff for e in self.buffs): return(0)
            return(self.buffs[self.indexbuff(buff)][1])
        
        def add_buff(self, buff, turns):
            if self.has_buff(buff) == 0: self.buffs.append([buff, turns])
            else: self.buffs[self.indexbuff(buff)][1] = turns
        
        def rem_buff(self, buff, turns=1):
            self.buffs[self.indexbuff(buff)][1] -= turns
        
        
        
        
        def indexdebuff(self, debuff):
            for i in range(0,len(self.debuffs)):
                if self.debuffs[i][0] == debuff: return(i)
        
        def has_debuff(self,debuff):
            if not any(e[0] == debuff for e in self.debuffs): return(0)
            return(self.debuffs[self.indexdebuff(debuff)][1])
        
        def add_debuff(self, debuff, turns):
            if self.has_debuff(debuff) == 0: self.debuffs.append([debuff, turns])
            else: self.debuffs[self.indexdebuff(debuff)][1] = turns
        
        def rem_debuff(self, debuff, turns=1):
            self.debuffs[self.indexdebuff(debuff)][1] -= turns
        
        
        
        def get_atk(self):
            atk_value = 0
            atk_value += self.atk
            if self.has_buff("Maply's Leaf") > 0:
                atk_value += 2
            if self.has_buff("Atk Up") > 0:
                atk_value += 2
            if self.has_debuff("Atk Down") > 0:
                atk_value -= 2
            return(atk_value)
        
        def get_pdef(self):
            pdef_value = 0
            pdef_value += self.pdef
            if self.has_buff("Jadk's Brew") > 0:
                pdef_value += 2
            if self.has_buff("Def Up") > 0:
                pdef_value += 2
            if self.has_debuff("Def Down") > 0:
                pdef_value -= 2
            return(pdef_value)
        
        def get_mdef(self):
            mdef_value = 0
            mdef_value += self.mdef
            if self.has_buff("Def Up") > 0:
                mdef_value += 2
            if self.has_debuff("Def Down") > 0:
                mdef_value -= 2
            return(mdef_value)










    def startactors(filename):
        with renpy.file(filename) as actorlist:
            for line in actorlist:
                line = line.decode("utf-8")
                data = line.rstrip().split("\t")
                if data == "" or data[0][0] == "#": continue
                try: 
                    globals()[data[0]]
                except KeyError: 
                    globals()[data[0]] = Actor(*data)
                else: 
                    continue


    def actorequipment(item, do):
        if do == "equip": Inventory.rem_item(item)
        else: Inventory.add_item(item)



    def startactorimages(filename):
        with renpy.file(filename) as actorlist:
            for line in actorlist:
                data = line.rstrip().split("\t")
                if data == '' or data[0][0] == '#': continue
                renpy.image(data[0], DynamicDisplayable(defimage, data[0]))



    def defimage(st, at, actor):
        actor = globals()[actor]
        layers=[]
        weapon_layer_1=[Rustysword]
        
        if actor == Avion:
            for i in range(0,len(actor.extras)):
                layers.append("Database/Actors/{}/{}.png".format(actor.objname, actor.extras[i]))
        
        if actor != Sabia:
            if actor.weapon != "None" and renpy.loadable("Database/Actors/{}/{}.png".format(actor.objname, actor.weapon.spriteimg)) and actor.weapon in weapon_layer_1:
                layers.append("Database/Actors/{}/{}.png".format(actor.objname, actor.weapon.spriteimg))
        
        if actor.armor == "None" and not renpy.loadable("Database/Actors/{}/basenaked.png".format(actor.objname)):
            if actor == Maply:
                layers.append("Database/Actors/{}/maple1.png".format(actor.objname))
            if actor == Neve:    
                layers.append("Database/Actors/{}/neve1.png".format(actor.objname))
            if renpy.loadable("Database/Actors/{}/basesimple.png".format(actor.objname)):
                layers.append("Database/Actors/{}/basesimple.png".format(actor.objname))
            elif renpy.loadable("Database/Actors/{}/base.png".format(actor.objname)):
                layers.append("Database/Actors/{}/base.png".format(actor.objname))
        
        elif actor.armor == "None" and renpy.loadable("Database/Actors/{}/basenaked.png".format(actor.objname)):
            layers.append("Database/Actors/{}/basenaked.png".format(actor.objname))
        
        if actor.armor != "None" and renpy.loadable("Database/Actors/{}/{}.png".format(actor.objname, actor.armor.spriteimg)):
            if actor == Sabia:
                layers.append("Database/Actors/{}/basesimple.png".format(actor.objname))
            if actor.armor == Barmaidclothes and "tray" in actor.extras:
                layers.append("Database/Actors/{}/baroutfit2.png".format(actor.objname))
            else:
                layers.append("Database/Actors/{}/{}.png".format(actor.objname, actor.armor.spriteimg))
        
        elif actor.armor != "None" and not renpy.loadable("Database/Actors/{}/{}.png".format(actor.objname, actor.armor.spriteimg)):
            layers.append("Database/Actors/{}/basesimple.png".format(actor.objname))
        
        if actor == Sabia and actor.armor == Exoticdancerclothes:
            layers.append("Database/Actors/{}/Exotic/{}.png".format(actor.objname, actor.face))
        elif actor == Kia:
            layers.append("Database/Actors/{}/{}.png".format(actor.objname, actor.face))
        else:
            layers.append("Database/Actors/{}/expressions/{}.png".format(actor.objname, actor.face))
        
        if actor.blush == True:
            if actor == Sabia and actor.armor == Exoticdancerclothes:
                layers.append("Database/Actors/{}/exotic/blush.png".format(actor.objname))
            else:
                layers.append("Database/Actors/{}/expressions/blush.png".format(actor.objname))
        
        if actor.acc != "None" and renpy.loadable("Database/Actors/{}/{}.png".format(actor.objname, actor.acc.name)):
            layers.append("Database/Actors/{}/{}.png".format(actor.objname, actor.acc.name))
        
        if actor.extras and actor != Avion and actor != Sabia:
            for i in range(0,len(actor.extras)):
                layers.append("Database/Actors/{}/{}.png".format(actor.objname, actor.extras[i]))
        
        if actor != Sabia:
            if actor.weapon != "None" and renpy.loadable("Database/Actors/{}/{}.png".format(actor.objname, actor.weapon.spriteimg)) and actor.weapon not in weapon_layer_1:
                layers.append("Database/Actors/{}/{}.png".format(actor.objname, actor.weapon.spriteimg))
        
        
        return Flatten(Fixed (*layers, fit_first=True)), None
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
