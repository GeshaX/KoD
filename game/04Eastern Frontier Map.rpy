


style map_desc:
    outlines [(3, "#000000")]

init -1:
    default ef_forest2_unlocked = False
    default ef_forest_ruin_unlocked = False
    default ef_grove_unlocked = False
    default ef_rogue_orc_camp_unlocked = False

    transform map_top:
        on show:
            yoffset -50 alpha 0.0
            easein 0.25 yoffset 0 alpha 1.0

    transform pink_arrow:
        "/maps/Arrows/1.png"
        pause 0.1
        "/maps/Arrows/2.png"
        pause 0.1
        "/maps/Arrows/3.png"
        pause 0.1
        "/maps/Arrows/4.png"
        pause 0.1
        "/maps/Arrows/5.png"
        pause 0.1
        "/maps/Arrows/4.png"
        pause 0.1
        "/maps/Arrows/3.png"
        pause 0.1
        "/maps/Arrows/2.png"
        pause 0.1
        "/maps/Arrows/1.png"
        pause 0.1
        repeat

    image animated_pink_arrow:
        contains pink_arrow

    transform blue_arrow:
        "/maps/Arrows/1a.png"
        pause 0.1
        "/maps/Arrows/2a.png"
        pause 0.1
        "/maps/Arrows/3a.png"
        pause 0.1
        "/maps/Arrows/4a.png"
        pause 0.1
        "/maps/Arrows/5a.png"
        pause 0.1
        "/maps/Arrows/4a.png"
        pause 0.1
        "/maps/Arrows/3a.png"
        pause 0.1
        "/maps/Arrows/2a.png"
        pause 0.1
        "/maps/Arrows/1a.png"
        pause 0.1
        repeat

    image animated_blue_arrow:
        contains blue_arrow


label eastern_frontier_map:
    scene bg black
    $ renpy.choice_for_skipping()
    while True:
        if orccampphase == 1:
            show screen eastern_frontier_phase1
        elif orccampphase == 2:
            show screen eastern_frontier
        elif orccampphase == 3:
            show screen eastern_frontier_phase3
        $ renpy.pause(hard=True)


screen eastern_frontier_phase1:
    $ renpy.block_rollback()
    add "maps/EasternFrontier/map clean.jpg"
    imagebutton auto "maps/EasternFrontier/Locked/Abandoned Mine_%s.png" action NullAction() anchor (0.5,0.5) pos (188,517) focus_mask True
    imagebutton auto "maps/EasternFrontier/Locked/Abandoned Stronghold_%s.png" action NullAction() anchor (0.5,0.5) pos (62,489) focus_mask True
    imagebutton auto "maps/EasternFrontier/Locked/Ancient ruins_%s.png" action NullAction() anchor (0.5,0.5) pos (295,722) focus_mask True
    imagebutton auto "maps/EasternFrontier/Locked/Arwan Lands_%s.png" action NullAction() anchor (0.5,0.5) pos (1039,173) focus_mask True
    imagebutton auto "maps/EasternFrontier/Locked/Avarton_%s.png" action NullAction() anchor (0.5,0.5) pos (388,143) focus_mask True
    imagebutton auto "maps/EasternFrontier/Locked/Bal og Dar_%s.png" action NullAction() anchor (0.5,0.5) pos (905,400) focus_mask True
    imagebutton auto "maps/EasternFrontier/Locked/Bariton_%s.png" action NullAction() anchor (0.5,0.5) pos (582,58) focus_mask True
    imagebutton auto "maps/EasternFrontier/Locked/Bariton Village_%s.png" action NullAction() anchor (0.5,0.5) pos (508,204) focus_mask True

    imagebutton auto "maps/EasternFrontier/Camp Outskirts_%s.png" anchor (0.5,0.5) pos (388,539) focus_mask True:
        action [Hide("eastern_frontier_phase1"), Jump("orcoutskirts1")]

    imagebutton auto "maps/EasternFrontier/Locked/Cardock_%s.png" action NullAction() anchor (0.5,0.5) pos (735,756) focus_mask True
    imagebutton auto "maps/EasternFrontier/Locked/Council Settlement_%s.png" action NullAction() anchor (0.5,0.5) pos (65,727) focus_mask True
    imagebutton auto "maps/EasternFrontier/Locked/Ellaek_%s.png" action NullAction() anchor (0.5,0.5) pos (715,95) focus_mask True
    imagebutton auto "maps/EasternFrontier/Locked/Escraenen_%s.png" action NullAction() anchor (0.5,0.5) pos (890,164) focus_mask True
    imagebutton auto "maps/EasternFrontier/Locked/Esk og Dar_%s.png" action NullAction() anchor (0.5,0.5) pos (928,638) focus_mask True
    imagebutton auto "maps/EasternFrontier/Locked/Eskan Village_%s.png" action NullAction() anchor (0.5,0.5) pos (721,418) focus_mask True
    imagebutton auto "maps/EasternFrontier/Locked/Eskan Village_%s.png" action NullAction() anchor (0.5,0.5) pos (802,480) focus_mask True
    imagebutton auto "maps/EasternFrontier/Locked/Eskan Village_%s.png" action NullAction() anchor (0.5,0.5) pos (799,640) focus_mask True
    imagebutton auto "maps/EasternFrontier/Locked/Forest_%s.png" action NullAction() anchor (0.5,0.5) pos (274,381) focus_mask True

    imagebutton anchor (0.5,0.5) pos (307,615) focus_mask True:
        if ef_forest2_unlocked == False:
            auto "maps/EasternFrontier/Locked/Forest2_%s.png"
            action NullAction()
        else:
            auto "maps/EasternFrontier/Forest2_%s.png"
            action [Hide("eastern_frontier_phase1"), Jump("ef_forest2")]

    imagebutton auto "maps/EasternFrontier/Locked/Forest Ruin_%s.png" action NullAction() anchor (0.5,0.5) pos (621,313) focus_mask True
    imagebutton auto "maps/EasternFrontier/Locked/Frontier Farm_%s.png" action NullAction() anchor (0.5,0.5) pos (390,324) focus_mask True
    imagebutton auto "maps/EasternFrontier/Locked/Frontier Village_%s.png" action NullAction() anchor (0.5,0.5) pos (314,310) focus_mask True

    imagebutton auto "maps/EasternFrontier/Grok og Dar_%s.png" anchor (0.5,0.5) pos (481,596) focus_mask True:
        action [Hide("eastern_frontier_phase1"), Jump("lowerorccamp")]

    imagebutton auto "maps/EasternFrontier/Locked/Grove_%s.png" action NullAction() anchor (0.5,0.5) pos (433,786) focus_mask True
    imagebutton auto "maps/EasternFrontier/Locked/Lundari Farm_%s.png" action NullAction() anchor (0.5,0.5) pos (61,209) focus_mask True
    imagebutton auto "maps/EasternFrontier/Locked/Maelton_%s.png" action NullAction() anchor (0.5,0.5) pos (615,186) focus_mask True
    imagebutton auto "maps/EasternFrontier/Locked/Mhanenvale_%s.png" action NullAction() anchor (0.5,0.5) pos (840,33) focus_mask True

    imagebutton anchor (0.5,0.5) pos (922,749) focus_mask True:
        auto "maps/EasternFrontier/Locked/Mountains_%s.png"
        action NullAction()

    imagebutton anchor (0.5,0.5) pos (349,426) focus_mask True:
        if ef_mountains1_unlocked == True:
            auto "maps/EasternFrontier/Mountains1_%s.png"
            action [Hide("eastern_frontier_phase1"), Jump("ef_mountains_phase1")]
        else:
            auto "maps/EasternFrontier/Locked/Mountains1_%s.png"
            action NullAction()


    imagebutton auto "maps/EasternFrontier/Locked/Mountains2_%s.png" action NullAction() anchor (0.5,0.5) pos (896,264) focus_mask True
    imagebutton auto "maps/EasternFrontier/Locked/Mountain Caves_%s.png" action NullAction() anchor (0.5,0.5) pos (493,279) focus_mask True
    imagebutton auto "maps/EasternFrontier/Locked/Mountain Tower_%s.png" action NullAction() anchor (0.5,0.5) pos (808,308) focus_mask True
    imagebutton auto "maps/EasternFrontier/Locked/Independent Village_%s.png" action NullAction() anchor (0.5,0.5) pos (168,374) focus_mask True
    imagebutton auto "maps/EasternFrontier/Locked/Independent Village_%s.png" action NullAction() anchor (0.5,0.5) pos (236,460) focus_mask True
    imagebutton auto "maps/EasternFrontier/Locked/Quadran Village_%s.png" action NullAction() anchor (0.5,0.5) pos (771,52) focus_mask True
    imagebutton auto "maps/EasternFrontier/Locked/Quadran Village_%s.png" action NullAction() anchor (0.5,0.5) pos (765,200) focus_mask True
    imagebutton auto "maps/EasternFrontier/Locked/Quadran Village_%s.png" action NullAction() anchor (0.5,0.5) pos (727,287) focus_mask True
    imagebutton auto "maps/EasternFrontier/Locked/Remote Ruins_%s.png" action NullAction() anchor (0.5,0.5) pos (653,515) focus_mask True
    imagebutton auto "maps/EasternFrontier/Locked/Riverside Ruins_%s.png" action NullAction() anchor (0.5,0.5) pos (904,519) focus_mask True
    imagebutton auto "maps/EasternFrontier/Locked/Rogue Orc Camp_%s.png" action NullAction() anchor (0.5,0.5) pos (443,385) focus_mask True
    imagebutton auto "maps/EasternFrontier/Locked/Shamanic Village_%s.png" action NullAction() anchor (0.5,0.5) pos (140,664) focus_mask True
    imagebutton auto "maps/EasternFrontier/Locked/Sorthyos Lake_%s.png" action NullAction() anchor (0.5,0.5) pos (478,462) focus_mask True
    imagebutton auto "maps/EasternFrontier/Locked/Sothen Bridge_%s.png" action NullAction() anchor (0.5,0.5) pos (202,612) focus_mask True
    imagebutton auto "maps/EasternFrontier/Locked/Vegardan Lands_%s.png" action NullAction() anchor (0.5,0.5) pos (1057,554) focus_mask True
    imagebutton auto "maps/EasternFrontier/Locked/Weaving Caverns_%s.png" action NullAction() anchor (0.5,0.5) pos (571,738) focus_mask True
    imagebutton auto "maps/EasternFrontier/Locked/Whitecrest_%s.png" action NullAction() anchor (0.5,0.5) pos (232,79) focus_mask True
    imagebutton auto "maps/EasternFrontier/Locked/Whitecrest Village_%s.png" action NullAction() anchor (0.5,0.5) pos (170,242) focus_mask True
    imagebutton auto "maps/EasternFrontier/Locked/Whitecrest Village_%s.png" action NullAction() anchor (0.5,0.5) pos (252,174) focus_mask True
    imagebutton auto "maps/EasternFrontier/Locked/Whitewater Pass_%s.png" action NullAction() anchor (0.5,0.5) pos (283,246) focus_mask True


screen eastern_frontier:
    $ renpy.block_rollback()
    add "maps/EasternFrontier/map clean.jpg"


    imagebutton anchor (0.5,0.5) pos (188,517) focus_mask True:
        auto "maps/EasternFrontier/Abandoned Mine_%s.png"
        action [Hide("eastern_frontier"), Jump("ef_abandoned_mine")]

    imagebutton anchor (0.5,0.5) pos (62,489) focus_mask True:
        auto "maps/EasternFrontier/Locked/Abandoned Stronghold_%s.png"
        action NullAction()

    imagebutton anchor (0.5,0.5) pos (295,722) focus_mask True:
        auto "maps/EasternFrontier/Locked/Ancient ruins_%s.png"
        action NullAction()

    imagebutton anchor (0.5,0.5) pos (1039,173) focus_mask True:
        auto "maps/EasternFrontier/Locked/Arwan Lands_%s.png"
        action NullAction()

    imagebutton anchor (0.5,0.5) pos (388,143) focus_mask True:
        auto "maps/EasternFrontier/Locked/Avarton_%s.png"
        action NullAction()

    imagebutton anchor (0.5,0.5) pos (905,400) focus_mask True:
        auto "maps/EasternFrontier/Locked/Bal og Dar_%s.png"
        action NullAction()

    imagebutton anchor (0.5,0.5) pos (582,58) focus_mask True:
        auto "maps/EasternFrontier/Locked/Bariton_%s.png"
        action NullAction()

    imagebutton anchor (0.5,0.5) pos (508,204) focus_mask True:
        auto "maps/EasternFrontier/Locked/Bariton Village_%s.png"
        action NullAction()


    imagebutton auto "maps/EasternFrontier/Camp Outskirts_%s.png" anchor (0.5,0.5) pos (388,539) focus_mask True:
        action [Hide("eastern_frontier"), Jump("orcoutskirts2")]

    imagebutton anchor (0.5,0.5) pos (735,756) focus_mask True:
        auto "maps/EasternFrontier/Locked/Cardock_%s.png"
        action NullAction()

    imagebutton anchor (0.5,0.5) pos (65,727) focus_mask True:
        auto "maps/EasternFrontier/Locked/Council Settlement_%s.png"
        action NullAction()

    imagebutton anchor (0.5,0.5) pos (715,95) focus_mask True:
        auto "maps/EasternFrontier/Locked/Ellaek_%s.png"
        action NullAction()

    imagebutton anchor (0.5,0.5) pos (890,164) focus_mask True:
        auto "maps/EasternFrontier/Locked/Escraenen_%s.png"
        action NullAction()

    imagebutton anchor (0.5,0.5) pos (928,638) focus_mask True:
        auto "maps/EasternFrontier/Locked/Esk og Dar_%s.png"
        action NullAction()

    imagebutton anchor (0.5,0.5) pos (721,418) focus_mask True:
        auto "maps/EasternFrontier/Locked/Eskan Village_%s.png"
        action NullAction()

    imagebutton anchor (0.5,0.5) pos (802,480) focus_mask True:
        auto "maps/EasternFrontier/Locked/Eskan Village_%s.png"
        action NullAction()

    imagebutton anchor (0.5,0.5) pos (799,640) focus_mask True:
        auto "maps/EasternFrontier/Locked/Eskan Village_%s.png"
        action NullAction()

    imagebutton anchor (0.5,0.5) pos (274,381) focus_mask True:
        auto "maps/EasternFrontier/Locked/Forest_%s.png"
        action NullAction()

    imagebutton anchor (0.5,0.5) pos (307,615) focus_mask True:
        if ef_forest2_unlocked == False:
            auto "maps/EasternFrontier/Locked/Forest2_%s.png"
            action NullAction()
        else:
            auto "maps/EasternFrontier/Forest2_%s.png"
            action [Hide("eastern_frontier"), Jump("ef_forest2")]

    imagebutton anchor (0.5,0.5) pos (621,313) focus_mask True:
        if ef_forest_ruin_unlocked == True:
            auto "maps/EasternFrontier/Forest Ruin_%s.png"
            action [Hide("eastern_frontier"), Jump("ef_forest_ruin")]
        else:
            auto "maps/EasternFrontier/Locked/Forest Ruin_%s.png"
            action NullAction()

    imagebutton anchor (0.5,0.5) pos (390,324) focus_mask True:
        auto "maps/EasternFrontier/Locked/Frontier Farm_%s.png"
        action NullAction()

    imagebutton anchor (0.5,0.5) pos (314,310) focus_mask True:
        auto "maps/EasternFrontier/Locked/Frontier Village_%s.png"
        action NullAction()


    imagebutton auto "maps/EasternFrontier/Grok og Dar_%s.png" anchor (0.5,0.5) pos (481,596) focus_mask True:
        action [Hide("eastern_frontier"), Jump("lowerorccamp")]

    imagebutton anchor (0.5,0.5) pos (433,786) focus_mask True:
        if ef_grove_unlocked == True:
            auto "maps/EasternFrontier/Grove_%s.png"
            if raidquest >=6:
                action [Hide("eastern_frontier"), Jump("ef_grove")]
            else:
                action [Hide("eastern_frontier"), Jump("ef_untrained")]
        else:
            auto "maps/EasternFrontier/Locked/Grove_%s.png"
            action NullAction()

    imagebutton anchor (0.5,0.5) pos (61,209) focus_mask True:
        auto "maps/EasternFrontier/Locked/Lundari Farm_%s.png"
        action NullAction()

    imagebutton anchor (0.5,0.5) pos (615,186) focus_mask True:
        auto "maps/EasternFrontier/Locked/Maelton_%s.png"
        action NullAction()

    imagebutton anchor (0.5,0.5) pos (840,33) focus_mask True:
        auto "maps/EasternFrontier/Locked/Mhanenvale_%s.png"
        action NullAction()

    imagebutton anchor (0.5,0.5) pos (922,749) focus_mask True:
        auto "maps/EasternFrontier/Locked/Mountains_%s.png"
        action NullAction()

    imagebutton anchor (0.5,0.5) pos (349,426) focus_mask True:
        auto "maps/EasternFrontier/Locked/Mountains1_%s.png"
        action NullAction()

    imagebutton anchor (0.5,0.5) pos (896,264) focus_mask True:
        auto "maps/EasternFrontier/Locked/Mountains2_%s.png"
        action NullAction()

    imagebutton anchor (0.5,0.5) pos (493,279) focus_mask True:
        auto "maps/EasternFrontier/Locked/Mountain Caves_%s.png"
        action NullAction()

    imagebutton anchor (0.5,0.5) pos (808,308) focus_mask True:
        auto "maps/EasternFrontier/Locked/Mountain Tower_%s.png"
        action NullAction()

    imagebutton anchor (0.5,0.5) pos (168,374) focus_mask True:
        auto "maps/EasternFrontier/Locked/Independent Village_%s.png"
        action NullAction()

    imagebutton anchor (0.5,0.5) pos (236,460) focus_mask True:
        auto "maps/EasternFrontier/Locked/Independent Village_%s.png"
        action NullAction()

    imagebutton anchor (0.5,0.5) pos (771,52) focus_mask True:
        auto "maps/EasternFrontier/Locked/Quadran Village_%s.png"
        action NullAction()

    imagebutton anchor (0.5,0.5) pos (765,200) focus_mask True:
        auto "maps/EasternFrontier/Locked/Quadran Village_%s.png"
        action NullAction()

    imagebutton anchor (0.5,0.5) pos (727,287) focus_mask True:
        auto "maps/EasternFrontier/Locked/Quadran Village_%s.png"
        action NullAction()

    imagebutton anchor (0.5,0.5) pos (653,515) focus_mask True:
        auto "maps/EasternFrontier/Locked/Remote Ruins_%s.png"
        action NullAction()

    imagebutton anchor (0.5,0.5) pos (904,519) focus_mask True:
        auto "maps/EasternFrontier/Locked/Riverside Ruins_%s.png"
        action NullAction()

    imagebutton anchor (0.5,0.5) pos (443,385) focus_mask True:
        if ef_rogue_orc_camp_unlocked == True:
            if raidquest >=6:
                if tutorialraiddone == False:
                    auto "maps/EasternFrontier/Rogue Orc Camp_%s.png"
                    action [Hide("eastern_frontier"), Jump("tutorialraid")]
                else:
                    auto "maps/EasternFrontier/Locked/Rogue Orc Camp_%s.png"
                    action NullAction()
            else:
                auto "maps/EasternFrontier/Rogue Orc Camp_%s.png"
                action [Hide("eastern_frontier"), Jump("ef_untrained")]
        else:
            auto "maps/EasternFrontier/Locked/Rogue Orc Camp_%s.png"
            action NullAction()

    imagebutton anchor (0.5,0.5) pos (140,664) focus_mask True:
        auto "maps/EasternFrontier/Locked/Shamanic Village_%s.png"
        action NullAction()

    imagebutton anchor (0.5,0.5) pos (478,462) focus_mask True:
        if SUlakequest > 0:
            auto "maps/EasternFrontier/Sorthyos Lake_%s.png"
            action [Hide("eastern_frontier"), Jump("ef_orclake")]
        else:
            auto "maps/EasternFrontier/Locked/Sorthyos Lake_%s.png"
            action NullAction()

    imagebutton anchor (0.5,0.5) pos (202,612) focus_mask True:
        auto "maps/EasternFrontier/Locked/Sothen Bridge_%s.png"
        action NullAction()

    imagebutton anchor (0.5,0.5) pos (1057,554) focus_mask True:
        auto "maps/EasternFrontier/Locked/Vegardan Lands_%s.png"
        action NullAction()

    imagebutton anchor (0.5,0.5) pos (571,738) focus_mask True:
        auto "maps/EasternFrontier/Locked/Weaving Caverns_%s.png"
        action NullAction()

    imagebutton anchor (0.5,0.5) pos (232,79) focus_mask True:
        auto "maps/EasternFrontier/Locked/Whitecrest_%s.png"
        action NullAction()

    imagebutton anchor (0.5,0.5) pos (170,242) focus_mask True:
        auto "maps/EasternFrontier/Locked/Whitecrest Village_%s.png"
        action NullAction()

    imagebutton anchor (0.5,0.5) pos (252,174) focus_mask True:
        auto "maps/EasternFrontier/Locked/Whitecrest Village_%s.png"
        action NullAction()

    imagebutton anchor (0.5,0.5) pos (283,246) focus_mask True:
        auto "maps/EasternFrontier/Locked/Whitewater Pass_%s.png"
        action NullAction()


    if (maplycaptured == False and catgirlraidquest == True):
        imagebutton anchor (0.5,0.5) pos (511,368) focus_mask True:
            idle "animated_pink_arrow"
            hover "animated_blue_arrow"
            hovered Show("ef_info", text="Observe the Catgirl raid party", pos=(511,298))
            unhovered Hide("ef_info")
            action [Hide("eastern_frontier"), Hide("ef_info"), Jump("ef_observe_catgirl")]


    if (orcfestivalquest == True and exhaustedhindhunts == False and arenatime <= 0):
        imagebutton anchor (0.5,0.5) pos (511,475) focus_mask True:
            idle "animated_pink_arrow"
            hover "animated_blue_arrow"
            hovered Show("ef_info", text="Hunt for the White Hind", pos=(511,405))
            unhovered Hide("ef_info")
            action [Hide("eastern_frontier"), Hide("ef_info"), Jump("ef_white_hind")]


    if vehlislocationquest < 3 and vehlislocationquest > 0:
        imagebutton anchor (0.5,0.5) pos (699,203) focus_mask True:
            idle "animated_pink_arrow"
            hover "animated_blue_arrow"
            hovered Show("ef_info", text="Travel to meet up with Vehlis", pos=(699,133))
            unhovered Hide("ef_info")
            action [Hide("eastern_frontier"), Hide("ef_info"), Jump("ef_travel_vehlis")]


    if (banditintroraiddone == False and recruitmentopened == True):
        imagebutton anchor (0.5,0.5) pos (509,308) focus_mask True:
            idle "animated_pink_arrow"
            hover "animated_blue_arrow"
            hovered Show("ef_info", text="Bandit Camp Raid", pos=(509,238))
            unhovered Hide("ef_info")
            if raidquest >=6:
                action [Hide("eastern_frontier"), Hide("ef_info"), Jump("ef_bandit_camp")]
            else:
                action [Hide("eastern_frontier"), Hide("ef_info"), Jump("ef_untrained")]


    if (KLshamans == True and KLshamanscampraided == False and recruitmentopened == True):
        imagebutton anchor (0.5,0.5) pos (576,550) focus_mask True:
            idle "animated_pink_arrow"
            hover "animated_blue_arrow"
            hovered Show("ef_info", text="Shaman's Camp Raid", pos=(576,480))
            unhovered Hide("ef_info")
            if raidquest >=6:
                action [Hide("eastern_frontier"), Hide("ef_info"), Jump("ef_shaman_camp")]
            else:
                action [Hide("eastern_frontier"), Hide("ef_info"), Jump("ef_untrained")]


    if kiaelmyquestion == True and kiaelmyscene == True and KLelmypotion == False:
        imagebutton anchor (0.5,0.5) pos (287,493) focus_mask True:
            idle "animated_pink_arrow"
            hover "animated_blue_arrow"
            hovered Show("ef_info", text="Escort Elmy", pos=(287,423))
            unhovered Hide("ef_info")
            action [Hide("eastern_frontier"), Hide("ef_info"), Jump("ef_escort_elmy")]


    if (rokgridfakeraidquest == True and rokgridraiddone == False):
        imagebutton anchor (0.5,0.5) pos (368,652) focus_mask True:
            idle "animated_pink_arrow"
            hover "animated_blue_arrow"
            hovered Show("ef_info", text="Rokgrid's Quest", pos=(368,582))
            unhovered Hide("ef_info")
            action [Hide("eastern_frontier"), Hide("ef_info"), Jump("ef_rokgrid_quest")]


    if (tekrokraidintroduced == True and tekroktargetraided == False):
        imagebutton anchor (0.5,0.5) pos (375,345) focus_mask True:
            idle "animated_pink_arrow"
            hover "animated_blue_arrow"
            hovered Show("ef_info", text="Tekrok's Quest", pos=(375,275))
            unhovered Hide("ef_info")
            action [Hide("eastern_frontier"), Hide("ef_info"), Jump("ef_tekrok_quest")]


    if (dajrabraidintroduced == True and dajrabcaravanfinished == False):
        imagebutton anchor (0.5,0.5) pos (998,341) focus_mask True:
            idle "animated_pink_arrow"
            hover "animated_blue_arrow"
            hovered Show("ef_info", text="Dajrab's Quest", pos=(998,271))
            unhovered Hide("ef_info")
            action [Hide("eastern_frontier"), Hide("ef_info"), Jump("ef_dajrab_quest")]


    if SUgivententaclequest == True and SUtentaclequestdone == False:
        imagebutton anchor (0.5,0.5) pos (380,699) focus_mask True:
            idle "animated_pink_arrow"
            hover "animated_blue_arrow"
            hovered Show("ef_info", text="Track the tentacle monster", pos=(380,629))
            unhovered Hide("ef_info")
            action [Hide("eastern_frontier"), Hide("ef_info"), Jump("ef_SUtentacle")]


    if tutorialraiddone == True:
        imagebutton anchor (0.5,0.5) pos (340,315) focus_mask True:
            idle "animated_pink_arrow"
            hover "animated_blue_arrow"
            hovered Show("ef_info", text="Base encampment", pos=(340,245))
            unhovered Hide("ef_info")
            action [Hide("eastern_frontier"), Hide("ef_info"), Jump("ef_basecamp")]


screen ef_info(text, pos):
    frame anchor (0.5,0.5) pos (pos) at map_top:
        background None
        text "[text]" style "map_desc"


label ef_mountains_phase1:
    scene bg countryside
    $ renpy.block_rollback()
    menu:
        "Bury the package" if dajraberrand == 3:
            if Inventory.has_item(Shovel) > 0:
                $ dajraberrand += 1
                "Using her shovel, Sabia managed to dig a decently-sized hole outside town, away from the nearest sentries."
                "Though she had worked daily on the training grounds, she hadn't done labor like this in years. She found herself surprisingly sore by the time she dug the hole deep enough."
                "But holding the package over the hole, she found herself hesitating."
                s "(Am I really going to just follow orders blindly? I suppose this could be a fake task to test if I'm trustworthy, but I don't think anyone followed me.)"
                menu:
                    "Just bury the package":
                        "Deciding it was better not to take a chance, Sabia set the package into the hole and covered it with dirt."
                        "After examining her work for a moment, she wiped her brow and headed back into camp."
                        jump eastern_frontier_map
                    "Look inside":
                        $ dajrablookedpackage = True
                        "Carefully undoing the package's ties so as not to deal any lasting damage, Sabia opened it on the ground near the hole."
                        "Inside, she found several stone slabs - no wonder it was so heavy - and two sacks."
                        "The slabs were covered in markings she couldn't read in the slightest. They looked ancient to her, but she couldn't tell anything else about them."
                        "One of the sacks contained dark blue stones: they didn't strike her as magic, but perhaps magically inclined."
                        "The third sack contained money. The Lundils contained within were old, minted before Lundar had dominated the land, but still valid."
                        s "(Huh? Does Dajrab have some kind of archeology hobby? What's the point of any of this?)"
                        s "(Hmm... if the next person to take these knows as little as Neve did, perhaps they don't know exactly what to expect. I could take these...)"
                        s "(It'd be a risk, though. I wonder...)"
                        menu:
                            "Take money":
                                $ dajrabtookmoney = True
                                $ money += 22
                                "Sabia took the sack of money and hid it in her cleavage. She needed everything she could get."
                            "Bury everything":
                                "No, not worth it. Sabia replaced the money."
                        "Carefully putting the package back together so that it looked the same as before, down to the individual ties, Sabia placed it inside the hole and covered it with dirt."
                        "After examining her work for a moment, she wiped her brow and headed back into camp."
                        jump eastern_frontier_map
            else:
                "The ground was hard and filled with roots, making it too difficult for Sabia to bury the package without a tool."
                jump eastern_frontier_map
        "Go back":
            jump eastern_frontier_map


label ef_observe_catgirl:
    scene bg forest with dissolve
    $ renpy.block_rollback()
    "Outside camp, Sabia noticed a group of angry, armed orcs. It became clear they intended to go and strike back at the catgirls who had stolen the shipment of metal."
    if catgirlraidpermission == False:
        "But without permission from the Warchief, Sabia doubted she could join an official raid. Better to stay cautious for now."
        jump eastern_frontier_map
    menu:
        "Do nothing":
            "It didn't seem like they were going anywhere immediately, so Sabia decided she still had time to prepare."
            jump eastern_frontier_map
        "Go with the orc raid (200 stamina)":
            if Sabia.stamina < 200:
                "Sabia was too tired to join the raid."
                jump eastern_frontier_map
            $ Sabia.stamina -= 200
            show bg countryside with dissolve
            "The band rushed from the camp, roaring and clanking their weapons. Sabia followed near the back, wondering if they could actually be that stupid, but eventually the group calmed down. Instead they marched in silence, going around low hills as they drew nearer to a large group of trees."
            scene bg forest with dissolve
            call sabiabase
            if catgirlraidinvestigation < 5:
                "When they reached the forest, the group began to spread out, scouting for signs of catgirls. Sabia rushed to the front, eager to be the first to spot one of the catgirls and prove herself."
                "She thought she saw something out of the corner of her eye, the shadow of a tree bending unnaturally. She whirled to look, but there was nothing there."
                show sabiaemo surprised3 at left
                "Then there was a soft sound, and something sharp bit into her neck."
                "Sabia reached up and ripped it out, discovering it was a small feathered dart. Small and harmless... yet her head was spinning..."
                scene bg black
                "Grimacing, Sabia fell to the ground as her body began to spasm... she tasted blood in her mouth and then everything began fading away..."
                show gameover with dissolve
                pause 3
                $ renpy.full_restart()
            else:
                "When they reached the forest, the group began to spread out, scouting for signs of catgirls. Sabia stayed back, instead looking for signs the hasty orcs might miss."
                show maply 1 at right
                show maplyemo surprise1 at right
                with dissolve
                "Suddenly, Sabia caught sight of one of the catgirls. It was a young one, eyes wide to see their band. She stared for only a second and then turned, tail whipping as she vanished into the forest."
                hide maply 1
                hide maplyemo surprise1
                with dissolve
                "Several other orcs saw her as well and roared, summoning the entire group charging after the catgirl."
                "At first, it seemed like they might catch up. Several times, Sabia caught a glimpse of the catgirl's shadow as she fled them. Yet they never seemed to get close enough to make an attempt at catching her."
                show sabiaemo closed2 at left
                "When she found the first body, Sabia realized what was going on. The orc lay dead with a dart in his neck, no doubt poisoned."
                "They had never come close to catching up with the catgirls, this was all their trap. The plan had been to lead them on a wild chase through the forest, wearing them down and taking down a few of them."
                s "Dammit..."
                scene bg black with dissolve
                "Eventually, even the orc leaders agreed. The group headed back to camp, not talking about how they had been bested by a few pathetic catgirls."
                "Sabia merely gritted her teeth and vowed to do better next time."
                $ catgirlraidperformance -= 5
            jump eastern_frontier_map
        "Shadow the orc raid (200 stamina)" if catgirlraidjadk:
            if Sabia.stamina < 200:
                "Sabia was too tired to shadow the raid."
                jump eastern_frontier_map
            $ Sabia.stamina -= 200
            "When the raiding party went off, whooping and hollering, Sabia followed them, keeping her distance. They did become stealthier as they went along and got serious, but their efforts were still too crude to be much good."
            "Sabia trailed them for quite some time as they headed to the location where they would allegedly find and punish the catgirls."
            scene bg forest
            call sabiabase
            with dissolve
            if catgirlraidinvestigation >= 6:
                $ catgirlraidperformance += 3
                "Recalling everything she knew about catgirls, Sabia decided to place the orcs between herself and the forest they were targeting. Once they had started pushing into it, she sneaked around the other side and entered the forests from behind."
            elif catgirlraidinvestigation >= 3:
                "Without being sure of their exact route, Sabia just stayed far back, letting the orcs draw all the attention."
            else:
                $ catgirlraidperformance -= 3
                $ catgirlraidinvestigation += 1
                "To stay out of sight of the orcs, Sabia headed into a grove of trees and trailed them from the shadows."
                "But after only a short time, Sabia realized that she was being watched. She whirled, and thought she caught sight of a fleeing tail, but it was too late."
                show sabiaemo closed2 at left
                "So she'd been spotted, just like the orcs. Cursing her foolishness, Sabia headed back to camp and gave the attempt up for lost. Perhaps another time..."
                jump eastern_frontier_map
            "From a distance, Sabia could see strange shadows shifting in the trees. They flitted around the group of orcs, making their attempts at sneaking look like they were rampaging through the forests. Just like she'd suspected, the catgirls had known that the orcs would be coming for them."
            "No doubt their caravan was nowhere near this forest anymore, and there were only a few scouts left behind to distract or spy on them. That was what Sabia had been counting on."
            "Though she couldn't move as quietly as the natural thieves, Sabia did her best to sneak closer to the area the orcs were searching. When she came too close to see their movements, she hid behind a large tree and waited, stretching all her senses to the maximum."
            show maply 1 at right
            show maplyemo surprise1 at right
            with dissolve
            "Then, without warning, a catgirl darted between the nearby trees. Sabia lunged from her hiding spot, intercepting her, and the catgirl yelped in surprise."
            catgirl "Aaah!"
            "Before the catgirl could flee, Sabia leapt to attack."
            scene bg forestF
            $ enemy_type = 1
            $ enemy_skills = [Enemyattack]
            $ enemy_level = 5
            $ enemy_maxhp = 350
            $ enemy_hp = enemy_maxhp
            $ enemy_attack = 70
            $ enemy_defense = 0
            $ enemy_magdefense = 35
            $ player = Sabia
            $ enemy = Maply
            $ Maply.face = "angry1"
            call duel
            if _return == "Victory":
                play music orccamp fadeout 2.0 fadein 2.0
                call sabiabase
                show maplyemo surprise2 at right
                show maply 1 at right
                with dissolve
                catgirl "Ah..."
                "Sabia smirked as the catgirl finally collapsed. She'd taken care not to kill her, but it had been harder than expected, with the catgirl darting around so quickly. But now she was done."
                s "Alright, girl, you're my prisoner now. What's your name?"
                show maplyemo angry2 at right
                catgirl "I'm not gonna tell you!"
                show sabiaemo eyebrow1 at left
                s "Heh, you think you're in a position to negotiate?"
                catgirl "..."
                show sabiaemo normal at left
                s "Alright, it doesn't matter. I'll have enough time for you once we get back to camp."
                scene bg countryside with dissolve
                "Not trusting the orcs to realize what an opportunity it was to have a live captive, Sabia gagged the catgirl and pulled her out of the forest."
                "The catgirl whined and squirmed the entire way, but she was surprisingly light and Sabia had no trouble overpowering her. For a moment she wondered if this was how orcs felt compared to humans, but she pushed the thought out of her mind."
                "What mattered was that she'd captured one of the enemy. That alone might have been considered a victory, but Sabia was aiming much higher than that. No, she had bigger plans..."
                scene bg sabiatent
                call sabiabase
                show maply 3 at right
                show maplyemo angry1 at right
                with dissolve
                catgirl "L-let me go! I don't wanna be here!"
                s "That doesn't really matter, now does it?"
                show maplyemo angry2 at right
                catgirl "Lemme go!"
                s "I'd be quiet, if I were you. Do you want the orcs to eat you? They've been hungry for catgirls lately..."
                show maplyemo sad1 at right
                catgirl "Would... would they really?"
                show sabiaemo closed2 at left
                s "(Is she really that naive, or just faking? Guess I'll find out soon enough.)"
                show sabiaemo normal
                menu:
                    "Play it hard":
                        $ catgirlraidperformance += 2
                        s "There's not much I can do... they really like chopping up and eating catgirls."
                        show maplyemo sad3 at right
                        catgirl "N-no! Don't let them eat me!"
                        s "I guess maybe I can hide you... but I'm taking a big risk here!"
                    "Play it soft":
                        $ A_maply += 1
                        s "If you listen to me and answer my questions, maybe I can keep them from eating you. Alright?"
                        catgirl "..."
                s "So... what's your name?"
                show maplyemo eyebrows at right
                maply "I... I'm Maply."
                s "Well, then, Maply... let's see how this goes..."
                $ maplycaptured = True
                $ a_list.append("Maply")
                jump sabiahq2
            else:
                call sabiabase
                show maply 1 at right
                show maplyemo surprise2 at right
                with dissolve
                "Sabia hit the ground, bleeding from dozens of small cuts. The catgirl gasped, as if she hadn't expected to win, much less do so much damage."
                catgirl "Oh! Why is a human... I didn't mean..."
                "But it was too late. Everything went dark as Sabia bled out..."
                show gameover with dissolve
                pause 3
                $ renpy.full_restart()
            jump eastern_frontier_map


label ef_forest2:
    scene bg forest
    $ renpy.block_rollback()
    menu:
        "Gain access to hunting grounds" if (recruitmentopened == True and huntingopen == False):
            call SUhuntingorc
            jump ef_forest2
        "Go hunting ([huntingcost] stamina)" if huntingopen == True:
            if foresthunting == 0:
                if Sabia.stamina < huntingcost:
                    "Sabia was too tired to hunt."
                    jump ef_forest2
                call sabiabase
                "Sabia wasn't sure exactly how hunting rights were supposed to work, just that Rokgrid had told her to come to this area. Fortunately, an orc quickly approached her."
                show orcbase at right
                show orcloincloth at right
                show orcnecklace at right
                show orcbeard1 at right
                show orcwrap at right
                show orcwrists at right
                show orcaxe at right
                show orcemo normalopen at right
                with dissolve
                orc "You the one Rokgrid sent, huh? You think you can actually contribute something?"
                s "I've hunted for myself in the past on the campaign trail, but I'm not an expert. And I don't exactly have full supplies."
                show orcemo normal at right
                orc "We can supply you with the very basics, though you'll probably want to get your own in time."
                orc "Anyway, here's how this works: you hunt and we pay you for whatever you come home with."
                s "That's it?"
                show orcemo normalopen at right
                orc "If you lose the equipment we give you, you'll have to pay for it. But otherwise, that's it."
                s "Good. This shouldn't be too hard, then."
                scene bg forest
                call sabiabase
                "Sabia's hunting skills were rusty, but as she wandered out into the forest, they started to come back to her. She'd never been good with a bow, but snares came easily to her."
                "By the end of the day, Sabia had only managed to find a few rabbits. Not good, given how rich with game the forests were, but not so bad."
                show orcbase at right
                show orcloincloth at right
                show orcnecklace at right
                show orcbeard1 at right
                show orcwrap at right
                show orcwrists at right
                show orcaxe at right
                show orcemo normalopen at right
                with dissolve
                orc "Huh. Didn't expect you to get anything."
                show sabiaemo eyebrow1 at left
                s "Hmph. This forest is easy pickings."
                show orcemo normal at right
                orc "Well, these are worth 6 Lundils. Come back again if you want more."
                $ Sabia.stamina -= huntingcost
                $ foresthunting += 1
                $ money += 6
                $ Sabia.xp += 1
                jump ef_forest2
            if Sabia.stamina >= huntingcost:
                $ Sabia.stamina -= huntingcost
                $ foresthunting += 1
                if foresthunting <= 10:
                    "Going hunting again brought back Sabia's old campaign habits and she felt a little sharper."
                    $ Sabia.xp += 1
                if foresthunting == 3:
                    $ money += 8
                    $ huntingcost -= 10
                    $ antlers += 1
                    $ Inventory.add_item(Antlers,1)
                    scene bg forest
                    call sabiabase
                    "To her surprise, one of Sabia's snares caught a small deer that sold for 8 Lundils."
                    "She felt like her old hunting skills were starting to come back to her, she thought she could hunt more efficiently in the future."
                elif foresthunting == 5:
                    $ money += 12
                    $ Inventory.add_item(Grayleaf)
                    scene bg forest
                    call sabiabase
                    "Several of Sabia's catches were taken by a bear or some other large animal before she could reach them, but she managed to take down a wolf with a fine pelt that sold for 12 Lundils."
                    "On top of that, there was a small amount of grayleaf growing near the wolf's den. Sabia gathered the useful herb before moving on."
                elif foresthunting == 6:
                    $ money += 3
                    $ hunttrainingopen = True
                    scene bg forest
                    call sabiabase
                    "Despite her best efforts, Sabia barely managed to catch anything. But when the head hunter gave her the 3 Lundils she'd earned, he looked thoughtful."
                    show orcbase at right
                    show orcloincloth at right
                    show orcnecklace at right
                    show orcbeard1 at right
                    show orcwrap at right
                    show orcwrists at right
                    show orcaxe at right
                    show orcemo normal at right
                    with dissolve
                    orc "You're more dedicated than I expected, human."
                    s "..."
                    orc "I don't usually do this, but... if you want to learn more, find me on the training grounds. I can teach you how to hunt these forests."
                    s "(Hmm. That's probably an opportunity I shouldn't overlook.)"
                elif foresthunting == 8:
                    $ money += 9
                    $ Inventory.add_item(Grayleaf)
                    "While hunting, Sabia noticed some grayleaf glimmering on the forest floor. She gathered it quickly and went back to work, earning 9 Lundils."
                elif foresthunting == 10:
                    $ money += 6
                    $ Inventory.add_item(Steelshrooms,3)
                    scene bg forest
                    call sabiabase
                    "Sabia's hunting was proceeding normally, but not spectacularly. While she was on the heels of a deer, she stumbled across a small cavern."
                    "Inside it, she discovered several steelshrooms. They'd been called the \"soldier's friend\" on the campaign trail for their use in healing. Good to keep for future use."
                else:
                    if orchuntingtraining:
                        $ money += 11
                        scene bg forest
                        call sabiabase
                        "Sabia attempted to hunt animals in the forest and managed to capture a few small rabbits. They sold for 11 Lundils."
                    else:
                        $ money += 6
                        scene bg forest
                        call sabiabase
                        "Sabia attempted to hunt animals in the forest and managed to capture a few small rabbits. They sold for 6 Lundils."
                jump ef_forest2
            else:
                "Sabia was too tired to hunt."
                jump ef_forest2
        "Clean up the site of the murders." if (bargroping == 5 and murderinvcleansite == False):
            $ murderinvcleansite = True
            "Though her orc allies had cleaned up the site of the murders, Sabia was paranoid that something might remain. She headed back to it... but not right away."
            "First she circled around aimlessly, just in case she was being followed. But it seemed like she wasn't tailed - the orcs were used to her traveling outside the camp. That meant she could return to the site without proving her guilt."
            "Once she arrived, Sabia found it basically clean, but not entirely. She considered wiping out the scuff marks and doing something about the axe damage to a few trees, but... the investigator seemed smart, he might figure out that evidence had been removed."
            "Instead, Sabia just made a path through the brush away from the site, eventually reaching a small stream and letting the path disappear after that. She was careful to only break older branches, to create the illusion that the path had been made some time ago."
            "When she was done and looked it over, Sabia was satisfied. There was evidence that orcs had fought here, but also evidence that they had left by a different path. That was nothing unusual."
            "Just to be safe, Sabia returned to camp by a different path."
            jump ef_forest2
        "Check for witnesses." if (bargroping == 5 and murderinvwitness2 == False and murderinvwitness2hint == False):
            $ murderinvwitness2hint = True
            "Investigating around the outskirts, Sabia quickly discovered that there was a hunter who had spotted her leaving the camp with the group of orcs. He didn't seem to particularly hate her, but he agreed to speak to the investigator about what he knew."
            "Sabia realized that she was going to need to do something about him. She considered killing the orc, but immediately realized that wouldn't work: the timing would be far too suspicious and just draw more attention to her."
            "Her only option was to eliminate him in a way that looked like an accident. Sabia didn't have the skills to set it up herself, but the orc hunted dangerous game every day... with the right potion, maybe she could make sure that he had an accident."
            "Sabia tried to remember what she knew of potions and decided that one called Haze Wine would be the ideal choice."
            jump ef_forest2
        "Check for witnesses." if (bargroping == 5 and murderinvwitness2 == False and murderinvwitness2hint == True):
            "The hunter who was going to testify against Sabia was still going out on daily hunts. Sabia thought she'd be able to poison his flask of beer, if she had the right potion."
            if Inventory.has_item(Hazewine):
                $ Inventory.rem_item(Hazewine)
                $ murderinvwitness2 = True
                $ bargropeinv += 2
                "While the hunter was restringing his bow, Sabia added Haze Wine to his beer. Then she sneaked away and waited, hoping it would work."
                "At the end of the day... nothing happened. The hunter didn't appear. Sabia realized that she'd been imagining someone showing up and dramatically announcing that he'd gotten himself killed, but of course it wouldn't go that way."
                "Instead she had to wait until the next day for someone to find his body. It seemed he'd foolishly attempted to attack a nest of monsters and been torn apart. The orcs shook their heads, but didn't consider it anything out of the ordinary."
                "Sabia wished she'd had another way, but she didn't regret what she'd done. With another witness gone, her case had become stronger."
            else:
                "Unfortunately, Sabia still hadn't created any Haze Wine."
            jump ef_forest2
        "Go to meet Kia" if orccampphase == 2 and recruitmentopened and kiaprogression > 1 and kiaprogression < 9:
            call kiaprogressionscenes
            jump ef_forest2
        "Kia's Valley" if orccampphase == 2 and recruitmentopened == True and kiaprogression >= 9:
            call kiaprogressionscenes
            jump ef_forest2
        "Kia's Cave" if orccampphase == 2 and recruitmentopened == True and kiaprogression >= 9:
            call kiaprogressionscenes
            jump ef_forest2
        "Go back":
            jump eastern_frontier_map


label ef_forest_ruin:
    scene bg forest
    $ renpy.block_rollback()
    menu:
        "Investigate suspicious area" if (recruitmentopened == True and SUarmorsuppliesquest == False):
            call SUarmorquest
        "Investigate the site of Barrin's dead drop." if barrinletterhint == True and barrinletterquest == False:
            if Sabia.stamina < 100:
                "Sabia was too tired to journey that far out of camp."
                jump orcoutskirts2
            $ barrinletterquest = True
            $ Sabia.stamina -= 100
            scene bg road
            call sabiabase
            with dissolve
            "Sabia headed out of camp, following the instructions she'd been given by Barrin. No doubt he and his contact considered the drop lost and would send another... which meant she had an opportunity to intercept their message."
            scene bg countryside
            call sabiabase
            with dissolve
            "After a long time traveling, she was well off the beaten path but approaching her destination. There was a cluster of trees where the mole had allegedly left the information he needed to give to the Sceyuer family."
            "At first, Sabia searched and couldn't find it anywhere. She started to wonder if she had gotten off track, but she checked and her sense of direction was good anyway. It was possible that Barrin had lied - she wouldn't have thought him capable of it, but maybe sex wasn't a good way to extract information."
            "Just as she was starting to regret wasting time with him, Sabia found it. A small package that contained a number of documents. Not wanting to take any chances, Sabia read over them then and there."
            "Some of it was useless, just information on local peasants and their pathetic crops. Important for the local Governors fighting over turf, of course, but useless for her."
            "Other pieces, however, were critical. Governor Andian was apparently having strange troubles with a minotaur farm to the west... the exact problems were unknown, but the mole thought they might be serious enough to undermine him with Lundar."
            "Above all, the letters gave Sabia an exact impression of the conflict between the two Governors. Both wanted to join Lundar, but only with the best of terms that let them steal part of their neighbor's land. Greedy, arrogant bastards."
            "Sabia committed all the key details to memory, then replaced the letters exactly as they had been, just in case the mole risked returning for his package."
            "As she headed back to camp, Sabia found a smile creeping across her face. This information might not be critical now, but eventually..."
            jump eastern_frontier_map
        "Go back":
            jump eastern_frontier_map


label ef_abandoned_mine:
    scene bg road
    $ renpy.block_rollback()
    menu:
        "Investigate the site of the catgirl theft (200 stamina)" if (catgirlraidsite == False and maplyoutskirts == False and maplytortured == False):
            if Sabia.stamina < 200:
                "Sabia was too tired to investigate the raid site."
                jump eastern_frontier_map
            $ catgirlraidsite = True
            $ Sabia.stamina -= 200
            $ catgirlraidinvestigation += 2
            call sabiabase
            "Sabia had the orcs direct her to the exact location where the catgirls had raided the caravan and made off with the metal. There wasn't much left and it matched the orc reports, so Sabia wondered if she'd wasted her time."
            "She sifted through the wreckage, noting some old blood stains and torn cloth. It looked like they'd done some serious damage, even though it had been a quick raid designed to run off with the horses and wagon."
            "Contrary to what the orcs had suggested, Sabia noticed remnants of reins and saddles - the catgirls must have cut loose some of the horses. That meant they couldn't have taken the wagon too far. Other than that, she didn't notice anything different."
            "Just as she was about to leave, Sabia noticed a grove of trees in the distance, an unusually tall tree looming over the others. She almost thought she saw someone watching her, then it vanished."
            "Abruptly Sabia realized how it had happened. The catgirls hadn't known the exact route of the shipment, that would be impossible. Instead, they'd stationed themselves in locations where they could catch sight of passing shipments."
            "Alone that wasn't enough information to accomplish anything meaningful, but it was useful to know. Sabia tucked the fact away and headed back to camp."
            jump eastern_frontier_map
        "Go back":
            jump eastern_frontier_map


label ef_white_hind:
    scene bg forest
    $ renpy.block_rollback()
    $ temp1 = huntingcost * 2
    if Sabia.stamina < temp1:
        $ Sabia.stamina = 0
        "Sabia tried to hunt, but she was much too tired to be effective and ended up back in camp without accomplishing anything."
        jump eastern_frontier_map
    else:
        if whitehindhunt == 0:
            $ Sabia.stamina -= temp1
            $ whitehindhunt += 1
            "Sabia set out to look for a white hind. She managed to find an area with many deer tracks, but didn't catch sight of even an ordinary deer."
            "The day was more boring than anything, but on her way back to camp, she found many hunters who had made similar attempts, many of them injured. When she asked, she learned that young bucks sought out the white hind and could be quite aggressive, making the task more difficult than it appeared."
        elif whitehindhunt == 1:
            $ Sabia.stamina -= temp1
            $ whitehindhunt += 1
            $ HGNantlers = True
            $ antlers += 1
            $ Inventory.add_item(Antlers,1)
            "Venturing out to the point where she had been the previous day, Sabia spent a long time watching and waiting. Though she failed to catch sight of a white hind, she did bring down a handsome buck."
            $ money += 11
            "Back at camp, she took the antlers and sold the meat for 11 Lundils."
        elif whitehindhunt == 2:
            $ Sabia.stamina -= temp1
            $ whitehindhunt += 1
            "That day, Sabia discovered that another hunter was also tracking a white hind. She decided to follow him and see if she could learn a few tricks."
            "To her surprise, they caught sight of the white hind, beautiful in a ghostly way, flickering through the forest. But when they tried to pursue, a young buck charged from the forest, horns stabbing wildly."
            "Sabia was unharmed, but the horns gored the hunting orc in the stomach."
            if Inventory.has_item(Orchealthpotion):
                $ L_orcs += 1
                $ Inventory.rem_item(Orchealthpotion)
                $ Inventory.add_item(Hearttreesyrup)
                $ whitehindhunt += 3
                $ antlers += 1
                $ Inventory.add_item(Antlers,1)
                $ money += 21
                "Realizing that she had an Orc Health Potion on her, Sabia brought it out and forced the hunter to drink it. The magic did its work and he made a swift recovery."
                "In gratitude for saving his life, the hunter taught her a few tricks he'd learned for how to hunt white hinds. He also gave her his catch for the day, which included meat worth 21 Lundils, some Heart Tree Syrup, and an impressive set of antlers."
            else:
                "Sabia wished that she had some kind of potion to help him. She tried to carry him back to camp, but it took long enough that he had fallen unconscious by the time she got back. The other orcs said that it didn't look good."
                "Still, she was encouraged to have caught sight of her quarry."
        elif whitehindhunt == 3:
            $ Sabia.stamina -= temp1
            $ whitehindhunt += 1
            "Sabia set out again, trying to track down the white hind, but even though she returned to the same place, she failed to locate it."
        elif whitehindhunt == 4:
            "Sabia headed out, almost assuming that she'd fail again. Yet to her surprise, after only a few hours she caught a glimpse of the white hind."
            "Yet somehow it noticed her and shot away. Sabia ran after it, sprinting through the forest in a desperate attempt to see where it would run."
            if Sabia.stamina >= 220:
                $ whitehindhunt += 1
                $ Sabia.stamina = 0
                "Though it took everything she had, Sabia managed to keep up with the white hind for a while. She noticed that it stayed within the deep forests, reluctant to cross streams or venture anywhere near the roads."
                "Eventually she exhausted herself, but as Sabia headed back, she found that she was smiling. She felt that she had a much better grasp of how the white hind moved and where it roamed."
            else:
                $ Sabia.stamina = 0
                "Unfortunately, she soon became exhausted and lost sight of it. Sabia went back to camp discouraged, not having felt like she made much progress. She just didn't have the stamina to keep up with the hind."
        elif whitehindhunt == 5:
            $ Sabia.stamina -= temp1
            $ whitehindhunt += 1
            $ Inventory.add_item(Hearttreesyrup)
            "Sabia tried to search for a white hind again, but failed to catch anything more than a few glimpses of it. However, to her surprise she found a heart tree, out of place in these lands. She tapped it for some syrup, which would be a useful ingredient."
        elif whitehindhunt == 6:
            $ Sabia.stamina -= temp1
            $ whitehindhunt += 1
            "Using her newfound knowledge of the white hind, Sabia managed to find one. She got within bow range without disrupting it, to her surprise."
            "Sabia held her breath, not daring to do anything that might draw its attention. She nocked an arrow and drew back... slowly... slowly..."
            "Without warning the white hind's ears perked up. It froze for only a moment, then sprinted away, faster than she could follow. Sabia sighed and set down her bow. There was no point trying again now."
        elif whitehindhunt == 7:
            $ Sabia.stamina -= temp1
            "Sabia set out, determined to bring down a white hind this time. She thought carefully about everything she had learned and decided that this time, what she needed more than speed was stealth."
            "She found a location deep within the woods, in an area where she had seen hinds in the past. Sabia got herself coated in dirt to mask her scent and hid herself away in a tree, just waiting."
            "And waiting."
            "And waiting."
            "She had known it would be a long, difficult wait, but Sabia was not prepared for just how much it would drain her. She couldn't relax or she might make noise, and she needed to stay on high alert at all times. As wary as the white hind was, she might only have a short time."
            if Inventory.has_item(Energypotion) > 0:
                $ huntedwhitehind = True
                $ Inventory.add_item(Whitehind,1)
                $ whitehindhunt += 1
                $ Inventory.rem_item(Energypotion)
                $ Sabia.stamina = 0
                "Realizing that she couldn't stay alert on her own, Sabia looked through her pack and removed an Energy Potion. It was meant to be drank in one gulp in battle, but instead she sipped it slowly."
                "Though the tingle of energy wouldn't have been enough to help her much in combat, it kept her on high alert. Sabia began taking sips from the potion every time she began to feel drowsy."
                "Focusing on spacing her sips almost distracted her when it actually happened: a white hind emerged from the brush."
                "Sabia went utterly still, waiting as it looked nervously about. Eventually it shifted forward, cautiously beginning to drink from the stream."
                "Forcing herself not to rush, Sabia nocked her bow and lined up her shot. It was excruciating to move so slowly when the hind could dart away at any moment, but she kept her movements steady, then took a deep breath."
                "She almost didn't notice when she let go, her fingers seeming to know the right moment. Her arrow went straight through the hind's neck and it collapsed with a loud cry."
                "Sabia rushed to the body and put the beast out of its misery, bright blood staining its beautiful coat. She hefted the body up on her shoulders and headed back toward camp."
                "When she returned carrying the white hind on her shoulders, she got a rousing cheer of applause. Sabia delivered it triumphantly, exhausted but incredibly satisfied."
                "Too tired for anything else, she headed straight back to her tent."
                jump sabiahq2
            else:
                "Wiping her eyes one more time, Sabia did her best to stay focused. Yet as the hours dragged on, she suddenly found herself opening her eyes and realizing that she had drifted off."
                "There were a few tracks near the stream, but no sight of any deer. Sabia sighed and stuck around, hoping that she would spot one yet, but in the end she was too tired and headed home empty-handed."
                "Though she wished that she could succeed by force of will, she recognized that was unlikely. Most likely, she would need an artificial aid to keep her energy up."
        elif whitehindhunt == 8:
            $ Sabia.stamina -= temp1
            $ whitehindhunt += 1
            "Though she'd successfully slain a white hind, Sabia headed back out into the forest again to hunt for more antlers. She didn't find any that day, but resolved to try again."
        elif whitehindhunt == 9:
            $ Sabia.stamina -= temp1
            $ whitehindhunt += 1
            $ antlers += 1
            $ Inventory.add_item(Antlers,1)
            $ money += 17
            "After carefully hunting for much of the day, Sabia shot a spectacular buck. Its antlers would work well for the feast, and the meat was worth 17 Lundils."
        elif whitehindhunt >= 10:
            $ Sabia.stamina -= temp1
            $ exhaustedhindhunts = True
            "Sabia tried to hunt more, but the animals were all skittish from so many hunters making attempts at them."
        else:
            "Sabia hunted aimlessly through the woods."
    jump eastern_frontier_map


label ef_travel_vehlis:
    scene bg road
    $ renpy.block_rollback()
    if Sabia.stamina < 200:
        "Sabia was too tired to journey that far out of camp. (Requires 200 stamina)"
        jump eastern_frontier_map
    else:
        jump travel_to_meet_vehlis


label ef_bandit_camp:
    scene bg countryside with dissolve
    $ renpy.block_rollback()
    if tutorialraiddone == False:
        s "(Unfortunately, I can't go raiding until I've finished the task Groknak gave me.)"
        jump eastern_frontier_map
    if orcalliance == "sabia":
        s "(That camp is no joke... but I don't have a lot of other allies to rely on. I'd better be ready before trying to take it on.)"
        menu:
            "Do nothing for now":
                jump eastern_frontier_map
            "Assault the camp":
                call banditintroraid
                jump eastern_frontier_map
    elif (rokgridraidaftermathdone or tekrokraidaftermathscene or dajrabraidaftermathscene) and banditintroraiddone == False:
        call banditintroraid
        jump eastern_frontier_map
    else:
        s "(They look pretty organized... it'd be suicide to go against them without more support from someone...)"
        jump eastern_frontier_map


label ef_shaman_camp:
    scene bg countryside with dissolve
    $ renpy.block_rollback()
    if tutorialraiddone == False:
        s "(Unfortunately, I can't go raiding until I've finished the task Groknak gave me.)"
        jump eastern_frontier_map
    call KLshamanscamp
    jump eastern_frontier_map


label ef_escort_elmy:
    call KLelmyscene2
    jump eastern_frontier_map


label ef_grove:
    scene bg countryside
    $ renpy.block_rollback()
    if kiaquesthidden == True:
        "Sabia swung by the small grove just in case there might be something of import, but it was empty."
    else:
        scene bg forest
        call sabiabase
        with dissolve
        $ kiaquesthidden = True
        $ kiabones += 1
        $ Inventory.add_item(Makhorbones,1)
        "Sabia was trying to scout when she wandered through a tiny grove, too small to be on a proper map. There was nothing unusual about it, but she decided to look closely just to be sure."
        "To her surprise, she found the corpse of a dead orc. It had died within a few days, seemingly struck down by violence - possibly bandits, judging from how he had been stripped of everything of value. They had left one thing he was carrying, though: a Makhor bone won in the Red God's Arena."
        if kiaprogression >= 7:
            "Idiots, not understanding its true value. Sabia took the bone to bring to Kia later, but pondered the corpse. If the orc had won a bone, he was no weakling - these bandits were obviously well-prepared."
        else:
            "Idiots, not understanding its true value. As Sabia took the bone for herself, though, she found herself pondering this. If the orc had won a bone, he was no weakling - these bandits were obviously well-prepared."
        "She headed back to camp with additional caution."
    jump eastern_frontier_map


label ef_rokgrid_quest:
    scene bg countryside with dissolve
    $ renpy.block_rollback()
    if tutorialraiddone == False:
        s "(Unfortunately, I can't go raiding until I've finished the task Groknak gave me.)"
        jump eastern_frontier_map
    call rokgridraidevent
    jump eastern_frontier_map


label ef_tekrok_quest:
    scene bg countryside with dissolve
    $ renpy.block_rollback()
    if tutorialraiddone == False:
        s "(Unfortunately, I can't go raiding until I've finished the task Groknak gave me.)"
        jump eastern_frontier_map
    call tekrokraidevent
    jump eastern_frontier_map


label ef_dajrab_quest:
    scene bg countryside with dissolve
    $ renpy.block_rollback()
    if tutorialraiddone == False:
        s "(Unfortunately, I can't go raiding until I've finished the task Groknak gave me.)"
        jump eastern_frontier_map
    call dajrabraidevent
    jump eastern_frontier_map


label ef_safety:
    scene bg countryside
    $ renpy.block_rollback()
    s "(No, it wouldn't be safe to wander far. Ridiculous as it sounds, I'm safer in the orc camp than in human lands.)"
    jump eastern_frontier_map


label ef_untrained:
    scene bg countryside
    $ renpy.block_rollback()
    s "(I have permission to actually travel further to raid... but it would be foolish to do that before my forces have been properly trained.)"
    jump eastern_frontier_map


label ef_SUtentacle:
    if SUtentaclerested == False:
        scene bg countryside
        "Sabia was too tired to track the tentacle monster today."
        jump eastern_frontier_map
    if SUtentacleprogression == 6:
        $ SUtentaclerested = False
        call SUtentacle6
    elif SUtentacleprogression == 5:
        $ SUtentaclerested = False
        call SUtentacle5
    elif SUtentacleprogression == 4:
        $ SUtentaclerested = False
        call SUkiameetsneve
    elif SUtentacleprogression == 3:
        $ SUtentaclerested = False
        call SUtentacle4
    elif SUtentacleprogression == 1:
        $ SUtentaclerested = False
        call SUtentacle3
    else:
        $ SUtentaclerested = False
        call SUtentacle2
    jump eastern_frontier_map


label ef_orclake:
    scene bg orclake
    if SUlakequest >= 8:
        "Sabia enjoyed a quiet moment by the lake."
    elif SUlakequest >= 7:
        if kiaprogression >= 12:
            call SUylvalake7
        else:
            "Sabia thought she caught a glimpse of Kia and Ylva by the lake, but they were gone by the time she got close."
            jump eastern_frontier_map
    elif SUlakequest >= 6:
        call SUylvalake6
    elif SUlakequest >= 3:
        menu:
            "Orcs on the southern side" if SUlakeorcs == False:
                $ SUlakequest += 1
                $ SUlakeorcs = True
                call SUylvalake3
            "Humans on the northwestern side" if SUlakehumans == False:
                call SUylvalake4
            "Bandits on the northeastern side" if SUlakebandits == False:
                $ SUlakequest += 1
                $ SUlakebandits = True
                call SUylvalake5
            "Nothing":
                jump eastern_frontier_map
    elif SUlakequest == 2:
        s "(I should stay away from Ylva's business in the area, since I said I wouldn't get involved.)"
    else:
        call SUylvalake2
    jump eastern_frontier_map


label ef_basecamp:
    scene bg countryside
    menu:
        "Test formations":
            "Sabia had her soldiers run through a few drills, not so much to improve them as to test how far they'd come..."
            $ reset_armies()
            $ deployarmies(["Drills",10])
            call deployment
            "Drill complete, Sabia ordered her soldiers back to work. So that was what she had to work with."
            jump ef_basecamp
        "Train Sabia's main squad" if SUorctraining == False:
            call orcsquadtraining
        "Nothing":
            pass
    jump eastern_frontier_map
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
