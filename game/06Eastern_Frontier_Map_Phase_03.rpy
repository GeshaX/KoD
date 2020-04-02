screen eastern_frontier_phase3:
    $ renpy.block_rollback()
    add "maps/EasternFrontier/map clean.jpg"

    imagebutton anchor (0.5,0.5) pos (188,517) focus_mask True:
        if ef_abandoned_mine_unlocked == True:
            auto "maps/EasternFrontier/Abandoned Mine_%s.png"
            action [Hide("eastern_frontier_phase3"), Jump("ef3_abandoned_mine")]
        else:
            auto "maps/EasternFrontier/Locked/Abandoned Mine_%s.png"
            action NullAction()

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
        if ef_avarton_town_unlocked == True:
            auto "maps/EasternFrontier/Avarton_%s.png"
            action [Hide("eastern_frontier_phase3"), Jump("avarton_town")]
        else:
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
        action [Hide("eastern_frontier_phase3"), Jump("orcoutskirts3")]

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
            action [Hide("eastern_frontier_phase3"), Jump("ef3_forest2")]

    imagebutton anchor (0.5,0.5) pos (621,313) focus_mask True:
        if ef_forest_ruin_unlocked == True:
            auto "maps/EasternFrontier/Forest Ruin_%s.png"
            action [Hide("eastern_frontier_phase3"), Jump("ef3_forest_ruin")]
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
        action [Hide("eastern_frontier_phase3"), Jump("lowerorccamp")]

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
        if ef_mountains1_unlocked == True:
            auto "maps/EasternFrontier/Mountains1_%s.png"
            action [Hide("eastern_frontier_phase3"), Jump("ef3_mountains1")]
        else:
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
        if ef_remoteruins_unlocked == True:
            auto "maps/EasternFrontier/Remote Ruins_%s.png"
            action [Hide("eastern_frontier_phase3"), Jump("ef3_remoteruins")]
        else:
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
        auto "maps/EasternFrontier/Sorthyos Lake_%s.png"
        action [Hide("eastern_frontier_phase3"), Jump("ef3_orclake")]

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
        if ef_whitecrest_village_unlocked == True:
            auto "maps/EasternFrontier/Whitecrest Village_%s.png"
            action [Hide("eastern_frontier_phase3"), Jump("wcvillage")]
        else:
            auto "maps/EasternFrontier/Locked/Whitecrest Village_%s.png"
            action NullAction()

    imagebutton anchor (0.5,0.5) pos (283,246) focus_mask True:
        auto "maps/EasternFrontier/Locked/Whitewater Pass_%s.png"
        action NullAction()



    if (jadk_chaos == True and groknak_route_prompt == True and groknak_route_investigation == False):
        imagebutton anchor (0.5,0.5) pos (290,480) focus_mask True:
            idle "animated_pink_arrow"
            hover "animated_blue_arrow"
            hovered Show("ef_info", text="Investigate Groknak's Route", pos=(290,410))
            unhovered Hide("ef_info")
            action [Hide("eastern_frontier_phase3"), Hide("ef_info"), Jump("ef3_groknaks_route")]



    if ambush_site_vehlis == True and chaos_met_merchants == False:
        imagebutton anchor (0.5,0.5) pos (699,203) focus_mask True:
            idle "animated_pink_arrow"
            hover "animated_blue_arrow"
            hovered Show("ef_info", text="Meet with Merchants", pos=(699,133))
            unhovered Hide("ef_info")
            action [Hide("eastern_frontier_phase3"), Hide("ef_info"), Jump("ef3_merchants_quest")]


    if phase3_nevegone == True and chaos_met_merchants == True and chaos_bandit_quest_done == False:
        imagebutton anchor (0.5,0.5) pos (147,411) focus_mask True:
            idle "animated_pink_arrow"
            hover "animated_blue_arrow"
            hovered Show("ef_info", text="Track the bandits", pos=(147,341))
            unhovered Hide("ef_info")
            action [Hide("eastern_frontier_phase3"), Hide("ef_info"), Jump("phase3_bandit_camp_solo")]



    if kira_quest_prompt == True:
        imagebutton anchor (0.5,0.5) pos (147,411) focus_mask True:
            idle "animated_pink_arrow"
            hover "animated_blue_arrow"
            hovered Show("ef_info", text="Kira's Bandit Camp", pos=(147,341))
            unhovered Hide("ef_info")
            action [Hide("eastern_frontier_phase3"), Hide("ef_info"), Jump("ef3_kira_camp")]



    if avion_quest == 3:
        imagebutton anchor (0.5,0.5) pos (103,533) focus_mask True:
            idle "animated_pink_arrow"
            hover "animated_blue_arrow"
            hovered Show("ef_info", text="Rival Bandit Camp", pos=(103,463))
            unhovered Hide("ef_info")
            action [Hide("eastern_frontier_phase3"), Hide("ef_info"), Jump("ef3_rival_camp")]



    if v10lynn_hal_chase == 4:
        imagebutton anchor (0.5,0.5) pos (456,175) focus_mask True:
            idle "animated_pink_arrow"
            hover "animated_blue_arrow"
            hovered Show("ef_info", text="Chase Hal", pos=(456,105))
            unhovered Hide("ef_info")
            action [Hide("eastern_frontier_phase3"), Hide("ef_info"), Jump("ef3_chase_hal")]



    if v10tekrok_quest_prompt == True and v10tekrok_quest_done == False and v10tekrok_camp_left == False:
        imagebutton anchor (0.5,0.5) pos (720,645) focus_mask True:
            idle "animated_pink_arrow"
            hover "animated_blue_arrow"
            hovered Show("ef_info", text="Grak's Camp", pos=(720,575))
            unhovered Hide("ef_info")
            action [Hide("eastern_frontier_phase3"), Hide("ef_info"), Jump("ef3_graks_camp")]


label ef3_forest_ruin:
    scene bg forest
    menu:
        "Go back":
            jump eastern_frontier_map


label ef3_orclake:
    scene bg orclake
    menu:
        "Talk to Ylva" if chaos_ylva_lake == 1 and chaos_ylva_spoken == False:
            $ chaos_ylva_spoken = True
            $ chaos_ylva_lake = 2
            call sabiabase
            show ylva normal at right
            show ylva2 arm1 at right
            with dissolve
            "Ylva gave a soft smile, and sighed. It looked as if she hadn't slept for several days."
            show ylva happy1 at right
            ylva "There's something about the water that is soothing, isn't there? The deep blue, the soft, cool wind."
            show sabiaemo question1 at left
            ylva "I imagine even the most industrial Lundarian would feel more relaxed here."
            show ylva normal at right
            show sabiaemo normalopen at left
            s "That might be true, Ylva."
            show sabiaemo normal at left
            "Letting out another long sigh, Ylva looked up to the clouds, and then back to Sabia."
            show ylva opennormal at right
            ylva "I heard you've been investigating Warchief Groknak's disappearance."
            show ylva openclosed1 at right
            ylva "Please tell me he's just around the corner, resting, before coming back?"
            show ylva closedsad at right
            show sabiaemo sad3 at left
            s "I can't do that, sorry, Ylva."
            show sabiaemo sad1 at left
            show ylva sad at right
            ylva "That's too bad. It would have saved a lot of trouble, and I would have liked to see Groknak back safely."
            ylva "I trust your ability to continue looking into it, though, Sabia."
            show ylva sad at right
            show sabiaemo normalopen at left
            s "If I can get another lead, I will."
            s "But, if you're out here resting, does that mean the issues in the camp have been resolved?"
            show sabiaemo normal at left
            show ylva sad at right
            ylva "I wish. Almost as far away as could be."
            ylva "But, I've managed to mediate well enough. Rokgrid, Tekrok and Dajrab will keep everyone off each others' necks."
            ylva "For now, at least."
            show ylva sad at right
            show sabiaemo normalopen at left
            s "That's good, but I can't imagine that's going to last indefinitely?"
            show sabiaemo normal at left
            show ylva opennormal at right
            ylva "It won't, no. There will be a meeting in the main hall soon."
            show sabiaemo surprised1 at left
            ylva "Tekrok, Rokgrid and Dajrab will voice their thoughts and opinions, and the election of a new Warchief will likely begin."
            show ylva normal at right
            show sabiaemo normalopen at left
            s "An election?"
            show ylva surprised at right
            show sabiaemo closed2 at left
            ylva "Of course. Why should the tribe be burdened with an inept leader, just because their predecessor deemed it so?"
            show ylva normal at right
            show sabiaemo normalopen at left
            s "I just - I suppose it makes sense, knowing what I do now about orcs..."
            show ylva opennormal at right
            show sabiaemo normal at left
            ylva "There will be a period where the captains try to earn votes. They'll offer promises, host events..."
            ylva "It will be similar to the Red God's Feast, in a way, Sabia."
            show ylva sad at right
            show sabiaemo irritated1 at left
            ylva "And in another way, it will be more vicious."
            show ylva sad at right
            show sabiaemo closed2 at left
            s "(Fuck. If the wrong captain becomes the Warchief... that's going to undo all of the progress I've made here.)"
            s "(That's not something I can let happen.)"
            show sabiaemo normalopen at left
            show ylva angry1 at right
            if orcalliance != "sabia":
                s "What can I do, for my captain? I don't want my position jeopardized, Ylva. I've worked too hard."
            else:
                s "What can I do? I don't want my position jeopardized. I've worked too hard."
            show ylva openangry at right
            show sabiaemo surprised1 at left
            ylva "What?! {i}'You've worked too hard'{/i}? The future of the tribe is at stake here, Sabia!"
            show sabiaemo closed2 at left
            ylva "A good chieftain will push it forward, and be good for the tribe. But if it's a bad Warchief - then that's going to be wholly detrimental!"
            ylva "I've spent entire days, fighting captains and even a shaman to ensure Grok og Dar and the surrounding tribes don't break out into war!"
            ylva "And you ask, what can {i}you{/i} be doing right now?"
            show ylva angry1 at right
            show sabiaemo angry1 at left
            s "Well of course I want to take advantage of the situation! I won't sit by and watch opportunity pass."
            show ylva openangry at right
            show sabiaemo angry2 at left
            ylva "'Take advantage'?! Sabia, this is the whole tribe-"
            show sabiaemo closed2 at left
            ylva "How can you say something like that?"
            ylva "You can't be-"
            show sabiaemo irritated1 at left
            show ylva closedangry at right
            "Ylva took a moment, rubbing her forehead with her hand, before looking back up, the fire in her eyes a bit less bright."
            show ylva opennormal at right
            ylva "I'm sorry, Sabia. We've been through this before. We both come from such a different backgrounds."
            ylva "It might even be just a little conceited of me to expect you to approach this problem from the same position I do."
            ylva "After all... I can imagine that someone looking out for the best of Lundar over their own family's interests would be frowned upon."
            show ylva normal at right
            show sabiaemo closed2 at left
            s "(...you could say that again.)"
            show sabiaemo sad3 at left
            s "I... I'm sorry if I upset you, Ylva. I don't wish ill upon the tribe or camp."
            show sabiaemo normalopen at left
            s "Everything I've worked toward... I don't want it to just fly away in the wind."
            show ylva opennormal at right
            show sabiaemo normal at left
            ylva "I know, Sabia. But my first charge must be to help the tribe."
            ylva "I'll see you at the meeting Sabia. I'll make sure you know when it's happening."
            show ylva normal at right
            "Realizing that Ylva wanted to be left alone to rest, Sabia nodded, and left the lake."
            scene bg black with dissolve
            pause (0.1)
            scene bg centralcamp
            call sabiabase
            with dissolve
            s "A new Warchief..."
            show sabiaemo closed2 at left
            if orcalliance != "sabia":
                s "I've spent months here, trying to move forward, and if the votes land wrong, it'll all be for nothing."
            else:
                s "I've spent months here, trying to move forward. And regardless of how the votes land, it'll all be for nothing."
                s "Any one of the three captains becoming Warchief would be disastrous for me."
            show sabiaemo closed4 at left
            s "The leads for Groknak seem to have come to a bit of a standstill for now - I can't do much until we can at least meet this Kira... I need to..."
            s "Fuck, all the orcs like doing is fighting and... and..."
            show sabiaemo surprised1 at left
            "Sabia's mouth hung open, and her eyes widened a little bit as the words trailed off."
            show sabiaemo closed2 at left
            s "...fucking."
            show sabiaemo closed1 at left
            "Of course. {i}Fucking{/i}."
            show sabiaemo closed2 at left
            "She almost wanted to slap herself - it had been so obvious, right there in front of her the whole time."
            show sabiaemo pout3 at left
            "And with her history... it should have been even more plain."
            show sabiaemo normal at left
            "The orcs' relief tents."
            "Plain, boring, bare."
            "Absolutely, completely, utterly unlike her mother's own brothel."
            "One of the busiest and most expensive places in the city, and along with the more-than respectable revenue stream, a free serve of information."
            "Sabia had been so focused on thinking like a commander, like a soldier, like a warrior."
            show sabiaemo closed2 at left
            "The opportunity before her, she hadn't grasped it."
            "The power and wealth that her mother had cultivated from a brothel and a set of high class courtesans."
            "She could barely believe she hadn't realized it before."
            show sabiaemo normalopen at left
            s "I need those tents. That's my card. I'm not as proficient in it as my mother, but then I don't think orcs are quite the same customer base as nobles and aristocrats."
            s "I need those tents. I'll make them something the orcs can't live without."
            s "I never thought I'd need to take a lesson from mother so literally... but the power she had from such establishments - I can't deny it."
            s "But first I need a rest. I'll deal with this tomorrow."
            $ Sabia.stamina = 0
            jump lowerorccamp
        "Nothing":
            jump eastern_frontier_map


label ef3_mountains1:
    scene bg countryside
    if rokgrids_quest_chaos_mountains == True:
        $ rokgrids_quest_chaos_mountains = False
        call sabiabase
        "Sabia had to admit that as she passed the lake, the area had seemed to come alive since Ylva's ritual."
        "New growth, plants and flowers were lining the banks of the lake, and were even creeping up toward the mountain path."
        "A cool sweat broke out on her forehead as she climbed the mountain pathway, a hand ready on the pommel of her sword."
        "It didn't hurt to be prepared."
        "Thankfully, it didn't come to that. Sabia spotted a small plume of smoke rising into the air not far ahead, and made sure she wasn't silent as she walked into their small camp."
        $ GenericOrc1.extras = ["Loincloth", "Hair","Beard2", "Axe"]
        $ GenericOrc2.extras = ["Loincloth", "Piercing", "Wrists", "Beard1", "Axe"]
        show GenericOrc1 at center
        show GenericOrc2 at right
        with moveinright
        orc1 "Sabia. What are you doing here?"
        show sabiaemo normalopen at left
        s "Rokgrid's summoning his patrols back. Forces need to be bolstered."
        show sabiaemo normal at left
        $ GenericOrc2.face = "suspicious"
        orc2 "...Rokgrid never calls patrols back without new ones. Are you meant to be the replacement?"
        $ GenericOrc1.face = "suspicious"
        show sabiaemo normalopen at left
        s "No. I think this is an extenuating circumstance."
        show sabiaemo annoyed2 at left
        $ GenericOrc1.face = "normalopen"
        orc1 "Extann... tanoo... a what?"
        $ GenericOrc1.face = "normal"
        show sabiaemo normalopen at left
        s "Something out of the ordinary. Groknak is missing."
        show sabiaemo normal at left
        $ GenericOrc2.face = "sad2"
        orc2 "Fuck, that's not good. Warchief missing is bad for a tribe."
        show sabiaemo normalopen at left
        s "Right. And Rokgrid needs as many arms as he can get ready, just in case."
        show sabiaemo normal at left
        $ GenericOrc2.face = "normalopen"
        orc2 "C'mon-"
        if sexworktimes >= 6:
            $ GenericOrc1.face = "smile2"
            show sabiaemo annoyed2 at left
            orc1 "Hang on... maybe Sabia didn't come all the way for just that."
            orc1 "How about you have a bit of fun Sabia?"
            "The orc made it clear what he meant by 'fun', with a hand pointing to his crotch."
            show sabiaemo annoyed1 at left
            s "I don't think so."
            show sabiaemo annoyed2 at left
            $ GenericOrc1.face = "sad2"
            orc1 "C'mon. Haklor never got to fuck you when you were working in the tents. Just this once? Haklor won't tell anyone!"
            show sabiaemo annoyed2 at left
            $ GenericOrc1.face = "sad1"
            s "I'm afraid I'm not in the mood for some fun right now. Groknak's disappearance, and all."
            $ GenericOrc2.face = "smile1"
            orc2 "Karnakh thinks you're not what Sabia is after, Haklor."
            $ GenericOrc1.face = "suspicious"
            orc1 "...what Karnakh mean?"
            show sabiaemo closed2 at left
            orc2 "Maybe Sabia wants an orc that's a little better at pleasing. Like Karnakh."
            $ GenericOrc1.face = "angry"
            show sabiaemo annoyed2 at left
            s "...not quite."
            s "I'm sure you're both very sad you missed my times in the tents, but I'd like to move past that now."
            show sabiaemo angry1 at left
            s "Unless you want me to mention to Rokgrid that you'd rather try and talk me into sucking your dicks than following his orders...?"
            orc1 "UGH FINE. Haklor will go back home. Haklor just wanted to see some human titties again..."
            menu:
                "Flash Haklor and Karnakh":
                    $ sub += 1
                    show sabiaemo pout3 at left
                    s "(...maybe just a little bit. They did ask nicely after all.)"
                    scene bg countryside
                    show GenericOrc1 at center
                    show GenericOrc2 at right
                    $ GenericOrc1.face = "smile3"
                    $ GenericOrc2.face = "smile3"
                    show basenaked at left
                    show sabiaemo closed2 at left
                    show sabiaemo2 blush at left
                    with dissolve
                    $ Tpanel.extras = []
                    $ Tpanel.armor = "Nude"
                    $ Tpanel.expression = "daring (2)"
                    $ Tpanel.blush = True
                    show Tpanel at right, menu_right
                    s "Well... I can show you that much, at least."
                    show sabiaemo normal at left
                    "Sabia felt her face flush with heat, as she blushed."
                    "The orcs swiveled on the spot, mouths half agape as she lifted her top up, just enough for the fabric to slide up, past her soft flesh."
                    "Her tits almost bounced out of their confinement."
                    show sabiaemo normalopen at left
                    s "Is that... is that what you wanted to see?"
                    show sabiaemo normal at left
                    orc1 "Yes! Haklor likes that!"
                    orc2 "Karnakh too!"
                    show sabiaemo surprised1 at left
                    $ Tpanel.expression = "irritated (1)"
                    $ Tpanel.extras = ["hand1nipplegrope"]
                    "They both moved in closer to Sabia, and with one hand Haklor cupped her left breast, forefinger and thumb squeezing the nipple."
                    $ Tpanel.expression = "irritated (4)"
                    "A soft yelp rumbled in her throat as the two orcs grabbed what bared skin of Sabia they could."
                    show sabiaemo angry1 at left
                    hide Tpanel
                    s "H-hey! That's enough now. I was just being nice!"
                    show sabiaemo irritated1 at left
                    "Sabia yanked her top down, covering her breasts once more. Both Haklor and Karnakh let out a groan of disappointment."
                    scene bg countryside
                    show GenericOrc1 at center
                    show GenericOrc2 at right
                    $ GenericOrc1.face = "sad2"
                    $ GenericOrc2.face = "sad1"
                    call sabiabase
                    with dissolve
                    orc1 "You're a tease!"
                    show sabiaemo closed4 at left
                    s "I was just giving you a little reward since you and Karnakh are going back nicely without any trouble."
                    show sabiaemo angry1 at left
                    s "Don't get used to it!"
                    $ GenericOrc2.face = "smile1"
                    orc2 "Heh... maybe Sabia wants to be back in the tents."
                    $ GenericOrc1.face = "smile3"
                    orc1 "Haha... maybe Karnakh right!"
                    orc2 "Karnakh and Haklor will go back now, but don't be shy, Sabia."
                    hide GenericOrc1
                    hide GenericOrc2
                    with moveoutright
                    show sabiaemo closed2 at left
                    s "(...fuck, I think I liked that more than I thought I would.)"
                    jump eastern_frontier_map
                "Hurry them up":
                    show sabiaemo annoyed1 at left
                    s "Maybe if you do a good job Rokgrid will see about getting some more humans in the tents!"
                    show sabiaemo irritated1 at left
                    $ GenericOrc1.face = "suspicious"
                    orc1 "...maybe."
                    $ GenericOrc1.face = "sad2"
                    orc1 "Haklor would prefer human tits now. But if Sabia won't show them, fine."
                    $ GenericOrc2.face = "normalopen"
                    orc2 "Karnakh and Haklor will head back."
                    jump eastern_frontier_map
        else:
            $ GenericOrc1.face = "suspicious"
            orc1 "Just in case of what?"
            show sabiaemo annoyed2 at left
            s "He didn't give me too much information."
            s "I'm just retrieving some of the patrols, that's all. You'd have better luck asking Rokgrid yourself when you get back to Grok og Dar."
            show sabiaemo irritated1 at left
            $ GenericOrc1.face = "normalopen"
            orc1 "Hmph. You probably speak truth. Karnakh will head back."
            $ GenericOrc2.face = "normalopen"
            orc2 "So will Haklor."
            hide GenericOrc1
            hide GenericOrc2
            with moveoutright
            show sabiaemo normalopen at left
            s "Another task down."
            jump eastern_frontier_map


label ef3_remoteruins:
    scene bg countryside
    if rokgrids_quest_chaos_remoteruins == True:
        $ rokgrids_quest_chaos_remoteruins = False
        call sabiabase
        "Sabia had to admit, the ruins were a good place to station a lookout."
        "It was positioned high enough that the top tower would have had a clear view of several Eskan villages to the east."
        "And no one would make it through the passes without having to go dangerously close to the old crumbling stones."
        show sabiaemo sad1 at left
        "It also meant that she was in clear view as she approached."
        "She sorely hoped that Rokgrid had been correct that all the patrols would recognize her."
        $ GenericOrc1.extras = ["Loincloth", "Helmet", "Axe"]
        show GenericOrc1 at center with moveinright
        show sabiaemo normalopen at left
        orc1 "Sabia?"
        show sabiaemo happy3 at left
        s "Yes! It's me, Sabia. Rokgrid sent me!"
        show sabiaemo normal at left
        "Sabia let out a breath of air, just then realizing how long she'd been holding her breath."
        "Dropping her hands, she moved closer to the base of the tower, and two of Rokgrid's orcs came out to meet her."
        $ GenericOrc1.face = "smile1"
        orc1 "Sabia. Why's Rokgrid sent you? A little bit of fun perhaps?"
        $ GenericOrc1.face = "normal"
        s "You wish."
        $ GenericOrc2.extras = ["Loincloth", "Beard1", "Axe", "Shoulder"]
        show GenericOrc2 at right with moveinright
        $ GenericOrc2.face = "smile3"
        orc2 "Takgor wishes that!"
        orc1 "Takgor wishes for anything with a vagina."
        if dom>sub:
            menu:
                "Reprimand them.":
                    $ dom += 1
                    show sabiaemo angry1 at left
                    s "Really? Are you two serious right now?"
                    s "Rokgrid needs his forces bolstered, Groknak is missing, and you're happy to make stupid jokes about wanting to get your dick wet."
                    show sabiaemo annoyed2 at left
                    s "I'm surprised Rokgrid even wants you back. If I told him about this, he might not."
                    show sabiaemo annoyed1 at left
                    $ GenericOrc2.face = "sad2"
                    orc2 "S-sorry. Takgor sorry! Please don't tell Rokgrid. Rokgrid already thinks Takgor doesn't take things seriously enough..."
                    $ GenericOrc2.face = "sad1"
                    show sabiaemo annoyed2 at left
                    s "I can't imagine why."
                    s "Get the fuck back to Grok og Dar. Now. Before you do something else that will embarrass yourself."
                    show sabiaemo annoyed1 at left
                    $ GenericOrc2.face = "normalopen"
                    orc2 "Takgor won't do it again!"
                    $ GenericOrc1.face = "normalopen"
                    orc1 "Takgor probably will..."
                    "Whether Takgor would or wouldn't do it again, Sabia didn't really care. They both left for Grok og Dar immediately."
                    "Admittedly, Takgor with a bit more haste in his step than the other orc."
                    jump eastern_frontier_map
                "Let them get it out of their systems.":
                    $ GenericOrc2.face = "smile1"
                    orc2 "Takgor likes fucking sluts!"
                    orc2 "Sometimes Takgor wonder if Rekbar likes cock. Hahahahahahaha!"
                    call shake ("h")
                    $ GenericOrc1.face = "angry"
                    $ GenericOrc2.face = "sad1"
                    show sabiaemo surprised1 at left
                    "The sound of the fist hitting Takgor in his face echoed through the remnants of the stone fort, Sabia wincing. It sounded like Takgor's nose just broke."
                    orc1 "Rekbar doesn't like cock. Rekbar will go back to Rokgrid and take Takgor too, Sabia."
                    show sabiaemo normalopen at left
                    s "Uh... does he need that looked at?"
                    $ GenericOrc1.face = "smile3"
                    orc1 "Rekbar will look at it for Takgor."
                    hide GenericOrc1
                    hide GenericOrc2
                    with moveoutright
                    show sabiaemo closed2 at left
                    s "I guess being up here with just two for company might end up grating on each other's nerves."
                    s "At least I don't have to deal with that."
                    jump eastern_frontier_map
        else:
            $ GenericOrc2.face = "smile1"
            orc2 "Takgor likes fucking sluts!"
            orc2 "Sometimes Takgor wonder if Rekbar likes cock. Hahahahahahaha!"
            call shake ("h")
            $ GenericOrc1.face = "angry"
            $ GenericOrc2.face = "sad1"
            show sabiaemo surprised1 at left
            "The sound of the fist hitting Takgor in his face echoed through the remnants of the stone fort, Sabia wincing. It sounded like Takgor's nose just broke."
            orc1 "Rekbar doesn't like cock. Rekbar will go back to Rokgrid, Sabia, and take Takgor too."
            show sabiaemo normalopen at left
            s "Uh... does he need that looked at?"
            $ GenericOrc1.face = "smile3"
            orc1 "Rekbar will look at it for Takgor."
            hide GenericOrc1
            hide GenericOrc2
            with moveoutright
            show sabiaemo closed2 at left
            s "I guess being up here with just two for company might end up grating on each other's nerves."
            s "At least I don't have to deal with that."
            jump eastern_frontier_map
    menu:
        "Nothing":
            jump eastern_frontier_map


label ef3_abandoned_mine:
    scene bg countryside
    if rokgrids_quest_chaos_mines == True:
        $ rokgrids_quest_chaos_mines = False
        call sabiabase
        "The abandoned mine seemed like a reasonable place for a patrol to rest. It was well situated, and provided cover."
        "It didn't take long for Sabia's thought to be proven correct, coming across a pair of Rokgrid's orcs."
        $ GenericOrc1.extras = ["Loincloth", "Wrists", "Beard2", "Axe"]
        $ GenericOrc2.extras = ["Loincloth", "Axe", "Necklace", "Wrap", "Hair"]
        show GenericOrc2 at center
        show GenericOrc1 at right
        with moveinright
        show sabiaemo angry1 at left
        s "Hey! You two, you need to head back to Grok og Dar, quickly!"
        show sabiaemo irritated1 at left
        $ GenericOrc1.face = "suspicious"
        orc1 "Whyssat?"
        show sabiaemo normalopen at left
        s "Rokgrid needs to bolster his forces. He's concerned about what Tekrok might do."
        $ GenericOrc2.face = "angry"
        orc2 "Fucking Tekrok, that bastard!"
        orc2 "What's he doing this time?!"
        show sabiaemo normalopen at left
        s "We're not sure yet. Which is why Rokgrid needs you to return. It's better to have his forces bolstered than spread out at the moment."
        show sabiaemo annoyed2 at left
        orc1 "But why is Rokgrid worried about Tekrok? What Tekrok do?"
        show sabiaemo normalopen at left
        s "The Warchief has gone missing."
        $ GenericOrc1.face = "normalopen"
        orc1 "Groknak missing?!"
        show sabiaemo normalopen at left
        s "Yes. So you can see why Rokgrid is needing..."
        show GenericOrc2:
            xzoom -1 xpos 1.5
        show GenericOrc1:
            xzoom -1 xpos 1.5
        with move
        show sabiaemo annoyed1 at left
        s "...needs you to go back..."
        show sabiaemo irritated1 at left
        "The orcs had turned and started to head back towards Grok og Dar at a swift, easy jog, ignoring Sabia's trailing words."
        show sabiaemo annoyed1 at left
        s "Okay then. Well, I guess I can't be too upset."
        jump eastern_frontier_map
    menu:
        "Nothing":
            jump eastern_frontier_map


label ef3_forest2:
    scene bg forest
    $ renpy.block_rollback()
    menu:
        "Gain access to hunting grounds" if (recruitmentopened == True and huntingopen == False):
            call SUhuntingorc
            jump ef3_forest2
        "Go hunting ([huntingcost] stamina)" if huntingopen == True:
            if foresthunting == 0:
                if Sabia.stamina < huntingcost:
                    "Sabia was too tired to hunt."
                    jump ef3_forest2
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
                orc "Well, these are worth 6 lundils. Come back again if you want more."
                $ Sabia.stamina -= huntingcost
                $ foresthunting += 1
                $ money += 6
                $ Sabia.xp += 1
                jump ef3_forest2
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
                    "To her surprise, one of Sabia's snares caught a small deer that sold for 8 lundils."
                    "She felt like her old hunting skills were starting to come back to her, she thought she could hunt more efficiently in the future."
                elif foresthunting == 5:
                    $ money += 12
                    $ Inventory.add_item(Grayleaf)
                    scene bg forest
                    call sabiabase
                    "Several of Sabia's catches were taken by a bear or some other large animal before she could reach them, but she managed to take down a wolf with a fine pelt that sold for 12 lundils."
                    "On top of that, there was a small amount of grayleaf growing near the wolf's den. Sabia gathered the useful herb before moving on."
                elif foresthunting == 6:
                    $ money += 3
                    $ hunttrainingopen = True
                    scene bg forest
                    call sabiabase
                    "Despite her best efforts, Sabia barely managed to catch anything. But when the head hunter gave her the 3 lundils she'd earned, he looked thoughtful."
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
                    "While hunting, Sabia noticed some grayleaf glimmering on the forest floor. She gathered it quickly and went back to work, earning 9 lundils."
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
                        "Sabia attempted to hunt animals in the forest and managed to capture a few small rabbits. They sold for 11 lundils."
                    else:
                        $ money += 6
                        scene bg forest
                        call sabiabase
                        "Sabia attempted to hunt animals in the forest and managed to capture a few small rabbits. They sold for 6 lundils."
                jump ef3_forest2
            else:
                "Sabia was too tired to hunt."
                jump ef3_forest2
        "Go to meet Kia":
            if tentacle_visit == 5 and tentacle_monster_talk == 1 and v10kia_bris_follow == 0 and v10introscene == True:
                $ v10kia_bris_follow = 1
                $ Sabia.face = "normal"
                show Sabia with dissolve
                pause (1)
                hide Sabia with moveoutleft
                pause(1)
                $ Bris.face = "furrowsad"
                show Bris at right with moveinright
                bris "..."
                $ Bris.face = "furrowun"
                bris "I'd like to know where Sabia keeps going when she disappears into the forest..."
                $ Bris.face = "narrowbrowun"
                bris "It might be useful information to have."
                $ Bris.face = "furrowsad"
                "Bris tried tracking Sabia through the forest. It seemed her skill at doing so was rusty from her time spent in Grok og Dar, though."
                "She lost Sabia after half an hour."
                bris "...I'll have to keep an eye on Sabia."
                scene bg black with dissolve
                pause(0.1)
                scene bg cave
                show Sabia at left
                with dissolve
                "Sabia had a look around and could not see Kia anywhere."
                "The tentacle monster was still lingering in the back of the cave."
                "At the sight of her, it pulled itself forward slowly."
                show Tentacle behind Sabia at right with moveinright
                $ Sabia.face = "happy3"
                s "Hello... no Kia I see?"
                $ Sabia.face = "normal"
                "A few of its tentacles seemed to flop onto the ground as if it were trying to show its sadness at Sabia's statement."
                "But it seemed odd it would be upset with Kia gone."
                $ Sabia.face = "normalopen"
                s "Are you... okay?"
                $ Sabia.face = "normal"
                "It rumbled, the sound bouncing on the hard rock walls of Kia's cave."
                $ Sabia.face = "normalopen"
                s "Is that a yes... or a no?"
                $ Sabia.face = "irritated2"
                "Sabia frowned. She found it difficult to understand what it meant, or what it wanted."
                "But she felt that it was unhappy. Something was wrong - more than just the capture of it, she thought."
                $ Sabia.face = "surprised1"
                "Its body rumbled again, but this time the sound it produced was high, almost a shrill screech that stung Sabia's ears."
                "She winced."
                $ Sabia.face = "normalopen"
                s "I'll come back soon when Kia is around, okay? Then maybe we can figure out what to do with you a bit better..."
                $ Sabia.face = "normal"
                "The creature's rumble was softer this time as it pulled itself back, away from Sabia."
                "Sabia left a few minutes later, unsure when Kia would return."
                jump ef3_forest2

            if tentacle_visit == 5 and tentacle_monster_talk == 1 and v10kia_bris_follow == 2:
                $ v10kia_bris_follow = 3
                $ Sabia.face = "normal"
                show Sabia with dissolve
                pause (1)
                hide Sabia with moveoutleft
                pause(1)
                show Bris at right with moveinright
                $ Bris.face = "furrowgrit"
                bris "Sabia has had a lot more practice lately... so losing her is understandable."
                $ Bris.face = "furrowsad"
                "Bris' nose twitched as if she didn't truly believe what she had said, and was merely trying to salve her pride."
                $ Bris.face = "furrowgrit"
                bris "I'll have to keep a better eye on her... maybe trail a bit closer."
                $ Bris.face = "furrowsad"
                "This time, Bris followed Sabia a bit closer. Still far enough that she hoped Sabia would not notice."
                "In her effort to avoid being detected by Sabia though, Bris fell behind and lost track of Sabia."
                "Bris sniffed, her nose twitching in annoyance."
                $ Bris.face = "narrowbrowgrit"
                bris "Perhaps I should not have left the tracking to others in the caravan... I am out of practice..."
                $ Bris.face = "narrownormalun"
                bris "I'll have to keep a closer eye on Sabia... maybe in town as well?"
                scene bg black with dissolve
                pause(0.1)
                scene bg cave
                show Sabia at left
                with dissolve
                $ Sabia.face = "surprised1"
                $ Kia.face = "happy2"
                show Kia behind Sabia:
                    xpos 0.2
                with moveinright
                call shake ("h")
                kia "Sabia!"
                $ Kia.face = "happy1"
                "Bounding from the relative darkness of the cave's mouth into the open forest, Kia knocked into Sabia and they both tumbled over."
                $ Sabia.face = "surprised2"
                $ Kia.face = "uncertain1"
                s "...Kia!"
                "Kia frowned at Sabia's tone. She leaned in, her nose brushing against Sabia's skin as she sniffed."
                $ Sabia.face = "normal"
                $ Kia.face = "uncertain2"
                show Kia at center with move
                "Taking a step back, Kia's frown continued."
                kia "Kia sorry."
                $ Sabia.face = "happy3"
                $ Kia.face = "happy1"
                s "That's okay, Kia. Sometimes you just surprise me since I don't see you before you're already on me."
                $ Sabia.face = "normal"
                "Kia cocked her head to the side at Sabia's words."
                $ Kia.face = "uncertain1"
                kia "Not eat."
                $ Sabia.face = "normalopen"
                s "I... huh?"
                $ Kia.face = "irritated2"
                "Kia growled and grabbed Sabia's hand, yanking her into the cave."
                hide Sabia
                hide Kia
                with moveoutright
                $ Sabia.face = "normal"
                scene bg black with dissolve
                pause(0.1)
                scene bg cave
                show Sabia at left
                show Kia behind Sabia at center
                with moveinleft
                "The familiar rumbling sound of the tentacle monster was quickly audible."
                $ Kia.face = "angry2"
                "Kia snarled. Sabia didn't think it was directed at the creature, or to her."
                "It just felt like Kia was... snarling. Like Sabia might sigh."
                $ Sabia.face = "irritated2"
                "Sabia found herself dragged a few feet deeper into the cave before the grip on her wrist was relinquished."
                $ Kia.face = "irritated2"
                "Kia darted about the area, jabbing a finger at offending piles of something."
                "Looking closer, Sabia saw that the back of her cave was littered now with half-decayed berries, fruits and plants."
                "A few small rat skeletons were dotted about."
                $ Kia.face = "irritated3"
                kia "Not. Eat."
                $ Kia.face = "irritated2"
                $ Sabia.face = "normal"
                "She ran a paw over the pile of offending plant and fruit."
                $ Sabia.face = "normalopen"
                s "Well... I don't think it's a herbivore, Kia..."
                $ Sabia.face = "normal"
                $ Kia.face = "uncertain1"
                "Kia frowned."
                kia "What?"
                $ Sabia.face = "normalopen"
                s "Uh..."
                $ Kia.face = "uncertain2"
                s "It doesn't eat plants. Or fruit."
                $ Sabia.face = "normal"
                "The tentacle monster made a short warbling sound as if it were agreeing with Sabia. Or at least, with the feeling of Sabia's words."
                kia "..."
                $ Kia.face = "irritated3"
                kia "But {i}chufk{/i} want eat. Kia know. Kia bring food. Not eat!"
                $ Sabia.face = "happy2"
                $ Kia.face = "irritated1"
                s "I- well. Kia... if I brought you some oranges and apples... would you want to eat that?"
                $ Sabia.face = "normal"
                $ Kia.face = "irritated3"
                show Kia:
                    xpos 0.55
                with move
                "Kia's nose wrinkled in disgust and she took a step back from Sabia."
                kia "Not like plant."
                $ Sabia.face = "happy3"
                $ Kia.face = "angry1"
                s "Exactly. You don't eat plants."
                $ Sabia.face = "normal"
                $ Kia.face = "irritated3"
                kia "Not like plant!"
                $ Kia.face = "irritated1"
                $ Sabia.face = "normalopen"
                s "Right. And neither does the {i}chufk{/i}."
                $ Sabia.face = "normal"
                $ Kia.face = "irritated3"
                kia "{i}Chufk{/i}!"
                $ Kia.face = "irritated1"
                $ Sabia.face = "normalopen"
                s "Exactly."
                $ Sabia.face = "normal"
                "Sabia took a few seconds to walk around the area. The tentacle monster pulled back from her path as she did so."
                $ Kia.face = "uncertain1"
                "She pointed out the few rat bones lying about - and noticed more than a couple of bat remains as well."
                $ Sabia.face = "normalopen"
                $ Kia.face = "uncertain2"
                s "See? It eats meat. It doesn't eat plants."
                $ Sabia.face = "normal"
                "Kia frowned again."
                "She fell to the ground."
                $ Kia.face = "normal1"
                kia "Sit."
                "Sabia followed Kia's example, and sat down opposite the makhor."
                $ Kia.face = "irritated1"
                kia "What give? Not {i}nifsk{/i}."
                $ Sabia.face = "normalopen"
                s "Well, not. Not {i}nifsk{/i}. That was the whole point... but we can't feed it something it doesn't like. Or won't eat."
                s "It will starve."
                $ Kia.face = "uncertain2"
                kia "..."
                "Kia glanced over at the plant and fruit pile."
                $ Sabia.face = "normalopen"
                s "Remember? We wanted to teach it how to eat better... so that it can still eat meat. But not eat... the wrong meat."
                $ Sabia.face = "normal"
                $ Kia.face = "irritated3"
                kia "Eat {i}nifsk{/i} wrong."
                $ Kia.face = "angry1"
                "Sabia nodded."
                $ Sabia.face = "normalopen"
                $ Kia.face = "uncertain1"
                s "Agreed. But it could eat... old deer, or a buck after mating season?"
                $ Sabia.face = "normal"
                "Kia frowned, thinking about what Sabia had said."
                "Like usual, Sabia wasn't entirely sure if Kia had understood everything. It was clear that Kia had either not understood the initial plan..."
                "Or, perhaps the makhor had and had simply decided to try and force the creature into a plant diet?"
                $ Kia.face = "uncertain2"
                kia "..."
                $ Sabia.face = "normalopen"
                s "How about I bring back a supply of food that it will eat, while you can teach it?"
                $ Sabia.face = "normal"
                kia "What food?"
                $ Sabia.face = "normalopen"
                s "I can get some elk or venison. It likes that."
                $ Sabia.face = "normal"
                $ Kia.face = "angry2"
                kia "Not good hunt time."
                $ Sabia.face = "happy3"
                $ Kia.face = "uncertain1"
                s "I won't hunt it, I'll get it from a trader. They should have some aged stuff."
                $ Sabia.face = "normal"
                show Tentacle behind Kia at right:
                    xpos 1.4
                with moveinright
                $ Kia.face = "uncertain2"
                "The tentacle monster had crept a bit closer while Sabia and Kia had been sitting."
                "The long tendrils had writhed about, moving closer to them but still far enough to retreat if it felt threatened."
                "Its body rumbled with a high pitched warble."
                $ Sabia.face = "irritated2"
                $ Kia.face = "normal1"
                kia "Want food."
                $ Sabia.face = "normalopen"
                s "I... how do you know that?"
                $ Sabia.face = "normal"
                $ Kia.face = "normal1"
                kia "Kia know. {i}Chufk{/i} want food."
                $ Sabia.face = "normalopen"
                $ Kia.face = "tilt2"
                s "Is that what it's saying?"
                $ Sabia.face = "sad1"
                kia "..."
                "Kia frowned, seeming as confused as Sabia was."
                $ Sabia.face = "normalopen"
                $ Kia.face = "normal1"
                s "...alright."
                s "Well, I'll see if I can get some food for it and be back soon."
                $ Sabia.face = "normal"
                "The tentacle monster rumbled again. The sound seemed a bit lighter, almost happier."
                $ Kia.face = "normal1"
                kia "Okay Sabia..."
                "Kia moved hesitantly toward the back of the cave as Sabia left, pushing the pile of half decomposed fruit and plants toward the tentacle creature hopefully."
                hide Kia
                hide Tentacle
                with moveoutright
                $ Sabia.face = "normalopen"
                s "I'll have to get some food for it... since now is apparently not a good hunting time."
                $ Sabia.face = "closed4"
                s "Hopefully we can find some better arrangement with it soon... I don't think Kia is still all that fussed on it being there."
                $ Sabia.face = "normalopen"
                s "I can't blame her."
                jump ef3_forest2

            if v10kia_bris_follow == 4 and v10kia_venison == False and v10kia_nomeat_visit == False:
                $ v10kia_nomeat_visit = True
                $ Sabia.face = "normalopen"
                show Sabia at left with dissolve
                s "Hmm. Kia must not be nearby...?"
                $ Sabia.face = "normal"
                "It was unusual for Kia to not bound out to meet Sabia when she was visiting the makhor."
                scene bg cave with dissolve
                show Sabia at left with moveinleft
                "But as Sabia walked up to the cave and the tentacle monster, she made out the silhouette of the makhor just beyond the shadow of the cave's mouth."
                $ Sabia.face = "normalopen"
                s "Hi Kia?"
                $ Sabia.face = "normal"
                show Kia at center with moveinright
                "Kia turned her head toward Sabia, glancing for just a moment before returning her stare toward the dejected creature in the back of her cave."
                $ Sabia.face = "sad1"
                "The makhor was sitting on the rocky ground, teeth almost bared and with angry eyes."
                $ Sabia.face = "sad3"
                s "What's wrong, Kia?"
                $ Sabia.face = "sad2"
                "Kia's lips pulled back further, her teeth seeming bright in the soft light of the cave."
                $ Sabia.face = "sad3"
                s "Did something happen...?"
                s "The tentacle monster didn't... didn't do anything, did it?"
                $ Sabia.face = "sad1"
                show Tentacle behind Kia at right:
                    xpos 1.45
                with moveinright
                "Like it knew Sabia was talking about it, it moved forward slowly, almost hesitantly."
                "It rumbled first, before turning to a high pitched drone."
                $ Sabia.face = "sad2"
                $ Kia.face = "irritated3"
                kia "NOT. EAT."
                kia "Sabia get food. {i}Chufk.{/i}"
                $ Sabia.face = "sad3"
                s "...you're angry that it won't eat what you bring?"
                $ Sabia.face = "sad1"
                kia "{i}Chufk{/i} not eat Kia food. Not eat plant."
                $ Sabia.face = "sad3"
                s "I'll try and find something I know it will eat as soon as I can then."
                $ Sabia.face = "sad1"
                "Sabia took a few steps out. She could feel the tension Kia held, and hoped that it hadn't been a mistake to suggest that the creature stay with Kia."
                $ Sabia.face = "sad3"
                s "I'll have to get the food soon."
                jump ef3_forest2

            elif v10kia_bris_follow == 4 and v10kia_venison == False and v10kia_nomeat_visit == True:
                $ Sabia.face = "normal"
                show Sabia at left with dissolve
                $ Sabia.face = "normalopen"
                s "...I think I should look at getting some venison first, before heading back there."
                s "I know it likes venison. Fresh."
                $ Sabia.face = "closed4"
                s "I don't think Kia will be pleased to see me return without some."
                jump ef3_forest2

            elif v10kia_bris_follow == 4 and v10kia_venison == True:
                $ v10kia_bris_follow = 5
                $ Sabia.face = "normal"
                show Sabia at left
                with dissolve
                "With venison in tow, Sabia made her way back through the forest toward Kia's cave, ensuring she was as stealthy as she could be with such a large package."
                "She had barely got within sight of the cave before Kia had bounded out toward her."
                "The almost-unearthly warbling thrum of the tentacle monster was as quick to catch her attention as Kia barreling into her."
                $ Kia.face = "happy3"
                show Kia behind Sabia at left:
                    xpos -1.0
                pause(0.1)
                show Kia at left with move
                show Sabia at center with move
                call shake ("h")
                $ Sabia.face = "pout1"
                "Sabia toppled down, the package of venison tumbling from her hands."
                kia "Sabia!"
                kia "Food for {i}chufk{/i}?"
                $ Kia.face = "uncertain1"
                $ Sabia.face = "normalopen"
                s "I- ugh! Yes! Can you please hop off, Kia?"
                show Kia:
                    xpos -0.05
                with move
                $ Sabia.face = "sad1"
                $ Kia.face = "angry1"
                kia "NOT {i}nifsk{/i}?"
                show Tentacle behind Kia at right:
                    xpos 1.4
                with moveinright
                tentacle "Mmmmmrmm!"
                "The creature surged out from Kia's cave, unheedful of the open forest."
                $ Kia.face = "tilt2b"
                "Tendrils carried it on top of the venison, and its body leaned forward, beak quickly starting to devour some of the meat that Sabia had brought."
                $ Sabia.face = "normal"
                "Sabia looked back to see Kia's worried face."
                $ Sabia.face = "happy3"
                $ Kia.face = "normal1"
                s "Not {i}nifsk{/i}."
                $ Sabia.face = "normal"
                kia "..."
                $ Kia.face = "happy3"
                kia "Good."
                $ Kia.face = "normal1"
                "Kia shifted around slowly as she watched the tentacle monster eat."
                "Unlike the sad, subdued sounds it had been making the last few visits - now it seemed to be much livelier."
                $ Sabia.face = "irritated2"
                "Sabia could sense Kia's... unease? No. That's not how she would put it."
                "But Kia did not seem pleased to be around the eating creature. At least not at the moment."
                $ Sabia.face = "normalopen"
                $ Kia.face = "uncertain1"
                s "Would you like to go and play, or hunt somewhere Kia? I will stay here with the {i}chufk{/i}."
                $ Sabia.face = "normal"
                kia "...Sabia stay?"
                $ Kia.face = "uncertain2"
                kia "Sit with {i}chufk{/i}?"
                $ Sabia.face = "happy3"
                s "Yes. I will sit."
                $ Sabia.face = "irritated2"
                $ Kia.face = "happy1"
                "Kia glanced over at the tentacle monster for a brief moment. Her nose twitched, and then she turned and darted off through the forest."
                hide Kia with moveoutright
                $ Sabia.face = "normalopen"
                s "Well... she wasn't too happy with the idea of you being here to begin with, I suppose."
                $ Sabia.face = "normal"
                "Sabia mused the words to herself, albeit out loud. The creature stopped eating for a moment, and its dark eyes locked with Sabia's own."
                "Just for a moment."
                "It quickly went back to eating."
                $ Sabia.face = "normalopen"
                s "Hmm..."
                s "I still can't understand what you are trying to say... or what you want me to know."
                $ Sabia.face = "pout1"
                "Sabia sighed."
                $ Sabia.face = "normalopen"
                s "At least you're eating. I'll have to bring some more venison soon, I suppose."
                s "Until you start hunting yourself... maybe? Once Kia teaches you the right things to eat to not upset her habitat, hopefully."
                s "Though, I have to admit I'm not sure how well that will go."
                $ Sabia.face = "pout1"
                "Sabia sighed again."
                $ Sabia.face = "normal"
                "She noticed that the skin of the creature wasn't shining that same, slick and wet glean like before."
                "Maybe it didn't secrete as much slime while under stress and hungry?"
                "Whatever the reason, she wouldn't be able to get any extra lundils from that at the moment."
                "Sabia watched it eat for a few more minutes."
                $ Sabia.face = "normalopen"
                s "Well, I'll leave you alone with the food then. I have other things to attend to, and I can't stay in the forest all day."
                s "And I really don't know what to do with you..."
                s "Kia will be back soon, I'm sure."
                $ Sabia.face = "normal"
                "The creature rumbled, a deep sound that sent vibrations through the ground."
                "Almost like a cat's purr, Sabia thought."
                $ Sabia.face = "happy2"
                s "Be good for Kia? I'll be back another time."
                $ Sabia.face = "normal"
                "The tentacle answered with a quick high pitched warble."
                "Sabia left, heading back towards Grok og Dar."
                hide Sabia with moveoutleft
                "A few minutes passed as the creature continued eating. In its hunger, its attention to everything else had waned."
                $ Bris.face = "furrowsad"
                show Bris at left with moveinleft
                "Bris had succeeded in following Sabia. Though, not without making several efforts to remember to practice her forest skills."
                bris "..."
                $ Bris.face = "narrowfurrowun"
                bris "Sabia has far more secrets than I thought... a tentacle monster..."
                bris "AND a Makhor, of all things?!"
                bris "I barely even believed that they existed..."
                $ Bris.face = "furrowsad"
                "Bris mused from her vantage point."
                $ Bris.face = "narrowfurrowun"
                bris "Sabia is going to have some explaining to do... and."
                $ Bris.face = "narrownormalopen"
                bris "Hmm. This could be... {i}very{/i} useful information to have."

                "MESSAGE TO THE PLAYERS:"
                "There is a CG here, but it will be added on a later date as Nomo wished to re-do this CG and we did not wish to delay. Thanks for your patience."
                "The CG here will also be what ties the preceding parts of the quest with the following parts of this quest. Thanks for your patience."
                "Make sure to create a save before the message to the players to see the scene."
                "You can and should keep playing from here to access all the content in 0.10 patch."
                jump ef3_forest2

            scene bg cave with dissolve

            if v10kia_bris_gone == True and v10kia_bris_visit == 0:
                $ v10kia_bris_visit = 1
                $ Sabia.face = "normal"
                scene bg cave
                show Sabia at left
                with dissolve
                $ Sabia.face = "normalopen"
                s "Bris is either definitely here... or Kia is out hunting."
                $ Sabia.face = "normal"
                "She gave a quick glance around the forest as she neared Kia's cave. No bounding makhor to meet her, she was sure Kia was busy."
                $ Sabia.face = "question1"
                "Sabia couldn't help but smirking a little at the thought of Kia or the tentacle monster 'occupied' with Bris again."
                $ Sabia.face = "happy2"
                s "Though, I wouldn't be upset to see it happen again... little blackmailing slut."
                $ Sabia.face = "normal"
                "Another few steps and Sabia started to hear voices coming from within the cave."
                bris "...that!"
                kia "Fluffy!"
                bris "Ugh!"
                $ Sabia.face = "question1"
                show Bris at center:
                    xpos 0.6
                show Kia behind Bris at right
                $ Bris.face = "normalsad"
                $ Kia.face = "normal1"
                with dissolve
                "Sabia stepped into the cave. Bris was sitting in Kia's lap - perhaps not entirely of her own choice."
                "It seemed Kia was {i}very{/i} enamored with Bris' tail."
                if bris_nickname_reveal == True:
                    $ Kia.face = "happy2"
                    $ kiabris = "Fluffy"
                    $ Sabia.face = "happy2"
                    $ Bris.face = "furrowgrit"
                    s "You know Kia, her friends {i}call{/i} her Fluffy, because of that tail."
                    $ Kia.face = "happy1"
                    $ Sabia.face = "normal"
                    "Kia looked over at Sabia."
                    "After a moment of thinking, she her smile widened into a pleased grin."
                    $ Kia.face = "happy2"
                    kia "[kiabris]!"
                    $ Kia.face = "uncertain1"
                    $ Bris.face = "furrowun"
                    bris "I {i}hate{/i} that name."
                    $ Bris.face = "furrowgrit"
                    kia "..."
                    $ Sabia.face = "happy3"
                    s "Don't worry, Kia. She says she hates it... but I think she likes it."
                    $ Sabia.face = "normal"
                    "Bris glared at Sabia, doing her very best to ignore Kia's paws pulling gently at Bris' tail a few times, before stroking it softly."
                    $ Bris.face = "narrownormalsad"
                    $ Kia.face = "uncertain2"
                    kia "Not... like?"
                    "Kia frowned, her paws moving from Bris down to her own sides."
                    $ Bris.face = "narrownormalun"
                    $ Kia.face = "happy1"
                    bris "I mean... well. I guess if you want to call me Fluffy, it's fine."
                    bris "I suppose."
                    bris "Just make sure you keep that thing away from me."
                    $ Bris.face = "narrownormalsad"
                    "Bris pointed toward the back of the cave. The tentacle monster rumbled sadly in reply."
                    $ Sabia.face = "happy3"
                    $ Kia.face = "happy2"
                    s "See, Kia? I told you it would be fine."
                    $ Sabia.face = "normal"
                    "Bris locked eyes with Sabia, her glare seething."
                else:
                    $ Sabia.face = "happy2"
                    $ Bris.face = "narrownormalsad"
                    s "I see you two are making good friends."
                    $ Kia.face = "happy2"
                    s "Kia is very fond of catgirls, you know."
                    bris "..."
                    $ Bris.face = "narrownormalun"
                    $ Kia.face = "happy1"
                    bris "I hadn't noticed."
                    $ Bris.face = "narrownormalsad"
                    "Kia looked from Sabia to Bris and smiled, running a hand over Bris' tail gently."
                    "The tentacle monster rumbled happily, moving closer to the pair."
                    $ Sabia.face = "irritated2"
                    $ Bris.face = "narrownormalun"
                    bris "Hey, you stay back there."
                    $ Kia.face = "uncertain1"
                    bris "You're not coming near me again. Take your food."
                    $ Bris.face = "narrownormalsad"
                    "The tentacles paused, and then the creature moved backward."
                    "A high pitched, almost sad sound bounced off the walls as it retreated."
                    $ Sabia.face = "normal"
                "Sabia could see the tension in Bris' shoulders disappear as the tentacle monster obeyed, retreating to the rear of the cave with the venison."
                "She was bristling under Kia's ministrations still, but whether she was too afraid to try and break free of the makhor's grip or something else - Sabia could not tell."
                $ Kia.face = "happy2"
                kia "[kiabris] smell good!"
                "She nodded emphatically to herself."
                $ Sabia.face = "question1"
                $ Bris.face = "browgrit"
                kia "Not. Eat."
                $ Bris.face = "browsurprise"
                $ Kia.face = "happy1"
                bris "I... what?!"
                $ Bris.face = "browun"
                bris "I would hope not..."
                $ Sabia.face = "happy2"
                $ Bris.face = "browsad"
                s "Don't worry, she doesn't mean it like that."
                $ Sabia.face = "normalopen"
                s "It's more of a... well, I'm sure you'll get used to talking to Kia with more venison deliveries."
                $ Sabia.face = "normal"
                $ Bris.face = "narrownormalsad"
                $ Kia.face = "happy2"
                kia "[kiabris] sit more?"
                $ Kia.face = "happy1"
                "Sabia nodded."
                $ Sabia.face = "normalopen"
                s "Yes, she will be. At least until we get that tentacle monster familiar with more... Kia-approved hunting methods."
                $ Sabia.face = "normal"
                $ Bris.face = "narrownormalhappy"
                $ Kia.face = "happy2"
                kia "Good! Kia like [kiabris]."
                $ Sabia.face = "normalopen"
                s "I figured. Well, I'll leave you alone for now. But don't be too long, Bris. The tents won't run themselves after all."
                $ Sabia.face = "normal"
                $ Bris.face = "narrownormalun"
                bris "I'll go back now."
                $ Bris.face = "narrownormalsad"
                $ Kia.face = "irritated2"
                "Bris moved to extricate herself from Kia's lap and grip, but the makhor clutched the small catgirl tighter."
                kia "SIT!"
                $ Sabia.face = "question1"
                "Bris looked at Sabia with pleading eyes."
                menu:
                    "Leave Bris with Kia.":
                        $ A_bris -= 1
                        $ dom += 1
                        $ Sabia.face = "normalopen"
                        $ Bris.face = "narrownormalgrit"
                        $ Kia.face = "happy1"
                        s "I think sitting is a good idea."
                        $ Sabia.face = "happy2"
                        s "You can stay here with Kia for now."
                        $ Sabia.face = "question1"
                        $ Bris.face = "narrownormalun"
                        bris "What?! But-"
                        $ Bris.face = "narrowfurrowgrit"
                        s "..."
                        $ Sabia.face = "happy2"
                        s "Yes?"
                        $ Sabia.face = "question1"
                        $ Bris.face = "narrownormalun"
                        $ Kia.face = "happy2"
                        bris "...nothing."
                        $ Bris.face = "narrownormalsad"
                        "Sabia gave a smug nod before leaving."
                        $ Sabia.face = "normal"
                        "Kia wouldn't do anything, and she was sure she had made it clear that Bris wasn't to be used in any mating..."
                        "But she wouldn't be too disappointed to hear that Kia had misunderstood, or the tentacle monster had found Bris too much of a treat."
                        jump eastern_frontier_map
                    "Take Bris back.":
                        $ v10kia_bris_gone = False
                        $ A_bris += 1
                        $ Sabia.face = "normalopen"
                        $ Bris.face = "narrownormalhappy"
                        $ Kia.face = "uncertain1"
                        s "Alright. Come on, Bris."
                        $ Sabia.face = "happy3"
                        s "Sorry Kia... but I need Bris back to help me out in camp, alright?"
                        $ Kia.face = "uncertain2"
                        $ Sabia.face = "normal"
                        kia "..."
                        "Kia's lips pulled back a little, teeth glinting."
                        $ Sabia.face = "happy2"
                        s "I'll send her back soon, don't worry. She'll need to deliver the meat for the tentacle monster, anyway."
                        $ Sabia.face = "normal"
                        "Bris wriggled out of Kia's reluctant grip, and followed Sabia back to camp."
                        jump eastern_frontier_map

            if v10kia_bris_gone == True and v10kia_bris_visit == 2:
                $ v10kia_bris_visit = 3
                $ Sabia.face = "normal"
                $ Bris.face = "normal"
                $ Kia.face = "normal1"
                scene bg cave
                show Sabia at left
                with dissolve
                "Sabia was surprised to hear less arguing and commotion than last time."
                show Bris at center
                show Kia at right
                with dissolve
                $ Sabia.face = "normalopen"
                s "Hmm, you two seem to be getting along better."
                $ Sabia.face = "normal"
                $ Bris.face = "normalhappy"
                $ Kia.face = "happy2"
                kia "Yes!"
                $ Kia.face = "happy1"
                "Kia nodded enthusiastically, sitting on the ground across from Bris."
                $ Bris.face = "narrownormalopen"
                bris "Kia's not so bad. She's just very... affectionate."
                $ Bris.face = "normalsad"
                kia "{i}Yrrkit!{/i}"
                $ Bris.face = "normalopen"
                bris "Though I don't know what that means."
                $ Bris.face = "normalhappy"
                $ Sabia.face = "normalopen"
                s "It's a special word that she has for catgirls... though I think there's more meaning to it than just denoting a catgirl."
                $ Sabia.face = "normal"
                $ Bris.face = "normalopen"
                $ Kia.face = "uncertain1"
                bris "I see."
                $ Bris.face = "normalhappy"
                "Kia pushed some of the food that she had between the two of them toward Bris."
                show Tentacle behind Kia at right:
                    xpos 1.4
                with moveinright
                "Quickly, the tentacle monster started to pull itself out and toward the group of them."
                "It rumbled softly."
                $ Sabia.face = "question1"
                $ Bris.face = "normalsad"
                $ Kia.face = "neutralE"
                kia "Sorry. [kiabris] not sit."
                $ Bris.face = "normalun"
                $ Kia.face = "tilt2"
                bris "What... do you mean? I'm sitting right now."
                $ Bris.face = "normalsad"
                "Sabia shook her head."
                $ Sabia.face = "normalopen"
                $ Kia.face = "uncertain2"
                s "That's... not quite what she's saying. I think it's directed toward the tentacle monster, and that you don't want it too close to you."
                $ Sabia.face = "normal"
                $ Bris.face = "normalgrit"
                $ Kia.face = "normal1"
                kia "{i}Chufk{/i} want sit. Bris not like. Not sit."
                $ Bris.face = "narrownormalun"
                bris "I suppose it's fine if it comes closer. As long as it doesn't-"
                $ Bris.face = "narrownormalsad"
                "Bris flushed red for a few moments."
                $ Sabia.face = "question1"
                $ Bris.face = "browsurprise"
                $ Kia.face = "happy2"
                kia "Mate?"
                $ Sabia.face = "happy3"
                $ Kia.face = "happy1"
                s "Hah. I think that's what Bris meant, yes."
                $ Sabia.face = "normal"
                $ Bris.face = "browsad"
                bris "..."
                show Tentacle:
                    xpos 1.35
                with move
                "The tentacle monster trilled happily and inched closer, one of its tendrils writhing out across the ground to gently tap Bris on the leg."
                $ Kia.face = "uncertain1"
                "Without speaking, Bris grabbed it with two fingers and pulled it off, her nose wrinkling."
                "It pulled its tentacles back in towards itself, its body leaning forward just slightly. It rumbled slowly, a low drawn out thrum."
                $ Kia.face = "tilt2b"
                kia "{i}Chufk{/i} sad..."
                $ Sabia.face = "question1"
                $ Bris.face = "narrownormalun"
                $ Kia.face = "uncertain2"
                bris "It will just have to be sad then."
                "Seeing that Bris was getting along a bit better and that the tentacle monster was much perkier - albeit temporarily sad - Sabia felt it was best to leave the three alone for now."
                $ Sabia.face = "normalopen"
                s "Don't be gone too long. The tents need your administration after all, Bris. I'll see you there later."
                $ Sabia.face = "normal"
                $ Kia.face = "uncertain1"
                "Sabia left while Bris was preoccupied with removing another apologetic tentacle from her leg."
                scene bg black with dissolve
                jump eastern_frontier_map

            if kia_tentacle_quest == 1:
                $ kia_tentacle_quest = 3
                $ A_kia += 1
                "As promised, Sabia came to help Kia the following morning."
            if kia_tentacle_quest == 2:
                $ kia_tentacle_quest = 3
                $ A_kia -= 2
                "Sabia hoped that Kia wouldn't be too mad that she hadn't come the following morning."
            jump ef3_forest2_kia
        "Go back":
            jump eastern_frontier_map


menu ef3_forest2_kia:
    "Ask Kia for help tracking Groknak" if groknak_missing == True and chaos_kia_help == False and chaos_maply_help == False and groknak_route_prompt == True:
        $ chaos_kia_help = True
        call sabiabase
        "Kia wasn't at her cave, but Sabia knew that she would be back at some point."
        "She had a suspicion that Kia was very well aware of who, or what, was at her cave even if not there."
        "Sure enough, after only a short while Kia popped up next to Sabia, out of nowhere."
        show kia happy2 at right with moveinright
        kia "Hello Sabia!"
        show sabiaemo normalopen at left
        s "Hi Kia. I have a problem."
        show sabiaemo normal at left
        show kia pawtilteager1 at right
        kia "What problem?"
        show sabiaemo normalopen at left
        s "Well, I'm not sure if you've talked to Ylva about it, but remember how my pack turned on me, and I want-"
        show sabiaemo normal at left
        show kia pawtiltsorry at right
        kia "No! Problem - what mean?"
        show sabiaemo happy1 at left
        s "Oh!"
        s "Well, a problem is where something is wrong, and I need to fix it, I suppose. Not what it should be."
        show sabiaemo normal at left
        show kia pawtiltconfused at right
        "Kia frowned, and thought about Sabia's words for a few moment before speaking a bit slower."
        kia "Like when hungry and no food? Problem?"
        show sabiaemo happy1 at left
        show kia happy2 at right
        s "Right! Like that."
        show kia neutralE at right
        show sabiaemo closed2 at left
        kia "Hunt and eat, mean not hungry. Problem gone?"
        show sabiaemo happy1 at left
        s "Exactly, Kia! But my problem isn't so easy to fix. Groknak's missing, and I need to track him down."
        show kia pawtiltconfused at right
        "Once more, Kia frowned."
        kia "Sabia said orcs not food."
        show sabiaemo normalopen at left
        s "No, no."
        s "I don't want to... eat him. Groknak said he would help me against my pack, the ones that betrayed me. But if he's gone, he can't help me - that's my problem."
        show sabiaemo normal at left
        show kia pawtiltcurious at right
        kia "Hmm..."
        show kia pawtilteager2 at right
        kia "Okay. Help Sabia!"
        show kia pawtiltconfused at right
        kia "...how help?"
        show sabiaemo happy1 at left
        show kia happy4 at right
        s "You're good at tracking things down, right?"
        show kia happy3 at right
        kia "Best!"
        kia "Help now?"
        menu:
            "Yes, now, thank you!":
                $ chaos_kia_help_early = True
                show sabiaemo happy3 at left
                jump ef3_groknaks_route
            "Not right now Kia!":
                show kia pawuncertain1 at right
                kia "Why no help now?"
                show sabiaemo normalopen at left
                show kia uncertain2 at right
                s "There's a few things I have to do first, Kia. It's complicated. Can I come here when I'm ready?"
                show kia happy3 at right
                show sabiaemo happy3 at left
                kia "Okay! Sabia come cave for help!"
                "Grinning, Kia licked Sabia's face before bounding off."
                hide kia with moveoutright
                show sabiaemo normalopen at left
                s "Having Kia help will make tracking it down easy, I think."
        jump ef3_forest2
    "Ask Kia for help tracking Groknak" if chaos_kia_help == True and chaos_kia_help_early == False:
        call sabiabase
        show kia happy3 at right
        kia "Help now?"
        menu:
            "Yes, now, thank you!":
                $ chaos_kia_help_early = True
                show sabiaemo happy3 at left
                jump ef3_groknaks_route
            "Not right now Kia!":
                show kia pawuncertain1 at right
                kia "Why no help now?"
                show sabiaemo normalopen at left
                show kia uncertain2 at right
                s "There's a few things I have to do first, Kia. It's complicated. Can I come here when I'm ready?"
                show kia happy3 at right
                show sabiaemo happy3 at left
                kia "Okay! Sabia come cave for help!"
                "Grinning, Kia licked Sabia's face before bounding off."
                hide kia with moveoutright
                show sabiaemo normalopen at left
                s "Having Kia help will make tracking it down easy, I think."
        jump ef3_forest2
    "Ask Kia about the Tentacle Monster" if kia_tentacle_quest == 3:
        $ Kia.face = "normal1"
        scene bg cave
        show Sabia at left
        show Kia at right
        $ kia_tentacle_quest = 4
        $ Kia.face = "happy2"
        kia "Sabia! You come."
        $ Kia.face = "happy4"
        $ Sabia.face = "happy3"
        s "Of course, Kia. You've helped me, and I'll be happy to help you if I can."
        $ Sabia.face = "normalopen"
        s "You mentioned {i}chufk{/i}... that's the tentacle monster Neve and I dealt with before, isn't it?"
        $ Sabia.face = "normal"
        $ Kia.face = "irritated3"
        kia "Not tell Neve!"
        $ Kia.face = "irritated2"
        $ Sabia.face = "normalopen"
        s "I... why not?"
        $ Sabia.face = "normal"
        $ Kia.face = "uncertain2"
        kia "Not tell. Please."
        $ Sabia.face = "normalopen"
        s "Well... she knows more about tentacle monsters than I do, but if you don't want me to Kia, I won't."
        s "But I'll need to know what the problem is."
        $ Sabia.face = "normal"
        $ Kia.face = "angry2"
        kia "{i}Chufk{/i} come back!"
        $ Kia.face = "irritated3"
        kia "Hunt Kia area!"
        $ Sabia.face = "normalopen"
        s "Stealing your area..."
        s "Do you mean it's invading your territory?"
        $ Sabia.face = "normal"
        $ Kia.face = "irritated3x"
        kia "Hunt area!"
        $ Kia.face = "irritated2"
        $ Sabia.face = "normalopen"
        s "I think I understand, Kia."
        s "But I'm not sure what you want me to help with. Neve and I didn't exactly attack or kill it when we managed to track it down..."
        $ Sabia.face = "happy3"
        s "And you're far more skilled at hunting than I am."
        $ Sabia.face = "irritated2"
        $ Kia.face = "irritated3"
        kia "Kia good hunt. {i}Chufk{/i} hard. Hide!"
        kia "{i}Chufk{/i} escape!"
        $ Kia.face = "irritated2"
        kia "Sabia help catch."
        $ Kia.face = "happy2"
        kia "Kia kill."
        $ Kia.face = "irritated2"
        $ Sabia.face = "normalopen"
        s "I'm surprised you're asking for help Kia. I wouldn't think you would have trouble with this."
        $ Sabia.face = "normal"
        $ Kia.face = "irritated3"
        kia "{i}Wakst{/i} Kia kill easy. Rip {i}chufk{/i} from ground. Kill!"
        $ Sabia.face = "sad2"
        "Kia huffed, and Sabia felt she had offended her friend."
        $ Sabia.face = "normalopen"
        $ Kia.face = "pawtiltconfused"
        s "{i}Wakst{/i} Kia... you mean, your other form?"
        $ Sabia.face = "normal"
        kia "What form?"
        $ Sabia.face = "normalopen"
        s "Like when we met in the Arena, before you were like you are now?"
        $ Sabia.face = "normal"
        $ Kia.face = "happy3"
        kia "Yes! {i}Wakst{/i} Kia. Kill easy."
        $ Kia.face = "irritated3"
        kia "Small Kia... kill {i}chufk{/i} hard. {i}Chufk{/i} fast."
        $ Kia.face = "irritated2"
        $ Sabia.face = "normalopen"
        s "Why don't you change back to deal with the problem then?"
        $ Sabia.face = "normal"
        $ Kia.face = "irritated3"
        kia "No change!"
        kia "Take long. {i}Chufk now{/i}."
        $ Kia.face = "irritated2"
        $ Sabia.face = "normalopen"
        s "So it takes a long time for you to be able to change form?"
        $ Kia.face = "irritated3"
        kia "YES."
        $ Sabia.face = "normalopen"
        $ Kia.face = "irritated2"
        s "How long does it take before you can change back?"
        $ Kia.face = "irritated1"
        "Kia frowned."
        kia "Long."
        $ Sabia.face = "closed2"
        s "(I guess I'm not finding out how long it takes anytime soon... but maybe I can find out another time.)"
        $ Sabia.face = "normalopen"
        s "I really think Neve would be able to help-"
        $ Sabia.face = "surprised1"
        $ Kia.face = "irritated3x"
        kia "NO!"
        kia "NO NEVE."
        $ Sabia.face = "sad2"
        $ Kia.face = "irritated3"
        kia "{i}SABIA{/i} help. Neve no help."
        $ Sabia.face = "normalopen"
        $ Kia.face = "irritated2"
        s "Okay okay. I don't understand why, but if it's that big of a deal, we can try and resolve this without Neve's help."
        $ Sabia.face = "normal"
        $ Kia.face = "happy3"
        kia "Good."
        kia "Go now. Find {i}chufk{/i}!"
        $ Sabia.face = "normalopen"
        $ Kia.face = "happy1"
        s "Do you know where it is?"
        $ Sabia.face = "normal"
        $ Kia.face = "irritated1"
        kia "{i}Chufk{/i} move lot."
        $ Sabia.face = "normalopen"
        s "Well, find where it has most recently been, Kia. I'll need to ask Neve about it - but don't worry, I won't say anything about you."
        $ Sabia.face = "normal"
        $ Kia.face = "irritated3"
        kia "Sabia, please. Now. Not wait."
        $ Sabia.face = "sad2"
        $ Kia.face = "neutralE"
        kia "Kia have area. Big area. All Kia. Hunt and eat like Kia want. Kia choose hunt or play. {i}Chufk{/i} ruin! {i}Chufk{/i} steal Kia area, steal Kia hunt."
        kia "Please."
        "Kia's chest was rising and falling, and a mix of distress, discomfort and anger were all broiling in her eyes."
        "It was the most Kia had ever spoken at once, and Sabia felt just how important this issue was to Kia."
        $ Sabia.face = "sad3"
        s "I promise I will help Kia, but last time when Neve and I managed to get close to it - it could have gotten away easily if it wanted to."
        s "We had no ability to keep it there any longer than it wanted to stay."
        s "If we're going to get rid of it, or force it to move out of your territory, I'm going to need to think of something, or get something to help."
        $ Sabia.face = "sad1"
        $ Kia.face = "irritated1"
        "Kia growled, her paws flexing and dangerously sharp claws extending."
        kia "Not like."
        $ Sabia.face = "normalopen"
        s "I can understand Kia. I will try my best to be fast."
        $ Sabia.face = "normal"
        $ Kia.face = "irritated2"
        "Kia growled again, but reluctantly nodded."
        "Sabia suspected it must be almost inconceivably hard for the makhor to suppress her instincts in favor of waiting for Sabia."
        "Nevertheless, Sabia felt this was the correct path. She left Kia's cave."
        jump ef3_forest2

    "Track the Tentacle Monster with Kia (200 stamina)" if kia_tentacle_quest == 4 or kia_tentacle_quest == 5:
        $ Kia.face = "normal1"
        $ Sabia.face = "normal"
        show Sabia at left
        show Kia at right
        with dissolve
        $ Kia.face = "happy3"
        kia "Hunt now, Sabia?"
        $ Sabia.face = "normalopen"
        $ Kia.face = "irritated2"
        s "Not yet, I still need to prepare a few things to lure the monster out."
        $ Sabia.face = "sad1"
        "Kia growled at the answer, baring her fangs. She clearly was not impressed with having to wait. She bounded off before Sabia could get another word in."
        jump ef3_forest2_kia

    "Track the Tentacle Monster with Kia (200 stamina)" if kia_tentacle_quest == 6:
        $ Kia.face = "normal1"
        $ Sabia.face = "normal"
        show Sabia at left
        show Kia at right
        with dissolve
        $ Kia.face = "happy3"
        kia "Hunt now, Sabia?"
        $ Sabia.face = "normalopen"
        $ Kia.face = "irritated2"
        s "Not yet, I still need to prepare a few things to lure the monster out."
        $ Sabia.face = "sad1"
        "Kia growled at the answer, baring her fangs. She clearly was not impressed with having to wait. She bounded off before Sabia could get another word in."
        jump ef3_forest2_kia

    "Track the Tentacle Monster with Kia (200 stamina)" if kia_tentacle_quest == 7:
        if Sabia.stamina < 200:
            "Sabia is too tired to do this right now."
            jump ef3_forest2
        $ Sabia.stamina -= 200
        $ kia_tentacle_quest = 8
        $ Kia.face = "normal1"
        $ Sabia.face = "normal"
        show Sabia at left
        show Kia at right
        with dissolve
        "Kia and Sabia left the cave."
        scene bg black with dissolve
        pause (0.01)
        scene bg countryside
        show Sabia at left
        show Kia at right
        with dissolve
        "Sabia really had no idea what to expect. The tentacle monster had shown some signs of understanding when she and Neve had encountered it last."
        $ Sabia.face = "closed2"
        "Would it know that Kia was hunting it? Or was it entirely oblivious to angering a makhor?"
        hide Kia with moveoutright
        $ Sabia.face = "normal"
        "Sabia's musings made her walk slower than Kia wanted, and she caught the flash of red as Kia bounded back toward her from far ahead."
        $ Kia.face = "happy3"
        kia "Sabia! Hurry! Not slow. Come, come!"
        $ Kia.face = "happy1"
        "Nodding, Sabia picked her pace up a little bit."
        "They travelled deeper into the forest, and it wasn't long before Kia was once more getting farther and farther away as Sabia's pace slackened."
        $ Sabia.face = "normalopen"
        s "Keeping up with a makhor wasn't something a human was meant to do at all."
        $ Sabia.face = "irritated2"
        $ Kia.face = "neutralE"
        "Just when Sabia's legs were starting to burn and ache, Kia stopped. Sabia took a few moments to catch up."
        show Sabia:
            linear (2.0) xoffset (1200)
        pause (0.01)
        scene bg black with dissolve
        pause (0.01)
        scene bg emptycave
        show Sabia at left
        show Kia at right
        with dissolve
        "The forest floor lead down into a small hollow. The sides were a rich green with moss, and the cave's opening was dark."
        "Kia paced around the edges of the hollow, peering in as Sabia clambered down the rough walls."
        "It didn't feel like there was anything here to Sabia. Not like last time."
        $ Sabia.face = "normalopen"
        s "Kia, I'm not sure anything is here."
        $ Sabia.face = "normal"
        kia "..."
        $ Kia.face = "pawsad1"
        kia "{i}Chufk{/i} here before..."
        $ Sabia.face = "normalopen"
        s "Could it have left?"
        $ Sabia.face = "normal"
        $ Kia.face = "neutralE"
        kia "...yes."
        kia "{i}Chufk{/i} not stop."
        $ Kia.face = "irritated1"
        kia "Catch hard."
        $ Sabia.face = "normalopen"
        s "That makes sense. I'll have a look around, at least."
        $ Sabia.face = "normal"
        $ Kia.face = "irritated2"
        "Kia frowned, clearly wanting to simply go to the next nest she knew of."
        "But it seemed she valued Sabia's help enough to overcome her instincts."
        "Kia continued circling about as Sabia inspected the hollow closer."
        scene bg black with dissolve
        pause (0.01)
        scene bg emptycave
        show Sabia at left
        with dissolve
        menu empty_hole1_menu:
            "Cave Entrance" if empty_hole1_ce == False:
                $ empty_hole1_ce = True
                "Looking a bit closer to the entrance to the cave, Sabia couldn't really spot anything out of the ordinary."
                "It was rocky, dark, and all around very much a cave."
                jump empty_hole1_menu
            "Walls" if empty_hole1_walls == False:
                $ empty_hole1_walls = True
                "The walls of the hollow had a soft glimmer to them."
                "Upon closer inspection, Sabia recognized it as dried tentacle slime. The creature had clearly been here."
                $ Sabia.face = "irritated2"
                "Unfortunately, it being dry meant that Sabia was not able to salvage any. Even a small amount was worth a lot."
                $ Sabia.face = "normal"
                jump empty_hole1_menu
            "Cave Mouth" if empty_hole1_cm == False:
                $ empty_hole1_cm = True
                "Sabia took a few moments to adjust to the darkness of the cave as she entered the threshold."
                "The area was mostly bare."
                "The only exception was the walls still held a little bit of wet tentacle slime. The farther in she moved, the more there was."
                $ Sabia.face = "irritated2"
                "Trying to scrape some off proved difficult. It seemed as dry as the slime outside upon touching it."
                "The cave narrowed quickly into a small hole that was no bigger than a minotaur's head."
                $ Sabia.face = "irritated1"
                "Capturing a tentacle monster was going to prove a lot more difficult than just getting some of its slime, if it could squeeze through spaces that tight."
                jump empty_hole1_menu
            "Head back up to Kia.":
                "Sabia climbed back out of the small hollow."
        scene bg black with dissolve
        pause (0.01)
        scene bg emptycave
        show Sabia at left
        show Kia at right
        with dissolve
        $ Kia.face = "uncertain1"
        kia "What find?"
        $ Kia.face = "neutralE"
        $ Sabia.face = "normalopen"
        s "Not much, sorry, Kia. There was a bit of slime left on the walls, though it was dry."
        s "And it seems like it is able to squeeze through very narrow spaces. That's going to make it difficult to catch."
        $ Sabia.face = "normal"
        $ Kia.face = "irritated2"
        kia "Not find."
        $ Sabia.face = "sad3"
        s "Not find. Sorry, Kia. We can look at another nest tomorrow."
        $ Sabia.face = "sad1"
        $ Kia.face = "irritated3"
        "Kia's fangs were bared as she growled down toward the hollow, before taking Sabia back to a part of the forest she could find her way from."
        scene bg black with dissolve
        pause (0.01)
        jump eastern_frontier_map

    "Track the Tentacle Monster with Kia (200 stamina)" if kia_tentacle_quest == 8:
        if Sabia.stamina < 200:
            "Sabia is too tired to do this right now."
            jump ef3_forest2
        $ Sabia.stamina -= 200
        $ kia_tentacle_quest = 9
        $ Kia.face = "normal1"
        $ Sabia.face = "normal"
        show Sabia at left
        show Kia at right
        with dissolve
        $ Kia.face = "happy3"
        kia "Kia find! {i}Chufk{/i}!"
        kia "Come Sabia!"
        hide Kia with moveoutright
        "Like before, Kia bounded off, ahead of Sabia."
        show Sabia:
            linear (2.0) xoffset (1200)
        pause (0.01)
        scene bg black with dissolve
        pause (0.01)
        "Though Sabia did her best to follow, Kia kept gaining distance, and had to round back a few times."
        "They went through the forest, a different direction than the initial nest location."
        scene bg black with dissolve
        pause (0.01)
        scene bg emptycave
        show Sabia at left
        show Kia at right
        with dissolve
        "After some times, they came to the place Kia had sniffed out."
        "Unlike the last, this one was not a hollow. Rather, it was a large cave mouth that slowly grew from the surrounding terrain."
        "Sabia could see the telltale signs of tentacle slime glistening on the ground."
        hide Kia with moveoutright
        "Before Sabia could ask Kia to wait, Kia had left her side and darted into the cave."
        "After a few seconds, Kia's echoing howl of disappointment rumbled through the cave."
        $ Kia.face = "neutralE"
        show Kia with moveinright
        "She re-emerged, a frown on her face."
        kia "Not here."
        kia "Sabia look?"
        $ Sabia.face = "normalopen"
        $ Kia.face = "normal1"
        s "Yes, I'll have a look around again. Although it's not here, we might be able to find something. Hopefully."
        $ Sabia.face = "normal"
        $ Kia.face = "irritated1"
        kia "..."
        $ Sabia.face = "sad1"
        kia "...okay."
        "Sabia could tell Kia was displeased with the lack of finding a tentacle monster."
        menu empty_hole2_menu:
            "Cave Entrance" if empty_hole2_ce == False:
                $ empty_hole2_ce = True
                "The forest floor gave way to stones and rocks closer to the cave. There was a dry layer of slime over most of it, though Sabia wasn't sure if it stopped at the vegetation, or continued farther."
                "It seemed like the tentacle monster had been gone long enough for the underbrush to grow over any remnants left behind."
                jump empty_hole2_menu
            "Enter the Cave" if empty_hole2_ce == True:
                scene bg black with dissolve
                pause (0.01)
                scene bg emptycave
                show Sabia at left
                with dissolve
                "It took a few moments for Sabia's eyes to adjust to the light in the cave."
                "Still, it seemed more promising than the previous nest."
                "She could see that the back of it went down gently, below ground level, but it was wide enough that she would be able to go at least a short distance to inspect."
                menu empty_hole2_insidecave_menu:

                    "Bones" if empty_hole2_bones == False:
                        $ empty_hole2_bones = True
                        "Sabia spotted a pile of bones. She would have suspected the bones to be littered about, but it seemed the tentacle monster liked to keep its home clean."
                        "Squatting down, she picked through the bones. Though there were definitely some bear bones there - the cave's last inhabitant, she surmised, they weren't the sole type."
                        "There was a large amount of smaller bones."
                        "They had been stripped clean of any meat."
                        $ Sabia.face = "normalopen"
                        s "Looks like it enjoys rabbits. At least, I can't really think of anything else that would have bones like that."
                        s "There are definitely more rabbit bones than anything else."
                        s "That must mean it ventures out farther than the cave for food, though. I can't see many rabbits into a cave."
                        s "Rabbits might be good bait for luring it out."
                        $ Sabia.face = "normal"
                        jump empty_hole2_insidecave_menu

                    "Walls" if empty_hole2_walls == False:
                        $ empty_hole2_walls = True
                        "The walls were coated in tentacle slime. There were a few patches where it was still damp to the touch."
                        "Sabia wasn't sure whether it was because the creature may have been here more recently than the other nest, or whether perhaps the cave had shielded it from drying out as quickly."
                        jump empty_hole2_insidecave_menu

                    "Deeper in the cave" if empty_hole2_deeper == False:
                        $ empty_hole2_deeper = True
                        "Not knowing what she might find, or what she was looking for - being able to go deeper into a system where the tentacle had been might be illuminating."
                        "The nest she had visited with Neve, and the last one with Kia had both been so small and tight that exploring deeper would have been impossible."
                        "Her feet started to make a wet squelching sound as she walked, and an odd scent filled the air."
                        "Running her hand along the wall, Sabia realized that the slime was still quite damp here."
                        "She tried to scoop some of it into a vial, but it was spread out thinly enough that it proved impossible."
                        "There was still a dim light that managed to reach from the entrance back this far."
                        "It caught on something hanging from the roof of the cave, and Sabia froze."
                        "For a moment, she waited, until realizing it was nothing alive."
                        "It was like a piece of rope, hanging from the roof and anchored to one of the walls."
                        "Sabia ran a finger over it."
                        $ Sabia.face = "normalopen"
                        s "That's... like tentacle slime, almost. But... a bit different. Thicker, and a bit stickier."
                        $ Sabia.face = "irritated2"
                        "Sabia touched her forefinger and thumb together and squished the stuff between her two digits, and pulled her fingers apart."
                        "It stretched slowly, straining against Sabia's efforts and trying to keep her fingers together."
                        $ Sabia.face = "normalopen"
                        s "Interesting."
                        $ Sabia.face = "normal"
                        "Sabia took a few steps deeper into the cave, and more and more of the slime ropes were evident, until they blocked off her path."
                        "They criss crossed in haphazard order, blocking her off. Almost like a spider's web."
                        $ Sabia.face = "normalopen"
                        s "Hmm, Neve never mentioned anything like this. I wonder if it's well known?"
                        s "I better take a sample of this. It could be worth something."
                        $ Sabia.face = "normal"
                        "Sabia cut a small segment of what - for now - she called the tentacle web."
                        "She put it in a small container she had with her."
                        $ Sabia.face = "normalopen"
                        s "Well, unless I want to be a fly in a web, I think that's as far as I'm going down here."
                        $ Sabia.face = "normal"
                        "Sabia retraced her steps up to the mouth of the cave."
                        jump empty_hole2_insidecave_menu
                    "Leave":

                        if empty_hole2_deeper == False:
                            s "I had better take the opportunity to look farther down the cave system before leaving."
                            jump empty_hole2_insidecave_menu
                        else:
                            scene bg black with dissolve
                            pause (0.01)
                            scene bg emptycave
                            show Sabia at left
                            show Kia at right
                            with dissolve
                            "Sabia left the cave, and saw Kia waiting on a small boulder."
                            $ Kia.face = "normal2"
                            kia "What find?"
                            $ Sabia.face = "normalopen"
                            s "Down the cave, I found some thick strands of tentacle slime that were almost solid."
                            $ Sabia.face = "normal"
                            $ Kia.face = "pawtiltconfused"
                            kia "What mean?"
                            $ Sabia.face = "normalopen"
                            s "Uh... it had like spider webs. But a chufk version of spider webs."
                            $ Sabia.face = "normal"
                            $ Kia.face = "normal2"
                            kia "No. {i}Chufk{/i}!"
                            $ Sabia.face = "happy3"
                            s "Yes, but... oh nevermind."
                            $ Sabia.face = "normalopen"
                            $ Kia.face = "angry2"
                            s "I also found a lot of rabbit bones. I think it prefers to eat rabbits."
                            s "We might be able to lure it out with some rabbit meat-"
                            $ Kia.face = "angry5"
                            $ Sabia.face = "surprised1"
                            kia "NO."
                            $ Kia.face = "angry4"
                            $ Sabia.face = "normalopen"
                            s "What's-"
                            $ Sabia.face = "sad1"
                            $ Kia.face = "angry5"
                            kia "NO {i}NIFSKS{/i}."
                            $ Sabia.face = "normalopen"
                            $ Kia.face = "angry4"
                            s "Why not?"
                            $ Sabia.face = "irritated2"
                            $ Kia.face = "angry2"
                            kia "No. Not {i}nifsks{/i}. Not eat."
                            if chaos_kia_help == True:
                                $ Sabia.face = "normalopen"
                                s "I've seen you catch and eat rabbits before, Kia."
                                $ Sabia.face = "irritated2"
                                $ Kia.face = "irritated2"
                                kia "Different. Not same."
                                $ Sabia.face = "normalopen"
                                s "How is it any different?"
                            else:
                                $ Sabia.face = "normalopen"
                                s "What do you mean? You eat rabbits, don't you?"
                            $ Sabia.face = "irritated2"
                            $ Kia.face = "normal2"
                            kia "Only old {i}nifsks{/i}. Kill right. Not kill bad. {i}Chufk{/i} kill bad."
                            kia "{i}Chufk{/i} eat {i}nifsks{/i} bad."
                            $ Sabia.face = "normalopen"
                            s "I... think I understand."
                            s "The only rabbits you will kill and eat, are ones that are already old?"
                            $ Sabia.face = "normal"
                            $ Kia.face = "normal1"
                            kia "Yes. Only old."
                            s "And... you kill them correctly? Which the tentacle monster does not?"
                            $ Sabia.face = "normal"
                            $ Kia.face = "normal2"
                            kia "{i}Chufk{/i} kill bad. Kia kill good. No {i}nifsks{/i}. No."
                            $ Sabia.face = "normalopen"
                            s "Well, what if we kill them correctly, and then use them as bait?"
                            $ Sabia.face = "normal"
                            $ Kia.face = "pawuncertain1"
                            "Kia took a moment to think about that. Sabia could see that Kia was clearly thinking it through, very thoroughly."
                            $ Kia.face = "normal2"
                            kia "No {i}nifsks{/i}."
                            $ Sabia.face = "closed2"
                            "Sabia let out a short sigh."
                            $ Sabia.face = "normalopen"
                            s "Okay, Kia. Regular meat worked last time, so it should work again, I suppose."
                            $ Sabia.face = "normal"
                            $ Kia.face = "happy2"
                            kia "Good. No {i}nifsks{/i}."
                            $ Sabia.face = "normalopen"
                            s "I understand, Kia."
                            scene bg black with dissolve
                            pause (0.01)
                            scene bg countryside
                            show Sabia at left
                            show Kia at right
                            with dissolve
                            "Kia continued frowning for a few moments, before leading Sabia back to the edge of the forest closest to Grok og Dar."
                            hide Kia with moveoutright
                            "Sabia watched Kia dart off into the forest."
                            $ Sabia.face = "normalopen"
                            s "Well, I can prepare another batch of meat like I had last time and try that. But given that it does seem to sense intent, at least to some degree..."
                            s "It might not come out for it in that case. Rabbit might prove more successful given how much it seems to like it from the bones."
                            $ Sabia.face = "closed4"
                            s "But Kia is most certainly not going to be happy about that."
                            $ Sabia.face = "normalopen"
                            s "If I go with rabbit, I'll have to first convince Kia."
                            s "Else, I'm sure I can get some meat from the trading lodge fairly easily."
                            scene bg black with dissolve
                            pause (0.01)
                            jump eastern_frontier_map

    "Track the Tentacle Monster with Kia (200 stamina)" if kia_tentacle_quest == 9 and kia_tentacle_capturetalk == False:
        $ Sabia.stamina -= 200
        $ kia_tentacle_capturetalk = True
        $ Kia.face = "normal1"
        $ Sabia.face = "normal"
        show Sabia at left
        show Kia at right
        with dissolve
        $ Sabia.face = "normalopen"
        s "Kia... we need to talk."
        $ Kia.face = "happy2"
        $ Sabia.face = "sad1"
        kia "Sit!"
        "Kia pushed Sabia down to the ground, and plonked down herself next to Sabia."
        $ Kia.face = "happy2E"
        kia "What talk?"
        $ Kia.face = "irritated2"
        $ Sabia.face = "sad3"
        s "I... the tentacle monster. I don't want to kill it."
        $ Sabia.face = "sad2"
        "Kia growled, baring her teeth, and adjusting her weight as if she were ready to pounce."
        $ Kia.face = "irritated3"
        kia "Why?"
        $ Kia.face = "angry2"
        $ Sabia.face = "sad3"
        s "Because, I think it it understands us. Sort of. Not as much as you... but it senses intent."
        s "Killing it would be a mistake, I think."
        $ Sabia.face = "sad1"
        kia "..."
        $ Sabia.face = "sad3"
        s "I think we might even be able to communicate with it, or teach it."
        s "Wouldn't it be better to be able to teach it how to hunt and eat properly?"
        s "It might even be able to help to make sure people don't overhunt the area, or hurt any animals that shouldn't be."
        $ Sabia.face = "sad1"
        kia "..."
        "Kia gave no reply to Sabia's words, as she thought about it, her face impassive."
        $ Kia.face = "irritated3"
        $ Sabia.face = "sad3"
        s "I understand where you are coming from, Kia... but I don't think I can help if we're going to kill it."
        $ Kia.face = "angry2"
        $ Sabia.face = "sad1"
        kia "..."
        "Kia stayed silent for a while longer, before reluctantly retracting her claws and sitting back down."
        $ Kia.face = "irritated3"
        kia "Not kill... what do?"
        $ Kia.face = "angry2"
        $ Sabia.face = "sad3"
        s "I think if we keep it somewhere it can't escape, and maybe spend some time with it... it might start to learn."
        $ Kia.face = "irritated3"
        kia "Where?"
        $ Kia.face = "irritated2"
        $ Sabia.face = "closed2"
        s "Every nest it has been in has been soft soil where it can burrow, or it lead into tunnels.... your cave doesn't have anything except solid rock."
        $ Kia.face = "irritated2x"
        $ Sabia.face = "sad1"
        kia "..."
        $ Kia.face = "irritated2"
        kia "..."
        $ Kia.face = "irritated1"
        $ Sabia.face = "normal"
        kia "...Sabia plan..."
        kia "Not worst."
        $ Kia.face = "irritated2"
        $ Sabia.face = "sad1"
        "Kia frowned, opening her mouth to speak. She closed it."
        "This happened a few more times before she found the words she was looking for."
        $ Kia.face = "normal2"
        $ Sabia.face = "normal"
        kia "Not like kill all. Teach good... maybe."
        kia "Try."
        $ Sabia.face = "happy3"
        s "Thank you, Kia."
        $ Sabia.face = "normal"
        $ Kia.face = "irritated2"
        "Sabia gave a sigh of relief. Though she wasn't sure Kia was entirely on board with the plan... at least she seemed willing to entertain the idea."
        "She suspected that if the tentacle monster could be taught how to hunt more ethically, Kia would not have a problem with it."
        $ Kia.face = "irritated3"
        kia "Not Kia cave."
        $ Kia.face = "irritated2"
        $ Sabia.face = "normalopen"
        s "But-"
        $ Sabia.face = "normal"
        kia "Kia know cave. Take Sabia."
        "Sabia followed Kia through the forest, to another cave. It had the same harsh, rocky inside that she hoped would prevent the tentacle monster's escape."
        "Kia left quickly, leaving Sabia to fashion as best she could a makeshift prison. She hoped that it would not try leaving via the surface. All other incidents with it had been subterranean, after all."
        "Several hours later, and she was satisfied with it. Making sure to mark the spot on her map, she left."
        scene bg black with dissolve
        pause (0.01)
        jump eastern_frontier_map

    "Track the Tentacle Monster with Kia (200 stamina)" if kia_tentacle_quest == 9 and kia_tentacle_capturetalk == True:
        if Sabia.stamina < 200:
            "Sabia is too tired to do this right now."
            jump ef3_forest2
        if kia_tentacle_quest_venison == False:
            "I still need to get the venison from the trading lodge."
            jump ef3_forest2
        $ Sabia.stamina -= 200
        $ kia_tentacle_quest = 10
        $ Kia.face = "normal1"
        $ Sabia.face = "normal"
        show Sabia at left
        show Kia at right
        with dissolve
        kia "Find nest. {i}Chufk{/i}. Come, Sabia, come! Quick!."
        $ Sabia.face = "normalopen"
        s "Okay, let's go. Lead the way Kia - but remember I'm not quite as fast as you."
        scene bg black with dissolve
        pause (0.01)
        scene bg emptycave
        show Sabia at left
        show Kia at right
        with dissolve
        "Kia kept a bit closer to Sabia on this trip, though she could tell that Kia was struggling to hold back her speed."
        "Sabia was glad that she had Kia to guide her, because she was fairly certain she would have got lost by now."
        "They came upon another hollow, smaller than the first one. But still larger than the one she had found with Neve."
        "If Sabia wanted to, she could probably get down and out easy enough."
        $ Sabia.face = "normalopen"
        s "Are you sure it's down there, Kia?"
        $ Sabia.face = "normal"
        $ Kia.face = "happy3"
        kia "Yes. Sure, very. Down there. {i}Chufk{/i}."
        $ Kia.face = "happy1"
        "Looking down, Sabia could see traces of recent activity - some slime that looked wet, and a few bones that still had a bit of meat clinging to them."
        $ Sabia.face = "normalopen"
        s "Well, I've got the potion from Elmy."
        $ Sabia.face = "irritated2"
        "Sabia hefted the sack of meat in one hand."
        $ Kia.face = "normal1"
        "She threw it into the small chasm, and it landed with a loud wet thud."
        $ Sabia.face = "normal"
        "Kia growled, crawling up to the rim of the hollow, and peered down. She bared her fangs."
        $ Sabia.face = "normalopen"
        $ Kia.face = "normal2"
        s "Kia, can you please move back? I don't think it will come out if you are so threatening like that."
        $ Sabia.face = "normal"
        kia "..."
        "Despite Kia's clear desire to stay, she moved a few feet back."
        "And waited."
        "Sabia waited."
        "They both waited, and the sun moved across its arc in the sky. It seemed the only thing interested in the sack of meat was a trail of ants."
        $ Sabia.face = "sad3"
        $ Kia.face = "pawsad2"
        s "I think we'll need something different for bait, Kia."
        s "It doesn't seem interested in that again, but-"
        $ Sabia.face = "normal"
        $ Kia.face = "normal1"
        "Kia leaned a bit farther forward, her claws curling about the edge of earth that served as the demarcation between above and below."
        $ Sabia.face = "pout1"
        $ Kia.face = "happy3"
        kia "Naked!"
        $ Sabia.face = "normalopen"
        s "What?"
        $ Sabia.face = "normal"
        show Kia at center with move
        "Kia had blurted it out, and upon Sabia's question, had pounced over toward Sabia."
        $ Sabia.face = "surprised1"
        kia "Naked. {i}Chufk{/i} mate."
        show Kia:
            linear (0.1) xoffset (-50)
            linear (0.1) xoffset (0)
            repeat 2
        $ Kia.face = "happy1"
        "Kia poked Sabia in the stomach as she spoke."
        $ Kia.face = "happy2"
        kia "{i}Naked{/i}!"
        $ Sabia.face = "closed2"
        $ Kia.face = "happy1"
        "This time, Kia was more insistent. She jabbed a finger into Sabia's stomach, and then stabbed the same finger down toward the pit."
        $ Sabia.face = "irritated2"
        $ Kia.face = "happy3"
        kia "Kia saw. Neve, Sabia, {i}chufk{/i}."
        $ Kia.face = "happy1"
        "She cocked her head to the side."
        $ Sabia.face = "normalopen"
        $ Kia.face = "happy2"
        s "Are you... saying that it will come out, if I go down there naked and ready to... {i}mate{/i} with it?"
        $ Sabia.face = "irritated2"
        show Kia at right with move
        "Kia grinned, and darted back over to the edge of the hollow, pointing down insistently."
        $ Kia.face = "irritated3"
        "Kia's lips pulled back, teeth glinting in the light."
        "{i}Chufk{/i} come."
        $ Kia.face = "irritated2"
        $ Sabia.face = "normalopen"
        s "Yes, but I'm not willing to do that again."
        s "Sorry, Kia. But I'll find another way. I'm sure there's other meat we can use as bait - not rabbits."
        $ Kia.face = "irritated1"
        $ Sabia.face = "irritated2"
        kia "..."
        $ Sabia.face = "normalopen"
        s "Though rabbits would be best, I think, because-"
        $ Sabia.face = "closed2"
        $ Kia.face = "irritated3"
        "Kia's throat rumbled with a predatory growl."
        $ Sabia.face = "normalopen"
        s "Okay, okay. No rabbits."
        $ Sabia.face = "normal"
        scene bg black with dissolve
        "Kia and Sabia went back to the edge of the forest."
        scene bg countryside
        show Sabia at left
        show Kia at right
        with dissolve
        pause (0.01)
        hide Kia with moveoutright
        "Sabia could tell Kia was frustrated and angry. The makhor left without saying goodbye."
        $ Sabia.face = "normalopen"
        s "Well... it seems that bait was a no-go. I can look for a different type of meat from the trading lodge that it might like or try and convince Kia to use rabbits and see if that works..."
        $ Sabia.face = "closed2"
        s "Or head down with no clothes on and see if the tentacle monster wants to come and 'play'..."
        scene bg black with dissolve
        pause (0.01)
        jump eastern_frontier_map

    "Convince Kia to use Rabbits as bait and try again (200 stamina)" if kia_tentacle_quest == 10:
        if Sabia.stamina < 200:
            "Sabia is too tired to do this right now."
            jump ef3_forest2
        $ Sabia.stamina -= 200
        $ kia_tentacle_quest = 11
        $ kia_tentacle_quest_done = True
        $ Kia.face = "normal1"
        $ Sabia.face = "normal"
        show Sabia at left
        show Kia at right
        with dissolve
        jump chufkhunt_rabbitbait

    "Try to hunt the tentacle again with fresh venison (200 stamina)" if kia_tentacle_quest == 10:
        if Sabia.stamina < 200:
            "Sabia is too tired to do this right now."
            jump ef3_forest2
        if kia_tentacle_quest_freshvenison == False:
            "I still need to get the fresh venison from the trading lodge."
            jump ef3_forest2
        $ Sabia.stamina -= 200
        $ kia_tentacle_quest = 11
        $ kia_tentacle_quest_done = True
        $ Kia.face = "normal1"
        $ Sabia.face = "normalopen"
        show Sabia at left
        show Kia at right
        with dissolve
        s "I have a different type of meat that I think might be more preferable for the tentacle monster."
        $ Sabia.face = "normal"
        $ Kia.face = "tilt2b"
        kia "What?"
        $ Kia.face = "normal1"
        "Sabia hefted the sack she was carrying it in."
        $ Sabia.face = "normalopen"
        s "Deer - fresh venison meat."
        $ Sabia.face = "normal"
        $ Kia.face = "happy1"
        kia "Good."
        $ Sabia.face = "normalopen"
        s "I'm glad. I hope it's more successful than the last bait."
        $ Sabia.face = "normal"
        scene bg black with dissolve
        pause (0.01)
        scene bg emptycave
        show Sabia at left
        show Kia at right
        with dissolve
        "With a reasonably fresh haunch of venison, Sabia and Kia trekked back to the tentacle monster's current nest."
        $ Kia.face = "pawsad2"
        kia "Hope this work. Not like {i}chufk{/i} still here."
        kia "Wish could be {i}wakst{/i} Kia."
        $ Kia.face = "irritated3"
        kia "Rip {i}chufk{/i} from hide. Kill."
        $ Kia.face = "normal2"
        $ Sabia.face = "normalopen"
        s "Well, if you cannot switch back, we'll have to manage another way. I know you didn't want to use rabbits."
        $ Sabia.face = "irritated2"
        $ Kia.face = "irritated3"
        kia "No {i}nifsks{/i}."
        $ Kia.face = "normal1"
        $ Sabia.face = "normalopen"
        s "But I thought, if it likes rabbits so much, maybe it's because of how gamey they are, possibly how lean? Deer are also quite lean."
        s "So we can try this."
        $ Sabia.face = "normal"
        $ Kia.face = "tiltirritated"
        "Kia's continued frustration was evident as she snatched the deer haunch from Sabia, and hurled it into the open area of the tentacle monster's nest."
        "Kia growled, watching, waiting."
        $ Kia.face = "irritated2"
        $ Sabia.face = "irritated2"
        "The minutes ticked by, and they turned to an hour, two hours."
        "No tentacle monster emerged. There were signs of it having moved between this visit and the previous, so Sabia was confident that it had been here."
        "But it seemed either not interested in coming out for the deer meat, or it could sense their intentions."
        $ Sabia.face = "normal"
        "A dilemna - if they moved back so that it felt safer, they wouldn't be able to administer the potion properly."
        "But if they stayed, it seemed the tentacle monster did not want to come out at all."
        "As the minutes continued to tick on, the only interest in the deer were some ants that, Sabia assumed, were having a very good week."
        $ Sabia.face = "irritated2"
        $ Kia.face = "irritated3"
        kia "This NOT work Sabia."
        kia "{i}Chufk{/i} stay here, not come. Keep kill. Keep eat. Bad. Wrong."
        $ Kia.face = "irritated3x"
        kia "Sabia plan BAD. Not work."
        $ Sabia.face = "normalopen"
        s "I'm trying my best, Kia, but there is not very much information-"
        $ Sabia.face = "irritated2"
        $ Kia.face = "irritated3"
        kia "Do Kia plan. Better. Kia plan work."
        "Kia shoved her hand out and grabbed the vial of potion."
        $ Kia.face = "tilt2b"
        kia "This potion?"
        $ Sabia.face = "normalopen"
        s "Yes, it is."
        $ Sabia.face = "normal"
        $ Kia.face = "tilt2"
        kia "How use?"
        $ Sabia.face = "normalopen"
        $ Kia.face = "normal2"
        s "Well, when - if - the creature comes out, dousing the surrounding area with it should be enough to send it to sleep before it gets down into the nest and beyond its... tentacle webs."
        s "But, dousing it on the creature should work better too, I imagine, and-"
        show Kia at center with move
        $ temp = Sabia.armor
        $ Sabia.unequip(Sabia.armor)
        show Sabia at left with dissolve
        $ Sabia.face = "angry1"
        $ Kia.face = "happy3x"
        "Razor sharp claws glinted in the light as she sliced through the fabric, undressing Sabia."
        s "KIA!"
        $ Sabia.face = "irritated1"
        kia "Sabia go in. Fun! {i}Chufk{/i} come. Sabia like! Sabia fun!"
        $ Kia.face = "happy3"
        menu:
            "Absolutely not." if usedmakhorpoison == False:
                $ kia_tentacle_quest_outcome = "kia"
                $ Sabia.face = "angry1"
                s "I am not going to let the tentacle monster fuck me again, just so-"
                $ Sabia.face = "surprised2"
                "Sabia didn't get a chance to finish her sentence."
                "Kia pounced on her and splattered some of the potion on to her."
                "Immediately, she felt the effects of it, her eyes getting heavier and her mind drifting."
                $ Sabia.face = "angry1"
                s "K... Kia... you, this isn't, what..."
                "Kia growled, her large paws grabbing hold of Sabia's shoulders, pinning her against a nearby rock."
                kia "Sabia in! {i}Chufk{/i} out!"
                s "Kia?! What are you doing?!"
                scene bg black with dissolve
                "Sabia's answer came in the form of being pushed down the outcroppings, into the small area."
                "Her feet carried her down the steep path, rocks and stones rolling after her. She tried to stop herself, but the momentum was too much."
                "Sabia found herself tumbling into the mouth of the cave."
                "She rolled over a few times, before scrabbling to her feet. She had not expected Kia to do that. At all."
                s "Ugh!"
                "Something slick touched her arms, and her legs. She hadn't been prepared for it. She flailed out, trying to bat it away."
                "Instead of batting it away, she only served to make it cling to her more."
                s "KIA. This is NOT going to work."
                s "Get me out of here. NOW."
                kia "Work! Kia plan good."
                call chufkhunt_kia
                $ Sabia.equip(temp)
                play music forest fadeout 2.0 fadein 2.0
                scene bg black with dissolve
                jump ef3_forest2
            "Fine.":
                $ kia_tentacle_quest_outcome = "nokia"
                scene bg black with dissolve
                "The tentacle monster didn't come out as Sabia descended, but she could hear the faint high pitched thrum in the back of the cave."
                "Somehow Sabia knew it sensed her, and was interested."
                "But it must have been unsure, with Kia so close."
                "Sabia walked forward, entering the cave. As she passed the threshold, darkness enveloped quickly and her eyes were not able to adjust quickly enough."
                "She walked into something half sticky, and jumped in surprise. Her arms and legs flailed about, and something latched on, holding her tight."
                "Sabia yelped loudly, her movements only seeming to make it worse."
                "For a moment Sabia's panic doubled, before she realized how stupid she had been."
                s "...walked right into the tentacle's web. Great."
                call chufkhunt_nokia
                $ Sabia.equip(temp)
                play music forest fadeout 2.0 fadein 2.0
                scene bg black with dissolve
                jump ef3_forest2
            "Go back and try to use rabbits as bait.":
                "Sabia decided that for now they should crawl back up from the cave."
                scene bg black with dissolve
                $ Sabia.equip(temp)
                "She picked her clothes back up and got dressed in the way."
                scene bg cave
                $ Sabia.face = "normalopen"
                $ Kia.face = "irritated3"
                show Sabia at left
                show Kia at right
                with dissolve
                jump chufkhunt_rabbitbait

    "Tentacle Monster" if kia_tentacle_quest_done == True and tentacle_visit == 0:
        $ tentacle_visit = 1
        $ Sabia.face = "irritated2"
        scene bg cave with dissolve
        show Sabia at left with dissolve
        "Sabia approached the makeshift prison, and looked in."
        "She could sense that the creature felt despondent, but at least it had not attempted to escape."
        $ Sabia.face = "question1"
        "There was still a long way to go with it - but some of the more... depraved houses in Lundarian aristocracy made use of tentacle monsters for 'fun'."
        "They were well suited to it."
        $ Sabia.face = "eyebrow1"
        "And with Sabia running the relief tents... maybe she could employ some of those uses she had heard about."
        jump ef3_forest2_kia

    "Tentacle Monster" if tentacle_visit == 2:
        $ tentacle_visit = 3
        scene bg cave with dissolve
        $ Sabia.face = "normal"
        show Sabia at left with dissolve
        "Sabia could hear the low, disconcerting sound of the tentacle monster as she approached the cave."
        "She could also hear Kia's huffs."
        show Kia at right with dissolve
        $ Kia.face = "irritated2"
        $ Sabia.face = "happy3"
        s "How's the teaching going?"
        kia "..."
        $ Sabia.face = "sad1"
        "Sabia took Kia's snarl to mean that it was not going particularly well."
        $ Kia.face = "irritated1"
        $ Sabia.face = "sad3"
        s "Have you managed to get it to eat other things, at least?"
        $ Sabia.face = "sad1"
        $ Kia.face = "irritated3"
        "Kia gave a gruff nod, but her lips pulled back enough for her teeth to show."
        $ Kia.face = "irritated1"
        "She crouched down, and pulled her hand over a small pile of bones."
        $ Sabia.face = "normal"
        kia "Not {i}nifsk{/i}."
        $ Sabia.face = "happy3"
        s "That's good, then!"
        $ Sabia.face = "sad1"
        $ Kia.face = "uncertain2"
        kia "Not like {i}chufk{/i} here..."
        $ Sabia.face = "normalopen"
        $ Kia.face = "tilt2b"
        s "But it seems like you're doing well, Kia. It would be good to have something else in your forest that can properly take care of it, wouldn't it?"
        $ Sabia.face = "normal"
        $ Kia.face = "uncertain2"
        kia "..."
        "Not wanting to push Kia any further, Sabia decided to leave the Makhor alone for now."
        jump ef3_forest2

    "Tentacle Monster" if tentacle_visit == 4:
        $ tentacle_visit = 5
        $ Sabia.face = "normal"
        $ Tentacle.face = "normal"
        scene bg cave with dissolve
        show Sabia at left
        show Tentacle at right
        with dissolve
        "Entering Kia's cave, Sabia didn't spot Kia anywhere."
        "The back of the cave was now open - the makeshift palisade she had erected had been discarded."
        $ Sabia.face = "irritated2"
        $ Tentacle.face = "sad"
        show Tentacle:
            xpos 1.1
        with move
        "The tentacle monster was no longer confined, but sensing that Sabia had entered, it retreated a little."
        "Pushing itself up into a corner, it's tendrils wrapped around itself."
        "It seemed that when it wasn't in a position to quickly flee, it was far less willing to interact."
        $ Sabia.face = "normalopen"
        s "Hello...?"
        $ Sabia.face = "normal"
        $ Tentacle.face = "angry"
        "The mass of glistening tentacles pulsed, and it started to rumble. The sound alternated from a deep low to a sharp high."
        "If Kia had decided that it was fine to not have it barred, then Sabia felt she would respect her friend's choice."
        "But for now, Sabia felt it would be best if she left the creature alone."
        jump ef3_forest2

    "Ask about fence." if tentacle_visit == 5 and kia_fence_talk == False:
        $ kia_fence_talk = True
        scene bg cave with dissolve
        $ Sabia.face = "normalopen"
        $ Kia.face = "irritated1"
        show Sabia at left
        show Kia at right
        with dissolve
        s "How come you took the fence down, Kia?"
        s "Have you been able to communicate with it, get it to understand anything?"
        $ Sabia.face = "normal"
        "Kia shook her head."
        $ Kia.face = "normal1"
        kia "Not need."
        "She placed both of her paws on the rocky cave wall."
        $ Sabia.face = "question1"
        kia "Not."
        "She moved closer to the cave entrance where some of the floor became a soft soil, and placed her hands there."
        $ Sabia.face = "normal"
        kia "Need."
        "Sabia nodded."
        $ Kia.face = "happy1"
        $ Sabia.face = "normalopen"
        s "It can't get through the solid rock... it needs the soft ground, I understand."
        $ Kia.face = "normal1"
        s "But, still-"
        $ Sabia.face = "normal"
        $ Kia.face = "irritated2"
        kia "Not. Need."
        $ Sabia.face = "normalopen"
        s "I... see."
        $ Sabia.face = "normal"
        "Decididing that she was not going to get any different answer, Sabia let it go with that."
        jump ef3_forest2_kia

    "Ask how tentacle monster is going." if tentacle_visit == 5 and kia_tentacle_talk == False:
        $ kia_tentacle_talk = True
        scene bg cave with dissolve
        $ Sabia.face = "normalopen"
        $ Kia.face = "irritated1"
        show Sabia at left
        show Kia at right
        with dissolve
        s "Kia, how is it going with the tentacle monster?"
        $ Sabia.face = "normal"
        "Kia frowned."
        "Her lip pulled back a little, twitching. To Sabia it looked like she was going to bare her fangs or hiss."
        $ Sabia.face = "irritated2"
        "But she stopped, and promptly sat herself down on the floor."
        $ Kia.face = "normal1"
        kia "..."
        kia "{i}Chufk.{/i}"
        s "..."
        $ Sabia.face = "closed2"
        s "(I don't think I'm going to get anything else out of her about it for now...)"
        jump ef3_forest2_kia

    "Talk to Tentacle monster." if tentacle_visit == 5 and tentacle_monster_talk == 0:
        scene bg cave with dissolve
        $ tentacle_monster_talk = 1
        show Sabia at left
        "Not sure how successful it would be, Sabia decided to try talking to the creature."
        show Tentacle at right with dissolve
        $ Tentacle.face = "normal"
        $ Sabia.face = "normalopen"
        s "So..."
        s "I get that it's not really the best place for you... but Kia said you were at least eating different things?"
        $ Tentacle.face = "sad"
        s "The whole rabbit thing was the issue, you know."
        $ Sabia.face = "normal"
        "The tentacle monster's tendrils writhed about, and it made a low, sad warble."
        $ Sabia.face = "sad1"
        "Sabia swore that it understood her... at least somewhat."
        "Any other questions she asked though, it gave the same sad sound."
        $ Sabia.face = "sad3"
        s "I guess I'm not going to be too successful... maybe another time."
        jump ef3_forest2_kia

    "Talk to Tentacle monster." if tentacle_visit == 5 and tentacle_monster_talk == 1:
        $ Sabia.face = "sad1"
        $ Tentacle.face = "sad"
        scene bg cave with dissolve
        show Sabia at left
        show Tentacle at right
        with dissolve
        "Sabia tried conversing with the creature again. It went about as well as the previous attempt."
        $ Sabia.face = "sad3"
        s "Maybe another time."
        jump ef3_forest2_kia
    "Go back":

        jump ef3_forest2


label chufkhunt_rabbitbait:
    $ Sabia.face = "normalopen"
    s "Kia, I know you're against the rabbits as bait."
    $ Sabia.face = "normal"
    $ Kia.face = "irritated3"
    kia "No {i}nifsks{/i}. Sabia not understand."
    $ Sabia.face = "normalopen"
    $ Kia.face = "irritated2"
    s "Well..."
    $ Sabia.face = "normal"
    $ Kia.face = "irritated3"
    kia "Kia only hunt properly. Protect rest. Keep safe."
    kia "Only hunt for eat. Only eat old."
    $ Sabia.face = "normalopen"
    $ Kia.face = "irritated2"
    s "I think I understand, Kia."
    s "But at the same time, if the creature likes eating rabbits, and we don't capture or stop it soon, how many rabbits and other creatures will it continue to eat?"
    s "You said it doesn't hunt correctly."
    $ Sabia.face = "normal"
    $ Kia.face = "pawuncertain1"
    kia "Hmmrmm..."
    "Kia frowned as she thought about what Sabia said."
    $ Sabia.face = "normalopen"
    s "If we can capture it, or prevent it from eating however and whatever it wants, wouldn't that be worth the sacrifice of one or two animals, instead of many more?"
    $ Kia.face = "pawtiltconfused"
    "Kia huffed, blowing some air out of her lips as she sat down, clearly thinking."
    $ Sabia.face = "normalopen"
    $ Kia.face = "normal2"
    s "So you agree, then?"
    $ Sabia.face = "normal"
    kia "Okay... find nifsk. Right nifsk."
    hide Kia with moveoutright
    "Kia darted off, leaving Sabia at the cave."
    $ Sabia.face = "normalopen"
    s "Well, I suppose I should just wait for Kia here...?"
    $ Sabia.face = "normal"
    "Sabia shrugged, deciding to simply wait."
    scene bg black with dissolve
    pause (0.01)
    scene bg cave
    show Sabia at left
    show Kia at right
    with dissolve
    "It didn't take too long before Kia came back with two rabbits in her paws."
    "The makhor had an uneasy look on her face as if she still were not entirely sure about the plan, even if understanding Sabia's point."
    "Though she had managed to convince Kia to use rabbits as bait, as they headed back toward the cave."
    "Whether it worked out or not, well - that was another question entirely."
    "She hoped it would, but really she was going off very little information, but it was better than giving up."
    scene bg black with dissolve
    pause (0.01)
    scene bg emptycave
    show Sabia at left
    show Kia at right
    with dissolve
    "Kia was deep in thought as they continued through the forest back to the tentacle monster's nest."
    "After reaching it, Kia stood at the rim of rocks circling the sunken nest. She frowned."
    "Climbing down easily, she placed the rabbits on the ground far gentler than Sabia would have thrown them in, before climbing back up and out."
    "The two of them waited for a few minutes, and Sabia was hoping that she hadn't been wrong about this."
    $ Sabia.face = "normalopen"
    s "Wait... look..."
    $ Sabia.face = "normal"
    "Sabia whispered her words to Kia. The creature's limbs writhed as it seemed to peek out of the nest, reaching for the dead rabbits."
    $ Kia.face = "irritated3"
    "Her fingers pressed against Kia's mouth instinctively, silencing her friend before Kia could growl, or hiss."
    $ Kia.face = "irritated2"
    $ Sabia.face = "irritated2"
    "Sabia shook her head."
    $ Sabia.face = "normalopen"
    s "Quiet. Don't spook it."
    $ Sabia.face = "irritated2"
    "Carefully, she unstoppered the vial. Anywhere would do, but hitting the creature would be ideal she knew."
    $ Kia.face = "pawuncertain1"
    "Taking a breath in, she upended the vial, and let its contents spill out, falling down into the small pit. She saw some of it hit the creature as its tentacles continued to reach for the rabbits almost nervously."
    "Sabia took a step back, beckoning Kia to do the same."
    $ Sabia.face = "normalopen"
    $ Kia.face = "normal1"
    s "Don't want us falling asleep from the potion. It should be fine in a few minutes."
    $ Sabia.face = "normal"
    $ Kia.face = "normal2"
    kia "{i}Chufk{/i} better not gone..."
    $ Sabia.face = "normalopen"
    s "It shouldn't. Ylva said its effects were rapid."
    $ Sabia.face = "normal"
    "They waited another few moments."
    scene bg black with dissolve
    pause (0.01)
    scene bg emptycave
    show Sabia at left
    show Kia at right
    with dissolve
    $ Sabia.face = "normalopen"
    s "Alright, I think that should be long enough... I guess."
    $ Sabia.face = "normal"
    $ Kia.face = "happy1"
    "Kia pounced onto the rim from her seated position."
    "She turned back around to Sabia, a wide grin on her face."
    $ Kia.face = "happy2"
    kia "Work! It work, Sabia! Sabia plan work!"
    $ Kia.face = "happy3x"
    kia "{i}Chufk{/i} sleep! Kia kill now."
    $ Sabia.face = "angry1"
    s "No, Kia!"
    $ Kia.face = "irritated2"
    kia "What?"
    $ Sabia.face = "normalopen"
    s "Remember... no killing it."
    $ Sabia.face = "sad3"
    s "It can sense intent... it might be more aware than we realise, Kia."
    $ Sabia.face = "sad1"
    $ Kia.face = "irritated3"
    "Kia flashed her teeth, and her claws extended from her paws."
    kia "..."
    $ Sabia.face = "sad3"
    s "It would be a waste, Kia... if it can be taught, or learn - how useful would that be?"
    $ Sabia.face = "sad2"
    $ Kia.face = "irritated3x"
    kia "..."
    $ Sabia.face = "sad1"
    $ Kia.face = "irritated2"
    "After another few minutes of arguing, Kia relented. They followed Sabia's plan - that had been agreed upon earlier, Sabia added to herself quietly."
    "It was difficult to take with all of its tentacles, but between the two of them they managed to return it to Kia's suggested cave, and imprison it in the makeshift jail they had fashioned."
    "There was no telling how many days it would take to wake again."
    scene bg black with dissolve
    pause (0.01)
    jump ef3_forest2


label ef3_groknaks_route:
    scene bg countryside with dissolve
    if chaos_maply_help == False and chaos_kia_help == False and groknaks_route_solo_checked == True:
        call sabiabase
        with dissolve
        show sabiaemo closed2 at left
        s "I'm not going to be able to pick the track up. It's clear Groknak went a round-a-bout way to the meeting."
        s "I'm going to need someone who can help me follow the track. And it's going to have to be fast."
        show sabiaemo irritated1 at left
        s "Risking the track disappearing isn't something I can do."
        jump eastern_frontier_map
    elif chaos_maply_help == False and chaos_kia_help == False and groknaks_route_solo_checked == False:
        $ groknaks_route_solo_checked = True
        call sabiabase
        with dissolve
        "It was easy to find the path that Groknak and his party had taken."
        "He had headed west. It was clear to Sabia that he had intended to avoid a direct path to Whitecrest over Whitewater Pass, and this seemed to be in line with what Jadk had mentioned."
        show sabiaemo normalopen at left
        s "Probably a good idea. Even if Andian wanted a meeting, it doesn't mean that no one else did. And clearly so."
        show sabiaemo closed2 at left
        s "Though, perhaps it might have been better had he gone that way? He might not have been ambushed."
        show sabiaemo normal at left
        "Pondering her thoughts, Sabia continued on as daylight waned."
        "Passing over a few streams, and bridges, she found herself stumped, looking across the other side of a larger body of water."
        "She wasn't an expert tracker and she realized that the track was dead for her."
        show sabiaemo irritated2 at left
        s "Fuck."
        show sabiaemo irritated1 at left
        s "Fuck."
        show sabiaemo angry1 at left
        s "I'm not going to be able to pick the track up. It's clear Groknak went a round-a-bout way to the meeting."
        s "I'm going to need someone who can help me follow the track. And it's going to have to be fast."
        show sabiaemo closed2 at left
        s "Risking the track disappearing isn't something I can do."
        jump eastern_frontier_map
    elif chaos_maply_help == False and chaos_kia_help == True and groknaks_route_solo_checked == False:
        call sabiabase
        show kia normal1 at right
        with dissolve
        "It was easy to find the path that Groknak and his party had taken."
        "He had headed west. It was clear to Sabia that he had intended to avoid a direct path to Whitecrest over Whitewater Pass."
        show sabiaemo normalopen at left
        s "Probably a good idea. Even if Andian wanted a meeting, it doesn't mean that no one else did. And clearly so."
        show sabiaemo closed2 at left
        s "Though, perhaps it might have been better had he gone that way? He might not have been ambushed."
        show sabiaemo normal at left
        show kia uncertain2 at right
        kia "What doing?"
        jump ef3_kia_ambush
    elif chaos_maply_help == False and chaos_kia_help == True and groknaks_route_solo_checked == True:
        call sabiabase
        show kia normal1 at right
        with dissolve
        "Sabia hadn't had many strokes of fortune, yet Kia seeing Groknak's party in passing was definitely one of them."
        "Already knowing where the trail fell off, Sabia led Kia there. Though it was a little bit faster than when Sabia tracked it initially, most of the day had already passed."
        jump ef3_kia_ambush
    elif chaos_maply_help == True and chaos_kia_help == False and groknaks_route_solo_checked == False:
        call sabiabase
        show maply 1 at right
        show maplyemo normal at right
        with dissolve
        "It was easy to find the path that Groknak and his party had taken."
        "He had headed west. It was clear to Sabia that he had intended to avoid a direct path to Whitecrest over Whitewater Pass."
        show sabiaemo normalopen at left
        s "Probably a good idea. Even if Andian wanted a meeting, it doesn't mean that no one else did. And clearly so."
        show sabiaemo closed2 at left
        s "Though, perhaps it might have been better had he gone that way? He might not have been ambushed."
        jump ef3_maply_ambush
    elif chaos_maply_help == True and chaos_kia_help == False and groknaks_route_solo_checked == True:
        call sabiabase
        show maply 1 at right
        show maplyemo normal at right
        with dissolve
        "Already knowing where the trail fell off, Sabia led Maply there. Though it was a little bit faster than Sabia tracking it initially, most of the day had already passed."
        jump ef3_maply_ambush


label ef3_kia_ambush:
    scene bg countryside
    show backdrop
    call sabiabase
    show kia normal1 at right
    with dissolve
    $ groknak_route_investigation = True
    s "Come on, Kia. We need to pick the trail up on the other side of the rivulet."
    show kia pawtiltconfused at right
    kia "Why?"
    show sabiaemo normalopen at left
    s "Because I need to find- I thought we were on the same page?"
    kia "Sabia, why going {i}that{/i} way?"
    "Kia pointed down the stream, almost due west, and most definitely not the direction Sabia was trying to get Kia to go."
    show kia happy2 at right
    kia "Sabia go that way!"
    show sabiaemo normalopen at left
    s "But... that's even further from Whitecrest. Are you sure, Kia?"
    kia "Sure!"
    show sabiaemo happy1 at left
    s "Alright then, let's go that way."
    show kia normal1 at right
    kia "No."
    show sabiaemo irritated2 at left
    show kia happy3 at right
    kia "Hungry. Hunt. Sabia rest! Track foo... orcs tomorrow!"
    hide kia with moveoutright
    show sabiaemo normalopen at left
    "Sabia's mouth was only half open by the time Kia bounded off."
    show sabiaemo normal at left
    "Though Sabia had a sense of urgency to it, she couldn't deny that the day was getting late, and whether she wanted to or not, she would have to rest."
    "Confident that Kia would find her when she was finished hunting, Sabia moved up a bit further to not be entirely in the open."
    "Sabia started a fire, waiting for Kia to return. It wasn't long before she heard the rustling that suggested Kia was returning."
    show sabiaemo normalopen at left
    s "Did you get anything to eat Kia?"
    show neve1 at right
    show neveemo smirk1 at right
    with moveinright
    n "Well, I don't know about eating Kia. Maybe if her and I get to know each other a little better."
    show sabiaemo happy3 at left
    s "Neve!"
    s "What are you doing here? I thought you had business?"
    show sabiaemo normal at left
    show neveemo normal at right
    n "I did. I resolved it. It's led me here and I thought I'd join you. Is Kia around, then?"
    show sabiaemo normalopen at left
    s "Uh, she is - she's hunting. What was your business that led you here?"
    show sabiaemo normal at left
    show neveemo closed4 at right
    n "Let's just say it was certainly interesting, and would take entirely far too long to explain."
    show neveemo normal at right
    n "But I think I'll help you investigate this ambush. Groknak deserves that much."
    show sabiaemo happy3 at left
    s "Well I won't say no to extra help."
    show sabiaemo normal at left
    show kia normal1 at center with moveinright
    kia "What danger doing here?"
    show sabiaemo happy3 at left
    s "Neve's offered to help."
    show kia uncertain2 at center
    kia "Why help?"
    show neveemo happy3 at right
    n "Because I liked Groknak."
    "Kia's throat rumbled as she thought about it."
    show kia happy2 at center
    kia "Groknak mate?"
    show neveemo smirk1 at right
    n "I wouldn't have said no to a tumble had he asked..."
    show neveemo normal at right
    n "But, no. Groknak wasn't my mate. Just a friend."
    show kia pawuncertain1 at center
    "Kia pondered it a little more, dumping several rabbits next to Sabia. They were lean, but there was enough of them that the three of them could have a good meal."
    show sabiaemo normalopen at left
    s "Kia, why do you call Neve danger?"
    show neveemo happy1 at right
    n "Because she's smart."
    show kia normal2 at center
    kia "Smell like danger."
    show sabiaemo normalopen at left
    s "But {i}how{/i} does she smell like danger?"
    show sabiaemo irritated2 at left
    show neveemo happy3 at right
    "Kia looked confused."
    show kia pawtiltconfused at center
    kia "{i}Chufk{/i} smell like {i}Chufk{/i}. Sabia smell like Sabia. Danger smell like danger."
    show neveemo smirk1 at right
    show kia normal1 at center
    n "Like I said, she's smart."
    show neveemo normal at right
    n "But Kia, I promise I'm not a danger to you. Nor to Sabia."
    show kia uncertain2 at center
    kia "..."
    show sabiaemo happy3 at left
    s "It's true. I trust Neve."
    show sabiaemo normal at left
    show kia pawtilteager2 at center
    "It seemed that that was enough for the Makhor. Kia grinned, and nodded."
    kia "Neve!"
    show kia happy4 at center
    "She jumped forward, and wrapped her large paws around Neve, squeezing the elf tightly."
    show neveemo smirk1 at right
    n "I bet you're fun, aren't you, Kia?"
    show kia happy3 at center
    kia "Kia very fun."
    show kia happy2E at center
    kia "Sabia tell Neve! Kia fun!"
    show sabiaemo lick2 at left
    show sabiaemo2 blush at left
    s "Haha... yeah."
    s "Kia can be quite... {i}fun{/i}."
    show sabiaemo eyebrow1 at left
    show neveemo smirk1 at right
    n "Oh? Maybe you'll have to show me sometime, Kia."
    show kia uncertain1 at center
    kia "..."
    kia "Maybe."
    show neveemo normal at right
    show kia normal1 at center
    show sabiaemo normalopen at left
    hide sabiaemo2
    s "Regardless of how fun everyone is, we'll need to rest. I don't want to waste any time and risk the trail going cold."
    show kia uncertain2 at center
    kia "...hunted... Sabia not eat?"
    show sabiaemo happy3 at left
    s "I'll eat some in the morning, Kia."
    "Kia frowned, but lightened up a little when Neve asked for some. Sabia drifted into sleep, and before long she woke to the morning."
    scene bg black with dissolve
    pause (0.1)
    scene bg countryside
    call sabiabase
    show kia normal1 at center
    show neve1 at right
    show neveemo normal at right
    with dissolve
    "Sabia stretched, yawned, and got up."
    "Glancing around their makeshift site, she noticed a pile of bones next to the fire, and an awake Kia and Neve chatting."
    show sabiaemo normalopen at left
    s "What happened to all the rabbit meat?"
    show kia irritated2 at center
    kia "Eat!"
    show neveemo happy3 at right
    n "Heh. I don't think Kia was too happy with you not eating any. She seemed a bit hurt about it."
    show sabiaemo sad2 at left
    s "Sorry Kia. I was just focused on... I promise I'll make it up to you."
    show sabiaemo sad1 at left
    show kia uncertain1 at center
    kia "Sabia eat next time?"
    show sabiaemo happy3 at left
    s "I will."
    show kia happy4 at center
    kia "Okay!"
    show sabiaemo normalopen at left
    s "Can we please start trying to track Groknak's path, now, Kia? I will eat later when we go back. This is very important to me."
    show sabiaemo normal at left
    show kia pawuncertain1 at center
    kia "Hmm. Important? Know important. Not know why important to Sabia. Help anyway!"
    show kia normal1 at center
    "It didn't take long for Sabia to realize just how thankful she was that Kia was helping."
    "There was almost no chance that she would have been able to follow the tracks. In fact, not a few moments passed where she wondered if they were still following Groknak's path."
    "Each time she was given a glower from Kia, and a resulting chuckle from Neve."
    show kia happy3 at center
    kia "Here!"
    show sabiaemo surprised1 at left
    show neveemo smirk1 at right
    "Kia stopped abruptly, and Sabia almost slammed into the Makhor's back."
    show kia uncertain2 at center
    show sabiaemo normal at left
    kia "Fight here. Still smell blood."
    show sabiaemo happy3 at left
    s "Thank you Kia. Really. If you'd like-"
    show kia pawuncertain1 at center
    kia "Smell bad. Smell weird. Don't like. See Sabia and Neve later!"
    hide kia with moveoutright
    show neveemo happy3 at right
    n "Haha, she does just bounce off once the task is done, doesn't she?"
    show sabiaemo normalopen at left
    s "It seems that way."
    scene bg black with dissolve
    pause (0.1)
    jump ef3_ambush_site


label ef3_maply_ambush:
    scene bg countryside
    show backdrop
    call sabiabase
    show maply 1 at right
    show maplyemo normal at right
    with dissolve
    $ groknak_route_investigation = True
    show sabiaemo normalopen at left
    s "Let's go Maply. We need to pick up the trail on the other side of the rivulet."
    show maplyemo sad2 at right
    maply "Uh, Saby. I'm sorry, but that's the wrong way."
    show sabiaemo normalopen at left
    s "What do you mean?"
    show sabiaemo normal at left
    show maplyemo normalopen at right
    maply "I can see from here the tracks aren't there. They disappear."
    maply "I think we need to go down the river a bit further, they may have traveled in the stream. Which direction, well I don't know about that."
    show sabiaemo normalopen at left
    show maplyemo normal at right
    s "Can Fluff Tooth pick up the scent?"
    show sabiaemo normal at left
    "The hound barked, hearing its name."
    show maplyemo normalopen at right
    maply "Probably not Saby. The scent will have washed away in the water. I think we should go... in the same direction Groknak was heading."
    show sabiaemo normalopen at left
    s "Well, if he was trying to lose people, wouldn't they head back the other way? Why keep going the same way? It wouldn't work well as a decoy or distraction."
    show maplyemo sad2 at right
    show sabiaemo normal at left
    maply "But what if Groknak thought people would think that, and then go back thinking he tried to trick them?"
    show sabiaemo pout3 at left
    s "I... Maply, you're making my head hurt."
    show maplyemo normalopen at right
    show sabiaemo normal at left
    maply "I think we should go that way, it's a hunch!"
    maply "You should always follow catgirl hunches."
    show maplyemo normal at right
    show sabiaemo normalopen at left
    s "Why?"
    show maplyemo happy at right
    show sabiaemo normal at left
    maply "Because I said so Saby! Plus, Fluff Tooth thinks it's the right way, don't you?"
    "Maply crouched down and ruffled his head with both hands. He barked, licked her face and darted backwards, snapping his jaws in the direction Maply had suggested."
    show sabiaemo happy3 at left
    s "Alright then. We'll go that way."
    show sabiaemo normal at left
    show maplyemo normalopen at right
    maply "We should make camp though! We don't want to go too far and miss something in the night, or get too wet and catch a chill."
    show maplyemo normal at right
    show sabiaemo normalopen at left
    s "You're probably right, even though the wait... yeah, we'll do that Maply."
    show sabiaemo irritated2 at left
    "Though Sabia had a sense of urgency, she couldn't deny Maply's valid points."
    show maplyemo happy at right
    show sabiaemo normal at left
    maply "Me and Fluff Tooth will go get something to eat for dinner, Saby."
    maply "Back soon!"
    hide maply 1
    hide maplyemo
    with moveoutright
    "Sabia nodded, watching Maply and the hound disappear into the trees."
    "Confident that the agile catgirl and bestial hound would find her when she was finishing hunting, Sabia moved up a bit further to not be entirely in the open."
    "Sabia started a fire, waiting for Maply and Fluff Tooth to return. It wasn't long before she heard the rustling that suggested the two were returning."
    show sabiaemo normalopen at left
    s "What did you find for us Maply?"
    show neve1 at right
    show neveemo normal at right
    with moveinright
    show sabiaemo surprised1 at left
    show neveemo smirk1 at right
    n "Well, it looks like I found a hungry Sabia."
    n "Maybe I can help you out with something to eat?"
    "Neve smirked, winking. The meaning in her words was painfully obvious."
    show sabiaemo normalopen at left
    s "Neve!"
    s "What are you doing here? I thought you had business?"
    show sabiaemo normal at left
    show neveemo closed4 at right
    n "I did. I resolved it. It's led me here and I thought I'd join you. Though I noticed you never answered my question... a shame."
    show neveemo happy1 at right
    n "Are Maply and Fluff Tooth around, then?"
    show sabiaemo normalopen at left
    s "They're out hunting for some dinner. I hope they don't get too distracted... uhm, playing."
    show sabiaemo closed2 at left
    show neveemo smirk1 at right
    n "Mmm. {i}Playing{/i}."
    show sabiaemo normalopen at left
    s "What was your business that led you here?"
    show sabiaemo normal at left
    show neveemo normal at right
    n "Let's just say that it was certainly interesting, and would take entirely far too long to explain."
    n "But I think I'll help you investigate this ambush. Groknak deserves that much."
    show sabiaemo happy3 at left
    s "I won't say no to extra help, especially from a keen eye like yours."
    show sabiaemo normal at left
    "Sounds of giggling and snapping jaws from beyond the line of trees let both of them know that Maply and Fluff Tooth had returned."
    show maply 1 at center
    show maplyemo happy at center
    with moveinright
    maply "Oh, Neve! Hello."
    show neveemo smirk1 at right
    n "Hello to you too, Maply. Did you find anything in your hunt for us to eat... or did you have a bit too much playtime?"
    show maplyemo angry2 at center
    maply "I'll have you know we found plenty! Look, there's at least eight rabbits here!"
    show maplyemo angry2 at center
    show sabiaemo eyebrow1 at left
    "Maply brandished both handfuls of rabbits in front of her."
    show neveemo happy2 at right
    n "Hope you two don't mind sharing with me? I could go for some rabbit."
    show maplyemo happy at center
    maply "I don't mind, and I'm sure Fluff Tooth doesn't mind?"
    "The hound barked in agreement."
    show sabiaemo normalopen at left
    s "We'll need to be rested for tomorrow. The day could be long. And, we might come across our own battle, though I feel safer with both Fluff Tooth and Neve here."
    show sabiaemo normal at left
    show maplyemo sad2 at center
    maply "...you're not going to eat anything we got Saby?"
    show sabiaemo normalopen at left
    s "I'll eat something in the morning, Maply. I don't think I'd enjoy it right now, anyway."
    show maplyemo sad1 at center
    "Maply frowned a little, but lightened up when Neve asked for some. Sabia drifted into sleep to the sounds of the two talking and Fluff Tooth yipping and nipping, and before long she woke to the morning."
    scene bg black with dissolve
    pause (0.1)
    scene bg countryside
    call sabiabase
    show maply 1 at center
    show maplyemo normal at center
    show neve1 at right
    show neveemo normal at right
    with dissolve
    "Sabia stretched, yawned, and got up."
    "Glancing around their makeshift site, she noticed a pile of bones next to the fire, and an awake Maply and Neve chatting."
    show sabiaemo normalopen at left
    s "What happened to all the rabbit meat?"
    show sabiaemo irritated2 at left
    show maplyemo normalopen at center
    maply "We ate it all! Well, Fluff Tooth helped a bit. We didn't see him filch the rest until it was too late. Sorry, Saby."
    show neveemo normal at right
    n "I'm sure we can forage or hunt something as we track, Sabia."
    show sabiaemo normalopen at left
    s "No, it's fine. I want to focus on this, I can eat something after."
    show maplyemo angry2 at center
    show neveemo smirk1 at right
    maply "Maybe next time you can eat something with the rest of us."
    show maplyemo angry1 at center
    "There was a little bit of sting in Maply's words."
    show sabiaemo sad3 at left
    show neveemo normal at right
    s "Sorry, Maply. My thoughts are just a bit too occupied at the moment, next time I'll be more polite."
    show maplyemo happy at center
    maply "Aww, that's okay Saby!"
    show sabiaemo normalopen at left
    s "Let's start trying to track down Groknak's path, now. This is very important to me."
    maply "Sure, Saby."
    "It didn't take long for Sabia to realize just how thankful she was that Maply and Fluff Tooth were helping."
    "There was almost no chance she would have found the tracks by herself. They went down the water for some distance, before Maply spotted some signs on the tree bank."
    "Sabia could barely see it standing next to it, and even Neve was impressed."
    "After that, Fluff Tooth caught the scent of orc, and the three of them chased the hellhound through the underbrush to a clearing."
    show maplyemo sad2 at center
    maply "This'll be it, Sabia."
    show maplyemo sad1 at center
    "The hound, immensely pleased with itself, barked loudly, darting this way and that in the clearing, jumping around in circles."
    show maplyemo sad2 at center
    maply "I think we'll go wait back near the water."
    show maplyemo sad1 at center
    show sabiaemo normalopen at left
    s "Your eyes might catch something we miss, though, Maply."
    show maplyemo sad2 at center
    show sabiaemo normal at left
    maply "I think you'll be fine, and, I really don't like this place. It has a bad feeling to it."
    show neveemo closed4 at right
    maply "Too many bad memories of ambushes and attacks both on and from the caravans. I never enjoyed that."
    show sabiaemo normalopen at left
    show neveemo normal at right
    s "Okay, Maply. You'll be fine with Fluff Tooth I'm sure."
    show neveemo smirk1 at right
    n "Of course she will. That hound isn't going to let anything happen to her."
    scene bg black with dissolve
    pause (0.1)
    jump ef3_ambush_site


label ef3_ambush_site:
    scene bg forest
    call sabiabase
    show neve1 at right
    show neveemo normal at right
    with dissolve
    show sabiaemo normalopen at left
    s "It's been picked pretty clean... but I think we can find something around here."
    show sabiaemo normal at left
    "Both Sabia and Neve gave a sigh, looking around the small clearing in the middle of the forest."
    "There were two small campfires in the clearing, the coals long since devoid of heat."
    "Some items glinted on the ground, a little bit of sunlight poking through the canopy."
    menu ambush_site_menu:
        "Investigate the campfires." if ambush_site_campfires == False:
            $ ambush_site_investigation += 1
            $ ambush_site_campfires = True
            show neveemo closed3 at right
            n "Honestly, the whole camp seems a bit... unprofessional."
            show sabiaemo normalopen at left
            s "Unprofessional? Is there usually professionalism in orc camps?"
            show sabiaemo normal at left
            show neveemo normal at right
            n "Sometimes there is, and sometimes there isn't. Just like I imagine the same is true of humans, and even some elves."
            show sabiaemo normalopen at left
            s "Fair enough."
            show sabiaemo normal at left
            n "But for Groknak, yes, it's a bit unprofessional. It just seems... a bit lax."
            show sabiaemo normalopen at left
            s "What do you mean by lax, Neve?"
            show sabiaemo irritated2 at left
            show neveemo normal at right
            n "Well, take for instance the location itself. Is this somewhere you'd want to set up camp for the night?"
            n "Look at how open it is. There's no choke point, no real defensible positions of any sort. Every direction is open to attack - it's a clearing in the middle of a forest, Sabia."
            show neveemo irritated1 at right
            n "I refuse to believe Groknak or his orcs would have been, in any other situation, happy with it."
            show sabiaemo sad3 at left
            s "That's a good point. The thought had crossed my mind, but I have no experience with how he conducts excursions."
            show sabiaemo normal at left
            n "Look, even from here I can see the main path that the attacking force took - they weren't subtle about it at all."
            "Neve pointed off to the right. The underbrush was trodden, and there were a lot of fresh leaves and sticks on the ground that had been snapped off the trees as the force passed through."
            show neveemo closed3 at right
            n "And what's more, that would not have been quiet."
            show neveemo irritated1 at right
            "Demonstrating, Neve walked down through the foliage, her feet crunching loudly on the forest ground."
            show sabiaemo irritated1 at left
            s "..."
            show sabiaemo normalopen at left
            s "You're right."
            show sabiaemo irritated1 at left
            show neveemo closed3 at right
            n "It doesn't sit right with me that a force could walk up, through that, against seasoned veterans and not alert them."
            show sabiaemo normalopen at left
            s "They did come in the right direction though, Neve."
            show neveemo irritated1 at right
            show sabiaemo normal at left
            "Sabia crouched down, and closed one eye, looking down the forest path."
            show sabiaemo normalopen at left
            s "There's the slightest elevation from where they came, compared to the other directions. It would have given them a few extra moments of being concealed."
            show sabiaemo irritated1 at left
            show neveemo normal at right
            n "That's not something you'd expect from run of the mill bandits. Most wouldn't pay attention to something so small, in fact, I doubt most would realize it."
            n "I'm almost positive if we have a closer look... here, and there, we'll find some arrows shot for cover fire."
            show neveemo irritated1 at right
            "Neve pointed as she spoke, her brow furrowed in thought."
            n "I'm sure there's more here we can find, as well."
            menu:
                "Bottle" if ambush_site_bottles == False:
                    $ ambush_site_investigation += 1
                    $ ambush_site_bottles = True
                    show neveemo happy1 at right
                    n "Now, that's something interesting."
                    show sabiaemo irritated2 at left
                    "Neve picked it up, and waved it under her nose, sniffing."
                    show sabiaemo normalopen at left
                    s "Poison?"
                    show sabiaemo normal at left
                    show neveemo closed3 at right
                    n "Not quite."
                    show neveemo normal at right
                    show sabiaemo surprised1 at left
                    n "It's uh, basically a hangover cure."
                    show sabiaemo angry1 at left
                    s "They were drunk?"
                    show sabiaemo irritated2 at left
                    show neveemo closed3 at right
                    n "Maybe a bit more than drunk. This is some potent stuff. Most orcs usually just prefer to sleep it off. Or fight it off. Or fuck it off."
                    show neveemo irritated1 at right
                    show sabiaemo normalopen at left
                    s "I remember Jadk said some of Groknak's warriors were in The Silvertusk the night before."
                    show sabiaemo normal at left
                    show neveemo normal at right
                    n "Asking Jadk what they were drinking seems like a good idea."
                    jump ambush_site_menu
        "Investigate the campfires." if ambush_site_investigation >= 6:
            menu:
                "Blood":
                    $ ambush_site_investigated = True
                    show sabiaemo normalopen at left
                    s "What's this?"
                    show sabiaemo normal at left
                    "Sabia crouched down into a squat, and ran her finger through the red sliver."
                    "It had dried and stained the dirt."
                    show neveemo closed4 at right
                    n "Blood."
                    show neveemo normal at right
                    show sabiaemo normalopen at left
                    s "There's a trail."
                    show sabiaemo normal at left
                    "There were spots of blood all around, but both Sabia and Neve had missed the trail that led away from the clearing, into the crowded trees."
                    show neveemo irritated2 at right
                    n "Follow it."
                    "Sabia and Neve followed the trail of blood. It took them a hundred yards or so away, and they came upon a wounded orc."
                    "Hearing them approach, he grasped the handle of his axe, his grip barely strong enough to hold it."
                    "Upon seeing Neve, he gave a content sigh, and let the weapon go."
                    $ GenericOrc1.extras = ["Loincloth", "Hair", "Strap", "Shoulder", "Beard2", "Axe"]
                    $ GenericOrc1.face = "sad2"
                    show GenericOrc1 at center with dissolve
                    orc "Neve. Sabia. You've not recovered Warchief Groknak, then?"
                    $ GenericOrc1.face = "angry"
                    orc "Tarrak not die... on ass."
                    "With an effort that astounded Sabia, he managed to pull himself up onto his feet, leaning against a tree. He pushed Sabia away as she tried to help, shaking his head."
                    show sabiaemo surprised2 at left
                    s "You've been here for two days?!"
                    show sabiaemo surprised1 at left
                    show neveemo sad at right
                    "He grunted."
                    show sabiaemo sad1 at left
                    orc "Maybe someone come. Someone look. Can give... argh, fuck it hurts. Can give information."
                    $ GenericOrc1.face = "sad1"
                    show neveemo normal at right
                    n "Groknak - did you see him die?"
                    $ GenericOrc1.face = "sad2"
                    orc "...no. Not sure if Warchief is dead or alive."
                    $ GenericOrc1.face = "sad1"
                    show sabiaemo angry1 at left
                    s "Who ambushed you? Do you know who it was - was it Andian?"
                    show sabiaemo irritated2 at left
                    $ GenericOrc1.face = "sad2"
                    orc "...not... sure. Orcs all... still... half drunk."
                    orc "Fuck! That... that drink."
                    $ GenericOrc1.face = "sad1"
                    show sabiaemo angry1 at left
                    s "What drink? From the night you all drank at Jadk's?"
                    show sabiaemo irritated2 at left
                    $ GenericOrc1.face = "sad2"
                    orc "They were... well prepared. Knew Groknak coming... not sure who. Andian... maybe. Don't think so."
                    $ GenericOrc1.face = "sad1"
                    show sabiaemo sad1 at left
                    "He heaved a great sigh, breath rumbling in his throat as the stench of rotting flesh filled the air."
                    "His hand pressed harder against the seeping wound in his abdomen."
                    $ GenericOrc1.face = "sad2"
                    orc "Drink... from some, {i}ugh{/i}. Some merchant. Warchief..."
                    orc "...fuck!"
                    $ GenericOrc1.face = "sad1"
                    show sabiaemo sad3 at left
                    s "What merchant? Is Groknak alive or dead?!"
                    show sabiaemo sad1 at left
                    $ GenericOrc1.face = "sad2"
                    orc "Can't... wasn't... couldn't see... not sure..."
                    $ GenericOrc1.face = "sad1"
                    "He spat, the stuff red with blood as the last of his strength left him. He crumpled to the floor as the lack of blood and his wounds claimed him."
                    hide GenericOrc1 with dissolve
                    show sabiaemo sad3 at left
                    s "I can't believe he clung on for so long."
                    show neveemo closed4 at right
                    n "Orcs are tough. I thought you'd figured that out by now."
                    show neveemo normal at right
                    show sabiaemo normalopen at left
                    s "I knew that to start with... but to know it, and then see this. Well, that's a bit different."
                    s "Should we bury him? Burn him? I don't... I don't know the proper customs."
                    show sabiaemo irritated1 at left
                    show neveemo closed3 at right
                    n "We leave him here."
                    show neveemo normal at right
                    show sabiaemo angry1 at left
                    s "What?!"
                    show sabiaemo irritated2 at left
                    show neveemo irritated2 at right
                    n "You heard him, you saw all the evidence. Right now, our best lead is a merchant. And merchants travel, Sabia."
                    n "We're timed, here."
                    show sabiaemo sad1 at left
                    "Neve nodded toward the fallen warrior."
                    n "Trust me, he'd say the same."
                    show sabiaemo normalopen at left
                    s "I'll tell someone when we get back. I don't feel comfortable leaving his body to rot in the forest, and be eaten by wild animals."
                    show sabiaemo normal at left
                    show neveemo normal at right
                    n "You can do that. I wouldn't bother. Talk to Ylva about it later, it's not seen as something bad, it's just a part of life."
                    show sabiaemo normalopen at left
                    s "I... hmm."
                    show sabiaemo normal at left
                    show neveemo irritated1 at right
                    n "In the meantime, I'm going to go and see a friend."
                    show sabiaemo normalopen at left
                    s "Again?"
                    show sabiaemo irritated2 at left
                    show neveemo happy1 at right
                    n "I've a lot of questions. And some of the answers I'm sure you'll find yourself, but some of them I'll need to get myself."
                    n "I shouldn't be too long, no more than a few days."
                    show sabiaemo normalopen at left
                    s "Alright. I won't say no to extra information right now. I have some good leads to follow up on. Jadk to start with, he might know a little about the drink they had."
                    s "And Vehlis might have information on merchants and traders. I know she keeps reports and records of everything."
                    show sabiaemo normal at left
                    show neveemo happy3 at right
                    n "Good. And, Sabia. Try not to do anything too reckless while I'm gone, I'll see this through once I'm back."
                    n "You know the way back to Grok og Dar?"
                    show sabiaemo normalopen at left
                    s "I do."
                    show sabiaemo normal at left
                    show neveemo normal at right
                    n "Then I will leave you here."
                    show sabiaemo normalopen at left
                    s "Who are you going to see?"
                    show sabiaemo normal at left
                    show neveemo smirk1 at right
                    n "An answer for another time, Sabia."
                    hide neve1
                    hide neveemo
                    with moveoutright
                    "Giving Sabia a quick grin, Neve disappeared into the forest."
                    show sabiaemo normalopen at left
                    if chaos_kia_help == True:
                        s "I suppose Kia running off didn't matter too much. Following this lead isn't something Kia can track."
                    show sabiaemo sad1 at left
                    "Sabia glanced at the fallen orc, and though it didn't sit too right with her, she decided to follow Neve's advice. She would have to ask Ylva about it at a later time."
                    if chaos_maply_help == True:
                        "For now, Sabia had to head back, picking Maply up on the way."
                        jump eastern_frontier_map
                    else:
                        "Sabia decided to head back."
                        jump eastern_frontier_map
        "Investigate the trees." if ambush_site_damaged_tree == False or (ambush_site_arrow == False and ambush_site_campfires == True):
            menu:
                "Damaged tree" if ambush_site_damaged_tree == False:
                    $ ambush_site_damaged_tree = True
                    $ ambush_site_investigation += 1
                    show neveemo normal at right
                    "Neve let out a whistle as the two of them moved to the ring of trees surrounding the clearing. She ran a finger along the marred bark."
                    n "That's one mighty large chunk of wood hacked out of this."
                    show sabiaemo sad1 at left
                    "It looked more as if someone had started trying to lop the tree down and given up halfway through, than a misplaced strike in a battle."
                    show sabiaemo sad3 at left
                    s "...yeah."
                    show neveemo sad at right
                    n "What's wrong?"
                    show sabiaemo normalopen at left
                    s "Whoever attacked Groknak - they had at least one minotaur with them. I've seen what their axes driven by those muscles can do. I wouldn't fast forget it."
                    show sabiaemo sad1 at left
                    show neveemo normal at right
                    "Neve let out a half-surprised exhale."
                    n "I've met my fair share of minotaurs, but I've never been in a fight with them. That strike went almost halfway through the trunk."
                    show sabiaemo normalopen at left
                    s "They're a dangerous foe. You don't want to get caught off-guard by one - it'll probably be the last thing you do."
                    s "Unfortunately it doesn't really help us though. A minotaur here doesn't mean too much, other than we should be just a little more careful, I think."
                    show sabiaemo normal at left
                    n "I'm sure we can find something else."
                    jump ambush_site_menu
                "Arrow" if ambush_site_campfires == True and ambush_site_arrow == False:
                    $ ambush_site_arrow = True
                    $ ambush_site_investigation += 1
                    show sabiaemo normalopen at left
                    s "Here, Neve."
                    show sabiaemo normal at left
                    show neveemo closed1 at right
                    "Walking over, Neve's face went dark, and she yanked the arrow from the tree."
                    show neveemo irritated1 at right
                    n "Elven."
                    show sabiaemo normalopen at left
                    s "A motley crew..."
                    show sabiaemo irritated2 at left
                    show neveemo normal at right
                    n "And as I said, perfect direction for cover fire."
                    n "Not something regular bandits would do. Even some of the more incompetent commanders I've seen would let such a tactic slide."
                    show sabiaemo sad3 at left
                    s "I feel like I've got more questions now than when we started. It's not something I like."
                    show sabiaemo normal at left
                    "Neve was silent, a cloud over her face as she stared intently at the arrow."
                    show neveemo irritated1 at right
                    n "I think I'll keep this, for now, Sabia."
                    show sabiaemo normalopen at left
                    s "Er, of course. I don't need it."
                    show sabiaemo normal at left
                    show neveemo normal at right
                    n "There might be something else here we're missing, have another look around."
                    jump ambush_site_menu
        "Investigate the ground" if ambush_site_glinting_items == False or ambush_site_furrowed_ground == False:
            "Taking a closer look, Sabia could see there was more on the ground than she had first thought."
            menu:
                "Glinting items" if ambush_site_glinting_items == False:
                    $ ambush_site_investigation += 1
                    $ ambush_site_glinting_items = True
                    "The gleam caught Sabia's eye."
                    show sabiaemo normalopen at left
                    s "Hmm. There are some rings and coin here..."
                    show sabiaemo normal at left
                    show neveemo closed3 at right
                    n "That's odd."
                    show neveemo normal at right
                    show sabiaemo normalopen at left
                    s "Yes. It's only a few rings and a couple of coins, and the bodies have been cleared. So they spent the time to clean up... and missed some of the spoils."
                    show sabiaemo irritated2 at left
                    show neveemo closed3 at right
                    n "That doesn't really fit a proper, organized force. Nor does it fit regular bandits - they'd make sure everything is looted."
                    show neveemo happy1 at right
                    n "But we might be able to look into if anyone's tried fencing anything recently, or an influx of wealth somewhere? Might get lucky."
                    show sabiaemo normalopen at left
                    s "I can't imagine anyone who is capable of taking down a Warchief's party would be too foolish to sell their spoils so quickly, but you're right - we might get lucky."
                    s "There might be something else to give us a lead here still, though."
                    show sabiaemo normal at left
                    jump ambush_site_menu
                "Furrowed ground" if ambush_site_furrowed_ground == False:
                    $ ambush_site_investigation += 1
                    $ ambush_site_furrowed_ground = True
                    show sabiaemo normalopen at left
                    s "What's this...? Tracks in the ground?"
                    show sabiaemo irritated2 at left
                    show neveemo irritated2 at right
                    n "Looks like they had a cart in here."
                    show sabiaemo normalopen at left
                    s "Groknak wouldn't have had a cart. That means the force that attacked them did."
                    show sabiaemo irritated2 at left
                    show neveemo closed4 at right
                    n "Seems that way. But a cart for what purpose, that's a bit harder to pin down Sabia."
                    show neveemo normal at right
                    show sabiaemo normalopen at left
                    s "Hmm. Could be what they used to cart the bodies away. Or to take all the spoils."
                    show sabiaemo irritated2 at left
                    show neveemo irritated2 at right
                    n "Difficult to say, Sabia. I'm sure there are more clues about."
                    jump ambush_site_menu


label ef3_merchants_quest:
    $ chaos_met_merchants = True
    $ phase3_nevegone = True
    scene bg road
    call sabiabase
    with dissolve
    "With both the tentacle slime, and the stamina potion Vehlis had thought to give her, Sabia straightened her belt and scabbard."
    show sabiaemo closed4 at left
    s "No time to lose, then."
    show sabiaemo normal at left
    "Sabia made sure not to stay too close to the main road as she set off."
    "She had been expecting she might need to down the stamina potion to keep up pace, and to close in on the merchant."
    "Thankfully, it seemed that either they - for it turned out to be two merchants - might have stopped to rest after leaving Grok og Dar."
    show sabiaemo normalopen at left
    s "Hmm, Vehlis didn't mention it was two merchants. I wonder if she was aware of that?"
    s "Or if only one of them came into the camp?"
    show sabiaemo normal at left
    "From what she could see, the small rickety cart that their two horses were pulling looked rather bare."
    "It seemed that most of their wares had already been sold."
    show sabiaemo closed2 at left
    "A thought crossed her mind - should she speed up a little, and settle down into a rhythm next to them?"
    show sabiaemo closed4 at left
    s "Probably best not to. They might hedge their conversation a bit while still on the road, next to a stranger."
    show sabiaemo normalopen at left
    s "Drink makes people a bit lax, though. The inn is still my best bet."
    show sabiaemo normal at left
    "With that in mind, Sabia spent the next couple of days following behind far enough that the merchants didn't see."
    scene bg black
    pause(0.01)
    scene bg road3tavern
    with dissolve
    "Eventually, all three of them came to the inn, and the two packed up the few remaining pieces they had, stabled their horses, and went into the inn."
    "Waiting outside, Sabia walked around the few buildings that had managed to pop up thanks to the traffic an inn affords, watching."
    "After an hour or so, with the merchants inside, and drinking from a table, Sabia judged that it was time to enter."
    scene bg black
    pause(0.01)
    scene bg HGNdajrab1
    with dissolve
    "Thankfully, no one seemed to remember her, and she took a table not too far from the two men she was following, and ordered a drink."
    "Sabia knew she would have to talk to them to get the information she needed."
    call sabiabase
    show sabiaemo closed2 at left
    with dissolve
    s "(I should listen in on them, and pay attention to what they say. I don't want to say something that's too unbelievable...)"
    show sabiaemo normal at left
    "As Sabia listened, she heard them exchanging multiple stories, and their beliefs on the validity of them. It felt familiar, and reminded her a little bit of the time she spent commanding."
    "She quickly realized that to keep them drinking when she introduced herself, she'd have to make sure her limited trade stories would be reasonable to them."
    "Once they got a little more drunk, she could use some of the more outlandish ones, and they'd probably buy it."
    show sabiaemo closed2 at left
    s "(This would be a lot easier if Vehlis were here... I only have so many stories that I can twist into a merchant scenario...)"
    show sabiaemo normal at left
    m1 "You know, Alensa said, the other day, when we was in town, that she had some Makhor claws."
    m2 "Makhor claws? Are you a fucking idiot. One: why would she have Makhor claws? She comes off bad in every deal."
    m2 "Two: how the fuck would she have gotten Makhor claws? You ever fucking seen a Makhor? How many people have you even heard talking about Makhors?"
    show sabiaemo closed2 at left
    s "(Better not say anything about Kia until they're pretty drunk... and, well, they're not wrong. If I hadn't met Kia, I would think the same.)"
    show sabiaemo normal at left
    m1 "All I'm sayings, is, maybe we should look and see if she's got them. They'd sell well somewhere!"
    m2 "She's as likely to have Makhor claws as she's gonna trade enchanted bows from Elves."
    m1 "Alensa said she did that too!"
    m2 "You're an idiot."
    m2 "You know what probably happened? She probably tried to sell axes to orcs, and instead of making the easiest sell, she got groped and fucked."
    m1 "What?! Alensa?! No way. If anyone's gonna grope and fuck Alensa, it's gonna be me!"
    m2 "You?! Haha."
    m2 "Not a chance. An orc's got way more of a chance with Alensa than you. They just grab and take what they want, after all."
    show sabiaemo closed1
    "Whoever Alensa was, Sabia realized the second merchant didn't have very much respect for her."
    "The first though, clearly liked Alensa and the feeling wasn't reciprocated."
    show sabiaemo annoyed2 at left
    "Sabia sighed, rolling her eyes a little. They weren't wrong about orcs wanting to grab and fuck, though. For the most part, anyway."
    show sabiaemo closed4 at left
    s "(I better not have to fuck them to get what I need out of them... but that first one, he seems so pent up. It might be the easiest way.)"
    show sabiaemo normal at left
    "Sabia missed a few sentences, lost in thought, but managed to slip back into listening."
    m2 "I'm telling you, if you wanna fuck Alensa, just set her up with that banker from Carchedon."
    show sabiaemo irritated2 at left
    m1 "What? She'll probably fuck HIM instead of me!"
    m2 "You think someone from Carchedon is gonna bother fucking a boring girl like Alensa, when they have all types of slaves?"
    m2 "Carchedonese are made for deals and trades. It's easy, quick, and it'll be big for her. She'll be begging to suck your dick to thank you."
    show sabiaemo annoyed2 at left
    m1 "I mean... I guess. Maybe. Fuck, I wish this inn had some whores. We've got all this gold and no pussies to fuck!"
    m2 "Yeah, just wait till we get back to the city. Maybe you can just buy Alensa."
    "The second trader snorted in laughter, took a swig of ale, then spat it out as he couldn't stop himself from letting out a raging guffaw."
    m1 "Fuck you."
    m2 "Yeah, if you give Alensa enough money, maybe that's what she'll do."
    show sabiaemo normal at left
    "The two men settled into a little bit of a lull in conversation. The perfect time to slip herself into their table."
    "Moving over, she grabbed up a chair, and sat down, before speaking."
    show sabiaemo happy2 at left
    s "Hi, there! My name's Sab...rina. Sabrina."
    show sabiaemo closed2 at left
    s "(...I should have had a name ready...)"
    show sabiaemo normal at left
    m2 "Uh... hello?"
    m1 "Hi!"
    show sabiaemo happy3 at left
    s "I couldn't help but overhear you two talking about trading deals and bankers and stuff."
    s "And you both sound really experienced in it! I thought I'd try to break out into being a merchant, since my Dad's farm was way too boring."
    show sabiaemo sad3 at left
    s "But... everything keeps going wrong for me! Trading is so hard!"
    show sabiaemo pout2 at left
    m2 "Hard? It's only hard if you're bad at it. Like my friend, Tomas here."
    m1 "It's not... I, that is... fuck you Harald."
    show sabiaemo irritated2 at left
    "Sabia couldn't help but feel both sets of eyes drinking in her body, her curves."
    "Trying her best not to roll her eyes, she knew it was going to come down to sex. Or something close."
    show sabiaemo normal at left
    "She leaned in closer, pressing her tits against the table."
    show sabiaemo sad3 at left
    s "Are you sure? Because, I've just been getting screwed over, all the time! Literally!"
    show sabiaemo sad1 at left
    "Tomas seemed unable to peel his eyes away from her breasts."
    m1 "Uh, how's that? Maybe, if you tell us a story, we might be able to see what you did wrong?"
    "The other merchant, Harald, glared at Tomas, rolled his eyes, and sighed."
    show sabiaemo closed2 at left
    s "(I'd better start off with something believable... something that a new trader would be familiar with...)"
    s "(And I'd better make it sexual, judging from their greedy eyes.)"
    menu ef3_merchants_quest_menu:
        "A catgirl tried to steal my stuff, and then I fucked her!" if chaos_merchants_quest_catgirls == False:
            $ chaos_merchants_quest_catgirls = True
            if chaos_merchants_quest == 0:
                show sabiaemo sad3 at left
                s "Well, I'd organized a deal with a catgirl caravan."
                m1 "That's a bad idea to start with!"
                m2 "No shit, any decent merchant could have told you that."
                show sabiaemo normalopen at left
                s "Well, like I said, I was new! And, well."
                m1 "Yes?"
                show sabiaemo
                s "Well, we were doing a trade - they wanted some tools, and I was buying some interesting trinkets."
                show sabiaemo closed4 left
                s "Stuff that they said they'd scavenged."
                m2 "Scavenged. Sure. More like stole!"
                show sabiaemo pout2 at left
                s "Yeah, I think so too. Because, while we were trading, I looked over, and I saw one of the catgirls stealing stuff from my cart!"
                m1 "Noooo! That's awful."
                show sabiaemo angry1 at left
                s "So, I called her out on it. I said 'Hey! What are you doing, that's my stuff. Why are you stealing it?!'"
                show sabiaemo normalopen at left
                s "And I guess she might have felt bad, because, she came over and apologized about it."
                m2 "A catgirl... apologizing for stealing?"
                s "Well, at the time, I thought it was nice of her."
                show sabiaemo happy3 at left
                s "And, also, she was really hot. Her boobs were, I think, almost three sizes bigger than what all the other catgirls had."
                m1 "Whoa! Really?! Those are some... big boobs!"
                "Tomas licked his lips, eyes several degrees lower than they would have needed to be to look into Sabia's eyes."
                show sabiaemo normalopen at left
                s "Yeah. So, I told her, I'd accept the apology if we could... y'know, have some {i}fun{/i}."
                show sabiaemo happy3 at left
                s "At the time, I didn't have any toys at all, so I just ate her out."
                s "And then slapped her boobs a little bit - she really liked it. She was squeaking and yelping, and shuddering."
                s "She had sensitive nipples and her whole body shook when I pinched them!"
                m1 "So, uhm, I mean - well, I guess it turned out alright, then?"
                show sabiaemo sad3
                s "Well, that's what I thought too. But when I left the caravan, I realized one of the other catgirls had stolen the same thing while I was making her eat me out!"
                m2 "I can believe that you ended up getting it stolen after all!"
                show sabiaemo happy3 at left
                "The three continued chatting, and both of the merchants sipped at their drink a little bit."
                "A while passed, and the conversation was dying down a little bit."
                "Sabia thought to pull her trump card."
                jump ef3_merchants_quest2
            else:
                $ chaos_merchants_quest += 1
                show sabiaemo sad3 at left
                s "Well, I'd organized a deal with a catgirl caravan."
                show sabiaemo normal at left
                m1 "That's a bad idea to start with!"
                show sabiaemo irritated2 at left
                m2 "Nooo! You can't... can't do good deals with catgirls! They steal stuff all the time!"
                show sabiaemo closed4 at left
                s "Well, like I said, I was new! And, well, their offer was really good even though I'd been told that!"
                show sabiaemo normal at left
                m1 "Yes?"
                show sabiaemo normalopen at left
                s "Well, we were doing a trade - they wanted some tools, and I was buying some interesting trinkets."
                s "Stuff that they said they'd scavenged."
                show sabiaemo normal at left
                m2 "Probably stole it - like they stole your stuff! That's {i}hic{/i} what happened right, they stole stuff?"
                show sabiaemo normalopen at left
                s "Yeah, one of them did. She was rummaging through my cart, taking her pick while I was trying to deal with another!"
                m1 "Noooo! That's awful."
                show sabiaemo angry1 at left
                s "So, I called her out on it. I said 'Hey! What are you doing, that's my stuff. Why are you stealing it?!'"
                s "And I guess she might have felt bad, because, she came over and apologized about it."
                show sabiaemo irritated2 at left
                m2 "They... {i}hic{/i} tricked you t-there!"
                show sabiaemo normalopen at left
                s "Well, at the time, I thought it was nice of her."
                show sabiaemo happy2 at left
                s "And, also, she was really hot. Her boobs were, I think, almost three sizes bigger than what all the other catgirls had."
                m1 "Whoa! Really?! Those are some... {i}hic{/i} big boobs!"
                "Tomas licked his lips, eyes several degrees lower than they would have needed to be to look into Sabia's eyes."
                show sabiaemo normalopen at left
                s "Yeah. So, I told her, I'd accept the apology if I could fuck her."
                s "At the time, I didn't have any toys at all, so I just ate her out."
                show sabiaemo happy1 at left
                s "And then slapped her boobs a little bit - she really liked it. She was squeaking and yelping, and shuddering."
                s "She had sensitive nipples and her whole body shook when I pinched them!"
                m1 "So, uhm, I {i}hic{/i} mean - well, I guess it turned out alright, then?"
                show sabiaemo angry1 at left
                s "Well, that's what I thought too. But when I left the caravan, I realized one of the other catgirls had stolen the same thing while I was making her eat me out!"
                show sabiaemo normal at left
                m2 "They'll - uh, catgirls will do that. They're sneaky and thievy."
                "All three continued chatting, and both of the merchants drank even more, their words starting to slur, and their attitudes more friendly and agreeable."
                "A while passed, before they came back around to Sabia's supposed merchanting, and they asked for another story."
                jump ef3_merchants_quest_menu
        "Deal with a Carchedonese banker as they were fucking a slave." if chaos_merchants_quest_banker == False:
            $ chaos_merchants_quest_banker = True
            $ chaos_merchants_quest += 1
            m1 "A slave? Hot. How big were the slave's tits? Was she branded? Tattooed? Pierced?"
            show sabiaemo surprised1 at left
            "The barrage of questions almost knocked her off her train of thought."
            "She had envisioned Vehlis and Alioch, but clearly these traders were imagining a male master and a female slave."
            show sabiaemo normal at left
            "Well, that probably worked out better - helped hide an identity, and Tomas was getting excited, and she could see Harald's eagerness to hear more."
            "Both of them picked up their drinks, and took a heavy swig, waiting for Sabia to tell the story."
            show sabiaemo happy1 at left
            s "Tits? Really big."
            "Sabia's chair legs screeched as she pushed herself back, and cupped her boobs teasingly."
            show sabiaemo eyebrow1 at left
            s "I'd say... probably twice as big as these!"
            m2 "Holy shit! That's... wow, those are some big boobs!"
            show sabiaemo happy1 at left
            s "And tattooed? Yep! And pierced too. Big barbell piercings on those giant tits!"
            show sabiaemo normal at left
            s "So anyway, I had organized a meeting with the banker, and, well, I walked in, and the slave was getting {i}demolished{/i} on the floor."
            show sabiaemo lick1 at left
            s "I have to admit, I might have been a little bit envious. It looked like a lot of fun!"
            m1 "R... really?"
            show sabiaemo sad3 at left
            s "Yeah. But, we ended up doing the deal, and I had to go. He didn't offer any fun as part of the sale!"
            show sabiaemo sad1 at left
            m2 "That's too bad!"
            show sabiaemo eyebrow1 at left
            s "Yeah, too bad indeed. It would have been an experience to know what it was like to be treated like a slave."
            "The two men laughed uproariously, shifting in their seats not-so-subtly, their excitement palpable."
            "All three continued chatting, and both of the merchants kept drinking, getting a little more intoxicated by the moment."
            show sabiaemo closed2 at left
            s "(If I keep them drinking... they'll be a lot more agreeable, and everything will be easier.)"
            show sabiaemo normalopen at left
            "A while passed, before they came back around to Sabia's supposed merchanting, and they asked for another story."
            jump ef3_merchants_quest_menu
        "Tried to buy a hellhound - but it just fucked me instead!" if chaos_merchants_quest_hellhound == False:
            $ chaos_merchants_quest_hellhound = True
            if chaos_merchants_quest == 0:
                m2 "A hellhound? Not a chance."
                show sabiaemo normalopen at left
                s "Yeah! I thought, a hellhound - wow, what a prize."
                show sabiaemo irritated2 at left
                m1 "But no one buys hellhounds! The only ones crazy enough to train them are orcs. And they don't sell."
                m2 "Not that you can even train hellhounds to begin with."
                show sabiaemo closed2 at left
                "Sabia laughed nervously."
                show sabiaemo happy3 at left
                s "Well, I know that, {i}now{/i}."
                show sabiaemo normalopen at left
                s "But at the time, I thought that if I could get one, and take it back to the city, it'd be amazing."
                m2 "And you said, that the hellhound fucked you? And you're happy to say that?"
                show sabiaemo pout1 at left
                s "Shh! Don't say it too loudly. It's embarrassing! But, it did fuck me, as I was trying to lead it back to the city."
                m1 "What'd it feel like?"
                show sabiaemo closed2 at left
                s "...different. I can't say I enjoyed it too much, but it was definitely an experience."
                show sabiaemo normalopen at left
                "Both Tomas and Harald looked in silence at Sabia for a moment, before giving a half-hearted chuckle."
                m1 "What happened to it?"
                show sabiaemo sad3 at left
                s "It ran away!"
                m2 "It just ran away?"
                show sabiaemo normalopen at left
                s "It's a bit hard to restrain a hellhound. Something I learned."
                show sabiaemo happy3 at left
                s "That's sort of why I wanted to chat to you guys, and learn a little bit more about good and bad deals."
                s "So, next time, I don't feel forced to make bad purchases."
                show sabiaemo normal at left
                "The three continued chatting, and both of the merchants sipped at their drink a little bit."
                "A while passed, and the conversation was dying down a little bit."
                "Sabia thought to pull her trump card."
                jump ef3_merchants_quest2
            else:
                $ chaos_merchants_quest += 1
                m2 "W-what? No {i}hic{/i} way!"
                show sabiaemo happy1 at left
                s "Yeeeep! I thought, a hellhound - wow! What a prize."
                m1 "No one buys hellhounds, 'cause, they are almost {i}hic{/i} impossible to train!"
                show sabiaemo happy3 at left
                s "Well. I know that. {i}Now{/i}."
                show sabiaemo normalopen at left
                s "But at the time, I thought, if I could take a hellhound back for a good price - everyone would be amazed."
                m2 "And... you said {i}hic{/i} it... that it... I mean, {i}hic{/i} that, you said it fucked you?"
                show sabiaemo pout1 at left
                s "Shh! Don't say it too loudly. It's not something I'm proud of. But, as I was trying to lead it back to the city, it uh..."
                m1 "Fucked you! {i}hic{/i}"
                show sabiaemo pout3 at left
                s "Yeah... it did."
                m1 "Jeez... what'd it {i}hic{/i} feel like? Was it, like rough? Did you end up with scratches?"
                show sabiaemo normalopen at left
                s "Well, yeah. It definitely scratched me, but it wasn't uh, it wasn't trying to do it on purpose."
                s "I don't think so, at least."
                show sabiaemo normal at left
                m2 "Did you end up getting it back to the city?"
                show sabiaemo sad3 at left
                s "No. It ran away after it finished fucking me. A giant load of hellhound jizz, right up inside me, and then it ran away!"
                show sabiaemo pout3 at left
                "Both Tomas and Harald looked in silence at Sabia for a moment. Then burst out into uncontrollable laughter, their mugs of ale jostled and spilling."
                m1 "It ran away?!"
                m2 "All that for nothing! It would've fetched a fine {i}hic{/i} price!"
                show sabiaemo normalopen at left
                s "It would have. This is why I wanted to talk to you guys, and learn a little bit more about how to do deals properly."
                show sabiaemo happy3 at left
                s "So next time, I don't feel forced to make such crazy purchases!"
                "All three continued chatting, and both of the merchants drank even more, their words starting to slur, and their attitudes more friendly and agreeable."
                "A while passed, before they came back around to Sabia's supposed merchanting, and they asked for another story."
                jump ef3_merchants_quest_menu
        "Orcs just groped and felt me up instead of buying my stuff!" if chaos_merchants_quest_orcs == False:
            $ chaos_merchants_quest_orcs = True
            $ chaos_merchants_quest += 1
            show sabiaemo annoyed1 at left
            s "Ugh, I heard you mention orcs before."
            s "You're definitely right."
            m1 "What about?"
            s "They don't wanna trade or buy or sell!"
            show sabiaemo irritated2 at left
            m2 "Not when you look like you do, if you don't mind me saying."
            show sabiaemo question1 at left
            "Sabia gave a little trill of a giggle, doing her best impression of a coquettish blush."
            show sabiaemo normalopen at left
            s "Well, lemme just say, that I definitely knew what it felt like to have an orc hand on my butt by the end of it."
            show sabiaemo pout2 at left
            m1 "Didn't you try to stop them?"
            show sabiaemo sad3 at left
            s "I {i}really{/i} needed the deal to go through. My boobs were sore for a day afterwards, with how much they groped and felt me up."
            show sabiaemo normalopen at left
            s "They were as nice about it as I could expect orcs to be though, they said they were the best boobs and ass they've seen!"
            show sabiaemo2 blush at left
            m1 "Maybe we can judge that for ourselves later, hah!"
            show sabiaemo happy3 at left
            s "...maybe! You'll have to tell me more about trading secrets first though!"
            "Tomas and Sabia chuckled, while Harald licked his lips, glaring blatantly at Sabia's assets."
            "All three continued chatting, and both of the merchants kept drinking, getting a little more intoxicated by the moment."
            show sabiaemo closed2 at left
            s "(If I keep them drinking... they'll be a lot more agreeable, and everything will be easier.)"
            "A while passed, before they came back around to Sabia's supposed merchanting, and they asked for another story."
            jump ef3_merchants_quest_menu
        "A real Makhor stole the Makhor claws I was selling!" if chaos_merchants_quest_makhor == False:
            $ chaos_merchants_quest_makhor = True
            if chaos_merchants_quest == 0:
                m2 "A real Makhor came down, and stole Makhor claws, that you'd purchased?"
                show sabiaemo happy3 at left
                s "Yeah, a real Makhor. I'd managed to purchase some claws from an orc."
                show sabiaemo closed4 at left
                s "I was told they were worth a lot, and I wasn't entirely sure that it was correct."
                show sabiaemo normalopen at left
                s "But it seemed that it was true - at least for another Makhor."
                show sabiaemo normal at left
                m1 "Well, something like that is a good opportunity. They sell very well in the cities."
                show sabiaemo normalopen at left
                s "That's what I thought."
                show sabiaemo closed2 at left
                m2 "So, tell me about the Makhor. How big was it? How did you not get eaten?"
                show sabiaemo normalopen at left
                s "Very big. At least five times the size of me. And, I assume I didn't get eaten because I handed the claws back pretty quickly!"
                show sabiaemo happy3 at left
                s "I guess the Makhor was nice, since it left me alone after."
                show sabiaemo irritated2 at left
                m2 "A Makhor came down, stole Makhor claws from you - and didn't attack you, then flew away?"
                show sabiaemo happy3 at left
                s "Well, I suppose it didn't really steal them. I gave them back."
                show sabiaemo closed2 at left
                "The skepticism was writ clearly on their faces, and Sabia regretted jumping into something so crazy, before they were smashed."
                "The only way she could have made the story more unbelievable were if she just told the actual story about Kia and the Makhor bones."
                show sabiaemo normal at left
                "The three continued chatting, and both of the merchants sipped at their drink a little bit."
                "A while passed, and the conversation was dying down a little bit."
                "Sabia thought to pull her trump card."
                jump ef3_merchants_quest2
            else:
                $ chaos_merchants_quest += 1
                m1 "I wouldn't... if {i}hic{/i}... I mean, a - well, {i}hic{/i} a Makhor?!"
                show sabiaemo happy3 at left
                s "Yeah! A Makhor. I managed to purchase some claws from an orc."
                show sabiaemo closed4 at left
                s "I was told they were worth a lot. I wasn't entirely sure that it was correct... but it seemed a good opportunity."
                show sabiaemo normal at left
                m2 "S'very good opportunity... Makhor clawssh're exshpenshive! {i}hic{/i}!"
                m2 "'Caush, you don't... don't really see {i}hic{/i} too many!"
                show sabiaemo normalopen at left
                s "That's what I thought. I'd heard about Makhors, but I'd never actually seen one. Or even seen their claws, or teeth, or bones!"
                show sabiaemo normal at left
                m1 "Wash... {i}hic{/i} wash the Makhor really... really big? How'd you.. you not get eaten?!"
                show sabiaemo eyebrow1 at left
                m1 "Cause... if I were... were the Makhor {i}hic{/i}! I'd... I'd totally eat you out!"
                "The awful joke seemed to delight Tomas, and he giggled drunkenly as Sabia brushed it off, trying her best to ignore it."
                "She was a little tipsy by now - she couldn't drink nothing. But she was drinking far, far less than either Tomas or Harald."
                show sabiaemo happy3 at left
                s "Well, thankfully the Makhor was sort of nice! I realized very quickly that they only wanted the claws."
                m1 "Didja... didja give 'em the clawsh?"
                show sabiaemo closed4 at left
                s "Of course! Otherwise I think I might have ended up with a second set of claws. But a bit more deadly than the ones I already had."
                show sabiaemo normal at left
                m2 "A Makhor! You're... you... you! {i}hic{/i} You're unlucky!"
                show sabiaemo normalopen at left
                s "I know. There was a lot of lundils tied up in those claws. But, I suppose what I bought with them was worth it - my life."
                show sabiaemo normal at left
                "Sabia didn't need to try too hard now, both Tomas and Harald were completely hammered, and as horny as they'd ever be."
                show sabiaemo irritated2 at left
                "She tried to pry some of the information out of them that she needed, but they simply broke down into a fit of giggles, shaking their head."
                show sabiaemo annoyed2 at left
                s "(Fuck sake...! I'll need to get them back to their room at least. I don't want to do anything so public.)"
                jump ef3_merchants_quest2
        "Elf fucking me with dildo instead of selling me goods." if chaos_merchants_quest_elf == False:
            $ chaos_merchants_quest_elf = True
            if chaos_merchants_quest == 0:
                show sabiaemo irritated2 at left
                m2 "That seems a bit unlikely."
                m2 "I can't say any of my trade deals have spontaneously combusted into sex."
                show sabiaemo happy3 at left
                s "Well, I guess that's because you two are such good traders, right?"
                m1 "And trading with an Elf? Some of them don't mind buying and selling. But it's not the most common thing."
                show sabiaemo pout3 at left
                s "Really? So I was pretty much wasting my time going out there, then, was I?"
                m2 "You're the one telling the story, Sabrina. Did you get a good deal, then?"
                show sabiaemo normalopen at left
                s "Well, the Elf wanted to play a little bit before a deal... testing out a new enchantment, apparently."
                s "An enchanted dildo..."
                show sabiaemo irritated1 at left
                m2 "I'm sorry, but I'm gonna have to call bullshit on this!"
                m1 "Aww, why? She could be telling the truth. You've seen some of those Elves getting antsy. And we did a deal with a couple this very month!"
                m2 "Be quiet Tomas. We're experienced merchants, we've had to work our way up to getting reliable trades with Elves."
                m2 "And when was the last time you had your dick sucked by one, as part of a sale?"
                show sabiaemo happy3 at left
                s "Well, just to be clear, I sort of got, uh... tentacle dicked. You're welcome to try it if you want me to take you to the Elf!"
                show sabiaemo irritated2 at left
                "Harald glared at Sabia. A moment passed, and him being tipsy, along with Sabia's awful attempt at a joke got to him."
                show sabiaemo happy3 at left
                "He smirked, and then broke into a laugh, Tomas joining him. Sabia sighed thankfully, though she was sure they still doubted her."
                "The three continued chatting, and both of the merchants sipped at their drink a little bit."
                "A while passed, and the conversation was dying down a little bit."
                "Sabia thought to pull her trump card."
                jump ef3_merchants_quest2
            else:
                $ chaos_merchants_quest += 1
                show sabiaemo annoyed2 at left
                m1 "Haha... hehehe! Magic dildo!"
                m2 "Elvsh... Elvsh like magic thingsh!"
                show sabiaemo normalopen at left
                s "They do! I tried to purchase some other things, but she said she wouldn't sell me anything unless we... did something first."
                show sabiaemo normal at left
                m1 "Tell ush! {i}hic{/i}"
                show sabiaemo normalopen at left
                s "She was very sexual - are all Elves like that, do you know?"
                show sabiaemo normal at left
                m2 "Shome... shome are... but... s... some aren't. They're all different, like ush!"
                show sabiaemo pout3 at left
                s "Oh, I see. Well, I guess I was just unlucky that I got that one. Like I said, I've not been lucky so far with my new trade."
                s "I just wanted to buy some enchanted flasks and pots."
                show sabiaemo normal at left
                m1 "They... they shell well!"
                show sabiaemo normalopen at left
                s "I know a lot of people who would have liked those, yes!"
                show sabiaemo pout3 at left
                s "But... instead, she said she'd only sell to me if we... ugh, it's embarrassing!"
                show sabiaemo closed1 at left
                "Sabia gave an uncharacteristic squeak, and covered her face with her hands, peeping through her parted fingers."
                "She could tell that both Tomas and Harald were spellbound by her story, and she hid the smirk behind her hands for a moment."
                show sabiaemo eyebrow1 at left
                m1 "Don't stop, we wanna hear the story! What'd she do?!"
                show sabiaemo normalopen at left
                s "Well... she had an enchanted dildo. I think it might have been a tentacle! And it was all wiggly."
                show sabiaemo normal at left
                show sabiaemo2 blush at left
                "Sabia wiggled both of her index fingers as she said it, much to Tomas' amusement, and Harald's excitement."
                show sabiaemo normalopen at left
                s "So... well, I really needed it for a big sale, so I said yes."
                show sabiaemo happy3 at left
                s "And... I don't want to go too much into details, but I ended up buying one of those off of her too!"
                hide sabiaemo2 blush at left
                show sabiaemo normal at left
                "Sabia didn't need to try too hard now, both Tomas and Harald were completely hammered, and as horny as they'd ever be."
                "She tried to pry some of the information out of them that she needed, but they simply broke down into a fit of giggles, shaking their head."
                show sabiaemo closed2 at left
                s "(Fuck sake...! I'll need to get them back to their room at least. I don't want to do anything so public.)"
                jump ef3_merchants_quest2


label ef3_merchants_quest2:
    if chaos_merchants_quest > 0:
        show sabiaemo happy3 at left
        s "Actually - I just remembered. I have something that I think is worth a lot. Well, I hope it is, because I paid a lot for it!"
        show sabiaemo normal at left
        m1 "What... whatcha got?"
        show sabiaemo closed1 at left
        "Sabia leaned across the table, glanced sideways, and whispered conspiratorially."
        show sabiaemo closed3 at left
        s "We should head to your room. I don't want anyone seeing what I have, since it's meant to be so valuable."
        show sabiaemo eyebrow1 at left
        "Tomas and Harald's eyes widened, and they too leaned across the table."
        show sabiaemo normalopen at left
        s "It's tentacle slime."
        show sabiaemo normal at left
        "Before they could say anything, Sabia put a finger to her lips, and made a 'hush' sound."
        "She could see the interest and greed on their faces though, mixed with the desire for Sabia's body that was plain as day."
        m1 "That'sh... that'sh a good idea. We'll go up! Let'sh go Harald."
        m2 "Right behind you!"
        m1 "C'mon... Shabrina!"
        "Sabia nodded, smiling."
        "Both Harald and Tomas were smashed by now, and they stumbled their way forwards, leading Sabia to their room."
        "She had to take the key off them to open the door, and they tumbled in, taking lurching steps before landing on the bed."
        "Sabia scanned the room as quickly as she could."
        if ambush_site_jadk == False:
            show sabiaemo question1 at left
            "She noticed a letter on the desk, unsealed, and unsent. It would be a good idea to check that out."
        show sabiaemo normal at left
        "Opposite the end of the bed stood a large set of drawers. A heavy unlit brass lamp rested there."
        "If Sabia wanted to... she could..."
        menu:
            "Get them to talk with sex.":
                $ chaos_merchants_quest_resolution = "sex"
                scene bg black with dissolve
                call merchant_good_end
                play music forest fadeout 2.0 fadein 2.0
                scene bg black with dissolve
                scene bg HGNdajrab1
                call sabiabase
                with dissolve
                jump ef3_merchants_quest3
            "Knock them out, and rifle through their stuff.":
                $ chaos_merchants_quest_resolution = "knockout"
                show sabiaemo happy1 at left
                s "Hey, close your eyes for a moment, I don't want you to see where I keep my slime!"
                "Both Tomas and Harald complied, and Sabia made her best effort at making it sound like she was rifling through her pockets."
                show sabiaemo eyebrow1 at left
                call shake ("h")
                "Instead, she took a few quiet steps over to the drawers, grabbed the brass lamp, and whapped it hard across Harald's head."
                show sabiaemo irritated2 at left
                m1 "What're you doing?!"
                "Tomas cried out loudly, jumping to his feet with confusion and horror on his face as his friend flopped back onto the bed limply."
                "He lunged toward Sabia, awkward, and untrained. She dodged the strike easily, and whapped Tomas over the head too."
                show sabiaemo normalopen at left
                s "Light's out, boys."
                jump ef3_merchants_quest3
    else:
        show sabiaemo happy3 at left
        s "Actually - I just had a thought! I have something that I think is worth a lot. Well, I hope it is, because I paid a lot for it!"
        show sabiaemo normal at left
        m2 "What is it?"
        show sabiaemo closed1 at left
        "Sabia leaned across the table, glanced sideways, and whispered conspiratorially."
        show sabiaemo closed3 at left
        s "We should head to your room. I don't want anyone seeing what I have, since it's meant to be so valuable."
        show sabiaemo normal at left
        "Tomas' eyes widened, and he leaned across the table as well, eyes on her tits. A spark of interest was on Harald's face, as well."
        show sabiaemo normalopen at left
        s "It's tentacle slime."
        show sabiaemo normal at left
        "Before they could say anything, Sabia put a finger to her lips, and made a 'hush' sound."
        "She could see the interest and greed on their faces though, mixed with the desire for Sabia's body that was plain as day."
        m1 "That's a good idea. We'll do that. Let's go, Harald."
        m2 "Fine. I'm behind you."
        m1 "C'mon, Sabrina. I'm interested in seeing this... uh, seeing the thing you have."
        show sabiaemo eyebrow1 at left
        "Sabia nodded, smiling."
        "She followed behind both Harald and Tomas as they made their way to their room."
        "The key turned in the lock, and they moved in, Harald closing the door behind them."
        show sabiaemo normal at left
        m2 "Alright, show us this tentacle slime then. Maybe we might be interested in buying it."
        m1 "Yeah. It is extremely val... er, interesting."
        "Tomas cut his words short at a vicious glance from Harald. He had a bad habit of giving out a little bit too much information."
        "That's why Harald was there, to keep that in check. He was the personable one."
        show sabiaemo happy3 at left
        s "Of course!"
        scene bg black with dissolve
        call merchant_bad_end
        scene bg black with dissolve
        call bandit_ultimate_bad_end
        show gameover with dissolve
        pause 3
        $ renpy.full_restart()


label ef3_merchants_quest3:
    if chaos_merchants_quest_resolution == "sex" and ambush_site_jadk == True:
        show sabiaemo normalopen at left
        s "Well, I guess that's all the information I needed out of those two, I suppose."
        show sabiaemo annoyed1 at left
        s "I'll need to have a wash when I get back to Grok og Dar, though."
        show sabiaemo annoyed2 at left
        "With the information about the bandit camp firmly in her mind, Sabia grimaced at the two drunk men passed out on the bed."
        "She stepped back into her leggings, and put her top on, doing her best to quietly leave the inn, and head back to Grok og Dar."
        jump ef3_merchants_quest4
    elif chaos_merchants_quest_resolution == "sex" and ambush_site_jadk == False:
        $ chaos_merchants_quest_letter = True
        "Remembering the letter she saw on the desk before, Sabia walked over, and picked it up."
        show sabiaemo annoyed2 at left
        "She almost sighed in disappointment - it didn't say anything except some cryptic instructions, that would only make sense if you knew how to get there to begin with."
        show sabiaemo normal at left
        "But the last part - that stood out at her."
        "{i}And make sure you don't do anything stupid. There are lots of patrols, and they're good at their job - you won't see them.{/i}"
        "{i}Do what you've been told to do, and leave. They're expecting two merchants with a cart, so you'll be fine if you follow instructions.{/i}"
        show sabiaemo annoyed2 at left
        "For a moment, Sabia wondered why they'd still have a letter like that. She realized they might just not be very bright."
        "If they were, they probably wouldn't have needed a letter like that to begin with. Whatever the reason they'd taken it with them, and left it there was..."
        show sabiaemo question1 at left
        "Well, Sabia was thankful for it."
        show sabiaemo normalopen at left
        s "At least I know once I manage to get to the bandit camp, I'll need to be very careful, if there are hidden patrols everywhere."
        s "Well, I guess that's all the information I needed out of those two, I suppose."
        s "I'll need to have a wash when I get back to Grok og Dar, though."
        show sabiaemo normal at left
        "With the information about the bandit camp firmly in her mind, Sabia grimaced at the two drunk men passed out on the bed."
        "She stepped back into her leggings, and put her top on, doing her best to quietly leave the inn, and head back to Grok og Dar."
        jump ef3_merchants_quest4
    elif chaos_merchants_quest_resolution == "knockout" and ambush_site_jadk == True:
        show sabiaemo normalopen at left
        s "Well... I'm not going to be able to get anything from them with words now."
        show sabiaemo normal at left
        "She spotted some bags on the ground, in the corner of the room, and shrugged her shoulders."
        show sabiaemo normalopen at left
        s "It's worth a shot."
        show sabiaemo normal at left
        "Going over, she grabbed the bags, upended them, and dumped the contents on the ground."
        show sabiaemo closed2 at left
        "Rummaging around in the pile, she almost sighed and gave up hope, before spotting a map."
        show sabiaemo closed4 at left
        s "No."
        s "I can't be this lucky."
        show sabiaemo normalopen at left
        s "Really?"
        show sabiaemo normal at left
        "A map - labeled with 'camp' and a giant X to mark the spot. It couldn't be more convenient, and her estimation of Tomas and Harald dropped further."
        "It was in one of the forests near Grok og Dar, to the south west."
        show sabiaemo happy3 at left
        "Pocketing the map, she nodded to herself and couldn't help smiling at her luck."
        s "I've got what I needed from them. I should be gone by the time they wake."
        show sabiaemo normal at left
        "Deciding to immediately follow her own advice, and the information and location about the bandit camp firmly pocketed, Sabia snuck out from the inn as quietly as she could."
        "She kept off the roads as she headed back to Grok og Dar - just in case the merchants tried to track her down."
        jump ef3_merchants_quest4
    else:
        $ chaos_merchants_quest_letter = True
        "Remembering the letter she saw on the desk before, Sabia walked over, and picked it up."
        show sabiaemo annoyed2 at left
        "She almost sighed in disappointment - it didn't say anything except some cryptic instructions, that would only make sense if you knew how to get there to begin with."
        show sabiaemo normal at left
        "But the last part - that stood out at her."
        "{i}And make sure you don't do anything stupid. There are lots of patrols, and they're good at their job - you won't see them.{/i}"
        "{i}Do what you've been told to do, and leave. They're expecting two merchants with a cart, so you'll be fine if you follow instructions.{/i}"
        show sabiaemo annoyed2 at left
        "For a moment, Sabia wondered why they'd still have a letter like that. She realized they might just not be very bright."
        "If they were, they probably wouldn't have needed a letter like that to begin with. Whatever the reason they'd taken it with them, and left it there was..."
        show sabiaemo question1 at left
        "Well, Sabia was thankful for it."
        show sabiaemo normalopen at left
        s "At least I know once I manage to get to the bandit camp, I'll need to be very careful, if there are hidden patrols everywhere."
        show sabiaemo irritated2 at left
        "But she still needed more information."
        show sabiaemo normal at left
        "She spotted some bags on the ground, in the corner of the room, and shrugged her shoulders."
        show sabiaemo normalopen at left
        s "It's worth a shot."
        show sabiaemo normal at left
        "Going over, she grabbed the bags, upended them, and dumped the contents on the ground."
        show sabiaemo closed2 at left
        "Rummaging around in the pile, she almost sighed and gave up hope, before spotting a map."
        show sabiaemo closed4 at left
        s "No."
        s "I can't be this lucky."
        show sabiaemo normalopen at left
        s "Really?"
        show sabiaemo normal at left
        "A map - labeled with 'camp' and a giant X to mark the spot. It couldn't be more convenient, and her estimation of Tomas and Harald dropped further."
        "It was in one of the forests near Grok og Dar, to the south west."
        show sabiaemo happy3 at left
        "Pocketing the map, she nodded to herself and couldn't help smiling at her luck."
        s "I've got what I needed from them. I should be gone by the time they wake."
        show sabiaemo normal at left
        "Deciding to immediately follow her own advice, and the information and location about the bandit camp firmly pocketed, Sabia snuck out from the inn as quietly as she could."
        "She kept off the roads as she headed back to Grok og Dar - just in case the merchants tried to track her down."
        jump ef3_merchants_quest4


label ef3_merchants_quest4:
    $ phase3_ylvagone = False
    scene bg black with dissolve
    scene bg centralcamp
    call sabiabase
    with dissolve
    "Upon returning to the camp, Sabia spotted Ylva sitting off to the side, the shaman's staff resting against a tent."
    "The poor shaman looked haggard and tired, but still caught Sabia's glance, and beckoned her over."
    show ylva normal at right
    show ylva2 arm2 at right
    with dissolve
    ylva "Hello Sabia."
    show ylva sad at right
    show sabiaemo sad3 at left
    s "I don't mean to offend, but you look absolutely terrible Ylva."
    show ylva opensad at right
    show sabiaemo irritated2 at left
    ylva "I can imagine. I've barely had any sleep, and it feels as if everything has been made harder by Ornshakar..."
    ylva "I'm... disappointed in him."
    show sabiaemo normalopen at left
    show ylva sad at right
    s "What have you had to do? And why would he make it harder for you? I mean, I haven't been doing anything for him to try to fuck with, have I?"
    show sabiaemo annoyed1 at left
    s "That's usually what he seems to like doing."
    show sabiaemo normal at left
    show ylva normalnarrow at right
    ylva "Sorry, Sabia, but I'm not in the mood for your jokes and jabs."
    ylva "I've spent all my waking time making sure Grok og Dar doesn't erupt into a civil war amongst the captains."
    show sabiaemo irritated2 at left
    ylva "If that happens, you can be sure that some of the lesser tribes would be involved."
    show sabiaemo pout1 at left
    show ylva sad at right
    s "I... hmm."
    show sabiaemo normalopen at left
    s "Aren't there rituals, trials and elections to be for a new Warchief?"
    show ylva opensad at right
    ylva "How can you win if you're dead?"
    show ylva sad at right
    show sabiaemo pout1 at left
    s "Oh."
    show ylva opennormal at right
    ylva "From what I've learned about human courts and politics, that's a fairly common thing, isn't it?"
    show ylva closedsad at right
    show sabiaemo normalopen at left
    s "It is. It just... it never struck me that orcs might do the same."
    show sabiaemo normal at left
    show ylva opennormal at right
    ylva "I think you'll find it wherever there's power to be had."
    show sabiaemo normalopen at left
    show ylva closedsad at right
    s "So what's happening with that, then? The camp's not gone to war."
    show sabiaemo normal at left
    show ylva opennormal at right
    ylva "No. I managed to keep them off each other's throats. Though..."
    show ylva sad at right
    ylva "I'm disappointed in Ornshakar. His goal should be the tribe's wellbeing, its welfare, and yet..."
    show ylva closedsad at right
    show sabiaemo irritated2 at left
    s "Yet?"
    show ylva sad at right
    ylva "No, I'm sorry, but I'd rather not go into that with you, Sabia."
    ylva "All I'll say is that if I weren't here, I suspect he might have done something very un-shamanistic."
    show ylva closedsad at right
    show sabiaemo happy3 at left
    s "Well, I'm glad you're here then, Ylva!"
    show ylva happy1 at right
    ylva "Thanks, Sabia."
    show sabiaemo sad1 at left
    show ylva opennormal at right
    ylva "It's still delicate. Tekrok and Rokgrid are at each other's throats. Dajrab has been mostly silent, but I think if it came to it, he would fight."
    show ylva closednormal at right
    show sabiaemo sad3 at left
    s "Well, I hope that doesn't happen."
    show sabiaemo normal at left
    show ylva opennormal at right
    ylva "It won't, if I can help it."
    show ylva sad at right
    ylva "Sabia, I wish I could talk more. It's been a nice bit of respite, but I just don't have the time at the moment."
    show ylva closedsad at right
    show sabiaemo normalopen at left
    s "I understand, Ylva."
    hide ylva
    hide ylva2
    with moveoutright
    show sabiaemo closed2 at left
    "After Ylva left, back to the main hall, Sabia pondered her choices."
    "She could either head straight to the camps with the new information she had, or wait for Neve."
    show sabiaemo normalopen at left
    s "Neve usually has pretty good timing... she shouldn't be longer than a day now."
    s "I'll have to decide before I rest."
    jump lowerorccamp


label phase3_bandit_camp_neve:
    $ chaos_bandit_quest_done = True
    scene bg forest
    call sabiabase
    show neve1 at right
    show neveemo normal at right
    with dissolve
    "Though Sabia felt that they might not find Warchief Groknak at the bandit camp, she still felt good about doing something."
    "She hoped that, at the least, they could find some information that would point them in the right direction."
    "Deep in thought, she realized she hadn't heard Neve talking to her, and she shook her head to clear her thoughts."
    show sabiaemo normalopen at left
    show neveemo irritated1 at right
    s "Sorry, Neve. What did you say?"
    show sabiaemo normal at left
    show neveemo normal at right
    n "We need to be very, very careful."
    n "My contact isn't one to give warnings lightly, and from everything I've seen so far, I think I trust their judgment."
    show sabiaemo normalopen at left
    s "Of course. I wouldn't be anything else."
    show sabiaemo normal at left
    "Sabia pulled out her map and her eyes flickered over it for a few moments."
    show sabiaemo normalopen at left
    show neveemo irritated1 at right
    s "We're here. Their camp is in here, somewhere. I'm not sure where, but I think we'll find it if we are careful."
    show sabiaemo normal at left
    show neveemo normal at right
    n "Let's go, then."
    n "Quietly."
    scene bg forest with dissolve
    "Sabia nodded to Neve, and they entered the thicker part of the forest."
    "The directions that Sabia had managed to source led them to the general area, but unfortunately the specifics weren't quite there."
    "With that knowledge unavailable, Sabia felt a little exposed as they made their way through the forest."
    "They could be only feet away from their main hideout, and they wouldn't know until they crested a hill or passed a thick grove of trees."
    "Neve, next to her, was as silent as a shadow. The Elf moved with a grace that, up until now, Sabia had never really appreciated."
    "Stealth had never been a quality she had needed to employ with Neve before. But, even for an Elf, it hit Sabia that Neve was exceptionally quiet."
    "By comparison, she felt like she might as well have been screaming 'Look out, bandits, here I come!' at the top of her lungs."
    call sabiabase
    show neve1 at right
    show neveemo normal at right
    with dissolve
    n "Shh, stop."
    "Neve's voice came out, barely a whisper as her hand pressed against Sabia's chest, shoving her against a tree."
    "Inclining her head, Neve indicated the bandits passing, about a hundred yards out."
    show sabiaemo surprised1 at left
    "Sabia inhaled, shocked at how she had missed it, only for Neve to nod her head in a different direction."
    "More bandits, dressed to conceal themselves in the forest. These ones less than half the distance of the first group."
    show neveemo closed1 at right
    n "Patrols. Getting closer."
    show neveemo normal at right
    "They disappeared after a few minutes, and Sabia managed to exhale, sweat on her forehead."
    show sabiaemo sad3 at left
    s "I wouldn't have seen them if I were here by myself. I would have missed them entirely. I barely noticed them after you pointed them out."
    show neveemo happy2 at right
    n "Well, it's a good thing you waited for me then, isn't it?"
    show sabiaemo happy2 at left
    s "I'd say that again."
    show sabiaemo normal at left
    show neveemo happy1 at right
    n "Come, let's keep going."
    "Sabia nodded to Neve, and the two kept moving."
    "Now that Sabia was aware of the patrols, she tried to match Neve's stealth. It was an exercise in futility, though."
    "There was no way she could ever be as silent and graceful as Neve was, but she tried her best."
    "Every few hundred yards, a patrol would pass near. They were getting closer each time."
    "Another hour or two passed - it was hard to tell, the forest canopy here was too dense to get a good view of the sun overhead, and they found the camp."
    "They crouched down in the underbrush, looking in. The camp was much larger than either of them had expected, bustling with people."
    "There were several campfires, a row of large tents - at least ten that they could see, each large enough for several people."
    "Sabia even spotted some cooking stations."
    show sabiaemo closed2 at left
    show neveemo irritated2 at right
    n "Well, we're certainly not going in there, blades drawn."
    show sabiaemo normal at left
    s "No. Definitely not. I'm not really sure what we're going to do here."
    show neveemo normal at right
    "Neve frowned, glancing this way and that."
    show sabiaemo question1 at left
    show neveemo smirk1 at right
    n "Here, this way."
    show neveemo normal at right
    scene bg forest with dissolve
    "The two moved down a little, around the camp's outskirts until they were closer to a small cave."
    scene bg cave
    call sabiabase
    show neve1 at right
    show neveemo normal at right
    with dissolve
    n "I'd hazard a guess that that's going to be where we need to go."
    show sabiaemo normalopen at left
    s "Why's that?"
    show sabiaemo closed2 at left
    show neveemo closed3 at right
    n "It's guarded."
    show neveemo normal at right
    show sabiaemo normalopen at left
    s "Right. Makes sense, then."
    show sabiaemo normal at left
    show neveemo sad at right
    n "Do you think we'll even get anything in there? Worth the risk?"
    n "I'm good. But I'm not sure I'm capable of beating an entire bandit camp."
    show sabiaemo normalopen at left
    show neveemo closed1 at right
    s "I think so. It's our only lead, and with so many connections pointing to these bandits, I don't think we have a choice."
    show sabiaemo normal at left
    show neveemo normal at right
    n "You might be right Sabia."
    show sabiaemo normalopen at left
    s "But how are we going to get in?"
    show sabiaemo normal at left
    show neveemo smirk1 at right
    n "Don't worry. I got this. Get in, find anything you can, and get out. I'll find you later. Or come find me - either way."
    show sabiaemo irritated2 at left
    hide neve1
    hide neveemo
    with moveoutright
    "Before Sabia had a chance to protest, Neve was walking out toward the cave. Blatantly."
    "Sabia felt blood pumping through her body as the two guards gripped their weapons tighter, glaring at Neve."
    scene bg cave with dissolve
    show neve1 at center
    show neveemo normal at center
    with dissolve
    guard1 "Oi, what do you want, elf slut?"
    s "(...I don't think that was the right thing to... to say...)"
    show neveemo happy1
    n "It's not nice to go around calling people sluts when you don't know them."
    show neveemo smirk1
    guard1 "I... uh... well."
    guard2 "We gotta guard this for the 'cap, is all. And we haven't seen you around."
    "The second guard nudged his spear to the cave-mouth."
    show neveemo normal
    "Neve pointedly looked the two up and down, making sure they knew she was judging them."
    show neveemo smirk1
    n "I'm not sure you two would be able to guard anything, if someone half skilled came through..."
    n "Why don't you come show me what you've got?"
    show neveemo normal
    guard2 "Two against one ain't fair. Just leave before we have to do something we all regret."
    "Despite his strong words, his eyes were lingering on Neve's bust, and he seemed quite unable to pull them away."
    show neveemo closed2
    n "Two against one can be fun sometimes. It's a real workout. Why don't we have a little training - a little competition maybe?"
    show neveemo normal
    guard1 "...uh..."
    show neveemo smirk1
    "Neve placed a hand each on one of her blades, doing so making her arms press up against her tits and making them push up and out."
    show neveemo closed2
    n "If you're not even comfortable against a lone elf, are you sure you should even be guarding anything? But alright, then."
    show neveemo normal
    "Neve turned, and started to walk away slowly. One step fell in front of the other, making her ass sway more than normal."
    "Barely three seconds passed before they called out after her."
    show neveemo smirk1
    guard1 "W- wait! Wait! We can, uh, probably spend some time with you."
    guard2 "Yeah, yeah. No one's gonna come around and fuck with the cap's stuff. We good, c'mon, we'll show you how skilled we are!"
    show neveemo happy3
    n "This way?"
    hide neve1
    hide neveemo
    with moveoutright
    "Sabia watched the three of them leave, wondering if the two guards were going to get to fuck Neve, or end up dead."
    call sabiabase
    with dissolve
    "She really had no idea which. As they rounded the corner and disappeared though, Sabia darted across the now-empty space, into the cave."
    "It took a few moments for her eyes to adjust to the darkness, but as it did she looked around."
    "Definitely quarters for someone important. A big living space, a desk that looked out of place in a bandit's hideout."
    show sabiaemo question1 at left
    s "Aha, a desk. Let's have a look over there..."
    "Sabia rummaged through the desk, through the papers dumped messily on top, and then through the drawers."
    s "What's this?"
    show sabiaemo normal at left
    "The last drawer had several loose pieces of small paper. Rough and torn edges."
    "Sabia was only able to make out a few words on the pieces as she glanced through them."
    "Shoving her hand into the drawer, Sabia pooled all the pieces together and grabbed them."
    show sabiaemo closed3 at left
    s "Fuck."
    s "If I take this... they're going to know someone was here. Any information I get could be pointless - they might make sure the information here becomes outdated."
    show sabiaemo normalopen at left
    s "I'm going to have to try and put them back together quickly - hopefully Neve can give me enough time."
    scene bg cave with dissolve
    $ puzzle_image = "database/puzzles/letter.png"
    $ puzzle_timer = 600
    call puzzle_game
    if _return == True:
        call sabiabase
        with dissolve
        show sabiaemo closed2 at left
        s "Huh. So this whole operation they have going on is MUCH bigger than I first thought... and much more organized."
        show sabiaemo normalopen at left
        s "I'm not really familiar with any of these names though. They must be what they've named their outposts and camps."
        s "Though, given that I know there's a minotaur at this camp... this might be Riftstone."
        s "Receiving payment, and them being here and Groknak being ambushed and captured doesn't seem to be a coincidence... but it's not conclusive, unfortunately."
        s "Though getting paid by Lundar seems to suggest that the bandits are being funded... seems Neve was right about them being far more organized than any other bandits before."
        show sabiaemo sad3 at left
        s "But unfortunately, none of this helps finding Groknak, and it's all fairly loose without any other information."
        show sabiaemo closed2 at left
        s "At any rate, I had best leave before the guards come back... I'll go and see where Neve got to and wait until she's... uh, finished."
        scene bg black with dissolve
        pause(1)
        scene bg forest
        call sabiabase
        with dissolve
        "With the information in hand, Sabia left the area, looking for Neve."
        "It took her a few minutes to track Neve down, and she caught a glance of the dark-skinned elf with the two bandits, rutting furiously on the forest floor."
        "Sabia pursed her lips."
        menu:
            "Watch from a distance.":
                call neve_bandits_live
                "Neve wandered over quietly after a few minutes, her 'distracting' clearly finished."
            "Don't watch and wait for Neve to finish.":
                show sabiaemo closed2 at left
                "Deciding that she didn't want to intrude quite so much, Sabia moved a few feet back, away from Neve."
                "She wasn't sure how long they were going to be, but at least it was better than killing them, she reasoned."
                show sabiaemo normal at left
                "She very much doubted whether grunts like that would willingly offer the information that they'd abandoned their post to their commander or captain."
                "Which was good for them, because keeping as low a profile was ideal. The most preferable scenario is one where no one except those two knew they'd been there, and they kept their mouths shut."
                "Sabia leaned against a tree, waiting for Neve to finish."
                "It was only another ten minutes or so before Neve wandered over quietly, her 'distracting' clearly finished."
        play music forest fadeout 2.0 fadein 2.0
        scene bg forest
        call sabiabase
        show sabiaemo normalopen
        with dissolve
        show neve1 at right
        show neveemo normal at right
        with moveinright
        s "Enjoy yourself?"
        show sabiaemo normal at left
        show neveemo happy3
        n "It was fun, yes."
        n "Enough about me though. What did you find, anything interesting?"
        show sabiaemo normalopen at left
        s "Yes. I found a very interesting document that affirms your information about the bandits' size and organization."
        s "And a link to them being funded, in some way, by Lundar or someone from Lundar. But unfortunately there are no names, and no other information - and nothing about Groknak."
        s "But what they call Riftstone is receiving a payment this month, and I think this camp is Riftstone, judging by the presence of the minotaur and what the letter said."
        show sabiaemo irritated2 at left
        show neveemo closed4 at right
        n "Well, fuck. It doesn't really seem like that's much to go on though - I mean, it sort of makes a link."
        show neveemo irritated1 at right
        show neveemo normal at right
        n "But it's sort of a dead end, it doesn't give us anything else to go on, Sabia. It seems like their tracks have been covered reasonably well."
        show sabiaemo sad3 at left
        s "Yeah... it's unfortunate."
        show neveemo happy2 at right
        n "I suppose you're lucky I came, then, aren't you?"
        show sabiaemo normalopen at left
        s "What do you mean?"
        show sabiaemo normal at left
        show neveemo happy3 at right
        n "Well, I found out that the bandits have a higher up leader by the name of Kira. If I believe what I'm told, she's quite attractive..."
        n "At any rate, she's meant to be participating in a meeting above the abandoned Lundarian gold mine in on the third moon from now."
        show neveemo happy1 at right
        show sabiaemo happy1 at left
        s "And you didn't say that earlier?"
        "Neve shrugged, smirking."
        s "Well, that's good then. With what I got, and what we might learn there, we might be on to something. Three moons is still a while away though, so in the meantime we shouldn't be too idle."
        show sabiaemo normal at left
        n "Agreed. Let's head back to Grok og Dar for now."
        scene bg black with dissolve
        pause (1)
        jump phase3_bandit_camp_return
    else:
        call sabiabase
        with dissolve
        show sabiaemo closed2 at left
        s "Huh. So this whole operation they have going on is MUCH bigger than I first thought... and much more organized."
        show sabiaemo normalopen at left
        s "I'm not really familiar with any of these names though. They must be what they've named their outposts and camps."
        s "Though, given that I know there's a minotaur at this camp... this might be Riftstone."
        s "Receiving payment, and them being here and Groknak being ambushed and captured doesn't seem to be a coincidence... but it's not conclusive, unfortunately."
        s "Though getting paid by Lundar seems to suggest that the bandits are being funded... seems Neve was right about them being far more organized than any other bandits before."
        show sabiaemo sad3 at left
        s "But unfortunately, none of this helps finding Groknak, and it's all fairly loose without any other information."
        show sabiaemo closed2 at left
        s "At any rate, I had best leave before the guards come back... I'll go and see where Neve got to and wait until she's.... uh, finished."
        scene bg black with dissolve
        pause (1)
        scene bg forest
        call sabiabase
        with dissolve
        "With the information in hand, Sabia left the area, looking for Neve."
        "The underbrush rustled heavily as she moved through the forest, and she cast a glance about."
        show sabiaemo irritated1 at left
        "But there wasn't anyone there - at least, none that Sabia could see, so she kept moving on."
        show sabiaemo annoyed2 at left
        "It took her a few minutes to track Neve down, and she caught a glance of the dark-skinned elf with the two bandits, rutting furiously on the forest floor."
        show sabiaemo normal at left
        "Sabia pursed her lips."
        $ GenericOrc1.face = "smile2"
        $ GenericOrc2.face = "smile2"
        $ GenericOrc1.extras = ["Loincloth", "Stick", "Wrap"]
        $ GenericOrc2.extras = ["Loincloth", "Beard1", "Necklace"]
        menu:
            "Watch from a distance.":
                call neve_bandits_kill
                play music forest fadeout 2.0 fadein 2.0
                scene bg forest
                show Sabia at left
                $ Sabia.face = "surprised3"
                with dissolve
                "Distracted from watching Neve, and getting a little bothered herself, Sabia didn't hear the two orcs closing in on her."
                show GenericOrc1 behind Sabia at center
                show GenericOrc2 behind Sabia at right
                with moveinright
                "By the time she saw the first charging toward her, the second orc's axe hilt was already whistling toward the back of her head."
                show GenericOrc1:
                    linear 0.3 xoffset -200
                pause(0.2)
                call shake ("h")
                "A surge of pain erupted for an instant before the world went dark."
                scene bg black with dissolve
                call orc_bandits
                play music forest fadeout 2.0 fadein 2.0
            "Don't watch and wait for Neve to finish.":
                scene bg forest
                show Sabia at left
                $ Sabia.face = "closed2"
                "Deciding that she didn't want to intrude quite so much, Sabia moved a few feet back, away from Neve."
                "She wasn't sure how long they were going to be, but at least it was better than killing them, she reasoned."
                $ Sabia.face = "normal"
                "She very much doubted whether grunts like that would willingly offer the information that they'd abandoned their post to their commander or captain."
                "Which was good for them, because-"
                $ Sabia.face = "surprised3"
                show GenericOrc2 at right with moveinright
                "Her blade sung as she pulled it out of the scabbard, an orc charging toward her from behind several large palm fronds."
                show GenericOrc1 behind Sabia at left:
                    xzoom -1
                    xoffset -200
                with moveinleft
                call shake ("h")
                "But it was a bit too slow, she hadn't heard the second orc behind her, and the pommel of his own blade struck her head heavily."
                "A surge of pain erupted for an instant before the world went dark."
                scene bg black with dissolve
                call orc_bandits
                play music forest fadeout 2.0 fadein 2.0
        scene bg black with dissolve
        pause (1)
        $ GenericOrc1.face = "smile2"
        $ GenericOrc2.face = "smile2"
        $ GenericOrc1.extras = ["Loincloth", "Stick", "Wrap"]
        scene bg cave
        show basenaked at left
        show sabiaemo closed2 at left
        show sabiaemo2 blush at left
        show GenericOrc1 at center
        with dissolve
        s "Fucking... get off me!"
        show basenaked:
            xoffset -50
        show sabiaemo:
            xoffset -50
        show sabiaemo2:
            xoffset -50
        with move
        "Grunting, Sabia managed to crawl a few inches away, her pussy throbbing and oozing with cum, and the taste of the stuff strong in her mouth."
        show neve1 behind GenericOrc1 at right
        show neveemo normal behind GenericOrc1 at right
        with dissolve
        n "Having some fun?"
        show sabiaemo angry1 at left
        show neveemo smirk1 at right
        s "I thought... you... about time!"
        $ GenericOrc1.face = "angry"
        orc "YOU KILL HIM! WHY YOU KILL FRIEND?!"
        show neveemo irritated1 at right
        n "Oh, be quiet."
        "Sabia knew it was coming this time, but her eyes still barely managed to track Neve's movement as the blade finished the second bandit."
        show expression "database/actors/neve/neve1.png" as nevebody at right:
            alpha 0.3
        show expression "database/actors/neve/expressions/normal.png" as neveface at right:
            alpha 0.4
        show neve1 at right:
            alpha 0.3
        show neveemo normal at right:
            alpha 0.4
        pause(0.01)
        show neve1 behind GenericOrc1 at center
        show neveemo behind GenericOrc1 at center
        with move
        $ renpy.show("GenericOrc1mask", at_list=[center], what=AlphaBlend(Transform("GenericOrc1", alpha=0.9), "GenericOrc1", bloodhit_effect, alpha=True))
        pause(0.01)
        hide GenericOrc1
        hide GenericOrc1mask
        hide nevebody
        hide neveface
        show neve1 at center:
            linear 0.5 alpha 1.0
        show neveemo at center:
            linear 0.5 alpha 1.0
        with Dissolve(1)
        "Neve helped Sabia back to her feet, and threw her the clothes she had lost a few yards away in the grass. Sabia cleaned herself off as best she could, and put her clothes back on."
        scene bg black with dissolve
        pause (1)
        scene bg cave
        call sabiabase
        show neve1 at right
        show neveemo normal at right
        with dissolve
        n "Just lucky that it was only two guards. I'm good, but if half the camp had been having a turn with you, you might've been stuck there."
        show sabiaemo pout3 at left
        s "I don't think I really want to talk about it."
        show neveemo happy3 at right
        n "Fair enough. What did you find, anything interesting?"
        show sabiaemo normalopen at left
        s "Yes. I found a very interesting document that affirms your information about the bandits' size and organization."
        s "And a link to them being funded, in some way, by Lundar or someone from Lundar. But unfortunately there are no names, and no other information - and nothing about Groknak."
        s "But what they call Riftstone is receiving a payment this month, and I think this camp is Riftstone, judging by the presence of the minotaur and what the letter said."
        show sabiaemo irritated2 at left
        show neveemo closed4 at right
        n "Well, fuck. It doesn't really seem like that's much to go on though - I mean, it sort of makes a link."
        show neveemo irritated1 at right
        n "But it's sort of a dead end, it doesn't give us anything else to go on, Sabia. It seems like their tracks have been covered reasonably well."
        show sabiaemo sad3 at left
        s "Yeah... it's unfortunate."
        show neveemo happy2 at right
        n "I suppose you're lucky I came, then, aren't you?"
        show sabiaemo normalopen at left
        s "What do you mean?"
        show sabiaemo normal at left
        show neveemo happy3 at right
        n "Well, I found out that the bandits have a higher up leader by the name of Kira. If I believe what I'm told, she's quite attractive..."
        n "At any rate, she's meant to be participating in a meeting above the abandoned Lundarian gold mine on the third moon from now."
        show neveemo happy1 at right
        show sabiaemo happy1 at left
        s "And you didn't say that earlier?"
        "Neve shrugged, smirking."
        s "Well, that's good then. With what I got, and what we might learn there, we might be on to something. Three moons is still a while away though, so in the meantime we shouldn't be too idle."
        show sabiaemo normal at left
        n "Agreed. Let's head back to Grok og Dar for now."
        scene bg black with dissolve
        pause (1)
        jump phase3_bandit_camp_return


label phase3_bandit_camp_solo:
    scene bg countryside
    call sabiabase
    with dissolve
    "Sabia pulled out the map, and her eyes flickered over it for a few moments, before nodding to herself."
    s "Maybe it would be a better idea to wait for Neve."
    menu:
        "Go now":
            pass
        "Wait for Neve":
            jump eastern_frontier_map
    "Though she wasn't sure whether she would find Groknak or not, she decided that going now was the right choice."
    "She hoped that, at the least, she could find some information that would point her in the right direction."
    show sabiaemo closed4 at left
    s "I need to be pretty careful. I don't have Neve to back me up right now."
    show sabiaemo normalopen at left
    s "But... I think this is the correct thing to do. If Groknak is there, time is important."
    s "It looks like it will take me about an hour to get to the part of the forest that the camp is supposedly in."
    show sabiaemo closed4 at left
    s "I don't have much time to waste."
    scene bg black with dissolve
    pause(1)
    scene bg cave
    show Sabia at left
    with dissolve
    $ Sabia.face = "happy1"
    s "Hmm. I've made good time, I think I might have shaved ten minutes off."
    $ Sabia.face = "normal"
    "Another brief study of the map, and Sabia made her way into the thicket of trees."
    "It didn't take long, and Sabia found herself in the thicker part of the forest."
    $ Sabia.face = "irritated2"
    "She couldn't see the edge of the trees anymore, and the only light came from through the canopy."
    "The pommel of her sword felt comforting as she walked as quietly through the undergrowth as she could manage."
    "Unfortunately, the information and the map she had acquired were a bit sparse on the specifics of exactly where in the forest the camp was."
    "But she was sure if she kept an eye out, she would find it. She only needed to catch signs of a path or trail."
    $ Sabia.face = "irritated1"
    "Still, without that knowledge, Sabia felt a little exposed as she made her way forward."
    if chaos_merchants_quest_letter == False:
        show humansoldier angry behind Sabia at center
        with moveinright
        $ Sabia.face = "surprised2"
        s "What-!"
        $ Sabia.face = "surprised3"
        s "(A patrol!)"
        show humansoldier angry:
            linear 0.2 xoffset -100
        pause (0.1)
        call shake ("h")
        "Caught off guard, Sabia wrapped her fingers about her sword, and began to pull it from its scabbard."
        "But she was just a fraction of a moment too slow."
        "Something hard, big and heavy hit her in the head, and the world went black."
        scene bg black with dissolve
        call human_bandits
        scene bg black with dissolve
        call bandit_ultimate_bad_end
        show gameover with dissolve
        pause 3
        $ renpy.full_restart()
    else:
        "At least she knew to keep an eye out for patrols, after reading the letter the merchants left. Neither Tomas nor Harald had thought to offer that tidbit to her."
        show sabiaemo surprised1 at left
        "Just as the thought crossed her mind, she managed to spot a patrol nearby - she would have missed it entirely if she hadn't been so on edge, and armed with the knowledge."
        show sabiaemo normal at left
        "Sabia cut her breath short, and her whole body dropped down, crouching against the tree."
        "It was wide and old enough to block her from the patrol in the distance."
        "They passed shortly after."
        show sabiaemo normalopen at left
        s "Getting closer."
        s "I better make sure I keep an even better eye out for patrols."
        show sabiaemo closed2 at left
        s "A second later and they probably would have spotted me..."
        show sabiaemo normal at left
        "As she inched closer toward the bandits' camp, she spotted a few more patrols, dressed to hide amongst the forest."
        "A few moments spent here, a minute spent there, and she slowly, painfully - but safely - made her way past the patrols."
        "It took another minute or two before Sabia found the camp - it was hard to tell how long, the canopy was too dense to get a good view of the sun."
        "She crouched down in the underbrush, looking in. The camp was much larger than she had expected, and bustling with people."
        "There were several campfires, a row of large tents - at least ten that she could see, each large enough for multiple people."
        "Sabia even spotted some cooking stations."
        show sabiaemo normalopen at left
        s "Well, there's no chance I'm managing to get in there."
        show sabiaemo irritated2 at left
        "Sighing, Sabia let the breath run from her mouth."
        show sabiaemo normalopen at left
        s "Hmm, what now?"
        show sabiaemo normal at left
        "Out of the corner of her eye, she saw a large blotch of dark muddy brown, and grayish stone."
        "She moved down a little, around the camp's outskirts until she was closer to the small cave."
        show sabiaemo normalopen at left
        s "Well, it's guarded. I don't really see anything else guarded."
        s "And I'm more capable of dealing with two than twenty. This might be my only shot."
        show sabiaemo irritated2 at left
        s "But... do I just distract them, or kill them?"
        show sabiaemo normalopen at left
        s "Killing them might draw some attention and make my escape harder. But distracting them might make it more difficult to find something in time."
        menu:
            "Distract the guards.":
                s "I guess distracting them might be safer."
                s "And it will leave less evidence of someone being here."
                show sabiaemo normal at left
                "Foraging for a few rocks seemed harder than Sabia would have thought."
                "But, really, how many rocks were on the forest floor?"
                show sabiaemo angry1 at left
                s "Apparently not fucking many..."
                show sabiaemo irritated2 at left
                "After a few minutes, she found enough, and moved back to her spot."
                "Though the bandits were reasonably armed and organized, she hoped that their common sense would be a little lacking."
                show sabiaemo normal at left
                "She threw a few rocks, and the sound startled both guards."
                guard1 "What's that?"
                guard2 "I dunno, I'm here like you, ain't I? Just some birds, isn't?"
                guard1 "Birds don't make sound like that, they're all high like 'cheep-cheep'!"
                "Sabia hurled another couple of stones."
                guard1 "Look, there it is again! I'm gonna go check it out."
                guard2 "I better come with you. You ain't so good at fighting. Not like me."
                guard1 "I don't need any help fighting birds."
                guard2 "It ain't a bird!"
                show sabiaemo annoyed2 at left
                "Sabia rolled her eyes as the conversation thankfully faded."
                show sabiaemo normal at left
                "Before anyone else could see, she darted into the cave."
                "It took a few moments for her eyes to adjust to the darkness, but as it did she looked around."
                "Definitely quarters for someone important. A big living space, a desk that looked out of place in a bandit's hideout."
                show sabiaemo question1 at left
                s "Aha, a desk. Let's have a look over there, and quickly. I don't have much time."
                "Sabia rummaged through the desk hastily, through the papers dumped messily on top, and then through the drawers."
                show sabiaemo normalopen at left
                s "What's this?"
                show sabiaemo irritated2 at left
                "The last draw had several loose pieces of small paper. Rough and torn edges."
                "Sabia was only able to make out a few words on the pieces as she glanced through them."
                show sabiaemo normalopen at left
                s "A bunch of different names - none of them I recognize. They must be using their own names for their camps..."
                s "But I see Lundar there... and payment."
                s "They must be-"
                show sabiaemo normal at left
                "Sabia's ears twitched, and she heard the rustling of steps coming back."
                show sabiaemo surprised2 at left
                s "Fuck. Fuck!"
                s "Even just one scream or yell and I'll have the whole camp on me!"
                show sabiaemo surprised1 at left
                "She grabbed as much of the paper as she could in a scrunched hand."
                "They were already coming back."
                call shake ("h")
                "Sabia needed to get out. She made for the mouth of the small cave, and just as she passed through, something heavy hit her on the head."
                "In the instant before she passed out, she realized she must have fallen for the same trick that the guards had fallen for minutes earlier."
                scene bg black with dissolve
                call human_bandits
                scene bg black with dissolve
                call bandit_ultimate_bad_end
                show gameover with dissolve
                pause 3
                $ renpy.full_restart()
            "Kill the guards.":
                show sabiaemo closed4 at left
                s "A more permanent solution does have its merits..."
                show sabiaemo normal at left
                "Fingering the small knife she had next to her sword, Sabia flipped it in the air, judging its weight and balance."
                "Gripping the blade easily with her left hand and her sword with her right, Sabia took aim."
                "The little sliver of metal whistled through the air, and landed in the far guard's throat at the same time as Sabia darted from her hiding spot."
                "The second guard had a moment of distraction, gazing in disbelief at his fellow bandit, before Sabia's sword connected."
                guard1 "U--ggh... I-"
                show sabiaemo irritated1 at left
                s "Shh!"
                "Sabia grunted, covering his mouth with her hand, before finishing the job with her sword."
                show sabiaemo normalopen at left
                s "Need to dump them somewhere..."
                s "I guess just in the brush is fine, I don't want to spend too much time and have other guards come in..."
                show sabiaemo normal at left
                "A few sweaty minutes later, and Sabia snuck back around, heading into the cave."
                "It took a few moments for her eyes to adjust to the darkness, but as it did she looked around."
                "Definitely quarters for someone important. A big living space, a desk that looked out of place in a bandit's hideout."
                show sabiaemo question1 at left
                s "Aha, a desk. Let's have a look over there..."
                "Sabia rummaged through the desk, through the papers dumped messily on top, and then through the drawers."
                show sabiaemo normalopen at left
                s "What's this?"
                show sabiaemo irritated2 at left
                "The last draw had several loose pieces of small paper. Rough and torn edges."
                "Sabia was only able to make out a few words on the pieces as she glanced through them."
                show sabiaemo irritated1 at left
                s "A bunch of different names - none of them I recognize. They must be using their own names for their camps..."
                s "But I see Lundar there... and payment."
                "Sabia spent a few minutes shuffling the papers around, trying to get them into a readable form. But she felt she didn't have much time being by herself with no one to cover her."
                "And it seemed only a few moments later, she heard steps."
                show sabiaemo surprised1 at left
                $ GenericOrc1.extras = ["Loincloth", "Stick"]
                show GenericOrc1 at right
                with moveinright
                $ GenericOrc1.face = "suspicious"
                guard2 "Hey, what you doing in here... wait, you not bandit!"
                guard2 "Get her!"
                show sabiaemo surprised2 at left
                s "Wait, I'm- oh. Oh, fuck! Fuck!"
                s "It's not like, wait-"
                show sabiaemo surprised1 at left
                "Sabia didn't get time to finish her sentence. A hulking frame charged forward."
                "The minotaur closed the distance far faster than his size would suggest."
                "Managing to dart around the minotaur, the torn papers fell from her hand."
                call shake ("h")
                "She tried to grab them with a knee-jerk reaction, and the lapse of concentration was all one of the orcs needed to knock her over the head."
                scene bg black with dissolve
                call mino_badend
                scene bg black with dissolve
                call bandit_ultimate_bad_end
                show gameover with dissolve
                pause 3
                $ renpy.full_restart()


label phase3_bandit_camp_return:
    scene bg black with dissolve
    pause (0.1)
    scene bg orclake
    call sabiabase
    with dissolve
    $ chaos_ylva_lake = 1
    "On the way back to Grok og Dar, Sabia caught the familiar form of Ylva walking toward the lake, staff in hand."
    "There was a hunch to the shaman's shoulders that wasn't usually there."
    show sabiaemo normalopen at left
    s "I should go talk to Ylva, I think."
    s "I haven't managed to have a proper conversation with her since Groknak went missing."
    scene bg black with dissolve
    pause(1)
    jump lowerorccamp


label ef3_kira_camp:
    play music forest fadeout 2.0 fadein 2.0
    scene bg cave with dissolve
    if avion_quest_bandit_freed == True and sub>dom and avion_quest_aftersex_talk == False:
        $ avion_quest_aftersex_talk = True
        $ Sabia.face = "normal"
        show Sabia at left with dissolve
        "Sabia felt uncomfortable heading back to Kira's camp after what had happened earlier."
        "Being used as a prop in a minotaur's deviant ritual, fucked until you pass out... well."
        "It was not exactly high on her bucket list, and she had no idea how Avion was going to treat her."
        "But Avion did no more than glance at her. He saw her. He looked away."
        "Sabia was taken aback."
        "No attempt at domineering her some more, no attempt at feeling her up or groping."
        "An almost apathetic attitude towards her."
        show Neve at right with moveinright
        $ Sabia.face = "pout2"
        $ Neve.face = "happy3"
        n "Got a taste for something a bit bigger than an orc or human?"
        s "..."
        $ Sabia.face = "normalopen"
        s "No..."
        $ Neve.face = "smirk1"
        s "I was just... I mean, I was worried it would have spread around camp, or perhaps Avion would try something."
        s "It seems like only you know, though."
        $ Sabia.face = "normal"
        $ Neve.face = "happy1"
        "Neve shook her head."
        n "Kira told me. Maybe if he felt you were worthy of doing so, he might have."
        $ Sabia.face = "pout2"
        $ Neve.face = "irritated1"
        n "But from what I understand, he was compelled by his invocation of his Gods."
        $ Sabia.face = "normalopen"
        s "And without a heart or a spirit..."
        $ Sabia.face = "pout2"
        $ Neve.face = "happy1"
        n "Exactly. You were just a thing for him to use in his rites."
        $ Sabia.face = "pout3"
        $ Neve.face = "happy3"
        n "Or maybe he likes you just a little bit more. Who knows?"
        $ Sabia.face = "irritated2"
        "Neve couldn't help but grin."
        $ Neve.face = "smirk1"
        n "But maybe you'll find out at some point, but I doubt you have much to worry about with the camp finding out. A confident warrior like that has little need to boast."
        scene bg cave with dissolve
    menu:
        "Talk to Kira":
            $ Kira.face = "normal"
            $ Sabia.face = "normal"
            show Sabia at left
            show Kira at right
            with dissolve
            if kira_quest == 5 and avion_quest_prompt == False and (reliefttents_trial_done == True or ornshakar_deal == True):
                $ avion_quest_prompt = True
                $ Kira.face = "normal"
                "Kira turned to Sabia."
                $ Kira.face = "irritatedopen"
                $ Sabia.face = "pout1"
                kira "I'm not in the mood to talk."
                $ Kira.face = "angry"
                $ Sabia.face = "normalopen"
                s "Is there anything I can do to help?"
                $ Sabia.face = "sad1"
                "Kira's expression darkened."
                $ Kira.face = "angryopen"
                kira "Listening to me might be a start... but..."
                $ Kira.face = "normalopen"
                $ Sabia.face = "normal"
                kira "Hmm. I suppose... there's something. And it would amuse me... hmm... alright."
                kira "You can help Avion with a... task."
                $ Kira.face = "normal"
                $ Sabia.face = "normalopen"
                s "I don't think Avion likes me all that much..."
                $ Kira.face = "normalopen"
                $ Sabia.face = "normal"
                kira "Of course not."
                $ Sabia.face = "pout1"
                kira "But you two will... do the task, nonetheless."
                $ Kira.face = "normalopen"
                $ Sabia.face = "normal"
                kira "Tell him I've sent you to... help."
                $ Kira.face = "normal"
                $ Sabia.face = "normalopen"
                s "Alright, I will."
            menu ef3_kira_camp_kira:
                "What are your tests?" if kira_quest == 0:
                    $ kira_quest = 1
                    $ Kira.face = "normalopen"
                    kira "There are two of them."
                    kira "A duel... of sorts. Best your opponent, or impress me as I watch, and you will pass. Indulge my dramatic flair though... I like to call it a test of skill."
                    $ Kira.face = "normal"
                    s "What else is there?"
                    $ Kira.face = "normalopen"
                    kira "You'll have to help carry out a raid."
                    s "A raid?!"
                    $ Kira.face = "browsopen"
                    kira "Well, yes. Of course! How else will I know you're capable of doing that, if I don't see it first?"
                    $ Kira.face = "normalopen"
                    kira "A raid requires a certain cunning to orchestrate, or even participate in. So... if you'll indulge me again - this is the test of cunning."
                    kira "So... you can come tell me when you're ready to start. Or... if you prefer, I'm sure I can find another use for you."
                    $ Kira.face = "normal"
                    s "I think I'll try the tests."
                    $ Kira.face = "irritatedopen"
                    kira "A shame... I don't think I'll be sad to see you fail."
                    jump ef3_kira_camp_kira

                "Ask about prevalence of orcs." if kira_orc_talk == False and kira_quest > 0:
                    $ kira_orc_talk = True
                    $ Kira.face = "irritatedopen"
                    kira "Yes... of course."
                    kira "It's difficult to not have a lot of orc warriors when you are in what is effectively orc land..."
                    $ Kira.face = "normal"
                    $ Sabia.face = "normalopen"
                    s "While that's true, it seems like you value Vegardan elves highly."
                    $ Kira.face = "irritatedopen"
                    $ Sabia.face = "normal"
                    kira "Naturally."
                    kira "It would be good to have more capable individuals in my ranks... but, failing that, I will take what suitable orcs I can get."
                    $ Kira.face = "sadopen"
                    kira "Though even the most accomplished warrior orc can be tiresome to deal with. All those ridiculous notions of honor and pride."
                    $ Kira.face = "normal"
                    $ Sabia.face = "normalopen"
                    s "It's almost a hallmark of orcs, I've found."
                    $ Kira.face = "browsopen"
                    $ Sabia.face = "normal"
                    kira "Mmm. It does make it much more enjoyable to watch them break, though..."
                    $ Kira.face = "browsbite"
                    $ Sabia.face = "normalopen"
                    s "I... can imagine."
                    jump ef3_kira_camp_kira

                "Test of skill." if kira_quest > 0 and kira_quest_testskill_done == False:
                    jump kira_test_of_skill

                "Test of cunning." if kira_quest > 0 and kira_quest_testcunning_done == False:
                    if Sabia.armor == Orcslavearmor:
                        kira "You're gonna need to change out of that armor first."
                        $ Kira.face = "browsbite"
                        $ Sabia.face = "irritated2"
                        kira "...but I'd rather you stay in it, and come to my tent."
                        kira "I'm sure we can have some fun..."
                        menu:
                            "Have fun!":
                                call kira_bandits_badend
                                show gameover with dissolve
                                pause 3
                                $ renpy.full_restart()
                            "I'll change.":
                                jump ef3_kira_camp_kira
                    jump kira_test_of_cunning

                "Have I passed?" if kira_quest == 3:
                    $ kira_quest = 4
                    $ Kira.face = "normalopen"
                    kira "Well... you did succeed with both tasks. And after that scene at the caravan... mmm!"
                    kira "You were quite... sadistic... with them. You didn't just kill them."
                    $ Kira.face = "normalbite"
                    $ Sabia.face = "normalopen"
                    s "You had a look at it on the way back?"
                    $ Sabia.face = "normal"
                    $ Kira.face = "normalopen"
                    kira "Of course! One person succeeding at a target like that - it simply begged us to investigate."
                    kira "And my, we weren't disappointed. I wasn't disappointed."
                    kira "You must have been like an animal. Organs and blood were... everywhere. So much of it."
                    $ Kira.face = "normalbite"
                    $ Sabia.face = "normalopen"
                    s "It wasn't something I was really thinking about. It just happened."
                    $ Sabia.face = "normal"
                    kira "Mmm..."
                    $ Kira.face = "normalopen"
                    kira "Regardless, with that demonstration, and your success - I am more than pleased to have you join us."
                    kira "You will prove a valuable asset, I think. I don't like weak links in my group."
                    $ Kira.face = "browsopen"
                    kira "Some of the other captains take whoever comes through. Numbers, they think."
                    $ Kira.face = "normal"
                    $ Sabia.face = "normalopen"
                    s "Numbers don't always make for the best force. You can have a legion of inept fools and accomplish little."
                    $ Kira.face = "normalopen"
                    $ Sabia.face = "normal"
                    kira "Exactly. I can see why Neve keeps you around. You aren't as useless as I first thought you might be."
                    $ Kira.face = "browsopen"
                    $ Sabia.face = "irritated2"
                    kira "A mage would be better, of course. But for now, you work with us."
                    $ Kira.face = "normal"
                    $ Sabia.face = "normalopen"
                    s "What should I do now, then?"
                    $ Sabia.face = "normal"
                    $ Kira.face = "normalopen"
                    kira "Now? Nothing. You delivered those stones to me personally. You knew what they were... and their value."
                    kira "Clearly, you were not lying about your family."
                    $ Kira.face = "normal"
                    $ Sabia.face = "normalopen"
                    s "I was not."
                    $ Sabia.face = "normal"
                    $ Kira.face = "normalopen"
                    kira "Then you know it will take time to... see them changed into something more liquid."
                    $ Sabia.face = "normal"
                    $ Kira.face = "normal"
                    s "Lundils."
                    $ Kira.face = "normalopen"
                    $ Sabia.face = "normal"
                    kira "A lot of lundils."
                    jump ef3_kira_camp_kira

                "Ask why Kia was recruiting." if (kira_quest_testskill_done == True or kira_quest_testcunning_done == True) and kira_quest_spearinfo == False and kira_quest_recruittalk == False:
                    $ kira_quest_recruittalk = True
                    $ Kira.face = "irritatedopen"
                    kira "Why was I recruiting?"
                    $ Sabia.face = "irritated2"
                    kira "Is that a serious question? I thought the daughter of a mage would be smart."
                    $ Kira.face = "normal"
                    $ Sabia.face = "normalopen"
                    s "I was just wondering. It seemed like a big recruitment, especially since we heard about it in Whitecrest. It seems like an uncommon occurrence."
                    $ Kira.face = "normalopen"
                    $ Sabia.face = "irritated2"
                    kira "Hmm..."
                    kira "It is."
                    $ Kira.face = "irritatedopen"
                    $ Sabia.face = "surprised1"
                    kira "But some of my warrior thought it would be a good idea to try and steal from a Lustrator."
                    $ Kira.face = "normal"
                    $ Sabia.face = "normalopen"
                    s "A..."
                    $ Kira.face = "irritatedopen"
                    kira "Lustrator. Yes, they're idiots."
                    kira "...were idiots. Even I would hesitate to take on a Lustrator..."
                    jump ef3_kira_camp_kira

                "Ask about fur on spear." if (kira_quest_testskill_done == True or kira_quest_testcunning_done == True) and kira_quest_spearinfo == False:
                    $ kira_quest_spearinfo = True
                    $ Kira.face = "normalopen"
                    kira "Oh... this?"
                    $ Kira.face = "normalbite"
                    "Kira's fingers touched the tuft of fur, and Sabia could tell a shiver ran down her spine."
                    $ Kira.face = "normalopen"
                    $ Sabia.face = "irritated2"
                    kira "It took almost two weeks... and a lot of dead men and women."
                    kira "I had to research, find the correct poison to weaken it. But I knew, even that would not be near enough."
                    kira "The research itself took me months after learning there was one nearby... but, oh, I knew. I had to find it. I had to drive my spear into its hide, and listen to it cry and its chest rattle as I took its life."
                    kira "We stalked it, for days, and days. Sometimes, it would come upon us, and some of those with me fell to those claws."
                    $ Kira.face = "browsbite"
                    $ Kira.blush = True
                    kira "The shrieks and pleading... oh. Beautiful."
                    $ Kira.blush = False
                    $ Kira.face = "browsopen"
                    $ Sabia.face = "surprised1"
                    kira "But, even a makhor's strength can reach its end. And reach its end it did..."
                    $ Kira.face = "browsbite"
                    $ Sabia.face = "sad1"
                    kira "It was but a shadow of its former self. Pierced with arrows, dripping blood, cuts exposed to the elements, and with my poison coursing through its veins."
                    kira "Even still, it almost killed me... it would have been easier if I had intended for a killing blow of course..."
                    $ Kira.face = "browsopen"
                    kira "But... oh! The sounds that the makhor made as it died... it was worth the risk."
                    kira "Those sweet sweet screams and pained roars fill my dreams nightly."
                    kira "You had to be there to enjoy it, though. My words would not do it justice."
                    $ Kira.face = "normalbite"
                    $ Sabia.face = "sad3"
                    s "You... killed a makhor?"
                    "Sabia was shocked. Every word that Kira said, the elf exulted in pain and blood."
                    $ Kira.face = "browsopen"
                    $ Sabia.face = "sad1"
                    kira "...eventually."
                    $ Kira.face = "normalbite"
                    "Kira licked her lips and closed her eyes, her fingers stroking the tuft of fur a bit more insistently."
                    $ Kira.face = "normalopen"
                    kira "But not before I enjoyed myself with the creature. It was... sublime."
                    $ Kira.face = "normalbite"
                    "Kira closed her eyes slowly, and her lips curled in a wicked smile."
                    $ Kira.face = "normalopen"
                    $ Sabia.face = "sad2"
                    kira "I can still taste its blood on my lips... if I focus hard enough. The beating of its great heart slowing... slowing... slowing..."
                    kira "And stopping. Beautiful."
                    $ Kira.face = "normalbite"
                    kira "I keep this as a reminder of that. A height that I have never reached before or since."
                    menu:
                        "Thank you for telling me that story":
                            $ A_kira += 1
                            $ Kira.face = "normalopen"
                            kira "It's one of my favorites... telling it is a task I relish."
                            jump ef3_kira_camp_kira
                        "You killed it for sport?!":
                            $ A_kira -= 1
                            $ Kira.face = "angryopen"
                            $ Sabia.face = "irritated1"
                            kira "And who are you to tell me what to enjoy?!"
                            kira "I should gut you right now for your insubordination."
                            $ Kira.face = "angrygrit"
                            "Kira spat."
                            $ Kira.face = "irritatedopen"
                            kira "But it would be a waste. Show more respect in the future."
                            kira "...or don't. I think you would make a fun toy..."
                            $ Kira.face = "normalopen"
                            kira "Before you break."
                            jump ef3_kira_camp_kira

                "Vehlis' Shipments." if vehlis_shipment_quest == 1 and vsq_human_bandit == True and vsq_kira == False:
                    $ vsq_kira = True
                    if vsq_solution == "orcs":
                        s "(I have already secured the help from Grazzag and Yregh, so I {i}really{/i} don't want to bother Kira about this.)"
                        jump ef3_kira_camp_kira
                    $ Kira.face = "normalopen"
                    kira "Ahh... Sabia. How are you today?"
                    $ Sabia.face = "pout1"
                    kira "Haven't changed your mind on..."
                    $ Kira.face = "normalbite"
                    "Kira licked her lips as her eyes flitted over Sabia's frame, fingers curling about her spear a bit tighter."
                    $ Kira.face = "browsopen"
                    $ Sabia.face = "irritated2"
                    kira "...having a bit of fun?"
                    $ Kira.face = "sad"
                    $ Sabia.face = "normalopen"
                    s "Sorry Kira, not quite..."
                    s "I had a thought."
                    $ Kira.face = "normalopen"
                    $ Sabia.face = "normal"
                    kira "Not quite what I want from you the most... but, I'm listening."
                    $ Kira.face = "normal"
                    $ Sabia.face = "normalopen"
                    s "I was scouting around a few of the nearby human villages - they wouldn't recognize me yet."
                    s "And one of them said that they kept being hit by bandits, and as a result their trade and shipments have been severely impeded."
                    $ Kira.face = "browsopen"
                    $ Sabia.face = "normal"
                    kira "Well of course... though it is so, so nice to hear that I affect them so!"
                    $ Kira.face = "normalbite"
                    "Kira shivered."
                    $ Sabia.face = "normalopen"
                    s "Instead of running them into the ground - I thought we could leave them be for some time."
                    $ Kira.face = "angry"
                    $ Sabia.face = "normal"
                    "Kira's gaze narrowed."
                    $ Kira.face = "normal"
                    $ Sabia.face = "happy2"
                    s "Like a pig for slaughter, I mean. Let them recuperate, build up some more coin from trades."
                    $ Sabia.face = "normalopen"
                    s "Hit them a few months down the line when it's really worth it."
                    $ Sabia.face = "normal"
                    if A_kira >= 1:
                        $ A_kira += 1
                        $ vsq_solution = "kira"
                        $ Kira.face = "normalopen"
                        kira "Hmmmmm..."
                        $ Sabia.face = "irritated2"
                        kira "It's not a bad idea. The screams and pleadings... they aren't as sweet if their hope has been extinguished as thoroughly as it has..."
                        $ Kira.face = "browsopen"
                        kira "Very well! I will let them rest, and fatten up... and then they shall bleed all the sweeter."
                        $ Sabia.face = "normalopen"
                        $ Kira.face = "normal"
                        s "There is a small issue though... they might not continue trading, or building up again."
                        s "They might expect further raids?"
                        $ Sabia.face = "normal"
                        "Kira's eyes were half-glazed over as Sabia spoke, nibbling at her lip. The thought of bleeding them was clearly on her mind."
                        $ Kira.face = "normalopen"
                        kira "What was that?"
                        $ Kira.face = "normal"
                        "Sabia repeated herself."
                        $ Kira.face = "normalopen"
                        kira "Ah. Yes. That is a good point..."
                        $ Sabia.face = "irritated2"
                        kira "A good slaughterhouse must take care of its herd, must it not, Sabia?"
                        kira "I will ensure... that I do so."
                        $ Kira.face = "browsbite"
                        $ Sabia.face = "normal"
                        "Sabia nodded."
                        hide Kira with moveoutright
                        $ Sabia.face = "normal"
                        s "I'll have to follow this up with Elliah and Reina in a few days after Kira does... whatever it is she is planning on doing."
                        jump ef3_kira_camp
                    else:
                        $ Kira.face = "normalopen"
                        $ vsq_kira_block = True
                        kira "No."
                        $ Kira.face = "normal"
                        menu:
                            "Accept Kira's position.":
                                $ A_kira += 1
                                "While it certainly didn't help Sabia's current goal, it was definitely better to not push Kira."
                                $ Sabia.face = "normalopen"
                                s "Of course."
                                $ Sabia.face = "normal"
                                $ Kira.face = "normalopen"
                                kira "I thought you might argue your point."
                                kira "You didn't."
                                $ Sabia.face = "eyebrow1"
                                kira "I like that. You... listen well."
                                $ Kira.face = "normal"
                                "Kira gave a sly, dangerous smile before leaving."
                                hide Kira with moveoutright
                                $ Sabia.face = "closed2"
                                s "Well, it seems Kira liked my attitude... but it doesn't help me getting any closer to resolving Vehlis' problem."
                                $ Sabia.face = "normalopen"
                                s "I'll have to find another way."
                                jump ef3_kira_camp
                            "Why?":
                                $ Kira.face = "angry"
                                $ Sabia.face = "angry1"
                                s "What?! Why?"
                                $ Kira.face = "angryopen"
                                $ Sabia.face = "normal"
                                kira "{i}Excuse me{/i}?"
                                $ Sabia.face = "sad1"
                                kira "You question me, in my own camp?"
                                $ Sabia.face = "sad2"
                                kira "Apologize. Now. Or I will drive this tip through your throat and do nothing more than delight in the gurgling sounds as your life slowly slips from you."
                                $ Kira.face = "angry"
                                "Sabia's heart beat faster."
                                $ Sabia.face = "sad3"
                                s "I- I'm sorry, Kira. I apologize."
                                $ Sabia.face = "surprised1"
                                "Kira's hands moved like a flurry - faster than she could react to - and the tip of the spear pressed upon Sabia's throat threateningly."
                                "The Vegardan's eyes bore into Sabia's own, and Sabia's forehead started to sweat immediately."
                                $ Sabia.face = "sad1"
                                $ Kira.face = "normalopen"
                                kira "I accept."
                                $ Kira.face = "normal"
                                "Kira withdrew her weapon."
                                "Sabia had no intention of sticking around at the moment."
                                hide Kira with moveoutright
                                $ Sabia.face = "sad3"
                                s "That was... close. She would have finished me before my hand reached my weapon if she had wanted."
                                s "I need to make sure I tread lightly around her..."
                                s "It seems I'll need to organize another way to resolve Vehlis' request."
                                jump ef3_kira_camp

                "Avion's task." if avion_quest < 6 and avion_quest_prompt == True:
                    kira "Well, have you finished my task, my sweet Sabia?"
                    s "Not yet."
                    kira "Then be doing that. Not talking to me."
                    jump ef3_kira_camp_kira

                "Avion's task." if avion_quest == 6:
                    $ avion_quest = 7
                    $ avion_quest_done = True
                    if avion_quest_plan == "ambush":
                        $ Kira.face = "normalopen"
                        kira "Ah! My sweet... tender Sabia..."
                        kira "Avion told me that the task is done. That my command of the area is stronger."
                        $ Kira.face = "browsopen"
                        kira "I would have liked to be there when they first saw Avion charging toward them."
                        $ Sabia.face = "irritated2"
                        kira "The screams that an unready man makes when they see such a specimen, full of murder and blood in their eyes... oh!"
                        $ Kira.face = "browsbite"
                        "Kira pulled her spear closer to her, letting the razor edge give her a shallow cut on her cheek. Her tongue ran deftly up the edge, licking her blood."
                        kira "Mmm!"
                        $ Kira.face = "normal"
                        $ Sabia.face = "normal"
                        "Sabia nodded hesitantly."
                        $ Sabia.face = "normalopen"
                        s "The ambush worked well. Avion did most of the work, I have to admit."
                        $ Sabia.face = "normal"
                        $ Kira.face = "normalopen"
                        kira "Mmm. Of course... why do you think I sent him?"
                        kira "I don't like the idea of you getting hurt... by anyone that's not me..."
                        $ Kira.face = "normal"
                        "Kira laughed, a pretty trill that somehow seemed even more unnerving than her sadistic words."
                        $ Kira.face = "normalopen"
                        kira "Expect to work with Avion again."
                        $ Kira.face = "normal"
                        $ Sabia.face = "normalopen"
                        s "Well, he's good at what he does."
                        $ Sabia.face = "normal"
                        $ Kira.face = "browsopen"
                        kira "Mmm... that he is. The music he makes with that axe..."
                        $ Sabia.face = "irritated2"
                        $ Kira.face = "browsbite"
                        "Kira shuddered, pulling the haft of her spear closer, pressing the shaft against her crotch."
                        $ Kira.face = "browsopen"
                        kira "Just delicious..."
                        $ Kira.face = "browsbite"
                        "Sabia took a step back as Kira's thoughts quickly began to focus on things other than Sabia."
                        jump ef3_kira_camp
                    elif avion_quest_plan == "cart":
                        $ Sabia.face = "normalopen"
                        s "Did Avion tell you-"
                        $ Sabia.face = "normal"
                        $ Kira.face = "normalopen"
                        kira "Yes! He did."
                        $ Sabia.face = "irritated2"
                        $ Kira.face = "browsopen"
                        kira "It sounded... delicious. I would have liked to have been there to sate my desires on their screams."
                        $ Kira.face = "sadopen"
                        kira "But... sometimes obligations prevent one from enjoying themselves. Don't you agree?"
                        $ Sabia.face = "normalopen"
                        $ Kira.face = "sad"
                        s "Well. That wasn't the plan at all - it was meant to be much quieter, and more efficient."
                        $ Sabia.face = "normal"
                        $ Kira.face = "normalopen"
                        kira "Mmm... I heard. Avion said."
                        kira "I think Avion's decision was correct. What enjoyment is there to be had... if those you are killing, do not scream?"
                        $ Sabia.face = "irritated2"
                        $ Kira.face = "normal"
                        s "..."
                        $ Kira.face = "sadopen"
                        kira "Mmm... what a waste of precious life. Thrown away... no enjoyment to be had."
                        kira "It is better that Avion took things into his own hands."
                        $ Kira.face = "normal"
                        menu:
                            "Agree.":
                                $ avion_sub += 1
                                $ Sabia.face = "normalopen"
                                s "I suppose..."
                                $ Sabia.face = "normal"
                                $ Kira.face = "normalopen"
                                kira "Hmmm..."
                                $ Sabia.face = "pout1"
                                kira "You and Avion may get along well, after all..."
                                $ Kira.face = "normalbite"
                                $ Sabia.face = "normalopen"
                                s "That doesn't seem too likely..."
                                $ Sabia.face = "normal"
                                "Kira's lips curled upward in a wicked grin."
                                $ Kira.face = "normalopen"
                                kira "Perhaps..."
                                $ Sabia.face = "normalopen"
                                $ Kira.face = "normal"
                                s "Well. At least the job is done."
                                $ Sabia.face = "normal"
                                $ Kira.face = "normalopen"
                                kira "Hmm?"
                                $ Kira.face = "normal"
                                $ Sabia.face = "normalopen"
                                s "The job is done."
                                $ Sabia.face = "normal"
                                $ Kira.face = "browsopen"
                                kira "Oh, yes. It is. So sad that I missed the... fun."
                                $ Kira.face = "browsbite"
                                "Kira seemed to lose interest in Sabia as her thoughts about what she might have done overtook her imagination."
                                "Sabia waited for a moment, before turning and leaving."
                                jump ef3_kira_camp
                            "Disagree.":
                                $ avion_dom +=1
                                $ Sabia.face = "normalopen"
                                s "I can't say I agree, but at least the job was done, right?"
                                $ Sabia.face = "normal"
                                $ Kira.face = "normalbite"
                                "Kira licked her lips, and nodded softly."
                                $ Kira.face = "normalopen"
                                kira "Yes. I am pleased with your performance. Even if Avion did not agree with your plan, it was..."
                                $ Sabia.face = "irritated2"
                                kira "..."
                                $ Kira.face = "normalbite"
                                "Kira pulled her spear closer, lapping at the edge with a tongue, eyelids fluttering as her words failed, and her thoughts overtook her."
                                "Sabia waited for a moment, but Kira seemed lost in her mind's eye. She turned and left."
                                jump ef3_kira_camp
                    else:
                        $ Sabia.face = "normalopen"
                        s "Did Avion tell you-"
                        $ Sabia.face = "normal"
                        $ Kira.face = "normalopen"
                        kira "Yes! He did."
                        kira "It sounded... delicious. I would have liked to have been there to sate my desires on their screams."
                        kira "But... sometimes obligations prevent one from enjoying themselves. Don't you agree?"
                        $ Kira.face = "normal"
                        $ Sabia.face = "normalopen"
                        s "It's not an uncommon occurrence at all."
                        $ Sabia.face = "normal"
                        $ Kira.face = "normalopen"
                        kira "Mmhmm... still..."
                        $ Kira.face = "normalbite"
                        "Kira pulled her spear closer to her, and her tongue caressed the glinting edge of the blade."
                        if avion_quest_lost_fight == False:
                            $ Sabia.face = "surprised1"
                            $ Kira.face = "normalopen"
                            kira "Avion said you did well."
                            $ Kira.face = "normal"
                            $ Sabia.face = "irritated2"
                            s "..."
                            $ Sabia.face = "normalopen"
                            s "Huh."
                            $ Sabia.face = "irritated2"
                            s "..."
                            $ Sabia.face = "normalopen"
                            s "Really?"
                            $ Sabia.face = "irritated2"
                            $ Kira.face = "normalopen"
                            kira "I am starting to see why Neve keeps you around... not just for your, hmm. Assets."
                            $ Kira.face = "browsopen"
                            kira "Though I think you would still make a better..."
                        else:
                            $ Sabia.face = "irritated1"
                            $ Kira.face = "normalopen"
                            kira "Avion said you lost..."
                            kira "But that many against one... Neve has convinced me the odds were not favorable and you should get a... {i}pass{/i}."
                            $ Kira.face = "browsopen"
                            kira "But... fail again and..."
                        $ Kira.face = "browsbite"
                        "Kira's words trailed off and she licked her lips, drinking in Sabia's body with her eyes."
                        $ Sabia.face = "normal"
                        $ Kira.face = "normalopen"
                        kira "You can go then, if you want. Your task is done... unless you wish to join me in my bed, finally?"
                        menu:
                            "I'll be fine.":
                                $ Kira.face = "sad"
                                $ Sabia.face = "normalopen"
                                s "Maybe another time..."
                                $ Sabia.face = "normal"
                                "Kira sighed theatrically, before giving Sabia a nod."
                                jump ef3_kira_camp
                            "Alright!":
                                call kira_bandits_badend
                                show gameover with dissolve
                                pause 3
                                $ renpy.full_restart()

                "Bandit prisoner." if avion_quest_bandit_freed == False and avion_quest_kira_bandit_talk == False and avion_quest > 5:
                    $ avion_quest_kira_bandit_talk = True
                    $ Sabia.face = "normalopen"
                    s "I haven't seen the girl we captured anywhere..."
                    s "I was wondering what happened to her?"
                    $ Sabia.face = "normal"
                    "Kira's face lit up."
                    "Her fingers curled a bit tighter around her spear, and her lips curled upward into a predatory grin."
                    $ Kira.face = "normalopen"
                    kira "They believe they need to break the spirit of an enemy's woman... but..."
                    $ Sabia.face = "irritated2"
                    $ Kira.face = "browsopen"
                    kira "Isn't it {i}so much more{/i} fun to break a mind?"
                    $ Kira.face = "browsbite"
                    s "..."
                    $ Sabia.face = "sad3"
                    s "After he... finished with her, he gave her to you, then?"
                    $ Sabia.face = "sad1"
                    $ Kira.face = "normalbite"
                    show Kira behind Sabia at center with move
                    "Kira's hand reached out, and she ran her fingers gently along Sabia's hair."
                    show Kira:
                        xpos 0.3
                    with move
                    $ Sabia.face = "sad2"
                    $ Kira.face = "normalopen"
                    kira "Do you feel some envy? There's a spot next to her for you, if you wish my sweet Sabia..."
                    $ Kira.face = "normal"
                    "Kira's breath was not only hot, but felt... {i}dangerous{/i} as it blew in her face."
                    menu:
                        "No.":
                            $ Sabia.face = "sad3"
                            $ Kira.face = "sad"
                            show Kira at center with move
                            s "No thank you..."
                            $ Sabia.face = "sad1"
                            $ Kira.face = "sadopen"
                            kira "Hmph..."
                            jump ef3_kira_camp
                        "Alright!":
                            $ Kira.face = "browsbite"
                            "Kira whimpered in delight - her thighs pressed against each other. Her fingers dug into Sabia's neck and she wrenched her close."
                            $ Sabia.face = "surprised1"
                            $ Kira.face = "browsopen"
                            kira "Get on your knees..."
                            call kira_bandits_badend
                            show gameover with dissolve
                            pause 3
                            $ renpy.full_restart()
                "Go back":


                    jump ef3_kira_camp
        "Talk to Neve":

            show Sabia at left
            show Neve at right
            with dissolve
            if sub_level == 1:
                $ temp = renpy.random.randint(1,3)
                if temp == 1:
                    $ Neve.face = "happy2"
                    $ Sabia.face = "irritated2"
                    n "Seems like you're getting quite quite the reputation in camp, Sabia..."
                    $ Neve.face = "smirk1"
                    $ Sabia.face = "normalopen"
                    s "I do what has to be done for my end goals."
                    $ Sabia.face = "normal"
                    n "Hmm..."
                elif temp == 2:
                    $ Neve.face = "irritated1"
                    n "I know you've been acting very... pliant lately. But I would caution against it around Kira."
                else:
                    $ Neve.face = "smirk1"
                    $ Sabia.face = "irritated1"
                    n "Better be careful around here Sabia or you'll end up with the same reputation you've earned in Grok og Dar..."
                    "Sabia frowned at Neve's grin."
            menu ef3_kira_camp_neve:
                "Leads on Dajrab's contact" if mariana_found == False and mariana_quest != 0:
                    if mariana_hint1 == False and mariana_hint2 == False and mariana_hint3 == False:
                        n "Found any leads on Dajrab's contact yet?"
                        $ Sabia.face = "normalopen"
                        s "Not yet."
                        jump ef3_kira_camp_neve
                    elif mariana_hint1 == True and mariana_hint2 == True and mariana_hint3 == True and neve_mariana_info1 == False:
                        $ neve_mariana_info1 = True
                        $ Sabia.face = "normalopen"
                        s "I've been talking to different people in the camp, and listening in where I can."
                        $ Neve.face = "happy3"
                        n "Good idea."
                        $ Sabia.face = "normalopen"
                        s "I think I might have a lead. There's one of their group that has apparently disappeared - Mariana."
                        $ Sabia.face = "normal"
                        $ Neve.face = "irritated1"
                        n "I heard similar things."
                        $ Sabia.face = "normalopen"
                        s "Do you think it's the contact we're looking for?"
                        $ Sabia.face = "normal"
                        $ Neve.face = "normal"
                        n "Might be. I think we'll need to try and get a bit more information first, before anything else."
                        $ Sabia.face = "normalopen"
                        s "Agreed. I'll see what I can find."
                        jump ef3_kira_camp_neve
                    elif mariana_quest == 2 and neve_mariana_info2 == False:
                        $ neve_mariana_info2 = True
                        n "What else have you found out, then?"
                        $ Sabia.face = "normalopen"
                        s "Well, seems like Mariana disappeared a few weeks ago. About three, though I wasn't able to get a specific date."
                        $ Sabia.face = "irritated2"
                        $ Neve.face = "irritated1"
                        n "Hmm... that's after Groknak was ambushed. Seems like a bit of a coincidence, doesn't it?"
                        $ Sabia.face = "normalopen"
                        s "If it's someone that was indirectly working for someone in Grok og Dar, but without direct contact..."
                        s "Do you think they might have deserted, fearing some sort of retribution?"
                        $ Sabia.face = "irritated2"
                        $ Neve.face = "normal"
                        n "It seems probable. The timing adds up, and from what we've learned, it seems this Mariana was a bit desperate. Desperate enough to serve as a contact for a third party?"
                        $ Sabia.face = "normalopen"
                        s "I could see it."
                        $ Neve.face = "happy1"
                        s "So if we are assuming that Mariana is the person we're looking for - then the next step is actually tracking her down."
                        $ Sabia.face = "normal"
                        n "Agreed."
                        jump ef3_kira_camp_neve
                    elif mariana_lake_search == 1 and neve_mariana_info3 == False:
                        $ neve_mariana_info3 = True
                        $ Sabia.face = "normalopen"
                        s "So, someone is definitely living somewhere near Lake Sorthyos."
                        $ Sabia.face = "normal"
                        n "You think it's Mariana?"
                        $ Sabia.face = "normalopen"
                        s "I'd say so."
                        $ Sabia.face = "normal"
                        "Sabia took a few moments to detail to Neve what she had learned before heading off to Lake Sorthyos."
                        n "Okay. I agree with your assessment. It's probably Mariana."
                        $ Neve.face = "sad"
                        n "But, are we sure that Mariana is the one Dajrab was after?"
                        $ Neve.face = "normal"
                        $ Sabia.face = "normalopen"
                        s "If there's smoke. And at any rate, I haven't managed to get any other leads."
                        s "I'll see what else I can find out about it."
                        s "I think I know who I need to see. Just sit tight for now."
                        $ Sabia.face = "normal"
                        $ Neve.face = "smirk1"
                        n "If you think you have it in hand, Sabia."
                        jump ef3_kira_camp_neve
                    else:
                        n "Any new information about Dajrab's contact?"
                        s "Working on it."
                        jump ef3_kira_camp_neve

                "Discuss joining the bandits" if kira_quest_testskill_done == False and kira_quest_testcunning_done == False:
                    $ Neve.face = "irritated1"
                    n "I'd make sure you're prepared before starting any of Kira's 'tests'."
                    $ Neve.face = "closed2"
                    n "Someone like her - you can't be sure what to expect."
                    $ Neve.face = "normal"
                    $ Sabia.face = "irritated2"
                    "Sabia nodded."
                    $ Sabia.face = "normalopen"
                    s "Thanks for the advice, Neve."
                    jump ef3_kira_camp_neve

                "Discuss joining the bandits" if (kira_quest_testskill_done == True and kira_quest_testcunning_done == False) or (kira_quest_testskill_done == False and kira_quest_testcunning_done == True):
                    n "Do your best, Sabia. The faster we are both accepted, the faster we can look into Groknak's abduction."
                    $ Sabia.face = "normalopen"
                    s "I don't intend to do anything less than my best."
                    jump ef3_kira_camp_neve

                "Discuss joining the bandits" if kira_quest >= 4 and neve_join_bandits_talk == False:
                    $ neve_join_bandits_talk = True
                    s "Well, we're both in now."
                    $ Neve.face = "happy2"
                    n "Yes, we are. Now we see where this leads, and hopefully we can learn something about Groknak."
                    $ Sabia.face = "happy2"
                    s "Neve?"
                    s "I was wondering, at this point with us both joining - you and Kira are both Vegardan, could you not just ask her directly?"
                    $ Neve.face = "sad"
                    $ Sabia.face = "irritated2"
                    n "I... think that would not go well. The common history we share is more likely to make that more difficult than easier."
                    $ Sabia.face = "normalopen"
                    $ Neve.face = "normal"
                    s "Ah... that's unfortunate. We'll see where this leads then. As you said."
                    $ Sabia.face = "normal"
                    "Neve nodded in agreement."
                    jump ef3_kira_camp_neve

                "What did Kira mean by 'all that white'?" if kira_quest_testskill_done == True and neve_allwhite_talk == False:
                    $ neve_allwhite_talk = True
                    $ Sabia.face = "normalopen"
                    s "I've been pondering what that could have meant. Kira made a point of it."
                    $ Sabia.face = "irritated2"
                    $ Neve.face = "happy3"
                    n "She did. Let's just say that it shows the breadth of my experience is greater than hers."
                    $ Sabia.face = "happy2"
                    $ Neve.face = "irritated1"
                    s "...how old are you Neve?"
                    $ Sabia.face = "eyebrow1"
                    n "You should know it's not polite to ask a woman her age, Sabia."
                    $ Sabia.face = "happy2"
                    $ Neve.face = "normal"
                    s "I mean - does a Vegardan's hair whiten as they age? I remember a few from my mother's parties."
                    $ Sabia.face = "normalopen"
                    s "But I don't think I recall them having white hair like you do."
                    $ Sabia.face = "irritated2"
                    $ Neve.face = "irritated1"
                    n "In a way, Sabia, I suppose."
                    n "It's not something I want to discuss at the moment."
                    n "Not when we have so many other tasks and issues at hand."
                    $ Sabia.face = "normalopen"
                    $ Neve.face = "normal"
                    s "Will you explain it to me some day?"
                    $ Sabia.face = "irritated2"
                    $ Neve.face = "happy3"
                    n "Perhaps."
                    jump ef3_kira_camp_neve

                "What did Kira mean by 'all that white'?" if kira_quest_testskill_done == True and neve_allwhite_talk == True:
                    "Sabia's interest in what Kira had meant by the remark hadn't dimmed at all."
                    $ Neve.face = "irritated1"
                    "She asked Neve what the other Vegardan had meant by it."
                    $ Neve.face = "normal"
                    $ Sabia.face = "irritated2"
                    n "Ask me again another time, Sabia."
                    $ Sabia.face = "normalopen"
                    s "That's basically what you said last time I asked."
                    $ Neve.face = "happy2"
                    $ Sabia.face = "irritated2"
                    n "I didn't say next time I'd tell you."
                    $ Neve.face = "happy1"
                    n "It's a story for another day and another time."
                    jump ef3_kira_camp_neve
                "Plans?":


                    $ Sabia.face = "normalopen"
                    s "So, we're in. What do you suggest we do for a plan from now on?"
                    $ Neve.face = "happy2"
                    $ Sabia.face = "irritated2"
                    n "You'll need to get in deeper with Kira."
                    if sub>dom:
                        $ Neve.face = "smirk1"
                        "Neve went to say something, and then paused, smirking."
                        $ Sabia.face = "annoyed1"
                        s "What?"
                        $ Sabia.face = "irritated2"
                        n "Nothing."
                        s "..."
                        "Neve's smirk grew wider."
                        $ Sabia.face = "angry1"
                        s "What is it?"
                        $ Sabia.face = "irritated2"
                        $ Neve.face = "happy2"
                        n "I just thought it was funny how I phrased that, considering how much of a... well, how you've been acting around Grok og Dar lately. Heh."
                        s "..."
                        $ Neve.face = "smirk1"
                        $ Sabia.face = "normalopen"
                        s "Hilarious."
                        $ Sabia.face = "pout2"
                        "Neve's smirk remained for a few seconds, grinning at Sabia's indignant look."
                    $ Neve.face = "normal"
                    n "Earn her trust a little bit."
                    $ Sabia.face = "normalopen"
                    s "How am I meant to do that? She seems unhinged enough that if I even ask a question, she might snap."
                    $ Neve.face = "irritated1"
                    $ Sabia.face = "normal"
                    n "She seems that way. But she won't. She's smart, she knows there's a time and place."
                    $ Sabia.face = "normalopen"
                    s "Alright, well I'll see what I can do."
                    jump ef3_kira_camp_neve

                "Ask Neve about tentacle monster" if kia_tentacle_quest == 4 and kia_tentacle_quest_neveinfo == False and kia_tentacle_quest_done == False:
                    $ kia_tentacle_quest = 5
                    $ kia_tentacle_quest_neveinfo = True
                    n "The tentacle monster?"
                    n "Is it back?"
                    $ Sabia.face = "normalopen"
                    s "No. Just trying to get your thoughts on it. Maybe what sort of prey it likes, or ways to lure it into the open."
                    $ Sabia.face = "happy2"
                    s "If I end up going past the Grey Isle, having as much information as I can would be valuable. The slime is very valuable, after all."
                    $ Sabia.face = "normal"
                    $ Neve.face = "irritated1"
                    n "I don't think trying to harvest tentacle slime from the Grey Isle is a great idea, Sabia."
                    $ Sabia.face = "surprised1"
                    $ Neve.face = "happy3"
                    n "Besides, you're asking me because it's back - and Kia's not too pleased with it. Right?"
                    $ Sabia.face = "irritated2"
                    s "..."
                    $ Sabia.face = "normalopen"
                    s "No, Kia hasn't mentioned anything-"
                    $ Sabia.face = "irritated2"
                    $ Neve.face = "smirk1"
                    n "Oh, don't feel so bad. It wasn't really a guess. I saw Kia sneaking out of Grok og Dar the other night, from the direction of your tent."
                    n "I've noticed a few new empty nests, and some signs of it roaming around as well. Just two and two together."
                    $ Neve.face = "happy3"
                    n "Don't worry though, no one else saw her."
                    $ Sabia.face = "normal"
                    "Sabia shrugged, holding her hands out in defeat."
                    $ Sabia.face = "normalopen"
                    $ Neve.face = "normal"
                    s "I hope you're right. Explaining Kia to the rest of the camp isn't something I'm looking forward to."
                    $ Sabia.face = "normal"
                    "Neve nodded in agreement."
                    $ Sabia.face = "closed2"
                    $ Neve.face = "smirk1"
                    n "Tentacle monster, though. You might need my help again."
                    $ Neve.face = "normal"
                    "Sabia shook her head."
                    $ Sabia.face = "normalopen"
                    s "No, sorry. While I would like your help, Kia was very adamant against you helping when I suggested it."
                    $ Sabia.face = "normal"
                    "Neve raised her eyebrows and shrugged almost nonchalantly."
                    n "Understandable. She's much closer with you, and a few other reasons, I'm sure..."
                    $ Neve.face = "irritated1"
                    n "Regardless, I don't know of any prey that a tentacle monster prefers. You could try some different types, if you wanted to."
                    $ Sabia.face = "irritated2"
                    n "Though I would hazard a guess that Kia being nearby is not helpful at all. Remember how it seemed to sense our intent?"
                    $ Sabia.face = "normalopen"
                    s "That's true..."
                    s "But it's going to be rather difficult to try and capture or move a tentacle monster if it senses the intent."
                    $ Sabia.face = "irritated2"
                    $ Neve.face = "closed4"
                    n "I only know about tentacle monsters from stories."
                    $ Neve.face = "normal"
                    n "But if it's in orc territory, maybe they've had them here before? You could try asking an orc if they know anything about them."
                    $ Neve.face = "happy3"
                    n "There's also the other route. It worked out well enough for us last time."
                    $ Sabia.face = "normalopen"
                    s "Fair point."
                    jump ef3_kira_camp_neve

                "Ask Neve about herb." if wcv_herb_quest == 3:
                    $ wcv_herb_quest = 4
                    $ Sabia.face = "normalopen"
                    s "Hey Neve, I've got a question for you."
                    $ Sabia.face = "normal"
                    $ Neve.face = "smirk1"
                    n "Well, I probably have an answer."
                    $ Sabia.face = "normalopen"
                    $ Neve.face = "normal"
                    s "So, it seems that I'm in need of a herb that grows mostly in Vegardan territory..."
                    s "And was wondering if you might possibly have a small dried supply of it?"
                    $ Sabia.face = "normal"
                    $ Neve.face = "irritated1"
                    n "There are a few plants that grow primarily in that region."
                    $ Sabia.face = "normalopen"
                    s "I'm after rotteral."
                    $ Sabia.face = "happy3"
                    $ Neve.face = "happy1"
                    n "Well, that I do have."
                    n "Why the sudden need for that though?"
                    $ Sabia.face = "normalopen"
                    $ Neve.face = "smirk1"
                    s "I'm trying to help Vehlis out with a request she had - organize a shipment of alcohol into The Silvertusk."
                    $ Sabia.face = "normal"
                    "Neve raised an eyebrow."
                    $ Sabia.face = "normalopen"
                    s "And I don't have any intention of dragging a caravan by myself from one of Whitecrest's outlying villages back to Grok og Dar."
                    $ Sabia.face = "normal"
                    $ Neve.face = "happy1"
                    n "I can't imagine anyone wanting to do that, no."
                    $ Sabia.face = "normalopen"
                    s "And the only animals available are some horses from a - hmm. Less than pleasant stable master, let's say."
                    s "But fortunately for me, one of her horses has taken ill, and I'm able to put her in my debt."
                    $ Sabia.face = "normal"
                    $ Neve.face = "happy2"
                    n "Ah. Well, that should be fine. I don't mind parting with a little bit of it to help you, Vehlis, and some sober orcs out."
                    $ Sabia.face = "happy3"
                    s "Thanks Neve."
                    $ Neve.face = "smirk1"
                    $ Sabia.face = "normal"
                    n "I might tag along."
                    $ Sabia.face = "normalopen"
                    s "Sure, I'd be happy to have your company."
                    n "Come to me when you're ready to go deliver the herbs."
                    jump ef3_kira_camp_neve

                "Go deliver herbs." if wcvillage_first_visit_stables == False and wcv_herb_quest == 4:
                    $ met_tijana = True
                    $ wcvillage_first_visit_stables = True
                    $ vsq_gothorse = True
                    $ wcv_herb_quest_done = True
                    $ Sabia.face = "angry1"
                    $ Neve.face = "happy3"
                    "Neve nodded. The two of them left for the small village."
                    scene bg black with dissolve
                    pause(0.1)
                    scene bg hcssstables
                    show Sabia at left
                    show Neve at center
                    with dissolve
                    s "Open up, Tijana!"
                    $ Sabia.face = "irritated1"
                    "Sabia heard some furniture scraping as the woman yelled."
                    tijana "Go away. Stables are {i}closed{/i}."
                    $ Sabia.face = "normalopen"
                    $ Tijana.face = "angry"
                    s "So I guess you {i}don't{/i} want those medicinal herbs you were after? I have them right here, but I guess I can find someone else that-"
                    $ Sabia.face = "irritated2"
                    $ Neve.face = "normal"
                    "Sabia had barely finished her sentence before she heard the lock unbolted, and the door swung open."
                    show Tijana at right with moveinright
                    $ Tijana.face = "angryopen"
                    tijana "No! Do you have them, truly?"
                    $ Tijana.face = "normal"
                    "Tijana's gaze instantly fell on Neve as she spoke."
                    $ Tijana.face = "angryopen"
                    tijana "Who is that?"
                    $ Tijana.face = "angry"
                    $ Neve.face = "happy3"
                    n "Just a friend of Sabia's."
                    $ Sabia.face = "irritated1"
                    $ Neve.face = "irritated1"
                    $ Tijana.face = "angryopen"
                    tijana "Well, you're not welcome here."
                    "Sabia produced a small pouch of herbs, showing it to Tijana as the woman walked over."
                    $ Sabia.face = "normalopen"
                    s "My friend who isn't welcome provided the herbs."
                    $ Sabia.face = "irritated1"
                    "Tijana held out her hand."
                    $ Tijana.face = "angry"
                    $ Sabia.face = "normalopen"
                    s "They're not free."
                    $ Sabia.face = "normal"
                    $ Neve.face = "irritated1"
                    "Tijana pulled her hand back quickly."
                    $ Tijana.face = "angryopen"
                    tijana "What do you want?"
                    $ Tijana.face = "angry"
                    $ Sabia.face = "normalopen"
                    s "You already know what I want. I want to rent a horse. A trade caravan, down to Grok og Dar. And then back."
                    $ Sabia.face = "normal"
                    "Tijana's face flickered for a moment, before giving a begrudging nod."
                    $ Tijana.face = "normalopen"
                    tijana "Deal."
                    $ Sabia.face = "irritated1"
                    $ Tijana.face = "normal"
                    "She tried to snatch the pouch from Sabia's grip, but Sabia kept a firm hold of it."
                    $ Tijana.face = "normalopen"
                    tijana "But if my horse is hurt in any way, I'll make sure that you experience the same."
                    $ Tijana.face = "normal"
                    $ Sabia.face = "normalopen"
                    s "He won't be."
                    $ Sabia.face = "normal"
                    $ Neve.face = "normal"
                    "Tijana kept a narrow gaze. She gave another curt nod."
                    $ Sabia.face = "normalopen"
                    s "And I want to borrow the horse now."
                    $ Sabia.face = "normal"
                    $ Tijana.face = "normalopen"
                    tijana "After I brew the herbs, then I'll ready him for you."
                    $ Tijana.face = "normal"
                    $ Sabia.face = "normalopen"
                    s "Deal."
                    $ Sabia.face = "normal"
                    "Sabia let go of the pouch, and Tijana yanked it back."
                    "Neve had a look around the stables while Tijana brewed the herbs."
                    "After a short while, Tijana administered the remedy. She looked perceptibly relieved."
                    "Sabia could hear snippets of the whispered murmurs from where she was standing."
                    $ Tijana.face = "sadopen"
                    tijana "...okay boy... better soon! Fun... later!"
                    $ Tijana.face = "sad"
                    "After giving the sick horse another few minutes of attention, Tijana selected one of her other stallions, and readied him."
                    $ Tijana.face = "normalopen"
                    tijana "If he comes back hurt or harmed, I will... hmph. You better bring him back safe."
                    $ Tijana.face = "normal"
                    $ Sabia.face = "normalopen"
                    s "I intend to."
                    $ Neve.face = "happy2"
                    $ Sabia.face = "surprised1"
                    n "I might stay here while you do your errand, Sabia."
                    $ Sabia.face = "normal"
                    "Neve looked Tijana up and down appraisingly."
                    $ Neve.face = "smirk1"
                    n "We might have some common conversation topics, Tijana."
                    $ Neve.face = "happy1"
                    $ Tijana.face = "normalopen"
                    tijana "...if you want."
                    $ Tijana.face = "normal"
                    $ Sabia.face = "closed2"
                    s "(Definitely seems like she just feels indebted to Neve and doesn't want to push her out of the door like she did me earlier...)"
                    $ Sabia.face = "normal"
                    "Sabia nodded, leading the horse out of the stables."
                    hide Neve
                    hide Tijana
                    with dissolve
                    $ Sabia.face = "happy3"
                    s "I'll be able to go and resolve that shipment, finally."
                    $ Sabia.face = "normalopen"
                    s "I better do that before anything else."
                    jump wcvillage
                "Go back":

                    jump ef3_kira_camp

        "Go find Mariana" if mariana_lake_search == 2 and mariana_found == False:
            jump finding_mariana

        "Talk to grizzled orc" if kira_camp_gorc_killed == False:
            $ GenericOrc2.extras = ["Loincloth", "Hair", "Wrists"]
            show Sabia at left
            show GenericOrc2 at right
            with dissolve
            if kira_camp_gorctalk == 0:
                $ kira_camp_gorctalk = 1
                $ GenericOrc2.face = "angry"
                orc "What?"
                $ Sabia.face = "normalopen"
                $ GenericOrc2.face = "suspicious"
                $ Sabia.face = "normalopen"
                s "I was just looking around, and getting to know everyone better."
                $ Sabia.face = "normal"
                $ GenericOrc2.face = "angry"
                orc "Hmph."
                $ GenericOrc2.face = "suspicious"
                $ Sabia.face = "normalopen"
                s "How long have you been working with Kira?"
                $ Sabia.face = "normal"
                $ GenericOrc2.face = "angry"
                orc "This one has been with Kira for the better part of a year."
                $ GenericOrc2.face = "suspicious"
                $ Sabia.face = "normalopen"
                s "What about before then?"
                $ GenericOrc2.face = "angry"
                $ Sabia.face = "normal"
                orc "This one has seen much war."
                $ GenericOrc2.face = "suspicious"
                $ Sabia.face = "normalopen"
                s "What's your name?"
                $ Sabia.face = "normal"
                $ GenericOrc2.face = "angry"
                orc "Hmph."
                $ Sabia.face = "closed2"
                s "(I don't think I'm getting much more out of him...)"
                jump ef3_kira_camp
            if neve_mariana_info2 == True and mariana_lake_search == 0:
                $ Sabia.face = "normalopen"
                s "I don't mean to bother you, but I've noticed you're very solitary and quiet. I imagine you notice quite a lot that goes on."
                $ Sabia.face = "irritated2"
                $ GenericOrc2.face = "suspicious"
                "The orc grunted. Whether it was in the affirmative or negative, that was left up to Sabia's interpretation."
                "She decided to test her luck."
                $ Sabia.face = "normalopen"
                s "Do you know anything about that Mariana that disappeared?"
                $ Sabia.face = "irritated2"
                $ GenericOrc2.face = "angry"
                orc "Hmph."
                $ Sabia.face = "annoyed1"
                "Sabia rolled her eyes, expecting nothing more from the orc."
                "She was pleasantly surprised when he spoke again."
                $ Sabia.face = "normal"
                $ GenericOrc2.face = "angry"
                orc "Haven't seen Mariana in almost a moon."
                orc "Young girl. Pretty. For a human."
                orc "Used to go to Lake Sorthyos often."
                $ GenericOrc2.face = "suspicious"
                $ Sabia.face = "normalopen"
                s "Lake Sorthyos? Do you know why she would have gone there?"
                $ Sabia.face = "normal"
                "The orc shrugged."
                $ GenericOrc2.face = "angry"
                orc "Why did you come here? Why did this one come here? Why did Kira come here?"
                $ GenericOrc2.face = "suspicious"
                $ Sabia.face = "normalopen"
                s "I'm not following."
                $ Sabia.face = "irritated2"
                $ GenericOrc2.face = "angry"
                orc "Because it suited the demands on oneself at the time. This is obvious."
                orc "Thought humans were meant to be smart."
                $ GenericOrc2.face = "suspicious"
                $ Sabia.face = "normalopen"
                s "We are, but that doesn't mean we are all excellent at understanding cryptic words."
                s "Just like not all orcs are violent brutes."
                $ Sabia.face = "normal"
                "The orc glared at Sabia, taking her words in."
                $ GenericOrc2.face = "normalopen"
                orc "This one was mistaken. You are not as narrow minded as this one first thought."
                orc "Many years of a certain type of treatment cause a certain type of... presumption of humans."
                $ GenericOrc2.face = "normal"
                $ Sabia.face = "normalopen"
                s "I understand. It goes both ways."
                $ Sabia.face = "normal"
                "The orc inclined his head slightly before turning away."
                hide GenericOrc2 at right
                $ Sabia.face = "closed4"
                s "Well... Lake Sorthyos, huh?"
                s "It's a bit of a trek, but it's all I've got at the moment. No one else seemed to know where she might have gone... only that she had disappeared."
                jump lake_sorthyos_mariana

            if neve_mariana_info3 == True and mariana_lake_search == 1:
                $ mariana_lake_search = 2
                $ Sabia.face = "happy2"
                s "So, that Mariana."
                $ Sabia.face = "eyebrow1"
                $ GenericOrc2.face = "normalopen"
                orc "Hmm?"
                $ GenericOrc2.face = "normal"
                $ Sabia.face = "happy2"
                s "I think you like her a bit more than you let on."
                $ Sabia.face = "irritated2"
                $ GenericOrc2.face = "normalopen"
                orc "This one is... confused?"
                $ GenericOrc2.face = "normal"
                $ Sabia.face = "happy2"
                s "You're the only one I've heard talk about her as anything other than a 'set of tits'."
                $ Sabia.face = "normal"
                $ GenericOrc2.face = "normalopen"
                orc "Respect is something that this orc values."
                $ GenericOrc2.face = "normal"
                $ Sabia.face = "normalopen"
                s "Hmm."
                menu:
                    "Not buying it. Tell Kira what Sabia has learned.":
                        $ GenericOrc2.face = "normalopen"
                        orc "Wait."
                        $ Sabia.face = "annoyed1"
                        s "What?"
                        $ Sabia.face = "annoyed2"
                        $ GenericOrc2.face = "normalopen"
                        orc "This one... might know something."
                        $ Sabia.face = "annoyed1"
                        s "Too late now. Dealing with an old cryptic orc that won't give me straight answers to start with, it's tiring."
                        $ Sabia.face = "happy2"
                        s "I expect I'll have better luck telling Kira what I have found."
                        $ GenericOrc2.face = "sad2"
                        $ Sabia.face = "irritated2"
                        orc "Mariana does not deserve what Kira will do to her."
                        $ Sabia.face = "normalopen"
                        $ GenericOrc2.face = "sad1"
                        s "Perhaps not. But that's out of my hands. I have my own problems, and my own things I need to accomplish."
                        s "And I'm not going to waste my time dealing with an old, stuffy orc with faux chivalric intentions."
                        $ Sabia.face = "normal"
                        $ GenericOrc2.face = "sad2"
                        orc "Please, don't... this orc does not want to be responsible for what happens after you tell Kira."
                        $ GenericOrc2.face = "sad1"
                        $ Sabia.face = "closed2"
                        s "(I could keep Kira out of this. It might be easier than dealing with her... but it might also curry me some favor with the elf.)"
                        menu:
                            "Tell Kira":
                                $ mariana_lake_search_toldkira = True
                                $ A_kira += 2
                                $ Sabia.face = "normalopen"
                                $ GenericOrc2.face = "suspicious"
                                s "Sorry. I gave you your chance to help."
                                $ Sabia.face = "irritated2"
                                "The orc growled."
                                $ GenericOrc2.face = "angry"
                                orc "This one was not wrong about you. He should never have distrusted his first opinion of you."
                                "He roared, and charged at Sabia."
                                $ GenericOrc2.face = "angry"
                                $ GenericOrc2.extras = ["Loincloth", "Hair", "Wrists"]
                                $ enemy_skills = [Preparation, PreparedstrikeI, Enemyattack]
                                $ enemy_level = 11
                                $ enemy_maxhp = 800
                                $ enemy_hp = enemy_maxhp
                                $ enemy_type = 2
                                $ enemy_attack = 75
                                $ enemy_defense = 20
                                $ enemy_magdefense = 20
                                $ player = Sabia
                                $ enemy = GenericOrc2
                                call duel
                                if _return != "Victory":
                                    show gameover with dissolve
                                    pause 3
                                    $ renpy.full_restart()
                                $ kira_camp_gorc_killed = True
                                scene bg cave with dissolve
                                pause (0.01)
                                show Sabia with dissolve
                                "Sabia grunted, throwing down her weapon as a crowd formed around them."
                                show Kira at right with moveinright
                                $ Kira.face = "browsbite"
                                "Kira licked her lips, watching as the blood oozed from the cuts left by the edge of Sabia's weapon."
                                $ Kira.face = "browsopen"
                                $ Sabia.face = "normal"
                                kira "Mmm... beautiful work, Sabia."
                                kira "But I do insist you tell me exactly why you're killing one of my best warriors."
                                kira "And... I oh so hope you don't have a good reason."
                                $ Kira.face = "normalbite"
                                $ Sabia.face = "normalopen"
                                s "I do, actually, have a good reason."
                                $ Sabia.face = "normal"
                                "Sabia relayed what she had learned about Mariana deserting, and how Sabia suspected she was hiding near Lake Sorthyos."
                                "She then told Kira how her suspicions were confirmed when she pressed the orc for more information, and he attacked."
                                $ Kira.face = "sad"
                                "Kira's face fell."
                                $ Kira.face = "sadopen"
                                kira "How... disappointing."
                                $ Kira.face = "normalopen"
                                kira "But no matter, no matter."
                                $ Kira.face = "browsopen"
                                $ Sabia.face = "irritated2"
                                kira "I'm sure some fun can be salvaged from this."
                                $ Kira.face = "normalopen"
                                kira "He's still alive. I'll get Mariana's location from him."
                                kira "Bring her to me. I always thought she was cute... and colored so nicely, too... if only she were an elf."
                                kira "Mmm. But I'm sure she'll make a fine... distraction."
                                $ Kira.face = "browsbite"
                                $ Sabia.face = "normal"
                                "Kira instructed two nearby orcs to help carry the old warrior away, and she left with them."
                                "She was gone barely ten minutes before returning, a sated smile on her face, and a plume of blood running from stomach to nose decorating her."
                                $ Kira.face = "normalopen"
                                kira "Give me your map. I know where my little Mariana lives..."
                                $ Kira.face = "browsopen"
                                kira "Bring her to me."
                                $ Sabia.face = "happy2"
                                s "Of course."
                                hide Kira with moveoutright
                                $ Sabia.face = "closed4"
                                s "Perhaps not... my initial plan. But I suppose it worked out in the end. Somewhat."
                                jump ef3_kira_camp
                            "Don't tell Kira":
                                "The orc heaved a great sigh."
                                $ GenericOrc2.face = "sad2"
                                orc "Very well... this orc will tell you where Mariana is."
                                orc "He can only hope that you do not harm her."
                                $ GenericOrc1.face = "sad1"
                                "With a great deal of reluctance, the orc marked a spot on Sabia's map for where she would be able to find Mariana."
                                jump ef3_kira_camp
                    "Look, I'm just trying to track her down":
                        $ GenericOrc2.face = "normalopen"
                        orc "This orc wonders why, though?"
                        orc "Are you perhaps family... is that why you have come to join us?"
                        $ GenericOrc2.face = "normal"
                        $ Sabia.face = "normalopen"
                        s "No. But someone has sent me after her, to try and retrieve her."
                        $ Sabia.face = "normal"
                        $ GenericOrc2.face = "normalopen"
                        orc "...a friend?"
                        $ GenericOrc2.face = "normal"
                        $ Sabia.face = "normalopen"
                        s "Yes."
                        $ GenericOrc2.face = "normalopen"
                        $ Sabia.face = "normal"
                        orc "Hmm..."
                        $ GenericOrc2.face = "normal"
                        "Not technically incorrect. He didn't ask who was whose friend... and Sabia reasoned Dajrab could be considered her friend..."
                        "The orc heaved a great sigh."
                        $ GenericOrc2.face = "normalopen"
                        orc "Very well... this orc will tell you where Mariana is."
                        $ GenericOrc2.face = "sad2"
                        orc "He can only hope that you do not harm her."
                        $ GenericOrc2.face = "sad1"
                        "With a great deal of reluctance, the orc marked a spot on Sabia's map for where she would be able to find Mariana."
                        jump ef3_kira_camp
            else:

                orc "Hmph."
                jump ef3_kira_camp
        "Talk to minotaur":

            show Sabia at left
            show Avion at right
            with dissolve
            if avion_quest_heart_ritual <= 4 and avion_quest_heart == True and avion_quest_done == True:
                menu:
                    "Observe Avion's ritual." if avion_quest_heart_ritual == 0:
                        $ avion_quest_heart_ritual = 1
                        "Sabia knew about the heart rituals that the minotaurs performed. She had heard about them, heard people talk about them."
                        "But she had never seen it in person. She doubted very much the truth of some of the claims that it did not rot or fester in the days left to the elements."
                        "She approached the area Avion had set it up. The round stone sat on the forest floor."
                        "It was etched with careful pictograms that Sabia didn't recognize, and was almost perfectly flat otherwise."
                        "A thin layer of gleaming oils sat atop the etched pictures."
                        "A small point protruded from the top as if they had smelted two different pieces of rock together."
                        "It was razor sharp and pointed upward. The heart was impaled on it, and the barest tip of it was poking out from the organ."
                        "The ritual would start tomorrow."
                        jump ef3_kira_camp
                    "Observe Avion's ritual." if avion_quest_heart_ritual_d1 == False and avion_quest_heart_ritual == 2:
                        $ avion_quest_heart_ritual_d1 = True
                        "The heart was immaculate, as if it had just been ripped from its home."
                        "Sabia would not have been surprised to see it beat a few times as it sat there impaled on Avion's stone."
                        "Even though it had only been a day, the blood should have congealed. Ants should have been swarming it."
                        "But nothing."
                        "She watched as Avion spoke softly over the heart, tipping more oils onto the pictograms carved into the stone, muttering softly."
                        "Sabia shrugged, deciding to leave it for now."
                        jump ef3_kira_camp
                    "Observe Avion's ritual." if avion_quest_heart_ritual_d2 == False and avion_quest_heart_ritual == 3:
                        $ avion_quest_heart_ritual_d2 = True
                        "Two days had passed already since Avion and Sabia had destroyed the motley bandit crew."
                        "And still, Avion's prize - a warrior's heart was as if it were only just torn from a body."
                        "Sabia was curious. She approached Avion."
                        $ Sabia.face = "normalopen"
                        s "So, what? Keeping it clean is part of the ritual?"
                        $ Sabia.face = "irritated2"
                        avion "No."
                        s "..."
                        $ Sabia.face = "normalopen"
                        s "Is it a different heart?"
                        $ Sabia.face = "irritated2"
                        avion "No."
                        $ Sabia.face = "normalopen"
                        s "It should be beginning to smell, to look off by now, then."
                        $ Sabia.face = "irritated2"
                        avion "So you think."
                        "Avion's tone suggested that he was not going to answer any more questions."
                        $ Sabia.face = "irritated1"
                        "Sabia furrowed her brows again before leaving him alone."
                        jump ef3_kira_camp
                    "Observe Avion's ritual." if avion_quest_heart_ritual_d3 == False and avion_quest_heart_ritual == 4:
                        $ avion_quest_heart_ritual_d3 = True
                        "After three days, still Avion's prize heart seemed unmarred."
                        "The air in the clearing seemed oddly still, even as the canopy of leaves above rustled."
                        "Sabia's curiosity got the better of her, and she approached Avion again."
                        $ Sabia.face = "normalopen"
                        s "There's no way that a piece of meat like that can sit where it has for several days and not even have blood congealing."
                        $ Sabia.face = "irritated2"
                        avion "So says one who follows the witch-god."
                        s "..."
                        $ Sabia.face = "normalopen"
                        s "Fine. Let's just ignore that then, for now. I can see you're not going to give me an answer."
                        s "What do you do with the heart? Do you really eat it after it's been sitting out for three days?"
                        $ Sabia.face = "irritated2"
                        avion "You said yourself it is fine."
                        s "..."
                        avion "If you must watch, do so without speaking - or I will take your heart and spirit both."
                        menu:
                            "Watch.":
                                $ Sabia.face = "normal"
                                "Sabia shrugged, and then gave a curt nod."
                                "Despite her misgivings, she was still interested. Fighting the minotaurs on the frontline and never having seen this ritual had made her curious."
                                "Avion looked as if he might say something - as if he had expected her to leave."
                                "But a moment later, he moved forward. He stood in front of the heart and the stone, and with a deliberate slowness, he fell to his knees in front of it."
                                "He whispered words. Sabia was too far to hear and suspected Avion would be more than displeased if she encroached too far."
                                "Avion's fingers splayed out a little, the sides of his hands pressing down on the edges of the stone, thumbs pointing skyward."
                                "They almost formed a cup. As slowly as he had with anything else, his hands moved inward."
                                "His palms pressed against the heart, and Sabia could see fresh streaks of scarlet blood dripping out of it."
                                "A copper tang filled the air, like the heart had only just stopped beating."
                                "Still speaking softly, Avion raised the heart and lifted it from the stone spike, and let it rest entirely in his grip."
                                "Bringing it closer still, he breathed in deeply, the heart only an inch from his face."
                                "Then, he opened his jaws and delicately pushed the whole organ into his mouth."
                                "Blood gushed out from his lips, staining his fur and running down his chin as he chewed the whole thing at once, swallowing it after only a few seconds."
                                "Avion closed his eyes and stayed still, until a minute later when Sabia judged that the ritual had finished and the minotaur stood once more."
                                avion "..."
                                "He ignored Sabia, turning away from her and began to gently clean the stone."
                                hide Avion with dissolve
                                "Sabia looked around, noticing that a soft breeze was blowing through the camp now."
                                "She frowned to herself before leaving Avion."
                                jump ef3_kira_camp
                            "Leave.":
                                $ A_avion += 1
                                $ Sabia.face = "normalopen"
                                s "I'll leave you to it."
                                jump ef3_kira_camp

            if kira_camp_minotaurtalk == 0:
                $ kira_camp_minotaurtalk = 1
                $ Sabia.face = "normalopen"
                s "Hey, I'm Sabia."
                $ Sabia.face = "irritated2"
                "The large frame of the minotaur hunched forward a little more on the log he was resting atop, facing away from Sabia."
                "He snorted, steam billowing from his nostrils."
                $ Sabia.face = "annoyed2"
                s "...alright, then."
                $ Sabia.face = "annoyed1"
                "Sabia blinked, pursing her lips as she turned away from the minotaur."
                "Neve caught Sabia's sight from a little bit across the camp, and walked over."
                show Neve at right with moveinright
                $ Neve.face = "irritated1"
                n "I wouldn't expect him to be overly communicative with you, Sabia."
                $ Neve.face = "normal"
                n "I think he noticed your tattoo. Your sleeve must have hiked up a bit too far."
                $ Sabia.face = "normalopen"
                s "Yeah... that makes sense."
                $ Sabia.face = "normal"
                n "I overheard before, his name is Avion. I'd try and avoid him if I were you."
                jump ef3_kira_camp
            elif kira_camp_minotaurtalk == 1 and mariana_quest >= 1:
                $ kira_camp_minotaurtalk = 2
                $ mariana_hint1 = True
                $ Sabia.face = "normalopen"
                s "You're far from home."
                $ Sabia.face = "normal"
                "The minotaur grunted, continuing to keep his seat on the fallen log, not budging or even turning to look at Sabia."
                avion "Yes."
                $ Sabia.face = "normalopen"
                s "And with strange company for a minotaur."
                $ Sabia.face = "normal"
                avion "Yes."
                $ Sabia.face = "normalopen"
                s "And with few words."
                $ Sabia.face = "normal"
                "The minotaur snorted, his large nostrils flaring and a plume of steam billowed out from them."
                avion "Words are for friends and family."
                $ Sabia.face = "irritated2"
                avion "Ones that you would slaughter. Ones that you have slaughtered."
                avion "I have seen others with that mark on your arm, I know who has it."
                $ Sabia.face = "normalopen"
                s "That was some time ago."
                $ Sabia.face = "normal"
                avion "Not long enough."
                avion "I thought I would not meet someone again that I dislike more than Mariana."
                avion "But it seems I was wrong. I can never be sure when it comes to humans."
                $ Sabia.face = "normalopen"
                s "Who's Mariana?"
                $ Sabia.face = "irritated2"
                avion "I would have thought it obvious when I no longer welcome talk."
                avion "It does not surprise me, human, that you can't take a hint."
                avion "Since that is the case, let me be clear: I do not wish to talk to you anymore. Talking with a human is tiresome at the best of times."
                jump ef3_kira_camp
            elif kira_camp_minotaurtalk == 2 and avion_quest_prompt == False:
                avion "I thought I made my intent toward you clear. Leave me alone."
                jump ef3_kira_camp
            elif avion_quest_prompt == True and avion_quest == 0:
                menu:
                    "Kira's task.":
                        $ avion_quest = 1
                        $ Avion.face = "angry"
                        $ Sabia.face = "annoyed2"
                        avion "Hmph. Not even worthy to be Tlactina, and still you insist on talking to me."
                        $ Sabia.face = "annoyed1"
                        $ Avion.face = "normal"
                        s "I'd be happy to follow your wish."
                        s "But Kira said I'm to help you with your job."
                        $ Sabia.face = "normal"
                        $ Avion.face = "normaleyes"
                        avion "..."
                        "Avion glared at Sabia for what seemed to be several minutes, before letting out a long, rumbling snorting sigh."
                        $ Sabia.face = "irritated2"
                        $ Avion.face = "normal"
                        avion "Very well. But I do not think that it is a good idea. One human is a hindrance, not help."
                        $ Avion.face = "angry"
                        avion "It took many..."
                        avion "Hmph."
                        $ Avion.face = "normal"
                        $ Sabia.face = "normalopen"
                        s "Trust me, it's not my idea of a good day out either. It's clear you don't like me."
                        s "Just tell me what Kira wants done, we'll do it, and we'll be on our way and hopefully that's it."
                        s "Deal?"
                        $ Sabia.face = "normal"
                        avion "..."
                        avion "If it must be done, then that seems like the best course of action."
                        avion "Kira wants one of the other bandit camps removed. They are encroaching too far, and being too reticent at instructions."
                        $ Avion.face = "angry"
                        "Avion paused for a moment, glaring at Sabia."
                        $ Sabia.face = "irritated2"
                        avion "Does that not remind you of anything?"
                        $ Sabia.face = "normalopen"
                        $ Avion.face = "normal"
                        s "Uh..."
                        $ Sabia.face = "normal"
                        "It seemed like Avion was determined to make this as awkward as possible for Sabia. She decided it was best to ignore it for now."
                        $ Sabia.face = "normalopen"
                        s "I thought we were sort of allied with the other bandit groups?"
                        $ Sabia.face = "irritated2"
                        avion "Kira cares little for that, or the others. Just as I care little for you. But when a thorn pricks your side, you remove it."
                        $ Avion.face = "smirk"
                        avion "If you do not agree with her plan, then I suggest you go tell her. Then perhaps I will not have to suffer seeing you in camp."
                        $ Avion.face = "normal"
                        $ Sabia.face = "normalopen"
                        s "No, it's fine. I'll help."
                        $ Sabia.face = "normal"
                        $ Avion.face = "angry"
                        avion "Excellent."
                        $ Avion.face = "normal"
                        "Avion's tone suggested that he thought it was anything but excellent."
                        $ Avion.face = "normal"
                        avion "Come back to me another time, and I will share the details."
                        $ Avion.face = "normal"
                        $ Sabia.face = "normalopen"
                        s "Why not now?"
                        $ Sabia.face = "annoyed2"
                        $ Avion.face = "angry"
                        avion "I wish to spare myself too much time spent with you."
                        $ Avion.face = "normal"
                        $ Sabia.face = "normal"
                        "Avion grunted, turning around and sitting back on his log. His back faced Sabia."
                        $ Sabia.face = "normalopen"
                        hide Avion with moveoutright
                        s "Well, alright then, I suppose."
                        s "Later it is."
                        jump ef3_kira_camp

            elif avion_quest == 2:
                menu:
                    "Kira's task.":
                        $ avion_quest = 3
                        $ Sabia.face = "annoyed2"
                        $ Avion.face = "normal"
                        avion "I was hoping you would go and tell Kira that you had decided against helping."
                        "He sighed again."
                        $ Sabia.face = "normal"
                        avion "There is a smaller group to the south west."
                        $ Avion.face = "smirk"
                        avion "I have watched, and decided that I will be enough to deal with it."
                        $ Sabia.face = "normalopen"
                        s "So what do you want me to do, then?"
                        $ Sabia.face = "normal"
                        $ Avion.face = "normal"
                        avion "You can watch."
                        $ Sabia.face = "normalopen"
                        s "And if you need help, I will jump in?"
                        $ Sabia.face = "normal"
                        "His eyes roamed up and down Sabia."
                        $ Sabia.face = "annoyed2"
                        $ Avion.face = "happy"
                        avion "Perhaps afterwards if there are no worthy women or warriors, I will use you. The Gods demand an offering after battle."
                        $ Sabia.face = "closed2"
                        $ Avion.face = "normal"
                        s "..."
                        s "(Better to just ignore the being used part. I don't have any intention of antagonizing him further. I want this done with.)"
                        s "(I know a minotaur can handle several men, and I'm sure the bandits are probably less ready, and less equipped than our soldiers were...)"
                        $ Sabia.face = "annoyed2"
                        s "(But still, I'm sure there's a better way than just charging in.)"
                        $ Sabia.face = "normalopen"
                        s "I think it would better if I do a bit of information gathering as well, and maybe we can come up with something a bit less risky."
                        $ Sabia.face = "normal"
                        $ Avion.face = "angry"
                        avion "No. We will do my plan."
                        menu:
                            "Submit to Avion's plan.":
                                $ avion_quest_plan = "avion"
                                $ avion_quest = 4
                                $ sub += 1
                                $ avion_sub += 1
                                $ Sabia.face = "normalopen"
                                $ Avion.face = "normal"
                                s "Alright, fine. If it gets it over and done with quickly - I'm in favor of it."
                                $ Sabia.face = "irritated2"
                                $ Avion.face = "smirk"
                                $ Avion.face = "happy"
                                avion "Your obedience makes me think you might make a fine pleasure slave."
                                $ Avion.face = "smirk"
                                avion "Not of quality enough for Naltaan. But... perhaps one of the smaller cities."
                                $ Avion.face = "normal"
                                avion "Come to me when you are ready to watch a true warrior."
                                jump ef3_kira_camp
                            "No - alternative.":
                                $ avion_dom += 1
                                $ Sabia.face = "irritated1"
                                "Sabia shook her head."
                                $ Sabia.face = "normalopen"
                                s "No. There's no need for a head on charge just yet. I am sure there's an easier way."
                                $ Sabia.face = "normal"
                                $ Avion.face = "angryeyes"
                                "Avion's eyes widened for a half moment. He seemed surprised that Sabia had continued her disagreement."
                                $ Avion.face = "angry"
                                avion "Let the Gods see how odd the world truly is past the mountains. Someone like you, daring to tell me what to do. Hmph."
                                $ Avion.face = "smirk"
                                avion "If we were in Naltaan, you would be chained and clothed properly, ready to serve as a pleasure slave."
                        $ Avion.face = "normal"
                        $ Sabia.face = "closed2"
                        s "..."
                        $ Sabia.face = "normalopen"
                        s "I'll need to know where their camp is."
                        $ Sabia.face = "normal"
                        "Sabia pulled out her map, ignoring his words. There was no point trying to argue with him."
                        $ Avion.face = "angry"
                        "Avion snatched it off her."
                        avion "Here."
                        $ Avion.face = "normal"
                        "He jabbed a finger. It was almost as large as Sabia's whole hand."
                        $ Sabia.face = "annoyed2"
                        "Avion turned around, taking a seat on his log before Sabia could reply."
                        hide Avion with moveoutright
                        $ Sabia.face = "annoyed1"
                        s "Well, alright then."
                        jump ef3_kira_camp

            elif avion_quest == 4:
                if avion_quest_plan == "avion":
                    $ avion_quest_plan = "avion"
                    $ avion_quest = 5
                    $ Sabia.face = "normalopen"
                    s "Let's go. We'll do it your way."
                    $ Sabia.face = "normal"
                    avion "Good. The Gods will watch me do this."
                    jump ef3_kira_camp
                menu:
                    "Kira's task.":
                        menu avion_quest_plan_menu:
                            "Alcohol plan." if avion_quest_plan_cart == True:
                                if avion_quest_cart_acquired == False:
                                    s "I must first acquire a cart of alcohol for this plan to work."
                                    jump avion_quest_plan_menu
                                $ Sabia.face = "annoyed1"
                                s "Look. I get you're strong, and can probably take out the camp by yourself. But I have an idea that minimizes the risk."
                                $ Sabia.face = "irritated2"
                                "Avion snorted."
                                $ Sabia.face = "normalopen"
                                s "I've got a decent cart's worth of alcohol. I'll run it through the forest near them - you stay nearby, just in case."
                                s "I'll make a big deal about being noisy, and screaming that I saw a bandit, and run off. Leaving the alcohol there."
                                $ Sabia.face = "irritated2"
                                avion "This seems like a good way to lose a lot of alcohol."
                                $ Sabia.face = "normalopen"
                                s "Right. Exactly."
                                $ Sabia.face = "normal"
                                avion "..."
                                $ Sabia.face = "normalopen"
                                s "They'll take it back, and drink it - I heard the camp discussing how desperate they are for a drink."
                                s "A group of disordered, unruly bandits is bound to spend the whole night drinking with a haul like that."
                                $ Sabia.face = "happy2"
                                s "While they're out - we attack. Kill them silently."
                                $ Sabia.face = "irritated2"
                                avion "This plan is... underhanded. The Gods would not wish to watch such a thing."
                                $ Sabia.face = "normalopen"
                                $ Avion.face = "angry"
                                s "Then they can look away while we do it."
                                $ Sabia.face = "sad1"
                                "Avion's face darkened. For a moment, Sabia was afraid he would lash out with the monstrous macuahuitl he held."
                                avion "If I do not find a worthy heart, I will need something else to sate the Gods."
                                $ Sabia.face = "normal"
                                $ Avion.face = "normal"
                                menu:
                                    "Change plan.":
                                        $ avion_quest_plan_cart = False
                                        $ Sabia.face = "normalopen"
                                        s "Fine, we'll do something else."
                                        jump avion_quest_plan_menu
                                    "Alcohol plan.":
                                        $ avion_quest = 5
                                        $ avion_quest_plan = "cart"
                                        $ Sabia.face = "normalopen"
                                        s "Fine."
                                        s "I have the alcohol cart ready nearby. I'll just have to fetch it."
                                        $ Sabia.face = "normal"
                                        $ Avion.face = "smirk"
                                        "Avion snorted. Sabia took it as agreement."
                                        jump ef3_kira_camp
                            "Ambush plan." if avion_quest_plan_ambush == True:
                                if avion_quest_falsenews == False:
                                    s "I must first spread the false news to lure the bandits for this plan to work."
                                    jump avion_quest_plan_menu
                                $ avion_quest_plan = "ambush"
                                $ avion_quest = 5
                                $ Sabia.face = "normalopen"
                                s "Look. I get you're strong, and can probably take out the camp by yourself. But I have an idea that minimizes the risk."
                                $ Sabia.face = "annoyed2"
                                "Avion snorted."
                                $ Sabia.face = "normalopen"
                                s "I'll organize - don't worry how - some fake information that will be leaked to their bandit camp."
                                s "They'll expect a very juicy target moving through the forest too close to them. One that they can't afford to not hit."
                                $ Sabia.face = "normal"
                                $ Avion.face = "smirk"
                                avion "I am listening."
                                $ Sabia.face = "normalopen"
                                s "Right. So, they'll be set up throughout the forest, ready to ambush it."
                                $ Avion.face = "normal"
                                s "We can split up, and pick them off until there are none left."
                                $ Sabia.face = "normal"
                                $ Avion.face = "angry"
                                avion "It would be better if the Gods were to watch a proper confrontation."
                                $ Avion.face = "smirk"
                                avion "But I agree, if only so we can finish this all the quicker and I can go back to not dealing with you."
                                $ Sabia.face = "normalopen"
                                $ Avion.face = "normal"
                                s "Agreed."
                                s "I'll be back when we are ready to go."
                                $ Sabia.face = "normal"
                                $ Avion.face = "happy"
                                avion "Perhaps I will even find a worthy heart during the fight."
                                $ Avion.face = "normal"
                                "Avion snorted."
                                jump ef3_kira_camp
                            "Decide later.":
                                jump ef3_kira_camp

            elif avion_quest == 5:
                menu:
                    "Proceed with the plan." if avion_quest_plan == "ambush":
                        jump ef3_rival_camp_ambush
                    "Proceed with the plan." if avion_quest_plan == "cart" and avion_quest_cart_deployed == False:
                        if Sabia.armor == Rags or Sabia.armor == Orcslavearmor:
                            $ Sabia.face = "normalopen"
                            s "(I probably shouldn't wear this, actually. I should change to something a struggling merchant might wear.)"
                            jump ef3_kira_camp
                        jump ef3_rival_camp_cart
                    "Go back to the rival bandits' camp." if avion_quest_plan == "cart" and avion_quest_cart_deployed == True:
                        jump ef3_rival_camp_cart2
                    "Let's go." if avion_quest_plan == "avion":
                        jump ef3_rival_camp_avion

            elif avion_quest > 5:
                if avion_quest_bandit_freed == True and sub>dom:
                    $ Avion.face = "smirk"
                    "Avion glanced at Sabia. His eyes did a quick roam up and down her frame, and his lips curled in a smirk that told Sabia everything he was imagining."
                elif avion_quest_bandit_freed == True and dom>sub:
                    "Avion met Sabia's gaze and gave a short nod. It was as respectful as he had been towards her since she had met him."
                menu:
                    "Talk.":
                        if sub>dom:
                            $ Avion.face = "smirk"
                            avion "I have no need to talk with you. When I wish to speak, you will know."
                        else:
                            "Avion gave Sabia another short nod, and the two exchanged a few pleasantries before Sabia moved on."
                        jump ef3_kira_camp
                    "Leave.":
                        jump ef3_kira_camp
            else:

                "He snorted, steam billowing from his nostrils."
                $ Sabia.face = "annoyed1"
                s "...alright, then."
                jump ef3_kira_camp

        "Talk to human" if kira_camp_jarredtalk == 0 and kira_quest_testskill_done == True:
            show Sabia at left
            show Humansoldier at right
            with dissolve
            $ kira_camp_jarredtalk = 1
            $ mariana_hint3 = True
            $ Humansoldier.face = "happy"
            bandit1 "Nice to see another human joining the group. And, one that's very skilled with a blade."
            bandit1 "My name's Jarrad."
            $ Sabia.face = "normalopen"
            $ Humansoldier.face = "normal"
            s "Sabia."
            bandit1 "Not to sound too much like Kira, but, where did you learn to fight?"
            $ Sabia.face = "normalopen"
            s "My father taught me. He was... exceptionally skilled at it, amongst other things."
            $ Humansoldier.face = "sad"
            bandit1 "You don't say. I suppose Kira would feel a bit vindicated hearing that you learned it from a male."
            bandit1 "She does have that whole... 'human women are mages or useless' attitude going on."
            $ Sabia.face = "happy2"
            $ Humansoldier.face = "normal"
            s "Yeah, I did notice that a bit."
            bandit1 "You're lucky you came with that elf. Kira probably wouldn't have looked at you twice otherwise."
            $ Sabia.face = "normalopen"
            s "Kira seems... hmm. Actually, nevermind."
            $ Humansoldier.face = "sad"
            bandit1 "Harsh? Unbalanced? Cruel?"
            $ Humansoldier.face = "normal"
            bandit1 "Any one of them works well, or all of them. But that said, I've never seen anyone as skilled as her with weapons, nor as ruthless and cunning."
            $ Sabia.face = "normalopen"
            s "Is that why you signed up?"
            "Jarrad snorted."
            bandit1 "No. I signed up because it was either go back to Whitecrest and face the noose, or continue on my own with a bounty on my back."
            $ Humansoldier.face = "happy"
            bandit1 "This proved safer for my neck, and a whole lot more profitable."
            $ Sabia.face = "normalopen"
            s "Yeah... I can see that being true."
            $ Humansoldier.face = "sad"
            bandit1 "I mean, that's really the reason most of us are here, at any rate."
            bandit1 "Either outcasts from our own people, running from the law, or poor."
            $ Sabia.face = "normalopen"
            $ Humansoldier.face = "normal"
            s "I expect there are a few here that are just in it for the gold and the blood, right?"
            bandit1 "Of course. But I think most would be surprised to learn that's not the majority of us."
            bandit1 "Take me for example. Or even, Avion over there. Or Mariana, though I haven't seen Mariana lately."
            $ Sabia.face = "normalopen"
            s "Yeah, what's Avion's deal?"
            $ Sabia.face = "irritated2"
            $ Humansoldier.face = "happy"
            bandit1 "Not sure. He never really likes to talk all that much. But fuck, he can swing an axe with a blade thicker than me like it's nothing more than a toothpick."
            $ Sabia.face = "normalopen"
            s "Sounds about right. And Mariana?"
            $ Sabia.face = "normal"
            $ Humansoldier.face = "normal"
            "Jarrad shrugged."
            $ Humansoldier.face = "sad"
            bandit1 "Cute girl. She never really fit in here. Didn't like blood all that much. I think she was just too poor and too desperate to do anything else."
            $ Sabia.face = "normalopen"
            $ Humansoldier.face = "normal"
            s "It's not a life for everyone."
            $ Sabia.face = "normal"
            $ Humansoldier.face = "happy"
            bandit1 "I think you'll be fine here, if that's what you're worried about."
            if orcalliance == "dajrab":
                $ Sabia.face = "normalopen"
                s "I was just wondering. It doesn't seem like Kira is the sort to let people... slip past."
                $ Sabia.face = "normal"
                $ Humansoldier.face = "sad"
                bandit1 "No, that's true."
                bandit1 "I suppose I never really thought about it. There's more than enough to keep a mind occupied in this environment than dwelling on things like that."
                $ Humansoldier.face = "normal"
                $ Sabia.face = "normalopen"
                s "But wouldn't Kira be concerned about one of her subordinates giving away information to someone?"
                $ Sabia.face = "normal"
                $ Humansoldier.face = "happy"
                bandit1 "I guess. I'm not really one to question Kira too much."
                bandit1 "If you're looking for Mariana, I'm afraid I can't really help. I haven't seen her around for a while."
                $ Humansoldier.face = "normal"
                $ Sabia.face = "normalopen"
                s "Is that common? People deserting from here?"
                $ Sabia.face = "normal"
                $ Humansoldier.face = "sad"
                bandit1 "I mean... it's not like it doesn't happen at all. But those that join up generally have a pretty good idea of what they're getting into."
                $ Sabia.face = "normalopen"
                s "That's a good point. Well, that's for your thoughts."
                $ Humansoldier.face = "normal"
                bandit1 "That's fine. But I wouldn't let Kira hear you talking about it. She doesn't particularly look kindly on deserters."
            "Sabia nodded her understanding before leaving Jarrad."
            jump ef3_kira_camp

        "Talk to human bandit." if vehlis_shipment_quest == 1 and vsq_human_bandit == False and met_elliah_reina == True:
            $ vsq_human_bandit = True
            show Sabia at left
            show Humansoldier at right
            with dissolve
            $ Sabia.face = "normalopen"
            s "Hey, I was just wondering - and I felt like it was probably best to not ask Kira directly."
            $ Sabia.face = "irritated2"
            bandit1 "That's a good idea, hah. Sometimes Kira doesn't take too well to questions."
            $ Sabia.face = "normal"
            bandit1 "Sometimes she does, though. It's really a shot in the dark. Still, I'd rather have her leading than others I've served with."
            bandit1 "What were you after?"
            $ Sabia.face = "normalopen"
            s "I was wondering about targets we might be hitting?"
            s "Maybe some of the small human villages neighboring the orc territory?"
            $ Sabia.face = "normal"
            bandit1 "Hmm."
            bandit1 "I wouldn't think so."
            bandit1 "We've raided them enough by now, they don't really have much more to give."
            $ Sabia.face = "normalopen"
            s "It feels like Kira would find that as compelling as if they did have more loot."
            $ Sabia.face = "normal"
            bandit1 "True. But she doesn't like to strip targets too bare - and besides, I think she has her sights set on something else at the moment."
            $ Sabia.face = "happy2"
            s "Oh, what's that?"
            $ Sabia.face = "pout1"
            bandit1 "Sorry, but I'm not sure I'm comfortable saying if you don't know. Kira doesn't take too kindly to that."
            $ Sabia.face = "normalopen"
            s "Yeah, I can imagine. Thanks though."
            $ Sabia.face = "normal"
            bandit1 "Of course."
            hide Humansoldier with moveoutright
            $ Sabia.face = "normalopen"
            s "It seems like it's probably safe for the merchants to start trading again. At least from Kira."
            s "But I doubt they'll take me at my word."
            $ Sabia.face = "closed4"
            s "I could try talking to Kira about it..."
            $ Sabia.face = "normalopen"
            s "Or maybe find some orcs that don't mind a bit of work. I'm sure the merchants would feel safe with an orc escort."
            s "Maybe Bris might have some information for me."
            jump ef3_kira_camp

        "Ask bandits near fire about Mariana." if neve_mariana_info1 == True and mariana_quest == 1:
            show Sabia at left with dissolve
            $ mariana_quest = 2
            $ GenericOrc1.extras = ["Loincloth", "Axe", "Hair"]
            $ GenericOrc2.extras = ["Loincloth", "Axe", "Shoulder"]
            $ GenericOrc1.face = "normal"
            $ GenericOrc2.face = "suspicious"
            show GenericOrc1 at center
            show GenericOrc2 at right
            with dissolve
            bandit2 "Eh? What'd'yer want?"
            $ Sabia.face = "normalopen"
            s "I've just overheard a few people talking about Mariana."
            s "I was wondering if you knew where she was?"
            $ Sabia.face = "normal"
            $ GenericOrc1.face = "normalopen"
            bandit1 "Fucked if I know. Though I wish I did, ain't many girls to look at except Kira. And fuck me if she won't try and fix you for doing so."
            $ GenericOrc2.face = "normal"
            bandit2 "Why d'yer wanna know where that girl's at anyways?"
            $ Sabia.face = "happy2"
            s "Well, like your friend said. There are not many girls here. I thought I might find a bit more suitable company with another girl."
            $ GenericOrc1.face = "normal"
            bandit1 "Eh. Makes sense."
            bandit2 "Yeh, dunno though. Ain't seen her in... what, a few weeks?"
            bandit1 "I reckon about that, yeah."
            bandit2 "Dunno, ta' be 'onest. She was bein' a bit skittish before she dropped off."
            $ Sabia.face = "normalopen"
            s "Oh... that's too bad. I was really hoping I'd be able to get some company."
            $ Sabia.face = "irritated2"
            bandit2 "I'll give yer some company if yeh like, heh."
            "The bandit licked his lips and Sabia knew what he meant by 'company'."
            $ Sabia.face = "normalopen"
            s "Not quite what I was after, but thanks for the offer."
            jump ef3_kira_camp
        "Eavesdrop on bandits near the fire.":

            show Sabia at left with dissolve
            $ tempnum = renpy.random.randint(1,3)
            if tempnum == 1:
                bandit1 "A toast to 'ol Nerraz!"
                bandit2 "Nerraz!"
                bandit1 "What about the rest 'o them what got smashed by that Lustrator?"
                bandit2 "Ah, fuck 'em. I only liked Nerraz."
            elif tempnum == 2:
                bandit1 "It's been so fucking boring since we did that orc in."
                bandit2 "Tell me about it."
            elif tempnum == 3:
                if mariana_hint2 == False:
                    $ mariana_hint2 = True
                    bandit1 "Where the fuck's Mariana gone?"
                    bandit2 "No idea. But I miss her. She's always good ta' look at!"
                    bandit1 "I'd wanna do more than just look at her."
                    bandit2 "I think Kira's got her eyes on that set of tits, though."
                    bandit1 "Yeah... I guess."
                    bandit1 "Wouldn't mind seeing both sets of tits, eh? Heh!"
                    bandit2 "Be quiet, ye idiot. If Kira heard ya, yer cock would be shoved down yer throat."
                else:
                    bandit1 "The new recruits have great tits too, eh?"
            jump ef3_kira_camp
        "Leave":

            jump eastern_frontier_map


label kira_test_of_skill:
    $ Kira.face = "normalopen"
    kira "Oh, you think you're ready are you?"
    kira "Do you even have a single callus? You look soft."
    $ Kira.face = "normal"
    $ Sabia.face = "normalopen"
    s "I am not. My hands are comfortable with a blade in them."
    $ Sabia.face = "normal"
    $ Kira.face = "browsopen"
    kira "...oh, is that so? Disappointing... the soft ones always make the best sounds, you know..."
    $ Kira.face = "browsbite"
    $ Sabia.face = "irritated2"
    kira "They're not used to pain."
    $ Kira.face = "normalopen"
    kira "But you say you are? Very well."
    $ Kira.face = "normalbite"
    $ Sabia.face = "normalopen"
    s "Who am I fighting, you?"
    $ Kira.face = "browsopen"
    $ Sabia.face = "irritated1"
    kira "Mmm... hah! No. You would lose."
    $ Kira.face = "normalopen"
    kira "Come, then... we'll see how good you are."
    hide Kira with moveoutright
    "Before Sabia had a chance to reply, Kira began to walk away."
    hide Sabia with dissolve
    "Sabia followed the Vegardan as she was lead out of the main camp, and through a narrow path, trees surrounding either side of them."
    scene bg forest
    show Sabia at left
    show Kira at right
    with dissolve
    "They came to a small clearing, and Kira pushed Sabia forward with a strength that belied the elf's frame."
    "She had only a second to draw her sword before the attacker slammed into her."
    $ enemy_level = 7
    $ enemy_maxhp = 400
    $ enemy_hp = enemy_maxhp
    $ enemy_type = 1
    $ enemy_skills = [Enemyattack,Enemyattack,Enemyquickattack]
    $ enemy_attack = 65
    $ enemy_defense = 0
    $ enemy_magdefense = 0
    $ GenericOrc1.face = "angry"
    $ GenericOrc1.extras = ["Loincloth", "Axe", "Hair"]
    $ player = Sabia
    $ enemy = GenericOrc1
    call duel
    if _return != "Victory":
        show gameover with dissolve
        pause 3
        $ renpy.full_restart()
    scene bg forest
    show Sabia at left
    show Kira at right
    with dissolve
    $ Sabia.face = "happy3"
    s "I thought this was meant to be a test?"
    $ Sabia.face = "normal"
    $ Kira.face = "browsopen"
    kira "Tests often have multiple questions, do they not?"
    $ Kira.face = "browsbite"
    "Sabia's question did not go unanswered for long, another combatant charging from behind the trees."
    $ GenericOrc2.face = "angry"
    $ GenericOrc2.extras = ["Loincloth", "Helmet", "Strap", "Shoulder", "Wrists", "Axe"]
    $ enemy_skills = [Enemyattack,Enemyattack,Enemyquickattack]
    $ enemy_level = 9
    $ enemy_maxhp = 400
    $ enemy_hp = enemy_maxhp
    $ enemy_type = 3
    $ enemy_attack = 70
    $ enemy_defense = 0
    $ enemy_magdefense = 0
    $ player = Sabia
    $ enemy = GenericOrc2
    call duel
    if _return != "Victory":
        show gameover with dissolve
        pause 3
        $ renpy.full_restart()
    scene bg forest
    show Sabia at left
    show Kira at right
    with dissolve
    "Sabia spat on the ground, and looked over at Kira."
    $ Sabia.face = "normalopen"
    s "I suppose there's still more?"
    $ Sabia.face = "irritated1"
    $ Kira.face = "normalopen"
    kira "The hardest question is always at the end, isn't it? Mmm... try not to fail too badly."
    $ Kira.face = "browsopen"
    kira "I don't want that face damaged... before I get a turn at it."
    $ GenericOrc1.face = "angry"
    $ GenericOrc1.extras = ["Loincloth", "Axe"]
    $ enemy_skills = [Preparation, PreparedstrikeI, Enemyattack]
    $ enemy_level = 11
    $ enemy_maxhp = 400
    $ enemy_hp = enemy_maxhp
    $ enemy_type = 2
    $ enemy_attack = 70
    $ enemy_defense = 0
    $ enemy_magdefense = 0
    $ player = Sabia
    $ enemy = GenericOrc1
    call duel
    if _return != "Victory":
        show gameover with dissolve
        pause 3
        $ renpy.full_restart()
    scene bg forest
    show Sabia at left
    show Kira at right
    with dissolve
    play music forest fadeout 2.0 fadein 2.0
    "After Sabia finished the last round, her brow was wet with sweat and loose strands of hair clung to her."
    $ Kira.face = "irritatedopen"
    $ Sabia.face = "irritated2"
    kira "Hmm. I suppose Neve was not wrong... you can fight."
    kira "Though I shouldn't be surprised, if she vouched for you. If someone with all that white says it, after all..."
    $ Kira.face = "normal"
    $ Sabia.face = "normalopen"
    s "All that white? What do you mean?"
    $ Kira.face = "normalopen"
    $ Sabia.face = "irritated2"
    kira "You don't know? It's a secret, then!"
    kira "You still have another test before I accept you."
    hide Kira with moveoutright
    "And with the abrupt change of tone, Kira turned and left as abruptly."
    $ kira_quest_testskill_done = True
    $ kira_quest += 1
    jump ef3_kira_camp


label kira_test_of_cunning:
    "Kira paused for a moment, her eyes flickering over Sabia's frame."
    $ Kira.face = "browsopen"
    $ Sabia.face = "irritated2"
    kira "Are you sure you're going to be... capable of that?"
    kira "I know human magi are quite cunning, but if you've given up on that path..."
    $ Kira.face = "normal"
    $ Sabia.face = "normalopen"
    s "I'm sure. I may not be a mage, but I know how they think. I know how to do what needs to be done."
    $ Sabia.face = "irritated2"
    "Kira shrugged."
    $ Kira.face = "normalopen"
    kira "Alright then."
    $ Kira.face = "normal"
    $ Sabia.face = "normalopen"
    s "What's the test, then?"
    $ Kira.face = "normalopen"
    $ Sabia.face = "normal"
    kira "There's a trade route from Lundar that runs through to Whitecrest."
    kira "And usually it's just boring old food and grain, and whatever else regular Lundarian and Whitecrest citizens need daily."
    $ Kira.face = "normal"
    $ Sabia.face = "normalopen"
    s "I feel a 'but' coming on."
    $ Kira.face = "normalopen"
    $ Sabia.face = "irritated2"
    kira "Instead of something usual, though, we've managed to get some information about a particularly delectable target."
    kira "We will set up an ambush some way ahead of the trade route. You will determine which is the correct target."
    $ Kira.face = "normal"
    $ Sabia.face = "normalopen"
    s "That seems risky. Why let someone new do something like this?"
    $ Kira.face = "irritatedopen"
    $ Sabia.face = "irritated2"
    kira "You're not doing well for a test of cunning already if you have to ask that."
    kira "A valuable target means more protection, more preparation on the trader's part. We can't risk any of them recognizing us."
    $ Kira.face = "normal"
    $ Sabia.face = "normalopen"
    s "I see."
    s "How am I to determine which caravan is the correct one, then?"
    $ Kira.face = "irritatedopen"
    $ Sabia.face = "irritated1"
    kira "You're not listening. I just told you."
    $ Kira.face = "browsopen"
    kira "Maybe it would be better to teach you to listen properly... hmm."
    kira "Perhaps not yet. I will see if you are worth keeping... unbroken."
    $ Kira.face = "browsbite"
    "The next few hours were spent in a bustle as everyone in the bandit camp prepared. They then left, Kira leading the way."
    scene bg black with dissolve
    pause (0.01)
    scene bg countryside
    show Sabia at left
    with dissolve
    "The road rolled over a multitude of hills, giving several viable vantage points. Sabia chose one of them, and the rest of the bandits moved on ahead."
    "It would give her a clear view of all caravans and travelers coming, and give her more than enough time to start walking along ahead of them, so as to give the illusion she was travelling as well."
    "She noticed that Neve had not been with the bandit group, and wondered where she had been. She surmised it was likely she had gone off to do something her own, once more."
    "Sabia really had no idea how long it would take for any caravans to come along, let alone the correct one. She lay down."
    "There was enough of an incline on the hill that she would be able to see any travelers with ease."
    "The lateness of the night wore on, and a rustling behind Sabia jolted her back to attention."
    $ Kia.face = "normal1"
    show Kia at right with moveinright
    $ Kia.face = "pawuncertain1"
    kia "Hi Sabia! What doing?"
    $ Sabia.face = "happy3"
    s "Kia! I had not expected to see you out here."
    $ Sabia.face = "normal"
    $ Kia.face = "happy2"
    kia "Kia see Sabia. Kia follow!"
    kia "Sabia not do anything?"
    $ Kia.face = "normal1"
    "The makhor leaned in and sniffed Sabia, her twitching nose brushing against Sabia's skin."
    $ Kia.face = "normal2"
    kia "Smell like a lot."
    $ Sabia.face = "normalopen"
    s "A lot what?"
    $ Sabia.face = "normal"
    kia "A lot!"
    $ Sabia.face = "pout1"
    s "That... doesn't really help Kia."
    $ Sabia.face = "normal"
    $ Kia.face = "tilt2"
    kia "...Sabia one. Sabia and Kia two."
    $ Kia.face = "normal1"
    kia "Sabia smell like a lot!"
    $ Sabia.face = "normalopen"
    s "I have a lot of people's scents on me?"
    $ Sabia.face = "normal"
    $ Kia.face = "happy3"
    kia "A lot!"
    "Kia's exclamation was more insistent now, and she pressed her head against Sabia's own, sniffing some more."
    $ Sabia.face = "normalopen"
    s "Yes, I'm with some... friends, and we're trying to ambush a caravan."
    $ Sabia.face = "normal"
    $ Kia.face = "uncertain2"
    kia "..."
    $ Kia.face = "tilt2b"
    kia "Cravavan? Ambush?"
    $ Sabia.face = "normalopen"
    s "Ambush should be easy for you to get - it's when you're hiding, following some prey and then attack when they aren't ready."
    $ Kia.face = "happy3"
    kia "Kia like ambush!"
    $ Sabia.face = "eyebrow1"
    $ Kia.face = "pawtiltconfused"
    kia "What cravavan?"
    $ Sabia.face = "happy3"
    s "Cah-rah-van."
    $ Sabia.face = "normal"
    "Kia frowned, her brows furrowing."
    $ Kia.face = "happy2"
    kia "Cra-va-van!"
    $ Sabia.face = "normalopen"
    $ Kia.face = "happy1"
    s "Not quite... but close enough."
    s "Remember that group of orcs that you attacked, and they were with a big thing with wheels? That's a caravan."
    s "There will be a few caravans coming along this road soon enough, and one of them has something very valuable in it. So we're going to ambush it, and take it."
    $ Sabia.face = "normal"
    "Kia took a moment to process the information."
    $ Kia.face = "tilt2b"
    kia "...Sabia hunt not food?"
    $ Sabia.face = "normalopen"
    $ Kia.face = "normal1"
    s "Hmm, I suppose it is a lot like hunting."
    s "And speaking of... here comes a caravan now."
    s "I'll be back shortly if you wait here."
    $ Sabia.face = "normal"
    $ Kia.face = "tilt2b"
    kia "Help Sabia?"
    $ Sabia.face = "normalopen"
    $ Kia.face = "normal1"
    s "No thanks Kia, I'll be fine by myself for this."
    hide Sabia with moveoutleft
    "Kia gave a little huff, and sat herself down on the hill as Sabia walked over to the road."
    scene bg black with dissolve
    pause (0.01)
    scene bg roadcaravan
    show Sabia at left
    with dissolve
    "She was there a good fifteen minutes before the caravan crested the hill and started trundling downward."
    "The caravan creaked up and started rolling alongside Sabia."
    "Sabia gave a few glances as the horses slowed next to her. It was an elderly man, and his 'caravan' was nothing more than an open cart."
    "Still, she had to double check."
    $ Sabia.face = "normalopen"
    s "It's a bit late for traveling, isn't it?"
    m1 "Bit nosy to be asking about my route."
    $ Sabia.face = "normal"
    s "I just meant it's still quite late, most travelers take the night to sleep."
    m1 "Hmph. Why aren't you sleeping, then, eh?"
    $ Sabia.face = "irritated2"
    "Sabia shrugged."
    $ Sabia.face = "normalopen"
    s "Sometimes necessity dictates cutting my sleep a bit short."
    $ Sabia.face = "normal"
    "The merchant gave a harsh bark of laughter."
    m1 "Sounds about right. Would be nice to get a proper night's sleep."
    m1 "But I prefer being in a city for that sleep, rather than on the road."
    $ Sabia.face = "irritated2"
    "Sabia could see him giving her a wary glance, and his fingers tightening about the reins."
    "His hands were callused, from what Sabia could see in the strong moonlight, but not from a sword or a weapon."
    "She could hear the rustling of grain and maize in large sacks on the back of his caravan."
    m1 "I think I might hurry on a bit faster, and see if I can't get that sleep."
    "He gave a bit more slack to the reins, and the pair of large workhorses picked up a bit of speed, passing Sabia."
    $ Sabia.face = "closed2"
    s "Hmm..."
    $ Sabia.face = "normalopen"
    s "It's obvious that's not the correct caravan, I had better wait to see what else comes along."
    hide Sabia with moveoutleft
    "Sabia hiked back up the hill, where Kia was waiting for her, a look of confusion on her face."
    scene bg black with dissolve
    pause (0.01)
    scene bg countryside
    show Sabia at left
    show Kia at right
    with dissolve
    $ Kia.face = "pawtiltconfused"
    kia "No eat cravavan?"
    $ Sabia.face = "normalopen"
    s "That wasn't the right one - at least, I'm fairly certain it was not."
    $ Kia.face = "happy3"
    kia "Hunt cravavan. Eat cravavan."
    $ Sabia.face = "happy2"
    $ Kia.face = "tilt1b"
    s "It would be nice if it were that simple Kia, but I need a specific caravan. If I get the wrong caravan, the correct one might hear or see something."
    $ Sabia.face = "normalopen"
    s "They might then be able to better prepare, or divert their course and our ambush becomes useless."
    $ Sabia.face = "normal"
    kia "..."
    hide Sabia with moveoutleft
    "Another caravan crested the hill after a while and Sabia did as she did before, heading down to the road."
    "The wheels of the caravan creaked as it approached."
    "Sabia settled into a slightly faster gait as the caravan slowed just a little."
    jump kira_test_of_cunning_caravans


label kira_test_of_cunning_caravans:
    $ tempnum = renpy.random.randint(1,3)
    if kira_test_of_cunning_caravan1_done == True and kira_test_of_cunning_caravan2_done == True and kira_test_of_cunning_caravan3_done == True:
        jump kira_test_of_cunning_badend
    if tempnum == 1 and kira_test_of_cunning_caravan1_done == False:
        $ kira_test_of_cunning_caravan1_done = True
        jump kira_test_of_cunning_caravans_1
    elif tempnum == 2 and kira_test_of_cunning_caravan2_done == False:
        $ kira_test_of_cunning_caravan2_done = True
        jump kira_test_of_cunning_caravans_2
    elif tempnum == 3 and kira_test_of_cunning_caravan3_done == False:
        $ kira_test_of_cunning_caravan3_done = True
        jump kira_test_of_cunning_caravans_3
    else:
        jump kira_test_of_cunning_caravans


label kira_test_of_cunning_caravans_1:
    scene bg black with dissolve
    pause (0.01)
    scene bg roadcaravan
    show Sabia at left
    with dissolve
    menu test_caravan1:
        "Greet the driver." if test_caravan1_greet == False:
            $ test_caravan1_greet = True
            $ Sabia.face = "happy2"
            s "Hello!"
            $ Sabia.face = "irritated2"
            m1 "Hmph. Great. A traveler on the road that wants to talk."
            $ Sabia.face = "happy2"
            s "Why not? It's a long road, and it gets boring by oneself."
            $ Sabia.face = "normal"
            m1 "Lucky for me then I ain't alone."
            $ Sabia.face = "normalopen"
            s "Oh? I just thought you were, because-"
            $ Sabia.face = "normal"
            m1 "Because you can't see anyone else. Well duh, you don't need to explain it. It's obvious."
            $ Sabia.face = "normalopen"
            s "Who else is with you?"
            $ Sabia.face = "irritated2"
            m1 "Bit rude as well, ain't you?"
            m1 "Me son's napping."
            m1 "It was nice having some peace 'n quiet while he did so."
            "Sabia caught on to him not really wanting to chat anymore."
            jump test_caravan1
        "Try to inspect the driver." if test_caravan1_inspect == False:
            $ test_caravan1_inspect = True
            "Sabia snuck a few glances over at the driver as they moved along the road."
            "He looked around middle-aged, though it was often hard to tell with men-of-the-road."
            "His figure wasn't extremely muscled, but she could see that he wasn't fat or entirely sedentary by any means."
            jump test_caravan1
        "Try to get a better look at the cart." if test_caravan1_cart == False:
            $ test_caravan1_cart = True
            "It's enclosed, and the shutters on the windows are closed as well."
            "The spokes on the wheels were old, and the wheels themselves looked to be in a state of disrepair, a constant creaking sound loud enough to be heard."
            "Sabia could spot that a few panels of wood had fallen off at some point, and newer ones had been nailed in to repair it, but it hadn't been done too professionally."
            jump test_caravan1
        "Is this the target caravan?" if test_caravan1_greet == True and test_caravan1_inspect == True and test_caravan1_cart == True:
            menu:
                "Yes, tell Kira.":
                    "Sabia decided that it would be best to let Kia know to head off before any fighting broke out."
                    "Hiking back up to the now-empty hill, it seemed apparent Kia had gotten tired of all waiting, and no hunting."
                    $ Sabia.face = "normalopen"
                    s "I'll need to cut across the hills to get to Kira in time."
                    "Sabia spent the better part of an hour heading over to the rendezvous point."
                    scene bg black with dissolve
                    pause (0.01)
                    scene bg countryside
                    show Sabia at left
                    show Kira at right
                    with dissolve
                    $ Kira.face = "normalopen"
                    kira "I take it you've got the right caravan, then?"
                    $ Sabia.face = "normalopen"
                    s "I do. It will be along shortly, and we'll be able to ambush it."
                    $ Sabia.face = "normal"
                    $ Kira.face = "normalopen"
                    kira "Excellent. They've a prize that will be worth a great deal."
                    scene bg black with dissolve
                    pause (0.01)
                    scene bg countryside
                    show Sabia at left
                    show Kira at right
                    with dissolve
                    "They waited another few hours for the caravan to slowly trundle along, and Sabia indicated which one it was."
                    $ Kira.face = "browsbite"
                    $ Sabia.face = "sad1"
                    "Kira gave a short click of her tongue, and shook her head."
                    $ Sabia.face = "normalopen"
                    s "What's wrong?"
                    $ Kira.face = "browsopen"
                    $ Sabia.face = "surprised1"
                    kira "That's not the right one at all."
                    $ Kira.face = "browsbite"
                    $ Sabia.face = "surprised3"
                    s "What? But I-"
                    $ Kira.face = "browsopen"
                    $ Sabia.face = "sad1"
                    kira "Oh, my sweet warrior, don't fret. I'm not upset. I'm not even disappointed. We knew which caravan we needed to target."
                    kira "I was hoping you'd fail..."
                    $ Kira.face = "browsbite"
                    $ Sabia.face = "surprised1"
                    "Kira's fingers gripped her spear tighter, and the point flashed in the red light of the dusk, darting straight toward Sabia."
                    show Kira:
                        linear 1.0 xoffset -300
                    scene bg black with dissolve
                    pause (0.5)
                    kira "Dear, oh dear... it's too bad Neve wasn't around to help you when you failed my test of skill... maybe she might have been able to rescue you...?"
                    kira "Would you have liked that, my lovely little warrior? I suppose we just won't know... hmm."
                    call kira_bandits_badend
                    show gameover with dissolve
                    pause 3
                    $ renpy.full_restart()
                "No, wait for another caravan.":
                    $ Sabia.face = "closed4"
                    s "I don't think that's the correct caravan."
                    $ Sabia.face = "annoyed1"
                    s "It would be easier if I knew what I was looking for."
                    $ Sabia.face = "normalopen"
                    s "But, this looked like nothing more than an old, grumpy man that was trying to get his work done."
                    s "That, and the rather lackluster state of his caravan - it's almost certainly not the type of transport something of value would see."
                    if kira_test_of_cunning_caravan1_done == True and kira_test_of_cunning_caravan2_done == True and kira_test_of_cunning_caravan3_done == True:
                        jump kira_test_of_cunning_badend
                    scene bg black with dissolve
                    pause (0.01)
                    scene bg countryside
                    show Sabia at left
                    with dissolve
                    "Sabia hiked back up the hill, but Kia was gone."
                    "Leaves and trees rustled, and twigs snapped underhoof as a frightened deer dashed through the open, towards the shelter of another thicket of trees."
                    "Kia emerged a few seconds after, smiling."
                    $ Kia.face = "happy2"
                    show Kia at right with moveinright
                    kia "Sabia, sit!"
                    "The makhor practically bounced over to Sabia, and pushed her down onto the ground, taking a seat next to her."
                    $ Sabia.face = "normalopen"
                    s "It got away."
                    $ Sabia.face = "normal"
                    $ Kia.face = "irritated2"
                    "Kia huffed."
                    kia "No."
                    s "No? It's off somewhere over there."
                    $ Kia.face = "normal1"
                    kia "Kia fun. Not eat."
                    kia "Not get away."
                    $ Sabia.face = "normalopen"
                    s "Somehow I'm not sure if the deer saw it quite the same way..."
                    hide Sabia with moveoutleft
                    "Another caravan crested the hill after a while and Sabia did as she did before, heading down to the road."
                    "The wheels of the caravan creaked as it approached."
                    "Sabia settled into a slightly faster gait as the caravan slowed just a little."
                    jump kira_test_of_cunning_caravans


label kira_test_of_cunning_caravans_2:
    scene bg black with dissolve
    pause (0.01)
    scene bg roadcaravan
    show Sabia at left
    with dissolve
    menu test_caravan2:
        "Greet the driver." if test_caravan2_greet == False:
            $ test_caravan2_greet = True
            $ Sabia.face = "happy3"
            s "Hello!"
            $ Sabia.face = "normal"
            m1 "Hi!"
            m1 "What brings you out on a road like this with no horse?"
            $ Sabia.face = "normalopen"
            s "Horses are expensive unfortunately. Plus the care and the feed."
            $ Sabia.face = "happy2"
            s "Sometimes it's just easier to travel by foot."
            $ Sabia.face = "normal"
            m1 "Oh, I don't know if I agree with that. But then again, I don't think either of us would be able to carry all our wares by ourselves."
            m1 "Isn't that right sweetie?"
            "The merchant paused, looking over at the elderly woman sitting next to him on the cart's front."
            m2 "Hmm?"
            m1 "I said, isn't that right?"
            m2 "Oh, yes! Of course, dear. Very right."
            m1 "Hmm... a young lady like yourself on the road alone. That's not good at all! Why don't you join us?"
            m1 "We're going as far as Whitecrest, before turning back."
            m2 "Really, dear, I don't think that-"
            m1 "Shush!"
            $ Sabia.face = "happy3"
            s "Oh, no thank you. I'm quite fine. I wouldn't want to impose. Thank you for the offer, though."
            s "I might just walk along with you for a bit longer."
            jump test_caravan2
        "Inspect the couple." if test_caravan2_inspect == False:
            $ test_caravan2_inspect = True
            "Sabia could see that the two were either extremely good actors, or they were genuinely a married couple."
            "They had that air about them."
            "She very much doubted whether the woman could even pick up a dagger, let alone something more dangerous."
            "And the man looked like he might have been strong once, but muscle had slowly left as he aged."
            "Sabia couldn't spot any weapons on them at all."
            jump test_caravan2
        "Try to get a better look at the cart." if test_caravan2_cart == False:
            $ test_caravan2_cart = True
            "Their cart looked like it was well cared for. None of the wheels creaked, and they looked fairly undamaged."
            "The panels themselves were well-varnished, and sturdy. No rot at all."
            "The pair of horses pulling it seemed almost as old as they did, and Sabia doubted they'd be able to do a long burst of speed."
            jump test_caravan2
        "Is this the target caravan?" if test_caravan2_greet == True and test_caravan2_inspect == True and test_caravan2_cart == True:
            menu:
                "Yes, tell Kira.":
                    "Sabia decided that it would be best to let Kia know to head off before any fighting broke out."
                    "Hiking back up to the now-empty hill, it seemed apparent Kia had gotten tired of all waiting, and no hunting."
                    $ Sabia.face = "normalopen"
                    s "I'll need to cut across the hills to get to Kira in time."
                    "Sabia spent the better part of an hour heading over to the rendezvous point."
                    scene bg black with dissolve
                    pause (0.01)
                    scene bg countryside
                    show Sabia at left
                    show Kira at right
                    with dissolve
                    $ Kira.face = "normalopen"
                    kira "I take it you've got the right caravan, then?"
                    $ Sabia.face = "normalopen"
                    s "I do. It will be along shortly, and we'll be able to ambush it."
                    $ Sabia.face = "normal"
                    $ Kira.face = "normalopen"
                    kira "Excellent. They've a prize that will be worth a great deal."
                    scene bg black with dissolve
                    pause (0.01)
                    scene bg countryside
                    show Sabia at left
                    show Kira at right
                    with dissolve
                    "They waited another few hours for the caravan to slowly trundle along, and Sabia indicated which one it was."
                    $ Kira.face = "browsbite"
                    $ Sabia.face = "sad1"
                    "Kira gave a short click of her tongue, and shook her head."
                    $ Sabia.face = "normalopen"
                    s "What's wrong?"
                    $ Kira.face = "browsopen"
                    $ Sabia.face = "surprised1"
                    kira "That's not the right one at all."
                    $ Kira.face = "browsbite"
                    $ Sabia.face = "surprised3"
                    s "What? But I-"
                    $ Kira.face = "browsopen"
                    $ Sabia.face = "sad1"
                    kira "Oh, my sweet warrior, don't fret. I'm not upset. I'm not even disappointed. We knew which caravan we needed to target."
                    kira "I was hoping you'd fail..."
                    $ Kira.face = "browsbite"
                    $ Sabia.face = "surprised1"
                    "Kira's fingers wrapped gripped her spear tighter, and the point flashed in the red light of the dusk, darting straight toward Sabia."
                    show Kira:
                        linear 1.0 xoffset -300
                    scene bg black with dissolve
                    pause (0.5)
                    kira "Dear, oh dear... it's too bad Neve wasn't around to help you when you failed my test of skill... maybe she might have been able to rescue you...?"
                    kira "Would you have liked that, my lovely little warrior? I suppose we just won't know... hmm."
                    call kira_bandits_badend
                    show gameover with dissolve
                    pause 3
                    $ renpy.full_restart()
                "No, wait for another caravan.":
                    $ Sabia.face = "closed4"
                    s "I don't think that's the correct caravan."
                    $ Sabia.face = "annoyed1"
                    s "It would be easier if I knew what I was looking for."
                    $ Sabia.face = "normalopen"
                    s "They were simply a friendly, old couple. Perhaps a little bit too friendly."
                    s "Definitely not the sort of people that would be guarding a valuable transport route."
                    if kira_test_of_cunning_caravan1_done == True and kira_test_of_cunning_caravan2_done == True and kira_test_of_cunning_caravan3_done == True:
                        jump kira_test_of_cunning_badend
                    scene bg black with dissolve
                    pause (0.01)
                    scene bg countryside
                    show Sabia at left
                    show Kia at right
                    with dissolve
                    "Sabia hiked back up the hill."
                    "Kia was sprawled out on the grass, looking up to the sky."
                    "She groaned."
                    $ Kia.face = "irritated2"
                    kia "Sabia take long."
                    kia "Not fun!"
                    "She rolled over onto her stomach, and over again."
                    $ Kia.face = "tilt1b"
                    kia "When done?"
                    $ Sabia.face = "normalopen"
                    s "I don't know Kia. When the right caravan comes along."
                    s "If you're bored, you don't have to stay... Kia..."
                    hide Kia with moveoutright
                    $ Sabia.face = "normal"
                    "Sabia's words trailed off as Kia grinned, darting off into the forest like a blur."
                    "She wasn't sure if Kia would be back or not."
                    hide Sabia with moveoutleft
                    "Another caravan crested the hill after a while and Sabia did as she did before, heading down to the road."
                    "The wheels of the caravan creaked as it approached."
                    "Sabia settled into a slightly faster gait as the caravan slowed just a little."
                    jump kira_test_of_cunning_caravans


label kira_test_of_cunning_caravans_3:
    scene bg black with dissolve
    pause (0.01)
    scene bg roadcaravan
    show Sabia at left
    with dissolve
    menu test_caravan3:
        "Greet the driver." if test_caravan3_greet == False:
            $ test_caravan3_greet = True
            $ Sabia.face = "normalopen"
            s "Hello!"
            m1 "Good day."
            $ Sabia.face = "closed2"
            s "(...not one for much conversation.)"
            $ Sabia.face = "normalopen"
            s "It's always good to have a bit of company on the road, don't you think?"
            $ Sabia.face = "normal"
            m1 "Can be. Depends on the company, doesn't it?"
            $ Sabia.face = "happy3"
            s "Your company?"
            $ Sabia.face = "normal"
            m1 "Not many that would say I'm good for that."
            m1 "But if you feel like following along while my beasts take a breather, feel free I guess."
            "The driver gave a few side glances towards Sabia as they moved forward on the road."
            jump test_caravan3
        "Try to inspect the driver." if test_caravan3_inspect == False:
            $ test_caravan3_inspect = True
            "Sabia could see that the driver was tough. He had a few scars that were visible on his arms and one on his face."
            "Though, at the same time, she couldn't see any weapon anywhere."
            "She had trouble judging whether he was muscled, or it was just a few layers of clothes over his upper arms and torso."
            "He certainly wasn't the sort that she would be surprised at seeing on a caravan route, however."
            jump test_caravan3
        "Try to get a better look at the cart." if test_caravan3_cart == False:
            $ test_caravan3_cart = True
            "The caravan was reasonably large, and seemed in good condition."
            "The only thing that immediately stood out to Sabia was the horses pulling it."
            "They were large, and powerful. She had definitely seen merchants with horses like that before, though it was far less often than more common breeds."
            "They would be expensive beasts as well."
            jump test_caravan3
        "Is this the target caravan?" if test_caravan3_greet == True and test_caravan3_inspect == True and test_caravan3_cart == True:
            menu:
                "Yes, tell Kira.":
                    $ kira_quest_testcunning_done = True
                    $ kira_quest += 1
                    $ Sabia.face = "normalopen"
                    s "Well, enjoy your travels."
                    $ Sabia.face = "normal"
                    m1 "Thanks. I'd offer you a ride, but, I can see you know how to handle yourself."
                    $ Sabia.face = "normalopen"
                    s "What do you mean?"
                    m1 "That tattoo."
                    $ Sabia.face = "normalopen"
                    s "My tattoo? I'm surprised a merchant knows about... wait a second."
                    $ Sabia.face = "irritated1"
                    m1 "Ah, fuck!"
                    "The driver swore loudly to himself, recognizing the potential threat to his cargo, he gripped the reins tight."
                    "Sabia was one step ahead, she had realized her mistake as she was speaking, and was already pulling herself up onto the trundling cart."
                    "She lunged over, and knocked the driver off the seat. The inertia carried Sabia tumbling down after him."
                    m1 "OI! Get out here!"
                    show Humansoldier at center
                    show Humansoldier as HS2 at right
                    show Humansoldier as HS3:
                        anchor (0.0,1.0) pos (0.7,1.0)
                    with moveinright
                    "The door at the back of the carriage burst open, and three soldiers rushed out."
                    "Sabia's blade had already finished the driver by the time the others had reached her."
                    "The horses, clearly used to fighting, weren't spooked but nonetheless trot a little bit away from Sabia and the soldiers."
                    "Steel against steel rang out in the open as Sabia parried, blocked, riposted."
                    "She was good, better than any one of the soldiers. But she wasn't good enough against three."
                    "A few strikes got through, their blades grazing against her arm or leg and leaving a trail of red behind."
                    "Sabia's blade rose up to block an overhand strike. Out of the corner of her eye she saw one of them circling around the back, and the blade lunging for her."
                    show Kia behind Humansoldier:
                        anchor (0.0,1.0) pos (0.7,1.0)
                    with moveinright
                    hide HS3 with dissolve
                    "His scream sent ravens to the air. He crumpled to the ground in a whimpering mess. His back was lacerated, skin parted easily by Kia's claws."
                    $ Kia.face = "power1"
                    kia "Hunt!"
                    "Kia growled, the scent of blood strong on her nose."
                    "The two other soldiers had clearly never been at the wrong end of a makhor, Sabia realized. They had taken a few steps back as Kia rounded on them."
                    "Even still, they knew enough that they wouldn't be able to outrun Kia."
                    "They lunged forward."
                    "Sabia watched Kia's body move. The power in every movement was evident, and Kia's speed was blinding."
                    "Claws deflected a blade easily, Kia's other paw sinking deep into a stomach."
                    show Kia at right with move
                    hide HS2 with dissolve
                    "The man let out a soft exhale, not even a scream managing to escape his lips as Kia ripped through his body, claws slicing upward."
                    "He, too fell to the ground, eviscerated. Sabia could see intestines and insides falling out of him."
                    "The last soldier's face went pale at what Kia had done to his comrade."
                    hide Humansoldier with moveoutleft
                    "Courage failing, he dropped his sword and turned. Sabia knew that he couldn't outrun Kia, and she suspected that he knew that as well."
                    hide Kia with moveoutleft
                    "He managed a few feet before Kia's full weight slammed into his back, and they both hit the ground and rolled over a few times."
                    "A trail of blood, flesh and organs painted the grass."
                    show Kia at right with moveinright
                    $ Kia.face = "happy3x"
                    kia "Good hunt."
                    $ Kia.face = "happy3"
                    "Sabia knew Kia could be dangerous. But somehow seeing it first hand like that, well, it was... something else."
                    $ Kia.face = "tilt2b"
                    kia "...Sabia hurt?"
                    $ Sabia.face = "normalopen"
                    s "Uhm, no, Kia, I think I'm fine. Thanks. I don't know if I could have managed to take on all three myself."
                    $ Sabia.face = "normal"
                    $ Kia.face = "happy2"
                    kia "Kia happy! Help Sabia."
                    kia "Eat now."
                    $ Sabia.face = "surprised3"
                    s "Wait, I don't think-"
                    $ Sabia.face = "surprised1"
                    "Kia looked like she was going to ignore Sabia's protest for a moment, looming over one of the bodies before she glanced up at Sabia."
                    $ Kia.face = "tiltirritated"
                    $ Sabia.face = "sad1"
                    kia "Hunt. Kill. Eat."
                    kia "Why no eat?"
                    $ Sabia.face = "normalopen"
                    s "Well, it's just that... I need them to think that I did this, and if you start taking chunks of them."
                    $ Kia.face = "tilt1b"
                    kia "Kia kill..."
                    $ Sabia.face = "normalopen"
                    s "Yes, I know. But, please, Kia. Trust me on this one."
                    $ Sabia.face = "normal"
                    "Kia frowned, clearly not understanding Sabia's position."
                    "Still, she had enough trust in Sabia to restrain herself from indulging her hunger."
                    $ Kia.face = "uncertain2"
                    kia "Okay..."
                    "Sabia sighed in relief."
                    $ Sabia.face = "happy3"
                    s "Thank you Kia."
                    s "Well, no need for that ambush now, I suppose. I may as well just have a look at what's in here."
                    $ Sabia.face = "normal"
                    $ Kia.face = "normal1"
                    "Rifling through what was left, Sabia didn't find much."
                    "Until she came to a small pouch."
                    "Thinking it might have some pearls, jewels, or maybe just some ingots of gold, she opened it."
                    $ Sabia.face = "surprised3"
                    s "What?!"
                    $ Sabia.face = "normalopen"
                    s "This is not what I was expecting... interesting."
                    $ Sabia.face = "normal"
                    "A few small stones tumbled into her hand. They thrummed with a soft power. Most people wouldn't notice it. But Sabia had grown up around her mother and sister."
                    "Even if she hadn't followed in Tyra's footsteps."
                    $ Sabia.face = "normalopen"
                    s "And what's more... an item like this. No one's going to let information about a trade or delivery like this slip."
                    s "Which begs the question... did Kira know what this caravan held, or did she just know that it held something valuable?"
                    $ Sabia.face = "closed4"
                    s "And if the former... how did Kira find out about this? And who let the information slip? And why?"
                    $ Sabia.face = "irritated2"
                    "Sabia frowned as she rolled the stones about in her hand. Their potent magical potential practically buzzed in the air."
                    $ Kia.face = "uncertain1"
                    kia "What doing?"
                    $ Sabia.face = "normalopen"
                    s "Nothing, Kia."
                    kia "What is?"
                    kia "Can smell! Smell like..."
                    $ Kia.face = "irritated2"
                    "Kia frowned, and pushed herself into the small space. The front of her body was dripping with red, and it rubbed over Sabia."
                    $ Kia.face = "irritated3"
                    "She took another sniff of it. Her eyes narrowed, and she hissed at it, pulling back quickly."
                    kia "Sabia keep."
                    $ Kia.face = "irritated2"
                    $ Sabia.face = "normalopen"
                    s "I'm not sure I want them either. Regardless, I need to give them to... a friend, Kia. If I'm to follow this lead to where it ends."
                    s "Thank you for the help, Kia. I'll talk to you later?"
                    $ Kia.face = "pawtiltconfused"
                    kia "Hunt finished?"
                    $ Sabia.face = "normalopen"
                    s "Yes."
                    $ Kia.face = "normal1"
                    $ Sabia.face = "normal"
                    kia "Hmm... okay. Bye!"
                    hide Kia with moveoutright
                    "Kia bounded off, but not without a brief moment where she gave the stones another wary look. Sabia had been lucky Kia had shown up."
                    "Sabia, with stones in hand, made her way to the ambush site."
                    scene bg black with dissolve
                    pause (0.01)
                    scene bg countryside
                    show Sabia at left
                    show Kira at right
                    with dissolve
                    $ Kira.face = "normalopen"
                    kira "Is the next caravan the target, then?"
                    "Sabia threw the pouch to Kira. The elf caught it."
                    $ Sabia.face = "happy3"
                    s "No need."
                    $ Sabia.face = "normal"
                    "Kira's eyes narrowed a little."
                    $ Kira.face = "angry"
                    kira "What do you mean no need?"
                    $ Sabia.face = "happy2"
                    s "Well. There's your prize, right? And the men that were transporting it are now dead."
                    $ Sabia.face = "normal"
                    $ Kira.face = "browsopen"
                    kira "You did that all by yourself? And you knew what to look for?"
                    $ Sabia.face = "annoyed1"
                    $ Kira.face = "normal"
                    s "I did mention my family had several mages in it, did I not? You think I wouldn't recognize something like that?"
                    $ Sabia.face = "normal"
                    $ Kira.face = "normalbite"
                    "Kira's narrowed eyes relaxed, and she grinned."
                    $ Kira.face = "normalopen"
                    kira "Mmm... maybe you're more useful than I thought."
                    kira "Alright! You heard our new friend. We're heading back to camp!"
                    $ Sabia.face = "normalopen"
                    $ Kira.face = "normal"
                    s "I'll meet you back there in a little bit. I need to make a detour."
                    $ Sabia.face = "normal"
                    $ Kira.face = "normalopen"
                    kira "Hmmm... sure. Of course."
                    "Sabia noted how distracted Kira's focus was, the elf's eyes kept flickering back to the small pouch she was now clutching tightly."
                    scene bg black with dissolve
                    jump eastern_frontier_map
                "No, wait for another caravan.":
                    $ Sabia.face = "closed4"
                    s "I don't think that's the correct caravan."
                    $ Sabia.face = "annoyed1"
                    s "It would be easier if I knew what I was looking for."
                    $ Sabia.face = "normalopen"
                    s "Strong horses, reasonably well armed man. Could be the correct one, but so little protection for something that is supposedly so valuable."
                    s "Seems unreasonable, more likely that it's just a soldier transporting some grain."
                    if kira_test_of_cunning_caravan1_done == True and kira_test_of_cunning_caravan2_done == True and kira_test_of_cunning_caravan3_done == True:
                        jump kira_test_of_cunning_badend
                    scene bg black with dissolve
                    pause (0.01)
                    scene bg countryside
                    show Sabia at left
                    show Kia at right
                    with dissolve
                    "Sabia hiked back up the hill and waited with Kia for another caravan."
                    hide Sabia with moveoutleft
                    "Another caravan crested the hill after a while and Sabia did as she did before, heading down to the road."
                    "The wheels of the caravan creaked as it approached."
                    "Sabia settled into a slightly faster gait as the caravan slowed just a little."
                    jump kira_test_of_cunning_caravans


label kira_test_of_cunning_badend:
    scene bg black with dissolve
    pause (0.01)
    scene bg countryside
    show Sabia at left
    with dissolve
    "Sabia hiked back up to the now-empty hill. It seemed Kia had gotten tired of all waiting, and no hunting."
    "Waiting for the next caravan, the minutes continued to pass, until it became hours, and still no more caravans came along."
    "She was beginning to get nervous."
    "Time continued to pass, and slowly, the sun began to creep down to the horizon."
    show Kira at right with moveinright
    $ Kira.face = "normalopen"
    $ Sabia.face = "sad1"
    kira "I see you missed the correct caravan."
    $ Kira.face = "normalbite"
    $ Sabia.face = "sad3"
    s "I didn't want to get the wrong one, and-"
    $ Kira.face = "browsopen"
    $ Sabia.face = "sad1"
    kira "Oh, my sweet {i}warrior{/i}, don't fret. I'm not upset. I'm not even disappointed. We knew which caravan we needed to target."
    kira "I was hoping you'd fail..."
    kira "And it seems my patience has paid off... you will be fun..."
    kira "...for a while!"
    $ Kira.face = "browsbite"
    $ Sabia.face = "surprised1"
    "Kira's fingers wrapped gripped her spear tighter, and the point flashed in the red light of the dusk, darting straight toward Sabia."
    show Kira:
        linear 1.0 xoffset -300
    scene bg black with dissolve
    pause (0.5)
    kira "Dear, oh dear... it's too bad Neve wasn't around to help you when you failed my test of skill... maybe she might have been able to rescue you...?"
    kira "Would you have liked that, my lovely little warrior? I suppose we just won't know... hmm."
    call kira_bandits_badend
    show gameover with dissolve
    pause 3
    $ renpy.full_restart()


label lake_sorthyos_mariana:
    scene bg black with dissolve
    pause (0.01)
    scene bg orclake
    show Sabia at left
    with dissolve
    menu:
        "Search for clues about Mariana":
            if mariana_lake_search == 0:
                $ mariana_lake_search = 1
                "Arriving at Lake Sorthyos, Sabia sighed."
                "It was no small body of water, and the hills surrounding the lake rolled up and down."
                $ Sabia.face = "closed4"
                s "Where am I meant to start? It's like I'll be looking for a needle in a haystack."
                $ Sabia.face = "normalopen"
                s "If the needle is even still here."
                $ Sabia.face = "normal"
                menu lake_sorthyos_mariana_search:
                    "Lake Perimeter" if mariana_lake_search_perimeter == False:
                        $ mariana_lake_search_perimeter = True
                        if mariana_lake_search_forested == True and mariana_lake_search_hills == True:
                            "The sun's light was waning, and Sabia realized she had spent most of the day out here."
                            "She would have to head back after checking out the last spot."
                        $ Sabia.face = "irritated2"
                        "Sabia sighed again."
                        "It would take a good hour to walk around Lake Sorthyos by itself, let alone looking for anything."
                        $ Sabia.face = "normalopen"
                        s "I suppose I better get started, then."
                        $ Sabia.face = "normal"
                        $ Sabia.face = "normal"
                        "Sabia spent a while walking along the Lake's edge."
                        "The soft rippling of water was relaxing, and made the task a little easier to bare."
                        "About halfway around the lake's edge, Sabia paused, and crouched down in the sand."
                        $ Sabia.face = "normalopen"
                        s "What's this...?"
                        $ Sabia.face = "normal"
                        "She ran her finger over the line, and pulled on it."
                        "It skipped through the water easily. There was nothing on the end."
                        $ Sabia.face = "normalopen"
                        s "But still, fishing line is promising. It could be anyone, but, it's better than finding nothing at all I suppose."
                        $ Sabia.face = "normal"
                        "A few more steps and Sabia paused again."
                        $ Sabia.face = "happy2"
                        s "What do we have here? This is even more promising..."
                        $ Sabia.face = "normal"
                        "A pile of fish bones, along with a few discarded skins and fish innards. It must have been fairly fresh, or the birds would have seen to it."
                        "There was also another pile of older bones picked clean and spread haphazardly around the ground."
                        $ Sabia.face = "normalopen"
                        if mariana_lake_search_forested == True:
                            s "Well, no guesses as to what my suspected Mariana has been eating."
                            jump lake_sorthyos_mariana_search
                        s "Well, it seems someone has been here recently."
                        s "But they're certainly not living on the lake's edge, just fishing and eating here."
                        jump lake_sorthyos_mariana_search

                    "Hills" if mariana_lake_search_hills == False:
                        $ mariana_lake_search_hills = True
                        if mariana_lake_search_perimeter == True and mariana_lake_search_forested == True:
                            "The sun's light was waning, and Sabia realized she had spent most of the day out here."
                            "She would have to head back after checking out the last spot."
                        "Hills rolled out northward, some of them taller than others."
                        $ Sabia.face = "normalopen"
                        s "I can't imagine anyone's going to be living at the bottom of a hill to hide out."
                        s "But... there could be a cave or two."
                        s "It's worth a look."
                        $ Sabia.face = "normal"
                        "Sabia set off toward the hills."
                        "It wasn't long before a heavy sheen of sweat was rolling down her forehead, and her clothes sticking to her body."
                        "Up, down, up, down. The hills were unrelenting in their assault."
                        $ Sabia.face = "irritated2"
                        "Sabia spent several hours traversing them, looking down from every peak she could. She found nothing."
                        $ Sabia.face = "annoyed2"
                        s "Ugh, what a waste of time."
                        jump lake_sorthyos_mariana_search

                    "Forested area" if mariana_lake_search_forested == False:
                        $ mariana_lake_search_forested = True
                        if mariana_lake_search_hills == True and mariana_lake_search_perimeter == True:
                            "The sun's light was waning, and Sabia realized she had spent most of the day out here."
                            "She would have to head back after checking out the last spot."
                        "Not too far from the lake there was a small grove of trees."
                        "Sabia had enough experience with forested areas now to know how well that could hide people. Or ambushes."
                        "Not expecting too much trouble if the bandit that had been described to her attacked her, Sabia nonetheless kept a firm hand on her weapon."
                        "The trees provided significant cover, and slowly, Sabia made her way through the grove."
                        $ Sabia.face = "irritated2"
                        "It seemed nothing was ever too easy for Sabia, and she wasn't able to spot any Mariana lying about."
                        "But it wasn't entirely a waste either."
                        "She found a pile of charred wood and charcoal. Clearly, someone had been here."
                        "Whether it had been Mariana or not, well that was still up for debate."
                        $ Sabia.face = "normalopen"
                        s "If I had to take a wild guess though, I'd say it would be Mariana."
                        s "Fled from the bandit camp. Hanging around Lake Sorthyos. And here I find a camp fire."
                        s "But, still, no Mariana."
                        jump lake_sorthyos_mariana_search

                    "Leave" if mariana_lake_search_perimeter == True and mariana_lake_search_hills == True and mariana_lake_search_forested == True:
                        $ Sabia.face = "normalopen"
                        s "I think I've got enough evidence here."
                        s "I suspect that old orc knows a little bit more than he's letting on."
                        s "If she's going to flee, then staying so close to the people or group you are fleeing from - well, it makes little sense."
                        jump eastern_frontier_map


label finding_mariana:
    show Sabia at left with dissolve
    show Neve at center with moveinright
    $ mariana_found = True
    n "Wait up, Sabia. I'll go with you. I owe Dajrab a few debts, anyway."
    $ Sabia.face = "normalopen"
    s "Fair enough. Let's go."
    scene bg black with dissolve
    pause (0.01)
    scene bg orclake
    show Sabia at left
    show Neve at right
    with dissolve
    "They set off toward the area where Mariana had been hiding."
    "It was near Lake Sorthyos, but far enough away that Sabia knew she would never have found Mariana wandering aimlessly about the lake."
    "The girl was not at all good at hiding, or perhaps she simply felt she was safe enough in her reclusive area."
    $ Neve.face = "closed3"
    "Neve and Sabia spotted her instantly."
    $ Neve.face = "normal"
    n "I'll go around the far side. Wait for my signal."
    "Sabia nodded."
    hide Neve with moveoutright
    "She watched Neve move about in silence. Not a snap of a twig underfoot, nor even a rustle of leaves."
    "Neve positioned herself, and called her signal."
    hide Sabia with moveoutright
    "Sabia dashed into the clearing."
    scene bg orclake
    show Sabia at left
    show Neve at right
    with dissolve
    "Mariana jerked upright, her face like a startled deer."
    "The ex-bandit froze for a moment, before she stumbled forward, running right into Neve who had come from behind."
    $ Neve.face = "smirk1"
    n "Not so fast."
    "The girl struggled, writhing under Neve's grip."
    "She was stronger than Neve had expected, and managed to slip one arm out from Neve's hold."
    $ Neve.face = "irritated1"
    n "Ugh."
    "With a flurry that Sabia couldn't see as anything more than a blur, Neve's hand grabbed hold of her dagger, and the pommel hit the side of Mariana's head, and the girl fell to the ground."
    $ Sabia.face = "normalopen"
    s "What are we meant to do now, Neve?"
    $ Neve.face = "normal"
    $ Sabia.face = "normal"
    n "Well, she's going to wake up, isn't she?"
    $ Sabia.face = "normalopen"
    s "I suppose so."
    s "We should tie her up, so she can't try to wriggle out again."
    $ Neve.face = "smirk1"
    $ Sabia.face = "normal"
    n "Yeah, good idea."
    "Sabia and Neve spent the next few minutes doing just that - binding and blind-folding her. It turns out Neve had been well prepared for this eventuality, and Sabia was yet again glad she had the elf's help."
    "The ebony-skinned girl was reasonably well-built, visible muscles and a toned midriff, but that didn't detract from her looks. Sabia admitted that she was fairly cute, and she could see why a few in the camp had been sad to see her disappear."
    $ Neve.face = "smirk1"
    n "She's cute..."
    $ Sabia.face = "normalopen"
    s "So what's the plan when she wakes up?"
    $ Sabia.face = "normal"
    $ Neve.face = "normal"
    n "We can either... play nice. Or play..."
    $ Sabia.face = "irritated2"
    $ Neve.face = "irritated1"
    n "Not so nice."
    menu:
        "Play nice.":
            $ Neve.face = "normal"
            $ Sabia.face = "normalopen"
            s "Well, you catch more flies with honey..."
            $ Sabia.face = "normal"
            n "Nice it is, then, and-"
            $ Neve.face = "happy2"
            n "Oh, she's awake finally..."
            $ Sabia.face = "angry1"
            $ Neve.face = "irritated2"
            s "No wonder it took so long, with how hard you hit her head. Maybe next time try to hold it back a little?"
            $ Sabia.face = "irritated2"
            $ Neve.face = "normal"
            n "You might have a point there, Sabia."
            call mariana_quest_interrogation
            play music forest fadeout 2.0 fadein 2.0
        "Play not so nice.":
            $ Neve.face = "normal"
            n "Well, we better wake her up then. No point in letting her wake nicely if we're going to play hard."
            "Sabia nodded."
            "The two of them moved closer to the unconscious girl, and shook her awake."
            "It didn't take much for the poor girl to crumple. A few punches, and the threat of something worse, and she was all words."
            scene bg black with dissolve
            "They spent an hour questioning her, finding out everything she knew."
            "Sabia and Neve consolidated the information they had learned at the end of it - Mariana had seen massive amounts of money pouring in. More than from what they had been getting from raids."
            "Troops and weapons beyond what bandits should be able to..."
            "She suspected a captain from Grok og Dar had been involved in Groknak's disappearance, and she had fled in fear of both Kira and Dajrab..."
            "But not confident enough, she had relied on the old orc's help and advice, hiding near Lake Sorthyos."
            "They walked away from Mariana to discuss what to do now."
    if mariana_lake_search_toldkira == True:
        scene bg orclake
        $ Sabia.face = "normalopen"
        $ Neve.face = "irritated1"
        show Sabia at left
        show Neve at right
        with dissolve
        s "Wait. We can't kill her."
        $ Sabia.face = "irritated2"
        n "Why? Dajrab didn't want his contact being a loose end."
        $ Sabia.face = "normalopen"
        s "I made an... arrangement with Kira. We have to return Mariana to her - it's how I get her location from the orc."
        $ Sabia.face = "normal"
        $ Neve.face = "sad"
        n "To... Kira?"
        "Neve paused, looking down at Mariana. Sabia thought she could see a bit of pity on Neve's face."
        $ Neve.face = "irritated1"
        n "Alright, then. I think it's safe to say she won't be a loose end... not being delivered to Kira."
        $ Sabia.face = "irritated2"
        "Sabia and Neve gagged Mariana back up, and headed back to Kira's camp."
        scene bg black with dissolve
        pause (0.01)
        scene bg cave
        $ Kira.face = "browsopen"
        $ Sabia.face = "normal"
        $ Neve.face = "normal"
        show Sabia at left
        show Neve at center
        show Kira at right
        with dissolve
        kira "Ah! My favorite little play-warrior has brought me a present...!"
        $ Kira.face = "browsbite"
        "Kira was ecstatic, rushing in and inhaling Mariana's scent, hands roaming over the cuffed girl."
        $ Kira.face = "angryopen"
        kira "Leave me!"
        $ Kira.face = "browsbite"
        kira "I'm going to have so much fun..."
        hide Kira with moveoutright
        $ Neve.face = "sad"
        n "Death might have been cleaner for the girl."
        $ Sabia.face = "normalopen"
        s "It might have..."
        scene bg black with dissolve
        pause (0.01)
        jump eastern_frontier_map
    else:
        scene bg orclake
        $ Sabia.face = "normal"
        $ Neve.face = "normal"
        show Sabia at left
        show Neve at right
        with dissolve
        n "Well... that was informative, to a degree..."
        $ Sabia.face = "normalopen"
        s "Yeah... if she's to be believed, then we need to keep an eye out for the captain's... and there might be something behind the bandit groups."
        $ Sabia.face = "normal"
        $ Neve.face = "happy3"
        n "It's a good thing we're cozying up to Kira, then. Though I doubt she's going to be giving up information readily."
        $ Sabia.face = "irritated2"
        $ Neve.face = "smirk1"
        n "Hmm... too bad we can't keep little Mari around. She was learning quickly."
        $ Neve.face = "sad"
        n "Not as quickly as you though. Perhaps I should have taken you under my wing earlier..."
        $ Sabia.face = "angry1"
        $ Neve.face = "smirk1"
        s "It was just to get the information..."
        $ Sabia.face = "irritated2"
        $ Neve.face = "happy2"
        n "Sure, Sabia."
        $ Sabia.face = "normalopen"
        s "Well... at any rate... that leaves us with Mariana..."
        $ Sabia.face = "normal"
        "Sabia left the thought hanging in the air."
        $ Neve.face = "normal"
        n "I'll take care of it, Sabia."
        menu:
            "Let Neve 'take care' of Mariana.":
                $ mariana_fate_decision = "neve"
                "Sabia gave a grim, half-reluctant nod. She left the area, letting Neve... finish Dajrab's request."
                scene bg black with dissolve
                pause (0.01)
                jump eastern_frontier_map
            "Let Mariana go.":
                $ Sabia.face = "sad3"
                s "Do we... really have to kill her?"
                s "She's just a desperate young girl, trying to live."
                $ Sabia.face = "sad1"
                $ Neve.face = "irritated1"
                n "Dajrab was quite insistent."
                if orcalliance == "dajrab":
                    $ Sabia.face = "normalopen"
                    s "Well, we don't even know if we can trust Dajrab."
                    $ Sabia.face = "pout1"
                    $ Neve.face = "normal"
                    n "Then that's all the more reason to not arouse his suspicion, isn't it?"
                    $ Sabia.face = "normalopen"
                    s "I still would rather we... don't."
                else:
                    $ Sabia.face = "angry1"
                    s "Well, I don't work for Dajrab. And I'm not going to see her killed."
                s "If it comes back to us, I'll take the blame. I'll say you had nothing to do with it."
                $ Sabia.face = "normal"
                $ Neve.face = "closed4"
                "Neve shrugged."
                $ Neve.face = "normal"
                n "I don't know what Dajrab will do if it ever comes out."
                $ Sabia.face = "normalopen"
                s "It might not ever come out."
                $ Sabia.face = "normal"
                n "It's up to you, Sabia. Are you sure?"
                menu:
                    "Yes.":
                        $ mariana_fate_decision = "free"
                        $ Sabia.face = "normalopen"
                        s "We'll undo her binds, and drag her a bit into hiding. I should have some parchment on me."
                        $ Sabia.face = "normal"
                        $ Neve.face = "irritated1"
                        n "How do you know she's going to actually run, and not just linger here?"
                        $ Sabia.face = "normalopen"
                        s "It's a chance I'm going to take, Neve."
                        $ Sabia.face = "normal"
                        $ Neve.face = "normal"
                        "Sabia wrote out a note, telling Mariana to go south. Don't stop until she makes it to Carchedon. Her best chance is there."
                        "Neve and Sabia both left the area near Lake Sorthyos."
                        if orcalliance == "dajrab":
                            "Sabia would have to report this to Dajrab."
                        scene bg black with dissolve
                        pause (0.01)
                        jump eastern_frontier_map
                    "No, let Neve 'take care' of Mariana.":
                        "Sabia gave a grim, half-reluctant nod. She left the area, letting Neve... finish Dajrab's request."
                        if orcalliance == "dajrab":
                            "She would need to report this to Dajrab."
                        scene bg black with dissolve
                        pause (0.01)
                        jump eastern_frontier_map


label ef3_rival_camp:
    play music forest fadeout 2.0 fadein 2.0
    scene bg cave with dissolve
    $ avion_quest = 4
    $ avion_quest_scouted = True
    show Sabia at left with dissolve
    $ Sabia.face = "irritated2"
    "It was much less of a camp than Kira's. Sabia had expected patrols, and a certain level of awareness as she approached like last time."
    "However, it seemed that they weren't at all as worried about intruders."
    $ Sabia.face = "normal"
    "A few rows of tents seemed to suggest that, at any rate. There were a few guards posted around the edges of the grove as well."
    "From what she could see, most of the bandits seemed like they had not been soldiers before joining. They were wiry and thin for the most part."
    "Not malnourished at all - but certainly not well-muscled."
    $ Sabia.face = "closed2"
    "She doubted any of them had any great skill. But even so, that many against a single minotaur? It seemed unlikely. Even if she were to help, she had her doubts."
    $ Sabia.face = "normalopen"
    s "Well, maybe Avion could deal with it. I haven't seen him fight, but I know that he was the one to take several of Groknak's guard out."
    s "And I remember what some of the minotaurs could do on the front lines."
    s "I could just let him try himself."
    $ Sabia.face = "annoyed1"
    s "If he dies, I'm not out an ally, but I could potentially be out a hindrance."
    $ Sabia.face = "normalopen"
    s "Kira might not be too happy though. I'm sure I can think of a safer way to deal with them."
    $ Sabia.face = "normal"
    menu:
        "Leave. Let Avion deal with it.":
            $ avion_quest_plan = "avion"
            $ Sabia.face = "annoyed1"
            s "I'll just let Avion deal with it his way. If he kills them all - great. If he dies - well, at least I don't have to deal with an antagonistic minotaur."
            jump eastern_frontier_map
        "Stay and try to overhear more info.":
            $ avion_quest_plan_ambush = True
            $ Sabia.face = "closed2"
            "Sabia decided to stay, and see if she could glean any relevant information."
            $ Sabia.face = "normal"
            "She could overheard little, but every now and then she managed to catch a snippet of conversation."
            scene bg black with dissolve
            bandit1 "I can't believe how little loot we've gotten... I didn't desert Whitecrest just to get scraps!"
            bandit2 "Hard to get anything else with that crazy Elf bitch... that's why we're trying to take her territory, you know?"
            bandit1 "Still... I wish we could get a nice easy payday, yeah?"
            scene bg cave
            show Sabia at left
            with dissolve
            "The bandits were walking as they talked, and soon they were too far for Sabia to catch anything else."
            $ Sabia.face = "normalopen"
            s "Hmmm... maybe I could lure them into an ambush? They must not {i}all{/i} leave on raids..."
            $ Sabia.face = "closed4"
            s "That would still only leave two against several times that many, though."
            $ Sabia.face = "normalopen"
            s "And if there are any scouts that we miss while fighting, they could get back to the camp before us."
            s "It wouldn't be ideal if that happened, but it's a potentially workable idea."
            $ Sabia.face = "normal"
            menu:
                "Stay.":
                    $ avion_quest_plan_cart = True
                    $ Sabia.face = "normalopen"
                    s "I'll stay a bit longer."
                    scene bg black with dissolve
                    bandit1 "...way is that going to work!"
                    bandit2 "It will!"
                    bandit1 "Nah. Fuck that, it's dumb. We should just go back into town and buy some."
                    bandit2 "I don't want to spend my lundils on fucking booze. We should be hitting drink merchants and enjoying our nights!"
                    bandit2 "Isn't that what being a bandit is all about anyway?"
                    bandit1 "I mean, well, maybe, but..."
                    "They kept walking, their voices fading until Sabia couldn't hear them anymore."
                    scene bg cave
                    show Sabia at left
                    with dissolve
                    $ Sabia.face = "normalopen"
                    s "Well, that's an idea that might work too... a cart of alcohol. They might even drink it and be hammered when we attack."
                    s "Hopefully, they would all be in their camp as well. But if any of them didn't drink, or are still awake - we might have to deal with more than we want."
                    $ Sabia.face = "normal"
                    menu:
                        "Stay.":
                            "Sabia decided to stay a bit longer."
                            $ Sabia.face = "closed2"
                            "After an hour or two of not managing to overhear anything relevant, she decided that the information she had was enough."
                            $ Sabia.face = "normalopen"
                            s "I'll have to choose one of these plans, I suppose."
                            jump eastern_frontier_map
                        "Leave.":
                            $ Sabia.face = "normalopen"
                            s "I have what I need. One of these plans will work, I'm sure. I just have to decide which."
                            jump eastern_frontier_map
                "Enough information. Leave.":
                    $ Sabia.face = "normalopen"
                    s "That's enough information. I already have a fair idea of how deadly Avion is in an ambush."
                    s "I'll have to drop some information about "
                    jump eastern_frontier_map


label ef3_rival_camp_avion:
    $ avion_quest = 6
    $ avion_quest_heart = True
    $ Avion.face = "normaleyes"
    avion "Very well. Do not get in my way."
    $ Avion.face = "normal"
    $ Sabia.face = "normalopen"
    s "Be my guest."
    $ Sabia.face = "normal"
    $ Avion.face = "angry"
    "Avion snorted, grabbing his macuahuitl. The thing was monstrous. It was almost as tall as Sabia."
    "Along its edges it was embedded with wicked, jagged stones. Some of them seemed worn, but Sabia knew that the real power came from who wielded it."
    $ Avion.face = "normal"
    "It did strike her as odd that a minotaur would let his weapon go like that, but given the war; she supposed he had his reasons."
    scene bg black with dissolve
    "The two traveled toward the offending bandit camp in silence."
    "Sneaking closer - with Avion surprising Sabia with his stealthiness - they came close enough to see in the camp."
    scene bg forest
    show Sabia at left
    show Avion at right
    with dissolve
    if avion_quest_scouted == True:
        "There were about twice as many bandits now than as Sabia had seen before."
    else:
        "There were about twice as many bandits now than as Avion had said."
    "Avion hefted the macuahuitl, his powerful fingers flexing against the wooden shaft."
    $ Sabia.face = "normalopen"
    $ Avion.face = "angry"
    s "That's a lot. Are you sure you don't want me to help?"
    $ Sabia.face = "irritated1"
    $ Avion.face = "normal"
    avion "The Gods will see me."
    $ Sabia.face = "annoyed1"
    s "Alright, fine."
    $ Sabia.face = "irritated1"
    "Sabia snapped it out. There was no changing his mind. That phrase had been burned into her mind from the war."
    $ Avion.face = "angry"
    avion "I do not wish the Gods to see us fighting side by side."
    $ Sabia.face = "normalopen"
    s "Go, then."
    $ Sabia.face = "irritated1"
    "Avion gave Sabia a look of displeasure as he surged to his feet, grunting under his breath."
    $ Avion.face = "normal"
    call shake ("h")
    "He slammed the weapon into the ground, tip first. It was with enough force to send a heavy thud blasting through the camp, and shaking the earth under Sabia."
    $ Avion.face = "angryeyes"
    avion "PROVE YOUR HEART!"
    hide Avion with moveoutleft
    "The hulking frame burst into the bandits' camp."
    hide Sabia with dissolve
    pause (0.1)
    $ Avion.face = "angryeyes"
    $ GenericOrc1.extras = ["Loincloth", "Beard1", "Axe"]
    $ GenericOrc1.face = "suspicious"
    $ GenericOrc2.extras = ["Loincloth", "Hair", "Axe"]
    $ GenericOrc2.face = "angry"
    show GenericOrc1 at center
    show GenericOrc2 at right
    with dissolve
    show Avion at left with moveinleft:
        xzoom -1
    $ renpy.show("GenericOrc1mask", at_list=[center], what=AlphaBlend(Transform("GenericOrc1", alpha=0.9), "GenericOrc1", bloodhit_effect, alpha=True))
    $ renpy.show("GenericOrc2mask", at_list=[right], what=AlphaBlend(Transform("GenericOrc2", alpha=0.9), "GenericOrc2", bloodhit_effect, alpha=True))
    pause(0.1)
    hide GenericOrc1
    hide GenericOrc1mask
    hide GenericOrc2
    hide GenericOrc2mask
    with dissolve
    "Two bodies were ripped in half in an instant, their lifeless remains falling to the ground as blood dripped from Avion's macuahuitl."
    $ Humansoldier.face = "angry"
    show Humansoldier at right with moveinright
    "The call went up about the camp, and the other bandits rushed to their own feet, grabbing weapons and hurrying over."
    show Avion at right with move
    $ renpy.show("Humansoldiermask", at_list=[right], what=AlphaBlend(Transform("Humansoldier", alpha=0.9), "Humansoldier", bloodhit_effect, alpha=True))
    pause(0.01)
    call shake ("h")
    hide Humansoldier
    hide Humansoldiermask
    with moveoutright
    $ GenericOrc2.extras = ["Loincloth", "Hair", "Axe", "Helmet"]
    $ GenericOrc2.face = "angry"
    show GenericOrc2 at left with moveinleft:
        xzoom -1
    show Avion at center with move:
        xzoom 1
    call shake ("h")
    $ renpy.show("GenericOrc2mask", at_list=[left, invertedx], what=AlphaBlend(Transform("GenericOrc2", alpha=0.9), "GenericOrc2", bloodhit_effect, alpha=True))
    pause(0.1)
    hide GenericOrc2
    hide GenericOrc2mask
    with dissolve
    "Avion lowered his head, and his horns pierced another foe. He threw them off with a flick of his head, even as his weapon came down and cleaved another bandit in two."
    "The sheer force of his strike ripped the man apart."
    hide Avion with dissolve
    pause (0.1)
    show Sabia with dissolve
    "Memories of the war rushed back to her; a minotaur was truly a frightening force."
    "Of course, it didn't help that the bandits were a motley crew of wiry, cocky men with no real martial skill."
    "Avion continued his brutal assault, flourishes of blood painting the trees and ground in great gashes of scarlet red."
    "Every few moments he roared his disappointment as another bandit fell behind him, his almost desperate pleas of 'Prove your heart' drowning the terrified screams for just a moment."
    "His macuahuitl dripped thick with blood and bone, and it was not long before some of the bandits were broken and routed."
    "Those that had, rushed toward Sabia, trying to escape."
    $ enemy_level = 9
    $ enemy_maxhp = 400
    $ enemy_hp = enemy_maxhp
    $ enemy_type = 1
    $ enemy_skills = [Enemyattack,Enemyattack,Enemyquickattack]
    $ enemy_attack = 70
    $ enemy_defense = 0
    $ enemy_magdefense = 0
    $ GenericOrc1.face = "angry"
    $ GenericOrc1.extras = ["Loincloth", "Axe", "Hair"]
    $ player = Sabia
    $ enemy = GenericOrc1
    call duel
    if _return != "Victory":
        $ avion_quest_lost_fight = True
        "Sabia was overwhelmed by bandits, but Avion came to her rescue."
        jump ef3_rival_camp_avion2
    $ enemy_level = 9
    $ enemy_maxhp = 400
    $ enemy_hp = enemy_maxhp
    $ enemy_type = 1
    $ enemy_skills = [Enemyattack,Enemyattack,Enemyquickattack]
    $ enemy_attack = 70
    $ enemy_defense = 0
    $ enemy_magdefense = 0
    $ GenericOrc2.face = "angry"
    $ GenericOrc2.extras = ["Loincloth", "Axe", "Beard1"]
    $ player = Sabia
    $ enemy = GenericOrc2
    call duel
    if _return != "Victory":
        $ avion_quest_lost_fight = True
        "Sabia was overwhelmed by bandits, but Avion came to her rescue."
        jump ef3_rival_camp_avion2
    $ enemy_level = 9
    $ enemy_maxhp = 400
    $ enemy_hp = enemy_maxhp
    $ enemy_type = 1
    $ enemy_skills = [Enemyattack,Enemyattack,Enemyquickattack]
    $ enemy_attack = 2
    $ enemy_defense = 2
    $ enemy_magdefense = -2
    $ GenericOrc1.face = "angry"
    $ GenericOrc1.extras = ["Loincloth", "Axe", "Shoulder", "Strap"]
    $ player = Sabia
    $ enemy = GenericOrc1
    call duel
    if _return != "Victory":
        $ avion_quest_lost_fight = True
        "Sabia was overwhelmed by bandits, but Avion came to her rescue."
    jump ef3_rival_camp_avion2


label ef3_rival_camp_avion2:
    scene bg forest with dissolve
    $ Banditgirl.face = "worried"
    show Sabia at left
    show Avion at right
    with dissolve
    if avion_quest_lost_fight == True:
        "She was lucky Avion had decided to intervene. She would not be standing now otherwise."
        $ Sabia.face = "irritated2"
        $ Avion.face = "smirk"
        avion "Hmph. You performed better than I expected. But that does not mean you performed well."
        $ Sabia.face = "normalopen"
        s "I'm just glad I didn't have to fight you as well."
    else:
        $ Sabia.face = "irritated2"
        $ Avion.face = "smirk"
        "Sabia's chest heaved as she breathed in deeply. Fighting three men at once - even ones below her skill - was no mean feat."
        "She didn't have the years of practical experience, nor the sheer brutal force of Avion to rely on."
        avion "Hmph. You did not get in my way. Perhaps you could make a worthy Tlactina."
        "A worthy Tlactina was about as close as she was going to get to a compliment from him, Sabia supposed."
        $ Sabia.face = "normalopen"
        s "Yeah, well. You did most of the work. I'm glad I don't have to fight you."
    $ Avion.face = "angry"
    $ Sabia.face = "normal"
    "Avion stared pointedly at Sabia at those words, his lips twitching and curling."
    $ Sabia.face = "normalopen"
    s "I mean-"
    $ Sabia.face = "normal"
    $ Avion.face = "angryeyes"
    avion "Quiet. I do not wish to speak about it."
    $ Sabia.face = "normalopen"
    s "Yeah. Alright. I'm fine with that."
    $ Avion.face = "normal"
    $ Sabia.face = "normal"
    hide Avion with moveoutright
    "Avion walked back toward the center of the clearing without another word."
    $ Sabia.face = "sad2"
    "Sabia watched as he bent down, and pried apart one bandit's chest with his bare hands."
    "The sounds of crunching bone reached her ears and she winced. Avion ripped his heart out, his furred fingers dripping red."
    "Still not done, Avion walked farther back into the forested area on the other side of the clearing."
    $ Sabia.face = "surprised1"
    "A shrill shriek sent birds flying from their perches."
    $ Sabia.face = "irritated2"
    show Avion at right
    show Banditgirl at right
    with moveinright
    show bgirltears at right with dissolve
    "Avion's arm was behind him as he walked back towards Sabia. A protesting girl was screaming, dragged along by his iron grip."
    "He ignored the protests."
    $ Avion.face = "happy"
    avion "A heart and a spirit."
    bandit1 "Please! No! Let me go, I didn't - I won't do anything again! I'm not like these others, please!"
    $ Sabia.face = "normalopen"
    $ Avion.face = "normaleyes"
    s "You're not going to-"
    $ Sabia.face = "normal"
    $ Avion.face = "normal"
    jump ef3_rival_camp_aftermath


label ef3_rival_camp_ambush:
    $ dom += 1
    $ A_avion += 1
    $ avion_quest = 6
    $ avion_quest_heart = True
    $ Sabia.face = "normalopen"
    s "Alright. Let's go. The other bandit camp thinks a very big payoff is going be trundling through the road nearest their camp."
    s "We can sneak in behind them, and ambush them. I doubt they'll be expecting it."
    $ Sabia.face = "normal"
    "Avion pulled himself up onto his hooves and nodded."
    $ Sabia.face = "irritated2"
    avion "This is a fine plan."
    $ Sabia.face = "happy2"
    s "Huh. I'm surprised you're alright with me coming up with a plan."
    $ Sabia.face = "normal"
    "He said no more, and gestured for Sabia to lead."
    $ Sabia.face = "normalopen"
    s "Alright then."
    scene bg black with dissolve
    "The two of them traveled for just over an hour. They came to the outskirts of the other group's territory."
    "Upon doing so, they left the road and sunk into the forest."
    "Sabia was surprised by Avion's ability at stealth."
    "They didn't speak, not wanting to give away their position. With how unskilled and inept most of the other bandits were, Sabia doubted anything outside of them speaking would alert them."
    "It only took a few moments before Avion spotted signs of their tracks and paths. He pointed it out to Sabia."
    scene bg forest with dissolve
    pause (0.1)
    show Sabia at left
    show Avion at right
    with dissolve
    "She nodded, and they moved in closer. Another few minutes, and they found a small group of bandits, milling about and whispering to themselves."
    "Avion and Sabia glanced at each other."
    $ Avion.face = "normal"
    avion "May the Gods watch my macuahuitl, may they watch my horns, may they watch me."
    "Avion half-muttered the war-ritual to himself under his breath. Sabia only understood it because she remembered it from the wars."
    "They nodded at each other."
    $ Sabia.face = "angry2"
    $ Avion.face = "angryeyes"
    hide Sabia
    hide Avion
    with dissolve
    pause (0.1)
    $ GenericOrc1.extras = ["Loincloth", "Axe"]
    $ GenericOrc1.face = "Angry"
    show GenericOrc1 at left with dissolve
    pause (0.1)
    show Sabia behind GenericOrc1 at left with dissolve
    $ renpy.show("GenericOrc1mask", at_list=[left], what=AlphaBlend(Transform("GenericOrc1", alpha=0.9), "GenericOrc1", bloodhit_effect, alpha=True))
    pause(0.1)
    hide GenericOrc1
    hide GenericOrc1mask
    with dissolve
    "Sabia's blade broke through the underbrush of the forest, a flash of bright steel that sliced through one of the bandits. He crumpled to the ground."
    hide Sabia with dissolve
    pause (0.1)
    show GenericOrc1 at center with dissolve
    show Avion behind GenericOrc1 at center with moveinright
    $ renpy.show("GenericOrc1mask", at_list=[center], what=AlphaBlend(Transform("GenericOrc1", alpha=0.9), "GenericOrc1", bloodhit_effect, alpha=True))
    pause (0.01)
    hide GenericOrc1mask
    hide GenericOrc1
    with moveoutleft
    $ Avion.face = "angry"
    "Avion's macuahuitl ripped one man in two from sheer force, the top half of the body tumbling several feet away."
    hide Avion with dissolve
    pause (0.1)
    show GenericOrc1 at right with dissolve
    pause (0.1)
    show Sabia behind GenericOrc1 at right with dissolve
    $ renpy.show("GenericOrc1mask", at_list=[right], what=AlphaBlend(Transform("GenericOrc1", alpha=0.9), "GenericOrc1", bloodhit_effect, alpha=True))
    pause(0.1)
    hide GenericOrc1
    hide GenericOrc1mask
    with dissolve
    "Not missing a step, Sabia turned to one of the others and finished another opposing bandit."
    hide Sabia with dissolve
    pause(0.1)
    $ GenericOrc2.extras = ["Loincloth", "Axe"]
    $ GenericOrc2.face = "sad2"
    show GenericOrc2 at right
    bandit1 "FUCK! HELP!"
    show Avion behind GenericOrc2 at right with moveinright
    with hpunch
    hide GenericOrc2 with moveoutleft
    "The bandit screeched into the forest, his voice was trembling with fear. Avion's wicked weapon had missed him, landing with an earth-shaking thud into the ground."
    $ Sabia.face = "angry1"
    show Sabia at left with dissolve
    s "Damn it!"
    hide Sabia
    hide Avion
    show GenericOrc2 at center
    with dissolve
    show Sabia behind GenericOrc2 at center with moveinright
    $ renpy.show("GenericOrc2mask", at_list=[center], what=AlphaBlend(Transform("GenericOrc2", alpha=0.9), "GenericOrc2", bloodhit_effect, alpha=True))
    pause(0.1)
    hide GenericOrc2
    hide GenericOrc2mask
    with dissolve
    $ Sabia.face = "angry2"
    "Sabia hissed her frustration, jumping forward and driving her blade into the screamer."
    "It was too late though, the rest had rushed over toward them."
    "Avion's size and presence dictated that more of them focused on him, but several bandits confronted Sabia."
    $ Avion.face = "angryeyes"
    avion "PROVE YOUR HEART!"
    "Avion roared his demand, charging toward those that had dared risk a fight with him. Fervor and hunger was etched on his features."
    $ Avion.face = "angry"
    "The bandits' attack stumbled for a moment, and Sabia took the opportunity to slice another one across the chest."
    $ enemy_level = 9
    $ enemy_maxhp = 400
    $ enemy_hp = enemy_maxhp
    $ enemy_type = 1
    $ enemy_skills = [Enemyattack,Enemyattack,Enemyquickattack]
    $ enemy_attack = 70
    $ enemy_defense = 10
    $ enemy_magdefense = 0
    $ GenericOrc1.face = "angry"
    $ GenericOrc1.extras = ["Loincloth", "Axe", "Hair"]
    $ player = Sabia
    $ enemy = GenericOrc1
    call duel
    if _return != "Victory":
        $ avion_quest_lost_fight = True
        "Sabia was overwhelmed by bandits, but Avion came to her rescue."
        jump ef3_rival_camp_ambush_2
    $ enemy_level = 9
    $ enemy_maxhp = 400
    $ enemy_hp = enemy_maxhp
    $ enemy_type = 1
    $ enemy_skills = [Enemyattack,Enemyattack,Enemyquickattack]
    $ enemy_attack = 65
    $ enemy_defense = 10
    $ enemy_magdefense = 0
    $ GenericOrc2.face = "angry"
    $ GenericOrc2.extras = ["Loincloth", "Axe", "Beard1"]
    $ player = Sabia
    $ enemy = GenericOrc2
    call duel
    if _return != "Victory":
        $ avion_quest_lost_fight = True
        "Sabia was overwhelmed by bandits, but Avion came to her rescue."
        jump ef3_rival_camp_ambush_2
    $ enemy_level = 9
    $ enemy_maxhp = 400
    $ enemy_hp = enemy_maxhp
    $ enemy_type = 1
    $ enemy_skills = [Enemyattack,Enemyattack,Enemyquickattack]
    $ enemy_attack = 65
    $ enemy_defense = 10
    $ enemy_magdefense = 0
    $ GenericOrc1.face = "angry"
    $ GenericOrc1.extras = ["Loincloth", "Axe", "Shoulder", "Strap"]
    $ player = Sabia
    $ enemy = GenericOrc1
    call duel
    if _return != "Victory":
        $ avion_quest_lost_fight = True
        "Sabia was overwhelmed by bandits, but Avion came to her rescue."
        jump ef3_rival_camp_ambush_2
    scene bg forest with dissolve
    show Sabia at left
    show Avion at right
    with dissolve
    $ Sabia.face = "sad1"
    "With a flash of red against the ground, Sabia pulled her blade from the last bandit."
    $ Avion.face = "happy"
    avion "A good fight."
    $ Avion.face = "normal"
    $ Sabia.face = "surprised1"
    jump ef3_rival_camp_ambush_2


label ef3_rival_camp_ambush_2:
    scene bg forest with dissolve
    show Sabia at left
    show Avion at right
    with dissolve
    $ Sabia.face = "sad1"
    $ Avion.face = "happy"
    avion "A good fight."
    $ Avion.face = "normal"
    $ Sabia.face = "surprised1"
    "Sabia looked over and her eyes widened a little bit. Avion's comment was short for the pile of ruined bodies she saw at his hooves."
    $ Sabia.face = "normal"
    $ Avion.face = "happy"
    avion "This was not all of them."
    "Sabia scanned the bodies."
    $ Avion.face = "normal"
    $ Sabia.face = "normalopen"
    s "No. It's not. Did any escape?"
    $ Sabia.face = "normal"
    "Avion let his axe thump on the ground, pondering the dripping red heart in his fingers."
    $ Avion.face = "angry"
    avion "I hope so. There was only one worthy heart amongst these bandits."
    $ Avion.face = "normal"
    $ Sabia.face = "irritated2"
    s "..."
    $ Sabia.face = "normalopen"
    s "We need to go to their camp, then. At the least, we've dispatched a good majority of them."
    "Avion nodded, agreeing."
    scene bg black with dissolve
    "Both of them moved with a brisk pace back towards the bandit's camp. They arrived shortly, and all that was left was a skeleton crew."
    "Avion charged in with his hulking frame and wicked axe swinging before Sabia had a chance to say anything."
    $ Banditgirl.face = "worried"
    scene bg forest
    show Sabia at left
    show Avion at right
    show Banditgirl at right
    show bgirltears at right
    with dissolve
    "Avion's arm was behind him as he walked through the clearing, back towards Sabia. A protesting girl was screaming, dragged along by his iron grip."
    $ Sabia.face = "irritated2"
    bandit1 "Please! No! Let me go, I didn't - I won't do anything again! I'm not like these others, please!"
    $ Avion.face = "happy"
    avion "A heart and a spirit. The Gods have judged this a good fight."
    $ Sabia.face = "angry1"
    $ Avion.face = "normal"
    s "You're not going to-"
    $ Sabia.face = "angry2"
    jump ef3_rival_camp_aftermath


label ef3_rival_camp_cart:
    $ A_avion -= 1
    $ avion_quest_cart_deployed = True
    $ Sabia.face = "normalopen"
    s "Alright. I've got the cart of alcohol just outside camp. Are you ready?"
    $ Sabia.face = "annoyed2"
    $ Avion.face = "angry"
    avion "This plan seems underhanded and dishonorable. The Gods watch, they will not be pleased."
    $ Sabia.face = "irritated2"
    avion "Pray to your own witch-god that I find a worthy heart."
    $ Avion.face = "normal"
    s "..."
    $ Sabia.face = "normalopen"
    s "Is that a yes, or a no?"
    $ Sabia.face = "normal"
    avion "Yes. I will watch."
    $ Sabia.face = "normalopen"
    s "Good."
    scene bg black with dissolve
    pause (0.1)
    scene bg road
    show Sabia at left
    with dissolve
    $ Sabia.face = "sad3"
    s "This cart is heavier than I thought..."
    $ Sabia.face = "sad1"
    "Avion had taken the cart up until the edge of the other bandit's territory, and Sabia had taken over from there."
    "Lugging a cart behind her was far different to the decisive, practiced form of combat. She was quickly out of breath."
    $ Sabia.face = "sad3"
    s "I shouldn't have to go too far..."
    $ Sabia.face = "normalopen"
    s "It's not a windy day, screams should carry far."
    $ Sabia.face = "irritated2"
    "Sabia frowned for a moment."
    $ Sabia.face = "normalopen"
    s "I hope this works. I don't want to be both out the lundils, and not succeed either."
    s "I better go a bit farther."
    $ Sabia.face = "normal"
    scene bg black with dissolve
    "Another sweaty half hour passed before Sabia felt she would be far enough into their territory."
    scene bg forest
    show Sabia at left
    with dissolve
    "She let go of the cart, and cleared her throat softly."
    "Sabia screamed, a very uncharacteristic, high-pitched screech that she tried to infuse with as much fright and terror as she could."
    hide Sabia with moveoutright
    "The shrill shrieks of 'bandit!' and 'Let me go, take it!' reverberated through the forest, bouncing of the trees and going farther and farther out."
    "As she ran, she made sure to leave signs behind her. Snapped twigs, knocks on tree trunks. Anything that even a half inept tracker could pick up on."
    "After twenty minutes of running, she slowed down into a brisk pace."
    show Sabia at left
    show Avion at right
    with dissolve
    "Avion slid into step next to Sabia, emerging silently from some underbrush."
    avion "Hmph. They found the cart."
    $ Sabia.face = "normalopen"
    s "Great. They'll be out of it by tomorrow, I expect. Makes the job much easier."
    $ Sabia.face = "normal"
    $ Avion.face = "angry"
    avion "You show no strength in this. It is the act of someone weak."
    $ Sabia.face = "annoyed2"
    avion "Your spirit would not make a worthy ritual."
    $ Avion.face = "normal"
    $ Sabia.face = "annoyed1"
    s "Yeah. Okay. Look, I'm not going to risk my life more than I have to, alright?"
    s "Deserting-soldiers-become-bandits will down every drop of booze they come across - if they are disorganised."
    $ Sabia.face = "normalopen"
    s "It's easier and safer."
    $ Sabia.face = "annoyed2"
    $ Avion.face = "normaleyes"
    avion "But you agree that there is no strength in this?"
    $ Sabia.face = "normalopen"
    $ Avion.face = "angry"
    s "I... sure."
    $ Sabia.face = "annoyed1"
    s "I agree."
    $ Sabia.face = "normal"
    "Avion snorted in disgust."
    $ Sabia.face = "normalopen"
    s "We'll come back later tonight."
    $ Sabia.face = "normal"
    $ Avion.face = "normal"
    avion "Very well. Come and get me then."
    $ Sabia.face = "normalopen"
    s "Fine."
    $ Sabia.face = "normal"
    hide Avion with moveoutright
    "Avion walked off ahead of Sabia, and she followed behind a few hundred yards on the way back to Kira's camp."
    scene bg black with dissolve
    jump ef3_kira_camp


label ef3_rival_camp_cart2:
    $ avion_quest = 6
    $ Sabia.face = "normalopen"
    s "Alright. It's been a good several hours. Let's head back."
    $ Sabia.face = "normal"
    "Avion pulled himself to his feet, took a hold of the almost-Sabia-tall haft of his wicked, serrated macuahuitl, and grunted."
    scene bg black with dissolve
    "The two traveled in silence back to the other bandit camp. Sabia's plan felt a lot more grim now that she was heading back."
    "At least in a battle, the death is in the heat of the moment."
    scene bg forest
    show Sabia at left
    show Avion at right
    with dissolve
    "They arrived just out of earshot of the camp. Immediately, Sabia felt a surge of vindication."
    "Her plan had worked - the cart was empty, and bottles of alcohol littered the camp ground, in amongst drunk and passed out bandits."
    $ Sabia.face = "normalopen"
    s "Ready?"
    $ Sabia.face = "normal"
    "Avion grunted."
    $ Sabia.face = "normalopen"
    s "Fine, let's go."
    $ Sabia.face = "angry2"
    $ Avion.face = "angry"
    hide Sabia
    hide Avion
    with dissolve
    "The hulking frame of the minotaur ripped branches and trees out of the way as he barrelled into the clearing."
    $ Avion.face = "angryeyes"
    $ GenericOrc1.extras = ["Loincloth", "Beard1", "Axe"]
    $ GenericOrc1.face = "suspicious"
    $ GenericOrc2.extras = ["Loincloth", "Hair", "Axe"]
    $ GenericOrc2.face = "angry"
    $ Humansoldier.face = "surprised"
    show GenericOrc1 at center
    show GenericOrc2 at right
    show Humansoldier at left
    with dissolve
    avion "PROVE YOUR HEART!"
    show Avion at left with moveinleft:
        xzoom -1
    $ renpy.show("GenericOrc1mask", at_list=[center], what=AlphaBlend(Transform("GenericOrc1", alpha=0.9), "GenericOrc1", bloodhit_effect, alpha=True))
    $ renpy.show("GenericOrc2mask", at_list=[right], what=AlphaBlend(Transform("GenericOrc2", alpha=0.9), "GenericOrc2", bloodhit_effect, alpha=True))
    $ renpy.show("Humansoldiermask", at_list=[left], what=AlphaBlend(Transform("Humansoldier", alpha=0.9), "Humansoldier", bloodhit_effect, alpha=True))
    pause(0.1)
    hide GenericOrc1
    hide GenericOrc1mask
    hide GenericOrc2
    hide GenericOrc2mask
    hide Humansoldier
    hide Humansoldiermask
    with dissolve
    "Several bandits were cut in half with the first few massive cleaves of his weapon."
    "Screams and cries erupted, but everyone was slow to act, confused and disoriented."
    hide Avion with dissolve
    show Sabia at left with dissolve
    "Sabia hadn't expected Avion to charge in like that - the plan had been to do it quietly and efficiently."
    "Fleeing bandits ran towards Sabia, desperate to get away from the massacre behind them."
    $ enemy_level = 9
    $ enemy_maxhp = 400
    $ enemy_hp = enemy_maxhp
    $ enemy_type = 1
    $ enemy_skills = [Enemyattack,Enemyattack,Enemyquickattack]
    $ enemy_attack = 65
    $ enemy_defense = 0
    $ enemy_magdefense = 0
    $ GenericOrc1.face = "angry"
    $ GenericOrc1.extras = ["Loincloth", "Axe", "Hair"]
    $ player = Sabia
    $ enemy = GenericOrc1
    call duel
    if _return != "Victory":
        $ avion_quest_lost_fight = True
        "Sabia was overwhelmed by bandits, but Avion came to her rescue."
        jump ef3_rival_camp_cart3
    $ enemy_level = 9
    $ enemy_maxhp = 400
    $ enemy_hp = enemy_maxhp
    $ enemy_type = 1
    $ enemy_skills = [Enemyattack,Enemyattack,Enemyquickattack]
    $ enemy_attack = 65
    $ enemy_defense = 0
    $ enemy_magdefense = 0
    $ GenericOrc2.face = "angry"
    $ GenericOrc2.extras = ["Loincloth", "Axe", "Beard1"]
    $ player = Sabia
    $ enemy = GenericOrc2
    call duel
    if _return != "Victory":
        $ avion_quest_lost_fight = True
        "Sabia was overwhelmed by bandits, but Avion came to her rescue."
        jump ef3_rival_camp_cart3
    $ enemy_level = 9
    $ enemy_maxhp = 400
    $ enemy_hp = enemy_maxhp
    $ enemy_type = 1
    $ enemy_skills = [Enemyattack,Enemyattack,Enemyquickattack]
    $ enemy_attack = 65
    $ enemy_defense = 0
    $ enemy_magdefense = 0
    $ GenericOrc1.face = "angry"
    $ GenericOrc1.extras = ["Loincloth", "Axe", "Shoulder", "Strap"]
    $ player = Sabia
    $ enemy = GenericOrc1
    call duel
    if _return != "Victory":
        $ avion_quest_lost_fight = True
        "Sabia was overwhelmed by bandits, but Avion came to her rescue."
        jump ef3_rival_camp_cart3
    $ Sabia.face = "normal"
    show Sabia at left with dissolve
    "Sabia stepped back, pushing one of the bandits off of her blade with a foot."
    "He crumpled to the ground."
    jump ef3_rival_camp_cart3


label ef3_rival_camp_cart3:
    show Sabia at left with dissolve
    $ Sabia.face = "angry1"
    s "What was that?! The plan was to do it quietly, efficiently! You woke the entire camp up!"
    $ Sabia.face = "angry2"
    $ Banditgirl.face = "worried"
    show Avion at right with moveinright
    show Banditgirl at right with dissolve
    $ Banditgirl.face = "worried"
    show bgirltears at right
    "Avion's arm was behind him as he walked through the clearing, back towards Sabia. A protesting girl was screaming, dragged along by his iron grip."
    "He ignored Sabia's protests."
    $ Avion.face = "angry"
    avion "There were no worthy hearts for ritual. Only... this."
    $ Banditgirl.face = "sadopen"
    bandit1 "Please! No! Let me go, I didn't - I won't do anything again! I'm not like these others, please!"
    $ Banditgirl.face = "worried"
    $ Sabia.face = "angry1"
    $ Avion.face = "normal"
    s "You're not going to-"
    $ Sabia.face = "irritated1"
    jump ef3_rival_camp_aftermath


label ef3_rival_camp_aftermath:
    show Banditgirl at right
    show bgirltears at right
    with dissolve
    avion "Of course not. She is not worthy of being Tlactina. I will break her spirit in ritual. It is almost as good as a heart."
    $ Banditgirl.face = "sadopen"
    bandit1 "What? I- no, please. Please. Let me go, I won't raid or pillage or anything... I didn't want to, to start with... please!"
    $ Banditgirl.face = "worried"
    $ Sabia.face = "closed1"
    "Sabia remembered from her time in the war as an officer. Some of the female officers had been captured."
    "The treatment they received was not kind. Sabia had always maintained that she would prefer death."
    $ Sabia.face = "closed2"
    $ Banditgirl.face = "sad"
    s "(But maybe death isn't necessary here. Maybe I can release her and Avion won't notice until it's too late)."
    s "(Of course... he might not be too pleased.)"
    menu:
        "Free the bandit.":
            $ freedom += 1
            $ avion_quest_bandit_freed = True
            $ Sabia.face = "normal"
            "Waiting for the right opportunity, Sabia followed behind Avion and his new prisoner for a short while."
            $ Banditgirl.face = "worried"
            "It was clear to her that he was getting frustrated with the woman. He could not take her here and now it seemed - it would not satisfy the needed rituals."
            "Avion's nostrils flared, and his voice had become a constant, angry grunt. Every now and then he yanked the sniffling prisoner, forcing her to hasten."
            "Sabia saw her opportunity to free the girl."
            $ Sabia.face = "normalopen"
            $ Avion.face = "smirk"
            $ Banditgirl.face = "sad"
            s "Avion - you fought well. You don't need to bother yourself with trekking that woman back. I will look after her."
            $ Sabia.face = "normal"
            avion "..."
            $ Avion.face = "normal"
            avion "Very well. I have little desire to listen to her pathetic whining."
            avion "She has lost. She should submit."
            $ Sabia.face = "normalopen"
            s "Of course. That only makes sense."
            $ Sabia.face = "normal"
            "Sabia ignored the whimpering pleading of the poor bandit girl, her eyes wide with desperation."
            $ Avion.face = "angry"
            call shake ("h")
            $ Banditgirl.face = "worried"
            "Avion threw the girl toward Sabia. She landed with a heavy thud on the ground, and tried pulling herself up. She failed. Her bound arms prevented it."
            hide Avion with dissolve
            "Helping her up, Sabia looked forward and saw Avion had already begun walking ahead of them."
            $ Banditgirl.face = "sadopen"
            bandit1 "Please... please, please. Don't let me go back with him... I'll do... I'll do whatever, I don't want a minotaur to-"
            $ Banditgirl.face = "worried"
            $ Sabia.face = "angry1"
            s "Shut. Up."
            s "Don't talk."
            $ Sabia.face = "normal"
            "Sabia's crass words seemed to tip the girl back off the precipice, and her eyes swam with tears."
            "They continued following Avion. Slowly, steadily, the minotaur pulled ahead of them until he was only just in sight, and then he was gone."
            "Waiting another few minutes just to be sure, Sabia stopped."
            $ Sabia.face = "normalopen"
            $ Banditgirl.face = "sad"
            s "I'm letting you go."
            $ Sabia.face = "angry2"
            $ Banditgirl.face = "sadopen"
            bandit1 "I- what?! Really?! Oh, thank you, thank you!"
            $ Sabia.face = "angry1"
            $ Banditgirl.face = "sad"
            s "SHH!"
            s "Do you want Avion to come back?"
            $ Sabia.face = "normal"
            "The bandit's lips snapped shut."
            "Sabia quickly untied the girl's bonds."
            $ Sabia.face = "normalopen"
            s "Run as far and as long as you can. I don't know if he will try to track you down."
            $ Sabia.face = "normal"
            "She nodded."
            $ Sabia.face = "normalopen"
            s "Don't go back to being a bandit. Find a new life. Go to Carchedon, go to Erxia."
            $ Sabia.face = "normal"
            $ Banditgirl.face = "sadopen"
            bandit1 "Thank you."
            $ Sabia.face = "normalopen"
            s "Hurry."
            $ Sabia.face = "normal"
            hide bgirltears
            "The girl wiped the tears from her face, nodded, and turned. She started to run away through the forest."
            hide Banditgirl with moveoutright
            "Sabia watched her flee for a few seconds before turning, and heading after Avion."
            "She judged it about ten minutes before she heard Avion round back and coming toward her."
            "As their eyes locked, Sabia could feel the anger burning there even from their vantage."
            show Avion at right with moveinright
            $ Avion.face = "angryeyes"
            avion "Where is my prize?"
            "The words were flat, but Sabia could sense the fury."
            $ Sabia.face = "normalopen"
            s "I released her. I wasn't going to let her..."
            $ Sabia.face = "irritated2"
            $ Avion.face = "angry"
            avion "That was not for you to decide."
            avion "You do not understand what you have done."
            $ Sabia.face = "normalopen"
            s "I do."
            $ Sabia.face = "surprised1"
            $ Avion.face = "normal"
            avion "Then you understand you must take her place as my prize, to sate the rituals demanded of me."
            $ Sabia.face = "angry1"
            s "What?!"
            $ Avion.face = "angry"
            s "Absolutely not!"
            $ Sabia.face = "irritated2"
            $ Avion.face = "normal"
            avion "I do not ask."
            avion "This must be done, to thank the Gods for the fight. For their protection. To offer my thanks."
            avion "I will take you when we return."
            $ Sabia.face = "normal"
            s "..."
            if sub>dom:
                $ Sabia.face = "sad2"
                $ Avion.face = "normaleyes"
                avion "Do you have issue with this? If so, then you should not have violated my ritual prize."
                $ Avion.face = "normal"
                avion "This is your own fault."
                s "(I can't have a minotaur being antagonistic toward me...)"
                $ Sabia.face = "sad3"
                s "Well... I know that it's your Gods that demand it... but my Goddess does not agree with rape of prisoners."
                $ Sabia.face = "sad2"
                $ Avion.face = "angry"
                avion "I do not care what your witch-god does or does not agree with. I care only for my Gods, and the rituals that must be observed."
                $ Sabia.face = "surprised1"
                if avion_quest_lost_fight == True:
                    avion "Losing your fight only makes me think that you are less worthy of being anything but a pleasure slave in Naltaan."
                show Avion behind Sabia at center with move
                $ temp = Sabia.armor
                $ Sabia.unequip(Sabia.armor)
                "Avion's lips curled back, and he took a step forward. He took hold of Sabia, and with his other hand, ripped her clothes from her."
                call avion_ritual_rough
                play music forest fadeout 2.0 fadein 2.0
                $ Sabia.equip(temp)
                scene bg black with dissolve
                pause (0.1)
                jump eastern_frontier_map
            else:
                $ Sabia.face = "angry1"
                $ Avion.face = "angry"
                s "Absolutely not."
                $ Sabia.face = "angry2"
                $ Avion.face = "angryeyes"
                avion "The Gods demand it. You do not have a choice! You have done this yourself!"
                $ Sabia.face = "angry1"
                $ Avion.face = "angry"
                s "Well, my witch-god as you call her doesn't look kindly on raping a prisoner."
                s "And as we have both you and I - and two differing beliefs - we have satisfied both by you finding a worthy heart, and by me releasing the prisoner."
                $ Avion.face = "normal"
                $ Sabia.face = "normal"
                avion "..."
                $ Sabia.face = "normalopen"
                s "You wouldn't be able to handle me, anyway."
                s "I wouldn't worry about it, this is probably for the best."
                $ Sabia.face = "normal"
                if avion_quest_lost_fight == True:
                    avion "..."
                    $ Sabia.face = "irritated2"
                    $ Avion.face = "smirk"
                    avion "You say this, but you are less than pathetic. You lost to malnourished, weak bandits and needed my strength to save you."
                else:
                    avion "..."
                    $ Avion.face = "smirk"
                    avion "A minotaur, not able to handle a human? You do not understand our endurance or might."
                $ Sabia.face = "irritated1"
                $ Avion.face = "normal"
                avion "You would lose your mind to pleasure and your body to orgasm quickly."
                $ Sabia.face = "normalopen"
                s "Sure, maybe some peasant, or farmer's wife who has spent her life in the fields."
                $ Sabia.face = "happy2"
                $ Avion.face = "normaleyes"
                s "But a human who knows what she's doing? You'd blow your load before you start thrusting."
                $ Sabia.face = "normal"
                avion "That is wrong. Naltaan has many human women and-"
                $ Sabia.face = "normalopen"
                $ Avion.face = "angry"
                s "But you aren't in Naltaan, are you? Is that why, you couldn't cut it?"
                $ Sabia.face = "normal"
                $ Avion.face = "normal"
                avion "If you seem so sure, then prove it. Prove your spirit."
                $ Sabia.face = "closed2"
                s "(...Avion isn't outright furious... but I can sense his anger. It will be better to just deal with it and not have an antagonistic minotaur angry at me...)"
                $ Sabia.face = "normalopen"
                $ Avion.face = "smirk"
                s "Fine. Once we get back to camp, we'll do your ritual. First one to cum, loses. They have to admit they were wrong."
                $ Sabia.face = "normal"
                avion "Hmph. Fine. There is no chance I lose."
                "Sabia and Avion headed back to the camp."
                scene bg black with dissolve
                "Sabia and Avion threw taunts and threats back and forth almost playfully, but Sabia still sensed that Avion was angry."
                "Before they reached the camp, Avion had turned to her and told her to strip. The ritual would be here."
                "Sabia smirked, taunting Avion that he was too eager, that he couldn't wait."
                call avion_ritual
                play music forest fadeout 2.0 fadein 2.0
                jump avion_ritual_post_scene
        "Let Avion have her.":
            $ slavery += 1
            "But still, the woman was no friend to her. And she had little interest in being the reason a minotaur's ritual was ruined."
            $ Avion.face = "smirk"
            $ Banditgirl.face = "worried"
            "She ripped some fabric off the woman's clothing, and shoved it into the bandit's mouth."
            $ Sabia.face = "normalopen"
            s "Don't try to speak."
            $ Avion.face = "normal"
            "The two continued back to Kira's camp, silence interjected by the bandit's tearful whimpering."
            $ Sabia.face = "normalopen"
            s "I'll have to report the job done to Kira."
            $ Sabia.face = "closed2"
            s "(I've always been interested in what exactly the heart ritual entails... I know it happens over the next three days. Maybe I could look into it?)"
            scene bg black with dissolve
            jump eastern_frontier_map


label avion_ritual_post_scene:
    scene bg black
    scene bg cave
    with dissolve
    $ temp = Sabia.armor
    $ Sabia.unequip(Sabia.armor)
    show Sabia at left
    show Avion at right
    with dissolve
    "Avion had been mostly quiet as he let Sabia down, and she cleaned herself up. Almost glowering."
    avion "It seems I underestimated you. You are... tougher than I thought. In more ways than one."
    s "(That's the closest thing to a compliment I've been given by him. I'll take it.)"
    s "Same here."
    avion "..."
    "Sabia felt like Avion did not particularly want to talk any more to her, given his glowering countenance."
    "But she still had to check."
    s "So do we still have an issue with the prisoner?"
    "Avion looked at her for a long minute, then shook his head."
    avion "No."
    s "Good."
    "Avion took a seat, and Sabia put on her clothes before leaving him alone."
    scene bg black with dissolve
    $ Sabia.equip(temp)
    jump ef3_kira_camp


label ef3_chase_hal:
    $ v10lynn_hal_chase = 5
    $ Sabia.face = "normal"
    scene bg countryside
    show Sabia at left
    with dissolve
    "Sabia followed the path out of Avarton, heading south-east off the track."
    "Hal was not good at hiding his tracks, and even Sabia managed to follow them easily."
    "He had made a makeshift camp with a small fire in a thicket of trees several miles out."
    $ Sabia.face = "normalopen"
    s "Hmm... waiting so close isn't what I'd be doing. But... maybe he's not sure where to go. Where is there to go for a Whitecrest soldier if you can't go to Whitecrest, Avarton or any of the villages, anyway?"
    $ Sabia.face = "normal"
    "Sabia frowned, and then shook her head. No time to be worried about him."
    scene bg countryside
    $ Humansoldier.face = "normal"
    show Humansoldier at right
    with dissolve
    pause (1)
    show Sabia behind Humansoldier at screen_farright with moveinright
    "She made her way toward him, moving from behind. She was quiet enough that he didn't hear her, or he was simply not paying attention."
    "Slowly, she drew her weapon and held the blade to Hal's neck."
    $ Humansoldier.face = "surprised"
    hal "Oh, Relona! No!"
    "Fear was etched on his face, and he darted for his sword."
    $ Sabia.face = "angry2"
    "Sabia had caught his eyes and managed to beat him, grabbing hold of the weapon his trembling hand had reached for."
    $ Sabia.face = "irritated2"
    hal "I haven't said... I haven't said {i}anything!{/i} Please! I left... to be out of the way. I didn't, please."
    $ Sabia.face = "normalopen"
    s "What are you talking about?"
    $ Sabia.face = "normal"
    $ Humansoldier.face = "sad"
    hal "You're sent by..."
    "He paused for a moment, looking Sabia over."
    $ Sabia.face = "question1"
    hal "You're not from-"
    $ Sabia.face = "normalopen"
    s "From Lynn? Hmph. No."
    $ Sabia.face = "normal"
    $ Humansoldier.face = "surprised"
    hal "How can... how can I be sure? Your hair! You look like Archmage Lynn..."
    $ Sabia.face = "normalopen"
    $ Humansoldier.face = "sad"
    s "Because if Lynn were after you, we wouldn't be having this conversation."
    s "In fact, she wouldn't be after you. You'd be in the dungeons already."
    s "I'm... from a separate mage faction."
    $ Sabia.face = "normal"
    "He frowned for a moment."
    $ Humansoldier.face = "surprised"
    hal "You... you're a mage too?"
    $ Sabia.face = "normalopen"
    s "Yes. So don't try my patience."
    s "I think you have some useful information about Lynn that I would like to hear."
    $ Sabia.face = "normal"
    $ Humansoldier.face = "surprised"
    "He shook his head violently."
    $ Sabia.face = "irritated2"
    hal "No. No. I do not. That is not true."
    s "Hmm."
    $ Sabia.face = "angry1"
    $ Humansoldier.face = "sad"
    s "You were just pleading, and saying you hadn't said anything."
    $ Sabia.face = "irritated2"
    "The man tightened his lips noticeably."
    show Sabia at center with move
    "Sabia passed him back his sword."
    $ Sabia.face = "normalopen"
    s "Look, I'm going to need that information."
    menu v10lynn_hal_menu_forest:
        "Convince him nicely.":
            $ v10lynn_hal_deal = "convince"
            $ Sabia.face = "happy3"
            $ Humansoldier.face = "surprised"
            s "There's no reason not to tell me."
            $ Sabia.face = "normal"
            hal "I disagree. There are many reasons. Staying alive, primarily."
            $ Sabia.face = "normalopen"
            s "Sure. But if I'm sent by Lynn - then I would simply be taking you back to Whitecrest."
            s "I'd be able to provide more than enough authority to anyone here to help me take you back."
            $ Sabia.face = "happy2"
            $ Humansoldier.face = "sad"
            s "If that's not what is happening, then clearly I am not sent by Lynn."
            s "Tell me what you know, and it might just help me solve that annoying Lynn problem."
            $ Sabia.face = "normal"
            hal "You... speak some sense."
            hal "And living here in fear for these past few weeks... I've not enjoyed it. Fine."
            $ Humansoldier.face = "normal"
            hal "I'll tell you what I know, and hopefully you can use it to make sure I don't have to look over my shoulder."
            $ Sabia.face = "normalopen"
            s "You're going to be looking over your shoulder for an awful long time if you stay around here. I'd suggest you move on. Carchedone, probably."
            $ Sabia.face = "normal"
            $ Humansoldier.face = "sad"
            hal "Perhaps. You might be right. Anyway, you were after information..."
            jump v10lynn_information
        "Threaten.":
            $ v10lynn_hal_deal = "threat"
            $ Sabia.face = "angry1"
            s "I'm not really wanting to waste any more time with this. I need what you know."
            $ Sabia.face = "irritated2"
            "He shook his head."
            hal "Not a chance... if I did know something, I wouldn't be able to risk anyone knowing it as well."
            $ Sabia.face = "closed2"
            "Sabia sighed."
            $ Sabia.face = "normalopen"
            $ Humansoldier.face = "sad"
            s "Look. You've seen what Lynn can do right?"
            s "How do you fancy being ripped apart from the inside, and your innards splattered everywhere?"
            s "Or maybe I'll just leave an enchantment on your room so you can't leave."
            $ Sabia.face = "happy2"
            $ Humansoldier.face = "surprised"
            s "A few words on a piece of parchment with the right address, and I am sure Lynn will be right along to pick you up. After all, if you're not going to actually give me what I want..."
            $ Sabia.face = "normal"
            hal "..."
            $ Humansoldier.face = "sad"
            hal "They probably already know and just haven't found me yet... I'm not staying here much longer, I'll be moving on."
            $ Sabia.face = "normalopen"
            s "Information, now."
            $ Sabia.face = "normal"
            "The man's head sunk, and he gave a depressed nod."
            hal "Fine. You leave me no choice but to hope that telling you won't lead anything back to me."
            $ Sabia.face = "normalopen"
            $ Humansoldier.face = "normal"
            s "Don't worry. I have more... issues with Lynn than you do."
            jump v10lynn_information
        "Offer 150 lundils." if v10lynn_hal_deal_attempt_bribe == False:
            if money < 150:
                s "(Unfortunately I don't have enough money to bribe him. I need to think of something else.)"
                jump v10lynn_hal_menu_forest
            $ v10lynn_hal_deal_attempt_bribe = True
            $ Sabia.face = "angry1"
            $ Humansoldier.face = "sad"
            s "And I don't have time to argue this and that and try to convince you. I'll pay you. Enough that you'll be able to get out of Whitecrest and Lundar's borders."
            s "Head south to Carchedone if you want. Or north to Erxia - though I wouldn't recommend going through Whitecrest or Lundar to do so."
            $ Sabia.face = "normalopen"
            s "One hundred and fifty lundils, along with what you have here. That should get you out. You're not going to get a better offer."
            $ Sabia.face = "irritated2"
            "Sabia watched him considering. She was sure he was trying to decide whether the risk of revealing anything was worth the potential of escaping with enough coin to make for another region."
            "She also suspected he was wondering if he were going to be betrayed after."
            $ Humansoldier.face = "normal"
            "He shook his head slowly."
            $ Sabia.face = "irritated1"
            hal "One hundred and fifty lundils... it's a nice offer. It won't get me far though. I had to leave so much behind in Avarton. I can't go back for it now."
            $ Humansoldier.face = "sad"
            hal "Not after you've been asking questions. My fleeing is bound to pique some interest."
            jump v10lynn_hal_menu_forest
        "Fine. 500 lundils." if v10lynn_hal_deal_attempt_bribe == True:
            if money < 500:
                s "(Unfortunately I don't have enough money to bribe him. I need to think of something else.)"
                jump v10lynn_hal_menu_forest
            $ v10lynn_hal_deal = "bribe"
            $ money -= 500
            $ Sabia.face = "angry1"
            $ Humansoldier.face = "surprised"
            s "Five hundred. That's more than enough."
            $ Sabia.face = "irritated1"
            $ Humansoldier.face = "sad"
            "He spent a moment considering it, before reluctantly nodding."
            $ Sabia.face = "normal"
            hal "Fine... I'm not in a position to not accept that. I just hope it can get me to Carchedon."
            jump v10lynn_information


label ef3_graks_camp:
    scene bg countryside with dissolve
    if v10tekrok_quest_met_grak == False:
        $ v10tekrok_quest_met_grak = True
        jump ef3_graks_camp_first_visit
    menu:
        "Ask for information." if v10tekrok_grak_information == False:
            $ GenericOrc2.extras = ["Loincloth", "Shoulder", "Strap", "Necklace", "Beard2"]
            $ GenericOrc2.face = "normal"
            $ Sabia.face = "normal"
            show Sabia at left
            show GenericOrc2 at right
            with dissolve
            if v10tekrok_camp_explain == True:
                $ v10tekrok_grak_information = True
                $ GenericOrc2.face = "normalopen"
                grak "Hmph. Very well."
                $ GenericOrc2.face = "normal"
                jump ef3_grak_ellia1
            if v10tekrok_ask_information == False:
                $ v10tekrok_ask_information = True
                $ v10tekrok_camp_trust -= 1
                $ Sabia.face = "normalopen"
                s "I can see that all of you aren't particularly enthused with a human being here."
                $ Sabia.face = "irritated2"
                $ GenericOrc2.face = "suspicious"
                "Grak spat on the ground."
                $ GenericOrc2.face = "angry"
                grak "Not in this purpose. Grak is thinking he would be more pleased if you had come in shackles, ready to serve orc masters."
                $ GenericOrc2.face = "suspicious"
                $ Sabia.face = "annoyed1"
                s "So, why don't you just give me the information Tekrok wants, and I will be on my way."
                $ Sabia.face = "irritated2"
                "The orcs narrowed their eyes suspiciously."
                $ GenericOrc2.face = "angry"
                grak "This is not a good idea. Grak is thinking that to give information so freely is foolish."
                $ Sabia.face = "irritated1"
                grak "You will explain to Grak why Tekrok has sent a human to retrieve this. Grak says you will do this now."
                jump ef3_graks_camp
            else:
                $ GenericOrc2.face = "suspicious"
                "Grak growled."
                $ Sabia.face = "irritated2"
                $ GenericOrc2.face = "angry"
                grak "You will explain why Tekrok has sent a human to do an orc's job. Now. Before Grak and others break you."
                $ GenericOrc2.face = "suspicious"
                jump ef3_graks_camp

        "Explain why Tekrok sent you." if v10tekrok_camp_explain == False:
            $ v10tekrok_camp_explain = True
            $ GenericOrc2.extras = ["Loincloth", "Shoulder", "Strap", "Necklace", "Beard2"]
            $ GenericOrc2.face = "normal"
            $ Sabia.face = "normalopen"
            show Sabia at left
            show GenericOrc2 at right
            with dissolve
            s "Alright."
            s "I realize that Tekrok probably doesn't send humans very often to do this sort of work."
            $ GenericOrc2.face = "angry"
            grak "Tekrok does not."
            $ GenericOrc2.face = "suspicious"
            $ Sabia.face = "normalopen"
            s "You have little idea of what is happening in camp right now, yes?"
            $ Sabia.face = "normal"
            $ GenericOrc2.face = "normalopen"
            grak "Grak and others know that the Warchief is gone."
            grak "Other than this, Grak and others are knowing little."
            $ GenericOrc2.face = "normal"
            "Sabia nodded."
            $ Sabia.face = "normalopen"
            s "The bandit issue is something that is growing, and Lundar's attempts to annex Whitecrest continue."
            s "There's a lot of tension and pressure. All of it was exacerbated greatly when Groknak-"
            $ Sabia.face = "irritated2"
            $ GenericOrc2.face = "angry"
            grak "Warchief Groknak."
            $ GenericOrc2.face = "suspicious"
            $ Sabia.face = "normal"
            "Sabia nodded apologetically."
            $ Sabia.face = "normalopen"
            s "When Warchief Groknak disappeared. All three captains are doing their best to keep an eye on the situation in Whitecrest, as well as two eyes on each other."
            s "Rokgrid and Dajrab have orcs watching Tekrok's forces. Anyone going in and out is a good target to follow."
            $ Sabia.face = "normal"
            $ GenericOrc2.face = "angry"
            grak "And you are not?"
            $ GenericOrc2.face = "suspicious"
            $ Sabia.face = "normalopen"
            s "Not particularly. I'm more adept at covering my tracks and subterfuge than what Tekrok has at his disposal without me. And I am often in and out of Grok og Dar."
            s "My departure is something less important to be noticed. I can come and get the information with much less risk than one of Tekrok's other orcs."
            $ Sabia.face = "normal"
            "Grak grunted, leaning forward and resting a hand on his knee."
            $ GenericOrc2.face = "angry"
            grak "Grak is still not liking this. For Tekrok to be using a human like this."
            $ GenericOrc2.face = "suspicious"
            $ Sabia.face = "irritated2"
            "He spat on the ground in front of Sabia."
            $ GenericOrc2.face = "angry"
            grak "It is an insult to Grak and others."
            $ GenericOrc2.face = "suspicious"
            $ Sabia.face = "irritated1"
            $ GenericOrc2.face = "angry"
            grak "But Grak is also thinking... you may not be sent by Grak at all. Information and words can be gained. Grak and orcs will be watching you while you are in this camp."
            grak "Walk with care, human."
            $ GenericOrc2.face = "suspicious"
            $ Sabia.face = "annoyed1"
            s "I am sent by Tekrok, truly."
            $ Sabia.face = "irritated1"
            $ GenericOrc2.face = "normalopen"
            grak "Hmph... the words you spoke were correct, and Grak can see why Tekrok would have sent you."
            $ GenericOrc2.face = "angry"
            grak "Still, Grak is thinking that this does not lessen the insult if you have been sent by Tekrok. You will tell Tekrok of this when you return."
            jump ef3_graks_camp

        "Offer alcohol." if v10tekrok_camp_alcohol == False:
            $ GenericOrc2.extras = ["Loincloth", "Shoulder", "Strap", "Necklace", "Beard2"]
            $ GenericOrc2.face = "normal"
            $ Sabia.face = "normal"
            show Sabia at left
            show GenericOrc2 at right
            with dissolve
            if v10tekrok_grak_information == False:
                s "(I should probably get the information first before they all end up too drunk to tell me.)"
                jump ef3_graks_camp
            if v10tekrok_camp_explain == True:
                $ v10tekrok_camp_alcohol = True
                $ GenericOrc2.face = "normalopen"
                grak "Yes, Grak will take this. It has been many moons since Grak and others have been drinking."
                $ GenericOrc2.face = "normal"
                "Sabia produced the two small bottles, unsure how annoyed he would be with the small amount."
                "But instead, a wide grin spread across Grak's face."
                $ GenericOrc2.face = "smile3"
                grak "Ah! Good. Grak is pleased. This will last many nights."
                $ GenericOrc2.face = "normal"
                $ Sabia.face = "normalopen"
                s "Really? There's... not much there."
                $ Sabia.face = "irritated2"
                $ GenericOrc2.face = "normalopen"
                grak "It is strong. Very strong. Even for an orc. Too strong for a human."
                $ GenericOrc2.face = "smile1"
                grak "If you are lucky, maybe Grak will share some with you. Makes it easier to break worthless, weak women into proper slaves."
                $ Sabia.face = "annoyed2"
                $ GenericOrc2.face = "smile3"
                grak "A more useful life than you would have lived, Grak is thinking."
                $ GenericOrc2.face = "normal"
                "A round of nodding assent waved through the small camp of orcs as they agreed."
                $ Sabia.face = "normal"
                $ GenericOrc2.face = "normalopen"
                grak "Grak and others will be drinking this later."
                $ GenericOrc2.face = "normal"
                jump ef3_graks_camp_drinking
            if v10tekrok_offer_alcohol == False:
                $ v10tekrok_offer_alcohol = True
                $ Sabia.face = "normalopen"
                $ GenericOrc2.face = "suspicious"
                s "Tekrok sent these bottles of alcohol along with me, as well."
                $ Sabia.face = "happy3"
                s "Perhaps a drink will take a bit out of the tension?"
                $ Sabia.face = "normal"
                grak "..."
                $ GenericOrc2.face = "angry"
                grak "Grak is thinking that it is best you explain the situation first."
                $ Sabia.face = "irritated2"
                grak "Getting drunk with an unknown human... Grak suggests that it is not a good idea."
                grak "You will explain why Tekrok sent a human. Now. Before Grak and others break you."
                $ GenericOrc2.face = "suspicious"
                jump ef3_graks_camp
            else:
                $ GenericOrc2.face = "suspicious"
                "Grak growled."
                $ Sabia.face = "irritated2"
                $ GenericOrc2.face = "angry"
                grak "You will explain why Tekrok has sent a human to do an orc's job. Now. Before Grak decides to see you used properly."
                $ GenericOrc2.face = "suspicious"
                jump ef3_graks_camp
        "Leave.":

            $ GenericOrc2.extras = ["Loincloth", "Shoulder", "Strap", "Necklace", "Beard2"]
            $ GenericOrc2.face = "normal"
            $ Sabia.face = "normal"
            show Sabia at left
            show GenericOrc2 at right
            with dissolve
            if v10tekrok_camp_explain == False and v10tekrok_camp_leave_try == False:
                $ v10tekrok_camp_leave_try = True
                $ v10tekrok_camp_trust -= 1
                $ GenericOrc2.face = "suspicious"
                "Grak stood in front of Sabia, glowering."
                $ Sabia.face = "irritated2"
                $ GenericOrc2.face = "angry"
                grak "Grak is thinking that you will not be leaving until Grak is satisfied with answers."
                grak "Or satisfied in other ways. There is little other use for a human female, Grak is thinking."
                grak "Grak is doubting Tekrok will be upset to learn that his messenger returns as a proper, orc-obedient human slave."
                $ GenericOrc2.face = "suspicious"
                $ Sabia.face = "sad1"
                "Other orcs nearby glanced over. Sabia noted that they were already prepared to move, watching Sabia carefully. She was surprised given the orc's boasts."
                "He gestured to seat back down. Sabia did not think it a good idea to disagree with Grak."
                jump ef3_graks_camp
            elif v10tekrok_camp_explain == False and v10tekrok_camp_leave_try == True:
                $ GenericOrc2.face = "suspicious"
                "Grak growled."
                $ Sabia.face = "sad1"
                $ GenericOrc2.face = "angry"
                grak "You will explain why Tekrok has sent a human to do an orc's job. Now. Before Grak and others break you."
                jump ef3_graks_camp
            if v10tekrok_camp_explain == True and v10tekrok_grak_information == False:
                $ Sabia.face = "normalopen"
                s "I can't leave yet. Tekrok would be... less than pleased if I don't return with the information, I imagine."
                jump ef3_graks_camp
            elif v10tekrok_camp_explain == True and v10tekrok_grak_information == True:
                if v10tekrok_camp_alcohol == True:
                    "Sabia left Grak's camp, heading back to Grok og Dar."
                    jump eastern_frontier_map
                else:
                    $ Sabia.face = "normalopen"
                    s "I better not try and leave before giving Grak and his orcs that alcohol. I doubt he would be impressed."
                    jump ef3_graks_camp


label ef3_graks_camp_first_visit:
    $ Sabia.face = "normal"
    show Sabia at left
    with dissolve
    "Sabia spent most of the day looking for the location of the camp. It seemed she had picked up some tricks in tracking from past exploits that, and caught a trail."
    "Whether it was luck or not, she wasn't entirely sure. But it was fortuitous at any rate, and led to the camp Tekrok had sent her to find."
    "Sabia peered from her vantage point on the hill. Looking down, the orcs had made a small camp in the middle of a clearing. It backed onto a cliff, and provided a defensible position while being difficult to locate."
    "If Sabia hadn't known where to look, she doubted very much whether she would have found it."
    "A couple of tents had been erected, and the remnants of a small fire smoldered away."
    $ Sabia.face = "closed2"
    s "Approaching a group of veteran orcs isn't ideal... but here goes."
    $ Sabia.face = "normal"
    scene bg countryside
    with dissolve
    "Slowly, she approached until she was close enough that she could call out and the orcs would hear."
    $ Sabia.face = "sad3"
    show Sabia at left with moveinleft
    s "Hello! Tekrok has sent me!"
    s "I am - slowly - coming out to speak with you."
    $ Sabia.face = "sad1"
    "Several of the orcs surged to their feet, barking at each other as Sabia stepped into the clearing with her hands held up, away from her weapon."
    $ Sabia.face = "sad3"
    s "Tekrok sent me."
    $ Sabia.face = "sad1"
    $ GenericOrc2.extras = ["Loincloth", "Shoulder", "Strap", "Necklace", "Beard2"]
    show GenericOrc2 at right with moveinright
    "One of them took a hesitant step forward. He looked slightly older than the others, and Sabia assumed it was Grak."
    "The eyes of the orc roamed over Sabia, and his hands darted toward his side, bringing up a small canister that he held with an easy, ready grip."
    $ Sabia.face = "irritated2"
    s "(...odd.)"
    "Sabia glanced over the other orcs, seeing that they too held similar looking items. A noticeable lack of axes."
    $ Sabia.face = "closed2"
    s "(...not that I'm complaining.)"
    $ Sabia.face = "normal"
    $ GenericOrc2.face = "angry"
    grak "Grak wonders why Tekrok sends a human."
    grak "Grak is thinking, that this is a lie. Perhaps Tekrok has sent a whore to us to sate ourselves with."
    $ GenericOrc2.face = "suspicious"
    $ Sabia.face = "normalopen"
    s "It's not. Tekrok sent me to retrieve information for him."
    $ Sabia.face = "normal"
    $ GenericOrc2.face = "angry"
    grak "Hmph. Grak is thinking that this is a poor lie. Why trust important tasks to a human? There is little humans can be of help with, other than using their bodies."
    grak "If what you say is true, Grak says to speak what Grak needs to hear."
    $ GenericOrc2.face = "suspicious"
    $ Sabia.face = "closed2"
    s "(Right... the phrase. Uh... what... what was it?)"
    $ Sabia.face = "normal"
    menu:
        "Red bleeds, green flows, earth hungers.":
            jump ef3_graks_camp_wrong
        "Earth bleeds, green hungers, red flows.":
            pass
        "Red hungers, earth flows, red bleeds.":
            jump ef3_graks_camp_wrong
    $ GenericOrc2.face = "normalopen"
    grak "..."
    grak "Those are the words that Tekrok said would be spoken."
    $ GenericOrc2.face = "normal"
    $ Sabia.face = "normalopen"
    s "Good. So maybe you can lower your... uh, whatever they are?"
    $ Sabia.face = "normal"
    "The orcs glanced at Grak, before the veteran gave a curt nod."
    $ GenericOrc2.face = "normalopen"
    grak "Grak is wondering why a human is sent by Tekrok."
    grak "You will come, sit. And speak."
    $ GenericOrc2.face = "normal"
    $ Sabia.face = "irritated2"
    "Grak gestured to logs surrounding the burning coals that served as makeshift seats."
    "Sabia took a seat."
    "Grak looked at her pointedly."
    $ Sabia.face = "normal"
    "The rest of Grak's orcs looked uneasy, and on edge as they watched Sabia."
    jump ef3_graks_camp


label ef3_graks_camp_wrong:
    "Sabia knew it was wrong almost straight away. Something about how it rolled off her tongue."
    $ GenericOrc1.face = "smile2"
    grak "Grak is thinking that though you were not sent by Tekrok, you may still be of use to Tekrok by serving his soldiers."
    "Grak's expression remained steadfast, and he motion for the other orcs to surround Sabia."
    scene bg black with dissolve
    "Her hand darted to grip her weapon as the first strike came down."
    "Utterly overwhelmed, there was nothing else Sabia could do."
    jump ef3_graks_camp_badend


label ef3_grak_ellia1:
    $ ellia = Character("{image=system/elf.png}", who_ypos=-68, what_ypos=-70)
    "Grak led Sabia to one of the smaller tents in their small camp."
    $ GenericOrc2.face = "smile2"
    grak "Slave, come!"
    $ GenericOrc2.face = "normal"
    $ Sabia.face = "irritated2"
    "Sabia frowned, unsure what Grak is intending with that call."
    $ Sabia.face = "surprised1"
    show Ellia at center with moveinright
    "But her confusion was short lived. Quickly, the tent's entrance opened and an elf emerged, dragged behind one of the orcs with a vicious pull of the leash."
    $ Sabia.face = "surprised2"
    s "What...!"
    $ Sabia.face = "angry2"
    $ GenericOrc2.face = "smile3"
    $ Ellia.face = "sadopen"
    ellia "H-hello... hello Master Grak."
    $ Ellia.face = "sad"
    "Sabia whirled on Grak, and placed a hand on the handle of her weapon."
    $ Sabia.face = "angry1"
    s "What is this?"
    $ Sabia.face = "angry2"
    "Grak's grin spread across his face, wicked and cruel."
    $ GenericOrc2.face = "smile2"
    grak "Now you see what is proper purpose of females. To be orc slave."
    $ GenericOrc2.face = "smile1"
    grak "Crawl to fire and back, slave."
    $ Ellia.face = "sadopen"
    ellia "Yes, Master Grak... thank you Master Grak."
    $ Ellia.face = "sad"
    $ GenericOrc2.face = "normal"
    hide Ellia with dissolve
    "Slowly, the elf began to crawl as instructed. Long, languid movements that left her legs trailing behind and her ass jiggling."
    "The orc guards followed along with the elf, jeering and spitting on her. Reaching down and slapping her ass hard when she slowed to what they deemed an unacceptable pace."
    "Grak turned to Sabia, pleased with the elf's obedience."
    $ Sabia.face = "surprised1"
    $ GenericOrc2.face = "smile3"
    grak "Elves are stronger than humans. But even an elf is easy to break. Especially mage. Grak is thinking that you do not appreciate this."
    $ GenericOrc2.face = "normal"
    $ Sabia.face = "surprised2"
    s "Wait- that's a {i}mage{i}!?"
    $ GenericOrc2.face = "suspicious"
    s "How did-"
    $ Sabia.face = "surprised1"
    "Grak spat on the ground again in disgust."
    $ GenericOrc2.face = "angry"
    grak "Mage."
    grak "Pfaw!"
    grak "They are easy to break if you are knowing what to do, and can do it. But humans, elves. They are weak."
    $ Sabia.face = "sad2"
    grak "A few piercings with the right metal... and the will of a mage crumbles."
    $ GenericOrc2.face = "smile2"
    grak "Without their magic, they are nothing more than slaves to be trained. Ego and sense of self crushed under weight of knowing they cannot rely on magic."
    grak "Grak is thinking you should keep this in mind while you are here."
    $ GenericOrc2.face = "suspicious"
    $ Sabia.face = "closed2"
    s "(Do... does he think I'm a mage...? That might explain...)"
    s "..."
    $ Sabia.face = "normalopen"
    s "I... see..."
    s "But... I am not sure how this is what Tekrok wanted?"
    $ Sabia.face = "normal"
    $ GenericOrc2.face = "normal"
    show Ellia at center with dissolve
    "Grak clicked his tongue, and the elf turned about quickly, crawling back towards them."
    $ Ellia.face = "sadopen"
    ellia "Yes, Master Grak? How can this one serve?"
    $ Ellia.face = "sad"
    $ GenericOrc2.face = "suspicious"
    "Grak gripped the elf's chin hard, and angled her face up as he spat on her."
    $ Sabia.face = "irritated2"
    "She lapped it up as best she could with her tongue, cheeks stained with days-old cum and tears."
    $ Ellia.face = "sadopen"
    ellia "Thank you Master Grak."
    $ Ellia.face = "sad"
    $ GenericOrc2.face = "angry"
    grak "Breaking is quickest way to get correct information."
    $ Sabia.face = "irritated1"
    grak "Grak is thinking you should tell this would-be human slut what she wants to know, so that she can return to Tekrok quickly."
    $ GenericOrc2.face = "suspicious"
    $ Sabia.face = "sad1"
    $ Ellia.face = "sadopen"
    ellia "Master Grak, of course. Thank you Master Grak."
    $ Ellia.face = "sad"
    "The elf turned to Sabia as Grak walked around his slave."
    $ Sabia.face = "sad3"
    s "What can you tell me about what's happening in Whitecrest with the mages?"
    $ Sabia.face = "sad1"
    $ Ellia.face = "sadopen"
    ellia "I was in charge of-"
    $ Ellia.face = "surprised"
    $ GenericOrc2.face = "smile2"
    call shake ("h")
    ellia "Ahhn!"
    $ Ellia.face = "sad"
    $ Sabia.face = "irritated2"
    "Grak smirked, his hand pulling back from the elf's bare ass. Her whole body had shuddered under the slap, knees digging deeper into the ground."
    "Sabia bit her tongue for now, and waited for the elf to continue."
    $ Ellia.face = "sadopen"
    ellia "Thank... thank you Master Grak."
    $ GenericOrc2.face = "suspicious"
    $ Sabia.face = "normal"
    ellia "I was in charge of dealing with the less important stuff... running between Whitecrest and the bandits."
    $ Ellia.face = "sad"
    "Sabia raised an eye."
    $ Sabia.face = "normalopen"
    s "Bandits?"
    $ Sabia.face = "normal"
    $ Ellia.face = "sadopen"
    ellia "Yes. Archmage Lynn-"
    $ Ellia.face = "sad"
    $ Sabia.face = "irritated2"
    $ GenericOrc2.face = "smile2"
    grak "Bark like bitch."
    $ GenericOrc2.face = "suspicious"
    $ Ellia.face = "sadopen"
    ellia "Arf! Arf!"
    $ Ellia.face = "sad"
    $ Sabia.face = "angry1"
    s "Is that... really necessary? That seems overly cruel."
    $ Sabia.face = "irritated2"
    "Grak growled, reaching over and grabbing hold of the elf's hair with one hand. She stumbled, almost falling as he wrenched the elf closer to him."
    "His hand whistled through the air before landing on the elf's bared tits. The bright metal piercings glinted in the sun as her tits heaved from the impact."
    $ Sabia.face = "irritated1"
    "The elf whimpered, trying her best to stifle the sobs rumbling in her throat."
    $ GenericOrc2.face = "angry"
    grak "Elf is our slave. Property. Nothing but a bitch. Grak is making sure that you understand this."
    $ GenericOrc2.face = "suspicious"
    $ Sabia.face = "normalopen"
    s "It seems too much."
    $ Sabia.face = "irritated2"
    $ GenericOrc2.face = "angry"
    grak "Grak is thinking that you should not judge methods. Or you will end up next to Grak's slave."
    grak "It is easiest, fastest way to get all information."
    $ GenericOrc2.face = "suspicious"
    s "..."
    $ Sabia.face = "normalopen"
    s "Alright. Can I keep talking to her now?"
    $ Sabia.face = "normal"
    "Grak nodded. His other orcs smirked."
    "The elf looked away from Grak hesitantly, before beginning to speak again."
    $ Ellia.face = "sadopen"
    ellia "Archmage Lynn had me to deliver payments and orders to the bandits so that they would continue pressuring Whitecrest and nearby areas."
    $ Sabia.face = "irritated2"
    ellia "This was important... Archmage Lynn had great faith in... faith in me."
    $ Ellia.face = "sad"
    $ GenericOrc2.face = "angry"
    grak "Weak mage thinking another weak mage can do important task."
    $ GenericOrc2.face = "suspicious"
    "The elf nodded."
    $ Ellia.face = "sadopen"
    ellia "I know now I was wrong, Master Grak... thank you for teaching me."
    $ Ellia.face = "sad"
    $ Sabia.face = "normalopen"
    s "Why was Lynn dealing with bandits?"
    $ Sabia.face = "normal"
    $ Ellia.face = "sadopen"
    ellia "Archmage Lynn wanted pressure on Whitecrest."
    ellia "I was only the go-between... I served as the errand runner for Archmage Lynn in Whitecrest and her apprentice, Shalye that was working with the bandits."
    ellia "That was all I knew though... the missives were sealed by Archmage Lynn herself."
    ellia "I was also responsible for ensuring stones were delivered safely to the palace from Lundar."
    $ Ellia.face = "sad"
    $ Sabia.face = "closed2"
    s "(...it seems Lynn has been busy.)"
    $ Sabia.face = "normal"
    $ GenericOrc2.face = "angry"
    grak "Grak would have liked to break this Lynn. But it is difficult, Grak is thinking, when they hide in their cities and do not come out."
    grak "That is why this elf whore is now our slave. She was often out of the city on her tasks."
    $ GenericOrc2.face = "suspicious"
    $ Sabia.face = "normalopen"
    s "So... Archmage Lynn has been funding all the bandit camps, to put pressure on Whitecrest?"
    $ Sabia.face = "normal"
    "The elf nodded."
    $ Sabia.face = "normalopen"
    s "But why was she providing stones to Whitecrest at the same time?"
    $ Sabia.face = "irritated2"
    $ Ellia.face = "sadopen"
    ellia "Archmage Lynn is... very busy, with many different schemes."
    $ Ellia.face = "sad"
    $ Sabia.face = "closed2"
    s "(Don't I know it?)"
    $ Sabia.face = "normal"
    $ Ellia.face = "sadopen"
    ellia "She was very close with Andian's wife, as well..."
    ellia "But I do now know much more, sorry Master Grak..."
    $ Ellia.face = "sad"
    $ Sabia.face = "irritated2"
    $ GenericOrc2.face = "smile2"
    grak "Good bitch. Back to your tent. Grak is thinking maybe you will get dinner tonight."
    $ Sabia.face = "normal"
    $ GenericOrc2.face = "suspicious"
    $ Ellia.face = "happy"
    "The elf's eyes lit up a little bit."
    ellia "Yes, Master Grak! Thank you!"
    $ Sabia.face = "sad1"
    "She wrapped her arms around Grak's leg, hugging tight."
    $ GenericOrc2.face = "angry"
    $ Ellia.face = "sad"
    grak "Get off! You reek of Grak's seed! Filth."
    $ Ellia.face = "sadopen"
    ellia "S-sorry Master Grak..."
    $ Ellia.face = "sad"
    grak "Hmph."
    $ GenericOrc2.face = "suspicious"
    hide Ellia with moveoutright
    "Sabia watched as the elf slowly started to crawl back to her tent, nipple piercings dangling and dancing underneath her heavy tits."
    "She looked back to Grak to make sure she was still allowed to keep moving."
    $ Sabia.face = "irritated2"
    $ GenericOrc2.face = "angry"
    grak "There. Information."
    grak "Archmage Lynn is funding bandits. Providing weak, human mage stones to Whitecrest."
    grak "Hmph. Probably being a slut with Andian's wife, Grak is thinking, trying to sleep her way to what she wants."
    $ GenericOrc2.face = "smile2"
    $ Sabia.face = "irritated1"
    grak "You see how easy it is to break a mage into nothing?"
    grak "Grak is thinking you had best remember this."
    $ GenericOrc2.face = "suspicious"
    $ Sabia.face = "angry1"
    s "I'm not a mage, if that's what you're implying."
    $ Sabia.face = "irritated2"
    "Grak chewed his lip, looking at her thoughtfully."
    "Instinctively, his hand moved to his left hip, fingers reaching for the small shining canister before he grunted and pulled away."
    $ GenericOrc2.face = "angry"
    grak "Grak is thinking perhaps. Now you will be coming away. Grak is thinking that you have no more need to talk to this elf, unless you wish to take her place."
    $ Sabia.face = "irritated1"
    $ GenericOrc2.face = "smile2"
    grak "It will not take long before you call orcs Master."
    $ GenericOrc2.face = "suspicious"
    "Grak turned to walk away from the tent, back towards the middle of the camp."
    menu:
        "Go talk to the elf.":
            $ v10tekrok_camp_trust -= 3
            $ Sabia.face = "normalopen"
            $ GenericOrc2.face = "suspicious"
            s "I think I would like to talk to the mage again-"
            $ Sabia.face = "irritated2"
            "Grak grunted, turning back around."
            $ GenericOrc2.face = "angry"
            grak "Slave."
            grak "Not mage. She is nothing but orc slave now. Weak, pathetic set of holes."
            grak "But no. Grak is thinking you will not do so. Grak has said what you will do."
            $ GenericOrc2.face = "suspicious"
            $ Sabia.face = "normalopen"
            s "But-"
            $ Sabia.face = "normal"
            $ GenericOrc2.face = "smile2"
            grak "It would be nice to have a human slave to go with our elf. You would make a nice pair."
            grak "Grak is thinking he will assume you wish this if you trying to disobey."
            $ GenericOrc2.face = "suspicious"
            s "..."
            $ Sabia.face = "normalopen"
            s "I guess I'll go back to the middle of the camp with you for now, then."
        "Leave her for now.":
            $ Sabia.face = "normalopen"
            s "...alright."
            s "I would like to ask more questions later, though."
            $ Sabia.face = "normal"
            grak "Hmph."
            $ GenericOrc2.face = "angry"
            grak "Grak has made sure that you have all information needed to report to Tekrok."
            $ GenericOrc2.face = "suspicious"
            "Sabia frowned. It seemed counter productive to argue with Grak right now. Maybe she could talk to the elf later tonight before heading back to Grok og Dar."
    $ Sabia.face = "closed2"
    s "(Maybe if they're more... relaxed, I might be able to sneak in without them paying much attention and I can ask some more specific questions about what Lynn might be up to.)"
    jump ef3_graks_camp


label ef3_graks_camp_drinking:
    $ Sabia.face = "sad3"
    s "You know, I was wondering. Surely big, strong orcs like you can't get drunk off such little alcohol?"
    "She asked it, putting a naive frown on her face as she asked the question, handing over the bottles."
    $ Sabia.face = "sad1"
    "The orcs seemed pleased at Sabia's deference to their strength, nodding and mumbling to each other as Grak grinned."
    $ GenericOrc2.face = "smile1"
    grak "It is good you understand orcs are strong, but Grak is thinking you do not understand that orcs make equally strong drink."
    grak "These bottles will make many mugs of drink for us tonight and tomorrow."
    $ GenericOrc2.face = "normal"
    $ Sabia.face = "normalopen"
    s "Mind if I stick around and have a little bit?"
    $ Sabia.face = "irritated2"
    $ GenericOrc2.face = "smile3"
    grak "Grak is wondering if you can handle this drink. Humans are weak."
    $ GenericOrc2.face = "normal"
    $ Sabia.face = "normal"
    menu:
        "I want to see how strong and tough orcs really are!":
            $ v10tekrok_camp_trust += 1
            $ Sabia.face = "happy3"
            s "I just wanna see how strong and tough all you big orcs are! It's not something I am used to in human cities, you know."
            $ Sabia.face = "normal"
            "Sabia almost winced at the words."
            $ GenericOrc2.face = "smile3"
            "Grak's pursed lips broke into a smile and threw his head back, laughing."
            $ Sabia.face = "question1"
            grak "Hah! It is good, Grak is thinking, when a human wants to see an orc's strength."
        "I could probably drink you under the table.":
            $ v10tekrok_camp_trust -= 2
            $ GenericOrc2.face = "suspicious"
            "Grak growled his annoyance."
            $ Sabia.face = "irritated2"
            $ GenericOrc2.face = "angry"
            grak "Not just weak. But arrogant too."
            grak "Grak is thinking you can stay, and see how much you can handle."
    $ GenericOrc2.face = "normal"
    $ Sabia.face = "normal"
    "Grak ushered over the rest of the orcs."
    "Though they seemed eager to drink and already had mugs mostly filled with water, Sabia still felt the tension and unease present in the camp."
    "They were still on edge and unsure about her."
    $ Sabia.face = "irritated2"
    "One of the orcs handed Sabia a mug, and she grabbed hold of it."
    $ GenericOrc1.face = "suspicious"
    orc "..."
    "For a moment the orc did not let go, but finally relinquished his grip with a sharp wrench of his hand that made some of the water splash over."
    $ Sabia.face = "irritated1"
    $ GenericOrc1.face = "angry"
    orc "Dumb slut."
    menu:
        "Oh no! You got me wet!":
            $ v10tekrok_camp_trust += 1
            $ Sabia.face = "happy2"
            s "Oh no... it looks like you got me a little bit wet there, haha!"
            $ Sabia.face = "question1"
            "Sabia fluttered her eyelashes as best as she could. She wasn't sure it was all that convincing, but the orcs next to her seemed to buy it."
            $ GenericOrc1.face = "smile3"
            "They grinned, laughing and nodding almost with acceptance."
            $ Sabia.face = "annoyed2"
            orc "Probably not hard to do when you are in between so many orcs."
            $ GenericOrc1.face = "normal"
            $ Sabia.face = "happy2"
            s "Oh no, it happens a lot, actually... !"
            $ Sabia.face = "closed2"
            "Sabia grimaced inwardly at her words, but the orcs seemed to buy it still."
        "Say nothing.":
            $ Sabia.face = "irritated1"
            "Sabia glowered at him."
            "She didn't say anything as he grunted, wrinkling his nose as he walked off."
    $ Sabia.face = "normal"
    "The drinking continued a bit longer and the fire grew larger as they threw more fuel on."
    "Much slower than Sabia imagined, the two small bottles of alcohol dwindled."
    "Only a few drops went in with every mug they downed. But they were noticeably getting drunker and drunker."
    "Every now and then, one of the orcs would get up and take some over to the guards watching the elf."
    $ Sabia.face = "irritated2"
    $ GenericOrc2.face = "angry"
    grak "Slut!"
    "Grak growled out the word in a long slur, beckoning Sabia over with a finger."
    $ Sabia.face = "irritated1"
    $ GenericOrc2.face = "suspicious"
    grak "Come here, whore!"
    "Sabia grit her teeth and walked over to Grak, doing her best to ignore the orcs speaking as she walked past."
    $ Sabia.face = "annoyed2"
    orc1 "She would be better than elf whore. Elf break too easy. Me think that this human would last... at least a day longer."
    orc2 "Maybe. Probably loose though, probably already orc whore from Grok og Dar."
    $ Sabia.face = "irritated1"
    orc1 "Probably true. Human slut wouldn't be able to stop herself."
    $ GenericOrc2.face = "normal"
    "Grak grunted, pushing a bottle toward Sabia as she came closer to him."
    $ GenericOrc2.face = "normalopen"
    grak "Take this to guards."
    $ GenericOrc2.face = "normal"
    $ Sabia.face = "normalopen"
    s "Alright..."
    $ Sabia.face = "irritated2"
    $ GenericOrc2.face = "smile3"
    grak "Already so obedient. Grak is thinking maybe you will not want to leave!"
    grak "That is okay. Grak will make spot for you in his tent. You will be very happy, Grak is thinking."
    menu:
        "No.":
            $ v10tekrok_camp_trust -= 1
            $ Sabia.face = "annoyed1"
            $ GenericOrc2.face = "suspicious"
            s "I don't think so."
            $ Sabia.face = "normalopen"
            s "I have Tekrok's tasks to do."
            $ Sabia.face = "normal"
            "It seemed though, that Grak had misunderstood what Sabia had meant."
            $ GenericOrc2.face = "angry"
            $ Sabia.face = "irritated2"
            grak "Hmph. Tekrok is a strong orc. But Grak is better at fucking. Keep that in mind."
            $ GenericOrc2.face = "suspicious"
            menu:
                "I will! (sincere)" if tekrokraidsexdone == True:
                    $ v10tekrok_camp_trust += 3
                    $ sub += 2
                    $ Sabia.face = "happy2"
                    $ GenericOrc2.face = "normal"
                    s "Really? Tekrok is pretty good at fucking me."
                    s "I've gotten to fuck him a few times, and I doubt any of the other orcs in Grok og Dar can match him... and I'm not so sure you could either!"
                    $ Sabia.face = "normal"
                    $ GenericOrc2.face = "normalopen"
                    grak "Hmph. A challenge."
                    $ GenericOrc2.face = "normal"
                    $ Sabia.face = "happy3"
                    s "His cock is massive... and he knows exactly what to do to make my knees weak."
                    $ Sabia.face = "question1"
                    "Sabia glanced over Grak."
                    $ Sabia.face = "happy2"
                    s "I'm not sure you've got it in you."
                    $ Sabia.face = "normal"
                    $ GenericOrc2.face = "smile2"
                    grak "Hah! Whether you like Grak or Tekrok more, Grak is thinking you are happy just to serve orc cock."
                    grak "This is good. Perhaps if you are lucky you will join the elf slave when Tekrok has no more use for you."
                    grak "Now go and deliver!"
                    $ GenericOrc2.face = "normal"
                "I will! (play along)":
                    $ v10tekrok_camp_trust += 1
                    $ Sabia.face = "happy3"
                    $ GenericOrc2.face = "normal"
                    s "Okay! I will definitely keep that in mind, Grak."
                    s "Orcs are just like, uhm..."
                    $ Sabia.face = "closed2"
                    s "(...)"
                    $ Sabia.face = "annoyed1"
                    $ GenericOrc2.face = "smile3"
                    s "Like, way better than humans at fucking!"
                    $ Sabia.face = "irritated1"
                    "Grak nodded his agreement with a wide smirk, too drunk too notice Sabia's expression."
                    $ GenericOrc2.face = "smile1"
                    grak "Yes! It is good when human sluts know their place, and understand orcs are better!"
                    grak "Go and deliver, now."
                    $ GenericOrc2.face = "normal"
                "I don't fuck Tekrok.":
                    $ v10tekrok_camp_trust -= 1
                    $ Sabia.face = "annoyed1"
                    $ GenericOrc2.face = "suspicious"
                    s "I don't fuck Tekrok at all."
                    $ Sabia.face = "annoyed2"
                    $ GenericOrc2.face = "smile2"
                    grak "Good. Then Grak's cock will be first to stretch your worthless human holes."
                    grak "It is good, Grak is thinking, to be given the chance to have value."
                    $ GenericOrc2.face = "normal"
                    $ Sabia.face = "irritated1"
                    "He nodded softly to himself, agreeing with his own words."
                    "Sabia's face darkened as she walked off, ignoring Grak."
                "...":
                    $ Sabia.face = "normal"
                    "Sabia didn't say anything, doing her best to avoid scowling as she walked off with bottle in hand."
        "Play along.":
            $ v10tekrok_camp_trust += 1
            "Sabia did her best attempt at a giggle."
            $ Sabia.face = "closed2"
            "She almost cringed at how fake it sounded, but Grak smile, seeming pleased with her."
            $ Sabia.face = "normal"
            "He slapped her ass hard as she turned around as if to send her off to the task he had set."
    hide Sabia with moveoutleft
    scene bg countryside with dissolve
    $ Sabia.face = "normal"
    $ GenericOrc1.extras = ["Loincloth", "Helmet", "Beard1"]
    $ GenericOrc2.extras = ["Loincloth", "Hair", "Necklace"]
    show GenericOrc1 at right
    show GenericOrc2 at center
    with dissolve
    pause (0.1)
    show Sabia at left with moveinleft
    guard1 "Good, more drink!"
    $ GenericOrc2.face = "angry"
    guard2 "No, no! Dumb human cunt."
    guard2 "Not like that. On knees. Crawl. Like proper servant."
    $ GenericOrc2.face = "suspicious"
    guard1 "What? Me just want drink! Grak said not to leave tent, and me want drink now, not after dumb human bitch crawls over."
    menu:
        "Crawl over." if sub>dom:
            $ v10tekrok_camp_trust += 2
            $ sub += 3
            $ Sabia.face = "closed2"
            s "Ugh..."
            s "(It will be easier to get them drunk and relaxed if I do it... I suppose. And given that they {i}are{/i} the guards..."
            $ Sabia.face = "irritated2"
            "Sabia sighed as she sunk down onto the soft grass."
            "The orcs roared their approval, slapping each other on the back as Sabia slowly slinked forward."
            "She kept her legs against one another time, making sure each leg moved as far forward as it could before the next moved."
            $ Sabia.face = "irritated1"
            "The effect made her ass rise and fall seductively, jiggling enough for it to be noticeable."
            "Sabia held the bottle of alcohol in her hand."
            $ Sabia.face = "annoyed2"
            $ GenericOrc1.face = "smile1"
            guard1 "Heh, me wrong. That was good."
            $ GenericOrc1.face = "normal"
            $ GenericOrc2.face = "smile3"
            guard2 "Told you."
            $ Sabia.face = "irritated2"
            "The orcs looked down at Sabia, laughing."
            $ GenericOrc1.face = "smile2"
            guard1 "Humans are pathetic. Nothing but would-be cum-guzzling whores."
            $ GenericOrc2.face = "smile2"
            guard2 "Isn't that right, slut?"
            $ Sabia.face = "irritated1"
            "The orc crouched down, cupping Sabia's chin in his grip and spat on her with mixed parts disgust and lust."
            menu:
                "Thank you!":
                    $ v10tekrok_camp_trust += 2
                    "Sabia grit her teeth. She was sure they would chip as the words barely escaped her lips."
                    $ Sabia.face = "happy2"
                    $ GenericOrc1.face = "smile3"
                    $ GenericOrc2.face = "smile3"
                    s "Thank. You."
                    $ Sabia.face = "angry2"
                    "She was practically seething, her anger almost rising off her in waves of heat."
                    "Thankfully, the orcs were too drunk on their booze or their perceived superiority to notice."
                    "They laughed again, and let Sabia leave."
                    $ Sabia.face = "normal"
                "Fuck you.":
                    $ v10tekrok_camp_trust -= 3
                    $ Sabia.face = "angry2"
                    "Sabia grunted in anger, rising to her feet and slapping the orc across the face. Hard."
                    "A few birds nestled in the trees squawked awake as the sound echoed through the forest."
                    $ GenericOrc2.face = "angry"
                    guard2 "Huh. Dumb slut tried to slap me."
                    $ Sabia.face = "angry1"
                    s "I {i}did{/i} slap you."
                    $ Sabia.face = "angry2"
                    $ GenericOrc1.face = "smile3"
                    guard1 "You sure? Don't think he felt it."
                    $ GenericOrc1.face = "normal"
                    $ GenericOrc2.face = "smile3"
                    guard2 "Human sluts aren't strong enough to hurt orcs. Dumb whore."
                    $ GenericOrc2.face = "angry"
                    guard2 "Go back to Grak before we set you next to elf slave."
                    $ GenericOrc2.face = "suspicious"
                    $ Sabia.face = "angry1"
                    s "Gladly."
                    $ Sabia.face = "angry2"
                    "Sabia left back to the main part of the camp, pleased to leave the guards."
        "Walk over.":
            $ v10tekrok_camp_trust -= 1
            $ Sabia.face = "annoyed2"
            "There was no way Sabia was going to crawl over to them. Even if they had asked nicely."
            $ GenericOrc1.face = "sad1"
            $ GenericOrc2.face = "sad1"
            "Instead, she stomped over."
            $ Sabia.face = "annoyed1"
            s "Here's your drink."
            $ Sabia.face = "annoyed2"
            "She shoved the bottle into their hands, and though the second guard was annoyed with her, it seemed they quickly forgot as they started to pour the last few drops into the mugs."
            "Sabia doubted the ability of drunk guards, but she wasn't going to argue against it when she needed them all drunk."
            $ Sabia.face = "closed2"
            s "(...guess I'm just lucky they've been dry for so long.)"
            "She left the two guards there as they were already quaffing down the drink, some of it dribbling down their cheeks as it overflowed."
    scene bg countryside with dissolve
    $ Sabia.face = "normal"
    $ GenericOrc2.face = "normal"
    $ GenericOrc2.extras = ["Loincloth", "Shoulder", "Strap", "Necklace", "Beard2"]
    show GenericOrc2 at right with dissolve
    show Sabia at left with moveinleft
    "The drinking continued and slowly the second bottle dwindled to nothing as well."
    if v10tekrok_camp_trust >= 2:
        "The two guards eventually left their posts. Sabia was sure Grak would be furious but it seemed that whether because of all the drink or that they simply decided Sabia was not too dangerous, their wariness had waned."
    else:
        "Eventually, the guards left their posts. Grak seemed mildly annoyed, but was too intoxicated to make a big deal of it. That's what Sabia thought at any rate."
        "She felt that the orcs had relaxed a little bit, but was not entirely sure if any wariness regarding her still remained."
    "At any rate, she still wanted to talk to the elf."
    "She asked Grak if she might be allowed to go speak to the elf for some personal questions, and Grak nodded his agreement."
    $ Sabia.face = "happy2"
    $ GenericOrc2.face = "normalopen"
    grak "Grak is... Grak is thinking this is fine."
    $ Sabia.face = "irritated1"
    $ GenericOrc2.face = "smile3"
    grak "Grak is thinking you just want to see how fun it is to be slave for proper, strong orcs! You may go ask how much elf slave enjoys being cum-dumpster."
    $ GenericOrc2.face = "normal"
    "He nodded to himself, pleased."
    scene bg countryside
    show Ellia at right
    with dissolve
    pause (1)
    $ Sabia.face = "normal"
    show Sabia at left with moveinleft
    $ Ellia.face = "sad"
    "The elf whimpered as Sabia entered the tent, pulling herself up off the floor into a small pile of messy, cum-stained flesh and hair."
    $ Sabia.face = "happy2"
    s "It's okay, no orcs with me."
    $ Sabia.face = "normal"
    "She glanced about fearfully, wondering if Sabia were telling the truth or not."
    $ Sabia.face = "sad2"
    $ Ellia.face = "sadopen"
    ellia "Th-they're not... not with you?"
    $ Ellia.face = "sad"
    $ Sabia.face = "sad1"
    "Sabia shook her head."
    "The elf's lips trembled and a few tears started to run down her cheeks."
    $ Sabia.face = "sad2"
    $ Ellia.face = "sadopen"
    ellia "Please! Please, please, please you have to help me get out!"
    $ Ellia.face = "sad"
    $ Sabia.face = "sad3"
    s "I don't think I can do that. I wanted to ask some more questions about-"
    $ Sabia.face = "sad2"
    $ Ellia.face = "sadopen"
    ellia "PLEASE!"
    $ Ellia.face = "sad"
    "The elf was frantic, wriggling over to Sabia's feet."
    $ Ellia.face = "sadopen"
    ellia "I c-can't... I can't do it. Anymore. It's... I can't, please."
    $ Sabia.face = "sad1"
    ellia "Please, you have to help me. I'll do anything!"
    ellia "Anything you want!"
    ellia "Just... help me get out. I've been here... for months and months or years... I can't remember, I can't tell!"
    ellia "All day... every day... they treat me like their slave. They use me. Abuse me. Make me do things..."
    $ Ellia.face = "sad"
    $ Sabia.face = "closed2"
    s "..."
    menu ef3_graks_camp_ellia_menu:
        "Don't make me get Grak in here." if v10tekrok_ellia_grak == False:
            $ v10tekrok_ellia_grak = True
            $ A_ellia -= 5
            $ Sabia.face = "normalopen"
            s "If you don't tell me what I want to know, I'll have to get Grak in here and say you've been misbehaving."
            $ Sabia.face = "normal"
            $ Ellia.face = "sadopen"
            ellia "...please. No..."
            $ Ellia.face = "sad"
            "The elf's voice was full of resigned despair. Her pleas short of hope."
            $ Sabia.face = "irritated2"
            $ Ellia.face = "sadopen"
            ellia "I have nothing more to tell... Archmage Lynn did not trust me with anything more."
            $ Ellia.face = "sad"
            $ Sabia.face = "closed2"
            s "(...I don't think she is lying. There would be little reason to lie. And if she is managing to lie still, then I have no chance of breaking the last pieces from her in a short time to learn anything new.)"
            jump ef3_graks_camp_ellia_menu
        "I can't free you. Sorry.":
            jump ef3_graks_camp_post_drinking
        "How would I be able to?":
            $ Sabia.face = "normalopen"
            s "Even if I wanted to help you... how would I go about helping you escape? In the middle of an orc camp full of orcs that have broken you?"
            $ Sabia.face = "normal"
            "The elf's mouth half-opened, as if she had expected Sabia to say no."
            "Presented with the faintest sliver of hope, she almost couldn't speak."
            $ Sabia.face = "sad2"
            $ Ellia.face = "happy"
            ellia "I- uh, well! If you loosen my bonds... and remove these piercings. And the orcs stay drunk..."
            ellia "I might be able to gather enough magic to be able to escape by myself... if you tried to help me out they would see and hear."
            $ Ellia.face = "sadopen"
            ellia "This is the only way... will you... will you help me?"
            $ Sabia.face = "sad1"
            ellia "Please?"
            $ Ellia.face = "sad"
            menu:
                "Yes.":
                    jump ef3_graks_camp_free_ellia
                "I need more information.":
                    $ Sabia.face = "normalopen"
                    s "Sorry. I need more information first."
                    $ Sabia.face = "normal"
                    "The elf's throat constricted as she cried, hope dwindling away quickly."
                    $ Ellia.face = "sadopen"
                    ellia "I don't... I have no more information... nothing more to tell."
                    $ Sabia.face = "sad1"
                    ellia "Archmage Lynn did not trust me with anything more..."
                    ellia "The orcs... they... no, I mean Master Grak! Please... don't tell him I said orcs."
                    ellia "Master Grak."
                    $ Ellia.face = "sad"
                    s "(...I don't think she is lying. There would be little reason to lie. And if she is managing to lie still, then I have no chance of breaking the last pieces from her in a short time.)"
                    $ Sabia.face = "normal"
                    $ Ellia.face = "sadopen"
                    ellia "...please... will you help me?"
                    $ Ellia.face = "sad"
                    menu:
                        "Yes.":
                            jump ef3_graks_camp_free_ellia
                        "I can't free you. Sorry.":
                            jump ef3_graks_camp_post_drinking
                "I can't free you. Sorry.":
                    jump ef3_graks_camp_post_drinking


label ef3_graks_camp_post_drinking:
    $ v10tekrok_camp_left = True
    if v10tekrok_ellia_freed == False:
        $ slavery += 2
        $ A_ellia -= 2
        $ Sabia.face = "sad3"
        s "I'm sorry. Freeing you isn't an option for me. I can't help you."
        $ Sabia.face = "sad1"
        ellia "..."
        $ Ellia.face = "sadopen"
        ellia "Master Grak would do no less to you if you tried and were caught..."
        $ Sabia.face = "sad2"
        ellia "I understand."
        $ Ellia.face = "sad"
        "The elf's voice was full of resigned despair. Dead, flat. She had not hoped, and had not been disappointed by Sabia's answer."
        "Sabia knew that whether the elf knew more or not, she had been broken enough that she would not be able to get any more information from her."
        $ Sabia.face = "sad1"
        "The elf's lip trembled and a wave of despair and hopelessness washed over her as Sabia left the tent."
        scene bg black with dissolve
        pause (1)
        scene bg countryside
        $ Sabia.face = "normal"
        show Sabia at left with dissolve
        "Sabia woke the next morning to the sound of hungover orcs. The orcs were groaning, holding their heads."
        "It seemed the drink Tekrok had provided had truly been potent."
        "A few of them dragged themselves to their feet before walking back towards the tent where the chained and bound elf had been."
        "Sabia made her way over to speak to Grak before leaving, but it was clear from his pained groan that he was in no mood to speak."
        "She shrugged, and left the orcs to their business. She had done what she needed to do."
        jump eastern_frontier_map
    else:
        scene bg black with dissolve
        pause (1)
        scene bg countryside
        $ Sabia.face = "normal"
        show Sabia at left with dissolve
        "Sabia woke the next morning with a little bit of trepidation. The orcs were groaning, holding their heads."
        "It seemed the drink Tekrok had provided had truly been potent."
        "A few of them dragged themselves to their feet before walking back towards the tent where the chained and bound elf had been."
        "It was not more than a few moments before the guards rushed back. They hurried over to Grak and leaned their heads forward, muttering."
        "Sabia felt a short surge of concern as Grak glanced over toward her, his eyes glowering and dark."
        "He looked back at the guards and they continued talking for a few minutes before the guards left."
        $ GenericOrc2.face = "suspicious"
        "Grak made his way over to Sabia."
        $ Sabia.face = "normalopen"
        s "Is... something wrong?"
        $ Sabia.face = "normal"
        $ GenericOrc2.face = "angry"
        grak "Yes."
        $ GenericOrc2.face = "suspicious"
        s "..."
        "Grak sighed, but it was clear there was anger simmering underneath."
        $ Sabia.face = "sad2"
        $ GenericOrc2.face = "angry"
        grak "Elf slave escaped."
        grak "...Grak is thinking it may have been Grak's fault."
        grak "He remembers playing with the slave's breasts too much... Grak must have knocked the piercings loose."
        $ GenericOrc2.face = "suspicious"
        $ Sabia.face = "sad3"
        s "Would that be enough to let her escape?"
        $ Sabia.face = "sad1"
        $ GenericOrc2.face = "angry"
        grak "Obviously."
        $ GenericOrc2.face = "suspicious"
        "Grak grated his teeth as he answered Sabia."
        $ GenericOrc2.face = "angry"
        grak "You will need to tell Tekrok about this."
        $ GenericOrc2.face = "suspicious"
        $ Sabia.face = "sad3"
        s "I uh... don't think Tekrok will be pleased."
        $ Sabia.face = "sad1"
        "Grak grunted, nodding."
        $ GenericOrc2.face = "angry"
        grak "Grak is thinking you should tell Tekrok that Grak and others will do best to recapture her before she can rejoin the Archmage whore, or report to the bandit's mage."
        $ GenericOrc2.face = "suspicious"
        $ Sabia.face = "normal"
        "Sabia nodded, still unsure if Grak believed it had been his fault."
        "But she was not waiting around to find out. At least now, it seemed Grak had bought whatever magic Ellia had managed to muster."
        "Grak and the orcs let Sabia leave without an issue, and she started to head back to Grok og Dar."
        $ Sabia.face = "closed2"
        "She would have to tell Tekrok about Ellia escaping..."
        jump eastern_frontier_map


label ef3_graks_camp_free_ellia:
    if v10tekrok_camp_trust >= 2:
        $ v10tekrok_ellia_freed = True
        $ freedom += 2
        $ A_ellia += 10
        "Sabia nodded."
        $ Sabia.face = "normalopen"
        s "I will do that. I hope you can make it out."
        $ Sabia.face = "normal"
        "She bent to loosen the bonds, but paused for a moment."
        $ Ellia.face = "sadopen"
        ellia "W-what are... please!"
        $ Ellia.face = "sad"
        $ Sabia.face = "normalopen"
        s "Shh... I will just check to make sure the orcs are not paying attention."
        $ Sabia.face = "normal"
        "Sabia moved over to the tent's entrance and peered through the opening. The guards had joined the rest of the orcs in the middle of the camp, and were all extremely intoxicated or passed out by now."
        "She nodded to herself and walked back to the elf."
        $ Ellia.face = "sadopen"
        $ ellia = Character("{image=system/ellia.png}", who_ypos=-68, what_ypos=-70)
        ellia "My name's Ellia..."
        $ Ellia.face = "sad"
        $ Sabia.face = "irritated2"
        "Sabia did not reciprocate. She bent and loosened the bonds, before unclasping the small piercings that dangled from Ellia's breasts."
        "Ellia sighed in relief."
        $ Ellia.face = "happy"
        ellia "Thank you! Even... even this... with those gone. It feels like a great pressue has been been relieved... I can only hope that Master-"
        $ Ellia.face = "sad"
        $ Sabia.face = "normal"
        "Her eyes narrowed."
        $ Ellia.face = "sadopen"
        ellia "That I can flee from these vile orcs, and make sure they regret this."
        $ Sabia.face = "normalopen"
        $ Ellia.face = "sad"
        s "I hope so as well. And I hope that the orcs will not suspect me."
        $ Sabia.face = "normal"
        $ Ellia.face = "sadopen"
        ellia "I will... do what I can to make sure they do not."
        $ Ellia.face = "happy"
        ellia "With them drunk, intoxicated... if I wait a bit longer I might be able to spare some magic to help them remember things..."
        "Sabia nodded."
        $ Sabia.face = "normalopen"
        $ Ellia.face = "sad"
        s "I appreciate that. I hope you succeed."
        $ Sabia.face = "normal"
        "Ellia still looked as if she only half believed that the metal sapping her magic was gone, that her bonds had been loosened. That she might truly be able to escape."
        "Sabia left the elf in the tent to recuperate her strength. She hoped that Ellia would be able to escape by morning."
        jump ef3_graks_camp_post_drinking
    else:
        "Sabia nodded."
        $ Sabia.face = "normalopen"
        s "I will do that. I hope you can make it out."
        $ Sabia.face = "normal"
        "She bent to loosen the bonds, but paused for a moment."
        $ Ellia.face = "sadopen"
        ellia "W-what are... please!"
        $ Ellia.face = "sad"
        $ Sabia.face = "normalopen"
        s "Shh... I will just check to make sure the orcs are not paying attention."
        $ Sabia.face = "surprised3"
        $ Ellia.face = "surprised"
        "Sabia moved over to the tent's entrance and peered through the opening. She jumped in shock as an orc rounded around to face her. Drunk, but clearly enraged."
        $ GenericOrc1.extras = ["Loincloth", "Beard1", "Piercing"]
        $ GenericOrc1.face = "angry"
        guard1 "You think orcs dumb?!"
        $ GenericOrc1.face = "suspicious"
        $ Sabia.face = "surprised1"
        $ GenericOrc2.face = "angry"
        guard2 "Orcs are paying attention, slut!"
        guard2 "Now you see how weak humans are!"
        "The orc roared out a warning as the last breaths escaped, and the camp turned into disarray. Even drunk, they were already on Sabia before she was able to escape."
        jump ef3_graks_camp_badend


label ef3_graks_camp_badend:
    scene bg black with dissolve
    if v10tekrok_grak_information == True:
        "Though Sabia did not use magic like Ellia, Grak and the other orcs made sure that she felt as weak and helpless as her Elven companion did."
    else:
        "Sabia found herself waking up sometime later, bound and restricted. Unable to move."
    call v10camp_badend
    show gameover with dissolve
    pause 3
    $ renpy.full_restart()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
