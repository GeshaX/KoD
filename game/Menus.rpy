

init -1:
    default a_list = []
    default a_order = []
    default actor = ""
    default statsinventory = []
    default statsscreen_inventory_page = 0
    default crafting_potions = "on"
    default crafting_weapons = "off"
    default crafting_armors = "off"
    default crafting_accessories = "off"
    default crafting_royal_gold_locked = False
    default gallery_workaround = False
    default gallery_picked = []
    default gallery_scenes_skip = ["Lutvrog", "Barrin", "Catgirls", "Alioch","Avion", "Misc"]




label progressionscreen:
    show screen progression_screen
    pause
    hide screen progression_screen
    return

screen progression_screen:
    key "game_menu" action [Hide("progression_screen"), Return]
    $ a_order = ["Groknak", "Rokgrid", "Tekrok", "Dajrab", "Neve", "Maply", "Vehlis", "Kia", "Ylva", "Lutvrog", "Jadk"]
    frame pos (450,100) xsize (480) xpadding 20 at menu_top:
        background Solid("#000000CC")
        has hbox:
            xfill True
            spacing 50
        vbox:
            text "Personality:" style "item_name" size 16
            text "Domination: [dom]" size 14
            text "Submission: [sub]" size 14
        vbox:
            text "Loyalty:" style "item_name" size 16
            text "Humans: [L_humans]" size 14
            text "Orcs: [L_orcs]" size 14
            text "Catgirls: [L_catgirls]" size 14
        vbox:
            text "Core stats:" style "item_name" size 16
            text "Freedom: [freedom]" size 14
            text "Slavery: [slavery]" size 14

    frame pos (450,200) xsize (480) xpadding 20 at menu_bottom:
        background Solid("#000000CC")
        text "Relationship stats:" align (0.5,0.01) style "item_name"

    frame pos (450,240) xsize (480) xpadding 20 at menu_bottom:
        background Solid("#000000CC")
        has vpgrid:
            scrollbars "vertical"
            ymaximum 360
            mousewheel True
            spacing 20
            xfill True
            cols 4
        for i in range(0,len(a_order)):
            if a_order[i] in a_list:
                vbox:
                    add "database/portraits/{}.png".format(a_order[i])
                    text "{}: {}".format(a_order[i], globals()["A_" + a_order[i].lower()]) size 14 at center




label statsscreen:
    $ statsinventory = Inventory.items
    $ clearactors()
    $ renpy.show(actor.objname, at_list=[actor_left])
    $ renpy.retain_after_load()
    call screen statsscreen(actor)
    pause (0.23)
    return


screen statsscreen(actor) tag menu:

    use statsscreen_inventory
    frame pos (400,8) xysize (360,150) xpadding 20 at menu_top:
        background Solid("#000000CC")
        has hbox:
            xsize 350
        vbox:
            xsize 220
            text "Name: [actor.name]"
            null height 2
            bar:
                style "bar_hp"
                xmaximum 130
                value actor.hp
                range actor.maxhp
                left_gutter 0
                right_gutter 0
                thumb None
                thumb_shadow None
            text " [actor.hp] / [actor.maxhp]" size 16 line_leading -20 ypos -7
            bar:
                style "bar_ep"
                xmaximum 130
                value actor.stamina
                range actor.maxstamina
                left_gutter 0
                right_gutter 0
                thumb None
                thumb_shadow None
            null width 5
            text " [actor.stamina] / [actor.maxstamina]" size 16 line_leading -20 ypos -6

            null height 2
            text "Level: [actor.level]"
            text "XP: [actor.xp] / [actor.nextxp]"
        vbox:
            xsize 130
            null height 8
            text "STR: [actor.str]" size 16
            text "CON: [actor.con]" size 16
            text "RES: [actor.res]" size 16
            text "ATK: [actor.atk]" size 16
            text "P-DEF: [actor.pdef]" size 16
            text "M-DEF: [actor.mdef]" size 16

    frame pos (800,8) xysize (300,150) padding (5,5) at menu_top:
        background Solid("#000000CC")
        has vbox:
            yfill True
            yanchor 1.0
            yalign 1.0
        text "Currently Equipped" size 16 at top
        hbox:
            vbox:
                text "Weapon" size 14 at truecenter
                null height 5
                button:
                    xysize (90,90)
                    background None
                    hover_background Frame("system/highlight.png")
                    if actor.weapon != "None":
                        hovered Show("statsscreen_iteminfo", actor=actor, item=actor.weapon, do="unequip")
                        unhovered Show("statsscreen_iteminfo", actor=actor, item=actor.weapon, do="unequip")
                        clicked [Function(actor.unequip, what=actor.weapon, inventory="yes"), SetVariable("statsinventory", Inventory.weapons), Hide("statsscreen_iteminfo")]
                        add actor.weapon.fullimg size (90,90) align (0.5,0.5)
            null width 10
            vbox:
                text "Armor" size 14 at truecenter
                null height 5
                button:
                    xysize (90,90)
                    background None
                    hover_background Frame("system/highlight.png")
                    if actor.armor != "None":
                        hovered Show("statsscreen_iteminfo", actor=actor, item=actor.armor, do="unequip")
                        unhovered Show("statsscreen_iteminfo", actor=actor, item=actor.armor, do="unequip")
                        clicked [Function(actor.unequip, what=actor.armor, inventory="yes"), SetVariable("statsinventory", Inventory.armors), Hide("statsscreen_iteminfo")]
                        add actor.armor.fullimg size (90,90) align (0.5,0.5)
            null width 10
            vbox:
                text "Accessory" size 14 at truecenter
                null height 5
                button:
                    xysize (90,90)
                    background None
                    hover_background Frame("system/highlight.png")
                    if actor.acc != "None":
                        hovered Show("statsscreen_iteminfo", actor=actor, item=actor.acc, do="unequip")
                        unhovered Show("statsscreen_iteminfo", actor=actor, item=actor.acc, do="unequip")
                        clicked [Function(actor.unequip, what=actor.acc, inventory="yes"), SetVariable("statsinventory", Inventory.accs), Hide("statsscreen_iteminfo")]
                        add actor.acc.fullimg size (90,90) align (0.5,0.5)

    frame pos (400,190) xysize (700,145) at menu_right:
        background Solid("#000000CC")

    frame pos (400,365) xysize (700,30) padding (-1,-1) at menu_bottom:
        background None
        has hbox
        button:
            style "menu_choice_button" xmaximum 117
            text "Items" at truecenter size 16
            clicked SetVariable("statsinventory", Inventory.items)
        button:
            style "menu_choice_button" xmaximum 117
            text "Weapons" at truecenter size 16
            clicked SetVariable("statsinventory", Inventory.weapons)
        button:
            style "menu_choice_button" xmaximum 117
            text "Armors" at truecenter size 16
            clicked SetVariable("statsinventory", Inventory.armors)
        button:
            style "menu_choice_button" xmaximum 117
            text "Accessories" at truecenter size 16
            clicked SetVariable("statsinventory", Inventory.accs)
        button:
            style "menu_choice_button" xmaximum 117
            text "Recipes" at truecenter size 16
            clicked SetVariable("statsinventory", Inventory.recipes)
        button:
            style "menu_choice_button" xmaximum 117
            text "Key Items" at truecenter size 16
            clicked SetVariable("statsinventory", Inventory.keyitems)

    button:
        align (0.01,0.01)
        clicked [Hide("statsscreen_iteminfo"), Hide("statsscreen_inventory"), Return]
        style "menu_choice_button" xmaximum 120
        text "Exit" at truecenter size 16


screen statsscreen_iteminfo(actor, item, do="nothing"):
    frame pos (400,190) xysize (700,145) padding (15,10):
        background None
        has hbox
        vbox:
            xsize 220
            text "[item.name]" size 16
            if hasattr(item, 'atk'):
                text "\nAtk: [item.atk]" size 16
            if hasattr(item, 'pdef'):
                text "Def: [item.pdef]" size 16
            if hasattr(item, 'mdef'):
                text "M-Def: [item.mdef]" size 16
            if hasattr(item, 'skill') and item.skill != "None":
                text "Skill: [item.skill.name]" size 16
        text "[item.description]" size 16
    if do == "unequip":
        button:
            pos (634,300)
            style "menu_choice_button" xmaximum 120
            text "Unequip" at truecenter size 16
            clicked [Function(actor.unequip, what=item, inventory="yes"), Hide("statsscreen_iteminfo")]
    elif do == "consumable":
        button:
            pos (634,300)
            style "menu_choice_button" xmaximum 120
            text "Consume" at truecenter size 16
            clicked Function(statsscreen_use_consumable, item=item)
    elif do == "nothing":
        if item.type == "Weapon" or item.type == "Armor" or item.type == "Accessory":
            button:
                pos (634,300)
                style "menu_choice_button" xmaximum 120
                text "Equip" at truecenter size 16
                clicked [Function(actor.equip, what=item, inventory="yes"), Hide("statsscreen_iteminfo")]


screen statsscreen_inventory:
    frame pos (400,395) xysize (700,400) padding (5,5) at menu_bottom:
        background Solid("#000000CC")
        $ x=0
        $ y=0
        $ statsscreen_inventory_nextpage = statsscreen_inventory_page + 1
        if statsscreen_inventory_nextpage > int(len(statsinventory)/28):
            $ statsscreen_inventory_nextpage = 0
        for i in range(0,len(statsinventory)):
            if i+1 <= (statsscreen_inventory_page+1)*28 and i+1 > statsscreen_inventory_page*28:
                if statsinventory[i][0].type == "Item" or statsinventory[i][0].type == "Recipe" or statsinventory[i][0].type == "Key item":
                    if hasattr(statsinventory[i][0], "consumable") and statsinventory[i][0].consumable == "Yes":
                        button:
                            pos (x,y)
                            xysize (90,90)
                            background None
                            hover_background "system/highlight.png"
                            add statsinventory[i][0].fullimg size (90,90) align (0.5,0.5)
                            $ stockamount = statsinventory[i][1]
                            text "{b}[stockamount]{/b}" size 14 anchor (1.0,1.0) align (1.1,1.05)
                            hovered Show("statsscreen_iteminfo", actor=actor, item=statsinventory[i][0], do="consumable")
                            unhovered Show("statsscreen_iteminfo", actor=actor, item=statsinventory[i][0], do="consumable")
                            clicked Function(statsscreen_use_consumable, item=statsinventory[i][0])
                    else:
                        button:
                            pos (x,y)
                            xysize (90,90)
                            background None
                            hover_background "system/highlight.png"
                            add statsinventory[i][0].fullimg size (90,90) align (0.5,0.5)
                            $ stockamount = statsinventory[i][1]
                            text "{b}[stockamount]{/b}" size 14 anchor (1.0,1.0) align (1.1,1.05)
                            hovered Show("statsscreen_iteminfo", actor=actor, item=statsinventory[i][0])
                            unhovered Show("statsscreen_iteminfo", actor=actor, item=statsinventory[i][0])
                            clicked Show("statsscreen_iteminfo", actor=actor, item=statsinventory[i][0])
                elif statsinventory[i][0].type == "Weapon" or statsinventory[i][0].type == "Armor" or statsinventory[i][0].type == "Accessory":
                    button:
                        pos (x,y)
                        xysize (90,90)
                        background None
                        hover_background "system/highlight.png"
                        add statsinventory[i][0].fullimg size (90,90) align (0.5,0.5)
                        $ stockamount = statsinventory[i][1]
                        text "{b}[stockamount]{/b}" size 14 anchor (1.0,1.0) align (1.1,1.05)
                        hovered Show("statsscreen_iteminfo", actor=actor, item=statsinventory[i][0])
                        unhovered Show("statsscreen_iteminfo", actor=actor, item=statsinventory[i][0])
                        clicked Function(actor.equip, what=statsinventory[i][0], inventory="yes"), Hide("statsscreen_iteminfo")
                $ x+=100
                if x > 600:
                    $ x = 0
                    $ y += 100
        if len(statsinventory)>28:
            button:
                pos (580,400)
                style "menu_choice_button" xmaximum 120
                text "Next Page" at truecenter size 16
                action SetVariable('statsscreen_inventory_page', statsscreen_inventory_nextpage)


init -1 python:
    def statsscreen_use_consumable(item):
        if item == Healthpotion:
            Inventory.rem_item(Healthpotion)
            if Inventory.has_item(Healthpotion) == 0:
                renpy.hide_screen("statsscreen_iteminfo")
            renpy.show("statsscreen_number_float", at_list=[number_float(0.25)], what=Text("+ {}".format(actor.maxhp - actor.hp), size=34, style="combat_number", color="#00FF00"))
            actor.hp = actor.maxhp
        
        if item == Energypotion:
            renpy.call_in_new_context("statsscreen_say", Energypotion)
        
        return


label statsscreen_say(what):
    if what == Energypotion:
        $ renpy.say(None, "(It'd just be a waste, it wouldn't last until I got into combat.)")
    return







label crafting_screen:
    $ clearactors()
    $ renpy.retain_after_load()
    call screen crafting_screen
    pause (0.23)
    return


screen crafting_screen tag menu:

    frame pos (0.01,0.01) padding (10,10) xysize (300,825) at menu_left:
        background Solid("#000000CC")
        viewport:
            scrollbars "vertical"
            xmaximum 300
            mousewheel True
            has vbox:
                xfill True

            if crafting_potions_unlocked:
                button:
                    background None
                    xfill True
                    hover_background Frame("system/highlight.png")
                    if crafting_potions == "on":
                        text "--- POTIONS ---" color "#FFFFFF" at truecenter
                        clicked SetVariable("crafting_potions", "off")
                    else:
                        text "+++ POTIONS +++" color "#FFFFFF" at truecenter
                        clicked SetVariable("crafting_potions", "on")
            if crafting_potions == "on":
                for i in range(0,len(Inventory.recipes)):
                    if Inventory.recipes[i][0].category == "Potions":
                        button:
                            background None
                            xfill True
                            hover_background Frame("system/highlight.png")
                            text "{}".format(Inventory.recipes[i][0].output.name) font "Lora.ttf" at truecenter
                            hovered Show("crafting_screen_output", recipe=Inventory.recipes[i][0])
                            unhovered [Show("crafting_screen_output", recipe=Inventory.recipes[i][0]), Hide("crafting_screen_crafted")]
                            if crafting_get_amount(Inventory.recipes[i][0]) > 0:
                                clicked Show("crafting_screen_confirm", recipe=Inventory.recipes[i][0])
                            else:
                                clicked Show("crafting_screen_crafted", recipe="None")

            null height 15
            if crafting_weapons_unlocked:
                button:
                    background None
                    xfill True
                    hover_background Frame("system/highlight.png")
                    if crafting_weapons == "on":
                        text "--- WEAPONS ---" color "#FFFFFF" at truecenter
                        clicked SetVariable("crafting_weapons", "off")
                    else:
                        text "+++ WEAPONS +++" color "#FFFFFF" at truecenter
                        clicked SetVariable("crafting_weapons", "on")
            if crafting_weapons == "on":
                for i in range(0,len(Inventory.recipes)):
                    if Inventory.recipes[i][0].category == "Weapons":
                        button:
                            background None
                            xfill True
                            hover_background Frame("system/highlight.png")
                            text "{}".format(Inventory.recipes[i][0].output.name) font "Lora.ttf" at truecenter
                            hovered Show("crafting_screen_output", recipe=Inventory.recipes[i][0])
                            unhovered [Show("crafting_screen_output", recipe=Inventory.recipes[i][0]), Hide("crafting_screen_crafted")]
                            clicked NullAction()

            null height 15
            if crafting_armors_unlocked:
                button:
                    background None
                    xfill True
                    hover_background Frame("system/highlight.png")
                    if crafting_armors == "on":
                        text "--- ARMORS ---" color "#FFFFFF" at truecenter
                        clicked SetVariable("crafting_armors", "off")
                    else:
                        text "+++ ARMORS +++" color "#FFFFFF" at truecenter
                        clicked SetVariable("crafting_armors", "on")
            if crafting_armors == "on":
                for i in range(0,len(Inventory.recipes)):
                    if Inventory.recipes[i][0].category == "Armors":
                        button:
                            background None
                            xfill True
                            hover_background Frame("system/highlight.png")
                            text "{}".format(Inventory.recipes[i][0].output.name) font "Lora.ttf" at truecenter
                            hovered Show("crafting_screen_output", recipe=Inventory.recipes[i][0])
                            unhovered [Show("crafting_screen_output", recipe=Inventory.recipes[i][0]), Hide("crafting_screen_crafted")]
                            clicked NullAction()

            null height 15
            if crafting_accessories_unlocked:
                button:
                    background None
                    xfill True
                    hover_background Frame("system/highlight.png")
                    if crafting_accessories == "on":
                        text "--- ACCESSORIES ---" color "#FFFFFF" at truecenter
                        clicked SetVariable("crafting_accessories", "off")
                    else:
                        text "+++ ACCESSORIES +++" color "#FFFFFF" at truecenter
                        clicked SetVariable("crafting_accessories", "on")
            if crafting_accessories == "on":
                for i in range(0,len(Inventory.recipes)):
                    if Inventory.recipes[i][0].category == "Accessories":
                        button:
                            background None
                            xfill True
                            hover_background Frame("system/highlight.png")
                            text "{}".format(Inventory.recipes[i][0].output.name) font "Lora.ttf" at truecenter
                            hovered Show("crafting_screen_output", recipe=Inventory.recipes[i][0])
                            unhovered [Show("crafting_screen_output", recipe=Inventory.recipes[i][0]), Hide("crafting_screen_crafted")]
                            clicked NullAction()

        button:
            align (0.5,0.99)
            clicked [Hide("crafting_screen_output"), Return]
            style "menu_choice_button" xmaximum 120
            text "Exit" at truecenter size 16


screen crafting_screen_output(recipe):
    add recipe.output.fullimg xanchor (0.5) align (0.63,0.15) at menu_top
    frame anchor (0.5,0,0) pos (0.63,0.5) xysize (600,200) padding (10,10) at menu_bottom:
        background Solid("#000000CC")
        has vbox:
            xfill True
        text "{}".format(recipe.output.name) style "item_name" size 26 at center
        text "{size=18}" + "({} in inventory)".format(Inventory.has_item(recipe.output)) + "{/size}" at center
        null height 15
        text "{}".format(recipe.output.description) size 22 at center
        null height 15
        text "Requires: {}".format(crafting_get_components(recipe)) size 18 at center
    frame anchor (0.5,0,0) pos (0.63,0.75) xysize (600,100) padding (10,10) at menu_bottom:
        background Solid("#000000CC")
        has vbox:
            xfill True
        text "In inventory: {}".format(crafting_get_inventory(recipe)) size 18 at center
        null height 20
        if crafting_get_amount(recipe) > 0:
            hbox:
                spacing 20
                xalign 0.5
                text "Craftable: {}".format(crafting_get_amount(recipe)) size 18
        else:
            hbox:
                spacing 20
                xalign 0.5
                text "Not enough materials" size 18 color "#FF0000" at center


screen crafting_screen_confirm(recipe):
    modal True
    frame anchor (0.5,0,0) pos (0.63,0.75) xysize (600,100) padding (10,10) at menu_bottom:
        background Solid("#000000")
        text "Craftable: {}".format(crafting_get_amount(recipe)) size 18 anchor (0.5,0.5) pos (0.5,0.1)
        button anchor (0.5,0.5) pos (0.1,0.5):
            style "menu_choice_button" xmaximum 120
            text "Cancel" at truecenter size 16
            clicked Hide("crafting_screen_confirm")
        button align (0.5,0.5):
            style "menu_choice_button" xmaximum 120
            text "Craft" at truecenter size 16
            if recipe == Rroyalgold and crafting_royal_gold_locked == True:
                clicked Function(crafting_craft, recipe=recipe)
            else:
                clicked [Show("crafting_screen_crafted", recipe=recipe), Function(crafting_craft, recipe=recipe)]


screen crafting_screen_crafted(recipe):
    frame anchor (0.5,0,0) pos (0.63,0.05) xysize (600,50) padding (10,10) at menu_top:
        background Solid("#000000CC")
        if recipe == "None":
            text "Not enough materials to craft." color "#FF0000" at center
        else:
            text "Crafted a {}!".format(recipe.output.name) at center
    timer 2.0 action Hide("crafting_screen_crafted")


init -1 python:
    def crafting_get_components(recipe):
        components = ""
        for i in range(0,len(recipe.components)):
            components = components + "{} x{}".format(recipe.components[i][0].name, recipe.components[i][1])
            if (i+1) < len(recipe.components):
                components = components + ", "
        return (components)

    def crafting_get_amount(recipe):
        amount = 0
        craftable = "None"
        for i in range(0,len(recipe.components)):
            amount = (Inventory.has_item(recipe.components[i][0]) / recipe.components[i][1])
            if craftable == "None":
                craftable = amount
            elif amount < craftable:
                craftable = amount
        return (craftable)

    def crafting_get_inventory(recipe):
        in_inventory = ""
        for i in range(0,len(recipe.components)):
            if Inventory.has_item(recipe.components[i][0]) >= recipe.components[i][1]:
                in_inventory = in_inventory + "{} x{}".format(recipe.components[i][0].name, Inventory.has_item(recipe.components[i][0]))
            else:
                in_inventory = in_inventory + "{color=#FF0000}" + "{} x{}".format(recipe.components[i][0].name, Inventory.has_item(recipe.components[i][0])) + "{/color}"
            if (i+1) < len(recipe.components):
                in_inventory = in_inventory + ", "
        return (in_inventory)

    def crafting_craft(recipe):
        global crafting_royal_gold_locked
        if recipe == Rroyalgold:
            if crafting_royal_gold_locked == True:
                renpy.call_in_new_context("royal_gold_locked")
                return
            else:
                crafting_royal_gold_locked = True
        for i in range(0,len(recipe.components)):
            Inventory.rem_item(recipe.components[i][0], recipe.components[i][1])
        Inventory.add_item(recipe.output)
        if crafting_get_amount(recipe) <= 0:
            renpy.hide_screen("crafting_screen_confirm")
        return


label royal_gold_locked:
    $ Sabia.face = "closed2"
    $ renpy.show(Sabia.objname, at_list=[actor_left])
    $ renpy.say(None, "(It'd just be a waste of ingredients, I don't need another Royal Gold for now.)")
    $ Sabia.face = "normal"
    return







label gallery:
    $ renpy.block_rollback()
    if gallery_workaround == False:
        $ startskills("Database/skills.tsv")
        $ startequipments("Database/equipments.tsv")
        $ startactors("Database/actors.tsv")
        $ startgallery("Database/gallery.tsv")
        $ gallery_workaround = True
    scene bg black
    $ catgirlscaptured = 999
    $ dom = 999
    $ sub = 999
    $ orcbarbeatdown = False
    $ gallery_picked = gallery_scenes_all
    call screen gallery
    $ gallery_workaround = False
    pause(0.23)
    $ renpy.full_restart()


screen gallery tag menu:
    key "game_menu" action [Hide("gallery"), Hide("gallery_description"), Return]

    add Solid("#000000CC")
    text "Scenes Gallery" align (0.5,0.01) size 50 style "item_name"
    use gallery_thumbs
    frame anchor (0.0,0.0) align (0.03,0.1) padding (5,5) xsize (150) ymaximum (545) at menu_left:
        background Solid("#a8a8a8CC")
        has viewport:
            scrollbars "vertical"
            mousewheel True
        vbox:
            xfill True
            button:
                clicked SetVariable("gallery_picked", gallery_scenes_all)
                style "menu_choice_button" xfill True
                text "All" style "item_name" at truecenter size 16
            for i in range(0,len(gallery_scenes_characters)):
                if gallery_scenes_characters[i] not in gallery_scenes_skip:
                    button:
                        clicked SetVariable("gallery_picked", globals()["gallery_scenes_{}".format(gallery_scenes_characters[i])])
                        style "menu_choice_button" xfill True
                        text "{}".format(gallery_scenes_characters[i]) style "item_name" at truecenter size 16
            button:
                clicked SetVariable("gallery_picked", gallery_scenes_Misc)
                style "menu_choice_button" xfill True
                text "Misc" style "item_name" at truecenter size 16
            button:
                clicked [Hide("gallery"), Hide("gallery_description"), Return]
                style "menu_choice_button" xfill True
                text "Exit" style "item_name" at truecenter size 16



screen gallery_thumbs:
    frame anchor (1.0,0,0) align (0.97,0.1) padding (5,5) xysize (841,545) at menu_right:
        background Solid("#a8a8a8CC")
        has vpgrid:
            yfill True
            cols 7
            spacing 5
            scrollbars "vertical"
            mousewheel True
        for i in range(0,len(gallery_picked)):
            if renpy.seen_label(gallery_picked[i]):
                button:
                    padding (0,0)
                    xysize (113,85)
                    background None
                    hover_foreground "scenes/thumbnails/highlight.png"
                    add "scenes/thumbnails/{} thumb.jpg".format(gallery_picked[i])
                    hovered Show("gallery_description", picked=gallery_picked[i])
                    clicked [Hide("gallery_description"), Jump(gallery_picked[i])]
            else:
                button:
                    padding (0,0)
                    xysize (113,85)
                    background None
                    hover_foreground "scenes/thumbnails/highlight.png"
                    add "scenes/thumbnails/{} thumb.jpg".format(gallery_picked[i]) alpha 0.2
                    add "system/locked.png" align (0.5,0.5)
                    hovered Show("gallery_description", picked=gallery_picked[i])
                    clicked NullAction()

init -1 python:
    def startgallery(filename):
        global gallery_scenes
        global gallery_scenes_characters
        global gallery_scenes_all
        gallery_scenes = []
        gallery_scenes_characters = []
        gallery_scenes_all = []
        with renpy.file(filename) as sceneslist:
            for line in sceneslist:
                line = line.decode("utf-8")
                data = line.rstrip().split("\t")
                if data == "" or data[0][0] == "#": continue
                gallery_scenes.append([data[0], data[1], data[2], data[3]])
                gallery_scenes_all.append(data[0])
                for i in range(0,len(data[1].split(","))):
                    try:
                        globals()["gallery_scenes_{}".format(data[1].split(",")[i].split()[0])]
                    except KeyError:
                        globals()["gallery_scenes_{}".format(data[1].split(",")[i].split()[0])] = []
                    if data[0] not in globals()["gallery_scenes_{}".format(data[1].split(",")[i].split()[0])]:
                        globals()["gallery_scenes_{}".format(data[1].split(",")[i].split()[0])].append(data[0])
                    if data[1].split(",")[i].split()[0] not in gallery_scenes_characters:
                        gallery_scenes_characters.append(data[1].split(",")[i].split()[0])


    def scene_characters(picked):
        for i in range(0,len(gallery_scenes)):
            if gallery_scenes[i][0] == picked:
                return(gallery_scenes[i][1])


    def scene_description(picked):
        for i in range(0,len(gallery_scenes)):
            if gallery_scenes[i][0] == picked:
                return(gallery_scenes[i][2])

    def hint_description(picked):
        for i in range(0,len(gallery_scenes)):
            if gallery_scenes[i][0] == picked:
                return(gallery_scenes[i][3])


screen gallery_description(picked):
    frame anchor (1.0,0.0) align (0.97,0.8) padding (5,5) xysize (841,120) at menu_bottom:
        background Solid("#a8a8a8CC")
        has vbox:
            xfill True
            yfill True
        if renpy.seen_label(picked):
            text "{u}Characters{/u}: " + "{}".format(scene_characters(picked))
            text "{}".format(scene_description(picked))
        else:
            text "{image=scenelocked} Scene Locked {image=scenelocked}" size 36 anchor (0.5,0.0) pos (0.5,0.05)
            text "{u}Hint{/u}: " + "{}".format(hint_description(picked)) size 16
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
