






init -1:
    default enemy_level = 0
    default enemy_maxhp = 0
    default enemy_hp = 0
    default enemy_attack = 0
    default enemy_defense = 0
    default enemy_magdefense = 0
    default enemy_type = 0
    default enemy_skills = []
    default player = ""
    default enemy = ""
    default duel_turn = ""
    default duel_damage = 0
    default duel_text = ""
    default duel_xp = 0
    default attacker = ""
    default defender = ""
    default defender_guard = 0
    default duel_momentum = 0
    default duel_enemy_action = ""
    default duel_dot_damage = 0

label duel:
    $ renpy.block_rollback()
    $ enemy.level = enemy_level
    $ enemy.maxhp = enemy_maxhp
    $ enemy.hp = enemy_hp
    $ enemy.ep = 0
    $ enemy.set_str(enemy_attack)
    $ enemy.set_con(enemy_defense)
    $ enemy.set_res(enemy_magdefense)
    if enemy_skills != []:
        $ enemy.actives.extend(enemy_skills)
    play music battle fadeout 2.0 fadein 2.0
    $ clearactors()
    show backdropF
    $ renpy.show(player.objname, at_list=[actor_left])
    $ renpy.show(enemy.objname, at_list=[actor_right])
    show screen duel(player, enemy)
    $ duel_turn = player
    $ duel_momentum = 5
    while player.hp > 0 and enemy.hp > 0:
        if duel_turn == enemy:
            $ attacker = enemy
            $ defender = player
            if enemy.ep >= 7 and duel_momentum <= 7 and enemy.has_debuff("No Crit") == 0:
                $ duel_use_skill(skill=Criticalhit)
            else:
                $ duel_enemy_action = duel_enemy_skill(enemy)
                if duel_enemy_action == "Consumable":
                    pass
                else:
                    $ duel_use_skill(skill=duel_enemy_action)
            show screen duel_damage_pop
            pause (2.1)
        else:
            $ attacker = player
            $ defender = enemy
            call screen duel_player_menu(player=player)
            show screen duel_damage_pop
            pause (2.1)
    hide screen duel
    hide screen duel_damage_pop
    $ player.ep = 0
    $ player.stance = "Normal"
    $ player.buffs = []
    $ player.debuffs = []
    $ enemy.ep = 0
    $ enemy.stance = "Normal"
    $ enemy.buffs = []
    $ enemy.debuffs = []
    $ EnemyInv.items = []
    if enemy.hp <= 0:
        $ duel_xp = enemy.level - player.level
        if duel_xp < 0:
            $ duel_xp = 0
        "[player.name] wins! Gained [duel_xp] XP!"
        $ player.xp += duel_xp
        $ clearactors()
        $ enemy.unequip(enemy.weapon)
        return ("Victory")
    else:
        "[player.name] is defeated!"
        $ clearactors()
        $ enemy.unequip(enemy.weapon)
        return ("Defeat")


screen duel(player, enemy):
    frame align (0.01,0.01) xysize (240,111) padding (20,10) at menu_left:
        background Frame("battle/frame.png")
        has vbox
        text "[player.name]" size 16
        bar:
            style "bar_hp"
            xmaximum 130
            value player.hp
            range player.maxhp
            left_gutter 0
            right_gutter 0
            thumb None
            thumb_shadow None
        text " [player.hp] / [player.maxhp]" size 16 line_leading -20 ypos -7
        null height 5
        bar:
            style "bar_ep"
            xmaximum 130
            value player.ep
            range player.maxep
            left_gutter 0
            right_gutter 0
            thumb None
            thumb_shadow None
        text " [player.ep] / [player.maxep]" size 16 line_leading -20 ypos -6

    frame align (0.16,0.01) xysize (80,111) padding (5,10) at menu_left:
        background None
        null height 20
        text "Stance: [player.stance]" size 12 ypos 0.2

    vbox anchor (0.0,0.0) pos (0.01,0.15) at menu_left:
        if player.buffs != []:
            frame xsize (130) padding (5,5):
                background Solid("#000000CC")
                has vbox
                text "{color=#00FF00}BUFFS:{/color}" size 14
                for i in range(0,len(player.buffs)):
                    text "{}: {} turns".format(player.buffs[i][0], player.buffs[i][1]) size 12

        if player.debuffs != []:
            frame xsize (130) padding (5,5):
                background Solid("#000000CC")
                has vbox
                text "{color=#FF0000}DEBUFFS:{/color}" size 14
                for i in range(0,len(player.debuffs)):
                    text "{}: {} turns".format(player.debuffs[i][0], player.debuffs[i][1]) size 12

    frame align (0.99,0.01) xysize (240,111) padding (20,10) at menu_right:
        background Frame("battle/frame.png")
        has vbox
        text "[enemy.name]" size 16
        bar:
            style "bar_hp"
            xmaximum 130
            value enemy.hp
            range enemy.maxhp
            left_gutter 0
            right_gutter 0
            thumb None
            thumb_shadow None
        text " [enemy.hp] / [enemy.maxhp]" size 16 line_leading -20 ypos -7
        null height 5
        bar:
            style "bar_ep"
            xmaximum 130
            value enemy.ep
            range enemy.maxep
            left_gutter 0
            right_gutter 0
            thumb None
            thumb_shadow None
        text " [enemy.ep] / [enemy.maxep]" size 16 line_leading -20 ypos -6

    frame align (0.99,0.01) xysize (80,111) padding (5,10) at menu_right:
        background None
        text "Stance: [enemy.stance]" size 12 ypos 0.2

    vbox anchor (1.0,0.0) pos (0.99,0.15) at menu_right:
        if enemy.buffs != []:
            frame xsize (130) padding (5,5):
                background Solid("#000000CC")
                has vbox
                text "{color=#00FF00}BUFFS:{/color}" size 14
                for i in range(0,len(enemy.buffs)):
                    text "{}: {} turns".format(enemy.buffs[i][0], enemy.buffs[i][1]) size 12

        if enemy.debuffs != []:
            frame xsize (130) padding (5,5):
                background Solid("#000000CC")
                has vbox
                text "{color=#FF0000}DEBUFFS:{/color}" size 14
                for i in range(0,len(enemy.debuffs)):
                    text "{}: {} turns".format(enemy.debuffs[i][0], enemy.debuffs[i][1]) size 12

    frame align (0.5,0.02) xanchor (0.5) padding (0,0) at menu_top:
        foreground "battle/mbg.png"
        has vbox
        bar:
            value duel_momentum
            range 10
            xysize (480,25)
            left_bar Frame("battle/mleft.png")
            right_bar Frame("battle/mright.png")
            left_gutter 0
            right_gutter 0
            thumb None
            thumb_offset 0





screen duel_player_menu(player):
    frame align (0.5,0.5) padding (-1,-1):

        background None
        xsize 230
        has vbox:
            spacing 1
            xalign 0.5
        button:
            xalign (0.5)
            style "menu_choice_button" xfill True
            text "Attack" at truecenter size 16
            clicked [Function(duel_use_skill, skill=Attack), Hide("duel_player_menu_description"), Return]
            hovered Show("duel_player_menu_description", skill=Attack)
            unhovered Hide("duel_player_menu_description")

        button:
            xalign (0.5)
            text "Quick Attack" at truecenter size 16
            if ((player.ep + Quickattack.ep) >= 0) and ((duel_momentum + Quickattack.momentum) >= 0):
                style "menu_choice_button" xfill True
                clicked [Function(duel_use_skill, skill=Quickattack), Hide("duel_player_menu_description"), Return]
            else:
                xfill True
                clicked NullAction()
            hovered Show("duel_player_menu_description", skill=Quickattack)
            unhovered Hide("duel_player_menu_description")

        button:
            xalign (0.5)
            if player.has_debuff("No Crit") > 0:
                text "Critical Hit {color=#FF0000}(Disabled){/color}" at truecenter size 16
                xfill True
                clicked NullAction()
            else:
                text "Critical Hit" at truecenter size 16
                if ((player.ep + Criticalhit.ep) >= 0) and ((duel_momentum + Criticalhit.momentum) >= 0):
                    style "menu_choice_button" xfill True
                    clicked [Function(duel_use_skill, skill=Criticalhit), Hide("duel_player_menu_description"), Return]
                else:
                    xfill True
                    clicked NullAction()
            hovered Show("duel_player_menu_description", skill=Criticalhit)
            unhovered Hide("duel_player_menu_description")

        for i in range(0,len(player.actives)):
            if (player.actives[i] == Preparation) and (player.stance == "Prepared"):
                pass
            elif (player.actives[i].stance == "Normal") or (player.actives[i].stance == player.stance):
                button:
                    xalign (0.5)
                    text "{}".format(player.actives[i].name) at truecenter size 16
                    if ((player.ep + player.actives[i].ep) >= 0) and ((duel_momentum + player.actives[i].momentum) >= 0):
                        style "menu_choice_button" xfill True
                        clicked [Function(duel_use_skill, skill=player.actives[i]), Hide("duel_player_menu_description"), Return]
                    else:
                        xfill True
                        clicked NullAction()
                    hovered Show("duel_player_menu_description", skill=player.actives[i])
                    unhovered Hide("duel_player_menu_description")

        button:
            xalign (0.5)
            if player.has_debuff("Guard Break") > 0:
                text "Guard {color=#FF0000}(Disabled){/color}" at truecenter size 16
                xfill True
                clicked NullAction()
            else:
                style "menu_choice_button" xfill True
                text "Guard" at truecenter size 16
                clicked [Function(duel_use_skill, skill=Guard), Hide("duel_player_menu_description"), Return]
            hovered Show("duel_player_menu_description", skill=Guard)
            unhovered Hide("duel_player_menu_description")

        button:
            xalign (0.5)
            style "menu_choice_button" xfill True
            text "Use a consumable" at truecenter size 16
            clicked [Show("duel_items"), Hide("duel_player_menu")]


screen duel_player_menu_description(skill):
    frame pos (0.5,0.7) anchor (0.5,0.0) xsize (580) padding (5,5) at menu_bottom:
        background Solid("#000000CC")
        has vbox
        text "{}".format(skill.description)
        hbox:
            spacing 5
            if skill.ep < 0:
                text "Costs EP: {color=#FF0000}[skill.ep]{/color}"
            else:
                text "Generates EP: +{color=#00FF00}[skill.ep]{/color}"
            text "|"
            if skill.momentum < 0:
                text "Costs Momentum: {color=#FF0000}[skill.momentum]{/color}"
            else:
                text "Generates Momentum: +{color=#00FF00}[skill.momentum]{/color}"


screen duel_items:
    frame anchor (0.5,0.5) pos (0.5,0.8) xysize (410,200) padding (5,5) at menu_bottom:
        background Solid("#000000CC")
        vpgrid:
            yfill True
            cols 4
            spacing 5
            scrollbars "vertical"
            mousewheel True
            for i in range(0,len(Inventory.items)):
                if Inventory.items[i][0].consumable == "Yes":
                    button:
                        xysize (90,90)
                        background None
                        hover_background Frame("system/highlight.png")
                        add Inventory.items[i][0].fullimg size (90,90) align (0.5,0.5)
                        $ stockamount = Inventory.items[i][1]
                        text "{b}[stockamount]{/b}" size 14 anchor (1.0,1.0) align (1.1,1.05)
                        hovered Show("duel_items_hover", item=Inventory.items[i][0])
                        unhovered Hide("duel_items_hover")
                        clicked [Function(duel_use_consumable, item=Inventory.items[i][0]), Hide("duel_items"), Hide("duel_items_hover"), Return]

        button:
            anchor (0.0,0.0)
            pos (1.0,0.0)
            style "menu_choice_button" xmaximum 120
            text "Cancel" at truecenter size 16
            action [Hide("duel_items"), Show("duel_player_menu", player=player)]


screen duel_items_hover(item):
    frame anchor (0.5,0.5) pos (0.5,0.6) xysize (400,100) padding (5,5) at menu_bottom:
        background Solid("#000000CC")
        has vbox
        text "[item.name]" size 16
        text "[item.description]" size 16
        text "\nUsing a consumable will cost {color=#FF0000}-2{/color} Momentum" size 14


screen duel_damage_pop:
    frame align (0.5,0.7) xmaximum 580 at menu_bottom:
        background Solid("#000000CC")
        text "[duel_text]" at truecenter
    timer 2.0 action Hide("duel_damage_pop")


init -1 python:



    def duel_use_skill(skill):
        global attacker
        global defender
        global defender_guard
        global duel_turn
        global duel_damage
        global duel_text
        global duel_momentum
        global duel_dot_damage
        duel_damage = 0
        duel_dot_damage = 0
        duel_text = ""
        duel_momentum_boost = 1
        
        
        defender_armor = defender.pdef
        
        
        if skill.formula != "None": 
            
            
            if defender.has_buff("Centered") > 0:
                pass
            elif attacker == player:
                duel_momentum = duel_momentum + skill.momentum
            elif attacker == enemy:
                if skill == Criticalhit:
                    if defender_guard == 0:
                        duel_momentum = duel_momentum - 2
                        duel_text = " A clean critical that swings the momentum heavily in {}'s favor!".format(enemy.name)
                    else: 
                        duel_momentum = duel_momentum + 4
                        duel_text = " {} clashes against {}'s defenses and loses momentum!".format(enemy.name,player.name)
                else:
                    duel_momentum = duel_momentum - skill.momentum
            if duel_momentum > 10:
                duel_momentum = 10
            if duel_momentum < 0:
                duel_momentum = 0
            
            
            
            if attacker.passives:
                for i in range(0,len(attacker.passives)):
                    if renpy.random.randint(0,100) <= attacker.passives[i].variance: 
                        passive_damage = eval(attacker.passives[i].formula)
                        if passive_damage < 0:
                            passive_damage = 0
                        
                        if attacker.passives[i].dtype == "EP":
                            if passive_damage > defender.ep:
                                passive_damage = defender.ep
                            defender.ep -= passive_damage
                            if attacker == player:
                                renpy.show("duel_number_float_ep", at_list=[number_float(0.75)], what=Text("- {}".format(passive_damage), size=34, style="combat_number", color="#0000FF"))
                            else:
                                renpy.show("duel_number_float_ep", at_list=[number_float(0.25)], what=Text("- {}".format(passive_damage), size=34, style="combat_number", color="#0000FF"))
                        
                        
                        if attacker.passives[i].dtype == "ARMOR":
                            defender.pdef -= passive_damage
                            if attacker == player:
                                renpy.show("duel_number_float_armor", at_list=[number_float(0.80)], what=Text("- {}".format(passive_damage), size=34, style="combat_number", color="#808080"))
                            else:
                                renpy.show("duel_number_float_armor", at_list=[number_float(0.20)], what=Text("- {}".format(passive_damage), size=34, style="combat_number", color="#808080"))
                        
                        
                        duel_text = duel_text + " {}".format(attacker.passives[i].text.format(passive_damage))
                        break 
            
            
            if attacker == player:
                if duel_momentum >= 8:
                    renpy.show("duel_momentum_boost", at_list=[momentum_msg(0.25)], what=Text("Momentum boost! Dmg up!", size=34, style="combat_number", color="#FF0000"))
                    duel_momentum_boost = 1.2
                elif duel_momentum <= 2:
                    renpy.show("duel_momentum_boost", at_list=[momentum_msg(0.25)], what=Text("Low Momentum! Dmg down!", size=34, style="combat_number", color="#0000FF"))
                    duel_momentum_boost = 0.8
            elif attacker == enemy:
                if duel_momentum <= 2:
                    renpy.show("duel_momentum_boost", at_list=[momentum_msg(0.75)], what=Text("Momentum boost! Dmg up!", size=34, style="combat_number", color="#FF0000"))
                    duel_momentum_boost = 1.2
                elif duel_momentum >= 8:
                    renpy.show("duel_momentum_boost", at_list=[momentum_msg(0.75)], what=Text("Low Momentum! Dmg down!", size=34, style="combat_number", color="#0000FF"))
                    duel_momentum_boost = 0.8
            
            
            
            duel_damage = eval(skill.formula)
            if duel_damage < 0:
                duel_damage = 0
            duel_damage = round(duel_damage * duel_momentum_boost)
            duel_damage = renpy.random.randint(int(round(duel_damage * (1 - (skill.variance/float(100))))),int(round(duel_damage * (1 + (skill.variance/float(100))))))
            duel_damage = int(round(duel_damage - (duel_damage * float(defender_guard))))
            defender_guard = 0
            if defender.has_buff("Physical Ward") > 0:
                duel_damage = int(round(duel_damage - (duel_damage * float(0.8))))
            
            
            defender.pdef = defender_armor
            
            duel_text = skill.text.format(attacker.name,defender.name) + " {} damage dealt.".format(duel_damage) + duel_text
            
            if skill.dtype == "HP":
                defender.hp -= duel_damage
                if defender.hp < 0:
                    defender.hp = 0
            
            elif skill.dtype == "EP":
                defender.ep -= duel_damage
                if defender.ep < 0:
                    defender.ep = 0
            
            
            elif skill.dtype == "DEBUFF":
                if skill.name == "Interrupting Blow":
                    defender.hp -= duel_damage
                    if defender.hp < 0:
                        defender.hp = 0
                    if defender.stance == "Prepared":
                        defender.stance = "Normal"
                        defender.add_debuff("Stance Lock",1)
                        if attacker == player:
                            duel_momentum += 1
                        else:
                            duel_momentum -= 1
                    defender.ep -= 2
                    if defender.ep < 0:
                        defender.ep = 0
                    duel_text = duel_text + " {} lost 2 EP.".format(defender.name)
                
                elif skill.name == "Disabling Blow":
                    defender.hp -= duel_damage
                    if defender.hp < 0:
                        defender.hp = 0
                    defender.add_debuff("No Crit",3)
                    defender.add_debuff("Guard Break",3)
                    duel_text = duel_text + " {} is afflicted by No Crit and Guard Break.".format(defender.name)
                
                elif skill.name == "Slowing Strike":
                    defender.hp -= duel_damage
                    if defender.hp < 0:
                        defender.hp = 0
                    defender.add_debuff("Atk Down",3)
                    defender.add_debuff("Def Down",3)
                    duel_text = duel_text + " {} is afflicted by Atk Down and Def Down.".format(defender.name)
                
                elif skill.name == "Defense Breaker":
                    defender.hp -= duel_damage
                    if defender.hp < 0:
                        defender.hp = 0
                    defender.add_debuff("Def Down",3)
                    duel_text = duel_text + " {} is afflicted by Def Down.".format(defender.name)
            
            
            
            
            
            if skill.stance != "Normal":
                attacker.stance = "Normal"
            
            if attacker == player:
                renpy.show(defender.objname, at_list=[stagger_actor(10)])
                renpy.show("duel_damage", at_list=[number_bounce(0.65)], what=Text("- {}".format(duel_damage), size=42, style="combat_number", color="#FF0000"))
            elif attacker == enemy:
                renpy.show(defender.objname, at_list=[stagger_actor(-10)])
                renpy.show("duel_damage", at_list=[number_bounce(0.35)], what=Text("- {}".format(duel_damage), size=42, style="combat_number", color="#FF0000"))
        
        
        else: 
            
            duel_text = skill.text.format(attacker.name,defender.name)
            
            if skill == Guard:
                duel_damage = "None"
                if attacker == player:
                    defender_guard = duel_momentum / float(10)
                    renpy.show("duel_guard", at_list=[number_float(0.35)], what=Text("Guard up!", size=42, style="combat_number", color="#DAA520"))
                elif attacker == enemy:
                    defender_guard = (10 - duel_momentum) / float(10)
                    renpy.show("duel_guard", at_list=[number_float(0.65)], what=Text("Guard up!", size=42, style="combat_number", color="#DAA520"))
                if defender_guard > 0.7:
                    defender_guard = 0.7
            
            
            if attacker == player:
                duel_momentum = duel_momentum + skill.momentum
            elif attacker == enemy:
                duel_momentum = duel_momentum - skill.momentum
            if duel_momentum > 10:
                duel_momentum = 10
            if duel_momentum < 0:
                duel_momentum = 0
            
            
            if skill == Preparation:
                attacker.stance = "Prepared"
            
            elif skill == Centering:
                if attacker.has_debuff("Atk Down") > 0:
                    attacker.rem_debuff("Atk Down",99)
                if attacker.has_debuff("Def Down") > 0:
                    attacker.rem_debuff("Def Down",99)
                duel_momentum = 5
                attacker.add_buff("Centered",2)
            
            elif skill == Physicalward:
                duel_damage = "None"
                if attacker == player:
                    renpy.show("duel_guard", at_list=[number_float(0.35)], what=Text("Physical Ward up!", size=42, style="combat_number", color="#DAA520"))
                elif attacker == enemy:
                    renpy.show("duel_guard", at_list=[number_float(0.65)], what=Text("Physical Ward up!", size=42, style="combat_number", color="#DAA520"))
                attacker.add_buff("Physical Ward",1)
        
        if skill.sfx != "None":
            renpy.play(skill.sfx)
        
        if skill == Criticalhit:
            renpy.transition(vpunch)
        
        attacker.ep += skill.ep
        if attacker.ep > attacker.maxep:
            attacker.ep = attacker.maxep
        
        
        
        for i in range(0,len(attacker.debuffs)):
            attacker.rem_debuff(attacker.debuffs[i][0])
            if attacker.debuffs[i][0] == "Bleed":
                duel_dot_damage = duel_dot_damage + 2
        
        
        if duel_dot_damage != 0:
            if attacker == player:
                renpy.show("duel_dot_damage", at_list=[number_bounce(0.35)], what=Text("- {}".format(duel_dot_damage), size=42, style="combat_number", color="#FF0000"))
            elif attacker == enemy:
                renpy.show("duel_dot_damage", at_list=[number_bounce(0.65)], what=Text("- {}".format(duel_dot_damage), size=42, style="combat_number", color="#FF0000"))
            attacker.hp -= duel_dot_damage
            if attacker.hp < 0:
                attacker.hp = 0
            duel_text = duel_text + " {} took [duel_dot_damage] damage due to afflictions.".format(attacker.name)
        
        attacker.debuffs[:] = [debuff for debuff in attacker.debuffs if attacker.has_debuff(debuff[0]) > 0]
        
        
        
        
        
        
        for i in range(0,len(attacker.buffs)):
            attacker.rem_buff(attacker.buffs[i][0])
        
        attacker.buffs[:] = [buff for buff in attacker.buffs if attacker.has_buff(buff[0]) > 0]
        
        
        duel_turn = defender
        
        return







    def duel_use_consumable(item):
        global attacker
        global defender
        global defender_guard
        global duel_turn
        global duel_text
        global duel_momentum
        duel_text = ""
        defender_guard = 0
        duel_turn = defender
        
        if attacker == player:
            duel_momentum = duel_momentum - 2
        else:
            duel_momentum = duel_momentum + 2
        if duel_momentum > 10:
            duel_momentum = 10
        if duel_momentum < 0:
            duel_momentum = 0
        
        if item == Healthpotion:
            duel_text = "{} consumed a Health Potion! {} HP recovered.".format(attacker.name,(attacker.maxhp - attacker.hp))
            if attacker == player:
                Inventory.rem_item(Healthpotion)
                renpy.show("duel_number_float_consumable", at_list=[number_float(0.25)], what=Text("+ {}".format(attacker.maxhp - attacker.hp), size=34, style="combat_number", color="#00FF00"))
            else:
                EnemyInv.rem_item(Healthpotion)
                renpy.show("duel_number_float_consumable", at_list=[number_float(0.75)], what=Text("+ {}".format(attacker.maxhp - attacker.hp), size=34, style="combat_number", color="#00FF00"))
            attacker.hp = attacker.maxhp
        
        if item == Energypotion:
            duel_text = "{} consumed an Energy Potion! {} EP generated.".format(attacker.name,(attacker.maxep - attacker.ep))
            if attacker == player:
                Inventory.rem_item(Energypotion)
                renpy.show("duel_number_float_consumable", at_list=[number_float(0.25)], what=Text("+ {}".format(attacker.maxep - attacker.ep), size=34, style="combat_number", color="#0000FF"))
            else:
                EnemyInv.rem_item(Energypotion)
                renpy.show("duel_number_float_consumable", at_list=[number_float(0.75)], what=Text("+ {}".format(attacker.maxep - attacker.ep), size=34, style="combat_number", color="#0000FF"))
            attacker.ep = attacker.maxep
        
        return







    def duel_enemy_skill(enemy):
        global enemy_type
        global duel_momentum
        
        
        if enemy_type == 1:
            while True:
                duel_enemy_use_skill = renpy.random.choice(enemy.actives)
                if enemy.ep + duel_enemy_use_skill.ep >= 0 and (10 - duel_momentum) + duel_enemy_use_skill.momentum >= 0:
                    return(duel_enemy_use_skill)
        
        
        elif enemy_type == 2:
            if enemy.stance == "Normal" and enemy.has_debuff("Stance Lock") == 0:  
                for i in range(0,len(enemy.actives)):
                    if enemy.actives[i].dtype == "STANCE":
                        duel_enemy_use_skill = enemy.actives[i]
                        if enemy.ep + duel_enemy_use_skill.ep >= 0 and (10 - duel_momentum) + duel_enemy_use_skill.momentum >= 0:
                            return(duel_enemy_use_skill)
            
            elif enemy.stance != "Normal": 
                for i in range(0,len(enemy.actives)): 
                    if enemy.actives[i].stance == enemy.stance and enemy.actives[i].dtype != "STANCE":
                        duel_enemy_use_skill = enemy.actives[i]
                        if enemy.ep + duel_enemy_use_skill.ep >= 0 and (10 - duel_momentum) + duel_enemy_use_skill.momentum >= 0:
                            return(duel_enemy_use_skill)
            
            while True: 
                duel_enemy_use_skill = renpy.random.choice(enemy.actives)
                if duel_enemy_use_skill.stance == "Normal" and duel_enemy_use_skill.dtype != "STANCE":
                    if enemy.ep + duel_enemy_use_skill.ep >= 0 and (10 - duel_momentum) + duel_enemy_use_skill.momentum >= 0:
                        return(duel_enemy_use_skill)
        
        
        elif enemy_type == 3:
            if enemy.has_buff("Physical Ward") == 0:
                return(Carefulblow)
            else:
                return(Physicalward)
        
        
        elif enemy_type == 99:
            
            if enemy.hp <= (enemy.maxhp / 2) and EnemyInv.has_item(Healthpotion) > 0:
                duel_use_consumable(Healthpotion)
                return("Consumable")
            
            
            elif duel_momentum >= 6 and enemy.ep >=3: 
                return(Quickattack)
            
            
            elif player.has_debuff("No Crit") == 0 or player.has_debuff("Guard Break") == 0:
                return(Disablingblow)
            
            
            elif player.has_debuff("Atk Down") == 0 or player.has_debuff("Def Down") == 0:
                return(Slowingstrike)
            
            
            elif duel_momentum <= 2:
                return(Enemyenchantedattack)
            
            
            elif enemy.ep >= 3 and duel_momentum <= 8:
                return(Guard)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
