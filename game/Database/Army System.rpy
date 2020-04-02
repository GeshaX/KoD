

init -1:
    default army_groups = []
    default army_deployed_groups = []
    default selected_group = ""
    default troop_selected = "None"
    default troop_inventory = []
    default troop_inventory_page = 0

init -999:
    default all_troops_list = []

init -950 python:



    class Army(object):
        def __init__(self, name, maxsize):
            self.name = name
            self.troops = []
            self.maxsize = int(maxsize)
        
        
        def indextroop(self, troop):
            for i in range(0,len(self.troops)):
                if self.troops[i] == troop: return(i)
        
        
        def has_troop(self, troop):
            if not any(e == troop for e in self.troops): return(False)
            return(True)
        
        
        def has_tag(self, tag):
            for i in range(0,len(self.troops)):
                if any(e == tag for e in self.troops[i].get_troop_tags()): return(True)
            return(False)
        
        
        def add_troop(self, troop):
            self.troops.append(troop)
        
        
        def rem_troop(self, troop):
            self.troops.pop(self.indextroop(troop))
        
        
        def injury_random(self, amount, turns):
            import random
            if amount > len(self.troops):
                amount = len(self.troops)
            injury_list = random.sample(self.troops, amount)
            for i in range(0,len(injury_list)):
                renpy.block_rollback()
                injury_list[i].injury = turns
                renpy.say(None, "Unit {} will be disabled for the next {} turn(s).".format(injury_list[i].name, turns))
        
        
        def heal_troops(self, turns):
            for i in range(0,len(self.troops)):
                self.troops[i].injury -= turns
                if self.troops[i].injury < 0:
                    self.troops[i].injury = 0
        
        
        def get_combat(self):
            army_combat = 0
            for i in range(0,len(self.troops)):
                army_combat = army_combat + self.troops[i].get_troop_combat()
            return(army_combat)
        
        
        def get_defense(self):
            army_defense = 0
            for i in range(0,len(self.troops)):
                army_defense = army_defense + self.troops[i].get_troop_defense()
            return(army_defense)
        
        
        def get_raid(self):
            army_raid = 0
            for i in range(0,len(self.troops)):
                army_raid = army_raid + self.troops[i].get_troop_raid()
            return(army_raid)
        
        
        def get_siege(self):
            army_siege = 0
            for i in range(0,len(self.troops)):
                army_siege = army_siege + self.troops[i].get_troop_siege()
            return(army_siege)
        
        
        def get_magic(self):
            army_magic = 0
            for i in range(0,len(self.troops)):
                army_magic = army_magic + self.troops[i].get_troop_magic()
            return(army_magic)
        
        
        def get_diplomacy(self):
            army_diplomacy = 0
            for i in range(0,len(self.troops)):
                army_diplomacy = army_diplomacy + self.troops[i].get_troop_diplomacy()
            return(army_diplomacy)
        
        
        def get_deployed(self):
            return(len(self.troops))








    class Troop(object):
        def __init__(self, objname, name, combat, defense, raid, diplomacy, siege, magic, imgname, tags):
            self.objname = objname
            self.name = name
            self.combat = int(combat)
            self.defense = int(defense)
            self.raid = int(raid)
            self.diplomacy = int(diplomacy)
            self.siege = int(siege)
            self.magic = int(magic)
            self.img = "Database/Troops/{}.png".format(imgname)
            self.tags = []
            for i in range(0,len(tags.split(","))):
                self.tags.append(tags.split(",")[i].strip())
            self.injury = 0
            
            self.eqoffense = "None"
            self.eqdefense = "None"
            self.eqaccessory = "None"
            self.equtility = "None"
            
            all_troops_list.append(self)
        
        
        def troop_equip(self, what, inventory="no"):
            if what == "None":
                return
            if what.type == "Offense" and self.eqoffense != "None": 
                self.troop_unequip(self.eqoffense, inventory=inventory)
            
            elif what.type == "Defense" and self.eqdefense != "None":
                self.troop_unequip(self.eqdefense, inventory=inventory)
            
            elif what.type == "Accessory" and self.eqaccessory != "None":
                self.troop_unequip(self.eqaccessory, inventory=inventory)
            
            elif what.type == "Utility" and self.equtility != "None":
                self.troop_unequip(self.equtility, inventory=inventory)
            
            if what.type == "Offense": self.eqoffense = what
            elif what.type == "Defense": self.eqdefense = what
            elif what.type == "Accessory": self.eqaccessory = what
            elif what.type == "Utility": self.equtility = what
            
            if inventory == "yes":
                TroopInv.rem_item(what)
        
        
        def troop_unequip(self, what, inventory="no"):
            if what == "None":
                return
            if what.type == "Offense": 
                if self.eqoffense == "None":
                    return
                else:
                    self.eqoffense = "None"
            elif what.type == "Defense": 
                if self.eqdefense == "None":
                    return
                else:
                    self.eqdefense = "None"
            elif what.type == "Accessory": 
                if self.eqaccessory == "None":
                    return
                else:
                    self.eqaccessory = "None"
            elif what.type == "Utility": 
                if self.equtility == "None":
                    return
                else:
                    self.equtility = "None"
            if inventory == "yes":
                TroopInv.add_item(what)
        
        
        def has_troop_tag(self, tag):
            troop_tags = []
            troop_tags.extend(self.tags)
            troop_tags_sub = []
            if self.eqoffense != "None":
                troop_tags.extend(self.eqoffense.tagadd)
                troop_tags_sub.extend(self.eqoffense.tagsub)
            if self.eqdefense != "None": 
                troop_tags.extend(self.eqdefense.tagadd)
                troop_tags_sub.extend(self.eqdefense.tagsub)
            if self.eqaccessory != "None": 
                troop_tags.extend(self.eqaccessory.tagadd)
                troop_tags_sub.extend(self.eqaccessory.tagsub)
            if self.equtility != "None": 
                troop_tags.extend(self.equtility.tagadd)
                troop_tags_sub.extend(self.equtility.tagsub)       
            troop_tags = [x for x in troop_tags if x not in troop_tags_sub]
            if any(e == tag for e in troop_tags): return(True)
            return(False)
        
        
        def get_troop_tags(self):
            troop_tags = []
            troop_tags.extend(self.tags)
            troop_tags_sub = []
            if self.eqoffense != "None":
                troop_tags.extend(self.eqoffense.tagadd)
                troop_tags_sub.extend(self.eqoffense.tagsub)
            if self.eqdefense != "None": 
                troop_tags.extend(self.eqdefense.tagadd)
                troop_tags_sub.extend(self.eqdefense.tagsub)
            if self.eqaccessory != "None": 
                troop_tags.extend(self.eqaccessory.tagadd)
                troop_tags_sub.extend(self.eqaccessory.tagsub)
            if self.equtility != "None": 
                troop_tags.extend(self.equtility.tagadd)
                troop_tags_sub.extend(self.equtility.tagsub)       
            troop_tags = [x for x in troop_tags if x not in troop_tags_sub]
            return(troop_tags)
        
        
        def get_troop_combat(self):
            troop_combat = 0
            troop_combat += self.combat
            if self.eqoffense != "None": troop_combat += self.eqoffense.combat
            if self.eqdefense != "None": troop_combat += self.eqdefense.combat
            if self.eqaccessory != "None": troop_combat += self.eqaccessory.combat
            if self.equtility != "None": troop_combat += self.equtility.combat
            return(troop_combat)
        
        
        def get_troop_defense(self):
            troop_defense = 0
            troop_defense += self.defense
            if self.eqoffense != "None": troop_defense += self.eqoffense.defense
            if self.eqdefense != "None": troop_defense += self.eqdefense.defense
            if self.eqaccessory != "None": troop_defense += self.eqaccessory.defense
            if self.equtility != "None": troop_defense += self.equtility.defense
            return(troop_defense)
        
        
        def get_troop_raid(self):
            troop_raid = 0
            troop_raid += self.raid
            if self.eqoffense != "None": troop_raid += self.eqoffense.raid
            if self.eqdefense != "None": troop_raid += self.eqdefense.raid
            if self.eqaccessory != "None": troop_raid += self.eqaccessory.raid
            if self.equtility != "None": troop_raid += self.equtility.raid
            return(troop_raid)
        
        
        def get_troop_diplomacy(self):
            troop_diplomacy = 0
            troop_diplomacy += self.diplomacy
            if self.eqoffense != "None": troop_diplomacy += self.eqoffense.diplomacy
            if self.eqdefense != "None": troop_diplomacy += self.eqdefense.diplomacy
            if self.eqaccessory != "None": troop_diplomacy += self.eqaccessory.diplomacy
            if self.equtility != "None": troop_diplomacy += self.equtility.diplomacy
            return(troop_diplomacy)
        
        
        def get_troop_siege(self):
            troop_siege = 0
            troop_siege += self.siege
            if self.eqoffense != "None": troop_siege += self.eqoffense.siege
            if self.eqdefense != "None": troop_siege += self.eqdefense.siege
            if self.eqaccessory != "None": troop_siege += self.eqaccessory.siege
            if self.equtility != "None": troop_siege += self.equtility.siege
            return(troop_siege)
        
        
        def get_troop_magic(self):
            troop_magic = 0
            troop_magic += self.magic
            if self.eqoffense != "None": troop_magic += self.eqoffense.magic
            if self.eqdefense != "None": troop_magic += self.eqdefense.magic
            if self.eqaccessory != "None": troop_magic += self.eqaccessory.magic
            if self.equtility != "None": troop_magic += self.equtility.magic
            return(troop_magic)









    def starttroops(filename):
        global all_troops_list
        with renpy.file(filename) as troopslist:
            for line in troopslist:
                line = line.decode("utf-8")
                data = line.rstrip().split("\t")
                if data == "" or data[0][0] == "#": continue
                try: 
                    globals()[data[0]]
                except KeyError: 
                    globals()[data[0]] = Troop(*data)
                else: 
                    globals()[data[0]].name = data[1]
                    globals()[data[0]].img = "Database/Troops/{}.png".format(data[8])
                    if globals()[data[0]] not in all_troops_list:
                        all_troops_list.append(globals()[data[0]])
                    try: 
                        globals()[data[0]].eqoffense
                    except:
                        globals()[data[0]].eqoffense = "None"
                        globals()[data[0]].eqdefense = "None"
                        globals()[data[0]].eqaccessory = "None"
                        globals()[data[0]].equtility = "None"


    def deployarmies(*args):
        global army_groups
        global army_deployed_groups
        army_groups = []
        for i in range(0,len(args)):
            armyname = args[i][0].replace(" ", "")
            globals()[armyname] = Army(*args[i])
            army_groups.append(globals()[armyname])
        army_deployed_groups.extend(army_groups)
        return


    def reset_armies():
        global Mainarmy
        global army_deployed_groups
        for i in range(0,len(army_deployed_groups)):
            Mainarmy.troops.extend(army_deployed_groups[i].troops)
            army_deployed_groups[i].troops = []
        army_deployed_groups = []
        return


    def transfer_to_group(troop,group):
        global Mainarmy
        if len(group.troops) == group.maxsize:
            renpy.show_screen("army_fullgroup")
            return
        Mainarmy.rem_troop(troop)
        group.add_troop(troop)
        return


    def transfer_to_forces(troop,group):
        global Mainarmy
        Mainarmy.add_troop(troop)
        group.rem_troop(troop)
        return


    def heal_all_troops(turns):
        global all_troops_list
        for i in range(0,len(all_troops_list)):
            all_troops_list[i].injury -= turns                
            if all_troops_list[i].injury < 0:
                all_troops_list[i].injury = 0     




label deployment:
    $ selected_group = army_groups[0]
    show screen group_description
    call screen army_deployment
    return




screen army_deployment:
    text "Army Deployment" align (0.5,0.01) size 50 style "item_name"
    text "Available Forces" align (0.25,0.1)
    text "Group(s)" align (0.775,0.1)
    text "Scroll over an unit for information" size 16 align (0.1,0.7775) style "item_name"
    text "Select a group to edit and see information" size 16 align (0.9,0.7775) style "item_name"
    use army_groups
    button:
        align (0.05,0.05)
        clicked [Hide("army_maingroup"), Hide("troop_description"), Hide("group_description"), Return]
        style "menu_choice_button" xmaximum 120
        text "Exit" at truecenter size 16
    frame anchor (0.0,0,0) align (0.04,0.15) xysize (515,505) at menu_left:
        background Solid("#000000CC")
        has vpgrid:
            yfill True
            cols 5
            spacing 10
            scrollbars "vertical"
            mousewheel True
        for i in range(0,len(Mainarmy.troops)):
            if Mainarmy.troops[i].injury == 0:
                button:
                    padding (0,0)
                    xysize (90,90)
                    background None
                    hover_foreground "system/highlight.png"
                    add "{}".format(Mainarmy.troops[i].img)
                    hovered Show("troop_description", troop=Mainarmy.troops[i])
                    clicked Function(transfer_to_group, troop=Mainarmy.troops[i], group=selected_group)
            else:
                button:
                    padding (0,0)
                    xysize (90,90)
                    background None
                    hover_foreground "system/highlight.png"
                    add "{}".format(Mainarmy.troops[i].img) alpha 0.5
                    hovered Show("troop_description", troop=Mainarmy.troops[i])
                    clicked NullAction()


screen troop_description(troop="None"):
    frame anchor (0.0,0.0) align (0.04,0.785) padding (5,5) xysize (515,160) at menu_bottom:
        background Solid("#000000CC")
        if troop == "None":
            text "No troops to display" at truecenter
        else:
            vbox:
                xfill True
                vbox:
                    if troop.injury == 0:
                        text "{}".format(troop.name) size 14
                    else:
                        text "[troop.name] {color=#ff0000}(Injured: [troop.injury] turn(s)){/color}" size 14
                    hbox:
                        xfill True
                        vbox:
                            text "Combat: {}".format(troop.get_troop_combat()) size 14
                            text "Defense: {}".format(troop.get_troop_defense()) size 14

                        vbox:
                            text "Raid: {}".format(troop.get_troop_raid()) size 14
                            text "Siege: {}".format(troop.get_troop_siege()) size 14

                        vbox:
                            text "Diplomacy: {}".format(troop.get_troop_diplomacy()) size 14
                            text "Magic: {}".format(troop.get_troop_magic()) size 14
                    $ trooptags = ", ".join(troop.get_troop_tags())
                    text "Tags: [trooptags]" size 14

                vbox:
                    text "\nEquipped Items:" size 14
                    hbox:
                        xfill True
                        vbox:
                            if troop.eqoffense == "None":
                                text "Offense: None" size 14
                            else:
                                text "Offense: {}".format(troop.eqoffense.name) size 14
                            if troop.eqdefense == "None":
                                text "Defense: None" size 14
                            else:
                                text "Defense: {}".format(troop.eqdefense.name) size 14
                        vbox:
                            if troop.eqaccessory == "None":
                                text "Accessory: None" size 14
                            else:
                                text "Accessory: {}".format(troop.eqaccessory.name) size 14
                            if troop.equtility == "None":
                                text "Utility: None" size 14
                            else:
                                text "Utility: {}".format(troop.equtility.name) size 14


screen army_groups:
    frame anchor (1.0,0,0) align (0.97,0.15) xysize (505,505) at menu_right:
        background Solid("#000000CC")
        has viewport:
            scrollbars "vertical"
            mousewheel True
        vbox:
            for i in range(0,len(army_groups)):
                vbox:
                    frame:
                        xfill True
                        ysize 50
                        text "{}".format(army_groups[i].name)
                        if selected_group == army_groups[i]:
                            background Solid("999900CC")
                            button:
                                xsize 80
                                xanchor 1.0
                                xpos 1.0
                                style "menu_choice_button"
                                text "Selected" size 16 color ("#999900") style "combat_number" at truecenter
                                clicked NullAction()

                        else:
                            background Solid("#000000CC")
                            button:
                                xsize 80
                                xanchor 1.0
                                xpos 1.0
                                style "menu_choice_button"
                                text "Select" size 16 at truecenter
                                clicked [Show("group_description"), SetVariable("selected_group", army_groups[i])]
                    frame:
                        background None
                        has vpgrid:
                            cols 5
                            spacing 5
                        for j in range(0,army_groups[i].maxsize):
                            if j < len(army_groups[i].troops):
                                button:
                                    padding (0,0)
                                    xysize (90,90)
                                    hover_foreground "system/highlight.png"
                                    add "{}".format(army_groups[i].troops[j].img)
                                    hovered Show("troop_description", troop=army_groups[i].troops[j])
                                    clicked Function(transfer_to_forces, troop=army_groups[i].troops[j], group=army_groups[i])
                            else:
                                button:
                                    padding (0,0)
                                    xysize (90,90)
                                    hover_foreground "system/highlight.png"
                                    hovered Show("troop_description")
                                    clicked [Show("group_description"), SetVariable("selected_group", army_groups[i])]


screen group_description(group=selected_group):
    frame anchor (1.0,0.0) align (0.97,0.785) padding (5,5) xysize (505,160) at menu_bottom:
        background Solid("#000000CC")
        has vbox
        text "{}\n".format(group.name)
        hbox:
            vbox:
                xsize 265
                text "Total Combat: {}".format(group.get_combat())
                text "Total Raid: {}".format(group.get_raid())
                text "Total Siege: {}".format(group.get_siege())
            vbox:
                xsize 265
                text "Total Defense: {}".format(group.get_defense())
                text "Total Diplomacy: {}".format(group.get_diplomacy())
                text "Total Magic: {}".format(group.get_magic())


screen army_fullgroup:
    frame anchor (0.5,0,0) pos (0.5,0.05) xysize (600,50) padding (10,10) at menu_top:
        background Solid("#000000CC")
        text "Group is already at full capacity!" at center
    timer 2.0 action Hide("army_fullgroup")




label troop_statsscreen:
    $ troop_inventory = TroopInv.weapons
    $ troop_selected = "None"
    $ clearactors()
    $ renpy.retain_after_load()
    hide screen infohud
    call screen troop_statsscreen
    pause (0.23)
    return

screen troop_statsscreen tag menu:

    button:
        pos (0.1,0.95)
        clicked [Hide("troop_statsscreen"), Hide("troop_status"), Hide("troop_iteminfo"), Return]
        style "menu_choice_button" xmaximum 120
        text "Exit" at truecenter size 16

    frame pos (0.01,0.01) padding (10,10) xysize (320,787) at menu_left:
        background Solid("#000000CC")
        has vbox
        text "Troop List" style "item_name" xalign (0.5)
        vpgrid:
            yfill True
            xfill True
            cols 3
            spacing 10
            scrollbars "vertical"
            mousewheel True
            for i in range(0,len(Mainarmy.troops)):
                button:
                    padding (0,0)
                    xysize (90,90)
                    background None
                    hover_foreground "system/highlight.png"
                    add "{}".format(Mainarmy.troops[i].img)
                    clicked [Show("troop_status", troop=Mainarmy.troops[i]), SetVariable("troop_selected", Mainarmy.troops[i])]

    frame pos (400,8) xysize (700,185) at menu_top:
        background Solid("#000000CC")
        text "Click a troop on the list to display information" anchor (0.5,0.0) align (0.5,1.05) size 14 style "item_name"

    frame pos (400,220) xysize (700,115) at menu_right:
        background Solid("#000000CC")
        text "Hover over items to display information" anchor (0.5,0.0) align (0.5,1.05) size 14 style "item_name"

    frame pos (400,365) xysize (700,30) padding (-1,-1) at menu_bottom:
        background None
        has hbox:
            xalign 0.5
        button:
            style "menu_choice_button" xmaximum 117
            text "Offense" at truecenter size 16
            clicked SetVariable("troop_inventory", TroopInv.weapons)
        button:
            style "menu_choice_button" xmaximum 117
            text "Defense" at truecenter size 16
            clicked SetVariable("troop_inventory", TroopInv.armors)
        button:
            style "menu_choice_button" xmaximum 117
            text "Accessories" at truecenter size 16
            clicked SetVariable("troop_inventory", TroopInv.accs)
        button:
            style "menu_choice_button" xmaximum 117
            text "Utility" at truecenter size 16
            clicked SetVariable("troop_inventory", TroopInv.keyitems)

    frame pos (400,395) xysize (700,400) padding (5,5) at menu_bottom:
        background Solid("#000000CC")
        $ x=0
        $ y=0
        $ troop_inventory_nextpage = troop_inventory_page + 1
        if troop_inventory_nextpage > int(len(troop_inventory)/28):
            $ troop_inventory_nextpage = 0
        for i in range(0,len(troop_inventory)):
            if i+1 <= (troop_inventory_page+1)*28 and i+1 > troop_inventory_page*28:
                if troop_selected == "None":
                    button:
                        pos (x,y)
                        xysize (90,90)
                        background None
                        hover_foreground "system/highlight.png"
                        add troop_inventory[i][0].img size (90,90) align (0.5,0.5)
                        $ stockamount = troop_inventory[i][1]
                        text "{b}[stockamount]{/b}" size 14 anchor (1.0,1.0) align (1.1,1.05) style "item_name"
                        hovered Show("troop_iteminfo", item=troop_inventory[i][0])
                        clicked NullAction()
                else:
                    button:
                        pos (x,y)
                        xysize (90,90)
                        background None
                        hover_foreground "system/highlight.png"
                        add troop_inventory[i][0].img size (90,90) align (0.5,0.5)
                        $ stockamount = troop_inventory[i][1]
                        text "{b}[stockamount]{/b}" size 14 anchor (1.0,1.0) align (1.1,1.05) style "item_name"
                        hovered Show("troop_iteminfo", item=troop_inventory[i][0])
                        clicked [Function(troop_selected.troop_equip, what=troop_inventory[i][0], inventory="yes"), Hide("troop_iteminfo")]
                $ x+=100
                if x > 600:
                    $ x = 0
                    $ y += 100
        if len(troop_inventory)>28:
            button:
                pos (580,400)
                style "menu_choice_button" xmaximum 120
                text "Next Page" at truecenter size 16
                action SetVariable('troop_inventory_page', troop_inventory_nextpage)
        text "Click on items to equip and unequip (if a troop is selected)" anchor (0.5,0.0) align (0.5,1.025) size 14 style "item_name"

screen troop_status(troop):
    frame pos (400,8) xysize (700,185):
        background None
        has vbox:
            xfill True
        hbox:
            vbox:
                xmaximum 290
                text "Name: {}".format(troop.name) size 16
                null height 20
                hbox:
                    xsize 290
                    vbox:
                        $ troop_combat = troop.get_troop_combat()
                        if troop_combat >= troop.combat:
                            text "Combat: {color=#00FF00}[troop_combat]{/color} ([troop.combat])" size 14
                        else:
                            text "Combat: {color=#FF0000}[troop_combat]{/color} ([troop.combat])" size 14


                        $ troop_raid = troop.get_troop_raid()
                        if troop_raid >= troop.raid:
                            text "Raid: {color=#00FF00}[troop_raid]{/color} ([troop.raid])" size 14
                        else:
                            text "Raid: {color=#FF0000}[troop_raid]{/color} ([troop.raid])" size 14

                        $ troop_siege = troop.get_troop_siege()
                        if troop_siege >= troop.siege:
                            text "Siege: {color=#00FF00}[troop_siege]{/color} ([troop.siege])" size 14
                        else:
                            text "Siege: {color=#FF0000}[troop_siege]{/color} ([troop.siege])" size 14


                    vbox:
                        $ troop_defense = troop.get_troop_defense()
                        if troop_defense >= troop.defense:
                            text "Defense: {color=#00FF00}[troop_defense]{/color} ([troop.defense])" size 14
                        else:
                            text "Defense: {color=#FF0000}[troop_defense]{/color} ([troop.defense])" size 14

                        $ troop_diplomacy = troop.get_troop_diplomacy()
                        if troop_diplomacy >= troop.diplomacy:
                            text "Diplomacy: {color=#00FF00}[troop_diplomacy]{/color} ([troop.diplomacy])" size 14
                        else:
                            text "Diplomacy: {color=#FF0000}[troop_diplomacy]{/color} ([troop.diplomacy])" size 14

                        $ troop_magic = troop.get_troop_magic()
                        if troop_magic >= troop.magic:
                            text "Magic: {color=#00FF00}[troop_magic]{/color} ([troop.magic])" size 14
                        else:
                            text "Magic: {color=#FF0000}[troop_magic]{/color} ([troop.magic])" size 14
                null height 5
            vbox:
                text "Currently Equipped" size 16 at center
                hbox:
                    vbox:
                        text "Offense" size 14 at truecenter
                        null height 5
                        button:
                            xysize (90,90)
                            background None
                            hover_foreground Frame("system/highlight.png")
                            if troop.eqoffense != "None":
                                hovered Show("troop_iteminfo", item=troop.eqoffense)
                                unhovered Show("troop_iteminfo", item=troop.eqoffense)
                                clicked [Function(troop_selected.troop_unequip, what=troop_selected.eqoffense, inventory="yes"), SetVariable("troop_inventory", TroopInv.weapons), Hide("troop_iteminfo")]
                                add troop.eqoffense.img size (90,90) align (0.5,0.5)
                    null width 10
                    vbox:
                        text "Defense" size 14 at truecenter
                        null height 5
                        button:
                            xysize (90,90)
                            background None
                            hover_foreground Frame("system/highlight.png")
                            if troop.eqdefense != "None":
                                hovered Show("troop_iteminfo", item=troop.eqdefense)
                                unhovered Show("troop_iteminfo", item=troop.eqdefense)
                                clicked [Function(troop_selected.troop_unequip, what=troop_selected.eqdefense, inventory="yes"), SetVariable("troop_inventory", TroopInv.armors), Hide("troop_iteminfo")]
                                add troop.eqdefense.img size (90,90) align (0.5,0.5)
                    null width 10
                    vbox:
                        text "Accessory" size 14 at truecenter
                        null height 5
                        button:
                            xysize (90,90)
                            background None
                            hover_foreground Frame("system/highlight.png")
                            if troop.eqaccessory != "None":
                                hovered Show("troop_iteminfo", item=troop.eqaccessory)
                                unhovered Show("troop_iteminfo", item=troop.eqaccessory)
                                clicked [Function(troop_selected.troop_unequip, what=troop_selected.eqaccessory, inventory="yes"), SetVariable("troop_inventory", TroopInv.accs), Hide("troop_iteminfo")]
                                add troop.eqaccessory.img size (90,90) align (0.5,0.5)
                    null width 10
                    vbox:
                        text "Utility" size 14 at truecenter
                        null height 5
                        button:
                            xysize (90,90)
                            background None
                            hover_foreground Frame("system/highlight.png")
                            if troop.equtility != "None":
                                hovered Show("troop_iteminfo", item=troop.equtility)
                                unhovered Show("troop_iteminfo", item=troop.equtility)
                                clicked [Function(troop_selected.troop_unequip, what=troop_selected.equtility, inventory="yes"), SetVariable("troop_inventory", TroopInv.keyitems), Hide("troop_iteminfo")]
                                add troop.equtility.img size (90,90) align (0.5,0.5)
        null height 10
        $ trooptags = ", ".join(troop.get_troop_tags())
        text "Tags: [trooptags]" size 14

screen troop_iteminfo(item):
    frame pos (400,220) xysize (700,115):
        background None
        has vbox
        text "[item.name]: [item.description]" size 16
        null height 10
        hbox:
            xfill True

            if item.combat >= 0:
                text "Combat:{color=#00FF00} [item.combat]{/color}" size 14
            else:
                text "Combat:{color=#FF0000} [item.combat]{/color}" size 14

            if item.defense >= 0:
                text "Defense:{color=#00FF00} [item.defense]{/color}" size 14
            else:
                text "Defense:{color=#FF0000} [item.defense]{/color}" size 14

            if item.raid >= 0:
                text "Raid:{color=#00FF00} [item.raid]{/color}" size 14
            else:
                text "Raid:{color=#FF0000} [item.raid]{/color}" size 14

            if item.diplomacy >= 0:
                text "Diplomacy:{color=#00FF00} [item.diplomacy]{/color}" size 14
            else:
                text "Diplomacy:{color=#FF0000} [item.diplomacy]{/color}" size 14

            if item.siege >= 0:
                text "Siege:{color=#00FF00} [item.siege]{/color}" size 14
            else:
                text "Siege:{color=#FF0000} [item.siege]{/color}" size 14

            if item.magic >= 0:
                text "Magic:{color=#00FF00} [item.magic]{/color}" size 14
            else:
                text "Magic:{color=#FF0000} [item.magic]{/color}" size 14

        null height 10
        $ itemaddtags = ", ".join(item.tagadd)
        $ itemsubtags = ", ".join(item.tagsub)
        text "{color=#00FF00}Adds Tags{/color}: [itemaddtags]" size 14
        text "{color=#FF0000}Removes Tags{/color}: [itemsubtags]" size 14
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
