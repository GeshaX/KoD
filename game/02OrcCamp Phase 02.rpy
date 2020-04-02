






screen lowerorccampscreen2:
    $ renpy.block_rollback()
    default mouse_clicked = False
    add "imagebuttons/orccamp1bg.png" xalign 0.0 yalign 0.0
    imagebutton auto "imagebuttons/sabiatent_%s.png" action [Hide("lowerorccampscreen2"), Jump("sabiahq2")] xpos 433 ypos 112 focus_mask True
    imagebutton auto "imagebuttons/centralcamp_%s.png" action [Hide("lowerorccampscreen2"), Jump("centralcamp2")] xpos 166 ypos 132 focus_mask True
    imagebutton auto "imagebuttons/silvertusk_%s.png" action [Hide("lowerorccampscreen2"), Jump("silvertusk2")] xpos 647 ypos 72 focus_mask True
    imagebutton auto "imagebuttons/traininggrounds_%s.png" action [Hide("lowerorccampscreen2"), Jump("traininggrounds2")] xpos 614 ypos 400 focus_mask True
    imagebutton auto "imagebuttons/kennels_%s.png" action [Hide("lowerorccampscreen2"), Jump("hellhoundkennels2")] xpos 0 ypos 100 focus_mask True
    imagebutton auto "imagebuttons/relieftents_%s.png" action [Hide("lowerorccampscreen2"), Jump("relieftents2")] xpos 0 ypos 512 focus_mask True
    imagebutton auto "imagebuttons/orcoutskirts_%s.png" action [Hide("lowerorccampscreen2"), Jump("eastern_frontier_map")] xpos 142 ypos 0 focus_mask True
    fixed at KeymapTransform([('mousedown_1', SetScreenVariable('mouse_clicked', True)), ('mouseup_1', SetScreenVariable('mouse_clicked', False))]):
        imagebutton idle "imagebuttons/upper_idle.png" hover ("imagebuttons/upper_clicked.png" if mouse_clicked else "imagebuttons/upper_hover.png") xpos 965 ypos 0 focus_mask True action [Hide("lowerorccampscreen2"), Jump("upperorccamp")]
    use infohud("center")


screen upperorccampscreen2:
    $ renpy.block_rollback()
    default mouse_clicked = False
    add "imagebuttons/orccamp2bg.png" xalign 0.0 yalign 0.0
    imagebutton auto "imagebuttons/mainhall_%s.png" action [Hide("upperorccampscreen2"), Jump("mainhall2")] xpos 0 ypos 0 focus_mask True
    imagebutton auto "imagebuttons/tekrok_%s.png" action [Hide("upperorccampscreen2"), Jump("tekroktent2")] xpos 597 ypos 333 focus_mask True
    imagebutton auto "imagebuttons/rokgrid_%s.png" action [Hide("upperorccampscreen2"), Jump("rokgridtent2")] xpos 0 ypos 456 focus_mask True
    imagebutton auto "imagebuttons/dajrab_%s.png" action [Hide("upperorccampscreen2"), Jump("dajrabtent2")] xpos 962 ypos 255 focus_mask True
    imagebutton auto "imagebuttons/tradinglodge_%s.png" action [Hide("upperorccampscreen2"), Jump("tradinglodge2")] xpos 223 ypos 370 focus_mask True
    imagebutton auto "imagebuttons/orctents_%s.png" action [Hide("upperorccampscreen2"), Jump("orctents2")] xpos 593 ypos 648 focus_mask True
    fixed at KeymapTransform([('mousedown_1', SetScreenVariable('mouse_clicked', True)), ('mouseup_1', SetScreenVariable('mouse_clicked', False))]):
        imagebutton idle "imagebuttons/lower_idle.png" hover ("imagebuttons/lower_clicked.png" if mouse_clicked else "imagebuttons/lower_hover.png") xpos 0 ypos 0 focus_mask True action [Hide("upperorccampscreen2"), Jump("lowerorccamp")]
    use infohud("center")






label sabiahq2:
    scene bg sabiatent
    show screen infohud("left")
    call sabiabase
    $ renpy.block_rollback()
    if orcfestivalquest == True and crafting_potions_unlocked == False:
        $ crafting_unlocked = True
        $ crafting_potions_unlocked = True
        $ Inventory.add_item(Rhealthpotion)
        s "It's clear that I'm going to need an edge to make the feast something special. This isn't really my area of expertise, but... maybe I need to try brewing potions."
        show sabiaemo closed2 at left
        s "I guess I should be glad my mother forced me to study it along with everything else. But I've been brewing nothing but combat potions for a long time... what was the one she used for celebrations?"
        show sabiaemo normal at left
        s "It was called Royal Gold, but I don't remember the exact ingredients. Not sure I can get them here in camp, either. But this likely isn't the only thing I'll need potions for, so I should start brushing up on my old skills."
    menu:
        "Inventory and Stats":
            hide screen infohud
            $ actor = Sabia
            call statsscreen
            while Sabia.armor == "None":
                $ Sabia.face = "closed2"
                s "I really don't want to walk around a bunch of orcs naked like this."
                call statsscreen
            $ Sabia.face = "normal"
            show screen infohud("left")
            jump sabiahq2
        "Craft items" if crafting_unlocked:
            hide screen infohud
            call crafting_screen
            jump sabiahq2
        "Check progression":
            call progressionscreen
            jump sabiahq2
        "Interrogate catgirl" if maplycaptured:
            if maplytortured:
                s "(After what I did to her, she's pretty much worthless. I'll have to go to the Warchief with the information I gained.)"
                jump sabiahq2
            if maplybefriended:
                s "(I got her to trust me and I think she's said all she knows. I should go the Warchief with what I know.)"
                jump sabiahq2
            call sabiabase
            if maplystripped:
                show maply 3n at right
            else:
                show maply 3 at right
            show maplyemo sad1 at right
            s "Well, now, what should I do with you?"
            call maplyinterrogation
            jump sabiahq2
        "Spend the night with the orcs blocking the training grounds" if raidquest == 3:
            call raidquest4
            jump sabiahq2
        "View world map":
            menu:
                "Geographical map":
                    $ worldmap = "maps/Aleria_with_names.jpg"
                "Colored countries":
                    $ worldmap = "maps/Aleria_with_colors.jpg"
            call screen worldmap
            jump sabiahq2
        "Rest":
            scene bg black

            $ temp1 = 0
            if maply_hellhound_quest >= 11 and SUtentaclequestdone == True and (SUlakequest == 2 or SUlakequest >= 8) and (SUorcstrained == True or SUorctraining == True) and kentarktraining >= 90:
                $ temp1 +=1

            if tutorialraiddone == True and banditintroraiddone == True and kiaprogression >=13:
                $ temp1 +=1

                if orcalliance == "rokgrid" and rokgridraidaftermathdone == True:
                    $ temp1 +=1

                elif orcalliance == "tekrok" and tekrokraidaftermathscene == True:
                    $ temp1 +=1

                elif orcalliance == "dajrab" and dajrabraidaftermathscene == True:
                    $ temp1 +=1

                elif orcalliance == "sabia":
                    $ temp1 +=1

            if temp1 == 3:
                jump orccampphase2_end
            if arenatime == 9:
                if hellhoundchoice == "drug":
                    call RGAhellhounddrug
                elif hellhoundchoice == "sub":
                    call RGAhellhoundhandjob
            if Sabia.stamina > 150:
                "Sabia wasn't too sleepy, but she lay down and, after tossing and turning for a while, managed to sleep."
            elif Sabia.stamina > 50:
                "Wanting to wake up fresh the next day, Sabia lay down and managed to get in a good night of rest."
            else:
                "Sabia lay down, exhausted, and was almost instantly asleep. Despite the roughness of the ground, she slept hard and woke up refreshed."
            $ trialtime += 1
            $ kiacooldown = False
            $ captaincooldown = False
            $ heal_all_troops(1)
            $ Sabia.rest()
            hide screen infohud
            if catgirlraidquest:
                $ catgirlraidperformance -= 1
                "It sounded like the camp was still in an uproar over the theft. If she wanted to do anything about it, she really needed to act soon."
            if catgirlraidquest == False and orcfestivalquest == False and orcfestivalscore < 1:
                "It seemed like an increasing number of orcs were heading toward the Silvertusk Bar every morning. Sabia decided that she should check it out when she got a chance."
            if bargroping == 4 and catgirlraidquest == False:
                call bargropinginvestigation
            if barrinintdelay:
                $ barrinintdelay = False
            if arenatime > 0 and arenatime < 20:
                $ arenatime += 1
                $ RGAtraincooldown = False
                $ RGAdailycooldown = False
                call RGAdailyevents
            if SUtentaclerested == False and SUtentaclequestdone == False:
                $ SUtentaclerested = True
            if maplyhellhoundprompt == True:
                if maply_hellhound_quest == 1:
                    $ maply_hellhound_quest += 1
                    if maplybefriended == True:
                        jump maply_hellhound_quest1
                    else:
                        jump maply_hellhound_quest1_unf
                if maply_hellhound_quest == 5:
                    $ maply_hellhound_quest += 1
                if maply_hellhound_quest == 8:
                    $ maply_hellhound_quest += 1


            jump lowerorccamp
        "Back to camp":
            hide screen infohud
            jump lowerorccamp
    jump sabiahq2


label centralcamp2:
    scene bg centralcamp
    $ renpy.block_rollback()
    if shamanmiracles1prime:
        $ shamanmiracles1prime = False
        "While moving through camp, Sabia saw a surprisingly large group of orcs gathering around something. For once, they were quiet, as if in awe. She headed closer to see what was going on."
        show orcshaman happy3 at right
        call sabiabase
        "To her surprise, the shaman was the one who held their attention. He seemed to be working small magic, granting blessings, giving out bone talismans charged with power, and so on."
        orcshaman "The gods of the orcs smile upon you! Go and attain glory!"
        s "(Gods? No way in hell is that divine magic...)"
        "Sabia was no mage, but she'd seen plenty of magic thanks to her sister. This was nothing but cheap parlor tricks, apparently being passed off as miracles."
        "She'd seen real miracles from the Order of Relona, ones even mages couldn't explain. And this was definitely not that, unless the orc gods were truly pathetic."
        "Every time he worked a new bit of magic, he stirred a circle of bones around with his power. He claimed it was the breath of the gods, but it was nothing but a cheap trick, since even his magic could control orcs' natural bone."
        "If she brought that up, she might damage the shaman's reputation even more. Was it worth it?"
        menu:
            "Mock him publicly":
                $ L_orcs += 1
                show sabiaemo happy2 at left
                s "Oh, shaman~! Could I get a blessing?"
                show orcshaman angry3 at right
                orcshaman "Our gods have nothing for you, human!"
                s "Are you sure? I just want a little blessing on my sword... if you empower all these talismans, surely you can empower an old sword."
                "That was the real test: to see if he had deceived himself, or if he was just a liar. After a flicker of surprise, she saw the shaman's eyes narrow in anger. He knew that he was faking it."
                s "You know... I haven't seen you enchant {i}any{/i} swords. Surely your gods can do that?"
                orcshaman "That is not our way, human. The gods grant blessings upon good, solid bone."
                s "Oh, I see... and here I thought it might be because orc magic couldn't work on metal..."
                orcshaman "Don't be absurd! These are blessings from the gods, not foolish human magic!"
                "A few of the orcs grumbled, however. They might not know anything about racial magical differences, but she heard some of them wondering why the shaman wouldn't bless any weapons. Sabia considered telling them, since she knew enough theory, but realized that wouldn't be as effective as a demonstration."
                "Meanwhile, the shaman was clearly coming to the same conclusion. He cast a larger number of bones and began moving them in a much larger circle, gathering power for some greater work. Maybe even one that would turn the crowd back to his side."
                "Not if she had anything to do about it. Sabia slipped a Lundil into her hand and clenched tightly. She hadn't been cut out to be a mage, but her mother had sent all her children to be tested. She could put just a tiny bit of human essence into the metal..."
                "And toss it directly into the circling orc magic."
                "As she'd hoped, the shaman's control was rough and indiscriminate, so his movement spell tried to grasp the coin as well. Unlike the natural bone, the metal repelled his efforts, sending the entire spell spiraling out of control and bones flying in every direction."
                orcshaman "You... you have insulted the gods!"
                "His roar came too late, though. The orcs had seen his big fancy spell get broken apart by a coin, and while they might not understand magic, they knew weakness when they saw it."
                "Some lingered, but only looking to see if there would be a fight between them. Most drifted away, no longer interested in the shaman's spells. He fumed at her, but didn't come closer."
                "Sabia gave him an innocent smile and then sauntered away. His reputation wouldn't recover from that one for a long, long time."
            "Keep the information to yourself":
                $ shamanmiracles1 = True
                "Smiling, Sabia slipped away. Maybe that information could come in useful one day. For now, he wasn't doing her any harm."
        jump lowerorccamp
    menu:
        "Pick up trash (30 stamina)" if workunlocked:
            $ workunlocked = False
            if cleaningtimes < 1:
                "Sabia took one look at the filthy grounds and shook her head. If she hadn't stooped to cleaning before, she certainly wasn't going to now."
            else:
                "Sabia walked into the center of camp, her eyes sweeping over the filth that had gathered there. Once, she had scrabbled in the dirt like a peasant for a few Lundils."
                "But no more. Vowing never to let herself be brought that low again, Sabia squared her shoulders and left the camp."
                jump lowerorccamp
        "Recruit an orc to fuck Maply" if (maplysexlook == True and maplysexdone == False):
            $ maplysexorc = True
            $ maplysexdone = True
            $ catgirlraidinvestigation += 2
            $ catgirlraidperformance += 3
            show orcbase2 at right
            show orcloincloth2 at right
            show orcstomach2 at right
            show orcemo2 normalopen at right
            call sabiabase
            orc "Huh? Me?"
            s "Who the fuck do you think I'm talking to? If you want me to ask someone else..."
            orc "No, me do it, me do it!"
            s "Good. Now, there are a few terms... I don't want her permanently injured - and don't forget the point is to get information out of her!"
            call orcmaply1
            $ maplystripped = True
            jump sabiahq2
        "Talk to idle orc":
            show orcbase2 at right
            show orcloincloth2 at right
            show orchair2 at right
            show orcstomach2 at right
            show orcemo2 normalopen at right
            call sabiabase
            if trashorcbug >= 6:
                orc "Me hate you."
            elif trashorcbug >= 5:
                $ trashorcbug += 1
                orc "Why you keep coming by? You like me? You want suck my cock?"
                show sabiaemo happy3 at left
                s "Sure, okay!"
                orc "Really?"
                show sabiaemo angry1 at left
                s "No! Don't be a fucking idiot!"
                orc "..."
            elif trashorcbug >= 3:
                $ trashorcbug += 1
                orc "If you not clean, go away!"
            elif trashorcbug >= 1:
                $ trashorcbug += 1
                orc "Seriously, me just want relax here!"
            else:
                $ trashorcbug += 1
                orc "What, you got nothing better to do? Fuck off!"
            jump centralcamp2
        "Talk to Ylva" if RGAylvapresent:
            call ylvaconvo1
            jump centralcamp2
        "Talk to shaman" if shaman_name_revealed == False:
            call sabiabase
            show orcshaman angry1 at right
            if bargroping == 5:
                show orcshaman happy1 at right
                orcshaman "Heh... keep enjoying your freedom, filth."
                s "(He sure seems smug about this murder investigation. I'd better do everything I can to avoid the charges.)"
            else:
                orcshaman "Me want nothing to do with you, filth."
            menu:
                "Rub it in":
                    s "Enjoying your newfound prestige after taking on a little human female?"
                    orcshaman "Shut up!"
                "What do you know about the catgirl raid?" if catgirlraidquest == True:
                    orcshaman "Me tell you nothing, filth!"
                "Have you heard any rumors about problems with the Silvertusk Bar?" if (bargroping == 5 and murderinvshamanhint == False):
                    $ murderinvshamanhint = True
                    orcshaman "Rumors? Can't say me know about any rumors..."
                    s "Well, I just thought I'd come talk to you. I know we haven't been on the best terms."
                    orcshaman "Heh. I'm sure that will change soon, human."
                    show sabiaemo closed2 at left
                    s "(He's much too confident about this - he must have some kind of evidence. I should investigate his tent when I get a chance.)"
                "Nothing":
                    orcshaman "Grrr..."
        "Talk to Ornshakar" if shaman_name_revealed == True:
            call sabiabase
            show orcshaman angry1 at right
            if bargroping == 5:
                show orcshaman happy1 at right
                ornshakar "Heh... keep enjoying your freedom, filth."
                s "(He sure seems smug about this murder investigation. I'd better do everything I can to avoid the charges.)"
            else:
                ornshakar "Me want nothing to do with you, filth."
            menu:
                "Rub it in":
                    s "Enjoying your newfound prestige after taking on a little human female?"
                    ornshakar "Shut up!"
                "Nothing":
                    ornshakar "Grrr..."
            jump centralcamp2
        "Speak to investigator" if bargroping == 5:
            call sabiabase
            show orcbase2 at right
            show orcbeard21 at right
            show orcloincloth2 at right
            show orcnecklace2 at right
            show orcpiercing2 at right
            show orcshoulder2 at right
            show orcemo2 normal at right
            show orcaxe2 at right
            with dissolve
            orc "The investigation of the murders is still ongoing."
            menu:
                "I've gathered all my evidence.":
                    orc "Have you? My investigations have been going well, so perhaps there will be a decision soon..."
                    call bargropingtrial
                "Good luck":
                    pass
            jump centralcamp2
        "Go back":
            jump lowerorccamp
    jump lowerorccamp


label silvertusk2:
    scene bg silvertusk
    $ renpy.block_rollback()
    if silvertuskintro == False:
        call silvertusk_intro
    if (elmyintroduction == False and vehlislocationquest >= 1):
        $ elmyintroduction = True
        show elmy normal at right
        "When Sabia stepped into the bar, she was surprised to notice a catgirl working in one corner. She didn't seem to be serving the tables, instead quietly mixing something not far from Jadk. Given the outfit she was wearing, it was doubtful that this was all she did for the bar."
        "Curious to see a catgirl working there, Sabia approached her."
        call sabiabase
        with moveinleft
        s "Hello there. Did Jadk hire you?"
        if catgirlstatus == "enslaved":
            elmy "..."
            s "What's that look for?"
            show elmy angry1 at right
            show elmy2 arm at right
            elmy "You know what you did! You're even worse than the orcs!"
            "The catgirl stalked away angry, but Sabia just shook her head. She'd known that she wouldn't make friends when she enslaved them, but it was still the best decision."
            jump silvertusk2
        elif catgirlstatus == "free":
            show elmy happy3 at right
            elmy "Oh, hello!"
            show elmy happy2 at right
            elmy "I can't thank you enough for what you've done for us. You're far more generous than we expected any human to be... honestly, I don't think many catgirls would be half as generous in your position."
            show sabiaemo happy1 at left
            s "It was the right thing to do. But if I may ask, why did you choose to stay in camp?"
            show elmy happy1 at right
            elmy "Well, considerable damage was still done to our caravan. Things aren't going to go back to the way they were."
            elmy "Some tried to start a new caravan, but I have to be practical. Since the orc camp is taking workers, it was much safer to stay here and try to build a new life for myself."
            s "I wish you well in that!"
        elif catgirlstatus == "recruited":
            show elmy happy1 at right
            elmy "Hello, milady. Do you need anything today?"
            s "No, I just wanted to speak with you. Apparently you agreed to Tekrok's plan, if you decided to stay and work here?"
            elmy "I don't know how I feel about all his grand statements, that's a little much for me. But the caravan is broken apart and this is a stable, well-paying job, so..."
        else:
            show elmy happy1 at right
            elmy "Hello, milady. Do you need anything today?"
            s "No, I just wanted to speak with you. Are you working off your debt here?"
            show elmy sad1 at right
            elmy "I have to do my part to help the others, but I'd rather not work in the tents. Fortunately, I found this job."
            show elmy happy1 at right
            elmy "Given the skills I have, it's the most practical way to pay off my debt quickly."
        if bartimes >= 3:
            $ L_catgirls += 1
            show sabiaemo happy1 at left
            s "I've worked here myself, actually."
            show elmy happy1 at right
            elmy "I know, Jadk mentioned it to me."
            s "He's a funny old goat, but he means well. Be careful about the patrons, though."
            show elmy normal at right
            elmy "Believe me, I know how they can be."
        else:
            if catgirlstatus == "free":
                pass
            else:
                s "I'll wish you well in your work, then."
        show elmy happy1 at right
        elmy "I'm also selling some things for Jadk, so let me know if you need anything!"
        scene bg silvertusk
    if catgirlraidquest == False and orcfestivalintro == False:
        "The bar was busier than normal, but not with normal patrons. The orcs seemed to be excited about some upcoming event, but Sabia couldn't determine exactly what."
    menu:
        "Ask about the commotion" if (catgirlraidquest == False and orcfestivalintro == False):
            $ orcfestivalintro = True
            call sabiabase
            show jadkbase at right
            show jadkemo closedhappy at right
            s "What's everyone so excited about? It's not another trial, is it?"
            jadk "Gwahaha, I hope not!"
            show jadkemo happy2 at right
            jadk "No, it's much simpler. Jadk guesses humans don't care about this, but it's almost time for the Horned God's Night."
            s "The what now?"
            jadk "It's said that on the longest night of the year, the Horned God dances through the forests, renewing the power of life itself. If we celebrate too, we join in the renewal, granting us new strength in the year to come!"
            jadk "At least, that's how the stories go. Jadk doesn't really believe it, gwahaha!"
            s "Ah, so it's a local festival. It seems to be a big deal, though."
            jadk "Aye, Jadk thinks it's perhaps the most important festival for orcs. Everyone has to prove they still have the strength to lead - even Warchief Groknak!"
            s "Hmm... everyone, huh? Does that include me? Could I become a leader?"
            jadk "Well... Jadk doesn't think that's very likely. But if you want to get orcs to follow you, now is the best time. They know you well enough that you could try."
            s "And what exactly does trying involve? Is this going to be a fight or something?"
            jadk "No! No blood can be shed on the Horned God's Night, or you will be cursed in the new year."
            jadk "No, it is a night for celebration! Every leader will compete to present the grandest feast, to prove that they have the blessings of strength to lead the tribe."
            show sabiaemo closed2 at left
            s "(It sounds like the perfect opportunity to turn the reputation I've generated among the orcs into an actual leadership position. But it's hard to judge what exactly they'd want...)"
            jadk "Anyone can host their own feast, but Jadk thinks that would be a hard path for you. But each of the Captains will be looking for any edge against their rivals..."
            s "Yeah, I get it. Thanks, Jadk!"
            jadk "Jadk looks forward to your feast, gwahaha!"
            s "(There's no middle ground on this one, since I'd just be working against myself. I need to pick a side and go all in...)"
            menu:
                "Assist Tekrok's feast" if A_tekrok >= 2:
                    $ orcalliance = "tekrok"
                    s "(Tekrok is my strongest bet. I should go speak with him as soon as I get a chance.)"
                "Assist Rokgrid's feast" if A_rokgrid >= 2:
                    $ orcalliance = "rokgrid"
                    s "(Probably best to go with Rokgrid. I should go speak with him as soon as I get a chance.)"
                "Assist Dajrab's feast" if A_dajrab >= 1:
                    $ orcalliance = "dajrab"
                    s "(I'll have to bet on Dajrab. I should go speak with him as soon as I get a chance.)"
                "Domination: Make your own feast" if dom >= 2:
                    $ orcalliance = "sabia"
                    $ dom += 1
                    s "(I've made my own way this far, I won't stop now. I can't be dependent on the Captains.)"
            s "(This isn't so different from courting other noble families, but that was never my strong suit. Plus, I have no idea what orcs think makes for the best feast. Booze? Fucking?)"
            s "(If the festival is on the solstice, I have quite a while. I should do everything in my power to prepare...)"
            jump silvertusk2
        "Ylva and Jadk" if (RGAylvapresent == True and ylva1jadktalk == False):
            call ylva1jadk
            jump silvertusk2
        "Set up a reward for Sabia's squad" if (SUelmyprompt == True and SUorcstrained == False):
            $ temp1 = SUelmyquest
            if Inventory.has_item(HGNBeer) > 0:
                $ temp1 += 1
            if Inventory.has_item(Cheapfood) > 0:
                $ temp1 += 1
            if temp1 >= 6:
                "Sabia checked over all her plans one more time, but she thought everything was set up properly. Time to use Elmy to motivate her squad a little..."
                $ SUorcstrained = True
                call SUelmypokerscene
            else:
                if temp1 > 3:
                    "Sabia had a clear idea how she wanted to motivate her squad, but didn't have all the details in order yet."
                else:
                    "Sabia wanted to motivate her squad, but she didn't feel remotely ready yet."
                if SUelmyjadk == False:
                    "For a start, she wasn't entirely sure how to begin. Best to find someone who could give her a few tips about how orcs thought."
                if SUelmyreservation == False:
                    "Getting a room for a whole night proved to be a problem - she wasn't sure how to go about formally reserving one."
                if Inventory.has_item(HGNBeer) <= 0:
                    "Sabia thought she'd need some beer to keep the orcs happy."
                if Inventory.has_item(Cheapfood) <= 0:
                    "She'd also need some food - the cheapest she could find, ideally."
                if SUelmyaccepted == False:
                    "Finally, she needed to find a vulnerable catgirl to do the work..."
        "Plan for the Horned God's Night" if (catgirlraidquest == False and orcfestivalintro == True and orcfestivalquest == False and arenatime <= 0):
            call sabiabase
            show jadkbase at right
            show jadkemo closedhappy at right
            if orcalliance == "sabia":
                $ orcfestivalquest = True
                jadk "So... you'll be making a feast all your own, huh? Quite an undertaking, gwahaha!"
                s "I was hoping that you could tell me what all will be necessary."
            else:
                jadk "Eh? You change your mind and want to make a feast yourself?"
                menu:
                    "Yes":
                        $ orcfestivalquest = True
                        $ orcalliance = "sabia"
                        s "I was hoping that you could tell me what all will be necessary."
                    "No":
                        s "No, I'm still hoping to make an alliance."
                        jump silvertusk2
            jadk "Just having a feast is no problem. Anyone can offer food and beer to his friends. Gwaha, Jadk will have a little feast of his own!"
            jadk "But a true feast, one that will bring honor and followers... that is what you want, and that is more difficult."
            s "For it to be a feast, I assume that I'll need food and drink."
            jadk "Of course, of course. The more the better!"
            jadk "You should also have a tent of some kind. Jadk does not know if you can find such a thing in the camp, you may need to wander further."
            s "I can try to get in contact with a human merchant, since that was my goal anyway. But what else do I need?"
            jadk "Well, the most important thing is to make a feast that will be remembered! Do all that you can!"
            jadk "But there is one thing that Jadk thinks will be new to you. At the center of your tent, there must be a great shrine of animal horns, an offering to the Horned God."
            s "Hmm... I guess I can try to go hunting for those."
            jadk "And not only that, you need a rare dish to start your feast. For a lesser warrior, any deer would be fine, but for you... Jadk suggests trying to bring down a white hind."
            s "That might be difficult, but I can try."
            if A_jadk >= 5:
                $ Inventory.add_item(Furnishings)
                jadk "Jadk has a little something to make things easier - you can use extra furnishings from the bar. Gwahaha, no need to get your own!"
                s "Thank you, Jadk."
            jadk "Those are Jadk's suggestions. Jadk looks forward to your feast, gwahaha!"
            jump silvertusk2
        "Buy a drink":
            call sabiabase
            show sabiaemo closed1 at left
            s "(I've never been one for drinking alone, and I'm sure as hell not getting drunk in a bar full of orcs.)"
            jump silvertusk2
        "Talk to Jadk":
            call sabiabase
            show jadkbase at right
            show jadkemo closedhappy at right
            jadk "Pull up a stool, then!"
            menu silvertusk2_jadk:
                "Chat":
                    "Sabia and Jadk chatted about nothing in particular."
                    jump silvertusk2_jadk
                "Can you offer any help for my troops?" if recruitmentopened == True and jadkmoralehelp == False:
                    $ jadkmoralehelp = True
                    jadk "Old Jadk isn't quite ready to fight, gwahaha!"
                    s "Haha, I didn't mean that. Just wondering if you had any insight."
                    if A_jadk >= 5:
                        $ Sabiasquad.combat += 1
                        jadk "Not so many insights... but Jadk can offer your boys a discount and a table to relax here. Ought to make them more motivated!"
                        s "Ah, would you? That's great, Jadk!"
                        if orcalliance == "sabia":
                            if kulganalive == True:
                                $ Kulganorcs.combat += 1
                                jadk "Gwahaha, no problem! Since you're going things alone, Jadk will even throw in drinks for other troops!"
                            else:
                                jadk "Gwahaha, no problem! Jadk thinks you need all the help you can get, trying to go things alone!"
                        else:
                            jadk "No problem, gwahaha!"
                    else:
                        jadk "Sorry to say Jadk isn't sure. But good luck, Sabia!"
                    jump silvertusk2_jadk
                "Can you help me prepare for Kentark training?" if kentarktraining > 1 and kentarkjadk == False:
                    $ kentarkjadk = True
                    $ kentarktraining += 10
                    jadk "Well! That is quite the thing! Old Jadk never tried to become a Kentark!"
                    s "But you know some about it and can help me, right?"
                    jadk "Probably not, but Jadk can try a trick or two!"
                    "Contrary to what he said, Jadk was able to teach her many things about Kentarks. By the time they finished talking, Sabia felt much more prepared for her training."
                    jump silvertusk2_jadk
                "How would I go about setting up a reward for my squad?" if SUelmyprompt == True and SUelmyjadk == False:
                    $ SUelmyjadk = True
                    $ SUelmyquest += 1
                    jadk "Eh? What's this now?"
                    "Sabia went about explaining what she had in mind. Jadk's eyebrows shot up, but in the end he nodded and seemed to understand."
                    "He didn't have a lot to say about it, but offered a few suggestions. By the end of it, Sabia felt that she had a clear idea as to how to do the event."
                    jump silvertusk2_jadk
                "Am I ready for the Horned God's Night?" if (orcalliance == "sabia" and arenatime < 1):
                    if vehlislocationquest < 3:
                        jadk "Jadk doubts it. You better find yourself some new contacts if you want to impress everyone."
                        jump silvertusk2_jadk
                    if huntedwhitehind == False:
                        jadk "Jadk really thinks you should try for a white hind. Hope it's not too rough to catch one, gwahaha!"
                        jump silvertusk2_jadk
                    if bargroping == 5:
                        jadk "Maybe take care of that investigation first, hmm?"
                        jump silvertusk2_jadk
                    jadk "Maybe so. You've sure worked hard, gwaha! But do you think everything is ready?"
                    menu:
                        "Yes":
                            jadk "Well, then, Jadk thinks you will have a very busy time preparing all the little details..."
                            jump HGNsabia
                        "Not yet":
                            jadk "Probably smart, Jadk thinks. Doing everything yourself, you have a rough path ahead of you."
                            jump silvertusk2_jadk
                "So... you own a bar?" if jadktalk1 == False:
                    $ jadktalk1 = True
                    $ A_jadk += 1
                    show jadkemo happy2 at right
                    jadk "Sure looks that way!"
                    s "Why, though?"
                    show jadkemo closednormal at right
                    jadk "Well, Jadk is getting old. Jadk's got some good years left in him, but not so many if Jadk try to fight with the young bucks. Running a bar is a good way to keep busy."
                    show sabiaemo closed2 at left
                    s "Okay, but that actually wasn't what I meant. Why go to the trouble of building something in a camp like this? Don't you risk losing it?"
                    show jadkemo normal at right
                    jadk "Definitely. But the longer we stay here, the more people get situated. Without a bar, the warriors end up drinking wherever, and that's just a mess."
                    show jadkemo angry at right
                    jadk "Besides, owning anything doesn't mean a lot anymore. No offense, but the Kingdom of Lundar tends to burn down property anywhere."
                    show sabiaemo pout2 at left
                    s "..."
                    show jadkemo happy2 at right
                    jadk "Clearly Jadk should have said \"no offense\" twice, huh?"
                    show sabiaemo closed4 at left
                    s "...no, I understand."
                    show jadkemo happy1 at right
                    jadk "A fine young thing like you has every reason to play it safe. But Jadk? Jadk is old, and happy to gamble what's left of his life."
                    show sabiaemo annoyed1 at left
                    s "...fine young thing?"
                    show jadkemo happy2 at right
                    jadk "Gwahaha, no offense intended!"
                    show sabiaemo normal at left
                    s "Heh, fair enough."
                    jump silvertusk2_jadk
                "Why the name Silvertusk?" if jadkwife == False:
                    if A_jadk > 3:
                        $ jadkwife = True
                        $ A_jadk += 1
                        show jadkemo closedsad at right
                        jadk "..."
                        show sabiaemo sad1 at left
                        s "Would you rather I stopped asking?"
                        show jadkemo sad at right
                        jadk "No, it's... alright. Just something Jadk hasn't gone back to in a long time."
                        jadk "Silvertusk was Jadk's mate's title."
                        show sabiaemo normal at left
                        s "She had a title? She was a strong warrior, then?"
                        show jadkemo happy1 at right
                        jadk "What, you think orcs only get titles for killing people? Gwahaha, no, she was a tough old bird, but she couldn't swing a sword to save her life."
                        show jadkemo closedhappy at right
                        jadk "No, she was a farmer. Real good one. Jadk felt right proud to protect her and her work."
                        show sabiaemo sad2 at left
                        s "I see. Perhaps I should go."
                        show jadkemo closednormal at right
                        jadk "Think Jadk is angry with you, huh? Nah, don't worry about it."
                        show sabiaemo sad1 at left
                        s "But I assume that humans killed her."
                        show jadkemo angry at right
                        jadk "You want the truth? Jadk honestly doesn't know. While Jadk was with the war party, someone raided the farm and left her dead. When it comes to straight killing, there's no real way to tell who did it."
                        show jadkemo happy1 at right
                        jadk "For a few years, Jadk was pissed at Lundar and all humans, gwaha. If not for the war, Jadk might have stayed beside her where he belonged, after all."
                        show jadkemo closedsad at right
                        jadk "But you can't stay young and angry forever. Eventually Jadk got old, and hanging on to that anger started to hurt."
                        show sabiaemo sad2 at left
                        s "..."
                        show jadkemo normal at right
                        jadk "Anyway, that's in the past. Jadk wishes to hell she was still here with me, but... she's not."
                        show sabiaemo sad1 at left
                        s "Do... do orcs believe in an afterlife? I know you have your superstitions, but..."
                        show jadkemo closedsad at right
                        jadk "Jadk is too old for that, girl. She's not with me here now."
                        show sabiaemo closed1 at left
                        s "..."
                        show sabiaemo sad2 at left
                        s "I'm sorry for bringing it up."
                        show jadkemo happy2 at right
                        jadk "No, no, don't worry about it, gwahaha! Felt good to talk about her again, truth be told!"
                        show sabiaemo normal at left
                        s "I'll keep what you said private."
                        show jadkemo closednormal at right
                        jadk "It's no secret, but... Jadk would appreciate that."
                        show sabiaemo happy3 at left
                        s "Thank you for confiding in me, Jadk."
                        show jadkemo happy2 at right
                        jadk "Hey, you almost got Jadk's name that time! You're getting better, gwahahahaha!"
                        s "Haha..."
                        jump silvertusk2_jadk
                    else:
                        show jadkemo normal at right
                        jadk "No story behind it, Jadk just likes the name."
                        show sabiaemo closed1 at left
                        s "(That's the first thing he's said that sounds like a lie.)"
                        jump silvertusk2_jadk
                "How well-defended is this camp?" if jadktalk2 == False:
                    $ jadktalk2 = True
                    show jadkemo happy1 at right
                    jadk "Looking for military intelligence, little lady? Jadk's fighting days are done, he doesn't pay too much attention to that sort of thing."
                    s "Honestly, I'm more concerned about it getting attacked at the moment."
                    show jadkemo normal at right
                    jadk "Well, this is probably the biggest, most stable camp in the whole region. We don't raid close to Lundar, try not to piss off the human towns, you get it."
                    show sabiaemo closed1 at left
                    s "Hmm."
                    show jadkemo happy2 at right
                    jadk "Maybe you aren't much for quietly minding your own business? Suit yourself, gwahaha!"
                    jump silvertusk2_jadk
                "I'm surprised non-orcs can walk freely in camp." if jadktalk3 == False:
                    $ jadktalk3 = True
                    $ A_jadk += 1
                    show jadkemo happy2 at right
                    jadk "Yeah, well, that's how it is here, gwaha!"
                    show jadkemo normal at right
                    jadk "Believe Jadk, there were some real differences of opinion about that. But in the end, Warchief Groknak took a middle road. We need the trade to get by."
                    show sabiaemo irritated2 at left
                    s "Are there many that come and go freely?"
                    show jadkemo happy2 at right
                    jadk "Just a few, we don't like to draw too much attention. Because of you humans, gwahaha!"
                    show jadkemo closedhappy at right
                    jadk "Neve goes where she wants, of course. She actually stops by here a lot, but she usually comes later."
                    jadk "We get merchants and traders, mostly elven and a few minotaurs. And one human woman who's brave, reckless, or insane... or possibly all three."
                    jadk "And now you, depending on the choices you make, Jadk thinks."
                    show sabiaemo normal at left
                    s "I see. Thank you for answering me."
                    show jadkemo happy2 at right
                    jadk "Oh, Jadk is just happy to have such a good listener, gwahaha!"
                    jump silvertusk2_jadk
                "What do you think about the Captains?" if captainsintro == True:
                    show jadkemo happy2 at right
                    jadk "Careful now, or Jadk will talk your ear off, gwahaha!"
                    s "I would actually like to know what you think, though."
                    show jadkemo closednormal at right
                    jadk "Honestly? This whole tribe is still young, it doesn't know what it is. This whole Captain fight is us growing up."
                    show sabiaemo irritated2 at left
                    s "How do you mean?"
                    show jadkemo normal at right
                    jadk "See, nobody is quite sure what our place in the world is anymore. Warchief Groknak thinks everything can stay just the way it was, but there aren't many who agree anymore."
                    jadk "Each Captain wants to take things in his own direction, Jadk thinks. Even Dajrab, much as he tries to pull a balancing act."
                    show jadkemo happy2 at right
                    jadk "Rokgrid thinks we should make peace instead of war, Tekrok thinks we should make... different war than the first time, Jadk guesses. Gwahaha!"
                    show jadkemo normal at right
                    jadk "If you ask Jadk? We probably won't turn out like any of them. Nobody knows who they really are when they're young."
                    show sabiaemo normal at left
                    s "And what about you? What do you think the camp should become?"
                    show jadkemo happy2 at right
                    jadk "Me? Jadk is too old to grow up, hahaha! Jadk just hopes he can hold on long enough to see what happens!"
                    if jadkcaptainboost == False:
                        $ jadkcaptainboost = True
                        $ A_jadk += 1
                        show sabiaemo closed2 at left
                        s "(At first I thought that laugh had to be faked, but he seems so earnest.)"
                        show sabiaemo closed1 at left
                        s "(I hate to admit it, but it's kind of infectious. I hope I'm half as happy when I'm old.)"
                        show sabiaemo annoyed2 at left
                        s "(And not like my mother. I'm not sure I've ever heard that woman laugh sincerely.)"
                    jump silvertusk2_jadk
                "Why do orcs speak in third person?" if ylvatalkthirdperson == False:
                    show jadkemo happy2 at right
                    jadk "Gwahaha, you should ask someone smarter than Jadk."
                    show jadkemo normal at right
                    jadk "For Jadk to say \"I\"... it would not be right. This is not our way."
                    show jadkemo happy2 at right
                    jadk "But some orcs speak like you humans, gwahaha! So don't listen to Jadk too much!"
                    jump silvertusk2_jadk
                "What do you know about the catgirl raid?" if (catgirlraidquest == True and catgirlraidjadk == False):
                    $ catgirlraidjadk = True
                    show jadkemo closedsad at right
                    jadk "Ah... Jadk knows too much about it."
                    s "What do you mean?"
                    jadk "Jadk schedules all the shipments into the camp. We need to avoid human patrols, find merchants willing to sell to us, many things."
                    show sabiaemo closed2 at left
                    s "I see. Does that mean you're blamed for this?"
                    show jadkemo sad at right
                    jadk "No, but it was no normal shipment. It is a great loss to the camp for it to be stolen..."
                    s "..."
                    show jadkemo normal at right
                    jadk "But this is only one part of life, there are others. Don't let Jadk make you sad."
                    show sabiaemo normal at left
                    s "No, I'm interested in this. What can you tell me about it?"
                    if A_jadk >= 5:
                        $ A_jadk += 1
                        $ catgirlraidinvestigation +=3
                        jadk "The catgirls stole a shipment of valuable metal. There was no one in on it, Jadk thinks, they just caught the shipment unawares."
                        s "Hmmm..."
                        jadk "Also... here, take this."
                        "Jadk handed Sabia a paper with orc scratchings on it. Making it out, Sabia realized that it was a bill of sale involving a large quantity of steel. Most importantly, it listed towns, suggesting an exact route for the caravan."
                        jadk "That's the safest path... at least Jadk thought so."
                        s "So, they didn't really have many opportunities to intercept the shipment, assuming they operate from nearby."
                        jadk "Jadk thinks so too."
                        show sabiaemo happy2 at left
                        s "This will be helpful. Thank you, Jadk."
                        jadk "Good luck! There is honor for you and for the tribe if you can recover what was stolen..."
                    elif A_jadk >= 2:
                        $ catgirlraidinvestigation +=1
                        jadk "The catgirls stole a shipment of valuable metal. There was no one in on it, Jadk thinks, they just caught the shipment unawares."
                        s "Alright. Thank you, Jadk."
                    else:
                        jadk "Just that the catgirls stole a shipment of valuable metal. Sorry, that's all Jadk knows."
                        s "Hmmm..."
                    jump silvertusk2_jadk
                "Can we talk about the murder investigation?" if bargroping == 5 and murderinvjadk == False:
                    $ murderinvjadk = True
                    $ bargropeinv += 1
                    $ A_jadk += 1
                    s "I'm not sure if you've heard, but..."
                    jadk "Aye, Jadk heard of this. Someone came around asking a few questions."
                    show sabiaemo closed2 at left
                    s "And?"
                    jadk "Jadk told him the truth: that he didn't see anything."
                    show sabiaemo normal at left
                    s "..."
                    show jadkemo happy2 at right
                    jadk "Can anyone blame Jadk if he didn't notice anything unusual and couldn't connect the dots? Jadk is getting older, after all!"
                    show sabiaemo happy1 at left
                    s "Thanks, Jadk!"
                    jadk "Gwaha, for what?"
                    jump silvertusk2_jadk
                "Where could I find venomnettle?" if nettlequest == False:
                    show jadkemo normal at right
                    jadk "Oh, Jadk bets it's growing all around the edges of camp, just poke around near the outskirts."
                    jadk "It's damn tough, though. You look like you got some muscle on ya, but you still might need something to help you out."
                    jump silvertusk2_jadk
                "Do you want to attend my feast?" if orcfestivalquest == True and arenatime <= 0:
                    jadk "Want to? Yes! But Jadk is already planning his own, a simple little party for those who want to drink without politics."
                    s "Sure, I understand."
                    jadk "Make sure to visit!"
                    jump silvertusk2_jadk
                "Any more advice about the Red God's Arena?" if (arenatime > 4 and recruitmentopened == False):
                    jadk "Nope, Jadk's said pretty much everything, gwahaha!"
                    jump silvertusk2_jadk
                "Go back":
                    jump silvertusk2
        "Recruit Elmy for the orc squad event" if SUelmyprompt == True and SUelmyaccepted == False:
            $ SUelmyaccepted = True
            $ SUelmyquest += 1
            call sabiabase
            with dissolve
            s "Stop sulking and get over here, Elmy."
            show elmy angry1 at center
            show elmy2 arm at center
            with moveinright
            elmy "What is it?"
            s "Alright, listen up..."
            "When Sabia explained what Elmy would be doing, the catgirl became more and more irritated."
            if elmybribery == True:
                elmy "You said that orc would be the last time!"
                show sabiaemo annoyed2 at left
                s "I lied. Honestly, I {i}own{/i} you - did you expect me not to make use of my possessions?"
                show elmy sad1 at center
                elmy "But... I was starting to help with the potions... some of the orcs even respected me a little..."
                show sabiaemo eyebrow1 at left
                s "Well, they won't after this. Now, do I need to threaten all your friends and family again, or will you cooperate?"
                show elmy angry1 at center
                elmy "..."
                show elmy normal at center
                elmy "I will do whatever you command."
                show sabiaemo happy2 at left
                s "Good. I'll let you know when you're needed."
            else:
                elmy "We may be slaves, but I'm not some tent whore! I have an important job to do here!"
                show sabiaemo angry1 at left
                s "Yes, and that's a privilege that can be taken away from you if you don't cooperate."
                show sabiaemo eyebrow1 at left
                s "Now, tell me: do you want to suck off a few orcs now, or as many orcs as you can fit into a day?"
                show elmy normal at center
                elmy "..."
                show elmy angry1 at center
                elmy "You're no different from these orcs. You think you can just strong arm me into doing whatever you want."
                show sabiaemo angry1 at left
                s "I {i}am{/i} different. The orcs just want to use you, but I {i}own{/i} you. Do you really think you're in a position to argue with me?"
                show elmy normal at center
                elmy "I..."
                show sabiaemo angry2 at left
                s "I could have you tortured or executed, but that's too easy... what about your family? Friends from the caravan? It wouldn't be hard to find them and punish them if you don't cooperate, then throw all of you to the cruelest of orcs."
                show sabiaemo eyebrow1 at left
                s "Or you could obey me, suck a few cocks, and keep everyone safe."
                elmy "..."
                show elmy sad1 at center
                elmy "Very well, I will do what I must."
            jump silvertusk2
        "Talk to Elmy" if elmyintroduction:
            if catgirlstatus == "enslaved":
                call openshop (ElmyshopEnslaved)
                jump silvertusk2
            call sabiabase
            show elmy happy1 at right
            elmy "Can I help you?"
            menu silvertusk2_elmy:
                "What can I purchase from you?":
                    call openshop (Elmyshop)
                    jump silvertusk2
                "Can you offer any help for my troops?" if recruitmentopened == True and elmymoralehelp == False:
                    $ elmymoralehelp = True
                    elmy "What manner of help do you think I can offer a bunch of orcs?"
                    s "I don't mean my orcs... I mean the catgirls working for me. You know them, right? Surely you want them to stay safe..."
                    elmy "...I suppose I should be grateful you've made them a normal part of your forces. There's a little I can do."
                    elmy "Normally our warriors went into combat assisted by various potions. Those systems fell apart when our caravan was taken. I could help your group get them organized again."
                    s "That would be great!"
                    elmy "There are a lot of options, though. Most of them fall into categories of increasing speed and stealth, or increasing strength and stamina - and those two aren't compatible. Basically, you can focus on increasing your strengths, or limiting your weaknesses."
                    s "Hmm..."
                    menu:
                        "Increase catgirl speed and stealth":
                            $ Catgirlrecruits.raid += 1
                            $ Catgirlallies.raid += 1
                            elmy "Understood. Once they're using their usual potions, you'll find they're better raiders."
                        "Increase catgirl strength and stamina":
                            $ Catgirlrecruits.defense += 1
                            $ Catgirlallies.defense += 1
                            elmy "Understood. Once they're using their usual potions, you'll find they're better defenders."
                    s "If those are the normal potions... any chance we can get them even more powerful ones?"
                    elmy "Maybe, but it would require ingredients we aren't likely to find around here."
                    jump silvertusk2_elmy
                "What do you think of Lundar?":
                    show elmy normal at right
                    elmy "Should I have elaborate thoughts about it?"
                    s "Well, not necessarily, but I'm surprised how calm you seem with me."
                    elmy "Fearing humans has never made sense to me. Maybe Lundar is dangerous, but that's too big for someone like me. On an individual level, humans aren't so different from us."
                    jump silvertusk2_elmy
                "How does the orc camp compare to the caravan?":
                    elmy "What surprised me is just how much {i}stuff{/i} the orcs have. I guess they can accumulate a lot, since they don't have to move all the time."
                    s "Huh, that's really the first thing that stuck out to you?"
                    show elmy sad1 at right
                    elmy "Their situation does seem a little sad to me. The drinking, the violence... it feels like they're trying to forget what they've lost."
                    s "..."
                    jump silvertusk2_elmy
                "You don't mind serving the orcs?":
                    elmy "It isn't so bad. They're at least honest and straightforward in what they want."
                    s "Huh. I guess catgirls can't afford to be as picky."
                    show elmy sad1 at right
                    elmy "That's not true. I don't mind men, but I'd really much rather be with other women."
                    s "How does that work, anyway? I assume you have sexual relationships with each other, but what if you want children?"
                    show elmy sad2 at right
                    elmy "If you find a good answer to that question, let us all know!"
                    show elmy happy2 at right
                    elmy "As I see it, that's just the way things are. Some catgirls are lucky enough to have an elf village that will cooperate, but others have to either make compromises or give something up."
                    s "And what about you?"
                    elmy "It doesn't seem very practical to think about romance or children right now, not with the way things are going."
                    jump silvertusk2_elmy
                "Do you want to attend my feast?" if arenatime < 1:
                    elmy "Thank you for the offer, but I will have to work here."
                    jump silvertusk2_elmy
                "Will you be involved with the Red God's Arena?" if (arenatime > 0 and recruitmentopened == False):
                    elmy "They've asked me to brew a lot of potions, but otherwise I'm content to ignore it."
                    jump silvertusk2_elmy
                "Have you ever heard of a potion called Royal Gold?" if (crafting_potions_unlocked == True and royalgoldunlocked == False):
                    $ Elmyshop.inventory.append([Rroyalgold,95,1])
                    $ royalgoldunlocked = True
                    elmy "Hmm... perhaps. Does it make celebrations more joyous?"
                    show sabiaemo happy1 at left
                    s "Yes, that sounds right! It also makes people more likely to bond while drinking it."
                    show elmy happy2 at right
                    elmy "We have something similar, but we call it \"Heart of the Pride\". But if you want one for orcs or humans, I may be able to figure it out..."
                    s "Please do! I'd gladly pay for the recipe!"
                    jump silvertusk2_elmy
                "Do you know why Maply doesn't stay in camp?" if (recruitmentopened == True and nevekiaprogression == 0):
                    $ nevekiaprogression = 1
                    elmy "We're not good friends or anything... but I do worry about her a bit. She's probably safer out there."
                    s "But does she seem to be acting strange to you?"
                    elmy "Yes, there's something strange. The oddest thing was that I saw her go visit that elf after hours..."
                    s "Alioch? Surely the two of them aren't..."
                    elmy "Elves are our historical allies, so it's possible. But Maply won't talk to me about it - perhaps you should ask Alioch?"
                    s "Yes, perhaps I should."
                    jump silvertusk2_elmy
                "(Ask about Kia)" if (kiaprogression >= 3 and kiaelmyquestion == False):
                    $ kiaelmyquestion = True
                    call KLelmyscene1
                "Pay Elmy to collect the ingredients" if (kiaelmyquestion == True and kiaelmyscene == False):
                    if money >= 110:
                        menu:
                            "Pay 110 Lundils":
                                $ money -= 110
                                $ kiaelmyscene = True
                                elmy "Good. I'll mark a location on your map - meet me there when you're ready."
                                jump silvertusk2_elmy
                            "Not now":
                                s "I'll be back later."
                                jump silvertusk2_elmy
                    else:
                        s "(I don't have enough.)"
                        jump silvertusk2_elmy
                "Do you know anything about Kentark potions?" if kentarktraining > 1 and kentarkelmy == False:
                    elmy "That sounds difficult, I certainly don't know anything myself. But if you know the method, I could try to help."
                    if Inventory.has_item(Venomnettle) and Inventory.has_item(Vigorreeds) and Inventory.has_item(Steelshrooms) and Inventory.has_item(Firemoss):
                        s "I have the ingredients here: Venomnettle, a Vigor Reed, Steelshroom, and Fire Moss. But the method to brew the potion is rather difficult."
                        elmy "If you're willing to give up all those ingredients, I can help!"
                        menu:
                            "Craft Kentark potion":
                                $ Inventory.rem_item(Venomnettle)
                                $ Inventory.rem_item(Vigorreeds)
                                $ Inventory.rem_item(Steelshrooms)
                                $ Inventory.rem_item(Firemoss)
                                $ kentarkelmy = True
                                $ kentarktraining += 20
                                $ Sabia.hp = 1
                                s "Alright, let's try it!"
                                "Sabia explained what she understood and, after some work, they successfully managed to brew the potion that it was said Kentarks drank."
                                "It left Sabia feeling like shit, but maybe her body would be more resistant to the poisons some Kentarks used in their training, in the future."
                                jump silvertusk2_elmy
                            "Not now":
                                s "Maybe later."
                                jump silvertusk2_elmy
                    else:
                        s "(I need Venomnettle, a Vigor Reed, Steelshroom, and Fire Moss.)"
                "Nothing":
                    jump silvertusk2
            jump silvertusk2
        "Talk to orc allies" if bargroping == 5 and murderinvallies == False:
            $ murderinvallies = True
            $ bargropeinv += 1
            call sabiabase
            show orcbase at right
            show orcloincloth at right
            show orcaxe at right
            show orcnecklace at right
            show orcemo normal at right
            with dissolve
            s "Did you hear that they're investigating the... fun we had?"
            show orcemo angry at right
            orc "Really? That's bullshit... lots of fights end in death."
            s "Yeah, well, the shaman has it out for me. I'm guessing the investigator will eventually ask you about it."
            orc "We say nothing!"
            s "Actually, I suggest you answer, we just need to have our stories straight..."
            scene bg black with dissolve
            pause 1
            scene bg silvertusk
            call sabiabase
            show sabiaemo happy1 at left
            show orcbase at right
            show orcloincloth at right
            show orcaxe at right
            show orcnecklace at right
            show orcemo normal at right
            with dissolve
            s "Is everyone's memory clear now?"
            show orcemo smile2 at right
            orc "Oh, we understand exactly what we saw."
            jump silvertusk2
        "Talk to orc witness" if bargroping == 5 and murderinvwitness1 == False:
            call sabiabase
            show sabiaemo normal at left
            show orcbase at right
            show orcloincloth at right
            show orcstomach at right
            show orcemo smile1 at right
            with dissolve
            orc "You know, human... it really would be a shame if someone noticed that you left with the missing orcs just before they disappeared..."
            show orcemo smile2 at right
            orc "Such a shame if it was mentioned to the investigator."
            show sabiaemo angry1 at left
            s "There's no need to play games. What do you want?"
            orc "100 Lundils and me keep my mouth shut."
            menu:
                "Bribe him" if money >= 100:
                    $ murderinvwitness1 = True
                    $ bargropeinv += 1
                    $ money -= 100
                    s "There... are you happy?"
                    show orcemo smile1 at right
                    orc "Oh, very happy! Me don't remember a thing!"
                "I don't have enough money" if money < 100:
                    orc "Such a shame... me just might finding myself wandering to the investigator if that doesn't change..."
                "Use a catgirl slave" if (catgirlstatus == "enslaved" and elmyintroduction == True):
                    $ murderinvwitness1 = True
                    $ elmybribery = True
                    $ bargropeinv += 1
                    $ slavery += 1
                    s "I have an alternate proposal. What if I let you use one of the catgirl slaves - not someone from the tents, one all to yourself."
                    orc "Oh! Me thinks that sounds good too..."
                    s "Good. Elmy - get over here!"
                    show elmy angry1 at center
                    show elmy2 arm at center
                    with moveinleft
                    "The catgirl came, but not happily. Judging from the irate way her ears twitched, she had heard their conversation."
                    elmy "We may be slaves, but I'm not some tent whore! I have an important job to do here!"
                    show sabiaemo angry1 at left
                    s "Yes, and that's a privilege that can be taken away from you if you don't cooperate."
                    show sabiaemo eyebrow1 at left
                    s "Now, tell me: do you want to suck off one orc now, or as many orcs as you can fit into a day?"
                    show elmy normal at center
                    elmy "..."
                    show elmy angry1 at center
                    elmy "You're no different from these orcs. You think you can just strong arm me into doing whatever you want."
                    show sabiaemo angry1 at left
                    s "I {i}am{/i} different. The orcs just want to use you, but I {i}own{/i} you. Do you really think you're in a position to argue with me?"
                    show elmy normal at center
                    elmy "I..."
                    show sabiaemo angry2 at left
                    s "I could have you tortured or executed, but that's too easy... what about your family? Friends from the caravan? It wouldn't be hard to find them and punish them if you don't cooperate, then throw all of you to the cruelest of orcs."
                    show sabiaemo eyebrow1 at left
                    s "Or you could obey me, suck one orc's cock, and keep everyone safe."
                    elmy "..."
                    show elmy sad1 at center
                    elmy "Very well, I will do what I must."
                    call HGNelmysceneA
                    play music orccamp fadeout 2.0 fadein 2.0
                    scene bg silvertusk
                    "Judging from the orc's satisfied look, Sabia was pretty sure he'd been adequately paid. She checked just to made sure, then was happy to move away from the loathsome vermin."
                "Refuse":
                    orc "Such a shame... me just might finding myself wandering to the investigator if that doesn't change..."
            jump silvertusk2
        "Deliver venomnettle" if nettlequest == False:
            if gotvenomnettle == True:
                $ nettlequest = True
                $ A_jadk += 1
                call sabiabase
                show sabiaemo happy1 at left
                show jadkbase at right
                show jadkemo normal at right
                "Sabia walked in and slapped the venomnettle down on the bar."
                s "Will this do?"
                $ money += 4
                show jadkemo happy1 at right
                jadk "Oh, this is plenty. Jadk thinks this much is worth... oh, about 4 Lundils. Many thanks, little lady!"
                show sabiaemo normal at left
                s "I'll take what I can get."
                show jadkemo normal at right
                jadk "You know, if you still need money, maybe you can help out around here..."
                show sabiaemo irritated2 at left
                s "Really, how so?"
                show jadkemo happy2 at right
                jadk "Jadk would get more orcs coming in here instead of bootlegging if they had something to attract them. And you, wearing the right outfit, would do wonderfully, gwahaha!"
                show sabiaemo closed4 at left
                s "What would I actually have to do to them?"
                show jadkemo closedhappy at right
                jadk "Oh, just serve drinks. Jadk wouldn't ask for anything more."
                show sabiaemo normal at left
                s "Well, I'll think about it."
                show jadkemo happy2 at right
                jadk "You do that. And you'll have to find an appropriate outfit... sorry, Jadk doesn't have anything in your size, gwaha!"
                jump silvertusk2
            else:
                s "(I should harvest some venomnettle, Jadk might pay well for it.)"
                jump silvertusk2
        "Work at the bar (50 stamina)" if nettlequest == True:
            if Sabia.armor == Barmaidclothes:
                if Sabia.stamina >= 50:
                    $ Sabia.stamina -= 50
                    $ money += 4
                    $ bartimes += 1
                    if (bargroping < 4 and orcbarbeatdown == False):
                        if bargroping >= 1:
                            "The group of rowdy orcs was back, leering at her and talking about human whores."
                        else:
                            "Sabia noticed a group of particularly rowdy orcs, ones that she recognized had spoken against her during the trial. They were leering at her, exchanging comments about how humans were fit only to be orc whores."
                            "Well, it would have been too much to hope that all the orcs accepted her, even after what she had done. It seemed like this group was intent on disrespecting her, and they were probably undermining her reputation elsewhere as well. Sabia considered her options..."
                        menu:
                            "Stay away from them":
                                pass
                            "Serve them drinks":
                                call sabiabargroping
                                jump silvertusk2
                    show orcbaseL at left
                    show orcloinclothL at left
                    show orcemo smile2L at left
                    show orcbase2 at right
                    show orcloincloth2 at right
                    show orcemo2 smile2 at right
                    show basesimple at center
                    show baroutfit2 at center
                    show sabiaemo closed2 at center
                    show sabiaemo2 blush at center
                    with dissolve
                    if bargroping >= 4:
                        $ money += 1
                        "While Sabia worked, many of the orcs ogled her body, but Sabia just smiled brightly at them. None of them dared to touch her and she pocketed 5 Lundils in the end."
                    else:
                        "Compared to her other options, Sabia didn't mind working at the bar. She carried drinks and dodged gropes for a while and pocketed 4 Lundils in the end."
                    if A_jadk >= 5 and Inventory.has_item(Silverblade) == 0 and Sabia.weapon != Silverblade:
                        hide orcbaseL at right
                        hide orcloinclothL at right
                        hide orcemo smile3L at right
                        hide orcbase2 at left
                        hide orcbase2 at left
                        hide orcbase2 at left
                        show basesimple at left
                        show baroutfit2 at left
                        show sabiaemo normal at left
                        show jadkbase at right
                        show jadkemo closedsad at right
                        hide sabiaemo2 blush at center
                        with dissolve
                        "At the end of the day, Sabia was about to leave when she noticed Jadk sitting at the bar alone. In that moment he looked very old and very tired."
                        show sabiaemo closed1 at left
                        s "Jadk... do you want some company?"
                        show jadkemo closednormal at right
                        jadk "You don't need to keep Jadk company, you know. Jadk has been on his own a long time, he'll be fine."
                        show sabiaemo happy1 at left
                        s "No, it's okay. I'm happy to spend the time here. Let me just set these down..."
                        hide baroutfit2 at left
                        show baroutfit1 at left
                        show sabiaemo closed1 at left
                        show jadkemo normalopen at right
                        jadk "Seriously? A hot young thing like you could do a hell of a lot better than an old goat like Jadk!"
                        s "..."
                        show jadkemo normal at right
                        show sabiaemo normal at left
                        s "Lundar is a young kingdom. Not just our history... our king is young, our leaders use magic to stay looking young."
                        show sabiaemo closed4 at left
                        s "I should be glad for that, otherwise I'd never have gotten promoted so far at my age. But I think we go too far, I've never really liked it."
                        s "I've known good men who got thrown away just because they were getting old. We won the war, yes, but I think we could have done even better if we hadn't ignored their expertise."
                        show sabiaemo normal at left
                        s "You remind me of them, Jadk. Maybe you don't want to fight anymore, but they should give you more respect than this."
                        show jadkemo closednormal at right
                        jadk "That's right kind of you, but you don't need to feel sad about me. Jadk will manage."
                        show sabiaemo closed1 at left
                        s "I know... I'm not going to tell you how to live your life."
                        show sabiaemo normal at left
                        s "But you didn't answer the question: do you want some company?"
                        show jadkemo happy1 at right
                        jadk "...aye, if you're offering."
                        "The two of them lingered in the bar and chatted about everything and nothing."
                        "It had been a long time since Sabia had been able to speak freely. Not just in the orc camp, as a commander she had been required to be on her best behavior at all times."
                        "Jadk didn't care how formal she was being - he just seemed happy to have someone to talk to. Sabia didn't think she was a great listener, but it didn't take much to be better than the average orc."
                        "When it grew late, Sabia didn't want to make it awkward, and so got up to leave. To her surprise, Jadk reached under the counter, then set a bundled object down on the bar."
                        show jadkemo closedsad at right
                        jadk "It's been a long time since Jadk has had fire like yours."
                        show sabiaemo sad1 at left
                        s "..."
                        show jadkemo sad at right
                        jadk "This old man is done fighting, whatever you say. But... Jadk would like to see what you do with this."
                        "Sabia unwrapped the fabric and confirmed that it contained a sword. The blade was old, but it had been well cared for and was still sharp."
                        show sabiaemo surprised2 at left
                        s "Is... this is yours? Why...?"
                        show jadkemo happy2 at right
                        jadk "It's just gathering dust here, Jadk hasn't used it in years, gwahaha!"
                        s "But... why?"
                        show jadkemo angry at right
                        jadk "Just felt like giving it to you, okay? Now get out of here, kid!"
                        show sabiaemo normal at left
                        "Sabia wasn't going to refuse such a potentially useful gift, so she thanked him and took the sword with her."
                        "For a long time she tried to figure out how he was trying to manipulate her. But she had basically no power he needed, and he didn't seem involved in the camp games in any case."
                        "Maybe it was just a gift. It had been a very long time since Sabia had received one that didn't have strings attached."
                        "It made her more uncomfortable than anything. Trying not to think about it, Sabia took the blade back to her tent as quickly as possible."
                        $ Inventory.add_item(Silverblade)
                        $ gotanysword = True
                    jump silvertusk2
                else:
                    "Sabia was too tired to work at the bar."
            else:
                jadk "Sorry, as sweet as you look, you'll need an outfit that shows you're working at the bar..."
        "Meet the orc blocking the training grounds" if raidquest == 1:
            call raidquest2
            jump silvertusk2
        "Go back":
            jump lowerorccamp
    jump lowerorccamp


label traininggrounds2:
    scene bg traininggrounds
    $ renpy.block_rollback()
    menu:
        "Visit the Red God's Arena" if (arenatime > 0 and arenatime < 20 and recruitmentopened == False):
            call RGAtraining
            jump traininggrounds2
        "Train Sabia's Squad" if (recruitmentopened == True and raidquest < 6):
            if raidquest == 5:
                call raidquest5
            elif raidquest == 0:
                call raidquest1
            else:
                "Until Sabia took care of the orcs who were blocking her training sessions, she wouldn't have any success turning her band of raiders into a real fighting force."
            jump traininggrounds2
        "Self-training (50 stamina)":
            if Sabia.stamina >= 50:
                $ Sabia.stamina -= 50
                $ selftraining += 1
                if selftraining <= 10:
                    $ Sabia.xp += 1
                if selftraining == 1:
                    "Though Sabia was in pretty good shape, she had to admit that since taking command, she wasn't at her absolute best."
                    "She started off with physical conditioning like she'd done in the old days and was surprised how much harder it was than she expected."
                    "After that she took one of the crude branches that served as practice weapons and went back to refining the basics of swordplay."
                    "The orcs gave her strange looks, but after a while they just got used to her strange efforts. This group, controlled by Lutvrog, seemed less disgustingly lustful than the others."
                    "By the time she was done, Sabia was covered in sweat, but she felt better for getting the exercise."
                elif selftraining == 5:
                    "Sabia spent a while training, adding some strength-building exercises to her workout."
                    "She couldn't lift nearly as much as the orcs, but to her surprise she noticed some of them giving her appreciative nods."
                    "They were condescending, but she'd take the respect she could get. Sabia finished her training in an unusually good mood."
                    $ Sabia.maxstamina += 10
                    $ Sabia.stamina += 20
                elif selftraining > 10:
                    "Sabia trained hard, but felt like she didn't make much progress. Perhaps she'd reached her peak performance again."
                else:
                    "Sabia trained until she was exhausted. By the end, she was covered in sweat but felt like she'd made some progress."
            else:
                "Sabia was too tired to train."
                jump traininggrounds2
            jump traininggrounds2
        "Kentark Self-training (140 stamina)" if kentarktraining > 1 and kentarkself1 == False:
            if Sabia.stamina >= 140:
                $ Sabia.stamina -= 140
                $ kentarkself1 = True
                $ kentarktraining += 10
                $ Sabia.xp += 5
                "Though there was a limit to how much she could do on her own, Sabia attempted to exercise to prepare for the Kentark training Lutvrog had told her about."
                "By the time she was finished, she was exhausted but felt like she had come a little closer to her goal."
            else:
                $ Sabia.stamina = 0
                "Sabia tried to work on the training she'd discussed with Lutvrog, but exhausted herself before she made any progress."
                jump traininggrounds2
            jump traininggrounds2
        "Kentark Self-training (250 stamina)" if kentarkself1 == True and kentarkself2 == False:
            if Sabia.stamina >= 250:
                $ Sabia.stamina -= 250
                $ kentarkself2 = True
                $ kentarktraining += 30
                $ Sabia.xp += 5
                "It was one of the most brutal exercise sessions of Sabia's life, but she managed to complete the exercise regimen that Lutvrog had described for Kentarks."
                "She felt that she was much closer to being ready for the training he had described, but doubted that she could get any further on her own."
            else:
                $ Sabia.stamina = 0
                "Sabia tried to work on the training she'd discussed with Lutvrog, but exhausted herself before she made any progress."
                jump traininggrounds2
            jump traininggrounds2
        "Purchase training":
            if gotanysword == True:
                menu:
                    "Purchase offensive training (50 Lundils, 50 stamina)" if orcattacktraining == False:
                        if Sabia.stamina < 50:
                            "Sabia was too tired to train."
                            jump traininggrounds2
                        if money >= 50:
                            $ orcattacktraining = True
                            $ Sabia.stamina -= 50
                            $ money -= 50
                            $ Sabia.add_str(1)
                            "If there was one thing Sabia had to admit orcs knew how to do well, it was destroying things. Her tutor relied less on raw power than she expected, actually teaching her a few new things."
                            "By the time their session was done, Sabia felt as though she'd gotten her money's worth. She could definitely cause more pain with a blade now."
                        else:
                            "Sabia didn't have enough money to purchase training."
                    "Purchase defensive training (50 Lundils, 50 stamina)" if orcdefensetraining == False:
                        if Sabia.stamina < 50:
                            "Sabia was too tired to train."
                            jump traininggrounds2
                        if money >= 50:
                            $ orcdefensetraining = True
                            $ Sabia.stamina -= 50
                            $ money -= 50
                            $ Sabia.add_con(1)
                            "Sabia didn't have too high of an opinion of the brute who tried to teach her how to defend herself better, but he did provide a lot of practice against larger, stronger opponents without the benefit of magic."
                            "By the time she was done, Sabia felt much more prepared to defend herself against orcs."
                        else:
                            "Sabia didn't have enough money to purchase training."
                    "Purchase stamina training (20 Lundils, 50 stamina)" if orchptraining == False:
                        if Sabia.stamina < 50:
                            "Sabia was too tired to train."
                            jump traininggrounds2
                        if money >= 20:
                            $ orchptraining = True
                            $ Sabia.stamina -= 50
                            $ money -= 20
                            $ Sabia.maxhp += 5
                            $ Sabia.maxstamina += 10
                            "The orcs cracked a few jokes about how they could help train her stamina, but when Sabia just rolled her eyes and didn't respond, they did get around to helping her."
                            "Sabia thought she had done endurance training before, but the orc version of it was brutal. It was clearly not designed for humans, much less human women, but she did her best."
                            "By the time it was over, she was sore all over. If she survived the aches the next morning, though, she was certain she'd be tougher."
                        else:
                            "Sabia didn't have enough money to purchase training."
                    "Purchase hunting training (30 Lundils, 50 stamina)" if orchuntingtraining == False:
                        if Sabia.stamina < 50:
                            "Sabia was too tired to train."
                            jump traininggrounds2
                        if hunttrainingopen:
                            $ orchuntingtraining = True
                            $ Sabia.stamina -= 50
                            $ huntingcost -= 20
                            $ Sabia.maxstamina += 10
                            orc "Ah, there you are. Normally only experienced hunters get this training, but I think you're close enough. Won't even charge you for it."
                            s "Thanks, I guess."
                            orc "But in return I expect you to bring me back a lot of game, okay?"
                            "He took her out into the forest and they went on a surprisingly rigorous journey covering all the local animals and areas."
                            "As much as Sabia hated to admit it, the orc knew what he was doing as well as any human hunter. Since she had no choice but to work for her money now, she did her best to listen to everything he said."
                            "When they finally finished Sabia was tired, but felt a little stronger and much better able to hunt in the area."
                        else:
                            "To her surprise, the orcs just shook their heads. Apparently hunting was only for experienced members of the tribe."
                    "Kulgan's training (free, 100 stamina)" if (kulganintro == True and kulgantraining == False):
                        if Sabia.stamina <= 100:
                            "Sabia was too tired to train."
                            jump traininggrounds2
                        else:
                            $ kulgantraining = True
                            $ Sabia.stamina -= 100
                            $ Sabia.maxhp += 5
                            $ Sabia.maxstamina += 10
                            $ Sabia.add_str(1)
                            $ Sabia.xp += 3
                            "Kulgan sparred with Sabia, showing her the tricks that orcs used to fight. Though she had experience fighting them, Sabia had never seen it all explained so clearly before."
                            "By the time it was done, she felt able to handle orc tricks better... and to use a few of them herself."
                    "Don't train":
                        jump traininggrounds2
                jump traininggrounds2
            else:
                s "I can't do anything but basic conditioning without a real sword..."
            jump traininggrounds1
        "Spar with orcs (50 stamina)" if Sabia.hp >= 1:
            if gotanysword == True:
                if Sabia.stamina >= 50:
                    scene bg traininggroundsF
                    $ Sabia.stamina -= 50
                    $ enemy_level = 3
                    $ enemy_maxhp = 400
                    $ enemy_hp = enemy_maxhp
                    $ enemy_type = 1
                    $ enemy_skills = [Enemyattack]
                    $ enemy_attack = 65
                    $ enemy_defense = 20
                    $ enemy_magdefense = 0
                    call randorc
                    $ player = Sabia
                    $ enemy = random_orc
                    call duel
                    if _return == "Victory":
                        if sparrespect == 3:
                            $ Inventory.add_item(Vigorreeds)
                            "Sabia grinned down at her defeated opponent. The watching orcs gave her a few nods, and to her surprise the orc she had beaten gave her a small bottle."
                            "Examining it, Sabia realized that it was bottle vigor reeds. Orcs just chewed them, but she remembered them as being useful for potions. Something to keep for future use."
                        else:
                            "Sabia grinned down at her defeated opponent. The watching orcs seemed to think it was more of a fluke than anything, but she got a few grudging nods."
                        $ sparrespect += 1
                        if sparrespect <= 3:
                            $ L_orcs += 1
                    else:
                        "Sabia winced and picked herself up carefully. If that had been a real battle, she would have been dead."
                    play music orccamp fadeout 2.0 fadein 2.0
                else:
                    "Sabia was too tired to spar."
            else:
                s "Without even a proper sword, there's no way any of them would spar with me."
            jump traininggrounds2
        "Talk to Lutvrog":
            call sabiabase
            show lutvrogbase at right
            show lutvrogaxe at right
            show lutvrogwraps at right
            show lutvrogwrists at right
            show lutvrogemo normal at right
            with dissolve
            menu traininggrounds2_lutvrog:
                "Ask to join forces" if (lutvrogtraininghelp == False and recruitmentopened == True):
                    $ lutvrogtraininghelp = True
                    s "Lutvrog... I know you don't like to get involved with politics, but I'm trying to put together strong warriors..."
                    lut "Lutvrog apologizes, but cannot join you in your raiding."
                    s "I was afraid of that. But you do help train promising warriors, right? If they were to come to you..."
                    if A_lutvrog >= 8:
                        lut "Then you wish for Lutvrog to train your warriors?"
                        s "Not as an official thing, but it's fine if they come to you for help, right?"
                        lut "Since you have a few strong allies... Lutvrog will help them grow stronger."
                        s "Great, tha-"
                        lut "But strength is not a single path. For Lutvrog's training to be worthwhile, you must choose how your warriors should better themselves."
                        s "At this stage, I think I have to go with raw combat strength. That's what I need most."
                        lut "Very well. Then choose... should Lutvrog assist their strength for assaulting, or for defending?"
                        menu:
                            "Train offense":
                                $ Sabiasquad.combat += 1
                                lut "Good. Lutvrog will train those warriors you send."
                                s "Thank you, Lutvrog!"
                            "Train defense":
                                $ Sabiasquad.defense += 1
                                lut "Good. Lutvrog will train those warriors you send."
                                s "Thank you, Lutvrog!"
                    else:
                        lut "Not an offensive offer... but no. Lutvrog seeks to better himself, not to become involved in conflicts."
                "(Approach Lutvrog)" if (tutorialraiddone == True and kentarktraining < 10):
                    call kentarkquestintro
                "Kentark Training ([kentarktraining]%%)" if kentarktraining > 1:
                    if kiaprogression < 8:
                        lut "Lutvrog is focused on an investigation right now. We can proceed with the training after Lutvrog has dealt with this matter."
                    if kentarkscenedone == True:
                        lut "You are not a Kentark yet, nor have you completed the higher levels of training. But for now, Lutvrog thinks you have done enough."
                    else:
                        if kentarktraining >= 100:
                            call kentarkquestscene
                        else:
                            "Sabia wanted to take advantage of the Kentark training that Lutvrog had discussed, but knew she wasn't completely prepared."
                "Ask about his fighting style" if lutvrogstyletalk == False:
                    $ lutvrogstyletalk = True
                    $ A_lutvrog += 1
                    show sabiaemo happy1 at left
                    s "You're not bad. No, that's not fair - you're actually really good."
                    show lutvrogemo happy at right
                    lut "Thank you."
                    show sabiaemo normal at left
                    s "Did you train somewhere? Maybe... an elven fighting style? I can't quite pin you down."
                    show lutvrogemo normal at right
                    lut "Why are you so certain Lutvrog is not using an orc fighting style?"
                    show sabiaemo eyebrow1 at left
                    s "No offense, but I've fought a lot of orcs. Some were pretty good, but it was all instinct, not polished style."
                    show sabiaemo normal at left
                    show lutvrogemo normalopen at right
                    lut "Yes, but you have fought raiders, the scattered remnants of orc kingdoms shattered before either of us were born."
                    show lutvrogemo sad at right
                    lut "Once, orcs had strong martial traditions. Those were largely lost during the initial clashes with the Kingdom of Lundar."
                    show sabiaemo closed2 at left
                    s "..."
                    show lutvrogemo normal at right
                    lut "Some documents survive, however. Lutvrog is attempting to revive the disciplines described in those records."
                    show sabiaemo normal at left
                    s "That's even more impressive, then. I wish you well."
                    lut "Do you truly?"
                    show sabiaemo happy2 at left
                    s "You're not my enemy anymore, right? But even then, I can respect an enemy warrior attempting something like that."
                    lut "..."
                "Ask about events around camp" if metnoblecaptive == False:
                    s "I know the catgirl thing has everyone's attention, but is there anything else I could be missing?"
                    lut "Lutvrog has been tasked to deal with... a problem for the camp. Visit me in the main hall and you will see."
                    s "We can't talk about it here?"
                    lut "It would be easier for you to simply see."
                "Ask about Neve":
                    show lutvrogemo happy at right
                    lut "She is unquestionably one of the most skilled warriors in the camp."
                    show sabiaemo normalopen at left
                    s "Better than you?"
                    show sabiaemo normal at left
                    show lutvrogemo suspicious at right
                    lut "We have sparred in the past, and Lutvrog emerged victorious. However, Lutvrog has reason to believe she restricted herself from using her full resources."
                    show lutvrogemo normal at right
                    lut "With her armor active, Lutvrog doubts if any in this camp could face her one-on-one."
                    show sabiaemo surprised2 at left
                    s "Active?"
                    show sabiaemo normal at left
                    show lutvrogemo normalopen at right
                    lut "That secret is not mine to tell, even if Lutvrog knew it in full."
                    show lutvrogemo normal at right
                "Ask about Warchief Groknak" if captainsintro:
                    show lutvrogemo normalopen at right
                    lut "The Warchief is a leader of the traditional style, obtaining his position by prowess in combat. He is an extremely experienced warrior and was unmatched in his prime."
                    lut "This may have been a good method of election during times of war, but some wonder if this still benefits the tribe."
                    show lutvrogemo normal at right
                    lut "Lutvrog does not have opinions on such matters."
                "Ask about Tekrok" if captainsintro:
                    lut "His savagery masks a surprising amount of skill. Though he may rely on his strength, he relies upon it as a useful tool."
                "Ask about Rokgrid" if captainsintro:
                    lut "He chose to abandon traditional orc fighting styles for a mix of human and elven technique. Most warriors have only middling opinions of his skill, but Lutvrog believes they underestimate his strength."
                "Ask about Dajrab" if captainsintro:
                    lut "He has a cautious, deadly style of fighting. It seems he has learned well from all his scars, because Lutvrog has never seen anyone injure him in combat."
                "Ask about catgirls" if catgirlraidquest:
                    lut "Though physically weak, they are both fast and agile. One must be careful not to let them get within one's range, for even a small blade can open a stomach or ruin a leg."
                "Would you attend my feast?" if (orcfestivalquest == True and HGNlutvrog == False):
                    if lutvrogsex:
                        if A_lutvrog >= 5:
                            $ orcfestivalscore += 3
                            $ HGNlutvrog = True
                            lut "Lutvrog hopes you realize that this is no small thing to ask. Lutvrog's presence will be noted and respected by many orcs."
                            s "I'm aware. But it will also be noted by me... I'd like you to be there, Lutvrog."
                            lut "...Lutvrog will attend. Thank you, Sabia."
                            s "No, thank you!"
                        else:
                            lut "A tempting offer, to be sure... Lutvrog must think on it more."
                    else:
                        lut "Lutvrog must decline. It is no small thing to officially be present at someone's feast."
                "Ask to spar" if Sabia.hp >= 1:
                    if lutvrogfight == True:
                        show lutvrogemo happy at right
                        if lutvrogsex == True:
                            lut "As much as Lutvrog enjoyed our... match, Lutvrog thinks we have sparred enough for now. Lutvrog is sure that you have much to do."
                        else:
                            lut "Once is enough, for now. Lutvrog is sure that you have much to do."
                        jump traininggrounds2
                    if (sparrespect + A_lutvrog) >= 5:
                        lut "Your chance of victory is slim, but Lutvrog respects the work he has seen from you. If you want, Lutvrog will fight you without his personal weapon or armor, using only the basics."
                        show sabiaemo angry1 at left
                        s "Are you pitying me?"
                        show lutvrogemo normal at right
                        show sabiaemo normal at left
                        lut "Lutvrog merely wants to see what you are capable of. Do we have an agreement, or not?"
                        menu:
                            "Fight Lutvrog normally":
                                lut "Well, the offer remains open."
                            "Fight Lutvrog with handicap":
                                lut "Let Lutvrog exchange his equipment for the basics, then we shall see what you can do."
                                scene bg traininggroundsF
                                $ enemy_type = 1
                                $ enemy_skills = [Enemyattack]
                                $ enemy_level = 7
                                $ enemy_hp = 700
                                $ enemy_maxhp = 700
                                $ enemy_attack = 65
                                $ enemy_defense = 10
                                $ enemy_magdefense = 10
                                $ Lutvrog.equip(Stick)
                                $ player = Sabia
                                $ enemy = Lutvrog
                                call duel
                                if _return == "Victory":
                                    $ lutvrogfight = True
                                    $ lutvrogsex = True
                                    $ sparrespect += 3
                                    $ L_orcs += 3
                                    $ A_lutvrog += 3
                                    play music forest fadeout 2.0 fadein 2.0
                                    call lutvrogprescene
                                    if lutvrogsex:
                                        "Sabia strode from the training ground building with an extra spring in her step. She was sore for multiple reasons, but she felt fantastic."
                                    else:
                                        "Sabia strode from the training ground building with an extra spring in her step. Winning a fight like that was a strong step toward earning the respect she needed."
                                    jump lowerorccamp
                                else:
                                    "Sabia hit the ground hard, but Lutvrog helped her up. At least there was no dishonor in losing to him."
                                play music orccamp fadeout 2.0 fadein 2.0
                                jump traininggrounds2
                    else:
                        lut "Given the present conditions, your chance of victory is slim, but Lutvrog respects your desire to challenge yourself."
                    scene bg traininggroundsF
                    $ enemy_type = 1
                    $ enemy_skills = [Enemyattack]
                    $ enemy_level = 12
                    $ enemy_hp = 800
                    $ enemy_maxhp = 800
                    $ enemy_attack = 120
                    $ enemy_defense = 120
                    $ enemy_magdefense = 50
                    $ Lutvrog.equip(Lutvrogsaxe)
                    $ player = Sabia
                    $ enemy = Lutvrog
                    call duel
                    if _return == "Victory":
                        $ lutvrogsex = True
                        $ sparrespect += 3
                        $ L_orcs += 3
                        $ A_lutvrog += 3
                        play music orccamp fadeout 2.0 fadein 2.0
                        call lutvrogprescene
                        if lutvrogsex:
                            "Sabia strode from the training ground building with an extra spring in her step. She was sore for multiple reasons, but she felt fantastic."
                        else:
                            "Sabia strode from the training ground building with an extra spring in her step. Winning a fight like that was a strong step toward earning the respect she needed."
                        play music orccamp fadeout 2.0 fadein 2.0
                        jump lowerorccamp
                    else:
                        "Sabia hit the ground hard, but Lutvrog helped her up. At least there was no dishonor in losing to him."
                    play music orccamp fadeout 2.0 fadein 2.0
                    jump traininggrounds2
                "Any thoughts about the Red God's Arena?" if (arenatime > 0 and recruitmentopened == False):
                    lut "Heh. Lutvrog will see you there."
                "Go back":
                    jump traininggrounds2
            jump traininggrounds2_lutvrog
        "Ylva and Lutvrog" if (RGAylvapresent == True and ylva1lutvrogtalk == False):
            call ylva1lutvrog
            jump traininggrounds2
        "Talk to Kulgan" if kulganalive == True and kulganrecruited == False:
            show orcbase at right
            show orcloincloth at right
            show orcpiercing at right
            show orcshoulder at right
            show orcstrap at right
            show orcwrap at right
            show orcbeard1 at right
            show orcemo smile1 at right
            call sabiabase
            if kulganintro == False:
                $ kulganintro = True
                kulgan "You saved Kulgan's life!"
                show sabiaemo closed1 at left
                s "No need to get too excited, all I had to do was tell the truth."
                kulgan "No! This is a debt Kulgan must repay!"
                s "(Well, that sounds useful to me. Might as well take advantage.)"
                kulgan "In these training grounds, Kulgan will provide special training, free of charge! And ask Kulgan anything, Kulgan will try to answer!"
            menu traininggrounds2_kulgan:
                "Who are you?":
                    kulgan "Kulgan is only warrior. Fights for Warchief Groknak, tries to become stronger."
                "So, were you actually involved?":
                    kulgan "What?"
                    s "The raid. Did you actually do whatever they said you did?"
                    kulgan "No! Kulgan is innocent!"
                "What do you know about the catgirl raid?" if (catgirlraidquest == True and catgirlraidkulgan == False):
                    $ catgirlraidkulgan = True
                    $ catgirlraidinvestigation += 1
                    kulgan "Kulgan does not know much, but... Kulgan knows that orc party did not scout ahead as they should."
                    show sabiaemo surprised1 at left
                    s "What was that?"
                    kulgan "For important shipments, orc warriors should scout ahead. Prevent ambushes. But these days, many only look for humans. Think catgirls are not a threat."
                    show sabiaemo normal at left
                    s "Interesting... so you know for sure they didn't scout during the raid?"
                    kulgan "No, Kulgan is not sure. But Kulgan knows that they did not scout on past steel shipments. Maybe this is why catgirls targeted them."
                    show sabiaemo happy1 at left
                    s "Very useful. Thank you, Kulgan."
                "Would you attend my feast?" if (orcfestivalquest == True and HGNkulgan == False):
                    $ orcfestivalscore += 2
                    $ HGNkulgan = True
                    kulgan "Kulgan would be honored to join you."
                    s "Good! I'll count on seeing you during the Horned God's Night!"
                    $ Inventory.add_item(HGNWine)
                    kulgan "Kulgan can do more than that. Kulgan was saving wine for his own feast, before the trial. It would be well served joining your feast."
                    s "Ah, thank you!"
                "Any help with the Red God's Arena?" if (arenatime > 0 and recruitmentopened == False):
                    kulgan "Sorry, but Kulgan cannot help you with something so difficult."
                "Can you join my raiding group?" if recruitmentopened:
                    $ kulganrecruited = True
                    $ Mainarmy.add_troop(Kulganorcs)
                    kulgan "Kulgan can do better than that! Kulgan has a few allies, a small raiding group. We may not be strong, but we will fight for you!"
                    show sabiaemo happy1 at left
                    s "Ah, really? Thanks, Kulgan!"
                    kulgan "Kulgan will join the others. Just tell us when we are needed."
                    jump traininggrounds2
                "Nothing":
                    jump traininggrounds2
            jump traininggrounds2_kulgan
        "Go back":
            jump lowerorccamp
    jump lowerorccamp


label hellhoundkennels2:
    scene bg kennels
    $ renpy.block_rollback()
    if recruitmentopened:
        if maply_hellhound_quest == 0:
            $ maply_hellhound_quest = 1
            call sabiabase
            "As Sabia approached the kennels, she could hear the roar of an angry orc."
            "The yelp of what she assumed was a disobedient hound followed."
            $ GenericOrc1.extras = ["Loincloth", "Shoulder", "Wrap", "Strap"]
            $ GenericOrc1.face = "angry"
            show GenericOrc1 at right with moveinright
            orc "Ugh. What do you want? Like job not tough enough as it is? Don't want to argue with nosy humans today."
            s "..."
            show sabiaemo annoyed1 at left
            s "Nosy?"
            s "I was just walking past."
            orc "Keep walking then! Kennels {i}closed{i}!"
            hide GenericOrc1 with moveoutright
            show sabiaemo annoyed2 at left
            s "It's probably only so hard because he's not good at the job. Wouldn't surprise me."
            show sabiaemo closed2 at left
            s "(I'd like to know what's going on, at least. More information never hurt. I might have to ask someone a bit more stealthy than I to have a look into it though...)"
        elif maply_hellhound_quest == 2:
            $ maply_hellhound_quest += 1
            if maplybefriended == True:
                jump maply_hellhound_quest2
            else:
                jump maply_hellhound_quest2_unf

        elif maply_hellhound_quest == 6:
            $ maply_hellhound_quest += 1
            jump maply_hellhound_quest5
        elif maply_hellhound_quest == 11:
            "Though Maply had helped calm the hellhounds, Sabia didn't think there was much more she could do with them for now."
        else:
            "The kennels seemed to have been mostly shut down now that the Red God's Arena was complete, so Sabia stayed away for the time being."
    elif arenatime >= 9:
        "Though the kennels were still filled with frenzied sounds, Sabia decided it was best to focus on the Red God's Arena for now. She had enough to worry about."
    else:
        "Strangely, the hellhound kennels were locked up tight. It sounded as though there were orcs inside, possibly arguing about something, but that was all Sabia was able to determine. After waiting for a while, she decided not to pry."
    jump lowerorccamp


label relieftents2:
    scene bg relieftents
    $ renpy.block_rollback()
    if relieftentreject == False:
        $ relieftentreject = True
        call sabiabase
        if sexworktimes >= 1:
            "Sabia walked between the familiar tents with a frown on her face. She was a true member of the tribe now, but that wouldn't erase what she'd done here."
            "But after a moment of thought, she decided that she didn't regret it. The orcs had been disgusting, but she had learned an entirely new way to manipulate people. She knew sex was a powerful weapon even in Lundar, so with the orcs she could use it to manipulate them even more effectively."
        else:
            "Sabia walked between the familiar tents with a thoughtful expression. Though working in them might have sped up her ascent, things had worked fine without them."
            "Still, the place they held in camp... Sabia resolved to keep in mind that sex could be a powerful weapon. One that she would deploy sparingly, but still a useful part of her arsenal."
        show orcbase2 at right
        show orcloincloth2 at right
        show orcaxe2 at right
        show orchelmet2 at right
        show orcaxe2 at right
        show orcpiercing2 at right
        show orcwrists2 at right
        show orcemo2 normalopen at right
        with dissolve
        if sexworktimes >= 1:
            orc "You back for more? Now that you're a really member of the tribe, there are a lot more warriors that'd want those lips around their cock!"
            show sabiaemo closed1 at left
            s "...no, I don't believe I'll be doing that."
            show orcemo2 sad2 at right
            orc "Huh? But you loved slobbering on orc cock!"
            show sabiaemo eyebrow1 at left
            s "I loved getting paid. Do you think I would have wasted time with any of you if it wasn't the fastest way to reach my goals?"
            orc "But..."
            s "Are you that obsessed with your own cocks, or are you just that dense? You can't tell when a woman is faking it?"
            show sabiaemo happy2 at left
            s "Well, I guess I shouldn't complain about you all being easy. Working here helped me get back on my feet, so it served its purpose."
            orc "Why'd you come here? Just to insult me?"
        else:
            orc "You here to work in the tents?"
            s "No. If it wasn't necessary before, it certainly isn't necessary now."
            orc "But... you could earn support fr-"
            show sabiaemo happy2 at left
            s "Right, because after everything I've done so far, sucking a few cocks is going to decide politics."
            orc "If you're not here to work... why'd you come here? Just to insult me?"
        show sabiaemo annoyed1 at left
        s "No, I'm here to ask what the hell you're doing, wasting the tents like this."
        orc "Huh?"
        show sabiaemo closed2 at left
        s "Both the camp's morale and economic situation depend on the relief tents, but your abysmal management has completely wasted their potential."
        orc "H-hey! Me run the tents lik-"
        if sexworktimes >= 1:
            show sabiaemo eyebrow1 at left
            s "Oh, please. I worked here, you can't pull lies like that with me. The orcs pay what they want inside the tents - I guarantee you're getting ripped off."
        else:
            s "Like an idiot. This is basically a business, and it's obvious you have no sense for business."
        orc "What, you think you could do better?"
        show sabiaemo annoyed2 at left
        s "Of course I could!"
        show sabiaemo closed1 at left
        s "(Actually, there are at least two ways I could take this, both better than this idiot's fumbling. But they're different tactics...)"
        menu:
            "Suggest enslaving more women":
                $ slavery += 1
                s "Right now, you have a half-assed system where the women are half-captives, half-workers. That's just asking them to fleece you of the excess profits."
                s "Stop being cowards and just go all the way. Get control of everyone here and make this place run properly."
            "Suggest hiring better women":
                $ freedom += 1
                s "Right now, you have a half-assed system where the women are half-captives, half-workers. That's just asking them to put in the minimum possible effort."
                s "Stop being idiots and make it more like a real job. Improve their working conditions and give them a reason to make you money."
        show sabiaemo closed4 at left
        if sexworktimes >= 1:
            show sabiaemo eyebrow1 at left
            s "And the most ridiculous thing is that you have no quality differentiation! I know for a fact that orcs pay based on what they think the experience is worth!"
        else:
            s "And the most ridiculous thing is that you have no quality differentiation! You're a bunch of savages, but even you care about more than fucking a hole!"
        s "Some of the whores here are only worth a few Lundils, and others are worth far more. But you're not getting any money from that fact because you don't take advantage of those who actually know what they're doing."
        s "You should have basic tents for the cheap orcs, more expensive tents for the good whores, maybe a few high class ones to milk warriors with too much money."
        show sabiaemo annoyed2 at left
        s "Of course, all the tents should be better than this pigsty. Nobody wants to work {i}or{/i} fuck in a place like this."
        orc "Hmph. You think it's so easy?"
        s "...why are you in charge of the tents, anyway?"
        orc "It's my job. No one else want organize, just use sluts."
        show sabiaemo normal at left
        s "Heh, is that so?"
        scene bg relieftents
    menu:
        "Alter the relief tents to improve troop morale" if recruitmentopened == True and relieftentmorale == False:
            $ relieftentmorale = True
            "It occurred to Sabia that she could probably gain a lot of control among her troops by giving them special access to the women of the relief tents."
            if catgirlstatus == "enslaved":
                "She had enslaved most of the catgirls and sent them to the tents, which had been a popular move. But she would be free to give her own warriors special access to them, perhaps a few other privileges."
                "Or, she supposed, she could allow some of the catgirls some relief in return for serving her. It wouldn't be popular with the orcs, but they might be more loyal to her."
                menu:
                    "Keep everything the same":
                        "Since things were working well enough so far, Sabia decided not to meddle. Later on she could take over the tents completely and change her mind if necessary."
                    "Give recruited orcs special privileges":
                        $ slavery += 1
                        $ Sabiasquad.combat += 1
                        $ Catgirlslaves.combat -= 1
                        "Since she'd already enslaved the catgirls, Sabia decided it wasn't worth trying to get their loyalty back. Better to use them as a resource to improve the morale of her orcs."
                        "It worked more smoothly than she expected, confirming her belief that this was a valuable method to manipulate morale. Later on she could take over the tents completely and change her mind if necessary."
                    "Give the catgirls more freedom":
                        $ Sabiasquad.combat -= 1
                        $ Catgirlslaves.combat += 1
                        "Deciding that she had enough orcs, Sabia gave orders to give more freedoms to catgirls who would work with her. They would likely be the more useful resource in the end."
                        "It worked more smoothly than she expected, confirming her belief that this was a valuable method to manipulate morale. Later on she could take over the tents completely and change her mind if necessary."
            elif catgirlstatus == "free":
                "Unfortunately, Sabia didn't have control of the main group of women, and she'd let the catgirls go free, so she didn't have any leverage."
                "Perhaps after more raiding, though... Sabia reminded herself to do more with it in the future."
            elif catgirlstatus == "recruited":
                "Unfortunately, Sabia didn't have control of the main group of women, and the catgirls were working with the orcs now, so she didn't have any leverage."
                "Perhaps after more raiding, though... Sabia reminded herself to do more with it in the future."
            else:
                "Since the catgirls were working in the tents to pay off their debts, they provided her with a unique option. Since the tents weren't managed particularly well, she could easily take advantage to give her own warriors special privileges."
                "Alternatively, she could offer the catgirls an alternate way of paying off their debt by giving them a share of what they raided. That might motivate the whole group a lot more."
                menu:
                    "Keep everything the same":
                        "Since things were working well enough so far, Sabia decided not to meddle. Later on she could take over the tents completely and change her mind if necessary."
                    "Give recruited orcs special privileges":
                        $ Sabiasquad.combat += 1
                        $ Catgirlslaves.combat -= 1
                        "The catgirls might have fit in a bit better than she'd expected, but ultimately, they were outsiders and she had an orc army. Sabia decided to keep focusing on her orcs and use the catgirls as a resource."
                        "It worked more smoothly than she expected, confirming her belief that this was a valuable method to manipulate morale. Later on she could take over the tents completely and change her mind if necessary."
                    "Give the catgirls more freedom":
                        $ freedom += 1
                        $ Sabiasquad.combat -= 1
                        $ Catgirlslaves.combat += 1
                        "Deciding that she had enough orcs, Sabia gave orders to give more freedoms to catgirls who would work with her. They would likely be the more useful resource in the end."
                        "It worked more smoothly than she expected, confirming her belief that this was a valuable method to manipulate morale. Later on she could take over the tents completely and change her mind if necessary."
            jump relieftents2
        "Check on women":
            if catgirlstatus == "working":
                "Catgirls were working in the tents, more eager than Sabia had expected."
                menu:
                    "Watch":
                        call catgirls1working
                        play music orccamp fadeout 2.0 fadein 2.0
                        jump relieftents2
                    "Return":
                        jump relieftents2
            else:
                "There were only a small number of women in the relief tents and the orcs seemed frustrated."
            jump relieftents2
        "Check on prisoners":
            if catgirlstatus == "recruited":
                "The leader of the catgirls that Tekrok had made an example of was still being roughly used by the orcs."
                menu:
                    "Watch":
                        call catgirls1punishment
                        play music orccamp fadeout 2.0 fadein 2.0
                        jump relieftents2
                    "Return":
                        jump relieftents2
            elif catgirlstatus == "enslaved":
                "The orcs were eagerly using all the catgirls Sabia had enslaved."
                menu:
                    "Watch":
                        call catgirls1enslaved
                        play music orccamp fadeout 2.0 fadein 2.0
                        jump relieftents2
                    "Return":
                        jump relieftents2
            else:
                "There were currently no prisoners in the relief tents."
            jump relieftents2
        "Go back":
            jump lowerorccamp
    jump lowerorccamp


label orcoutskirts2:
    scene bg countryside
    $ renpy.block_rollback()
    $ temp1 = huntingcost * 2
    if maply_hellhound_quest == 9:
        $ maply_hellhound_quest += 1
        jump maply_hellhound_quest7
    menu:
        "Leave camp":
            s "(No, it wouldn't be safe to wander far. Ridiculous as it sounds, I'm safer in the orc camp than in human lands.)"
            jump orcoutskirts2
        "Follow Ylva out of camp" if recruitmentopened and kiaprogression < 1:
            call KLkiaintro1
            jump orcoutskirts2
        "Investigate attack sites for Rokgrid" if (rokgridfakeraidquest == True and rokgridraidkia == False and kiaprogression >= 5 and rokgridraiddone == False):
            call rokgridraidkia
            jump orcoutskirts2
        "Manage troops" if recruitmentopened:
            menu:
                "Test formations":
                    "Sabia had her soldiers run through a few drills, not so much to improve them as to test how far they'd come..."
                    $ reset_armies()
                    $ deployarmies(["Drills",10])
                    call deployment
                    "Drill complete, Sabia ordered her soldiers back to work. So that was what she had to work with."
                    jump orcoutskirts2
                "Organize Sabia's squad" if righthandpicked == False:
                    $ righthandpicked = True
                    "So far, Sabia had been organizing her warriors herself, but she realized that it would quickly become tedious. She wanted to lead her forces, not micro-manage. So she needed a leader who would manage her group and relay her orders."
                    "She had been afraid that the orcs would have some massive ritual or competition to decide which could lead, but thankfully they quickly put forward three candidates. Sabia didn't know them well, but they seemed to be orcs that the others respected and that could do their job."
                    "Not equally well, though. One of the potential leaders was a big warrior who spent all his time on the training grounds. The second was actually a smith, who promised to make their group work on forging better armor. And finally, there was a lean veteran of past raids."
                    "All three would serve well enough and follow her orders, Sabia thought, but they would develop her forces in a different direction..."
                    menu:
                        "Promote the warrior":
                            $ Sabiasquad.combat += 1
                            "Sabia picked the warrior and the other two candidates backed down. Seeing her warriors going off to train, Sabia felt she'd made the right decision."
                        "Promote the smith":
                            $ Sabiasquad.defense += 1
                            "Sabia picked the smith and the other two candidates backed down. Seeing her warriors going off to develop armor for themselves, Sabia felt she'd made the right decision."
                        "Promote the raider":
                            $ Sabiasquad.raid += 1
                            "Sabia picked the raider and the other two candidates backed down. Seeing her warriors begin going over raiding plans, Sabia felt she'd made the right decision."
                    jump orcoutskirts2
                "Nothing":
                    jump orcoutskirts2
        "Neve and Maply" if (recruitmentopened == True and maplynevescene == True and maplynevesex == False and nevekiaprogression == 3):
            $ maplynevesex = True
            $ nevekiaprogression = 4
            call nevemaplychat1
            jump orcoutskirts2
        "Talk to Neve":
            show backdrop
            if (maplynevescene == False and maplysexneve == True and maplytortured == False and catgirlraidquest == False):
                $ maplynevescene = True
                show neve1 at left
                show neveemo normal at left
                show maply 1 at right
                show maplyemo eyebrows at right
                show maplyblush at right
                with dissolve
                maply "..."
                n "..."
                maply "..."
                n "Do you need something?"
                show maplyemo surprise1 at right
                pause 1
                hide maply 1
                hide maplyemo surprise1
                hide maplyblush
                with moveoutright
                pause 1
                show neveemo happy3 at left
                n "Heh. Cute."
                jump orcoutskirts2
            call sabiabase
            show neve1 at right
            show neveemo normal at right
            n "Sabia."
            menu orcoutskirts2_neve:
                "Did you fight in the war?" if nevewarconvo == False:
                    $ nevewarconvo = True
                    $ A_neve += 1
                    show neveemo irritated1 at right
                    n "Are you serious? How old do you think I am?"
                    s "You don't look much older than me. I'm not saying I think you fought in the old elven kingdoms, but you still could have fought."
                    show neveemo normal at right
                    n "You didn't really see a lot of of races working together until the very end."
                    show neveemo closed1 at right
                    n "Hell, the elves couldn't even suppress their internal conflicts. That's one thing you humans did fairly well, and part of the reason you won."
                    show neveemo normal at right
                    s "You look experienced in combat, though... have you worked as a mercenary?"
                    n "I did work in the last elven king's court, but that feels like a long time ago. I don't want to talk about it."
                    show sabiaemo irritated1 at left
                    s "..."
                    show neveemo happy1 at right
                    n "If you're wondering if I'm one of the guerrillas fighting against Lundar, you can relax. I'm staying away from politics of all kinds."
                    show neveemo normal at right
                    show sabiaemo normal at left
                    n "What about you? You were no minor commander, as I understand it."
                    s "I fought on the front lines in the minotaur suppression conflict. Made my way through the ranks slowly."
                    s "But then one day my squad got ambushed, I and a few others barely fought our way to safety. After that, my family decided it wasn't safe to have me in so much danger."
                    n "So they got you promoted, huh?"
                    show sabiaemo angry1 at left
                    s "Hey, it's not like I didn't deserve it!"
                    show sabiaemo normal at left
                    s "But... my mother did spin surviving the ambush into a victory, and that was enough to get me into a position of command."
                    s "So I stayed away from the front lines during the final battle with the horde. I think I did pretty well, and I deserved every promotion I got during those battles."
                    show neveemo sad at right
                    n "But you haven't used your own blade so much. You sound almost wistful."
                    show sabiaemo sad1 at left
                    s "No, I wouldn't... well, maybe a little."
                    show sabiaemo normal at left
                    show neveemo normal at right
                    s "My mother always said our family was meant to go into politics. She considered wielding a sword to be beneath us."
                    s "When I turned out to be talented there and earned our family influence in the army, she accepted it, but I don't think she's entirely happy about it."
                    n "..."
                    s "..."
                    show sabiaemo pout2 at left
                    s "You're good at getting people talking, aren't you?"
                    show neveemo smirk1 at right
                    n "You could say that."
                    show sabiaemo pout3 at left
                    s "Hmph. Most of that was public knowledge anyway."
                    jump orcoutskirts2_neve
                "Where are you from?" if nevehistoryconvo == False:
                    $ nevehistoryconvo = True
                    $ A_neve += 1
                    show neveemo closed1 at right
                    n "Oh, just a wrecked little forest kingdom east of the Eskra River. Not many there even remember the traditions we used to have, as we fell generations ago."
                    show neveemo normal at right
                    n "I wasn't anyone special in the dark elf kingdom."
                    show neveemo happy1 at right
                    n "But the difference between elf ethnicities matters much less now, so I left to travel the world."
                    show sabiaemo irritated2 at left
                    s "You weren't worried about getting captured by slavers? I mean, when you were younger."
                    show neveemo normal at right
                    n "Not really. By the time I left I had enough experience to take care of myself."
                    show neveemo irritated1 at right
                    n "More importantly, human slavers tend to come down to our old kingdoms, they don't look for random travelers."
                    show sabiaemo closed2 at left
                    s "..."
                    show neveemo closed2 at right
                    n "You know, I almost admire your ability to just ask about how your people enslaved mine so casually."
                    s "..."
                    show neveemo smirk1 at right
                    n "Heh. You're fun."
                    jump orcoutskirts2_neve
                "Why are you here in the orc camp?":
                    show neveemo closed3 at right
                    n "Let's just say it's more interesting than the alternatives."
                    jump orcoutskirts2_neve
                "What are those faces on your armor?" if nevefacesconvo == False:
                    if A_neve >= 3:
                        $ nevefacesconvo = True
                        n "..."
                        show neveemo closed1 at right
                        n "They're one of the last divine artifacts from my home."
                        show sabiaemo surprised1 at left
                        s "Divine artifacts?"
                        show neveemo closed4 at right
                        show sabiaemo normal at left
                        n "You don't think the Order of Relona has a monopoly on gods, do you? No, we dark elves had our own gods."
                        show neveemo sad at right
                        n "Each one of these is a face of one of our gods. They may be nearly forgotten, but they still exist. And when I call upon them... well, let's just say this armor is tougher than it looks."
                        show sabiaemo closed2 at left
                        s "Hmm, so it wouldn't work for anyone else?"
                        show neveemo normal at right
                        n "No, only for someone who still believes in the old elven gods. And there aren't many of us left these days."
                    else:
                        show neveemo closed1 at right
                        n "Just faces. Don't worry about them."
                        show sabiaemo irritated2 at left
                        s "..."
                    jump orcoutskirts2_neve
                "Are orcs really that good at sex?" if (dajraberrand >= 2 and nevesexconvo == False):
                    $ nevesexconvo = True
                    $ A_neve += 3
                    show neveemo smirk1 at right
                    n "Heh, what are you implying?"
                    show sabiaemo closed3 at left
                    s "Well, you were with them..."
                    n "Meaning you think the only reason I could want to be with an orc is if they're supernaturally good at fucking?"
                    show sabiaemo irritated1 at left
                    s "..."
                    show neveemo closed2 at right
                    n "Heh, you're so easy to tease."
                    show neveemo happy3 at right
                    n "I really want to mock you with tales of their magical sexual prowess. A lot of them certainly have an inflated opinion of it. But really, they're only people. Orcs just happen to be the ones I have on hand right now."
                    show neveemo happy2 at right
                    n "They do have nice cocks, though - pretty thick compared to humans or elves. You the type who can come with just a bunch of thrusting?"
                    show sabiaemo surprised1 at left
                    show sabiaemo2 blush at left
                    s "I, uh..."
                    show neveemo closed2 at right
                    n "Fine, don't answer if you don't want. Well, they're good for rough hammering sex. Good luck finding one who will give your clit too much attention, though."
                    show sabiaemo closed2 at left
                    s "I see..."
                    show neveemo smirk1 at right
                    n "But I think you're learning plenty about all that here, aren't you?"
                    show sabiaemo irritated2 at left
                    hide sabiaemo2 blush
                    s "I'd rather not talk about it."
                    jump orcoutskirts2_neve
                "What's your opinion on catgirls?" if (catgirlraidquest == True and catgirlraidneve == False):
                    $ catgirlraidneve = True
                    $ A_neve +=1
                    show neveemo happy3 at right
                    n "Oh, they're adorable."
                    show sabiaemo closed2 at left
                    s "Not what I meant. Didn't elves use to forbid catgirl caravans from entering their kingdoms?"
                    n "That's in the past. Me personally, I'm more interested in their breeding."
                    show sabiaemo surprised2 at left
                    s "Breeding?"
                    show sabiaemo normal at left
                    show neveemo smirk1 at right
                    n "Didn't you know? There aren't any male catgi... catboys. Legends say they existed once, but there are definitely none today."
                    n "Instead, catgirls can mate with anyone and produce catgirl children. Allegedly they're eager about it too. I'm quite curious how that works."
                    show sabiaemo irritated1 at left
                    s "Wouldn't you just end up with a bunch of diseases and no money?"
                    show neveemo happy3 at right
                    n "Haha, Lundar makes people so predictable."
                    jump orcoutskirts2_neve
                "What do you know about the catgirl theft?" if (catgirlraidquest == True and catgirlraidneve2 == False):
                    $ catgirlraidneve2 = True
                    n "I wasn't nearby at the time, so I can't say I have any special information."
                    s "Yes, but I'm sure I know even less. I know they're thieves, but I don't get this one."
                    if A_neve >= 3:
                        $ catgirlraidinvestigation += 2
                        show neveemo happy2 at right
                        n "Oh, that part is easy. Technically an orc secret, but simple."
                        show neveemo normal at right
                        n "The reason orcs have decent weapons despite not having much smithing is that they use bone steel. Makes a better edge, cuts through armor."
                        s "Bone steel?"
                        n "It's an alloy made with bone dust. Allegedly it contains the spirits of past warriors and they help fight."
                        show neveemo smirk1 at right
                        n "Seems like it's just good quality steel to me."
                        show neveemo normal at right
                        s "Hmm... so that's why the catgirls went after it. That makes sense, good steel sells for a lot and would be easy to fence."
                        n "Plus, that's why the orcs are so upset."
                        show sabiaemo closed2 at left
                        s "I don't follow."
                        n "It's dishonorable to steal something that contains the spirits of great warriors."
                        show sabiaemo pout3 at left
                        s "Oh, right."
                    else:
                        show neveemo closed1 at right
                        n "Well, that's thieving catgirls for you."
                        show sabiaemo annoyed1 at left
                        s "..."
                    jump orcoutskirts2_neve
                "Would you help me interrogate a catgirl?" if (maplysexlook  == True and maplysexdone == False):
                    $ maplysexneve = True
                    $ maplysexdone = True
                    $ catgirlraidinvestigation += 2
                    $ catgirlraidperformance += 5
                    $ A_maply += 1
                    n "Getting involved in the raid politics, I take it? Well, that's none of my business, but I'll pass. I'm not interested in torture, anyway."
                    show sabiaemo closed2 at left
                    show sabiaemo2 blush at left
                    s "I... didn't mean torture. There are, uh, other ways..."
                    show neveemo smirk1 at right
                    n "I'm confused about what you could possibly mean by that. Could you be more specific?"
                    show sabiaemo2 blush angry1 at left
                    hide sabiaemo2 blush
                    show sabiaemo2 blush at left
                    s "You know what I mean!"
                    show neveemo smirk1 at right
                    n "Alright, I'll be merciful this time, if only because I'm really interested in getting to play with a catgirl."
                    show sabiaemo normal
                    hide sabiaemo2 blush
                    n "Besides, better to get information from the poor thing via a gentle method instead of using orcs, or whatever Lundar would usually do."
                    s "Alright, we need any information we can get, so here's what I was thinking..."
                    scene bg black with dissolve
                    pause 1
                    scene bg sabiatent
                    show neve1 at left
                    show neveemo happy1 at left
                    show maply 3n at right
                    show maplyemo surprise1 at right
                    with dissolve
                    maply "Oh my! Who are you?"
                    show neveemo happy2 at left
                    n "I'm Neve. And you are?"
                    show maplyemo happy at right
                    maply "Hi, I'm Maply!"
                    show neveemo happy3 at left
                    n "Pleased to meet you, Maply. We're going to get to know each other very, very well..."
                    call nevemaply1
                    play music orccamp fadeout 2.0 fadein 2.0
                    $ maplystripped = True
                    scene bg black with dissolve
                    n "She was pretty willing to talk, once she got relaxed. Let me tell you everything she said..."
                    jump sabiahq2
                "Ask about the dildo she used on Maply" if (maplysexneve == True and maplytortured == False and nevedildohint == False):
                    $ nevedildohint = True
                    s "What exactly was that... thing you used with Maply?"
                    show neveemo smirk1 at right
                    n "Well, you see, a dildo is a-"
                    show sabiaemo angry1 at left
                    show sabiaemo2 blush at left
                    s "I know what a dildo is!"
                    show sabiaemo closed2 at left
                    s "But that thing was not normal. I want to know what it was - and don't make some crack about me wanting one!"
                    show neveemo normal at right
                    n "Alright, I'll play nice. I'm not surprised that you haven't seen one before, considering how much Lundar restricts such things."
                    n "You know the tentacle monsters from the mountains to the south, right? Well, if you remove a tentacle and enchant it with the right magic, it makes one hell of a dildo. Stays warm, hard but not too hard..."
                    show sabiaemo normal at left
                    hide sabiaemo2 blush
                    s "Something like that is possible?"
                    n "Not with human magic, but it's definitely possible."
                    show neveemo closed4 at right
                    n "This one is actually lower quality, there are better ones that can move... but they're so rare I haven't been able to find one."
                    s "...I see."
                    jump orcoutskirts2_neve
                "(Ask about help with the tentacle)" if (SUgivententaclequest == True and SUnevejoined == False):
                    call SUtentacle2neve
                    jump orcoutskirts2
                "What do you know about Jadk?" if (A_jadk >= 1 and nevejadkconvo == False):
                    $ nevejadkconvo = True
                    $ A_jadk += 1
                    $ A_neve += 1
                    show neveemo happy2 at right
                    n "Oh, you met him, have you? Happy old goat, isn't he?"
                    s "Assuming he's sincere, yes."
                    show neveemo happy1 at right
                    n "You won't find anybody more up-front than him. I heard he was real tough back in the day, he was actually a Captain in another tribe, but I think now he's too old to play games."
                    show sabiaemo closed2 at left
                    s "But he didn't try to become Captain here? I understand he's too old now, but surely before..."
                    show neveemo normal at right
                    n "He refused the position. That's one thing he's never explained, even when I've gotten him drunk. He might have just gotten tired of it."
                    show sabiaemo irritated2 at left
                    s "One more thing... should I be offended that he keeps complimenting me?"
                    show neveemo smirk1 at right
                    n "Hah! No, no, he does the same to me and every other attractive woman that comes through. He doesn't mean anything negative by it, I assure you."
                    show sabiaemo normal at left
                    s "Hmm..."
                    show neveemo closed1 at right
                    n "Truth be told... I think he's lonely. He still has desires, he's an orc after all, but he knows he's gotten old so he just tries to be friendly about it."
                    s "I see. Thank you for the information, Neve."
                    show neveemo irritated1 at right
                    n "When you say it like that I feel like a spy or something..."
                    jump orcoutskirts2_neve
                "Would you attend my feast?" if (orcfestivalquest == True and HGNneve == False and arenatime <= 0):
                    if orcalliance == "tekrok":
                        if A_neve >= 5:
                            n "I'd like to, but... Tekrok? Sorry, I'll have to pass."
                            jump orcoutskirts2_neve
                        else:
                            n "Sorry, Sabia, but it would be better if I didn't attend Tekrok's feast."
                            jump orcoutskirts2_neve
                    if A_neve >= 5:
                        $ orcfestivalscore += 2
                        $ HGNneve = True
                        n "I'd like to think you just want my company... but you're looking to solidify your reputation with this, aren't you?"
                        s "Of course I am. But I do honestly want you to be there, Neve. There aren't many people I can actually relax with here."
                        show neveemo happy1 at right
                        n "Hmmm... you are quite a bit of fun. I'll lend you the support of my presence if you promise to show me a good time."
                        show sabiaemo happy1 at left
                        s "Deal!"
                    else:
                        n "Hmm... I'm afraid I'm going to have to pass for now."
                    jump orcoutskirts2_neve
                "Any thoughts about the Red God's Arena?" if (arenatime > 0 and recruitmentopened == False):
                    n "I'll watch some of the matches, but it isn't my sort of thing."
                    jump orcoutskirts2_neve
                "Go back":
                    jump orcoutskirts2
        "Talk to Maply" if (maplyoutskirts == True and catgirlraidquest == False):
            call sabiabase
            show maply 1 at right
            show maplyemo normal at right
            with dissolve
            if maply_hellhound_quest == 7:
                $ maply_hellhound_quest += 1
                jump maply_hellhound_quest6
            elif maply_hellhound_quest == 10:
                $ maply_hellhound_quest += 1
                jump maply_hellhound_quest_end
            if catgirlstatus == "enslaved" or maplytortured == True:
                show maplyemo angry2 at right
                if maplyhellhoundprompt == True:
                    maply "..."
                    jump orcoutskirts2
                maply "Go away!"
                if maplyhellhoundprompt == False and tutorialraiddone == True and maply_hellhound_quest > 0:
                    $ maplyhellhoundprompt = True
                    show maplyemo angry1 at right
                    show sabiaemo closed2 at left
                    s "Maply, please wait."
                    s "You're always sneaking around... do you know what might be wrong with the hellhounds?"
                    show maplyemo angry2 at right
                    maply "Not that someone like you would care, but yes, I think they're just not cooperating!"
                    s "You sound really confident - since when do you know so much about hellhounds?"
                    show maplyemo angry1 at right
                    maply "I know a little about hellhounds, I actually care about other beings. There was another caravan that used them to pull their wagons."
                    s "So what do you mean by not cooperating?"
                    show maplyemo angry2 at right
                    maply "You can't tame hellhounds, not really. Tame animals think they're one of you - wild animals might become less dangerous, but at best they think you're one of them."
                    show maplyemo normal at right
                    s "Huh, I hadn't thought about it that way before. So it's not that the hellhounds can't be trained, it's that something's making them angry?"
                    show maplyemo normal at right
                    maply "Yeah, something like that. I'll go take a look."
                    "Sabia was about to object that she hadn't wanted that, but decided against it. Perhaps Maply had some expertise that could help her after all. And she never expected to make positive progress and talk with the catgirl that disliked her for the events that happened recently."
                jump orcoutskirts2
            menu orcoutskirts2_maply:
                "(Ask about Neve)" if (recruitmentopened == True and nevekiaprogression == 2):
                    $ nevekiaprogression = 3
                    s "You're sweet on Neve, aren't you?"
                    show maplyemo surprise1 at right
                    maply "What? How did you know?"
                    show sabiaemo eyebrow1 at left
                    s "It wasn't that hard to figure out."
                    show maplyemo sad1 at right
                    show maplyblush at right
                    maply "Gosh, this is so embarrassing..."
                    show sabiaemo happy1 at left
                    s "Why don't you just go talk to her?"
                    maply "Alioch said that too, but I don't know... I'm bad at this kind of thing... and what if she says no?"
                    show sabiaemo normal at left
                    s "Your only choices are to face rejection or wait forever. But I think Neve likes you - if she didn't, she wouldn't let you lurk around watching her."
                    show maplyemo happy at right
                    maply "R-really?"
                    show maplyemo sad1 at right
                    maply "Geez, I don't know if I can work up the nerve..."
                "Ask about the hellhounds" if maplyhellhoundprompt == False and tutorialraiddone == True and maply_hellhound_quest > 0:
                    $ maplyhellhoundprompt = True
                    s "Maply, you're always sneaking around... do you know what might be wrong with the hellhounds?"
                    maply "Oh, I think they're just not cooperating!"
                    s "You sound really confident - since when do you know so much about hellhounds?"
                    show maplyemo happy at right
                    maply "I know a little about hellhounds, ehehe. There was another caravan that used them to pull their wagons."
                    show maplyemo normal at right
                    s "So what do you mean by not cooperating?"
                    show maplyemo normalopen at right
                    maply "You can't tame hellhounds, not really. Tame animals think they're one of you - wild animals might become less dangerous, but at best they think you're one of them."
                    show maplyemo normal at right
                    s "Huh, I hadn't thought about it that way before. So it's not that the hellhounds can't be trained, it's that something's making them angry?"
                    show maplyemo happy at right
                    maply "Yeah, something like that! I'll go take a look!"
                    "Sabia was about to object that she hadn't wanted that, but decided against it. Perhaps Maply had some expertise that could help her after all."
                "What are you doing out here?":
                    show maplyemo happy at right
                    maply "Hunting! There's lots of food in camp, but I want to keep my skills sharp!"
                    if maplysexneve == True:
                        show sabiaemo eyebrow1 at left
                        s "And there's no other reason you're hanging around Neve?"
                        show maplyblush at right
                        maply "Hehehe..."
                "How are the other catgirls doing?":
                    if catgirlstatus == "free":
                        show maplyemo happy at right
                        maply "Everybody is great! They're amazed you just let us all go!"
                    elif catgirlstatus == "recruited":
                        show maplyemo normalopen at right
                        maply "The idea of working with orcs is still really strange to everybody, but some people are starting to get used to the idea..."
                    else:
                        show maplyemo eyebrows at right
                        maply "Some people don't like having to work off our debt, but it's a lot nicer than people trying to kill us... and we {i}did{/i} steal from you..."
                "Would you attend my feast?" if (orcfestivalquest == True and HGNmaply == False):
                    if A_maply >= 5:
                        $ orcfestivalscore += 1
                        $ A_maply += 1
                        $ HGNmaply = True
                        show maplyemo eyebrows at right
                        maply "Are you really inviting me? It's not like having some catgirl at your feast will help your reputation..."
                        s "I know, I just want you to attend. Will you?"
                        show maplyemo happy at right
                        maply "Hehehe, sure! Thanks, Saby!"
                        s "(That name... I really should ask her about it later.)"
                    else:
                        show maplyemo eyebrows at right
                        maply "Uhh... I don't know if I wanna be around so many drunk orcs, sorry..."
                "What do you know about Makhor?" if (maplykiatalk == False and recruitmentopened == True):
                    $ maplykiatalk = True
                    call KLmaplyconvo
                "Nothing":
                    jump orcoutskirts2
            jump orcoutskirts2_maply
        "Ylva and Neve" if (RGAylvapresent == True and ylva1nevetalk == False):
            call ylva1neve
            jump orcoutskirts2
        "Ylva and Maply" if (RGAylvapresent == True and ylva1maplytalk == False and maplytortured == False):
            call ylva1maply
            jump orcoutskirts2
        "Harvest venomnettle (10 stamina)" if (crafting_potions_unlocked == True and gotvenomnettle == True):
            if Sabia.stamina < 10:
                "Sabia was too tired to harvest any venomnettle."
                jump orcoutskirts2
            $ Inventory.add_item(Venomnettle)
            $ Sabia.stamina -= 10
            "Using her knife, Sabia harvested a small amount of venomnettle."
            if Inventory.has_item(Venomnettle) > 1:
                $ renpy.say(s, "(I have enough venomnettle to serve as an ingredient in {} potions.)".format(Inventory.has_item(Venomnettle)))
            else:
                s "(Alright, that should be enough for one potion.)"
            jump orcoutskirts2
        "Harvest venomnettle (10 stamina)" if (gotvenomnettle == False and silvertuskintro == True):
            if Inventory.has_item(Knife) > 0:
                if Sabia.stamina < 10:
                    "Sabia was too tired to harvest any venomnettle."
                    jump orcoutskirts2
                $ gotvenomnettle = True
                "Using her knife, Sabia was able to cut through the venomnettle at the root and harvest an adequate amount."
                s "(Alright, now I just need to take that back to Jadk!)"
                jump orcoutskirts2
            else:
                if Sabia.stamina < 10:
                    "Sabia was too tired to harvest any venomnettle."
                    jump orcoutskirts2
                $ Sabia.stamina -= 10
                "Sabia found some venomnettle and tried to pull it, but the tough plants refused to be uprooted and only hurt her hands."
                s "They're too low to the ground to use a sword on, I'd need something smaller..."
                jump orcoutskirts2
        "Go back":
            jump eastern_frontier_map
    jump orcoutskirts2


label travel_to_meet_vehlis:
    $ Sabia.stamina -= 200
    if vehlislocationquest == 1:
        $ vehlislocationquest = 2
        scene bg countryside
        "After orienting herself carefully, Sabia set off from the camp. It would be a bit of a journey, but since she wasn't headed toward a primary road, she hoped that she would be safe from bandits."
        "She settled into a steady march as if she was on the campaign trail, letting her mind drift to her plans. Though getting back at Lynn felt extremely far away, at least she was making progress."
        "That was a far better motive to look for this Vehlis than just helping with the orc festival. If she could find a representative of the Bank of Talos, she could potentially get a crucial ally in her conflict against her own family."
        "Of course, she'd need to prove that she was worth backing. Getting evidence of her birthright and building a true army would help with that. Hopefully this representative would be open to the idea, considering that she was open to something as mad as trading with orcs."
        "In the distance, Sabia actually saw what looked like the outer fields of a tiny village. Part of her longed to go toward it, just to be among humans again, but she restrained herself."
        "The chance that anyone would recognize her was low, but it was a risk she didn't need to take. And more importantly, she had nothing to gain in these tiny villages. No, the only one that mattered was the one where Vehlis was staying."
        scene bg black with dissolve
        pause 1
        scene bg road with dissolve
        "After a long march, Sabia knew that she must be getting close. She tried to plan for the encounter in her head as best she could. Appearances would be everything, since she needed to make her case effectively."
        "Unfortunately, she had no idea what kind of person Vehlis was, or why she had stopped visiting the orc camp. It was even possible that she had some kind of connection to Lynn, though that was a risk she'd have to take. Sabia sighed and decided that she simply lacked the information to fully prepare."
        call sabiabase
        "Just as Sabia was starting to feel like she'd arrive soon, she caught a glimpse of someone else in the nearby woods. She immediately leapt on guard, eyes narrow and her hand on her sword."
        show orcbase2 at right
        show orcloincloth2 at right
        show orcbeard21 at right
        show orcemo2 normalopen at right
        show orcwrists2 at right
        show orcaxe2 at right
        with moveinright
        "To her surprise, it was an orc. He seemed rather suspicious of her, and though Sabia stayed on guard, she gave him a smile."
        show sabiaemo happy1 at left
        s "Hello there! I don't suppose you're looking for Vehlis too?"
        orc "Who the fuck are you?"
        show sabiaemo surprised1 at left
        "Sabia blinked in surprise, not having expected that reaction. After a stunned moment, she realized her mistake. She had no reason to believe that this orc was from Groknak's tribe, especially given how close to human lands she had wandered."
        show sabiaemo normal at left
        s "Apologies, I thought I recognized you."
        orc "What kind of human recognizes orcs?"
        s "I fight for Chief Groknak."
        orc "Hunh. Me did not expect that, and not sure if me believe it."
        s "Well, I am. Which tribe are you from?"
        orc "Hmph. What you want?"
        menu:
            "Just leave":
                s "Well, since you aren't who I thought you were, we can just go on our way and not bother each other."
                orc "...wait."
                show sabiaemo normal at left
                s "..."
                orc "You say you want meet Vehlis?"
                s "That's right, I'm here on behalf of Chief Groknak. If you know her... did she say anything when you met? She doesn't have some kind of new policy against orcs, does she?"
                orc "Vehlis wasn't there. She's moved southeast."
                "Seemingly more comfortable with her, the orc approached and they talked about the specific location. Sabia groaned as she realized that she had gone far out of her way. At this point, it was probably safer to go back to camp than to cut across the countryside to her new location."
                s "Do you think she's going to stay there, or move on again?"
                orc "That place is special waystation. Maybe her trade route is done, does business there before returning."
                "If that was true, then Sabia had to find her quick before she headed back to Carchedon. She thanked the orc for his help and headed back to camp."
                hide orcbase2 at right
                hide orcloincloth2 at right
                hide orcbeard21 at right
                hide orcemo2 normalopen at right
                hide orcwrists2 at right
                hide orcaxe2 at right
                with moveoutright
                "Once he was out of sight, she doubled back to the hamlet to make sure, but a farmer told her that the Bank of Talos representative had been present but gone. Apparently she could have trusted the orc after all, but Sabia was still glad she had checked."
                "Though it irritated her to have wasted so much time, at least she was much closer to her goal."
                scene bg black with dissolve
                pause 1
            "Ask him for information":
                $ L_orcs += 1
                show sabiaemo normal at left
                s "What are you doing in these parts? I don't suppose you were looking for Vehlis too?"
                orc "...actually, yes."
                show sabiaemo happy1 at left
                s "Well? What did she say? She doesn't have some kind of new policy against orcs, does she?"
                orc "Vehlis wasn't there. She's moved southeast."
                "Seemingly more comfortable with her, the orc approached and they talked about the specific location. Sabia groaned as she realized that she had gone far out of her way. At this point, it was probably safer to go back to camp than to cut across the countryside to her new location."
                s "Do you think she's going to stay there, or move on again?"
                orc "That place is special waystation. Maybe her trade route is done, does business there before returning."
                "If that was true, then Sabia had to find her quick before she headed back to Carchedon. She thanked the orc for his help and headed back to camp."
                hide orcbase2 at right
                hide orcloincloth2 at right
                hide orcbeard21 at right
                hide orcemo2 normalopen at right
                hide orcwrists2 at right
                hide orcaxe2 at right
                with moveoutright
                "Once he was out of sight, she doubled back to the hamlet to make sure, but a farmer told her that the Bank of Talos representative had been present but had left recently. Apparently she could have trusted the orc after all, but Sabia was still glad she had checked."
                "Though it irritated her to have wasted so much time, at least she was much closer to her goal."
                scene bg black with dissolve
                pause 1
            "Fight him":
                $ L_orcs -= 2
                $ dom += 1
                show sabiaemo angry1 at left
                s "I don't know what kind of game you're playing, but you won't get away with it!"
                $ enemy_level = 5
                $ enemy_maxhp = 450
                $ enemy_hp = enemy_maxhp
                $ enemy_type = 1
                $ enemy_skills = [Enemyattack]
                $ enemy_attack = 65
                $ enemy_defense = 20
                $ enemy_magdefense = 0
                $ GenericOrc2.extras = ["Loincloth", "Beard1", "Wrists", "Axe"]
                $ GenericOrc2.face = "normalopen"
                $ player = Sabia
                $ enemy = GenericOrc2
                call duel
                if _return == "Victory":
                    pass
                else:
                    show gameover with dissolve
                    pause 3
                    $ renpy.full_restart()
                call sabiabase
                orc "Pl-please, wait! Don't kill me!"
                show sabiaemo annoyed1 at left
                s "I won't if you tell me just what you were trying to do here."
                orc "Me... me was looking for Vehlis too! Please, me tell you everything me know!"
                s "If what you have to say is worth it, I'll think about it."
                show sabiaemo normal at left
                "Desperate to save his life, the orc hastily explained that he had been looking for Vehlis, but found that she had already moved to the southeast. Sabia groaned as she realized that she had gone far out of her way. At this point, it was probably safer to go back to camp than to cut across the countryside to her new location."
                s "If I find out you were lying, I will track you down and kill you slowly."
                orc "Me not lying! Me not!"
                hide orcbase2 at right
                hide orcloincloth2 at right
                hide orcbeard21 at right
                hide orcemo2 normalopen at right
                hide orcwrists2 at right
                hide orcaxe2 at right
                with moveoutright
                "Sabia let the orc go, since he was no more threat to her. The much bigger concern was what he said."
                "If that was true, then Sabia had to find Vehlis quick before she headed back to Carchedon. She thanked the orc for his help and headed back to camp."
                "Once he was out of sight, she doubled back to the hamlet to make sure, but a farmer told her that the Bank of Talos representative had been present but gone. Apparently she could have trusted the orc after all, but Sabia was still glad she had checked."
                "Though it irritated her to have wasted so much time, at least she was much closer to her goal."
                scene bg black with dissolve
                pause 1
        jump orcoutskirts2
    elif vehlislocationquest == 2:
        $ vehlislocationquest = 3
        scene bg countryside
        "Armed with more updated information about Vehlis's location, Sabia headed out from camp. This time, she wouldn't come back until she had an agreement from the Bank of Talos representative."
        "Heading through the same countryside was rather dull, though. Sabia found her mind quickly drifting..."
        "At long last, she stumbled across a ring of defenses. Exactly the kind of thing that would be used to keep an official waypoint safe. Shaking off her lethargy, Sabia began scouting around the periphery."
        "Unfortunately, she didn't see any gaps in their lines. The soldiers were heavily armored, too - the very best she could do would be to find a guard alone and take him down to get through the circle."
        "Sabia scanned until she found a likely candidate, then took a deep breath and approached."
        show humansoldier normal at right
        with dissolve
        call sabiabase
        with moveinleft
        s "Hello there! This is the path to the waypoint, right?"
        soldier "Show your permission to approach immediately."
        s "Well, you see, bandits attacked and I lo-"
        show humansoldier angry at right
        soldier "You think you're the first person to try that? Back away or be cut down!"
        s "No choice but to do this, then..."
        $ enemy_level = 6
        $ enemy_maxhp = 600
        $ enemy_hp = enemy_maxhp
        $ enemy_type = 1
        $ enemy_skills = [Enemyattack]
        $ enemy_attack = 70
        $ enemy_defense = 30
        $ enemy_magdefense = 10
        $ Humansoldier.face = "angry"
        $ player = Sabia
        $ enemy = Humansoldier
        call duel
        if _return == "Victory":
            pass
        else:
            show gameover with dissolve
            pause 3
            $ renpy.full_restart()
        call sabiabase
        show sabiaemo closed2 at left
        with dissolve
        play music orccamp fadeout 2.0 fadein 2.0
        s "(Managed to beat him. I need to get in, speak with Vehlis, and get permission from her before he's discovered.)"
        s "(The question is whether or not I kill him...)"
        menu:
            "Kill him":
                $ L_orcs += 1
                $ L_humans -= 1
                "Sabia slit the soldier's throat and dragged his body into the bushes. She tried to strip off his armor, but realized that it would take too long and wouldn't fit her anyway."
            "Leave him unconscious":
                $ L_orcs -= 1
                $ L_humans += 1
                "Sabia dragged the soldier into the bushes. She tried to strip off his armor, but realized that it would take too long and wouldn't fit her anyway."
        s "(Well, now there's no option to retreat. I need to find Vehlis quickly.)"
        scene bg road3tavern with dissolve
        "Past the guard, Sabia spotted a structure at the end of the road. It looked like a lone inn, but it was surprisingly nice - that meant it had to be a waystation. Exactly the kind of place where someone like Vehlis might stay in between business deals."
        "Smiling, Sabia picked up her pace and quickly entered the inn. She found it mostly empty except for a few wealthy customers who took one glance at her and turned away. There was a woman standing behind the front desk who gave her a polite bow."
        innkeeper "Can I help you? Our rooms are rather expensive, I don't thi-"
        s "I'm not here to stay, I have a meeting with someone. Vehlis is still here, right?"
        innkeeper "Hmm? Yes, she is, but she didn't tell me that she was expecting anyone..."
        "Confused, the woman's eyes shifted behind her, to one of the ornate doors down the left hallway. Sabia caught the movement of her eyes and smiled."
        s "Well, she'll be glad to see me."
        innkeeper "W-wait! You can't just disturb guests like that!"
        "Sabia ignored her and marched down the hallway. The waystations had strong guards to ward off attacks, but they relied on good manners inside their walls. Well, she had gone too far for good manners, so she might as well press her advantage."
        "Finding the right door, Sabia pushed it open."
        call vehlisaliochA
        play music orccamp fadeout 2.0 fadein 2.0
        scene bg road3tavern
        call sabiabase
        show vehlis normal at right
        show vehlis2 arm1 at right
        with dissolve
        $ a_list.append("Vehlis")
        "A short time later, Sabia suppressed her embarrassment and focused on what she needed. Fully dressed, the aura of self control surrounding Vehlis was strengthened, if a little less shocking."
        vehlis "Now, what is it you wanted to speak about?"
        show sabiaemo annoyed1 at left
        s "I didn't realize the Bank of Talos allowed its representatives to behave like this!"
        vehlis "That was pleasure, this is business. But if we're speaking of professionalism, you've chosen an interesting outfit for a business meeting."
        show sabiaemo normal at left
        "Her eyes flickered up and down Sabia as if appraising the exact value of everything she was wearing."
        if Sabia.armor == Rags:
            $ A_vehlis += 0
            vehlis "The Bank of Talos chooses clients based on their ability to repay loans. And if you will excuse me saying so, you look like you're going through a difficult time."
            show sabiaemo closed2 at left
            s "(Sabia gritted her teeth and didn't let it get to her. She was sure that Vehlis wasn't mocking her clothes for petty reasons: no, it was a ploy to see what she would do when provoked. Instead, Sabia needed to respond rationally.)"
            show sabiaemo normal at left
            s "I won't deny that my fortunes have fallen lately. But I wouldn't have come here if I didn't think that could change, given the right support."
            vehlis "Hmm, I'll take what you say into consideration."
        if Sabia.armor == Leatherarmor:
            $ A_vehlis += 2
            vehlis "It does seem you've gone to some effort repurposing orc armor for yourself. That's resourceful, at least. Not terribly defensive, though."
            show sabiaemo closed2 at left
            s "(Sabia gritted her teeth and didn't let it get to her. She was sure that Vehlis wasn't mocking her for her clothes for petty reasons: no, it was a ploy to see what she would do when provoked. Instead, Sabia needed to respond rationally.)"
            show sabiaemo normal at left
            s "I can't overpower most of the opponents I fight, so speed is of the utmost importance."
            vehlis "Combat is not really my area of expertise, so I will take your word for it."
        if Sabia.armor == Orcslavearmor:
            $ A_vehlis += 1
            vehlis "That looks to me like orc armor, crafted for a sex slave. Not exactly the Bank's usual clientele."
            show sabiaemo closed2 at left
            s "(Sabia gritted her teeth and didn't let it get to her. She was sure that Vehlis wasn't mocking her for her clothes for petty reasons: no, it was a ploy to see what she would do when provoked. Instead, Sabia needed to respond rationally.)"
            show sabiaemo normal at left
            s "I do what I need to do in order to survive. Surely that's a desired quality in a client?"
            vehlis "Potentially. For the record, I have no objection to prostitution - it's a thriving part of business. Lundari orcs are not particularly known for doing it profitably, though."
        if Sabia.armor == Barmaidclothes:
            $ A_vehlis += 0
            vehlis "It seems you should be working in a tavern of some sort. Perhaps your pay there would be more appropriate for your financial needs?"
            show sabiaemo closed2 at left
            s "(Sabia gritted her teeth and didn't let it get to her. She was sure that Vehlis wasn't mocking her for her clothes for petty reasons: no, it was a ploy to see what she would do when provoked. Instead, Sabia needed to respond rationally.)"
            show sabiaemo normal at left
            s "It's sufficient for my survival. I came to you because I think there's the potential for a real profit."
            vehlis "Hmm, I'll take what you say into consideration."
        s "In any case, I'm not here to ask for a personal loan."
        show vehlis eyebrow1 at right
        vehlis "Oh? Well, then, please state your business."
        s "I'm here on behalf of Warchief Groknak."
        show vehlis closed2 at right
        vehlis "Hmm... that's certainly unexpected. They want me to return to do business with them again, I presume?"
        show sabiaemo irritated1 at left
        s "That's correct. May I ask why you stopped visiting?"
        vehlis "I have some questions for you first. How exactly does a human woman end up working with Groknak?"
        show sabiaemo normal at left
        s "..."
        menu:
            "Say you're an ally of the orcs":
                $ A_vehlis -= 1
                s "Not all humans hate orcs. I happen to be working with this group."
                show vehlis closed1 at right
                vehlis "Fascinating. It seems we were misinformed about the attitude of Lundari toward orcs."
                s "Some other details might have slipped past you as well. That's why I'm urging you to consider your investment."
            "Claim you're just doing your duty as a slave":
                if Sabia.armor == Orcslavearmor:
                    $ A_vehlis += 0
                else:
                    $ A_vehlis -= 1
                s "I don't want to get into the details, but they enslaved me. They needed a human to contact you, so they assigned me this."
                show vehlis eyebrow1 at right
                vehlis "That's rather a large amount of autonomy for a slave. A curious choice."
                s "The tribe is changing. They're worth your time and investment."
            "Refuse to answer":
                $ A_vehlis += 1
                s "Does it matter? I'm only a representative - all I need to convince you of is their economic value."
                show vehlis happy at right
                vehlis "Heh. Fair enough."
            "Explain some of the truth":
                $ A_vehlis += 2
                s "Truth be told... I'm a Lundari noble. I don't want to get into the politics that led me here, but I've been disowned. Working with orcs is my best chance to regain what I've lost."
                vehlis "I confess, I hadn't expected you to tell the truth. The Dufuor family isn't known for it."
                show sabiaemo surprised1 at left
                s "You were just testing me? How did you know who I was?"
                show vehlis closed1 at right
                vehlis "Relax, it's not for any sinister reason."
                show sabiaemo normal at left
                show vehlis normal at right
                vehlis "As a representative to the region surrounding Lundar, part of my job is to be intimately familiar with all the noble families. Your hair color is somewhat uncommon, and when combined with the rumors of your death... it wasn't so hard to put together."
                s "Then... are you going to tell anyone?"
                vehlis "No, I don't believe that would be in my best interest. But I would like to hear what you have to say."
        show vehlis normal at right
        vehlis "So, to business. Why exactly should I return to Groknak's tribe?"
        s "They're not even sure why you didn't return. At minimum, I would like to be able to explain the reason to them."
        vehlis "The blunt truth? It's no longer worth it to act as a liaison for them."
        show vehlis normalL at right
        show vehlis2 arm2 at right
        vehlis "I represent and bring the goods of a variety of mercantile interests. Many of them are operating on small margins - they aren't interested in doing business with a tribe that does not reach certain minimum levels of profit."
        show vehlis normal at right
        vehlis "It is not my place to comment on the choices Groknak has made for his tribe. But they have led returns to fall by 17 percent, which is unacceptable to most clients."
        "Vehlis held her book up as she spoke, but Sabia had a feeling that she was reciting the numbers from memory. The other woman's eyes watched her steadily, polite on the surface and yet shark-like underneath."
        s "It may not be your place, but it is mine. The Warchief is leading his tribe to stagnation. But I don't believe it will continue that way, and I believe it would be worth your while to maintain business connections with them."
        show vehlis2 arm1 at right
        vehlis "How so?"
        if orcalliance == "tekrok":
            s "Groknak will most likely be succeeded by a younger Captain named Tekrok. He has far more ambitious plans for the tribe."
        elif orcalliance == "rokgrid":
            s "Groknak will most likely be succeeded by a younger Captain named Rokgrid. He intends to increase production and trade relations with humans and other races."
        elif orcalliance == "dajrab":
            s "Groknak will most likely be succeeded by a Captain named Dajrab. His understanding of the orcs' current situation is far more nuanced."
        else:
            $ A_vehlis += 1
            s "Because the tribe is changing. They allowed me into their ranks as a warrior - their period of stagnation is in the past."
            vehlis "Oh? That's rather uncommon, for Lundari orcs."
            s "Are you still skeptical? It's the truth."
        vehlis "Hmm. That's easy enough to say, but the Bank of Talos has learned that the word of rulers is worth much less than gold. Look me in the eye and tell me that you really believe that."
        s "Of course I believe it!"
        if L_orcs >= 10:
            $ orcfestivalscore += 2
            $ A_vehlis += 1
            "Sabia put all the conviction she could into her words. Though it was ridiculous, she had a good feel for the orc tribe now and really believed what she was saying."
            "Vehlis stared at her, eyes penetrating, then gave a slight nod."
        elif L_orcs >= 5:
            $ orcfestivalscore += 1
            "Sabia tried to fill her words with conviction, but she hesitated slightly. The orcs might have accepted her, but she doubted they liked her. She believed in her own words, but she had doubts."
            "Vehlis stared at her, eyes penetrating, then gave a slight shrug."
        else:
            $ orcfestivalscore -= 1
            "Sabia tried to make the lie believable, but she stumbled a little. Thinking over how many of the orcs disliked her, she wasn't truly sure of the changes or how much impact she could have on them."
            "Vehlis stared at her, eyes penetrating, and didn't seem convinced. But after a pause, she gave a slight shrug."
        vehlis "Very well. If the tribe is truly moving in a less stagnant direction, that might be worth revisiting the issue. But my job is not to produce a narrow profit. Keep convincing me."
        menu:
            "Bring up the catgirls":
                if catgirlstatus == "recruited":
                    $ A_vehlis += 2
                    s "There was an interesting incident in camp involving a caravan of catgirls. I won't get into the details, but now there's the beginning of a true alliance between orcs and catgirls."
                    show vehlis eyebrow1 at right
                    vehlis "Truly? I can't imagine you'd lie about something that bizarre, so perhaps there is something interesting going on. That's quite a change for them..."
                elif catgirlstatus == "free":
                    $ A_vehlis += 1
                    s "We've formed the beginning of an alliance with one of the nearby catgirl caravans. I don't need to explain to you the potential benefits to the tribe."
                    show vehlis closed1 at right
                    vehlis "Is that so? A curious development, but an interesting one."
                elif catgirlstatus == "enslaved":
                    $ A_vehlis -= 1
                    s "The orcs have a brand new source of economic strength that I doubt you know anything about. They recently enslaved a group of catgirls, which will be a real boost to their productivity."
                    show vehlis closed1 at right
                    vehlis "Hmm..."
                    s "What? Carchedon and the Bank of Talos are basically built on slavery - surely you can't disapprove."
                    show vehlis eyebrow1 at right
                    vehlis "Of course not. Need I remind you what I was doing when you entered?"
                    show vehlis normal at right
                    vehlis "But I've found that Lundar - and I mean all races in the region - tends to do slavery with a heavy hand. It's certainly not the economic powerhouse it is in Carchedon."
                    s "But still... the addition of so many slaves must have some value."
                    vehlis "You're right, it does. I'm intrigued, I just wonder if you'll be able to hold it together."
                else:
                    $ A_vehlis += 1
                    show sabiaemo closed3 at left
                    s "There was an interesting incident in camp involving a caravan of catgirls. I won't get into the details, but suffice it to say, they're now working off a debt to the tribe."
                    show sabiaemo happy1 at left
                    s "In addition to the immediate benefits, I believe this will develop into the orcs becoming less isolationist than usual."
                    vehlis "That's certainly quite a change from previous policy, I'm surprised Groknak agreed."
            "Bring up Governor Andian":
                if barrinletterquest:
                    $ A_vehlis += 2
                    s "You're well-connected, you must know that Governor Andian is lying about the state of his region in a bid to join Lundar."
                    show vehlis closed1 at right
                    vehlis "You don't say?"
                    s "I wonder... how much do you know about Governor Sceyuer's plans for the incorporation?"
                    show vehlis eyebrow1 at right
                    vehlis "It seems you're more connected than one would imagine. I don't think I want to share what I know in that regard, but... you have my interest."
                    s "Their conflict is going to cause this region to change, and the chaos will upset all current trade. Would you rather bet on those who are oblivious to it, or those who are preparing for it?"
                else:
                    $ A_vehlis += 1
                    s "You're well-connected, you must know that Governor Andian is lying about the state of his region in a bid to join Lundar."
                    show vehlis closed1 at right
                    vehlis "You don't say?"
                    s "That's going to cause this region to change, and the chaos will upset all current trade. Would you rather bet on those who are oblivious to it, or those who are preparing for it?"
            "Reiterate your arguments":
                if dom >= 5:
                    $ A_vehlis += 1
                    s "I've been among the tribe, I've seen things change. Trust me, you're going to want to be involved before it becomes more profitable, or you won't get a chance later."
                else:
                    s "I've been among the tribe, I've seen things change. Trust me, it will be different than you saw before."
        show vehlis normal at right
        vehlis "This is more interesting than expected. I think I can justify another exploratory visit."
        show sabiaemo happy1 at left
        s "Ah, wonderful! I can provide an escort if you like!"
        vehlis "Please... the Bank of Talos takes care of its own. I'll be along in my own time, though it shouldn't be long."
        show sabiaemo normal at left
        vehlis "But our conversation isn't done yet... what about you, Sabia? Is assisting these orcs so altruistically really your highest goal in life?"
        "Though the question made her uncomfortable, the way she asked it made it obvious that lying would be pointless."
        s "Obviously not. I have business to return to in human lands, but due to recent setbacks, I have no choice but to work with orcs to get there. Perhaps at a later time we can discuss further business."
        vehlis "Hmm... if that business involves destabilizing Lundar, I'm going to have to nip that possibility in the bud."
        show sabiaemo surprised1 at left
        s "Huh? But... isn't Carchedon interested in funding rebels?"
        show vehlis eyebrowL at right
        vehlis "My, it seems you take your own propaganda seriously."
        show sabiaemo closed2 at left
        s "Explain yourself."
        show sabiaemo normal at left
        vehlis "Carchedon and Lundar may not be comfortable allies, but do you really think we want Lundar overthrown? No, most would rather Lundar become a more stable country."
        show vehlis normal at right
        vehlis "The present Lundar, not to mention the surrounding regions, is far larger than most nations and possesses many valuable natural resources. Better for those to be controlled by a reliable trading partner than scattered among constantly shifting tribes."
        show sabiaemo closed1 at left
        s "Oh, please. Funding rebels doesn't have to mean overthrowing the whole monarchy. You don't expect me to believe Carchedon doesn't try to manipulate Lundari politics?"
        show vehlis angry3 at right
        vehlis "I won't insult your intelligence."
        show vehlis closed1 at right
        vehlis "However, I personally would rather not get involved with political complications. So if you intend to give me a proposal in the future... I suggest you think about it carefully."
        s "Noted."
        show sabiaemo closed1 at left
        s "(Not as much as I'd hoped, but far better than I feared. If I prove myself reliable, Vehlis could well be an invaluable resource in the future.)"
        show vehlis normal at right
        vehlis "I've heard enough - I'll return to Groknak's camp and see what I think of these changes. I trust that will be agreeable to you?"
        show sabiaemo happy1 at left
        s "Yes, thank you!"
        vehlis "Then I'll conduct some business of my own, while you arrange details with my slave. Alioch?"
        show sabiaemo normal at left
        show alioch normal at center with moveinright
        alioch "Yes, Mistress?"
        "The elf slave had slipped away after the first encounter and Sabia was impressed with just how well he'd stayed out of the way. Slaves from Carchedon really were on a different level compared to most elven slaves in Lundar."
        vehlis "Arrange the petty details with her, then see her on her way. After that, you'd best begin packing quickly."
        alioch "Of course, Mistress."
        hide vehlis normal
        hide vehlis2 arm1
        with moveoutright
        "Vehlis disappeared deeper into her rooms, leaving Sabia left standing awkwardly with the slave. She didn't know how to read the symbols on his collar, but apparently he was one of the better trained varieties of slaves from Carchedon."
        "He was able to read and write, showing her some papers and arranging details for basic trade with the orc camp. Though he was very subservient, there was still an edge of something that she didn't like."
        "The best slaves might come from Carchedon, but her mother had always said that no one from the country could be trusted. There were many free elves there, humans could be slaves, slaves could be freed... the natural order was upset in many small ways that no amount of training could ever truly remove."
        show alioch sad at center
        alioch "Is something amiss? Let me know if I can serve you better."
        s "It's nothing, just wrapped up in my own thoughts. You'll be coming to the camp soon, then?"
        show alioch happy at center
        alioch "I believe so. Though she doesn't show it, Mistress Vehlis was pleased by your visit. This should prove interesting to her."
        s "Hmm, really? Pleased enough that you think she'll help us?"
        show alioch normal at center
        alioch "It depends on her analysis of conditions in camp, of course."
        if A_vehlis >= 5:
            $ orcfestivalscore += 4
            show alioch happy at center
            alioch "But personally, I think she's very interested in you. And that is better than her liking you."
        elif A_vehlis >= 2:
            $ orcfestivalscore += 2
            alioch "But personally, I think you made a good impression."
        elif A_vehlis >= 0:
            $ orcfestivalscore += 1
            alioch "But personally, I think you made a decent impression."
        else:
            $ orcfestivalscore -= 1
            show alioch sad at center
            alioch "I think she's rather skeptical of what you've said, but the fact that she is changing her plans is significant."
        "It felt awkward to be talking to an elven pleasure slave like this. But her conversations with Neve had made it easier for Sabia, and she'd never felt elves were as worthless as races like orcs. She actually found it in herself to smile at Alioch."
        show sabiaemo happy1 at left
        s "I hope we'll be working together, then. Will you be coming to the camp as well?"
        show alioch eyebrow2 at center
        alioch "Though there are few places I would less like to be than an orc encampment... yes. Mistress Vehlis should not waste her time executing the trade that she will arrange at the broader level."
        s "I will count on seeing you there, then."
        scene bg black with dissolve
        "Motivated by how well the meeting had gone, Sabia headed back toward camp with a spring in her step. She'd laid the groundwork for not only this festival, but for all of her plans."
        "By the time she got back, she was tired and sore, but Sabia felt more satisfied than she had been in a long time."
        jump lowerorccamp



label mainhall2:
    scene bg mainhall
    $ renpy.block_rollback()
    if mainhallintro == False:
        $ mainhallintro = True
        $ catgirlraidpermission = True
        "Now that Sabia was a respected member of the tribe, the guards allowed her into the Warchief's hall with barely a nod."
        "She found it mostly empty, at least compared to how full it had been during the trial. A few orcs sharpened weapons, some were stacking loot, others spoke in low voices."
        show groknak normal at right
        "At the far end of the hall was Warchief Groknak, just finishing some meeting. He saw her, scowled, and approached."
        call sabiabase
        if A_groknak >= 2:
            show groknak angry1 at right
            g "Warchief Groknak told you to stay away. But you're not good at listening, are you?"
        else:
            show groknak angry3 at right
            g "Warchief Groknak never wanted to see you again, human! Do you have no ears?"
        show sabiaemo eyebrow1 at left
        s "Would you rather I just be lurking in your camp, or come deal with you directly?"
        show groknak normal at right
        g "Hmph. Very well. Why are you here?"
        show sabiaemo normal at left
        s "I've heard about your little problem with the catgirls. I want permission to help get back what they stole."
        show groknak suspicious1 at right
        g "In order to gain further advantage. Warchief Groknak swears, you are the most ruthless human he has ever met."
        if sexworktimes >= 1:
            g "Most human females cry and scream. But you barely hesitated to use your body to gain an advantage."
            show sabiaemo eyebrow1 at left
            s "What, as opposed to not taking advantage of it?"
            g "Hmph. You are a dangerous human."
        show sabiaemo normal at left
        if A_groknak >= 2:
            $ catgirlraidinvestigation += 1
            show groknak happy at right
            g "Warchief Groknak hopes that you can make this problem better instead of worse. You have your permission, though Warchief Groknak advises you to come up with the second plan, not the first."
            s "The second plan? What do you mean?"
            g "Whenever the catgirls steal, the first plan is always a raid on the nearest caravan. It fails, and then calmer heads invent a second plan. Be part of that second plan."
        else:
            show groknak angry3 at right
            g "Warchief Groknak grants you permission. But if you shame this tribe, you will regret it."
        s "Thank you. I'll make this little problem of yours go away."
        g "We shall see."
    menu:
        "Talk to Warchief Groknak":
            call sabiabase
            show sabiaemo normal at left
            show groknak normal at right
            g "What? I'm busy."
            menu:
                "So, is the trial completely over?" if recruitmentopened == False:
                    g "When the Warchief has ruled, the ruling is permanent. The matter is in the past."
                "Can I lead a raid to recover the stolen metal?" if (maplycaptured and catgirlraidquest):
                    g "You'd better not be wasting my time, human."
                    s "(I'm only going to have one shot at this... I'd better do everything I can to prepare first.)"
                    menu:
                        "Start the plan":
                            jump catgirlraidevent
                        "Not yet":
                            jump mainhall2
                "Do you know anything about Governor Andian?":
                    show groknak suspicious2 at right
                    g "Warchief Groknak will not be part of your games!"
                "Do you need any help around here?" if mainhalljob == False:
                    $ mainhalljob = True
                    g "What?"
                    s "I'm part of the tribe, right? I'm just curious if there's anything I can do to help."
                    show groknak suspicious1 at right
                    g "Hunh."
                    show groknak suspicious2 at right
                    g "Warchief Groknak thinks it is perhaps human nature to meddle in such things. It is not orc nature."
                    g "There are many tasks that go unfinished because few warriors want to do them. Speak to the orcs here. The payment is high for such work."
                "Any thoughts about the Red God's Arena?" if (arenatime > 0 and recruitmentopened == False):
                    g "It is a grand event. Do not dishonor the tribe with a weak performance."
                "Nothing":
                    show groknak angry3 at right
                    g "Don't waste my time!"
            jump mainhall2
        "Talk to Vehlis" if vehlislocationquest == 3:
            if arenatime > 0 and arenatime < 11:
                "To Sabia's surprise, Vehlis was nowhere to be found."
                jump mainhall2
            if maply_hellhound_quest == 3:
                $ maply_hellhound_quest += 1
                jump maply_hellhound_quest3
            call sabiabase
            show sabiaemo normal at left
            show vehlis normalL at right
            show vehlis2 arm2 at right
            vehlis "Hmm?"
            menu mainhall2_vehlis:
                "So, what do you think of the orc camp?":
                    show vehlis normal at right
                    vehlis "It seems you were right about it changing. Whether it's changing in a positive direction remains to be seen."
                "Why did you end up working in Lundar?":
                    show vehlis normal at right
                    vehlis "I was assigned here by the Bank of Talos because they believed I would be well-suited to the position."
                    s "That's it? No more story than that?"
                    show vehlis normalL at right
                    vehlis "I'm here for business purposes, not personal ones."
                "What's the situation in Carchedon?":
                    show vehlis normal at right
                    vehlis "Nothing so far out of the ordinary."
                    s "Maybe so, but I haven't exactly had access to good sources of news lately."
                    vehlis "As usual, there is discussion of trade routes. Debate about how best to trade with Kazzak. Some are claiming they've found more reliable paths across the Karima Desert. Concern about monster attacks on our ports on the continent."
                    show sabiaemo eyebrow1 at left
                    s "And Lundar?"
                    show vehlis eyebrow1 at right
                    vehlis "As always, we wish nothing but the best for our northern neighbors."
                "Will you attend my feast?" if HGNvehlisinvited == False:
                    $ HGNvehlisinvited = True
                    s "I'm planning something special, do you want to spend some time at my feast?"
                    vehlis "Sorry, but I must refuse. As a neutral party, I will be making a perfunctory appearance at the Warchief's bonfire only."
                    s "Ah, I see..."
                    show vehlis eyebrow1 at right
                    vehlis "Playing politics, are we? I won't get involved personally, but perhaps I can offer you a little something. Speak with me if you have Lundils to spare."
                    s "Alright, thank you."
                    vehlis "A tribe of nothing but males will drink a lot. You'd better speak to Alioch to be ready."
                "Do you have any special goods?" if (HGNvehlisinvited == True and Inventory.has_item(HGNTent) == 0 and arenatime <= 0):
                    show vehlis normal at right
                    vehlis "I have an extra tent of my own, much higher quality than you'd see in this camp. It's yours, for 175 Lundils."
                    menu:
                        "Purchase (175 Lundils)":
                            if money < 175:
                                "Sabia didn't have enough money."
                                jump mainhall2
                            $ money -= 175
                            $ Inventory.add_item(HGNTent)
                            s "It's big enough to host a feast in?"
                            vehlis "More than big enough."
                            s "Then I suppose I'll take it."
                            vehlis "Alioch will have it delivered in time for the feast. Nice doing business with you."
                        "Not now":
                            vehlis "Suit yourself."
                "Any thoughts about the Red God's Arena?" if (arenatime > 0 and recruitmentopened == False):
                    vehlis "No. What the orcs do with their own time is their own business."
                "So, Neve mentioned something to me..." if SUgreyisle_prompt == 1:
                    $ SUgreyisle_prompt += 1
                    show vehlis normalL
                    show sabiaemo normalopen
                    s "Something about a Carchedonese expedition to the Grey Isle."
                    s "She added that there are records of it?"
                    show sabiaemo normal
                    show vehlis eyebrow2
                    vehlis "Of course there are records of it. We keep records of everything that we can."
                    show vehlis happy
                    vehlis "You never know when having proper records might prove you right in a valuable trade deal."
                    show vehlis normalL
                    show sabiaemo happy2
                    s "I can't imagine you've ever been on the poor end of a trade deal, somehow."
                    show sabiaemo normal
                    show vehlis happy
                    vehlis "You might be right about that, Sabia."
                    show vehlis open
                    vehlis "Were you after anything in particular? I have the records on hand, if you'd like to look at them."
                    show vehlis eyebrow2
                    vehlis "Though I can't promise they'll be too exciting."
                    show vehlis normalL
                    show sabiaemo happy3
                    s "Sure, if you don't mind!"
                    show sabiaemo normal
                    "Vehlis looked down at her desk, shuffling documents and pieces of paper around until she found what she was looking for."
                    "She held it out, and Sabia accepted it."
                    show sabiaemo irritated2
                    "Sabia skimmed through it quickly."
                    "It listed - in detail - each ship, the crew on each of them, all supplies and debts that the captains carried, and all the trade agreements brokered before they set sail."
                    show sabiaemo normal
                    "After finishing reading it, she handed it back to Vehlis who filed it neatly back where she had found it."
                    show sabiaemo normalopen
                    s "That's... uh, very detailed. I've seen more than a few military and intelligence reports far less detailed than that."
                    show sabiaemo normal
                    show vehlis happy
                    vehlis "We do try our best."
                    show sabiaemo happy1
                    s "I've never had access to a Carchedonese report before. Thanks, Vehlis."
                    vehlis "Of course, Sabia."
                    if SUtentaclequestdone == True:
                        hide vehlis
                        hide vehlis2
                        show sabiaemo closed2
                        show sabiaemo2 blush at left
                        s "(Hopefully mine and Neve's exploits will go unrecorded though...)"
                "Nothing":
                    jump mainhall2
            jump mainhall2_vehlis
        "Notice unusual Vehlis conversation" if (kiaprogression >= 9 and SUgivententaclequest == False):
            call SUtentacle1
            jump mainhall2
        "Reserve a room for Sabia's Squad" if SUelmyprompt == True and SUelmyreservation == False:
            $ SUelmyquest += 1
            "After a lot of uncertainty about how to get a room for her orcs, Sabia eventually realized that she needed to reserve it at the main hall."
            if admintimes >= 5:
                "Though the shabby orc administration looked like a nightmare, Sabia was glad to see orcs she recognized from her work. They were glad to put her request first and said she only needed to pay 50 Lundils instead of the usual price."
                menu:
                    "Pay (50 Lundils)":
                        if money >= 50:
                            $ SUelmyquest += 1
                            $ SUelmyreservation = True
                            $ money -= 50
                            "Sabia paid the fee and got her date established. She still needed to set it all up at the Silvertusk Bar, of course."
                        else:
                            "Sabia didn't have enough money."
                    "Not now":
                        pass
            else:
                "One of the orcs told her that it would cost 200 Lundils to rent a room for the event, which struck her as robbery, but she didn't have much of a choice."
                menu:
                    "Pay (200 Lundils)":
                        if money >= 200:
                            $ SUelmyquest += 1
                            $ SUelmyreservation = True
                            $ money -= 200
                            "Sabia paid the fee and got her date established. She still needed to set it all up at the Silvertusk Bar, of course."
                        else:
                            "Sabia didn't have enough money."
                    "Not now":
                        pass
            jump mainhall2
        "Assist administrators (50 stamina)" if mainhalljob:
            if Sabia.stamina < 50:
                "Sabia was too tired to work."
                jump mainhall2
            $ Sabia.stamina -= 50
            if admintimes >= 5:
                $ admintimes += 1
                $ money += 5
                "Sabia worked on the orc records, but things were running smoothly thanks to her new system and the orcs hadn't fucked it up yet. She was paid 5 Lundils."
            elif admintimes >= 4:
                $ admintimes += 1
                $ money += 20
                $ L_orcs += 1
                "Sabia set about organizing more of the orcs records and miraculously, by the end of the day, she felt like she had accomplished most of the work. Their records were no longer an utter mess."
                "Amazingly, some of the orcs even helped out. They didn't care enough to make such a system themselves, but they appreciated actually being able to find what they needed in a reasonable amount of time."
                "Eventually Sabia sat back and surveyed her work with a strong sense of satisfaction. She'd actually made a difference here. The orcs seemed to agree, paying her 20 Lundils for the day."
            elif admintimes >= 1:
                $ admintimes += 1
                $ money += 12
                "Having remade some of the orcs' record systems, Sabia set about organizing the old material into them and working with everything new that came in. Soon, orcs were bringing her problems they didn't want to deal with."
                "It was a little irritating, but Sabia felt like she had made significant progress. When she finished, she was paid 12 Lundils."
            else:
                $ admintimes += 1
                $ money += 8
                "Sabia sat down with some of the orcs and began looking over their papers. It seemed they had primitive systems for keeping inventories and some records, but they weren't kept up remotely enough to be adequate."
                "It wasn't as if they could just ignore those things, either, since their tribe had enough complexity that they really did need systems of organization. Instead they just operated inefficiently and no one seemed to care."
                "Irritated by the principle of the thing, Sabia set about reforming what she could. Though she preferred leading, she thought she was a pretty decent administrator."
                "By the time she finished, she felt like she had gone more backwards than forwards. Still, she was paid 8 Lundils for her efforts."
            jump mainhall2
        "Investigate back rooms" if metnoblecaptive == False:
            $ metnoblecaptive = True
            scene bg mainhall
            call sabiabase
            "Most of the smaller rooms in the hall were locked and looked like unremarkable storerooms. But there were a number of orcs milling around one, grumbling unhappily. Sabia headed closer to find out just what was happening."
            "The orcs were muttering something about... a human captive? Sabia blinked in surprise and looked around for someone she could ask. To her surprise, Lutvrog was standing by the doorway."
            show lutvrogbase at right
            show lutvrogaxe at right
            show lutvrogwraps at right
            show lutvrogwrists at right
            show lutvrogemo normal at right
            with dissolve
            s "Just what's going on here?"
            lut "There is... a problem. We have captured a human."
            s "...and? Isn't that something that happens regularly?"
            lut "This one is a noble, Lutvrog thinks. Attacking his group was an accident, they were moving near our camp. More humans may come looking for them. Lutvrog thinks maybe it was a trap to lure us into battle."
            s "I see. Do we know why they were here?"
            lut "No. He is terrified and refuses to speak with us."
            s "And this is your problem now? Alright, Lutvrog, I'll help you out at least a little."
            lut "Thank you, Sabia."
            scene bg mainhall
            call sabiabase
            with dissolve
            s "Alright, let me see the captive..."
            show barrin normal at right with dissolve
            "She entered the small room and spotted the captive, a young man built like a warrior. He was strapped to a table with his armor unstrapped and askew - no doubt the orcs had searched it to make sure he wasn't hiding anything. Sabia scanned his face and nodded to herself."
            s "(I think I recognize him. Definitely a son of Governor Sceyuer, what was his name? Hmmm... Barrin Sceyuer?)"
            s "(The Sceyuer lands are out in the boondocks, he probably won't recognize me. I should pretend I don't know him either, though.)"
            show barrin sad at right
            barrin "Is... is someone there?"
            show sabiaemo happy3 at left
            s "Oh, thank Relona! They didn't hurt you!"
            barrin "A... another human? What are you doing here?"
            s "The orcs captured me too... but they're acting like you're important! Are... are you a noble?"
            show barrin angry at right
            barrin "I'm Barrin Sceyuer! They... they can't treat me this way!"
            show sabiaemo sad2 at left
            s "Oh... I'm sorry, Barrin, but they're trying to decide how to kill you..."
            show barrin angry2 at right
            barrin "What? Th-that's absurd! My father would exterminate all of them!"
            s "I'll try to convince them, but... what were you doing here?"
            show barrin sad at right
            barrin "This isn't the time for that! Help me!"
            s "I'll do what I can..."
            hide barrin normal with dissolve
            show sabiaemo closed2 at left
            s "(He's panicking. My meek act made sure he didn't suspect me, but it's not going to be enough. If I want to extract information from him, I'll need a better plan...)"
            show lutvrogbase at right
            show lutvrogaxe at right
            show lutvrogwraps at right
            show lutvrogwrists at right
            show lutvrogemo normal at right
            with dissolve
            lut "Did you learn something?"
            show sabiaemo normal at left
            s "I'm not sure why they were here, but it definitely wasn't some scheme. Not unless he wasn't in on it."
            lut "So it was... an accident."
            s "Seems that way to me. All he wants to do is go back home. If you can negotiate some kind of agreement with him, maybe we can get out of this without starting any wars."
            lut "Difficult, but possible. Lutvrog thanks you."
            s "No problem!"
            show sabiaemo closed2 at left
            s "(I might be able to get information from him about politics in Lundar, or at least Governor Andian's position. Maybe I should interrogate him myself before the orcs get rid of him one way or another...)"
            jump mainhall2
        "Interrogate Barrin Sceyuer" if (metnoblecaptive == True and barrinint2 == False):
            if barrinint1:
                if barrinintdelay:
                    s "(I need to let him squirm a little longer first to loosen his tongue.)"
                    jump mainhall2
                call barrininterrogation2
            else:
                call barrininterrogation
            jump mainhall2
        "Investigate human merchants" if (orcfestivalquest == True and vehlislocationquest < 1):
            $ vehlislocationquest = 1
            call sabiabase
            show orcbase at right
            show orcloincloth at right
            show orcbeard1 at right
            show orcnecklace at right
            show orcwrap at right
            show orcemo normal at right
            with dissolve
            "Sabia approached one of the administrators who didn't seem to be busy."
            s "The tribe can't have manufactured all of this... do you trade with local humans in any way?"
            orc "Nuh. Too dangerous. Most of our trade is through Vehlis."
            s "Vehlis? Who's that?"
            orc "From Bank of Talos. Sometimes comes by to trade an-"
            show sabiaemo closed2 at left
            s "Wait, as in {i}the{/i} Bank of Talos? The real one?"
            show orcemo normal at right
            orc "You think we make fake Bank out of mud and sticks?"
            show sabiaemo normal at left
            s "No, nothing like that! I was just surprised!"
            show sabiaemo closed2 at left
            s "(The Bank of Talos trades with orcs? I wouldn't believe it if I hadn't seen evidence... what's wrong with them? Carchedonese degenerates...)"
            show sabiaemo closed1 at left
            s "(But this is an incredible stroke of luck. A bank representative would have all the mercantile connections I need, both for the festival and for longer term goals.)"
            show sabiaemo normal at left
            s "Do you have some kind of arrangement with the Bank?"
            show orcemo normal at right
            orc "Not formally. Also, very long time since Vehlis visit. She is still nearby, so maybe she think not safe now."
            s "She's nearby, huh? You know where she is now?"
            orc "Last heard she was making deal in nearby human province."
            "The orc got out a rough map and showed her a specific location, a tiny hamlet that wasn't so far from camp. Sabia quickly memorized the location."
            s "Thank you, this is useful."
            orc "If you convince Vehlis to come back, me thank you. Her trade very important."
            s "I'll see what I can do."
            jump mainhall2
        "Go back":
            jump upperorccamp
    jump upperorccamp


label tekroktent2:
    scene bg tekroktent
    $ renpy.block_rollback()
    if tekrokblock:
        s "(It's clear I'm not welcome in Tekrok's tent anymore.)"
        jump upperorccamp
    if A_tekrok < 1:
        s "I'm not on the best of terms with Tekrok, I'd better stay away."
        jump upperorccamp
    if (orcalliance == "tekrok" and recruitmentopened == True and tekrokraidintroduced == False):
        call tekrokraidintro
        $ captaincooldown = True
        jump upperorccamp
    if (orcalliance == "tekrok" and tekroktargetraided == True and tekrokraidaftermathscene == False):
        call tekrokraidaftermath
        jump upperorccamp
    if (orcalliance == "tekrok" and tekrokraidintroduced == True and tekrokraidsexdone == False and captaincooldown == False):
        call tekrokraidsex
        jump upperorccamp
    if orcalliance == "tekrok":
        if orcalliance == "tekrok" and orcfestivalquest == False and arenatime <= 0:
            $ orcfestivalquest = True
            call sabiabase
            show tekrok normal at right
            if tekrokalliance:
                s "It seems the Horned God's Night is coming up soon. I assume we will be working together."
                t "Yes. This will be your chance to prove your worth to Tekrok, for it will be no minor festival."
                t "But the two of us working on the same feast will create a permanent alliance. Tekrok trusts you understand that is best?"
            else:
                s "It seems the Horned God's Night is coming up soon. Do you still need my help?"
                t "Hah! After spurning Tekrok, you now come crawling back?"
                t "But yes, this will be a great opportunity and Tekrok cannot turn down aid."
                t "You have proved you are less worthless than most humans. Tekrok is willing to make an alliance, if you understand the seriousness of the decision."
            s "I wouldn't have come here if I wasn't sure. What exactly can I do to get the support I need?"
            t "Heh, very well. The Horned God's Night is indeed your best chance. It is also Tekrok's chance to edge out his enemies."
            s "So, what exactly needs to be done?"
            t "Tekrok has already begun gathering food and alcohol for the feast. But we always need more, bring what you can. However, Tekrok thinks that you can be more useful in two other ways."
            t "First, we must create a grand pavilion to outshine the others. Tekrok plans to build a fearsome one, but it will require gold and other human finery as well. You are more likely to be able to acquire such things."
            s "Right, because you can't really trade with humans. I'll see what I can do. What's the last thing?"
            t "Each feast will be centered upon a shrine to the Horned God. It will be made of many antlers, as large as possible - if you wish to be taken seriously, you must bring a grand set of antlers."
            t "Actually, fuck that... since you're human and all, you'd better bring a white hind."
            s "Do you actually have those around here? I thought they were quite rare."
            t "There are a few. That's why they're the best offering for the feast. Tekrok thinks you should find one if you wish to be taken seriously."
            s "Hmmm... alright, that doesn't seem so hard. I'll do everything I can to make our feast better than the others."
            if A_tekrok >= 7:
                $ Inventory.add_item(Furnishings)
                t "Do not waste your time acquiring furnishings. Tekrok already has those."
            t "It is still many days until the Horned God's Night. Do not disappoint me."
            hide tekrok normal with moveoutright
            show sabiaemo closed2 at left
            s "To do all that, I'm going to need to get in contact with a human merchant somehow. Well, that was already on my list of things to do, so now is as good a time as any."
            jump upperorccamp
        if orcalliance == "tekrok":
            menu:
                "Talk to Tekrok":
                    call sabiabase
                    show tekrok normal at right
                    menu:
                        "Are we ready for the Horned God's Night?" if arenatime <= 0:
                            if vehlislocationquest < 3:
                                t "No! Get your act together and find me a human merchant!"
                                jump tekroktent2
                            if huntedwhitehind == False:
                                t "You'd better bring down a white hind, or Tekrok can't have you at his feast."
                                jump tekroktent2
                            if bargroping == 5:
                                t "No! Take care of this accusation against you, we can't have anything distracting from the Horned God's Night!"
                                jump tekroktent2
                            t "Hmm... yes, the feast is prepared. But are you ready?"
                            menu:
                                "Yes":
                                    t "Good. We have much to discuss regarding your exact role..."
                                    jump HGNtekrok
                                "Not yet":
                                    t "Then why are you talking to me? Go work!"
                                    jump tekroktent2
                        "What are you going to do after the trial?" if (arenatime <= 0 and recruitmentopened == False):
                            t "Tekrok wants to tear out Rokgrid's throat, but that is impossible. No. Tekrok will wait and gain strength for the perfect time to strike."
                            t "Rokgrid will no doubt try new tricks. We must watch, so that Tekrok can eliminate him when the time comes."
                            t "Do well, and Tekrok will support you in your revenge."
                        "Any advice about the catgirl incident?" if (catgirlraidquest == True and catgirlraidtekrok == False):
                            $ catgirlraidtekrok = True
                            $ catgirlraidinvestigation += 2
                            t "They have stolen our sacred steel! This cannot be allowed to stand."
                            s "Will you be able to catch them, though?"
                            t "Tekrok is not sure. They have often slipped away from us in the past."
                            t "If you are able to assist us in this, many will respect you more. You should do so, Tekrok will help to spite Rokgrid."
                            s "Hmm..."
                        "What kind of alcohol do your warriors like?" if (arenatime <= 0 and recruitmentopened == False):
                            t "Beer, and a hell of a lot of it. Doesn't matter who makes it."
                        "Any objectives for the Red God's Arena?" if (arenatime > 0 and recruitmentopened == False):
                            t "Warriors are on their own. Tekrok will say if he needs you."
                        "Any suggestions for the Red God's Arena?" if (arenatime > 0 and recruitmentopened == False):
                            t "Go into matches fully rested or your puny human body will not be able to keep up."
                        "Nothing":
                            pass
                    jump tekroktent2
                "Go back":
                    jump upperorccamp
    else:
        menu:
            "Talk to Tekrok":
                call sabiabase
                show tekrok normal at right
                menu:
                    "What are you going to do after the trial?" if recruitmentopened == False:
                        t "Tekrok wants to tear out Rokgrid's throat, but that is impossible. No. Tekrok will wait and gain strength for the perfect time to strike."
                        t "Rokgrid will no doubt try new tricks. We must watch, so that Tekrok can eliminate him when the time comes."
                        t "Do well, and Tekrok will support you in your revenge."
                    "Any advice about the catgirl incident?" if (catgirlraidquest == True and catgirlraidtekrok == False):
                        $ catgirlraidtekrok = True
                        $ catgirlraidinvestigation += 2
                        t "They have stolen our sacred steel! This cannot be allowed to stand."
                        s "Will you be able to catch them, though?"
                        t "Tekrok is not sure. They have often slipped away from us in the past."
                        t "If you are able to assist us in this, many will respect you more. You should do so, Tekrok will help to spite Rokgrid."
                        s "Hmm..."
                    "Nothing":
                        pass
                jump tekroktent2
            "Go back":
                jump upperorccamp
    jump upperorccamp


label rokgridtent2:
    $ renpy.block_rollback()
    scene bg rokgridtent
    if rokgridblock:
        s "(It's clear I'm not welcome in Rokgrid's tent anymore.)"
        jump upperorccamp
    if showedevidence == True:
        s "After what I did, I'd better stay the hell away from Rokgrid."
        jump upperorccamp
    if A_rokgrid < 1:
        s "I'm not on the best of terms with Rokgrid, I'd better stay away."
        jump upperorccamp
    if (orcalliance == "rokgrid" and recruitmentopened == True and rokgridfakeraidquest == False):
        call rokgridraidintro
        jump upperorccamp
    if (orcalliance == "rokgrid" and rokgridraiddone == True and rokgridraidaftermathdone == False):
        call rokgridraidaftermath
        jump upperorccamp
    if (orcalliance == "rokgrid" and orcfestivalquest == False and arenatime <= 0):
        $ orcfestivalquest = True
        call sabiabase
        show rokgrid happy2 at right
        r "Sabia! An auspicious time is almost upon us!"
        s "I heard - the Horned God's Night, isn't it?"
        r "Ah, it seems you have already heard! Yes, it is quite an important night... not only for all orcs, but for our potential alliance as well."
        if rokgridalliance:
            s "That's why I'm here. If I help you with this, does that make our alliance permanent?"
            r "Of course, I would have done my utmost to assist you regardless... but yes, this will be quite a boon to our joint efforts."
        else:
            s "That's why I'm here. I know we haven't always seen eye-to-eye, but I think it's for the best if we throw our efforts together."
            r "Then this feast will mark the beginning of a true alliance between us as well! Truly, a joyous occasion!"
        r "Of course, I hope you know that the Horned God's Night is a competition among factions. We must do a great deal of work to ensure that ours is by far the finest!"
        s "I figured as much. But what exactly matters for an orc festival like this?"
        r "The better question is: what is our goal for the festival? All of us mean to project an image of strength, of course, but what other messages are we sending?"
        r "For me, I desire to show a glorious future for our tribe! That means that we must have the finest tent, fine dining knives, wondrous foods, and so on! And that is just where you can come in."
        s "You need me to get the more exotic stuff from a human merchant, huh? I'll see what I can do."
        if A_rokgrid >= 7:
            $ Inventory.add_item(Furnishings)
            r "One thing you do {i}not{/i} need to acquire are furnishings for the feast. Thanks to your assistance in many matters, I already have those."
        r "Of course, if you can acquire more food, or alcohol, or other necessary ingredients, it will be very helpful as well."
        r "Traditionally, each warrior must bring a special dish. Deer is preferred, but in your case... I think you should try to hunt a white hind. They're quite rare, but they can be found in the forests surrounding the camp."
        r "We must also create a shrine to the Horned God - I will handle the construction, but you should bring a set of antlers to join it, to seal our alliance."
        s "Human goods, a white hind, antlers. Got it."
        r "Always so business-like! I'm glad you're on my side!"
        hide rokgrid happy2 with moveoutright
        show sabiaemo closed2 at left
        s "To do all that, I'm going to need to get in contact with a human merchant somehow. Well, that was already on my list of things to do, so now is as good a time as any."
        jump upperorccamp
    if orcalliance == "rokgrid":
        call sabiabase
        show rokgrid happy2 at right
        menu:
            "Spend some personal time with Rokgrid" if (rokgridsexunlocked == True and captaincooldown == False):
                $ captaincooldown = True
                "Sabia gave Rokgrid a coy smile."
                s "It doesn't look like you're very busy, are you?"
                r "Ah... no..."
                s "In that case..."
                "The two of them sat together and talked about their plans as well as lighter subjects, having a few drinks along the way. As the conversation went on, Sabia found them drifting closer together..."
                call rokgridraidsex
            "Spend some personal time with Rokgrid" if (gotrokgridfood == True and rokgridfoodunlocked == True and captaincooldown == False and rokgridsexunlocked == False):
                $ captaincooldown = True
                $ rokgridsexunlocked = True
                $ A_rokgrid += 2
                "When Sabia entered bearing the human wine and food she'd purchased, Rokgrid's eyes lit up. He had been in the middle of something else with some orcs, but he brushed them aside so they could be alone."
                "That was when Sabia knew that she had him. She wasn't just an ally to him anymore, he was in love with her. That was something she could definitely use."
                "They chatted casually over the meal, and when Rokgrid reached out his hand to touch hers, Sabia didn't pull back. She knew where this was going, it was just a question of how she intended to handle things..."
                call rokgridraidsex
                "Afterward, Sabia reflected that she had probably done enough to make Rokgrid loyal. His longing for her would do the rest, for the most part."
                "He wasn't a bad fuck, though, and much better than the average orc. Maybe this could happen again..."
            "Are we ready for the Horned God's Night?" if arenatime <= 0:
                if vehlislocationquest < 3:
                    r "No... we still need an edge, some human flair that no other feast will possess. Please, do see if you can arrange something of the sort!"
                    jump rokgridtent2
                if huntedwhitehind == False:
                    r "Can you try to bring down a white hind for the feast? It would really do a great deal for your reputation."
                    jump rokgridtent2
                if bargroping == 5:
                    r "Perhaps we could be ready, but I heard there's an investigation. You'll want to take care of that before the Horned God's Night."
                    jump rokgridtent2
                r "Yes, I think we have done enough that we could have a good feast. Are we ready?"
                menu:
                    "Yes":
                        r "Wonderful! In that case, let us discuss some of the finer details as we wait..."
                        jump HGNrokgrid
                    "Not yet":
                        r "Of course. We will not get another chance, so prepare as much as possible."
                        jump rokgridtent2
            "What are you going to do after the trial?" if recruitmentopened == False:
                r "My struggle against Tekrok's brutality will continue, of course. Only one of us can lead this tribe."
                r "But the fact is that the balance has been upset. We will be struggling to gain an edge over the other as incidents occur."
                r "If you attain anything like what you hope, then you will likely bring matters to a head. I will stay defensive, gaining strength for that inevitable conflict."
                r "In the meantime, I will support you as I can. And if I do become the next Warchief, I will help you with your revenge."
            "What kind of alcohol do your warriors like?" if (arenatime > 0 and recruitmentopened == False):
                r "Well, honestly, most of them just want to drink. But I supply them with plenty of our own beer - what they'd really like to try is foreign wine."
            "Any objectives for the Red God's Arena?" if (arenatime > 0 and recruitmentopened == False):
                r "Oh, don't worry about me! Just do your best and we can talk about plans later."
            "Any suggestions for the Red God's Arena?" if (arenatime > 0 and recruitmentopened == False):
                r "It's not just fights, you know! Be alert for all resources and opportunities available to you."
            "Go back":
                jump upperorccamp
    else:
        menu:
            "Talk to Rokgrid":
                call sabiabase
                show rokgrid happy2 at right
                menu:
                    "What are you going to do after the trial?" if recruitmentopened == False:
                        r "My struggle against Tekrok's brutality will continue, of course. Only one of us can lead this tribe."
                        r "But the fact is that the balance has been upset. We will be struggling to gain an edge over the other as incidents occur."
                        r "If you attain anything like what you hope, then you will likely bring matters to a head. I will stay defensive, gaining strength for that inevitable conflict."
                        r "In the meantime, I will support you as I can. And if I do become the next Warchief, I will help you with your revenge."
                    "Any advice about the catgirl incident?" if (catgirlraidquest == True and catgirlraidrokgrid == False):
                        $ catgirlraidrokgrid = True
                        $ catgirlraidinvestigation += 2
                        r "Random chance has given you an opportunity to take steps toward your goal in multiple ways! You've heard of the theft of the steel shipment, I assume?"
                        s "Yeah, I know a little. The details seem unclear, though."
                        r "That is not by accident. The loss is very shameful for the orcs involved, so they are trying to skew the facts to blame others."
                        s "I see. But how does this help me?"
                        r "If you can do something to catch those responsible, you gain status in our tribe, acquire valuable resources, and scout the area all in one stroke!"
                        r "But I strongly recommend you do your research first. Those catgirls can be tricky, and if you go charging off after them without a plan, you're sure to fail."
                        s "I'll see what I can do."
                        show rokgrid happy3
                        r "I will offer you my support in this endeavor!"
                    "Nothing":
                        pass
                jump rokgridtent2
            "Go back":
                jump upperorccamp
    jump upperorccamp


label dajrabtent2:
    scene bg dajrabtent
    $ renpy.block_rollback()
    if dajrabblock:
        s "(It's clear I'm not welcome in Dajrab's tent anymore.)"
        jump upperorccamp
    if (orcalliance == "dajrab" and recruitmentopened == True and dajrabraidintroduced == False):
        call dajrabraidintro
        jump upperorccamp
    if (orcalliance == "dajrab" and dajrabcaravanfinished == True and dajrabraidaftermathscene == False):
        call dajrabraidaftermath
        jump upperorccamp
    if orcalliance == "dajrab":
        if (orcalliance == "dajrab" and orcfestivalquest == False and arenatime <= 0):
            call sabiabase
            show dajrab normalclosed at right
            d "Sabia. What brings you here?"
            if dajrabtookmoney:
                $ A_dajrab -= 3
                $ dajrabblock = True
                s "I heard about the Horned God's Night. Are you going to host feast? Could I... help you?"
                d "I'm afraid not."
                show sabiaemo surprised1 at left
                s "Wait, you're just refusing me?"
                d "That is correct. Please leave."
                jump dajrabtent2
            if dajraberrand > 4:
                s "I heard about the Horned God's Night. Are we going to be hosting a feast, or are you sitting out of that as well?"
                d "Ah, so you are serious about our alliance. Good."
            else:
                s "I heard about the Horned God's Night. Are you going to host a feast? Could I... help you?"
                d "You did not seem so interested in working together before. What has changed your mind now?"
            $ orcfestivalquest = True
            d "In any case, yes, I must host a feast. It is a challenge for dominance, but it is not only that. Many will host smaller feasts in order to prove their strength to their peers."
            d "For me to sit back on the Horned God's Night would be for me to surrender all influence on the tribe. And that has never been my intention."
            s "Alright, then. If I'm going to help your feast be the best, what do you need from me?"
            d "Of course, your primary motive is to advance your own prestige."
            s "I ju-"
            d "It was not a condemnation, only a statement. What I was going to say is that you must seek not just to contribute to the feast, but to contribute in a spectacular way that will draw attention."
            d "You should, of course, bring food and alcohol, as many warriors will. But if you want to be remembered as a significant partner in the feast, you will need something more memorable."
            s "So not something just any orc would bring... think the warriors would be interested in human goods?"
            d "That would be a fine way to go about it, yes. Many orcs prefer strong wine, since it is different from what we brew ourselves."
            d "Every feast must also create an altar of antlers to the Horned God. I have made the necessary preparations for this, but I could include a set of antlers if you wish to gain more prestige in that way."
            s "Sure, I think I get it. Is that all?"
            d "No, there is another thing I must insist upon. Each warrior who participates in a major feast traditionally brings an offering of meat. The rarer the catch, the greater the honor."
            d "You are respected here, but you cannot rest. Simpler antlers would help, but they are not enough - I suggest you bring down the highest prey, a white hind."
            s "That's a rare animal, but I'll try. Anything else?"
            if A_dajrab >= 3:
                $ Inventory.add_item(Furnishings)
                d "Since you have assisted me in multiple ways, I have already acquired furnishings. We have no need for more."
            d "No doubt there will be complications for the event itself. Do all that you can to prepare."
            hide dajrab normalclosed with moveoutright
            show sabiaemo closed2 at left
            s "To do all that, I'm going to need to get in contact with a human merchant somehow. Well, that was already on my list of things to do, so now is as good a time as any."
            jump upperorccamp
        if orcalliance == "dajrab":
            call sabiabase
            show dajrab normalclosed at right
            menu:
                "Can you help me prepare for Kentark training?" if kentarktraining > 1 and kentarkdajrab == False:
                    $ kentarkdajrab = True
                    $ kentarktraining += 30
                    d "Oh? You are attempting it with Lutvrog, I presume?"
                    s "That's right."
                    d "Hmm. In light of our alliance, I'm willing to help you out a little."
                    "Though he called it a little help, Dajrab gave Sabia a huge amount of advice, knowledge of herbs, and suggestions for physical training."
                    "By the time they finished, Sabia's head was spinning, but she felt far more prepared for her Kentark training."
                "Are we ready for the Horned God's Night?" if arenatime <= 0:
                    if vehlislocationquest < 3:
                        d "We are not. Perhaps you could use the time to get in contact with a broader selection of merchants?"
                        jump dajrabtent2
                    if huntedwhitehind == False:
                        d "If you want this to go well, your offering should be nothing less than a white hind."
                        jump dajrabtent2
                    if bargroping == 5:
                        d "First, you should clear up the matter of the investigation against you."
                        jump dajrabtent2
                    d "Enough for a sufficient feast, yes. Are you ready?"
                    menu:
                        "Yes":
                            d "Good. I will handle the details, so rest and prepare yourself for the feast..."
                            jump HGNdajrab
                        "Not yet":
                            d "More can always be done. But if there was ever a time to be thorough, it is now."
                            jump dajrabtent2
                "What are you going to do after the trial?" if arenatime <= 0:
                    d "With such business over, it is time for a period of renewal. First, the Horned God's Night, and after that, the test of arms in the arena."
                    d "It is during this time that Tekrok and Rokgrid will make their moves and try to position themselves to seize leadership. Likewise, I must show myself to the tribe."
                    d "As for specific plans... if you continue being a stalwart ally, we will discus them in greater depth later."
                    jump dajrabtent2
                "What kind of alcohol do your warriors like?" if (arenatime <= 0 and recruitmentopened == False):
                    d "Most of those who follow me prefer a variety. For the feast, perhaps something a little sweeter than usual?"
                    jump dajrabtent2
                "Any objectives for the Red God's Arena?" if (arenatime > 0 and recruitmentopened == False):
                    d "Other than one melee, politics plays less of a role. Focus on yourself and do as well as you can."
                "Any suggestions for the Red God's Arena?" if (arenatime > 0 and recruitmentopened == False):
                    d "You will find the final day most difficult, but you will be allowed to use more equipment. Bring a variety and use it well."
                "Go back":
                    jump upperorccamp
    else:
        menu:
            "Talk to Dajrab":
                call sabiabase
                show dajrab normalclosed at right
                menu:
                    "What are you going to do after the trial?" if recruitmentopened == False:
                        d "The same thing I did before the trial."
                        s "..."
                        show sabiaemo pout3 at left
                        s "Seriously? That's all you're gonna say?"
                    "Any advice about the catgirl incident?" if (catgirlraidquest == True and catgirlraiddajrab == False):
                        $ catgirlraiddajrab = True
                        if dajrabtookmoney:
                            d "I have none."
                            show sabiaemo angry1 at left
                            s "Bastard..."
                        else:
                            $ catgirlraidinvestigation += 2
                            d "...perhaps I do. The tribe will soon launch several attempts to steal the metal back, or at least punish some catgirls. They want glory, but they will be unsuccessful."
                            s "You have something else in mind?"
                            d "Their attempts will be watched by those who conducted the raid. Perhaps someone could take advantage of that fact?"
                            show sabiaemo happy2 at left
                            s "I get what you mean. Thanks, Dajrab!"
                    "Nothing":
                        jump dajrabtent2
                jump dajrabtent2
            "Go back":
                jump upperorccamp
    jump upperorccamp


label tradinglodge2:
    scene bg tradinglodge
    $ renpy.block_rollback()
    if tradinglodgeintro == False:
        $ tradinglodgeintro = True
        "Sabia walked into the large building and to her surprise, was completely ignored. Elsewhere in camp she got plenty of stares, but here, everyone seemed too busy to care about her."
        "Though not nearly as busy as any market in Lundar, the trading lodge was filled with purposeful activity. Most of it seemed to be based on basic supplies like furs, but there were a few merchants selling weapons and armor as well."
        "Since there didn't seem to be any limits on her movement, Sabia began to browse the stores."
    menu:
        "Purchase equipment":
            call openshop (Orcequipmentshop)
            if Inventory.has_item(Rustysword) > 0:
                $ gotanysword = True
        "Purchase clothing":
            call openshop (Orcclothshop)
        "Purchase general goods":
            call openshop (Orcgeneralshop)
        "Purchase human food" if (rokgridfoodunlocked == True and gotrokgridfood == False):
            s "(They do sell some human food here, though for high prices... I should buy some to help seduce Rokgrid.)"
            menu:
                "Purchase (75 Lundils)":
                    if money >= 75:
                        $ money -= 75
                        $ gotrokgridfood = True
                        "Sabia purchased enough human foods and wine for two, then secreted them away for use on Rokgrid."
                    else:
                        "Sabia didn't have enough money."
                "Not now":
                    pass
            jump tradinglodge2
        "Purchase food" if (gotHGNfood2 == False and orcalliance == "sabia" and orcfestivalquest == True):
            "If she was going to host her own feast, Sabia realized that she needed a substantial amount of food. She couldn't afford for all of it to be high class fare, so she needed to buy some standard orc food."
            "After searching through all the available merchants, Sabia found one that was able to supply a large amount of food that didn't immediately turn her stomach, for a price she was willing to accept."
            menu:
                "Purchase (325 Lundils)":
                    if money >= 325:
                        $ money -= 325
                        $ gotHGNfood2 = True
                        "Sabia purchased a large supply of the food and arranged to have it brought to her feast on the Horned God's Night."
                    else:
                        "Sabia didn't have enough money."
                "Not now":
                    pass
            jump tradinglodge2
        "Investigate orc smith":
            "The orc working on supplies didn't look like he had much talent, so Sabia doubted he could do anything for her, but she investigated him anyway."
            call SUorcsmith
            jump tradinglodge2
        "Investigate suspicious orc" if kentarktraining >= 1:
            call sabiabase
            show orcbase at right
            show orcloincloth at right
            show orcbeard2 at right
            show orcwrap at right
            show orcemo normal at right
            with dissolve
            if kentarkstoreintro == False:
                $ kentarkstoreintro = True
                "Sabia noticed an orc sitting in the shadows near the merchants, but clearly not one of them judging from his large cloak. When she approached, he gave her a suspicious look and shifted further into the shadows as if avoiding her gaze."
                orc "Me hear you're aiming to become a Kentark."
                s "That's true. What's it to you?"
                show orcemo smile1 at right
                orc "Me have some old orc scrolls for sale that speak of Kentark training. I could sell them to you for a small fee, and translate them fo-"
                s "I can read your script."
                show orcemo angry at right
                "That caused a sour expression on the orc's face, but he nodded acceptance and reached into his cloak for his wares."
            if kentarkstore1 == True and kentarkstore2 == True:
                "Sabia noted the suspicious orc but didn't think he had anything else useful to her for the time being."
                jump tradinglodge2
            "The orc slid the scrolls onto the table surreptitiously and raised an eyebrow at her without a word."
            menu:
                "Purchase old scroll (250 Lundils)" if kentarkstore1 == False:
                    if money < 250:
                        "Sabia didn't have enough money."
                    else:
                        $ kentarkstore1 = True
                        $ kentarktraining += 20
                        $ money -= 250
                        "The scroll didn't look like much, but Sabia purchased it and took it aside to read."
                        "To her surprise, the script had a lot of interesting things to say. Rather blunt, but more thoughtful about combat and herb lore than she would have expected."
                        "By the time she finished, Sabia felt that she had learned several significant things about Kentark training."
                "Purchase new scroll (1000 Lundils)" if kentarkstore2 == False:
                    if money < 1000:
                        "Sabia didn't have enough money."
                    else:
                        $ kentarkstore2 = True
                        $ kentarktraining += 10
                        $ money -= 1000
                        "The scroll seemed nice and new... suspiciously so. Sabia took it aside to read and quickly confirmed her suspicions."
                        "Though it had a few useful things to say, she felt as though it had probably been written recently based on other rumors, not by someone who was actually a Kentark. Perhaps by the orc himself, looking to scam her out of her Lundils."
                        "But since it had taken her a little closer to her goal, Sabia decided that she could accept it."
                "Nothing":
                    "Deciding against a purchase, Sabia left the man alone."
            jump tradinglodge2
        "Look for work" if tradinglodgejob == False:
            $ tradinglodgejob = True
            call sabiabase
            show orcbase at right
            show orcloincloth at right
            show orcbeard1 at right
            show orcnecklace at right
            show orcwrap at right
            show orcemo normal at right
            with dissolve
            "Sabia approached the table that seemed to be the hub of the trading lodge. There were several signs on it, including ones offering jobs for cleaning, but Sabia ignored those, instead focusing on the orc behind the table."
            s "I'm looking for work. Something meaningful, not picking up trash."
            orc "Uh... want help merchants?"
            s "Not if you mean just lugging boxes around."
            orc "No, help organize. Irritating thing, orcs no like. Maybe human females are good for this."
            "Well, it sounded better than the alternatives she'd been contemplating not too long ago. Besides, it got at her true goal: figuring out exactly how the orc camp worked economically. That could be very important if she intended to manipulate them in the future."
            "Sabia put her name on a list - her calligraphy looked absurd next to the scrawls or just x marks - and the orc showed her some of the local orc merchants. It seemed like she had her work cut out for her."
            "Next time she visits the local merchants store, she can work for them."
            $ Orcequipmentshop.payment = [5,8]
            $ Orcclothshop.payment = [3,6]
            $ Orcgeneralshop.payment = [1,11]
            jump tradinglodge2
        "Talk to Alioch" if vehlislocationquest == 3:
            call sabiabase
            show alioch happy at right
            if aliochintroduction == False:
                $ aliochintroduction = True
                "Sabia spotted Vehlis' slave at a table in the trading lodge, apparently conducting business despite being surrounded by orcs. He was well-built, but looked rather small compared to the hulking warriors around him."
                show alioch sad at right
                "As Sabia watched, one of the orcs bumped into him. Alioch rocked backward, but only lowered his head when the orc glared at him. The orc was clearly at fault, not that it was going to matter."
                "Though Sabia didn't care if they bullied some elven slave, he did serve Vehlis. Perhaps it would be wise to intercede on his behalf?"
                menu:
                    "Do nothing":
                        "Sabia merely waited until the conflict ended, the orc spitting into Alioch's face and stomping away. The elven slave stopped for a moment, wiped the spit off with a sigh, then went back to work."
                        "She'd come to expect such spinelessness from elves, but at least he went back to being productive. Sabia approached his table to see what he had to sell."
                    "Interrupt":
                        $ L_orcs -= 1
                        $ A_vehlis += 2
                        show sabiaemo angry1 at left
                        s "Get out of the way! I have shit to buy!"
                        "The orc turned to glower at her, but she stared back into his eyes without flinching."
                        s "We all need to get ready for the Horned God's Night. You want to be the one explaining why the supplies we need are late?"
                        show alioch happy at right
                        "Cursing under his breath, the warrior wandered off. Alioch gave her a grateful smile and a slight bow."
                show sabiaemo normal at left
                s "You're Alioch, right? Vehlis has you working here?"
                show alioch happy at right
                alioch "That's correct. As a representative of the Bank, Mistress Vehlis does not waste her time with simple mercantile activities. The deals that she negotiates are generally delegated to me."
                s "So you're the one I need to talk to about supplies for the feast?"
                alioch "I'll provide anything I can, though obviously our supplies are limited. If you want quality equipment or foreign items, you'll have to wait for the Mistress to finish her dealings."
                s "That's fine, I think we don't need much fancy for now."
                alioch "Then please feel free to speak with me if you desire to buy anything."
                jump tradinglodge2
            if maply_hellhound_quest == 4:
                $ maply_hellhound_quest += 1
                jump maply_hellhound_quest4
            else:
                alioch "Is there something I can do to help you?"
                menu tradinglodge2_alioch:
                    "I'm here to make purchases":
                        call openshop (Aliochshop)
                        jump tradinglodge2
                    "What's it like being a slave?":
                        alioch "I couldn't tell you."
                        show sabiaemo surprised1 at left
                        s "Huh?"
                        show sabiaemo irritated2 at left
                        s "Oh, this is one of those fine distinctions you Carchedonese like to stress, isn't it?"
                        alioch "It's not a trivial difference. As a \"servant\" I have certain rights that no \"slave\" - in Carchedon or Lundar - possesses."
                        show sabiaemo normal at left
                        s "Would any of those really stop Vehlis if she wanted to hurt you?"
                        show alioch eyebrow1 at right
                        alioch "Lundar has laws against murder, does that prevent murders?"
                        show sabiaemo happy1 at left
                        s "Heh, fair enough. You're pretty sharp, and apparently a man of many talents... I should have guessed Vehlis wouldn't own a low quality slave."
                        show alioch eyebrow2 at right
                        alioch "You could say that Mistress Vehlis likes nice things."
                    "What do you think of your mistress?" if aliochvehlissecret == False:
                        $ aliochvehlissecret = True
                        show alioch normal at right
                        alioch "Mistress Vehlis treats everyone fairly, including her slaves and servants."
                        show sabiaemo annoyed2 at left
                        s "Oh, come on. Tell me what you really think."
                        alioch "..."
                        show alioch sad at right
                        alioch "As you can imagine, Vehlis demands the utmost of everyone, including herself. In fact, I think I've seen her express weakness or personal sentiment only once..."
                        show sabiaemo irritated1 at left
                        s "When?"
                        show alioch eyebrow1 at right
                        alioch "When she told me what to say when people came asking around about her weaknesses."
                        show sabiaemo irritated1 at left
                        s "Dammit, I should have known it wouldn't be easy to get anything on her."
                        show alioch happy at right
                        alioch "Haha, my apologies."
                        show sabiaemo irritated1 at left
                        s "Did she really command you to snark at people investigating her, though?"
                        alioch "No. If you were an enemy, I would have fed you believable lies. Since you are likely to be an ally..."
                        show sabiaemo happy3 at left
                        s "Fair enough, I won't try again. I do hope we'll end up being allies, though."
                        alioch "As do I."
                    "Would you attend my feast?" if arenatime < 1:
                        alioch "Apologies, but I will have multiple duties during the event. You will find me running Mistress Vehlis's supply tents, if you need me for anything."
                    "What's going on with Maply?" if (recruitmentopened == True and nevekiaprogression == 1):
                        $ nevekiaprogression = 2
                        show alioch happy at right
                        alioch "I'm fucking that sweet catgirl ass."
                        show sabiaemo surprised1 at left
                        s "You..."
                        show sabiaemo irritated1 at left
                        s "Wait, you're not serious, are you?"
                        show alioch eyebrow1 at right
                        alioch "God, no - young and naive women are not my type. She came to me for advice, hoping that I would keep her secret better than fellow catgirls."
                        show sabiaemo closed2 at left
                        s "Advice? I know this is supposed to be a secret, but if it's relevant to me..."
                        show alioch happy at right
                        alioch "Heh, it actually isn't much of a secret. It's obvious to anyone with eyes that Maply has a crush on Neve, but she's not sure what to do with it."
                        show sabiaemo irritated1 at left
                        s "Seriously? That's what this is all about?"
                        show alioch normal at right
                        alioch "I've been encouraging her to work up her courage and just talk to Neve, but she won't take the leap. I think she only needs a little nudge..."
                        show sabiaemo closed2 at left
                        s "..."
                    "Do you have anything unusual for sale?" if (recruitmentopened == True and kiaquestalioch == False):
                        alioch "As a matter of fact, yes. One of the warriors from the Arena has already drank away his winnings. He pawned off the Makhor bone he won... you interested?"
                        if kiaprogression >= 7:
                            s "Yes, perhaps... what does it cost?"
                            alioch "100 Lundils."
                            menu:
                                "Purchase (100 Lundils)":
                                    if money >= 100:
                                        $ money -= 100
                                        $ kiaquestalioch = True
                                        $ kiabones += 1
                                        $ Inventory.add_item(Makhorbones,1)
                                        alioch "Then it's yours!"
                                        s "(Kia should appreciate this.)"
                                    else:
                                        s "(I don't have enough.)"
                                "Not now":
                                    alioch "It won't stay here forever - Vehlis could sell it for a greater profit when she departs on another trip."
                        else:
                            s "Thanks for letting me know, but I'm not sure what the point would be."
                    "Nothing":
                        alioch "Of course. Let me know if I can ever be of service."
                        jump tradinglodge2
                jump tradinglodge2_alioch
        "Eavesdrop on random orcs":
            $ tempnum = renpy.random.randint(1,7)
            if orcgossip1catgirls == False:
                $ orcgossip1catgirls = True
                $ catgirlraidinvestigation += 1
                "First Orc" "You think the catgirls really knew the shipment was coming from the mine?"
                "Second Orc" "Whaddya mean?"
                "First Orc" "How the fuck are they gonna get in here? Who's gonna spy for them? Nah, me think they just guessed until they got it right."
                "Second Orc" "Yeah, me bet. Just like those mangy scavengers..."
                s "Hmm..."
                jump tradinglodge2
            if tempnum == 1:
                if vehlislocationquest == 3:
                    "First Orc" "Fuck yeah, the huge tits lady is back."
                    "Second Orc" "Me heard she barely came back. Don't offend her."
                    "First Orc" "But of course we only get stupid elf slave here..."
                else:
                    "First Orc" "Where's that human with the huge tits?"
                    "Second Orc" "Went back to human lands to negotiate new things, me think."
                    "First Orc" "Dammit, me wanted to have something to watch while me worked. Wouldn't mind fucking her, either."
                    "Second Orc" "Don't be an idiot. You think someone from the Bank is gonna let you touch her?"
                    "First Orc" "Me know, me know..."
            if tempnum == 2:
                if trialoutcome == "tekrok":
                    "First Orc" "Warchief sure smacked down Tekrok. He needs to stop bringing up this feud with Rokgrid."
                    "Second Orc" "Yeah, but he always does. That what they do."
                    "First Orc" "That's all Tekrok does, though. Gonna bring Lundar down on our asses..."
                else:
                    "First Orc" "Damn. Rokgrid probably did it, but he got off..."
                    "Second Orc" "Yeah, but we knew no captain wuz gonna get killed. They too tough."
                    "First Orc" "He's still a human-loving bastard..."
            if tempnum == 3:
                "First Orc" "These furs are worth twice that. Fuck your offer!"
                "Second Orc" "Fuck {i}you{/i}!"
                "First Orc" "No, fuck {i}you{/i}!"
                "Second Orc" "No, fuck YOU!"
                "First Orc" "FUCK, FUCK YOU!"
                call sabiabase
                show sabiaemo pout3 at left
                s "..."
            if tempnum == 4:
                if recruitmentopened:
                    "First Orc" "Finally got a proper Red God's Arena..."
                    "Second Orc" "The Captains better not fuck it up. We need a good year."
                else:
                    if arenatime < 1:
                        "First Orc" "They ever gonna open the real arena again?"
                        "Second Orc" "Maybe so, now that the damn trial is over."
                        "First Orc" "What a waste of time THAT was."
                        "Second Orc" "What, better than getting your ass kicked by Lutvrog?"
                        "First Orc" "Shuddup. I'll win one day..."
                    else:
                        "First Orc" "Hell yes, they finally reopened the Red God's Arena! Me told you!"
                        "Second Orc" "Like it matters for scrubs like us. Fucking Sabia has a better chance at a tree."
            if tempnum == 5:
                "Merchant Orc" "Fucking tentacles ate the whole thing... dammit..."
            if tempnum == 6:
                "First Orc" "Heard the hellhounds ain't doin' so well."
                "Second Orc" "Idiot! Don't talk about that here!"
            if tempnum == 7:
                if kulganalive:
                    "First Orc" "Me thought they execute Kulgan for a bit."
                    "Second Orc" "Me not worried. Is good warrior, know is innocent."
                    "First Orc" "No... damn captains almost killed him. If Sabia not say innocent..."
                    "Second Orc" "She's not bad for a human female..."
                else:
                    "First Orc" "Still can't believe they executed Kulgan."
                    "Second Orc" "You think he did it?"
                    "First Orc" "Hell no! We lost a good orc..."

            jump tradinglodge2
        "Go back":
            jump upperorccamp
    jump upperorccamp


label orctents2:
    $ renpy.block_rollback()
    scene bg orctents
    if raidquest == 2:
        menu:
            "Meet the orcs blocking the training grounds":
                call raidquest3
                jump upperorccamp
            "Just pass through":
                pass
    if L_orcs >= 20:
        "Walking through the orc tents had become strange, as most of the orcs gave her respectful nods. Part of Sabia was a little proud, and part of her wondered what the hell had become of her life."
    elif L_orcs >= 15:
        "As Sabia went through the tents, most of the orcs gave her the greatest respect: they ignored her. Other than a few that nodded to her, one warrior to another, they let her go on her way."
    elif L_orcs >= 10:
        "When Sabia wandered through the tents, she was surprised by the responses. Though a few orcs glowered or leered, many more gave her respectful nods."
    elif L_orcs >= 5:
        "A few orcs nodded at Sabia begrudgingly. After a while in the tents, she decided it would be better to leave."
    else:
        "The orcs glared at Sabia in undisguised hostility and she beat a hasty retreat."
    if bargroping == 5 and murderinvshamanhint == True and murderinvshamanevidence == False:
        $ bargropeinv += 2
        $ murderinvshamanevidence = True
        s "(Hmm... I believe the shaman's tent is in this area... I should go investigate...)"
        "Managing to avoid too many prying eyes, Sabia returned that night, when the shaman was busy with a public ritual. She managed to sneak inside his tent without being seen."
        "It mostly held charms and ingredients for his rituals, though he did have a number of fine goblets and hangings that surprised Sabia. Apparently shamans had more of a taste for wealth than most orcs."
        "Eventually she found it... a box hidden beneath the shaman's bed. It contained a number of letters with rough scrawling... fortunately, Sabia was able to figure them out."
        "Apparently, the shaman was reporting on the tribe to a council of shamans. Sabia wasn't sure if that was normal or not, but the way he talked about it seemed incredibly suspect."
        "Finally she stumbled upon what she needed: the shaman talking about her. He made it explicit that he was hoping to remove her and regain control in the tribe. It couldn't get much more suspicious than that - Sabia stole the relevant sheet and replaced everything else as it was."
        "He'd suspect that she'd stolen it, of course, but that didn't matter. They were already mortal enemies - what mattered was avoiding his attack on her."
        "Sabia smirked and slipped away from the tents, thinking of a story to tell the investigator..."
    jump upperorccamp



label maplyinterrogation:
    menu:
        "Interrogate Maply":
            if maplysexorc == True:
                show maplyemo sad1 at right
                maply "..."
                s "(After using the orc on her, she's probably not going to give me any more information...)"
            elif A_maply >= 4:
                $ maplybefriended = True
                $ A_maply += 2
                $ L_catgirls += 1
                $ freedom += 1
                show maplyemo normal at right
                maply "I guess... you haven't been too mean. And we {i}did{/i} steal all your metal..."
                show sabiaemo happy1 at left
                s "If we get it back, the orcs will calm down and won't try to kill or eat you. Can you help us with that, just a little?"
                show maplyemo sad1 at right
                maply "But... I don't know very much. They never tell lowly scouts like me much, in case we get caught..."
                show maplyemo happy at right
                show maplyblush at right
                maply "Eheheh, just like this, I guess!"
                show sabiaemo closed2 at left
                s "You might still be able to help. Does your caravan still have the metal, or did you sell it off?"
                show maplyemo normal at right
                hide maplyblush
                maply "Oh, there's no way we sold it! For something that valuable, you hafta lie low, move far away, {i}then{/i} sell it!"
                show sabiaemo normal at left
                s "So it's with the caravan... do you know where the caravan is?"
                show maplyemo sad1 at right
                maply "Uhh... it's gonna be hidden. They would have told me where to find it after the mission, so..."
                s "But which direction?"
                maply "...n-north..."
                show sabiaemo happy1
                s "Good! Thank you for the help, Maply!"
                show maplyemo happy at right
                maply "You'll help me now, right?"
                s "Sure, I just need to talk to the warchief!"
                show sabiaemo closed2 at left
                s "(I still have the choice to do whatever I want, of course, but I've gotten what I need from her. I should go propose a plan to Groknak.)"
            elif A_maply >=1:
                show maplyemo sad1 at right
                maply "You seem nice... but I don't want anyone else to get hurt..."
                s "(I need to work on her a little more...)"
            elif A_maply >= 0:
                show maplyemo sad1 at right
                maply "I can't tell you anything... please don't hurt me..."
                s "(Maybe if I can make her warm to me, she'll give more information.)"
            else:
                show maplyemo angry2 at right
                maply "I'll never tell you anything!"
                s "(She may have gone too far... maybe I should stop trying to convince her nicely.)"
            return
        "Talk to Maply" if (maplytalked == False and maplysexorc == False):
            $ maplytalked = True
            $ A_maply += 1
            s "Alright, let's talk."
            show maplyemo angry2 at right
            maply "I told you, I'm not telling you anything."
            s "No, I don't mean questioning you. Let's just talk, person to person."
            show maplyemo angry1 at right
            maply "..."
            show sabiaemo happy1 at left
            s "Honestly. There aren't very many women in this camp, I could really use someone to talk to."
            show maplyemo sad1 at right
            maply "..."
            show maplyemo normal at right
            show sabiaemo normal at left
            maply "Okay... I guess there's no harm in just talking a little!"
            menu:
                "Ask her about her life":
                    s "So... how did you end up raiding orcs?"
                    show maplyemo happy at right
                    maply "Who else are we going to raid, silly?"
                    s "..."
                    show maplyemo normal at right
                    maply "If we take anything from humans, they'll come after us, or worse, get armies from Lundar! There aren't any minotaurs near here and the elves don't have a lot, so..."
                    menu:
                        "You think humans retaliate worse than orcs?":
                            maply "Haha, are you sensitive about it?"
                            show sabiaemo closed2 at left
                            s "I'm just asking. The orcs are trying to murder and eat you, you know."
                            maply "Yeah, but just because they're angry. They'll get over it soon... humans never forgive you."
                        "That's nice, but I meant you personally.":
                            $ A_maply += 1
                            show maplyemo happy at right
                            maply "Oh! That's easy - I've always thought that scouting was the best part! Some people like making things or trading, but I like to run between the trees, draw in all the scents!"
                            show sabiaemo happy1 at left
                            s "I can understand that. I became a soldier for similar reasons."
                            show maplyemo eyebrows at right
                            maply "Haha, I wouldn't have expected the two of us to be similar..."
                        "So why this caravan in particular?":
                            $ A_maply -= 1
                            show maplyemo sad1 at right
                            maply "Hey... you said you weren't gonna interrogate me..."
                            s "Sorry, didn't mean to make this too serious..."
                "Stay silent":
                    $ A_maply += 1
                    if maplystripped:
                        show maplyemo sad1 at right
                        maply "So, umm... why did you have to take away my clothes?"
                        s "..."
                        menu:
                            "Because you're my prisoner.":
                                show maplyemo normalopen at right
                                maply "I don't get it... maybe it's a human thing..."
                            "I had to be sure you weren't hiding anything.":
                                show maplyemo normal at right
                                maply "Oh, okay. That makes sense!"
                            "To see your body.":
                                $ A_maply -= 1
                                show maplyemo surprise2 at right
                                maply "Wh-wh-wha?"
                                show maplyemo surprise1 at right
                                maply "I... I didn't think humans could be like that! That's... that's perverted!"
                                s "You didn't think humans could be like what, exactly?"
                                show maplyemo angry1 at right
                                maply "..."
                                s "Alright, sorry... did you have anything else you wanted to ask me?"
                    else:
                        maply "So, umm... why is a human like you working with a bunch of orcs?"
                        menu:
                            "It's part of a new alliance with Lundar.":
                                show maplyemo surprise1 at right
                                maply "Whaaaat?"
                                show sabiaemo closed2 at left
                                s "(I guess she really is naive. Maybe I can use that.)"
                            "Because I hate your kind.":
                                $ A_maply -= 1
                                show maplyemo angry1 at right
                                maply "Hey, that's mean!"
                            "Because my family betrayed me.":
                                $ A_maply += 1
                                show maplyemo sad1 at right
                                maply "Your own kin... betrayed you?"
                                show sabiaemo closed2 at left
                                s "My sister wanted to get rid of me, so she tried to get the orcs to kill me. But I've managed to make them accept me into their tribe."
                                show maplyemo happy at right
                                maply "Wowww, that's amazing!"
            show maplyemo sad1 at right
            maply "So... if you're from Lundar originally... can I ask why?"
            show sabiaemo normal at left
            s "Why? What do you mean?"
            maply "Why did you force us out? We weren't even trying to fight you or anything..."
            menu:
                "Because you were selling supplies to our enemies.":
                    maply "That's not true!"
                    maply "Well... maybe some of us did. Each caravan is different, you know? We decide things for ourselves."
                    s "And because of that, we can't know your loyalty."
                    maply "Hmmm..."
                "Because you catgirls are thieves.":
                    $ A_maply -= 1
                    $ L_catgirls -= 1
                    show maplyemo angry1 at right
                    maply "Hey, that's mean!"
                "Because the war was Lundar versus everyone else.":
                    $ A_maply += 1
                    maply "You mean... you couldn't trust us? That's what everyone says..."
                    s "Try to see it from our perspective. We had enemies on all sides, and catgirls could have been helping them - you aren't going to deny that some did, right?"
                    maply "Well... maybe some. But other caravans would have helped humans if you asked!"
                    s "Yes, but it's hard to trust anyone during a war."
                    show maplyemo eyebrows at right
                    maply "I... didn't think I could feel sad for Lundar..."
            if A_maply >= 2:
                show sabiaemo normal at left
                s "You seem like a decent person, Maply. I wish I could do more to help you."
                show maplyemo happy at right
                maply "You seem okay to me, too! I just wish you'd let me go..."
                show sabiaemo closed2 at left
                s "I'm afraid it's more complicated than that. But... I'll do what I can, if you help me a little too."
                show maplyemo sad1 at right
                maply "Uhh... I need to think..."
            else:
                show sabiaemo closed2 at left
                s "(It's obvious I'm not going to become her friend or anything. Maybe trying to talk to her was useless...)"
            return
        "Use sexual manipulation" if maplysexdone == False:
            if maplysexlook:
                s "(I need to recruit someone else for this.)"
            else:
                $ maplysexlook = True
                s "(They say that catgirls can be easily manipulated sexually... I wonder if I could get information out of her that way.)"
                show sabiaemo closed2 at left
                s "(Unfortunately, I really don't have much experience with women and I doubt I could pull it off. That's... something to think about in the future.)"
                s "(But for now... I need to find someone in camp who could do it for me. Not someone too important, though, who would try to take the credit.)"
                s "(Hmm...)"
            return
        "Use torture":
            s "(The most straightforward option would be to just torture her until she tells me what I need to know. I can cause some pain, but I'm not an expert on torture, so that will probably leave her a wreck...)"
            menu:
                "Torture Maply":
                    $ maplytortured = True
                    $ slavery += 2
                    $ L_catgirls -= 2
                    s "..."
                    show maplyemo surprise2 at right
                    maply "What... what are you doing?"
                    show sabiaemo irritated1 at left
                    s "If you're not going to talk... I'll make you talk."
                    maply "Noooo!"
                    scene bg black with dissolve
                    pause 3
                    scene bg sabiatent
                    call sabiabase
                    show sabiaemo closed2 at left
                    s "(That was cruel... but I got what I needed. She gave us a specific location, the locations of scouts, everything.)"
                    if maplysexneve:
                        $ A_neve -= 3
                        show neve1 at right
                        show neveemo irritated1 at right
                        show sabiaemo irritated1 at left
                        with moveinright
                        n "What the fuck, Sabia?"
                        s "I did what I had to do."
                        show neveemo sad at right
                        n "This poor girl... she'll probably never recover, physically or mentally."
                        show sabiaemo angry1 at left
                        s "She should have cooperated!"
                        show neveemo closed1 at right
                        n "..."
                        show neveemo irritated2 at right
                        n "I won't forget this."
                        hide neve1
                        hide neveemo irritated2
                        with moveoutright
                    show sabiaemo closed2 at left
                    s "(Alright, that's all I'm getting out of her. I should go propose a plan to Groknak.)"
                    jump sabiahq2
                "Go back":
                    jump sabiahq2
        "Strip Maply" if maplystripped == False:
            $ maplystripped = True
            $ A_maply -= 1
            s "As a captive, I don't think you deserve those clothes..."
            show maplyemo surprise2 at right
            maply "Ah, wait!"
            show maply 3n at right
            show maplyemo sad3 at right
            show maplyblush at right
            with dissolve
            maply "Nnnn... give them back..."
            jump sabiahq2
        "Return Maply's clothes" if maplystripped:
            $ maplystripped = False
            $ A_maply += 1
            s "Alright, you can have these back."
            show maplyemo normal at right
            maply "Ah... I can?"
            show maply 3 at right
            show maplyemo happy at right
            with dissolve
            maply "Mm! That's better!"
            jump sabiahq2
        "Do nothing":
            jump sabiahq2


label catgirlraidevent:
    g "So, you're serious about this."
    s "Of course I am."
    g "Technically, any warrior in the tribe may lead a raid. And you would probably have support. But traditionally, one does it under the leadership of a more important warrior."
    s "..."
    menu:
        "Give Warchief Groknak credit":
            $ A_groknak += 1
            g "Hah! Seeking to avoid conflict?"
            s "What? You're the Warchief, can anyone object?"
            g "No. It is a safe, if boring, choice. Warchief Groknak will grant official permission to this raid... if you can prove it is worth it."
            g "Give Warchief Groknak a moment to make preparations, then we can discuss the details of our strategy..."
        "Give Captain Tekrok credit":
            if rokgridalliance:
                $ A_rokgrid -= 2
                g "Hunh. And so you scorn Rokgrid. So be it."
            if tekrokalliance:
                g "Very well. Make it official with Tekrok, then we will discuss our specific plans."
                scene bg mainhall
                call sabiabase
                show tekrok happy1 at right
                with dissolve
                $ catgirlraidinvestigation += 2
                $ catgirlraidperformance += 3
                t "Not bad, human, not bad! Just what have you been doing to investigate the theft so thoroughly?"
                s "Maybe if you actually commit to this alliance, I'll tell you."
                t "Well, you have Tekrok's support. I will tell the scouts everything Tekrok's warriors have learned."
                t "Then, in the end... if we capture these catgirls, Tekrok will tell you what to do."
                s "We'll see."
            else:
                g "Very well. Make it official with Tekrok, then we will discuss our specific plans."
                scene bg mainhall
                call sabiabase
                show tekrok angry2 at right
                with dissolve
                $ A_tekrok += 2
                $ catgirlraidperformance += 1
                t "Just what are you trying to do, human?"
                s "Look, I know we're not on the best of terms. But you can take the offer and get credit for this, or you can get nothing."
                t "Hmph. If you give Tekrok gifts like this all the time, maybe Tekrok will reconsider..."
        "Give Captain Rokgrid credit":
            if tekrokalliance:
                $ A_tekrok -= 2
                g "Hunh. And so you scorn Tekrok. So be it."
            if rokgridalliance:
                g "Very well. Make it official with Rokgrid, then we will discuss our specific plans."
                scene bg mainhall
                call sabiabase
                show rokgrid happy2 at right
                with dissolve
                $ catgirlraidinvestigation += 2
                $ catgirlraidperformance += 3
                r "Ah, Sabia! I had not expected to you to accomplish another such feat so soon!"
                s "Yeah, well, let's call it a feat once we actually pull it off."
                r "In truth, the greater quest will be what we choose to do with the catgirls after they are captured. But yes, let us first consider the task at hand."
                r "My scouts have discovered a little about the caravan's movements. I will order them to do everything they can to assist you."
                s "Sounds good. Get ready while I figure out details with the Warchief..."
            else:
                g "Very well. Make it official with Rokgrid, then we will discuss our specific plans."
                scene bg mainhall
                call sabiabase
                show rokgrid angry1 at right
                with dissolve
                $ A_rokgrid += 2
                $ catgirlraidperformance += 1
                r "Why give this to me? We have not been on the best of terms."
                s "Maybe I want to turn that around. Look, at this point, your only options are to be left out, or to get some free credit for what's going to be a popular operation."
                show rokgrid happy2 at right
                r "You make a good point, and never let it be said that I am not willing to forgive! Please, feel free to take the lead role..."
        "Give Captain Dajrab credit":
            if rokgridalliance:
                if tekrokalliance:
                    $ A_rokgrid -= 2
                    $ A_tekrok -= 2
                    g "Hah! You make alliances with both Rokgrid and Tekrok, then work with neither? You are a bold human."
                else:
                    $ A_rokgrid -= 2
                    g "Hunh. And so you scorn Rokgrid. So be it."
            elif tekrokalliance:
                $ A_tekrok -= 2
                g "Hunh. And so you scorn Tekrok. So be it."
            if dajrabtookmoney:
                g "Very well. Make it official with Dajrab, then we will discuss our specific plans."
                scene bg mainhall
                call sabiabase
                show dajrab normalclosed at right
                with dissolve
                $ catgirlraidinvestigation -= 1
                $ catgirlraidperformance -= 5
                s "There you are. Now, I need your authority to make this operation more official, but I'll be leadi-"
                show dajrab normalopen at right
                d "I refuse."
                show sabiaemo surprised1 at left
                s "What? You'll get approval in return for nothing! Why?"
                d "Because I do not trust you."
                hide dajrab normalclosed with moveoutright
                show sabiaemo closed2 at left
                s "(Dammit, now I look bad. But it's fine, I can handle it myself...)"
            else:
                $ A_dajrab += 1
                g "Very well. Make it official with Dajrab, then we will discuss our specific plans."
                scene bg mainhall
                call sabiabase
                show dajrab normalclosed at right
                with dissolve
                $ catgirlraidinvestigation += 2
                $ catgirlraidperformance += 3
                d "Dajrab wonders just what you are trying to do. I stand aside from these matters."
                s "Making you a nice, neutral choice, right?"
                d "...very well. Dajrab will tell some of Dajrab's warriors to assist you with what they know, and we shall see how this plays out."
        "Take all the credit":
            $ dom += 1
            $ L_orcs += 1
            s "No, I'm an important enough warrior."
            g "Do you... understand what Warchief Groknak has said?"
            s "Yeah, I understand. But fuck the tradition - whether this succeeds or fails, give me all the credit!"
            g "Hunh. Very well, it is on your head."
            g "Give Warchief Groknak a moment to make preparations, then we can discuss the details of our strategy..."
    scene bg black with dissolve
    pause 1
    scene bg mainhall
    call sabiabase
    show groknak normal at right
    with dissolve
    $ catgirlscaptured = 10
    g "Everything is in order. Now, we shall see if you truly have the ability to lead this raid."
    show sabiaemo closed1 at left
    s "Of course I do. The question is if you orcs can actually pull it off - I won't be able to come along, after all, since that would tip them off."
    show sabiaemo normal at left
    s "There are three basic parts to this plan: a new caravan, the forces guarding it, and the real strike force."
    s "For the caravan, set up another load of bone steel and then..."
    menu:
        "Follow the same route as before":
            $ catgirlscaptured -= 4
            g "Exactly the same? They'll be suspicious."
            s "Eh, they'll just think it's a stupid orc decision."
        "Follow a random route":
            $ catgirlscaptured -= 3
            s "We didn't get enough information about how they planned the first caravan, so we'll just do it randomly and trust our strike force to handle things."
        "Set up a fake raiding party" if catgirlraidinvestigation >= 8:
            $ catgirlscaptured -= 1
            s "They'd be suspicious if you just sent another wagon... so what we need to do is have a sizable force defending it this time."
            g "Catgirls are cowards. They won't attack."
            s "No... but they'll definitely scout out the wagon, then our real strike force can track them back to their caravan."
        "Set up a fake raiding party and a fake caravan" if catgirlraidinvestigation >= 12:
            $ catgirlscaptured += 1
            s "They'd be suspicious if you just sent another wagon... so we need to make it seem plausible via more than one method."
            show sabiaemo closed1 at left
            s "We're going to have two different wagons. One will follow the old route, but be covered in a suspicious way, make it clear that it's a fake wagon."
            s "Meanwhile, the real metal will go via a secret route, with a much smaller group. They should buy that, and attack the second wagon - and that's when we'll hit them with our real force."
    g "That is fine for what it is, but... this wagon, do you imply that it will actually contain bone steel?"
    s "Of course. At least some of them will be suspecting a trap, so the more we can do to make it believable, the better."
    g "Warchief Groknak disapproves. If anything goes wrong, the catgirls could steal from us {i}again{/i}. Unacceptable."
    show sabiaemo closed2 at left
    s "(He seems stubborn about this... I guess I could bow to his wishes to make nice with the orcs, but it will be a worse plan.)"
    menu:
        "Send a real shipment":
            $ realshipment = True
            $ catgirlscaptured += 2
            $ dom += 1
            show sabiaemo angry1 at left
            s "No! The entire plan hinges on making them believe it - we have to commit!"
            g "Hunh. This better work."
        "Send a fake shipment":
            $ realshipment = False
            $ A_groknak += 1
            $ sub += 1
            show sabiaemo happy3 at left
            s "Alright, if you say so. Just try to make the fake shipment look believable..."
            g "Hunh. Good."
    show sabiaemo normal at left
    g "So... how will our scouts be armed? If they are unprepared, some may die. But if they are too prepared, the catgirls will be suspicious."
    if catgirlraidkulgan:
        s "..."
        menu:
            "Send scouts":
                pass
            "Follow Kulgan's advice":
                $ catgirlscaptured += 2
                s "Actually, I don't think we should send scouts. I have it on good authority that the orcs guarding the wagon didn't have good security."
                g "Bah, fools."
                s "But we still need to make a similar decision regarding the forces escorting the metal."
    s "You already get the problem: it's a question of risking warriors versus risking the operation being discovered."
    g "You think Groknak will give you an answer? This is your raid."
    s "In that case..."
    menu:
        "Have the orcs be heavily armed":
            $ catgirlscaptured -= 3
            s "They're more dangerous than they look... and it would make sense for us to increase security anyway. Let them be as armed as they want."
            g "You should hope we can still capture them."
        "Have the orcs be lightly armed":
            $ catgirlraiddeaths = True
            s "Deceiving the catgirls is paramount - nobody should take anything they wouldn't normally take."
            g "You should hope that not many warriors die because of your choice."
        "Have them prepare for opportunistic attacks" if catgirlraidsite:
            $ catgirlscaptured += 1
            s "Actually, I think we can mix both. The catgirls won't have heavy forces, they'll be hitting the decoy opportunistically. That should be an assault we can repel, if we know it's coming."
            g "Hunh. Maybe."
    s "Now, the last issue we have to decide is where exactly the real strike force will hit. We need to take them hard and fast if we want to capture them."
    g "Obviously. If we knew where they were, we would have already done it."
    s "Yes, but I've been gathering information of my own..."
    if maplytortured:
        $ catgirlscaptured -= 3
        $ catgirlraiddeaths = True
        show sabiaemo closed1 at left
        s "(Fortunately, that stupid catgirl gave up a lot of specific information. I should be able to coordinate our forces perfectly.)"
    elif maplybefriended:
        $ catgirlscaptured += 2
        show sabiaemo closed1 at left
        s "(Fortunately, I got plenty of information from Maply. That makes things easier...)"
    else:
        if catgirlraidinvestigation >= 16:
            $ catgirlscaptured -= 0
            show sabiaemo closed1 at left
            s "(I've gathered a lot of information about their location and movements, I can do this.)"
        elif catgirlraidinvestigation >= 12:
            $ catgirlscaptured -= 1
            show sabiaemo closed1 at left
            s "(I think I've been able to gather a decent amount of information about their locations, I should be able to do this.)"
        elif catgirlraidinvestigation >= 8:
            $ catgirlscaptured -= 2
            show sabiaemo closed2 at left
            s "(I wish I had more knowledge of their movements, but if I delay longer, we'll lose the opportunity.)"
        elif catgirlraidinvestigation >= 4:
            $ catgirlscaptured -= 3
            show sabiaemo closed2 at left
            s "(Unfortunately, I still don't know very much. I'm going to have to bluff...)"
    show sabiaemo normal at left
    s "Give me the forces to command, and I'll direct them myself!"
    g "Hunh."
    g "It is not a bad plan. Better than the wild attempts of young warriors. Warchief Groknak will permit this raid."
    s "Excellent..."
    scene bg black with dissolve
    pause 2
    scene bg countryside
    call sabiabase
    with dissolve
    s "..."
    show sabiaemo closed2 at left
    s "(Just standing here, waiting while warriors fight on my behalf... it feels...)"
    show sabiaemo normal at left
    s "(It feels almost like things are back to normal.)"
    s "(Part of me does want to fight, but I know I'm better suited to commanding. Plus, when I'm at a distance like this, thinking about it in the abstract, it doesn't really matter that they're orcs.)"
    s "(And they actually took my orders, and obeyed them. This whole idea wasn't as insane as I thought. It may not be the army I want, but it might be a good enough army.)"
    s "(Not just to get revenge... manipulating the orcs into that and then discarding them would be shortsighted. No, perhaps this could actually be the beginning of something more interesting...)"
    show orcbase at right
    show orcloincloth at right
    show orcaxe at right
    show orcnecklace at right
    show orcemo normal at right
    with moveinright
    if catgirlraidinvestigation <= 4:
        $ catgirleventfailed = True
        $ A_groknak -= 2
        $ A_tekrok -= 2
        $ A_rokgrid -= 2
        $ A_dajrab -= 2
        $ A_lutvrog -= 1
        $ A_neve -= 2
        $ L_orcs -= 3
        $ L_catgirls -= 1
        orc "It was an utter failure."
        show sabiaemo surprised2 at left
        s "What?"
        show sabiaemo surprised2 at left
        orc "We not find caravan... they steal metal... kill many warriors."
        s "Shit!"
        orc "Warchief Groknak angry. Say your plan is failure."
        s "(Shit, I guess I miscalculated. I'm not going to get another chance at this...)"
        $ catgirlraidquest = False
        jump lowerorccamp
    orc "The raid is over! Me bring first report!"
    s "Well? Get on with it!"
    if maplytortured:
        orc "The raid went badly. None of the guards were where you said they'd be!"
        show sabiaemo surprised2 at left
        s "(Did that catgirl bitch {i}lie{/i} to me? I didn't think she had the spine!)"
        show sabiaemo closed2 at left
        s "(Or maybe she just said whatever she thought I wanted to hear to escape the pain... Shit, it's too late to back down now.)"
        show sabiaemo normal at left
        s "What's done is done. How did the raid go overall?"
    if catgirlraidperformance >= 5:
        orc "Very successful! We took their caravan and claimed their stolen goods! Here is your share."
        $ catgirlscaptured += 2
        $ temp1 = catgirlraidperformance * 65
        $ temp1 += 200
        $ money += temp1
        "Received [temp1] Lundils."
        orc "Also... find this in leader's wagon. Think is best for you."
        $ Inventory.add_item(Catgirlring)
        "Received a Catgirl Ring."
        show sabiaemo happy1 at left
        s "So, it sounds like it went great!"
    elif catgirlraidperformance > 0:
        orc "Mostly good! We took their caravan and claimed their stolen goods! Here is your share."
        $ catgirlscaptured += 1
        $ temp1 = 0
        $ temp1 = catgirlraidperformance * 50
        $ money += temp1
        "Received [temp1] Lundils."
        s "So, it sounds like it went fairly well."
    elif catgirlraidperformance > -10:
        orc "Not so good. We captured some, and took the caravan, but some fled with most of their stolen goods."
        if realshipment:
            $ L_orcs -= 3
            $ A_groknak -= 2
            orc "And the catgirls steal new shipment of bone steel! Warchief Groknak very angry!"
        else:
            orc "At least catgirls only steal fake metal..."
        s "Not what we would have wanted, but it could have been worse."
    else:
        $ catgirlscaptured -= 2
        orc "It was disaster. Was hard to capture catgirls, did not take caravan, they fled with their stolen goods..."
        if realshipment:
            $ L_orcs -= 3
            $ A_groknak -= 2
            orc "And the catgirls steal new shipment of bone steel! Warchief Groknak very angry!"
        else:
            orc "At least catgirls only steal fake metal..."
        s "I see. I'll have to figure out what we can salvage from this disaster."
    if catgirlraiddeaths == False:
        $ L_orcs += 2
        orc "One more thing... we think maybe your plan kill many warriors. But most are still alive. Sabia is... good leader."
        show sabiaemo happy1 at left
        s "Hey, all of you are my soldiers! I'm not going to ask you to throw your lives away."
        orc "Good leader."
    else:
        $ L_orcs -= 1
        orc "Many warriors die. Me hope it worth it."
        s "I made the choices I had to make."
        orc "..."
    orc "Warchief Groknak talk to you now."
    show sabiaemo normal at left
    hide orcbase at right
    hide orcloincloth at right
    hide orcaxe at right
    hide orcnecklace at right
    hide orcemo normal at right
    with moveoutright
    s "..."
    if catgirlraidperformance >= 5:
        show groknak happy at right with moveinright
        g "Not bad, human! Not bad at all!"
    elif catgirlraidperformance > 0:
        show groknak normal at right with moveinright
        g "So, the raid is done."
    elif catgirlraidperformance > -10:
        show groknak normal at right with moveinright
        g "So, the raid is done. Not well, but it is done."
    else:
        show groknak angry3 at right with moveinright
        g "It's time for you to answer for this disaster, human!"
    s "I just got a report on most of the details, but what about the catgirls? How many did we capture?"
    if catgirlscaptured >= 15:
        $ A_groknak += 3
        g "We captured far more than Warchief Groknak thought possible! We overwhelmed them, and many lay down their arms to surrender!"
        g "This is good. Warchief Groknak is very impressed."
    elif catgirlscaptured >= 10:
        $ A_groknak += 2
        g "It was a rout! We took the caravan and most of the catgirls along with it!"
        g "This is good. Warchief Groknak is impressed."
    elif catgirlscaptured >= 5:
        $ A_groknak += 1
        g "We captured a good number along with their caravan."
    elif catgirlscaptured > 0:
        $ A_groknak += 0
        g "Only a few. Though we took the caravan, many slipped away."
    else:
        $ A_groknak -= 1
        g "None. Those who did not escape fought to the bitter end."
    if catgirlscaptured > 0:
        show groknak normal at right
        g "Now, you must make a decision: what do we do with the captives?"
        s "Hmmm..."
        g "This was your raid, so you may decide. But... Warchief Groknak recommends you listen to the Captains."
        s "Oh? Are they here?"
        g "Yes... and they would like to speak with you."
        hide groknak normal with moveoutright
        s "(Honestly, I just assumed the orcs would rape all the catgirls to death or something. Perhaps this can be more useful than I thought... but I should listen to the Captains.)"
        show tekrok normal at right with moveinright
        t "Sabia. This raid was... almost worthy of orcs."
        s "I'll accept that, for now. But you're here to advise me about the captured catgirls?"
        t "Yes. Traditionally, they would be kept as slaves in the relief tents."
        show sabiaemo annoyed2 at left
        s "And I suppose you want them all to yourself or something?"
        t "No. You do not understand Tekrok."
        t "Tekrok believes all races must unite against Lundar. The catgirls should be our allies."
        show sabiaemo surprised1 at left
        s "Seriously?"
        t "They are small, but not weak. Warriors who underestimate them often die. Tekrok respects them."
        show sabiaemo closed1 at left
        s "Huh."
        show sabiaemo normal at left
        s "But are all your friends going to be okay with that?"
        t "This is Tekrok's plan: learn which catgirl decided to attack us. Make an example of her in the relief tents. Tell all the others they may work with us and receive no punishment."
        s "...I'll keep it in mind."
        t "Do not toy with Tekrok, human."
        hide tekrok normal with moveoutright
        s "..."
        show rokgrid normal at right with moveinright
        r "Well done, Sabia, well done!"
        s "It's been a long day. Let's leave the congratulations for later and get to the decision-making: what do you think I should do with the catgirls?"
        r "Only what is fair. They have stolen from us, so it is reasonable and just for them to work off their debt. They may choose to work in the tents, in camp, or anywhere they are needed."
        s "Huh, is that all? You get worse than that for theft in Lundar."
        r "Yes, but we are not Lundar, and we cannot remove the hands of a whole caravan. I believe this is more fair."
        s "That's reasonable, yes. I'll think about it."
        r "Please do. This is your opportunity to show us not only your tactical prowess, but your wisdom as well."
        hide rokgrid normal at right with moveoutright
        s "Hmm, no Dajrab? I'll go see what he has to say..."
        scene bg countryside
        show dajrab normalclosed at right
        d "..."
        call sabiabase
        with dissolve
        s "So, what about you? What would you have me do with our captives?"
        d "Nothing. Dajrab offers no plan."
        s "Seriously? Surely you have an opinion."
        d "Opinions, yes. But Dajrab does not wish to enforce them on others, only to assist the tribe."
        show sabiaemo annoyed2 at left
        s "Fine, have it your way."
        hide dajrab normalclosed with moveoutright
        show sabiaemo closed2 at left
        s "(Honestly, I'm not sure I like either of the options they gave. Kind of weak, for a bunch of orcs.)"
        s "(Trying to make them work with us might backfire - they're a sneaky race and they'd start slipping away. Better to enslave them all, get use out of them in the relief tents.)"
        s "(Though... I guess those thieves aren't as bad as I thought. Maybe it would be better just try to get on their good side, show some mercy.)"
        if maplybefriended:
            s "(It's obvious which one Maply would want me to choose, but I need to consider the question logically, not emotionally.)"
        s "..."
        show groknak normal at right with moveinright
        g "So? What will we do with the captives?"
        show sabiaemo normal at left
        menu:
            "Tekrok's Plan: Recruit the catgirls":
                $ catgirlstatus = "recruited"
                $ A_tekrok += 3
                $ L_orcs += 0
                $ L_catgirls += 1
                g "Ah. Captain Tekrok believes he can create a new horde against Lundar... perhaps foolish, but Warchief Groknak knows he will work hard to support this plan. It is a good decision."
            "Rokgrid's Plan: Make them work off their debt":
                $ catgirlstatus = "working"
                $ A_rokgrid += 3
                $ L_orcs += 1
                $ L_catgirls += 1
                g "Ah. Captain Rokgrid believes he can expand law to all tribes. Warchief Groknak does not care, but Rokgrid will work hard to support his plans. It is a good decision."
            "Sabia's Plan: Enslave them all":
                $ catgirlstatus = "enslaved"
                $ A_tekrok -= 1
                $ A_rokgrid -= 1
                $ L_orcs += 3
                $ L_catgirls -= 3
                $ slavery += 5
                g "...are you certain?"
                s "Oh, come on. You're orcs, just enslave them! You can't tell me this won't be a popular option with the men."
                g "No, many warriors will approve. Many young warriors."
                s "Well, let them know who's responsible for all their new sluts in the tents."
                g "...very well."
            "Sabia's Plan: Let them go free":
                $ catgirlstatus = "free"
                $ A_tekrok -= 1
                $ A_rokgrid -= 1
                $ L_orcs -= 2
                $ L_catgirls += 5
                $ freedom += 5
                g "...are you certain?"
                s "Trying to force them to stay here would just be asking for a lot of thefts, sabotage, and other trickery. It's what catgirls do."
                s "But like this... we punished them for stealing, the men got to let out their rage... this is a good result."
                g "Hunh. Groknak did not think anyone from Lundar could be soft."
                s "I'm just not being cruel. Don't get the two confused."
    else:
        g "Had we captured any catgirls, you would have an interesting decision to make... but as things stand, this must be enough."
        s "Is it? This wasn't really the result I wanted."
        g "The warriors are appeased. They have had their revenge, if not satisfaction. It will have to be enough."
        show sabiaemo closed2 at left
        s "..."
        show sabiaemo normal at left
        s "Alright, then. If the raid is over, let's go back to camp."
        scene bg black with dissolve
        pause 2
        $ catgirlraidquest = False
        $ maplycaptured = False
        jump sabiahq2
    g "So... the raid is over. What will you do now?"
    s "Any more business to take care of, or decisions to make?"
    g "No."
    s "In that case... I think I'm going to get some sleep."
    $ catgirlraidquest = False
    $ maplycaptured = False
    $ maplyoutskirts = True
    scene bg black with dissolve
    pause 3
    scene bg sabiatent with dissolve
    call sabiabase
    if maplytortured:
        pass
    elif maplybefriended:
        s "(Wait a minute, where's Maply? Her bonds are here... did she escape?)"
        if catgirlstatus == "recruited":
            show maply 1 at right
            show maplyemo normal at right
            with dissolve
            maply "Hmmm... do the orcs really wanna work with us?"
            s "That's the plan."
            maply "That's weird, I don't think orcs have ever done that before... but I guess that's okay!"
            s "Better than them punishing you, right?"
            show maplyemo happy at right
            maply "Yeah, this isn't so bad!"
        elif catgirlstatus == "working":
            show maply 2 at right
            show maplyemo sad1 at right
            with dissolve
            maply "Awww... do we really gotta work for the dumb orcs?"
            s "Considering how much you stole, I think that's pretty merciful."
            show maplyemo normal at right
            maply "Well... I guess we'll see how it goes."
        elif catgirlstatus == "enslaved":
            $ A_maply -= 5
            show maply 2 at right
            show maplyemo angry2 at right
            with dissolve
            maply "You... you're a terrible person! How could you do that to everyone?"
            show sabiaemo closed2 at left
            s "What did you expect to happen?"
            maply "Some... something better than e-enslaving everyone! You're awful!"
            s "..."
            maply "I hate you! We'll make you regret this!"
        elif catgirlstatus == "free":
            show maply 1 at right
            show maplyemo happy at right
            with dissolve
            maply "I heard you let everyone go free!"
            s "Yes, I was coming to let you go too, but it seems you already got out."
            maply "Yeah, but I waited for you! I wanted to say thanks for not being mean to everyone else!"
            show sabiaemo closed1 at left
            s "You shouldn't target these orcs again, though."
            maply "We won't! We won't forget this, Saby!"
            hide maply 1
            hide maplyemo happy
            with moveoutright
            show sabiaemo normal at left
            s "(What did she just call me? Well, it probably doesn't matter...)"
    else:
        s "(Hmm, it looks like Maply slipped out of her bonds. Well, it doesn't really matter...)"
    scene bg black with dissolve
    jump lowerorccamp



label barrininterrogation:
    $ barrinint1 = True
    $ barrinintdelay = True
    call sabiabase
    show lutvrogbase at right
    show lutvrogaxe at right
    show lutvrogwraps at right
    show lutvrogwrists at right
    show lutvrogemo normal at right
    with dissolve
    s "Is it alright if I talk to that noble prisoner again? I think I might be able to get some more information out of him..."
    lut "Lutvrog will allow this."
    hide lutvrogbase at right
    hide lutvrogaxe at right
    hide lutvrogwraps at right
    hide lutvrogwrists at right
    hide lutvrogemo normal at right
    with dissolve
    show sabiaemo closed2 at left
    s "(Alright, I need to decide exactly what strategy I'll take with Barrin. I can see two different ways of manipulating him...)"
    menu:
        "Use threats":
            $ dom += 1
            $ sub -= 1
            $ barrindom = True
            show barrin happy at right with dissolve
            barrin "You're back! You've gotta help me get out of this place!"
            show sabiaemo sad1 at left
            s "I've got bad news, Barrin. The orcs think you were spying on them."
            show barrin sad at right
            barrin "Sp-spying? That's absurd! Why would we want to spy on a bunch of filthy orcs?"
            show sabiaemo sad2 at left
            s "That doesn't matter - all that matters is what they believe. And unless I can give them a damn good explanation of what you were doing, your head is ending up on a spike."
            show barrin normal at right
            barrin "..."
            show sabiaemo closed3 at left
            s "So you really were spying, huh?"
            show barrin sad at right
            barrin "N-no! We don't even care about them right now, the real threat is Governor Andian!"
            show sabiaemo eyebrow1 at left
            s "Explain yourself."
            show barrin happy2 at right
            barrin "He wants his territory to join Lundar, right? Well, he plans to claim a lot of our territory as his when he joins and it's hard for us to refute his claims, since there's no official paperwork..."
            "Barrin explained at length even though she understood it immediately. Governor Andian planned to join Lundar with many of Governor Sceyuer's best lands in tow. So Barrin Sceyuer had been sent to prevent this... and promptly fucked things up."
            show sabiaemo closed2 at left
            s "I understand. Not sure if the orcs will buy that, but it's better than nothing."
            show barrin sad at right
            barrin "Come on, please... you seem like a reasonable woman, surely you can do more to help me..."
            show sabiaemo normal at left
            s "...do you have news from Lundar? What about the Dufuor family?"
            show barrin normal at right
            barrin "Well, we're not exactly the capital, most of our news is old. I heard that one of the Dufuor daughters was killed, and they're trying to find someone to blame. Best to stay away from all that until the big houses settle down!"
        "Use promises":
            $ sub += 1
            $ dom -= 1
            $ barrinsub = True
            show barrin happy at right with dissolve
            barrin "You're back! You've gotta help me get out of this place!"
            show sabiaemo sad2 at left
            s "I'm sorry, Barrin... but there's not much I can do... the orcs are really angry..."
            show barrin angry at right
            barrin "Angry? They're the ones who attacked me!"
            show sabiaemo sad1 at left
            s "But... you were coming near the camp. Right now they might think you were spying... please, give me something better to tell them..."
            show barrin normal at right
            barrin "..."
            show sabiaemo happy3 at left
            s "I want to help you, Barrin. I'm trapped here, but you don't have to be. But unless you give me something to tell them..."
            barrin "Look... tell them we don't even care about their stupid camp. We were scouting for human enemies, not orcs."
            show sabiaemo eyebrow1 at left
            s "Human enemies?"
            barrin "Peasants probably don't know this, but Governor Andian is planning to join his territory to Lundar. But think for just a moment... what exactly is his territory?"
            show sabiaemo surprised1 at left
            s "Oh!"
            barrin "You see, out here in the unorganized territories, there aren't deeds to land... perhaps I should explain, a deed is..."
            show sabiaemo closed2 at left
            s "(Pompous ass. I'm far more familiar with these schemes to claim territory than you are.)"
            "Barrin explained at length even though she understood it immediately. Governor Andian planned to join Lundar with many of Governor Sceyuer's best lands in tow. So Barrin Sceyuer had been sent to prevent this... and promptly fucked things up."
            barrin "You got all that?"
            show sabiaemo happy3 at left
            s "Yeah, I understand now!"
            show barrin sad at right
            barrin "But... will the orcs believe it?"
            show sabiaemo sad1 at left
            s "I don't know... but I'll try to explain it to them... if you had more information..."
            show barrin normal at right
            barrin "Sorry, but that's the truth."
            show sabiaemo normal at left
            s "Umm... do you have news from Lundar? What about the Dufuor family?"
            barrin "Well, we're not exactly the capital, most of our news is old. I heard that one of the Dufuor daughters was killed, and they're trying to find someone to blame. Best to stay away from all that until the big houses settle down!"
    show sabiaemo closed2 at left
    s "(Hmm. That's useful information, but I need more. He's thinking too rationally right now, he's just going to give me carefully prepared information...)"
    show barrin happy at right
    barrin "If I do get out of this, maybe you can help me with something... can you tell me about the orc raiding patterns?"
    show sabiaemo normal at left
    s "What?"
    show barrin happy2 at right
    barrin "If I get back to my father, we'll have a chance to take revenge! Maybe not directly, but we can kill these orc bastards when they try to raid outlying farms!"
    show sabiaemo closed2 at left
    s "(I don't know enough to make a huge difference either way, but I could definitely cause problems for either group. Human and orc lives hang in the balance... which lives are more beneficial for me?)"
    menu:
        "Tell the truth about orc raids":
            $ L_orcs -= 2
            $ L_humans += 3
            "Sabia told him what she knew about the camp's raiding patterns. Giving him the truth now could well increase her influence later."
        "Mix truth and lies":
            "Sabia gave a mix of information that wouldn't particularly hurt either side. She didn't care about orc thugs or human peasants, but either might be useful and she wasn't sure which she would need more later."
        "Lie about the orc raids":
            $ L_orcs += 3
            $ L_humans -= 2
            "Sabia gave him realistic-sounding info that would send troops to all the wrong places. He'd trust her less if she needed him again, but the entire family was her enemy anyway."
    show barrin happy at right
    barrin "Great! Now, can we get me out of here?"
    show sabiaemo sad1 at left
    s "Not yet... I've run out of time with you, I have to go."
    show barrin sad at right
    barrin "W-wait! How long are you going? They might decide to kill me any minute!"
    show sabiaemo sad2 at left
    s "That's true, but I have to go. Please, try to think of anything else you can that might help us, I'll be back tomorrow..."
    hide barrin sad with dissolve
    "She left him squirming like that. The orcs agreed to rough him up a little bit during the night - it didn't take much to convince them. By tomorrow, he ought to be ready to cooperate with her."
    return


label barrininterrogation2:
    $ barrinint2 = True
    call sabiabase
    show lutvrogbase at right
    show lutvrogaxe at right
    show lutvrogwraps at right
    show lutvrogwrists at right
    show lutvrogemo normal at right
    with dissolve
    lut "Back to get more information?"
    s "He's hiding something, I'm sure of it. Can we just torture him?"
    lut "No. Lutvrog cannot risk such conflict."
    s "I'll do what I can, then..."
    scene bg mainhall
    call sabiabase
    show sabiaemo closed2 at left
    show barrin normal at right
    with dissolve
    s "(Barrin is probably panicked and ready to talk, but he's still a little too prepared, he won't give up more than he needs to. What I need to do is lower his defenses somehow...)"
    menu:
        "Just interrogate him.":
            show sabiaemo angry2 at left
            s "Alright, this is your last chance to save your sorry hide!"
            show barrin sad at right
            barrin "Wh-what?"
            scene bg mainhall with dissolve
            "Sabia interrogated him as ruthlessly as she could without violence. Barrin quickly gave up everything he knew about Andian and Sceyuer troop positions, which wasn't amazing but still useful. By the time she was done, Sabia felt satisfied that she understood what his mission had been and the conflict between the two regional Governors."
            "Could that be useful to her? She wasn't sure, but she was glad that she had gotten the information out of him. Both Governors were likely to be in her path back to Lundar."
            "Sabia left the rest to Lutvrog, who resolved things basically as he'd planned to do before. They sent a message via somewhat neutral merchants, and Governor Sceyuer was glad to look the other way provided that his son was returned unharmed."
            $ barrinoutcome = "interrogate"
            call barrininterrogation3
        "Use sexual torture." if barrindom:
            show sabiaemo eyebrow1 at left
            s "You're out of time, Barrin."
            show barrin sad at right
            barrin "What is that supposed to mean?"
            scene bg mainhall
            show barrin normal at right
            show basenaked at left
            show sabiaemo eyebrow1 at left
            with dissolve
            s "You need to tell me everything you know."
            show barrin blush at right
            barrin "Wh-whoa! Why are you taking off your clothes? What the hell is going on?"
            call barrinintscenedom
            play music orccamp fadeout 2.0 fadein 2.0
            $ barrinoutcome = "dom"
            $ barrinletterhint = True
            $ ef_forest_ruin_unlocked = True
            call barrininterrogation3
        "Use sexual manipulation." if barrinsub:
            show sabiaemo sad1 at left
            s "Barrin... we don't have much time..."
            show barrin sad at right
            barrin "What is... what is that supposed to mean? Are they going to kill me?"
            show sabiaemo sad2 at left
            s "They might... unless you can convince them that they can trade you safely somehow."
            show barrin angry2 at right
            barrin "What? Of course they can! My father will go to any lengths to recover me!"
            show sabiaemo surprised2 at left
            s "R-really?"
            show barrin angry at right
            barrin "Just let me talk to the orcs! Show me who to talk to and I can definitely do it!"
            show sabiaemo happy3 at left
            s "Oh, Barrin... I don't know how you can think so clearly, even captured by orcs..."
            show barrin happy at right
            barrin "I'll be Governor one day, I have to do at least this much!"
            s "You're very brave..."
            show sabiaemo closed2 at left
            s "(And not going to tell me anything useful, at this rate. Guess I have no choice...)"
            show sabiaemo normal at left
            s "It might be hard for you to negotiate with the orcs... you need to be fully relaxed so you can think clearly..."
            scene bg mainhall
            show barrin normal at right
            show basenaked at left
            show sabiaemo normal at left
            with dissolve
            s "Please, let me help you..."
            show barrin blush at right
            barrin "Wh-whoa! Why are you t-taking off your clothes?"
            show sabiaemo sad1 at left
            s "Please... I haven't seen a real man in so long... just let me do this..."
            call barrinintscenesub
            play music orccamp fadeout 2.0 fadein 2.0
            $ barrinoutcome = "sub"
            $ barrinletterhint = True
            $ ef_forest_ruin_unlocked = True
            call barrininterrogation3
    return


label barrininterrogation3:
    $ barrinint3 = True
    scene bg black with dissolve
    pause 3
    scene bg road with dissolve
    "Though Sabia had no interest in having anything more to do with Barrin Sceyuer, she did want to see things through to the end. She'd need to avoid being seen, since the knights who were sent might be able to recognize her, but it would be worth watching."
    "The orc scouts determined that there was no ambush waiting for them. In fact, there was only one man."
    show hessian normal at center with dissolve
    hessian "There's no ambush. Show yourselves and we can speak as warriors."
    "While the orcs moved Barrin out to meet with him, Lutvrog stayed closer to Sabia, watching her closely."
    hide hessian normal
    call sabiabase
    show lutvrogbase at right
    show lutvrogaxe at right
    show lutvrogwraps at right
    show lutvrogwrists at right
    show lutvrogemo normal at right
    with dissolve
    lut "You know this human, do you not?"
    s "Yeah. His name is Hessian - family is extremely minor nobility, but he's a veteran of multiple campaigns."
    lut "A confident warrior, to come here alone."
    s "He's strong, but I'm not sure he's all that. But he's experienced and he's not the type to walk into a trap, so it makes sense they'd send him. I'm just surprised he's in the region, I thought his home was north of Lundar."
    lut "You speak as if you know him well."
    s "We met during the minotaur campaign. I respect his skill, but we could never get along. He's an aloof bastard."
    "Lutvrog only considered her words in silence, so Sabia crept a little closer to hear how the negotiations were going."
    scene bg road
    show hessian normal at left
    show barrin normal at right
    show orcbase2 at center
    show orcloincloth2 at center
    show orchair2 at center
    show orcstomach2 at center
    show orcemo2 normalopen at center
    with dissolve
    orc "Ha! Whadja do then?"
    hessian "I stabbed him in the knee, of course. Minotaurs always have their guard too high."
    show orcemo2 smile1 at center
    orc "Haw! Damned horned bastards are too tall for their own good!"
    "As usual, Hessian seemed to be comfortable, even when speaking to orcs. Sabia could tell he was ready to fight, and knew he'd decapitate the orc laughing at his story in an instant if necessary. Sabia never really understood Hessian, and it irritated her."
    show barrin angry at right
    barrin "Are... are we done with this nonsense? The deal is done!"
    show orcemo2 angry at center
    orc "Feh... fine, be gone with you."
    hessian "I am glad to see your word is still your bond."
    barrin "Don't compliment these animals! Take me home!"
    hide barrin angry with moveoutleft
    show orcemo2 normal at center
    orc "..."
    hessian "Forgive the foolish words of young warriors. I will be escorting him to our lands, so we all may return to our own duties and our own battles."
    show orcemo2 smile1 at center
    orc "Aye, as you say."
    scene bg road with dissolve
    "Both groups split up, their work done. Sabia watched the humans closely: Barrin was trying to look like he wasn't fleeing, while Hessian glided along at a comfortable pace. Meanwhile, the orcs were in a generally good mood about the whole thing, so the meeting had been a success."
    "It surprised Sabia, honestly. She had expected it to fall apart in one way or another. Yet it seemed that the orcs honestly just wanted to avoid trouble and the Governor really just wanted his son. If everyone was always so reasonable, maybe a war wouldn't have been necessary."
    if barrinletterhint:
        "No one was ever that reasonable for long, though. Plus, there was the matter of the dead drop, apparently in the forests north of camp. Sabia shook her head and returned to camp."
    else:
        "No one was ever that reasonable for long, though. Sabia shook her head and returned to camp."
    return



label sabiabargroping:
    if bargroping == 0:
        call sabiabargrope1
    elif bargroping == 1:
        call sabiabargrope2
    elif bargroping == 2:
        call sabiabargrope3
    elif bargroping == 3:
        call sabiabargrope4
    if bargroping == 1:
        $ money += 3
        "That day, Sabia was paid a total of 7 Lundils - apparently she'd gotten some tips. Not what she had been going for... but she'd take it."
        return
    elif bargroping == 2:
        $ money += 4
        scene bg silvertusk
        show jadkbase at right
        show jadkemo normal at right
        with dissolve
        show basesimple at left
        show baroutfit2 at left
        show sabiaemo normal at left
        with moveinright
        "As Jadk paid her 8 Lundils, he gave her a thoughtful look."
        jadk "Jadk sees some of the boys getting a little rowdy."
        s "Thank you, but it's fine. I have a plan."
        jadk "...if you say so."
        return
    elif bargroping == 3:
        $ money += 5
        $ sub += 1
        scene bg silvertusk
        show jadkbase at right
        show jadkemo normal at right
        with dissolve
        show basesimple at left
        show baroutfit2 at left
        show sabiaemo normal at left
        with moveinright
        "That day, Sabia was paid a total of 9 Lundils - quite a few tips, but she doubted she'd be getting them for too much longer."
        jadk "You sure about this?"
        s "Yes. Angry orcs like that... they must have made a lot of enemies, right?"
        jadk "Jadk thinks so..."
        return
    elif bargroping == 4:
        $ L_orcs += 2
        $ dom += 1
        $ Sabia.xp += 3
        $ money += 209
        $ Inventory.add_item(Orcaxe)
        $ gotanysword = True
        scene bg silvertusk
        show basenaked at left
        show sabiaemo normal at left
        show orcbase at right
        show orcloincloth at right
        show orcaxe at right
        show orcnecklace at right
        show orcemo normal at right
        with dissolve
        "They didn't fight back until it was too late, not quite believing what they were seeing. No, they had seen what they wanted to see, and now it was too late for them."
        s "Good work."
        orc "Bastards deserved it."
        s "Like we agreed, you can have everything they're carrying. Just get them cleaned up, alright?"
        orc "No problem."
        s "What? Is there something else?"
        orc "You're a very cold warrior. It will be hard to order drinks from you now."
        s "Heh. I don't mind if you look, just keep your hands to yourself."
        orc "Okay."
        scene bg black with dissolve
        "Getting her clothes back in order, Sabia returned to the bar. She cleaned up the soldiers' things without comment and pocketed all the money they had, and though the orcs watched her, they didn't say anything."
        "Sabia cheerfully finished her shift before collecting her pay. Combined with what the orcs had left behind, she had gained 209 Lundils and an axe that looked light enough for her to use."
        return
    return


label bargropinginvestigation:
    $ bargroping += 1
    $ bargropeinv = 0
    $ ef_forest2_unlocked = True
    scene bg sabiatent
    call sabiabase
    with dissolve
    "To Sabia's surprise, there was an orc waiting outside her tent. He gestured as if to come in and, after a pause, Sabia nodded to allow him to enter."
    show orcbase2 at right
    show orcbeard21 at right
    show orcloincloth2 at right
    show orcnecklace2 at right
    show orcpiercing2 at right
    show orcshoulder2 at right
    show orcemo2 normal at right
    show orcaxe2 at right
    with moveinright
    orc "Sorry, but me must speak with you about an important matter."
    s "What is it?"
    orc "Did you murder several orcs from the Silvertusk Bar?"
    show sabiaemo surprised1 at left
    s "..."
    s "Someone was murdered at the bar? That's awful... I work there, I didn't realize anything like that..."
    show sabiaemo closed1 at left
    s "(Barely saved that one. Hopefully it was enough.)"
    show sabiaemo normal at left
    orc "They weren't killed at the bar, but some say they were seen with you before they went missing."
    s "..."
    orc "Warchief Groknak has assigned me to investigate this matter. Normally, me would not tell you of this, but..."
    show orcemo2 angry at right
    orc "This investigation is happening mostly because our shaman insisted upon it. The evidence seems unclear to me, and he is known to have a vendetta against you."
    if shamanmiracles1 == True:
        pass
    else:
        $ bargropeinv += 1
        orc "Me saw you prove his miracles false, too. He is a weak shaman, he should not be bringing up such petty cases when we are at war."
    s "Thank you for telling me about these false charges. Is there anything I can do to help your investigation?"
    show orcemo2 normal at right
    orc "No, me will look for evidence and present it to the Warchief. But me thought you should know, as you can present evidence of your own to refute the charges."
    s "I see..."
    menu:
        "Thank him":
            s "I know there are warriors who will vouch for me. I'll have them speak with you and trust that justice will be done."
            orc "Good. The matter will be decided before the Horned God's Night."
        "Seduce him":
            s "Thank you for fighting this false charge... if there's anything I can do for you personally..."
            show orcemo2 smile1 at right
            orc "Truly? If me help you with charges, you fuck me? Is that what you're offering?"
            menu:
                "Yes":
                    $ bargropeinv -= 2
                    show sabiaemo happy1 at left
                    s "You bet, big guy!"
                    show orcemo2 suspicious at right
                    orc "Attempting to manipulate justice with your wiles... that does not suggest innocence."
                    show sabiaemo surprised1 at left
                    s "Wait, I-"
                "No":
                    $ bargropeinv -= 1
                    show sabiaemo surprised1 at left
                    s "What? No, I didn't mean anything like that!"
                    show orcemo2 suspicious at right
                    orc "..."
            show orcemo2 normal at right
            orc "Me will gather all the evidence and come to a conclusion before the Horned God's Night."
    hide orcbase2 at right
    hide orcbeard21 at right
    hide orcloincloth2 at right
    hide orcnecklace2 at right
    hide orcpiercing2 at right
    hide orcshoulder2 at right
    hide orcemo2 normal at right
    hide orcaxe2 at right
    with moveoutright
    show sabiaemo closed2 at left
    s "(Shit. At least the investigator isn't biased against me, but since I actually did it, there will be evidence. He strikes me as the fair type, so that won't go well for me.)"
    show sabiaemo closed2 at left
    s "(Well then, time to get away with murder.)"
    return


label bargropingtrial:
    scene bg mainhall
    call sabiabase
    with dissolve
    "Sabia entered the main hall nervously, hoping that she'd done enough to prove her innocence... despite her lack of innocence. Fortunately, it looked like this trial was nowhere near as important as the previous one, as very few orcs had attended."
    show groknak normal at center
    with dissolve
    "Groknak rose from his seat, gesturing for her to come forward."
    g "Warrior Sabia, you stand accused of murdering four warriors outside this very camp. What say you?"
    s "It's false. Whatever happened, it has nothing to do with me."
    g "There were no witnesses to the crime, but some have insisted. Therefore, Groknak assigned an investigator. Come forward!"
    show orcbase2 at right
    show orcbeard21 at right
    show orcloincloth2 at right
    show orcnecklace2 at right
    show orcpiercing2 at right
    show orcshoulder2 at right
    show orcemo2 normal at right
    show orcaxe2 at right
    with moveinright
    "The investigator emerged to stand beside them, nodding first to the Warchief and then to the crowd."
    show sabiaemo closed2 at left
    orc "This is an odd murder. One fact is clear: four warriors have disappeared from the camp. Another fact: some believe that Sabia was responsible. But is this true?"
    if murderinvallies:
        orc "Me began by speaking to those who had been seen with Sabia. They said that Sabia had been serving them when the missing warriors disappeared. Though I spoke with them individually, their stories all matched in every detail."
    else:
        $ bargropeinv -= 1
        orc "Me began by speaking to those who had been seen with Sabia. They said that Sabia had been serving them when the missing warriors disappeared. When I spoke with them, their stories did not match well, though this is perhaps normal for drunken warriors."
    if murderinvwitness1:
        orc "Though I asked everyone who had been present, no one else spoke up. All agree that Sabia was working in the Silvertusk Bar when the disappearances happened."
    else:
        orc "But while me was in the bar, a former warrior came forward and claimed that Sabia had gone with the missing warriors the previous night. Hardly proof of murder, but a strike against Sabia."
    orc "If an incident did occur, it allegedly happened outside the camp. So for my next attempt, me journeyed to the locations where some claimed to have seen them go."
    if murderinvwitness2:
        pass
    else:
        $ bargropeinv -= 1
        orc "One hunter saw Sabia go with a group of orcs outside the camp. He saw no violence, but it is nevertheless a suspicious detail."
    orc "After much investigation, me found a location where there had been a battle. However, there were no bodies."
    if murderinvcleansite:
        $ bargropeinv += 1
        orc "Furthermore, there were signs that orcs had come to the location and then left, far from camp. If anything the evidence suggests that the orcs may have deserted."
    else:
        orc "The location was much disrupted, which suggests there may have been some conflict. The exact kind, me cannot say."
    g "Warchief Groknak understands. Is that all?"
    if murderinvshamanevidence:
        orc "There is one more thing, Warchief. Since the shaman brought forth this accusation, me investigated him as well."
        "This prompted a shout of rage from the sidelines, but Groknak glared it into silence and the investigator continued."
        orc "Look at this letter... the shaman has been speaking with the council of all matters, even on the subject of Sabia. It seems obvious that he had a motive to accuse Sabia."
    else:
        orc "Yes, Warchief."
    g "Hmm... thank you. You may go."
    hide orcbase2 at right
    hide orcaxe2 at right
    hide orcbeard21 at right
    hide orcloincloth2 at right
    hide orcnecklace2 at right
    hide orcpiercing2 at right
    hide orcshoulder2 at right
    hide orcemo2 normal at right
    with moveoutright
    show sabiaemo normal at left
    s "And? What is your verdict?"
    g "..."
    if bargropeinv >= 5:
        $ bargroping += 1
        $ L_orcs += 2
        $ A_groknak += 1
        g "The evidence is clear: these deaths had nothing to do with warrior Sabia."
        show sabiaemo happy1 at left
        s "..."
        show groknak angry3 at center
        show sabiaemo normal at left
        g "That means that our shaman has wasted our time with a baseless charge."
        show orcshaman angry3 at right with moveinright
        orcshaman "This is an outrage! Me know she was responsible!"
        show groknak angry3 at center
        g "Do you doubt my ruling? Do you have any new evidence to offer? Or do you wish to waste the Warchief's time?"
        show orcshaman sad1 at right
        orcshaman "..."
        show orcshaman sad1 at right
        orcshaman "No, Warchief."
        s "..."
        menu:
            "Just let him go":
                $ A_groknak += 1
                "Sabia decided to be the bigger person and let him walk away. He was beaten anyway."
            "Undercut him harshly":
                $ dom += 1
                show sabiaemo eyebrow1 at left
                s "Is this the best you can do? Make up false charges and try to get others to fight your battles for you?"
            "Undercut him softly":
                $ sub += 1
                show sabiaemo sad1 at left
                s "I joined your tribe and I've done my best to help you. Why do you hate me so much?"
        hide shaman sad1 at right with moveoutright
        "The shaman stalked away with a scowl on his face. Warchief Groknak returned to his chair. The small crowd disappeared."
        "That, it seemed, was that."
        "Sabia had been expecting more, but she realized that orcs likely wouldn't go for pomp and circumstance around most trials. But she had been expecting a duel to the death or something, so their investigation had impressed her."
        "Though she doubted the orcs had any principle of double jeopardy, she was willing to bet they didn't have the patience for multiple false accusations. She was home free. Sabia left the main hall with a spring in her step."
    else:
        show groknak angry3 at center
        if murderinvshamanevidence:
            g "The shaman may have had an ulterior motive, but that does not mean he was wrong. The evidence is clear: warrior Sabia was responsible for these deaths."
        else:
            g "The evidence is clear: warrior Sabia was responsible for these deaths."
        show sabiaemo angry1 at left
        s "Dammit."
        show orcshaman happy1 at right with moveinright
        orcshaman "So happy to hear that justice was done. That means this is a matter for the council, is it not?"
        g "So be it. Do what you want with her."
        "Sabia knew it was hopeless, but she still tried to make a break for it. She didn't even get out of the hall before warriors brought her to the ground. Her head hit the floor and her world went dark."
        call badendmurdertrial
        pause 3
        $ renpy.full_restart()
    return



label HGNscorefrominventory:
    if Inventory.has_item(Cheapfood) > 0:
        $ gotHGNfood = True
        $ orcfestivalscore += 2
    if Inventory.has_item(Goodfood) > 0:
        $ gotHGNfood = True
        $ orcfestivalscore += 4
    if Inventory.has_item(Expensivefood) > 0:
        $ gotHGNfood = True
        $ orcfestivalscore += 5
    return


label HGNsabia:
    call HGNscorefrominventory
    scene bg sabiatent with dissolve
    "The Horned God's Night began the moment the sun touched the horizon, a long horn being blown so loudly that it resonated over the entire camp. In the midst of planning, Sabia was taken a little off guard, so she hastened to begin making her final decisions."
    show bg HGNsabia1
    call sabiabase
    show jadkbase at right
    show jadkemo normal at right
    with dissolve
    jadk "Well, well, well... Sabia is about to start her own feast!"
    s "I already feel behind - does the horn mean that everything is starting already?"
    jadk "Not quite yet, but expect the warriors to begin looking for where to start."
    s "Well, I'm glad I made most of my preparations beforehand. I know you have to get to your own feast, but... what do you think?"
    if orcfestivalscore >= 10:
        show jadkemo happy2 at right
        jadk "Jadk is impressed, gwahaha! Who would have thought a human warrior would be hosting a major feast?"
    else:
        show jadkemo normal at right
        jadk "This will certainly be remembered. Who would have thought a human would try to host a feast?"
    s "Oh, come on, give me more feedback than that!"
    if gotHGNfood2:
        if gotHGNfood:
            $ orcfestivalscore += 1
            jadk "The most important thing is food, and you've bought food aplenty, gwaha!"
            jadk "Jadk is quite impressed, actually. Lots of good meat to fill stomachs, but some human food as well to draw in curious warriors. Well done!"
        else:
            jadk "The most important thing is food, and you've bought food aplenty, gwaha!"
    else:
        if gotHGNfood:
            $ orcfestivalscore -= 1
            jadk "You have some strange human dishes that are sure to draw in warriors. Perhaps it would have been better to have more food, even if simpler, but it will help."
        else:
            $ orcfestivalscore -= 3
            jadk "To be honest... you do not have nearly enough food. Warriors may stop by, but they will not stay and feast."
    if Inventory.has_item(HGNTent) > 0:
        $ orcfestivalscore += 3
        jadk "Your tent is quite impressive! Only Rokgrid can begin to compare, and you will still draw much attention!"
    else:
        $ orcfestivalscore -= 1
        jadk "More might have been impressed with a better tent... but the fact that you could acquire an orcish tent may be impressive enough."
    if Inventory.has_item(Furnishings) > 0:
        $ orcfestivalscore += 3
        jadk "And you've put real effort into filling the tent with finery! Even Jadk's bar is put to shame, gwahaha!"
    else:
        $ orcfestivalscore -= 1
        jadk "It would have been better if you had more finery to show off, but you will still draw some warriors by the novelty of your feast."
    if antlers >= 4:
        $ orcfestivalscore += 1
        $ L_orcs += 1
        jadk "Your altar to the Horned God is very impressive! People will definitely take notice of it!"
    elif antlers >= 3:
        $ orcfestivalscore += 1
        jadk "Your altar to the Horned God isn't bad at all! People will definitely take notice of it!"
    elif antlers >= 1:
        jadk "It's a shame your altar has so few horns, but it will do. At least you're honoring the Horned God."
    else:
        $ orcfestivalscore -= 1
        jadk "You really should have put together an altar of horns, but... Jadk think it will be forgiven."
    s "I'll need to focus fully on arranging everything soon... any last suggestions?"
    jadk "Think about the first drinks you serve carefully! Everyone will be watching to see how you start."
    s "Hmm... should I start with something special?"
    menu:
        "Beer" if Inventory.has_item(HGNBeer) > 0:
            $ orcfestivalscore += 2
            $ Inventory.rem_item(HGNBeer)
            s "I purchased some beer that should be better than the usual orc drinks. Let's start with that."
            jadk "As good a choice as any! Get them good and drunk, gwahaha!"
        "Mead" if Inventory.has_item(HGNMead) > 0:
            $ orcfestivalscore += 2
            $ Inventory.rem_item(HGNMead)
            s "I purchased some mead that should be better than the usual orc drinks. Let's start with that."
            jadk "As good a choice as any! Get them good and drunk, gwahaha!"
        "Wine" if Inventory.has_item(HGNWine) > 0:
            $ orcfestivalscore += 2
            $ Inventory.rem_item(HGNWine)
            s "I purchased some wine that should be better than the usual orc drinks. Let's start with that."
            jadk "As good a choice as any! Get them good and drunk, gwahaha!"
        "Nothing":
            $ orcfestivalscore -= 2
            s "Orcish beer is fine."
            jadk "They'll drink through what little you have quickly, but that will do."
    jadk "Jadk wishes you the best of luck - drop by the bar again before the night is over!"
    s "I wanted to ask you about that... can I visit other feasts? Or should I stay near my own the entire time?"
    jadk "You can go where you want. And it would be wise to visit the Warchief's feast, to show your respect."
    jadk "But Jadk thinks you'll have your hands full just taking care of your own feast, gwahaha!"
    hide jadkbase at right
    hide jadkemo normal at right
    with moveoutright
    "Alone, Sabia sighed and rested her eyes for a moment."
    if Inventory.has_item(Royalgold) > 0:
        $ Inventory.rem_item(Royalgold)
        "There was one thing she hadn't mentioned to him... the bottle of Royal Gold."
        s "(It's not some magic potion that can make people instantly loyal, but it will have an effect and improve things. It will only go so far, though... how should I use it?)"
        menu:
            "To draw in as many orcs as possible.":
                $ orcfestivalscore += 6
                s "(I'll use it when I get a large, susceptible group. That ought to get my feast off on the right track.)"
            "To encourage orcs already loyal to her.":
                $ orcfestivalscore += 3
                $ L_orcs += 5
                s "(I'll wait for some orcs that already approve of me and try to get them on my side for good with some private drinking.)"
            "To get support from the Warchief.":
                $ orcfestivalscore += 3
                $ A_groknak += 3
                s "(Despite the changes, the Warchief is still the heart of the camp. Best to improve his opinion of me.)"
            "To get support from the Captains.":
                $ orcfestivalscore += 3
                $ A_rokgrid += 2
                $ A_tekrok += 2
                $ A_dajrab += 2
                s "(Striking out on my own like this is risky... best to seem impressive but unthreatening by sharing drinks with the Captains.)"
            "Don't use it.":
                $ Inventory.add_item(Royalgold)
                s "(Better save it for later.)"
    "Orcs were beginning to move between the tents, shouting to one another and laughing over jokes. Soon, the sky would dim and the bonfires would be lit. Sabia had made a lot of preparations beforehand, but she knew there was still a lot to do."
    s "Alright, it's time for the Horned God's Night to begin. Let's do this."
    "Squaring her shoulders, Sabia headed out to the campfire to speak with warriors and make sure she was seen."
    "If she had taken an offer from one of the Captains, she would have had a clear path to follow. But now, she would have to manage everything herself. Sabia had always hated this part of politics - and her mother had scolded her endlessly over it - but she hoped she could do a little better with orcs."
    if orcfestivalscore >= 10:
        scene bg HGNsabia2
        call sabiabase
        with dissolve
        "For a while, she feared that she would go completely ignored, but soon there were orcs milling about near her fire. They seemed to be wandering throughout the entire camp, without any real allegiance, just looking for feasts that interested them. Fortunately, Sabia alone was a draw, so she didn't go ignored."
    else:
        "Some orcs milled around near her fire, drawn by her alone, but it wasn't long before they began to wander away. Soon there were fewer and fewer of them present..."
    "But she hoped to be more than novelty. Sabia scanned the orcs for any she recognized..."
    $ temp1 = 0
    if bartimes >= 5:
        $ temp1 += 1
        "Plenty of orcs from the bar."
    if sexworktimes >= 5:
        $ temp1 += 1
        "Some orcs from the tents that leered but didn't touch her."
    if sparrespect >= 5:
        $ temp1 += 1
        "Warriors from the sparring grounds."
    if foresthunting >= 5:
        $ temp1 += 1
        "To her surprise, she recognized some of the hunters."
    if temp1 >= 3:
        "All in all, more orcs were attending than Sabia had expected. Maybe it wasn't premature of her to have tried to host her own feast after all."
    elif temp1 >= 2:
        $ orcfestivalscore -= 2
        "All in all, not as many as Sabia had hoped. That shouldn't have surprised her, given that she was a human outsider."
    else:
        $ orcfestivalscore -= 5
        "All in all, not nearly as many orcs as Sabia had hoped. Perhaps it had been too early for her to try to host her own feast."
    "Interacting with so many orcs made Sabia realize that she needed to adopt a more consistent position, however. There were some who respected her, some who lusted after her, and many who did both. Sabia had no qualms about using either to her advantage, but she wasn't sure which was the superior option..."
    menu:
        "Lean on sex appeal":
            $ sub += 1
            $ dom -= 1
            if sexworktimes >= 5:
                $ orcfestivalscore += 1
            "Sabia decided that most orcs weren't likely to respect her as a warrior for a multitude of reasons. If they were going to think of her as weak, she might as well use that against them."
        "Lean on skill in combat":
            $ dom += 1
            $ sub -= 1
            if Sabia.level >= 4:
                $ orcfestivalscore += 1
            "Sabia decided that the orcs were probably already thinking of her sexually, she needed to focus on reminding them that she was a warrior, too."
    if temp1 >= 2:
        "After long enough with the orcs, Sabia was tired of pretending to care about random warriors. A decent number of orcs were gathering now, so she decided it would be better to spend time with friends and allies."
    else:
        "After long enough with the orcs, Sabia was tired of pretending to care about random warriors. Very few orcs were gathering by her fire, so she might as well spend her time with friends and allies."
    $ temp1 = 0
    if HGNlutvrog:
        $ temp1 += 1
    if HGNkulgan:
        $ temp1 += 1
    if HGNmaply:
        $ temp1 += 1
    if HGNneve:
        $ temp1 += 1
    if temp1 >= 4:
        $ orcfestivalscore += 1
        $ L_orcs += 1
        "To Sabia's surprise, she actually saw quite a few people she recognized. Having so many here would probably help her reputation, but she was more glad just to see them."
    elif temp1 >= 2:
        $ orcfestivalscore += 0
    elif temp1 >= 1:
        $ orcfestivalscore -= 1
        if HGNneve:
            "Unfortunately, the only person Sabia saw was Neve, who seemed to be busy with several other warriors. Sabia decided to meet up with her later."
    else:
        $ orcfestivalscore -= 3
        "Unfortunately, as much as Sabia searched, she didn't recognize anyone she really liked. That didn't bode well, but Sabia just swallowed her frustration and kept moving forward."
    if HGNlutvrog:
        call HGNlutvrog_dialogue
    if HGNkulgan:
        call HGNkulgan_dialogue
    if HGNmaply:
        call sabiabase
        show maply 3 at right
        show maplyemo happy at right
        with dissolve
        "Looking around the fire, Sabia noted Maply near the edge. She was looking around at the bustling of the feast happily, but wasn't getting directly involved herself. Sabia approached her with a smile."
        maply "Oh, hello there, Saby!"
        call HGNmaply_dialogue
    "It was pitch black now, and all the feasts were well underway. Sabia glanced around her own, also eyeing the other bonfires. The Captains' were the largest, and the main hall was burning brightly, but there were many smaller warriors' fires like her own."
    "As she turned her gaze back to her own group, however, she spotted orcs rummaging around, looking for more alcohol. Had they gone through what she'd provided already? This could be a real problem."
    s "(Shit, I wish I'd known how much I'd need. Do I have any other stores I could bring out?)"
    menu:
        "Beer" if Inventory.has_item(HGNBeer) > 0:
            $ orcfestivalscore += 1
            $ Inventory.rem_item(HGNBeer)
            s "I'll throw out the beer as well. Hopefully they're drunk enough that they don't care what they get."
        "Mead" if Inventory.has_item(HGNMead) > 0:
            $ orcfestivalscore += 1
            $ Inventory.rem_item(HGNMead)
            s "I'll throw out the mead as well. Hopefully they're drunk enough that they don't care what they get."
        "Wine" if Inventory.has_item(HGNWine) > 0:
            $ orcfestivalscore += 1
            $ Inventory.rem_item(HGNWine)
            s "I'll throw out the wine as well. Hopefully they're drunk enough that they don't care what they get."
        "Nothing":
            $ orcfestivalscore -= 2
            s "Shit, this is bad."
    s "(That isn't going to be enough, not at this rate. I need to take more drastic measures.)"
    scene bg silvertusknight
    call sabiabase
    with dissolve
    "Sabia rushed across camp, knowing that she probably only had one option. Asking any of the Captains for booze would just embarrass her, but Jadk..."
    call HGNjadk_dialogue
    scene bg HGNsabia2
    call sabiabase
    with dissolve
    if gotHGNfood2:
        "When she got back, Sabia checked everything, especially the stores of food. The orcs were eating more than she had expected, but fortunately she had plenty of extra supplies. It didn't seem like they cared about the quality, anyway."
    else:
        $ orcfestivalscore -= 2
        "As soon as she got back, Sabia realized that she had another problem: the orcs were eating through all the food she had provided as well. She had a deal with Vehlis for resupply, but didn't want to expend that resource so quickly. They'd have to live with it for now."
    "Having done the best she could, Sabia looked over her feast. It seemed to be moving along smoothly enough, at least. She decided that now was her best chance to make an appearance at the Warchief's feast."
    scene bg mainhallnight
    call sabiabase
    with dissolve
    call HGNwarchief_feast
    scene bg HGNsabia2
    call sabiabase
    with dissolve
    "Back at her own feast, Sabia felt like it was a little tame compared to the others. She hadn't planned any formal activities, not thinking something like that would be necessary, and wasn't sure what to do now."
    if HGNkulgan:
        show orcbase at right
        show orcloincloth at right
        show orcpiercing at right
        show orcshoulder at right
        show orcstrap at right
        show orcwrap at right
        show orcbeard1 at right
        show orcemo normal at right
        with dissolve
        "As if sensing her problem, Kulgan approached her."
        kulgan "If you want to liven things up, we should start a drinking game."
        "Sabia blinked in surprise. It was a good enough idea, a common pastime of soldiers, but she had no idea what the orcs played. Kulgan seemed to understand, holding up a dark jug."
        kulgan "This is Orcish Sunset, one of our stronger brews. Kulgan thinks it would be fun... and it would be even better if Sabia took the first drink."
        s "An interesting idea, Kulgan. Thanks for suggesting it."
        menu:
            "Take the first drink":
                s "Alright, I'll start things off. Call them."
                "Kulgan eagerly gathered a group of orcs, waving his jug over his head. It drew quite a few, more than she had expected. Apparently it was a popular game."
                "When Kulgan announced that she would start the game, she smiled... until she accepted the small cup he handed to her. Just the scent of it burned her nose and made her eyes water. This was going to be rough."
                "But all the orcs were watching her now, so she couldn't back down. Hopefully just one cup wouldn't do her any harm."
                "Bracing herself, Sabia downed the entire cup at once. It screamed through her body and for a moment she went completely blind."
                if Sabia.level >= 3:
                    $ L_orcs += 1
                    "Sabia staggered, but remained on her feet. Her head was spinning, but she fought it down and raised the cup over her head before tossing it back to Kulgan."
                    "There was a moment of stunned silence, then the orcs cheered, several of them thumping her roughly on the back. There was no way she could have taken another one of those, but it seemed like they hadn't really expected her to and were just impressed that she'd made the attempt."
                    "Another drink would have been awful, but since she had started the game, that seemed to be enough. Kulgan began pouring cups for the others and they started drinking. Sabia watched the game for a moment, but it seemed to be more \"drinking\" than \"game.\" It seemed to make them happy, though, so she left satisfied."
                else:
                    $ orcfestivalscore -= 1
                    "When Sabia came to, she was lying on the ground. The orcs were laughing at her, but their mocking was gentle. Apparently they hadn't really expected her to try it and were impressed that she'd made the attempt."
            "Tell him to set it up himself":
                $ L_orcs -= 1
                s "Sorry, can you handle this part yourself? I need to stay sober."
                "Kulgan nodded in understanding and then called a group of orcs around. The game seemed to be quite popular - it also seemed to be nothing but drinking and collapsing - and Sabia smiled to see her feast become more lively."
            "Forbid him from playing the game":
                $ orcfestivalscore -= 2
                s "We'll have none of that here at my feast!"
                "Kulgan seemed frustrated, but didn't argue, merely slipped away. Sabia scowled and tried to think of other ideas, but came up with nothing."
        "Leaving the orcs behind, Sabia headed out to see what actually needed to be done."
        hide orcbase at right
        hide orcloincloth at right
        hide orcpiercing at right
        hide orcshoulder at right
        hide orcstrap at right
        hide orcwrap at right
        hide orcbeard1 at right
        hide orcemo normal at right
        with dissolve
    else:
        "Nothing really came to mind, so Sabia had to leave the orcs to their own devices."
    if HGNneve:
        call HGNneve_dialogue
        scene bg HGNsabia2
        call sabiabase
        with dissolve
        if aliochnevesex:
            "Back at camp, it was easy to replace the lost supplies and the feast continued without a problem. Part of Sabia felt guilty for abandoning her duty... but the experience left her feeling so satisfied she decided that she wouldn't let it bother her."
        else:
            "Back at camp, it was easy to replace the lost supplies and the feast continued without a problem. Irritating, but not ultimately a problem."
    else:
        $ orcfestivalscore -= 1
        "As the night wore on, food started to run low. Sabia had to sweep by the supply tents, but found neither Alioch nor Vehlis there. She took what she needed and it was enough, but it took her forever to carry it back to her camp."
    "Sabia took a few steps back and just looked over her feast. However well it went, she was glad she had taken this path. Allying with any of the Captains would have just made her dependent on them. This way, at least she was forging her own path."
    "For better or for worse, she had hosted a feast at an orc festival. And now orc brutes were attending it, and Sabia thought she caught a glimpse of a catgirl or two. Plus Neve had made an appearance."
    "This rough celebration between so many races would once have disgusted her. Now, Sabia wasn't sure exactly how she felt..."
    menu:
        "Accept it as a good thing":
            $ freedom += 1
            "Sabia decided not to overthink it. This wasn't so bad, and she'd found some people she actually liked. If it felt good, then there was nothing wrong with living this way."
            "Of course, it couldn't last forever. There would need to be a reckoning with her sister, and when that happened Sabia would need to make some difficult choices."
            "But if possible, maybe another feast like this wouldn't be so bad."
        "Accept it as the randomness of chance":
            "Sabia shook her head, rejecting any great narrative for the event. It was what it was. She didn't care what anyone else thought of it."
        "Accept it as a necessary evil":
            $ slavery += 1
            "Sabia frowned as she looked over the mixed crowd. It was a necessary step to get what she wanted, but she couldn't let herself forget who and what she was. This was just a platform for her to return to her true position."
            "Maybe these creatures could have some role once she got what was hers, but it would be nothing like this."
    scene bg dajrabtentnight
    call sabiabase
    with dissolve
    call HGNdajrab_dialogue
    if orcfestivalscore >= 20:
        scene bg HGNsabia2
        call sabiabase
        with dissolve
    else:
        scene bg HGNsabia1
        call sabiabase
        with dissolve
    "When she got back to her own bonfire, things seemed to have wound down. She examined the sky and was surprised how late it was - early, now. Though she didn't know exactly how long it extended, surely the Horned God's Night would be over at dawn, if nothing else."
    "Looking over those attending her feast, Sabia tried to estimate how well she had done..."
    if orcfestivalscore >= 35:
        $ L_orcs += 7
        $ A_groknak += 2
        $ A_lutvrog += 1
        $ A_neve += 1
        $ Sabia.xp += 12
        $ dom += 1
        $ sub += 1
        s "(I don't think anyone could complain about my feast! There were a ton of people here, maybe even more than Dajrab's feast!)"
    elif orcfestivalscore >= 30:
        $ L_orcs += 5
        $ A_groknak += 1
        $ Sabia.xp += 10
        s "(I think I did pretty damn well. Only Dajrab's feast was bigger than mine, and he obviously surprised everyone with that stunt.)"
    elif orcfestivalscore >= 25:
        $ L_orcs += 3
        $ Sabia.xp += 8
        s "(I think I did okay, for a human outsider. Dajrab's feast was bigger, since he outdid everyone, but I didn't compare poorly to the other Captains.)"
    elif orcfestivalscore >= 20:
        $ L_orcs += 1
        $ Sabia.xp += 6
        s "(I suppose it could have been worse. It's not a small thing for an outsider like me to successfully host a feast.)"
    elif orcfestivalscore >= 15:
        $ L_orcs -= 1
        $ A_groknak -= 1
        $ Sabia.xp += 4
        s "(I have a feeling that most of the orcs who came here were disappointed. I probably didn't do my reputation any favors with this.)"
    elif orcfestivalscore >= 10:
        $ L_orcs -= 3
        $ A_groknak -= 2
        $ A_rokgrid -= 1
        $ A_tekrok -= 1
        $ A_dajrab -= 1
        $ Sabia.xp += 2
        s "(This was pretty bad. Maybe it could have been worse, but I just proved I wasn't ready.)"
    else:
        $ L_orcs -= 5
        $ A_groknak -= 3
        $ A_rokgrid -= 1
        $ A_tekrok -= 1
        $ A_dajrab -= 1
        $ dom -= 1
        $ sub -= 1
        s "(This was an utter disaster. The orcs will remember this, and they won't remember it favorably.)"
    "Sabia stayed in the darkness outside of the campfires, waiting in silence. At last she saw that her presence was no longer necessary and she turned back to her tent to finally rest."
    "She had a feeling that things would get a lot rougher after this, but she would deal with that when she was better rested."
    jump HGNaftermath


label HGNtekrok:
    call HGNscorefrominventory
    "The Horned God's Night began the moment the sun touched the horizon, a long horn being blown so loudly that it resonated over the entire camp. In the midst of planning, Sabia was taken a little off guard, so she hastened to begin making her final decisions."
    scene bg HGNtekrok1
    call sabiabase
    show tekrok normal at right
    with dissolve
    if orcfestivalscore >= 10:
        "She met Tekrok alone in his tent, before the festivities truly started. He looked tense, but the nod he gave her was a little respectful."
        t "Tekrok was skeptical, but you have added something significant to these festivities. Thank you."
        s "Huh, that's more thanks than I expected."
    elif orcfestivalscore >= 3:
        "She met Tekrok alone in his tent, before the festivities truly started. He looked tense, and when he saw her he scowled."
        t "Tekrok is still unsure letting you be involved was a good idea. Hopefully you will prove yourself."
        s "Well, see what I've done."
    else:
        show tekrok angry1 at right
        "She met Tekrok alone in his tent, before the festivities truly started. When he saw her, his face changed to an expression of pure rage."
        t "You offer to make an alliance with Tekrok, and then {i}this{/i} is the best you can do?"
        s "What, you expected me to go all out on your shitty festival?"
        t "Tekrok expected you to offer something! Get out of my sight - this alliance is over!"
        jump HGNbadend
    if Inventory.has_item(Furnishings) > 0:
        $ orcfestivalscore += 3
        $ A_tekrok += 1
        t "Tekrok thought you would add only weak, human elements. But these furs and horns you purchased... these things even true warriors appreciate."
    if Inventory.has_item(HGNTent) > 0:
        $ orcfestivalscore += 3
        t "The tent you purchased... Tekrok made a few changes, but it is finer than anything orcs could find. It will impress many."
    t "These things are only trappings to the true feast. The heart of it is food and drink."
    if gotHGNfood:
        s "Surely you're not going to complain about that? I contributed my part!"
        t "Yes, you did. The food you sent is of good quality, we will use it before the orcs become too drunk to notice."
        s "Yeah, I wondered if that would happen."
    else:
        $ A_tekrok -= 1
        s "Sorry I didn't contribute more. Do we have enough?"
        t "Of course we have enough! Tekrok is no fool!"
    t "Quality will be most noticed at the beginning, before everyone is swept up in the Horned God's Night. Tekrok hopes you have some alcohol of finer quality to begin everything?"
    menu:
        "Beer" if Inventory.has_item(HGNBeer) > 0:
            $ orcfestivalscore += 3
            $ A_tekrok += 1
            s "I purchased some beer that should be better than the usual orc drinks. Let's start with that."
            t "Good! Tekrok's warriors want nothing fancy, but brewing beer is one of the only things humans are good for."
            s "How generous of you."
        "Mead" if Inventory.has_item(HGNMead) > 0:
            $ orcfestivalscore += 2
            s "I purchased some mead that should be better than the usual orc drinks. Let's start with that."
            t "Mead, huh? An odd choice, but it will do."
        "Wine" if Inventory.has_item(HGNWine) > 0:
            $ orcfestivalscore += 1
            s "I purchased some wine that should be better than the usual orc drinks. Let's start with that."
            t "Wine? A sad human drink... at least it will get them drunk quickly."
        "Nothing":
            $ A_tekrok -= 1
            s "Sorry, no. I figured the warriors would drink what they're used to."
            t "Hmph. It will be fine."
    if Inventory.has_item(Royalgold) > 0:
        $ Inventory.rem_item(Royalgold)
        $ orcfestivalscore += 5
        t "Now, we must speak o-"
        s "Actually, I have something else to add. Do you recognize this?"
        t "A strange golden potion?"
        t "I hope you do not plan to poison or manipulate anyone, human. Not on this night, of all nights."
        s "Relax, this is harmless. It's a potion called Royal Gold, and humans use it all the time. It doesn't control people or anything, just improves their mood, helps people bond together."
        t "Hunh."
        s "Mix it in with drinks and give it to your top warriors. Give them this and a good time, and I guarantee they'll be primed to be more loyal than before."
        t "Tekrok does not like such tricks... but perhaps this will be useful. Very well. But we must speak of your behavior during the feast."
    else:
        t "Now, we must speak of how exactly this feast will go."
    t "It is expected that warriors will move between feasts. Even Tekrok will visit others. But you must spend most of your time here, to increase our honor!"
    s "It's not like this is a foreign concept to me, humans do similar things. I've got it."
    t "You should visit the Warchief's feast, out of respect. Otherwise, you should stay here and be prepared for any problems that might occur."
    s "Believe me, I get it. Let's celebrate the Horned God's Night already."
    hide tekrok normal at right
    with dissolve
    "Leaving Tekrok for the moment, Sabia headed out to the campfire to speak with warriors and make sure she was seen."
    if orcfestivalscore >= 10:
        scene bg HGNtekrok2
        with dissolve
        "The atmosphere was strange. Usually there was an aura of violence seething underneath the surface, but for once Sabia didn't really feel threatened. The orcs seemed happy, celebrating the new year without any inhibitions."
        "It was an odd experience, but she felt almost welcome. Orcs that were usually respectful were friendly, and even those who disliked her were polite. Most likely it would only last one night, but still..."
    else:
        "The atmosphere was strange. Usually there was an aura of violence seething underneath the surface, but for once Sabia didn't really feel threatened. The orcs seemed uninterested in the feast, but they just wandered away instead of becoming violent."
        "At first she thought nothing of it, but she realized that it wasn't just a temporary ebb. The orcs were leaving, making her bonfire seem lonelier and lonelier as time went on. Though the fire still burned hot, it seemed small and cold with no one around it."
        show tekrok angry1 at right with dissolve
        "Without warning, Tekrok appeared in front of her, furious."
        t "You offer to make an alliance with Tekrok, and then {i}this{/i} is the best you can do?"
        s "What, you expected me to go all out on your shitty festival?"
        t "Tekrok will not accept this pathetic effort! Get out of my sight - this alliance is over!"
        jump HGNbadend
    if HGNlutvrog:
        call HGNlutvrog_dialogue
    else:
        call sabiabase
        with dissolve
        "She didn't really know any of them, though, and Sabia found herself a little lonely. They were all enjoying themselves, but she was just acting out a role."
        "But she couldn't just feel sorry for herself. Sabia shook her head and got up, resolving to be more proactive."
    "To Sabia's surprise, several of the orcs called her over. They were clustered around a jug and several small cups that looked childish in their hands. She wasn't entirely sure what to make of it."
    "It seemed to be some kind of drinking game, though there wasn't much of a game to it. Whatever kind of alcohol they had, it seemed to be strong, because they seemed to feel even the small cups of it. While she watched, one of the orcs keeled over. The others all laughed and drank another cup."
    orc "Come on, Sabia, drink!"
    s "What exactly is that?"
    orc "Orcish Sunset. Come on, join us!"
    s "I can't play games with you, I need to keep everything running smoothly."
    orc "Come on, just one drink!"
    "Sabia stared at them skeptically, wondering if this was some plot. But given how Tekrok used her, they didn't need an excuse to take advantage of her, and she saw them all drinking from the same jug. Just one would probably be harmless, but..."
    s "..."
    menu:
        "Take a drink":
            "Deciding that she couldn't back down from a challenge, Sabia picked up one of the cups and cocked an eyebrow. The orcs cheered raucously and filled her cup."
            "She brought it closer to her mouth and had to suppress her reaction. Just the scent of it burned her nose and made her eyes water. This was going to be rough."
            "Bracing herself, Sabia downed the entire cup at once. It screamed through her body and for a moment she went completely blind."
            if Sabia.level >= 3:
                $ L_orcs += 1
                "Sabia staggered, but remained on her feet. Her head was spinning, but she fought it down and handed the cup back to the orc with a smirk."
                "There was a moment of stunned silence, then the orcs cheered, several of them thumping her roughly on the back. There was no way she could have taken another one of those, but it seemed like they hadn't really expected her to and were just impressed that she'd made the attempt."
            else:
                "When Sabia came to, she was lying on the ground. The orcs were laughing at her, but their mocking was gentle. Apparently they hadn't really expected her to try it and were impressed that she'd made the attempt."
        "Refuse":
            $ L_orcs -= 1
            s "Sorry, I have work to do."
            orc "Booo!"
            "The orcs seemed to disapprove, but Sabia really didn't give a shit. There was too much to do for her to waste time on drinking games."
    "Leaving the orcs behind, Sabia headed out to see what actually needed to be done."
    show tekrok normal at right with moveinright
    "She got an answer not long after, when Tekrok approached her with a scowl. It seemed like this one wasn't directed at her, though."
    t "Sabia. We have a problem: more orcs came to our feast than expected."
    s "And that's a problem because?"
    t "We'll run out of beer. Not now, but late in the night when everyone is almost out. We can't let this happen."
    hide tekrok normal at right with moveoutright
    "Sabia was about to ask him what he expected her to do about it, but Tekrok stalked off. Apparently he just expected her to take care of the problem on her own. Well, that was an expression of trust in a way, she'd have to make the most of it."
    scene bg silvertusknight
    call sabiabase
    with dissolve
    "Sabia rushed across camp, knowing that she probably only had one option. Asking any of the Captains for booze would just embarrass her, but Jadk..."
    call HGNjadk_dialogue
    scene bg HGNtekrok2
    call sabiabase
    if HGNmaply:
        call sabiabase
        show maply 3 at right
        show maplyemo happy at right
        with dissolve
        "Compared to the other feasts that Sabia had seen on her way, Tekrok's seemed the most consistent. Lots of rough-looking orcs and not much else. That was why Maply stuck out like a sore thumb. Sabia approached her with a smile."
        maply "Oh, hello there, Saby!"
        call HGNmaply_dialogue
    else:
        "Compared to the other feasts that Sabia had seen on her way, Tekrok's seemed the most consistent. Lots of rough-looking orcs and not much else. Sabia lurked by the edges of it, actually hoping something would go wrong so she'd have something to do."
    call sabiabase
    show tekrok angry2 at right
    with dissolve
    "Without warning, Tekrok appeared on the other side of a campfire, lit up harshly by its light. He glowered at her and raised a hand."
    t "Get over here, human."
    "Obviously she had no choice but to agree, so Sabia approached, wondering what he might do. But when she got closer, Tekrok merely jerked his head for her to follow him. They moved some distance away, to a smaller campfire."
    "Separate from the others, it was lit at the base of a column of bones, the Horned God's altar. No one else seemed to approach it. As he sat down, Tekrok's expression became less harsh."
    show tekrok normal at right
    t "It is time for us to talk."
    s "And you couldn't have just said that? If you need to keep shouting at me in front of your men all the time, this alliance will be a real pain."
    t "That is because Tekrok must work with fools. But you... are not a fool."
    show sabiaemo eyebrow1 at left
    s "What's this? Are you really complimenting me?"
    show tekrok angry1 at right
    t "Tekrok can respect strength, even in humans."
    show tekrok normal at right
    show sabiaemo normal at left
    t "Tekrok will be blunt: the tribes of orcs are scattered. Some still follow the shamans, as if they have not failed. Many are led by cowards, others by fools who plan to attack Lundar in small, useless raids."
    s "And which one of those is Groknak?"
    t "...the Warchief was once a great warrior. And his actions saved many women of our tribe. But he has grown old, and he must surrender leadership to a younger warrior."
    show sabiaemo surprised1 at left
    s "He saved the women of your tribe? Are they all hiding somewhere?"
    show sabiaemo normal at left
    t "No, they were surrendered as hostages to the shamans. You do not know this?"
    s "I never fought directly on the orc front."
    t "Tekrok is no storyteller. But Lundar tried to turn us against our own kind, offering mercy to tribes that would help them. The shamans took their offer."
    show sabiaemo normal at left
    s "And so Groknak gave them your women as hostages? That's... quite a bold move."
    t "Perhaps the only one that could have saved them. It was unpopular, but smart. But that time is passed - we accomplish nothing on our own, now we need to unify again!"
    show sabiaemo closed2 at left
    s "(I guess I bought into our own propaganda about how many orc women we'd killed. But I suppose given the current situation, that isn't all bad.)"
    show sabiaemo normal at left
    s "So, just what would you do differently?"
    t "Tekrok knows that you think he is a fool to want to challenge Lundar."
    s "..."
    show tekrok happy1 at right
    t "Heh, it is good that you do not deny it."
    show tekrok normal at right
    t "But Tekrok believes that it is others who are most foolish. Peace with Lundar? Surviving like this on the borders? Bah, even Groknak's strategies only ensure that we die a slow death, with no new children to replenish our numbers."
    t "The greatest fools of all are those who think Lundar will forget about us. Your people believe us to be vermin. You may be distracted by other threats, but when you have a chance, you will hunt us down."
    s "..."
    show sabiaemo closed3 at left
    s "Well, I don't think you're a fool when it comes to understanding Lundar. You're right, it's just a matter of time."
    t "Tekrok learned this lesson well, in his youth. He is all that remains of his tribe."
    show sabiaemo normal at left
    s "You're... not from Groknak's tribe?"
    t "No. There was another, smaller tribe that Groknak defeated. Tekrok was the Warchief's son - taken as a hostage to ensure that my tribe obeyed. So Tekrok grew up here, but he remembered his true family."
    s "And... what came of all that?"
    t "Humans slaughtered every last one of my people."
    s "...I hope you're not looking for my sympathy."
    t "No. Tekrok would spurn it if it was offered. One thing that can be said for humans: you understand that strength is what rules."
    s "So, you've gotten accepted in this tribe, become a Captain... for what? What's your ultimate goal here?"
    t "Defeating Lundar may be risky, but it is the only chance we have. If we do not form a new horde and defeat Lundar, we will all be killed."
    show sabiaemo eyebrow1 at left
    s "And you expect me to just cheer you on?"
    t "No. Tekrok understands that you will not agree to this. But Tekrok wants to challenge you honestly, not tell lies."
    show tekrok happy1 at right
    t "We can work together for now. And perhaps one day, we can stand on the opposite sides of the field of battle and decide this, once and for all."
    show sabiaemo happy1 at left
    s "Heh, we'll see."
    t "But Tekrok believes it would be better for Sabia to understand her place. We do not seek to exterminate all humans - you will have a place at our feet in the new world."
    show sabiaemo happy2 at left
    s "Don't get ahead of yourself."
    show tekrok normal at right
    t "..."
    show sabiaemo normal at left
    s "..."
    t "Tell me... do humans still tell tales of Baldar?"
    s "I don't even know who that is. Some important orc?"
    show tekrok angry1 at right
    t "Some important..."
    show tekrok normal at right
    t "No. Baldar was an orc so strong that his legends are only shadows of the truth. His deeds were so powerful that they are still remembered, even when so much else in our history has been forgotten."
    "Tekrok tapped the skulls at his waist, almost as if reminiscing."
    t "Stories of Baldar inspired many, including young Tekrok. But few had the strength to bring back his traditions. Just as he wore the skulls of his enemies, so I wear mine."
    s "You're telling me those weren't just from prisoners of war?"
    show tekrok angry2 at right
    t "Of course not! Each was won honorably on the field of battle!"
    show tekrok normal at right
    t "These are only the beginning. Tekrok will prove himself strongest, unite a new horde that will bring all to join him. When Lundar is crushed, our women will see that it is safe and return, and we will create a new kingdom."
    show sabiaemo happy2 at left
    s "Well, Sabia plans to prove herself the strongest, rule Lundar, and expand it to cover the entire continent. What do you think of that?"
    show tekrok happy2 at right
    t "Tekrok will enjoy seeing your spirit bend to serve him."
    show sabiaemo normal at left
    s "But seriously, what do we do in the short term? We can both be useful to each other, but what's the plan?"
    show tekrok normal at right
    t "Tekrok will not interfere with your efforts to gain power, and in time you may use Tekrok's forces against your family. In return, you will be Tekrok's shield hand."
    s "...shield hand?"
    t "Baldar taught that warriors must fight with both hands: the axe, and the shield. The axe is what everyone watches, what kills. But the shield is also important, pushing subtly. Both are necessary."
    show sabiaemo happy1 at left
    s "Ah, so while you bluster as a big strong warrior, you want me to apply the soft power. Makes sense."
    t "There is much we must discuss, Sabia, and much we will argue about. Perhaps this will end in blood."
    t "But for now, that is enough. Go enjoy the feast."
    hide tekrok normal with dissolve
    "Sabia moved away from Tekrok, returning to the main feast with a great deal on her mind."
    if HGNkulgan:
        call HGNkulgan_dialogue
    "Since everything seemed under control, Sabia decided that it was time to wander a little. She headed for the main hall first, to make sure that she was seen visiting the Warchief's feast."
    scene bg mainhallnight
    call sabiabase
    with dissolve
    call HGNwarchief_feast
    scene bg dajrabtentnight
    call sabiabase
    with dissolve
    call HGNdajrab_dialogue
    scene bg HGNtekrok2
    call sabiabase
    with dissolve
    show tekrok angry1 at right with moveinright
    "Sabia had barely gotten back to their feast when Tekrok approached her, fuming."
    t "That bastard... he thinks he's better than us..."
    s "He certainly got everyone's attention. But it's not like he has his own agenda, so we just have to work with him, right?"
    t "No. No, he cannot be allowed to seem the strongest."
    s "What can we do about it at this stage, though?"
    t "..."
    show tekrok happy1 at right
    t "We need a demonstration of the Horned God's fertility. Something that only you can do."
    show sabiaemo2 blush at left
    "As Tekrok started to explain what would be required of her, Sabia's face flushed. Was she really going to go through with this?"
    s "But... that's..."
    t "Are you a fool? What did you think would happen when you threw your lot in with me?"
    show sabiaemo closed2 at left
    s "..."
    "She didn't want to do it... but she also didn't want to let Dajrab win. She'd thrown her lot in with Tekrok, after all, she needed to put everything she had into the alliance, even her body. Still, even if she had to agree, she had a little choice..."
    menu:
        "Agree enthusiastically":
            $ sub += 1
            $ dom -= 1
            $ A_tekrok += 1
            show sabiaemo happy1 at left
            s "Alright... let's give them a real show!"
        "Agree submissively":
            $ sub += 2
            $ A_tekrok += 1
            $ dom -= 2
            show sabiaemo closed1 at left
            s "If that's what you think is best..."
        "Agree reluctantly":
            $ sub += 1
            show sabiaemo angry1 at left
            s "Fine - but I'm only doing it because we have to win this thing!"
    t "Good, you're learning. Then start getting ready!"
    call HGNtekrokscene
    play music orccamp fadeout 2.0 fadein 2.0
    scene bg HGNtekrok2
    show basenaked at left
    show sabiaemo closed2 at left
    "When it was over, Sabia was aching and stained with cum. After just lying there and catching her breath for a while, she was able to leave and find some privacy."
    "Though the orcs didn't drink much water, she'd placed some barrels of it in one of the smaller tents in case of fires. Sabia stripped and began cleaning herself off."
    show tekrok happy1 at right with moveinright
    t "Very good, Sabia."
    show sabiaemo surprised1 at left
    s "H-hey!"
    t "Heh... this is nothing that Tekrok hasn't seen."
    show sabiaemo closed2 at left
    s "Fine, whatever... just tell me, did it work?"
    "By the time they had finished fucking her, she estimated that it was almost dawn. Many of the warriors had exhausted themselves with her, while others were well-fed, drunk, or asleep. It certainly seemed that the Horned God's Night was nearly over."
    t "Oh, it worked alright..."
    show sabiaemo normal at left
    if orcfestivalscore >= 32:
        $ L_orcs += 5
        $ A_tekrok += 3
        $ Sabia.xp += 10
        $ dom += 1
        $ sub += 1
        show tekrok happy1 at right
        t "A perfect finish to a perfect night! No orcs will forget who gave them the grandest feast they have ever seen!"
        t "Tekrok thinks we even managed to best Dajrab's tricks. We have won!"
        s "Great!"
    elif orcfestivalscore >= 28:
        $ L_orcs += 4
        $ A_tekrok += 2
        $ Sabia.xp += 8
        show tekrok happy1 at right
        t "A perfect finish to a good night. This feast will not be soon forgotten!"
        t "Dajrab's tricks were a surprise, but Tekrok thinks we have equaled him."
        s "Great!"
    elif orcfestivalscore >= 24:
        $ L_orcs += 3
        $ A_tekrok += 1
        $ Sabia.xp += 6
        show tekrok normal at right
        t "The rest of our feast was memorable as well. It is what Tekrok hoped."
        t "Most likely, more orcs were impressed by Dajrab's tricks. But even Tekrok did not foresee this, so there is nothing that can be done. Our feast was at least as good as Rokgrid's."
        s "Good."
    elif orcfestivalscore >= 20:
        $ L_orcs += 2
        $ Sabia.xp += 4
        show tekrok normal at right
        t "Aside from that, it was a good enough feast. Respectable for a Captain."
        s "Good."
    elif orcfestivalscore >= 15:
        $ L_orcs += 1
        $ Sabia.xp += 2
        show tekrok angry2 at right
        t "The feast could have gone better. Tekrok is not pleased."
        s "Well, that isn't entirely my fault, is it?"
        t "...no. Both of us must fight harder in the days to come."
    show tekrok normal at right
    t "But now, the Horned God's Night is done. Officially we must wait until the sun rises, but that means nothing. The important part is done."
    s "And what comes next?"
    t "Fighting, but not immediately. Take some time to rest and prepare yourself for what is to come."
    jump HGNaftermath


label HGNrokgrid:
    call HGNscorefrominventory
    "The Horned God's Night began the moment the sun touched the horizon, a long horn being blown so loudly that it resonated over the entire camp. In the midst of planning, Sabia was taken a little off guard, so she hastened to finish preparations."
    show bg HGNrokgrid1
    call sabiabase
    show rokgrid happy2 at right
    with dissolve
    if orcfestivalscore >= 3:
        r "Ah, Sabia! Wonderful to see you!"
        s "I just hope we've done enough..."
        r "Please, enjoy yourself at least a little tonight! But yes, we must also speak of the competition between Captains..."
    else:
        show rokgrid angry1 at right
        "When Sabia met Rokgrid, to her surprise his expression shifted to a scowl."
        r "Sabia... I'm very disappointed in you."
        s "What?"
        r "Did I not make it clear how important this night is to us? For you to just brush it off like this..."
        s "You really expect me to give my all to some shitty festival?"
        r "Yes, I did. If this is how you're going to behave, then I'm afraid this alliance is over..."
        jump HGNbadend
    if Inventory.has_item(Furnishings) > 0:
        $ orcfestivalscore += 3
        r "I must say, I am rather impressed with all the finery you were able to add! Our feast shall be like no other!"
    else:
        r "I must admit, I was hoping you could add a little human flair to our furnishings... but no matter, the feast shall go on."
    if Inventory.has_item(HGNTent) > 0:
        $ orcfestivalscore += 3
        $ A_rokgrid += 1
        r "And this tent! I had spoken with Alioch about purchasing better ones, but you have outdone me! I am quite impressed."
    else:
        pass
    if gotHGNfood:
        r "Between the two of us, we have prepared ample supplies of food and drink. None shall go hungry or thirsty, that I promise you!"
    else:
        r "I have prepared ample supplies of food and drink. None shall go hungry or thirsty, that I promise you!"
    r "However, we might want to start the drinking with a special round. Do you have anything to suggest?"
    menu:
        "Beer" if Inventory.has_item(HGNBeer) > 0:
            $ orcfestivalscore += 1
            s "I purchased some beer that should be better than the usual orc drinks. Let's start with that."
            r "The men will certainly never complain about more beer."
        "Mead" if Inventory.has_item(HGNMead) > 0:
            $ orcfestivalscore += 2
            s "I purchased some mead that should be better than the usual orc drinks. Let's start with that."
            r "Good, that will be a change of pace for them."
        "Wine" if Inventory.has_item(HGNWine) > 0:
            $ orcfestivalscore += 3
            s "I purchased some wine that should be better than the usual orc drinks. Let's start with that."
            r "Excellent! Nothing like fine human wine to separate ourselves from the others!"
        "Nothing":
            s "Let's stick to the basics."
            r "No matter, then."
    r "I have made all the preparations - there will be plenty to drink for all!"
    if Inventory.has_item(Royalgold) > 0:
        $ Inventory.rem_item(Royalgold)
        $ orcfestivalscore += 5
        $ A_rokgrid += 1
        s "About that... I actually made something special. Have you ever heard of a potion called Royal Gold?"
        r "I confess that I have not."
        s "It's a powerful potion for putting everyone in the right mood. It fosters trust and new alliances. Obviously, I'm saying this because I have some."
        r "Ah, this is a truly exceptional contribution! Does it need to be consumed directly, or...?"
        s "No, you can mix it into alcohol or any other drink. There's no harm done if other people drink it, but I suggest that you use it on a group that already views you favorably, but you want to seal the deal. It's not magic, it can only encourage what already exists."
        r "Oh, I quite understand. Indeed, that is already the purpose I intended alcohol to serve at this feast, but I trust this will do even better."
    s "So, our preparations are complete... what now?"
    r "Now, perhaps you could try to actually enjoy yourself? Mingle with the warriors, have a drink, and so on. Feel free to visit some of the other feasts as well, though spend most of your time here."
    s "Alright. Let's celebrate the Horned God's Night, then."
    hide rokgrid happy2 at right
    with dissolve
    "Leaving Rokgrid for the moment, Sabia headed out to the campfire to speak with warriors and make sure she was seen."
    if orcfestivalscore >= 10:
        scene bg HGNrokgrid2
        with dissolve
        "The atmosphere was strange. Usually there was an aura of violence seething underneath the surface, but for once Sabia didn't really feel threatened. The orcs seemed happy, celebrating the new year without any inhibitions."
        "It was an odd experience, but she felt welcome. Orcs that were usually respectful were friendly, and even those who disliked her were polite. Most likely it would only last one night, but still..."
        call sabiabase
        with dissolve
    else:
        "The atmosphere was strange. Usually there was an aura of violence seething underneath the surface, but for once Sabia didn't really feel threatened. The orcs seemed uninterested in the feast, but they just wandered away instead of becoming violent."
        call sabiabase
        with dissolve
        "At first she thought nothing of it, but she realized that it wasn't just a temporary ebb. The orcs were leaving, making her bonfire seem lonelier and lonelier as time went on. Though the fire still burned hot, it seemed small and cold with no one around it."
        show rokgrid angry1 at right with dissolve
        r "Sabia... I'm very disappointed in you."
        s "What?"
        r "Did I not make it clear how important this night is to us? For you to just brush it off like this..."
        s "You really expect me to give my all to some shitty festival?"
        r "Yes, I did. If this is how you're going to behave, then I'm afraid this alliance is over..."
        jump HGNbadend
    if HGNkulgan:
        call HGNkulgan_dialogue
    if HGNneve:
        "While Sabia scanned the fire, without warning a drink was placed into her hand. She discovered Neve standing beside her, smiling slightly."
        show neve1 at right
        show neveemo happy1 at right
        with dissolve
        n "For someone who's helping run the show, you're really not drinking very much."
        "Sabia sipped the drink and discovered it was some kind of spiced wine, presumably something Neve brought herself. After another drink, she shook her head and gave a wry smile."
        s "Well, there's a lot at stake here. I have to stay focused."
        n "Try to have some fun too, okay?"
        s "Are you going somewhere?"
        n "I want to slip away before Rokgrid notices me and makes a big deal of my presence. But I'll make sure people know I'm here."
        s "Thanks, Neve."
        n "Not a problem."
        hide neve1 at right
        hide neveemo happy1 at right
        with dissolve
    if HGNlutvrog:
        call HGNlutvrog_dialogue
    show rokgrid happy2 at right
    with dissolve
    "Rokgrid appeared from the shadows, raising a bottle of wine."
    r "We are off to a fine start, Sabia. Care to share a drink with me before we need to put out any fires?"
    "Sabia nodded and followed him. Rokgrid quickly led her to his tent and they stepped through a partition. Though it was only a silk sheet, it managed to keep out much of the sound and light from the outside."
    s "I hope you don't mean literally putting out fires."
    r "Heh, one would hope not."
    show rokgrid normal at right
    r "If the two of us are to work together, I thought that we should speak at greater length about what we can hope to accomplish."
    show sabiaemo irritated1 at left
    s "Now? Seems premature, considering that we have to make sure this feast goes well first. And there's fighting after that, right?"
    show rokgrid normalclosed at right
    r "Heh, well, I do not consider myself superstitious, but the night of renewal seems a good time to discuss plans for the coming year, does it not?"
    s "It doesn't hurt to plan, I guess. I take it you have some master scheme?"
    show rokgrid happy5 at right
    r "Haha, hardly. But I do have plans I would enact, if I became Warchief."
    show rokgrid normal at right
    r "Warchief Groknak's strategy was logical, at one time. But as the years have passed, it has become increasingly futile. Without any females, we are doomed to die."
    s "I thought that your group seemed pretty calm about all your women being dead. Why is that?"
    r "Hmm? Our females are not dead. They are being held by the tribe of shamans."
    show sabiaemo surprised1 at left
    s "Wait, what?"
    r "Did you truly not know? I had heard Lundar told many stories of how many orc women it had slain, but I did not imagine they had spread far."
    s "I never fought on the orc front, that was before my military career. What do you mean?"
    r "Even Lundar could not fight everyone at once. They tried to induce our tribes to surrender and cooperate, and those that did received mercy. The tribe of shamans believed that it was the only hope for our people."
    s "So if your women were given to them as hostages... that was Groknak's way of keeping them alive?"
    r "Correct. We did not want to leave our lands, and at that time Groknak had not convinced everyone to join his path of nonaggression."
    s "..."
    show sabiaemo closed2 at left
    s "(I guess I bought into our own propaganda about how many orc women we'd killed. But I suppose given the current situation, that isn't all bad.)"
    show sabiaemo normal at left
    s "So, you think that the tribe needs to change its strategy now that things are more stable?"
    r "Indeed. We need to reconnect with smaller bands that still have women, but first, we need to have something to offer them. The greatest thing that we can offer is peace with Lundar."
    show sabiaemo irritated2 at left
    s "Look, if we're going to be allies, I have to be honest: I don't think there's any way that could happen."
    r "Are you so sure? You've seen yourself that Lundar is accepting new territories without having a comprehensive understanding of the situation within. What if we brokered a deal with a local lord, then joined Lundar as part of a human province?"
    show sabiaemo closed1 at left
    s "Hmm... that's not as suicidal as I was thinking, but it still sounds unrealistic to me. You think humans are going to just accept your presence?"
    r "I believe that they could, Sabia. And this is not mere idealism talking."
    show rokgrid sad1 at right
    show sabiaemo normal at left
    r "Before the chaos of the war, I was not a member of Groknak's tribe. I lived in a much smaller group, one that survived for many years near Lundar's borders without incident before other orc groups drew their ire."
    show rokgrid sad2 at right
    r "We were able to live in peace with local human villages, even trade from time to time. And there are tales that further in the past, orcs and humans even lived together."
    show sabiaemo closed2 at left
    s "I have a hard time believing that."
    r "So do many orcs. But I refuse to believe that such a thing is impossible."
    show rokgrid happy2 at right
    r "Groknak's tribe was once part of the problem, antagonizing Lundar. He succeeded in pulling us away from the brink... now it falls to me to take the next step. There can be peace with Lundar, and in our lifetimes."
    show sabiaemo normal at left
    s "Say that I believe it's possible. How exactly is it going to happen?"
    r "Well, I have a great many plans. The key thing is for us to become an accepted entity in the territories surrounding Lundar, which can take many forms. After that..."
    r "No doubt Lundar will still be uncomfortable to have so many armed warriors near its borders. At that time, I would have us sign a peace treaty that involves retreating the body of our forces to the southeast. There, we would naturally be able to collect a great many other tribes, including our women."
    show rokgrid happy3 at right
    r "From there, we would flourish! Our numbers would be restored, but more importantly our trade and productivity could vastly increase! We would become a stable potential ally for Lundar, far enough away not to be considered a threat."
    show sabiaemo happy1 at left
    s "Still seems unlikely to me... but you've given this more thought than I gave you credit for, Rokgrid."
    show rokgrid normal at right
    r "And what do you think our chances of success would be?"
    show sabiaemo normal at left
    s "Right now? They'd be low, Lundar is ascendant. But if there was another conflict... a war with Kazzak, trade disputes with Carchedon, another minotaur uprising... then Lundar might care less about what exactly you're doing."
    r "It seems to me that, given enough time, one of those must come to pass. I hope in that time, we can establish ourselves as a stable kingdom."
    "The idea of orcs being able to do that struck Sabia as unlikely, even given someone like Rokgrid in charge. She held her tongue, but his eyes narrowed slightly and he seemed to notice her skepticism."
    r "I am not naive, Sabia. I know the attitudes of humans will not change easily, and I know the violence of war will not be soon forgotten."
    show sabiaemo closed2 at left
    s "I didn't sa-"
    r "Some will have to be sacrificed, I am sure. There will be orcs we can hand over to Lundar as the source of the raiding - tell me, do you think Lundar would not notice if we sent Tekrok to them in chains?"
    show sabiaemo normal at left
    s "...I don't know what they'd think of that."
    r "There are already some connections between races, Sabia. Whoever was responsible for your betrayal, for example."
    show sabiaemo closed2 at left
    s "That was just using orcs as tools."
    r "Yes, but being tools are better than being vermin. It is a step in the right direction."
    show sabiaemo normal at left
    s "..."
    r "Orcs have always been easy targets because we often fight on our own. But I believe that will not be the case for long, and we will show that we are not warlike by nature. Come, let me show you something."
    "Rokgrid led Sabia out of their partition to a low tent. The moans and grunts within made it clear exactly what was going on, but Sabia kept following as Rokgrid swept open the entrance."
    $ hentai_scene(13,"catgirlsworking",dissolve)
    if catgirlstatus == "enslaved":
        r "We forced none of them to come here. We said all slaves were free to rest tonight, yet some of them still chose to come."
    elif catgirlstatus == "free":
        r "We forced none of them to come here. Though I believe your choice to free them was rather impulsive... look, some catgirls still chose to come."
    elif catgirlstatus == "recruited":
        r "We forced none of them to come here. This is merely an... agreement between allies, if you will."
    else:
        r "We forced none of them to come here. I said that any of those working in the tents could rest tonight, merely offered better pay than usual."
    "The lurid scene certainly did seem to be pleasurable for everyone involved. Sabia didn't let it affect her and just watched Rokgrid coolly."
    r "Orcs have desires, yes. But so do humans, and elves, and every other race. Catgirls even need others to mate with them. Agreements can be reached."
    s "What exactly are you trying to say?"
    r "Nothing, exactly. It is merely a demonstration of the fact that it is possible to find balance. We could create a different world."
    hide hentai_scene with dissolve
    "Absurdly ambitious, yet Sabia found herself smiling."
    show sabiaemo happy3 at left
    s "Big dreams. Let's focus on small steps for now, okay?"
    "Rokgrid smiled and gave a low bow."
    r "But of course."
    scene bg HGNrokgrid2
    call sabiabase
    with dissolve
    "Rokgrid left her, returning to the campfire and greeting all of his supporters. Sabia stayed a little further away, in the cool space between heat of the fire and the heat of the bodies in the tent."
    if HGNmaply:
        call sabiabase
        show maply 3 at right
        show maplyemo normal at right
        with dissolve
        "After a moment, she realized that Maply was standing not far away. The catgirl had a pleasant expression on her face, but Sabia wasn't sure if she had heard what Rokgrid said."
        s "Hello, Maply."
        show maplyemo happy at right
        maply "Hi, Saby!"
        "Sabia inclined her head toward the tent, where the moans were still quite audible."
        s "What do you think of all this? Do you agree with what Rokgrid said?"
        show maplyemo normalopen at right
        maply "I wasn't trying to listen or anything! I didn't mean to hear, but... I kinda did."
        s "And?"
        show maplyemo happy at right
        if catgirlstatus == "free":
            maply "I think it's a good thing! Usually we don't really like orcs, but the worst part about them is that they might hurt you. If these ones aren't being violent and some of us want to use them... why not?"
        elif catgirlstatus == "recruited":
            maply "I dunno about all this alliance stuff, but if they want to do it, that's fine! Usually we don't really like orcs, but the worst part about them is that they might hurt you. If these ones aren't being violent and some of us want to use them... why not?"
        else:
            show maplyemo sad1 at right
            maply "I don't think I really trust Rokgrid. The way he made everybody work off their debts... I don't know."
            show maplyemo normal at right
            maply "But the tent is fine. Usually we don't really like orcs, but the worst part about them is that they might hurt you. If these ones aren't being violent and some of us want to use them... why not?"
        show sabiaemo happy1 at left
        s "Thanks for giving me your thoughts, Maply."
        show sabiaemo normal at left
        show maplyemo normal at right
        "They paused for a moment, slightly awkward, before Sabia headed back toward one of the bonfires with Maply following her."
        call HGNmaply_dialogue
    else:
        "She wished she had someone to ask other than Rokgrid's grand designs, but there was no one nearby. After a moment, Sabia shook her head and moved on."
    if catgirlstatus == "enslaved":
        $ orcfestivalscore -= 1
    else:
        call HGNelmysceneB
        "Setting the experience behind her, Sabia returned to the main area. Though the feast was still raging, she wasn't sure if something was a little off. Sabia frowned and looked closer."
    play music orccamp fadeout 2.0 fadein 2.0
    scene bg HGNrokgrid2
    call sabiabase
    with dissolve
    show rokgrid normal at right
    with moveinright
    "Without warning, Rokgrid appeared nearby. He had a pleasant look on his face, but his eyes were serious."
    r "Sabia, we have our first problem. We're going to run out of alcohol before the night is done - I suspect theft from another feast, but I can't be sure."
    s "Then... what do we do?"
    r "I keep pretending everything is fine. You find a way to get some more. The quality doesn't matter and I don't care where you get it, just make sure you do."
    hide rokgrid normal at right
    with moveoutright
    scene bg silvertusknight
    call sabiabase
    with dissolve
    "With that, he left her alone. Sabia rushed across camp, knowing that she probably only had one option. Asking any of the Captains for booze would just embarrass her, but Jadk..."
    call HGNjadk_dialogue
    scene bg HGNrokgrid1
    call sabiabase
    "Soon the stores were replenished with no one the wiser. Sabia had been hoping for some acknowledgment from Rokgrid, but he was engaged with orc politics. Well, that was how it went."
    "Since everything seemed under control, Sabia decided that it was time to wander a little. She headed for the main hall first, to make sure that she was seen visiting the Warchief's feast."
    scene bg mainhallnight
    call sabiabase
    with dissolve
    call HGNwarchief_feast
    scene bg dajrabtentnight
    call sabiabase
    with dissolve
    call HGNdajrab_dialogue
    scene bg HGNrokgrid2
    call sabiabase
    with dissolve
    "Sabia returned to Rokgrid's campfire and monitored the feast, but it seemed that nothing else was going to go wrong. Most of the warriors were full and a little drunk, more likely to fall asleep than to fight or argue."
    "So it was probably over. Sabia breathed a sigh of relief. The Horned God's Night had been much more of a pain than she'd imagined a simple festival could possibly be."
    show rokgrid normalclosed at right
    with dissolve
    "After a while, she saw Rokgrid come to stand next to her. Though he still carried a glass of wine, he didn't look even slightly drunk. He gave her a respectful nod."
    s "So, it's over?"
    r "Some will celebrate until dawn, but yes. We've made our mark."
    s "And? How well did we do?"
    if orcfestivalscore >= 35:
        $ L_orcs += 5
        $ A_rokgrid += 3
        $ Sabia.xp += 10
        $ dom += 1
        $ sub += 1
        show rokgrid happy3 at right
        r "Excellently! This was one of the finest feasts the Horned God's Night has ever seen!"
        r "I was worried when Dajrab made such an impressive showing, but I think we managed to outdo even him!"
        s "Great!"
    elif orcfestivalscore >= 30:
        $ L_orcs += 4
        $ A_rokgrid += 2
        $ Sabia.xp += 8
        show rokgrid happy3 at right
        r "We did well! Truly a feast worthy of our tribe and the Horned God!"
        r "I was worried when Dajrab made such an impressive showing, but I think our showing matched him."
        s "Great!"
    elif orcfestivalscore >= 25:
        $ L_orcs += 3
        $ A_rokgrid += 1
        $ Sabia.xp += 6
        show rokgrid happy2 at right
        r "We did well. A worthy feast for the Horned God's Night."
        r "Dajrab surprised everyone with his grand feast, and I believe he has bested us, but that was a surprise that no one could have anticipated."
        s "Good."
    elif orcfestivalscore >= 20:
        $ L_orcs += 2
        $ Sabia.xp += 4
        show rokgrid happy2 at right
        r "We did somewhat well. A worthy feast for the Horned God's Night."
        r "Dajrab has taken the top prize with his impressive showing, of course. But our feast was at least on par with the other Captains."
        s "Good."
    elif orcfestivalscore >= 15:
        $ L_orcs += 1
        $ Sabia.xp += 2
        r "I wish that it would have gone better. Our feast was not an embarrassment, but it was a poor showing compared to the other Captains."
        s "Hey, I did my part."
    elif orcfestivalscore >= 10:
        $ L_orcs += 0
        $ A_rokgrid -= 1
        show rokgrid angry1 at right
        r "This was pathetic, the efforts of some minor warrior, not a Captain. I expected more from you, Sabia."
        s "Hey, I did my part."
    else:
        $ L_orcs -= 2
        $ A_rokgrid -= 3
        $ dom -= 1
        $ sub -= 1
        show rokgrid angry2 at right
        r "Pathetic - did you even try? I expected more from you, Sabia!"
        s "You expect me to waste my time on this stupid barbarian festival?"
    show rokgrid normalclosed at right
    r "..."
    r "Stay to watch the sun rise, Sabia. Then the Horned God's night will be truly over."
    s "And after that? I hope I'm not expected to fight the next day or anything."
    r "No, no... everyone will be sleeping this off tomorrow."
    r "But the day after that..."
    jump HGNaftermath


label HGNdajrab:
    call HGNscorefrominventory
    "The Horned God's Night began the moment the sun touched the horizon, a long horn being blown so loudly that it resonated over the entire camp. In the midst of planning, Sabia was taken a little off guard, so she hastened to begin making her final decisions."
    show bg HGNdajrab1
    call sabiabase
    show dajrab normalclosed at right
    with dissolve
    if orcfestivalscore >= 3:
        d "Sabia. There you are."
        s "I didn't realize that it would begin right away. Is everything ready?"
        d "Never fear, I have been working with our preparations for some time. All will move forward smoothly."
    else:
        d "...is this a joke to you?"
        s "What? You expected me to do more? I didn't join this alliance to plan feasts."
        d "That is fair. You can set your own priorities and pursue your own ends."
        show dajrab normalclosed at right
        d "But you will not pursue them with me. Be gone."
        jump HGNbadend
    if Inventory.has_item(Furnishings) > 0:
        $ orcfestivalscore += 3
        d "These furnishings you have provided will be quite useful. The quality is quite fine - I presume you purchased them from Vehlis?"
        s "Her slave, actually, but yes."
        if Inventory.has_item(HGNTent) > 0:
            $ orcfestivalscore += 3
            $ A_dajrab += 1
            d "And the unique tent you purchased... it will also be a useful addition. I appreciate that you have gone above and beyond in this."
        else:
            d "Well, your contribution is appreciated. Both by me now, and by the warriors who visit later."
    else:
        if Inventory.has_item(HGNTent) > 0:
            $ orcfestivalscore += 3
            "The unique tent you purchased will be a useful addition and make our feast stand out. Thank you for your contribution."
        else:
            $ A_dajrab -= 1
            d "I had hoped you would provide more in the way of unique elements to the feast, but it will not matter. I am very well prepared."
    if gotHGNfood:
        d "Though I had gathered more than enough for all the warriors to eat, your contributions will be helpful as well. Variety always impresses."
    s "Is everyone just free to eat and drink, or will it be more formal than that?"
    d "The night will begin with an opening feast, there will be moments of ritual, then it will descend into uncontrolled feasting."
    d "The initial moments of the feast, before anyone has grown drunk, will be our first chance to make an impression. Have you purchased anything you'd like to begin with?"
    menu:
        "Beer" if Inventory.has_item(HGNBeer) > 0:
            $ orcfestivalscore += 2
            s "I purchased some beer that should be better than the usual orc drinks. Let's start with that."
            d "A reasonable choice. We should stand out from all the other feasts serving orcish beer."
        "Mead" if Inventory.has_item(HGNMead) > 0:
            $ orcfestivalscore += 3
            s "I purchased some mead that should be better than the usual orc drinks. Let's start with that."
            d "A good choice. Mead will definitely stand out compared to all the orcish beer available."
        "Wine" if Inventory.has_item(HGNWine) > 0:
            $ orcfestivalscore += 2
            s "I purchased some wine that should be better than the usual orc drinks. Let's start with that."
            d "A reasonable choice. We should stand out from all the other feasts serving orcish beer."
        "Nothing":
            $ A_dajrab -= 1
            s "Sorry, no. I figured the warriors would drink what they're used to."
            d "It will be fine. I have some unique mead of my own I have been saving."
    if Inventory.has_item(Royalgold) > 0:
        $ Inventory.rem_item(Royalgold)
        $ orcfestivalscore += 5
        $ A_dajrab += 1
        s "I have something else to add: a bottle of Royal Gold."
        d "Oh? That's rather ambitious of you... I hope that it has been created for orcs instead of humans?"
        s "I made it myself based on that assumption. Give this drink to your loyal orcs and they should be primed to bond with each other even more than normal."
        d "Actually, I may give it to a circle of warriors who respect me, but are not entirely convinced. Those are the ones who need their loyalty improved."
        s "Fair enough."
        d "But this is a valuable contribution, Sabia. I will not forget it."
    s "So, what happens now?"
    d "Now, we feast until dawn. It is expected that warriors will move between feasts - we seek not to keep them at our tents alone, but to encourage them to mostly spend their time near us. It is not an exact art."
    s "I understand. Should I mostly stay here to draw warriors in, or move around?"
    d "I suggest you visit the Warchief's feast out of respect. Otherwise, feel free to move as you see fit, but I suggest remaining near our feast to provide your support."
    s "Got it. Let the Horned God's Night begin."
    hide dajrab normalclosed at right with dissolve
    "Leaving Dajrab for the moment, Sabia headed out to the campfire to speak with warriors and make sure she was seen."
    if orcfestivalscore >= 10:
        scene bg HGNdajrab2
        with dissolve
        "The atmosphere was strange. Usually there was an aura of violence seething underneath the surface, but for once Sabia didn't really feel threatened. The orcs seemed happy, celebrating the new year without any inhibitions."
        "It was an odd experience, but she felt welcome. Orcs that were usually respectful were friendly, and even those who disliked her were polite. Most likely it would only last one night, but still..."
        call sabiabase
        with dissolve
    else:
        "The atmosphere was strange. Usually there was an aura of violence seething underneath the surface, but for once Sabia didn't really feel threatened. The orcs seemed uninterested in the feast, but they just wandered away instead of becoming violent."
        "At first she thought nothing of it, but she realized that it wasn't just a temporary ebb. The orcs were leaving, making her bonfire seem lonelier and lonelier as time went on. Though the fire still burned hot, it seemed small and cold with no one around it."
        show dajrab normalclosed at right with dissolve
        d "...is this a joke to you?"
        s "What? You expected me to do more? I didn't join this alliance to plan feasts."
        d "That is fair. You can set your own priorities and pursue your own ends."
        show dajrab normalclosed at right
        d "But you will not pursue them with me. Be gone."
        jump HGNbadend
    if HGNmaply:
        call sabiabase
        show maply 3 at right
        show maplyemo happy at right
        with dissolve
        "Looking around the fire, Sabia noted Maply near the edge. She was looking around at the bustling of the feast happily, but wasn't getting directly involved herself. Sabia approached her with a smile."
        maply "Oh, hello there, Saby!"
        call HGNmaply_dialogue
    "Though Sabia had expected there to be some kind of disaster by this point, Dajrab seemed to run a very tight ship. She'd done all the mingling she'd wanted to do, though, and didn't spot anyone else she wanted to spend time with."
    scene bg mainhallnight
    call sabiabase
    with dissolve
    "Since everything seemed under control, Sabia decided that it was time to wander a little. She headed for the main hall first, to make sure that she was seen visiting the Warchief's feast."
    call HGNwarchief_feast
    scene bg HGNdajrab2
    call sabiabase
    with dissolve
    "She returned to the campfire and found things as stable as before, though it looked like a larger number of people had gravitated toward their bonfires."
    if orcfestivalscore >= 10:
        "Sabia didn't blame them - between Dajrab and her contributions, they had a nice variety. It would have been rough in Lundar, but even nobles would have found something to eat."
    else:
        "Sabia didn't blame them - Dajrab had really gone all out and they had a nice variety. It would have been rough in Lundar, but even nobles would have found something to eat."
    if HGNkulgan:
        call HGNkulgan_dialogue
    if HGNlutvrog:
        call HGNlutvrog_dialogue
    show dajrab normalclosed at right with dissolve
    "Dajrab emerged beside her, surprisingly quiet for an orc. He gave her a low nod, but his eyes were shifting."
    s "Is everything alright?"
    d "I'm getting ready for something, and I want to have as many orcs here as possible. Many of those here are rather boisterous, they need something more to hold them."
    s "And? Did you have something in mind?"
    d "Yes... but you may not like it. You have the option to refuse."
    show sabiaemo eyebrow1 at left
    s "What is it?"
    d "There was once a ritual during the Horned God's Night during which one of our women would dress up as a representation of the Horned God and dance. If you were to do so, it would both further your status in the tribe and increase the size of our feast."
    s "What's the catch?"
    d "This is what you would be wearing."
    show sabiaemo surprised1 at left
    "Sabia spent a long time looking at the outfit, if it could even be called that."
    show sabiaemo closed2 at left
    s "I see. And knowing warriors like those, I can imagine how it might go."
    d "Yes. You can refuse, or stop them. It is up to you, but I believe it would be for the best."
    s "..."
    menu:
        "Refuse":
            s "Sorry, no."
            d "As you wish."
        "Agree":
            $ HGNdajrabagree = True
            $ L_orcs += 2
            $ A_dajrab += 1
            s "Alright, fine."
            d "Good. Put this on and get ready."
            call HGNdajrabscene
            play music orccamp fadeout 2.0 fadein 2.0
    scene bg HGNdajrab2
    call sabiabase
    if HGNdajrabagree:
        "After her dance, Sabia expected the orcs to view her differently, but to her surprise, not many leered at her. She reminded herself that she had taken on the role of an orc woman: surely these warriors had memories of Nights past. They might want to fuck her, but maybe it had done something for her as well."
        "Still, it took her a while to get back into the swing of things again. Dajrab was simply gone, so she had to trust that he was taking care of what mattered. Meanwhile, she drifted around the feast to make sure that everything was going well."
    if HGNneve:
        call HGNneve_dialogue
        scene bg HGNdajrab2
        call sabiabase
        with dissolve
        if aliochnevesex:
            "Back at camp, it was easy to replace the lost supplies and the feast continued without a problem. Part of Sabia felt guilty for abandoning her duty... but the experience left her feeling so satisfied she decided that she wouldn't let it bother her."
            "But a moment later, the sky was lit up a bright green and Sabia realized that it might not even matter."
        else:
            "Back at camp, it was easy to replace the lost supplies and the feast continued without a problem. Irritating, but not ultimately a problem."
            "But a moment later, the sky was lit up a bright green and Sabia realized that it might not even matter."
    scene bg dajrabtentnight
    call sabiabase
    with dissolve
    "The sound of the bonfires had been so constant that Sabia no longer heard it, but she did hear a rush of flame that sounded far louder - and nearby. For a moment she feared that the entire camp might be set ablaze and her hand flew to her sword as her eyes flickered around her."
    "To her surprise, she saw a huge plume of green fire shoot into the air from her own bonfire. That almost confirmed her fears that the camp was ablaze, but it seemed too controlled. Another burst of green flame temporarily blinded her, but Sabia began stumbling toward it."
    "One of their own bonfires burned emerald green and larger than normal. For a moment Sabia feared some kind of sabotage, but then she got closer..."
    show dajrab normalclosed at right with dissolve
    "The others got out of her way and she saw him: Dajrab knelt before the green bonfire, apparently praying. Three enormous altars to the Horned God loomed around it, lit up a surreal green by the flames. Three priests stood in front of them, adding powder to the fire that made it flare brighter green."
    "At least the orcs seemed just as astonished as she was. Many were actively gaping, while others began to be drawn into Dajrab's feast."
    "So this was obviously a stunt to earn him more support for the coming year. It seemed effective, and Sabia should have been glad that it was helping their cause, but part of her was irritated that he hadn't told her what he was planning."
    "Then again, this was only one act. The orcs who saw the emerald bonfire seemed to consider it a comprehensible, if unusual, religious ritual. They then moved to take food and drink while they watched."
    "Dajrab slowly rose to his feet, expression somber, and nodded to all those who had gathered to watch. There was nothing but piety on his face, but Sabia could see through it - he knew exactly what he was doing."
    d "Tonight is dedicated to the Horned God. Please, enjoy yourselves and renew your strength."
    "His voice was quiet, yet it carried to everyone. His expression remained calm, though she imagined that he must be smug as hell."
    "Even Tekrok and Rokgrid had come to see what was going on, and they looked pissed. Sabia edged closer to overhear their conversation and heard Dajrab speaking of order and unity."
    "Apparently he was trying to establish himself as the most responsible, neutral power. He might not become a leader that way, but he'd establish himself as someone that anyone who did want to lead needed to take seriously. So that was his approach."
    hide dajrab normalclosed at right with dissolve
    "As soon as she understood it, Sabia left the Captains to him and went to speak with other warriors. Her opinion might not be the most important factor, but she could at least feed into the image he wanted to project."
    "She mingled with the warriors and realized that his strategy had been effective. Her presence only seemed to support Dajrab's position, making him seem rational and with a large base of support."
    "Sabia played her part until abruptly she realized that the orc in front of her was Dajrab himself."
    show dajrab normalclosed at right with dissolve
    d "Dajrab thanks you, Sabia. This would not have been possible without you."
    "While Sabia stood in numb shock, Dajrab shook her hand firmly. All the orcs at the feast were staring at them, or more specifically at her. She saw new respect in his eyes - too much of it, Dajrab was lowering his own status by putting so much attention on her."
    scene bg HGNdajrab1
    call sabiabase
    show dajrab normalclosed at right
    with dissolve
    "Abruptly Dajrab put an arm around her shoulders and drew her away, toward his own tent."
    d "Come, Sabia. Dajrab has many questions for us to discuss."
    s "Of... course."
    "They moved away from the main crowds, around the bonfire. Though its glow had returned to normal, flecks of the powder still occasionally caught flame, resulting in a burst of jade."
    "Dajrab stared into the flame a while, saying nothing, then turned away and moved into his tent. Sabia followed and found it lowly lit, a peaceful purple shade compared to the stark black and red outside."
    s "What was that about?"
    d "You did this to further your own reputation, yes?"
    s "Right, but what do you get out of it?"
    d "As I said outside, I have no interest in leading the tribe. I seek not to attract glory to myself, but to prove myself the leader of a faction that cannot be ignored. That includes you."
    show dajrab happy at right
    d "Besides, if your plan is successful, you could be a valuable ally long after you have left the orc tribe."
    show sabiaemo irritated2 at left
    s "My plan is that clear to you?"
    show dajrab normalclosed at right
    d "Let me see if I cannot guess."
    d "Betrayed by someone in your family, you need to build a new base of support. You wish to begin by gaining some control over this tribe, which you will use either directly or as an outside threat when you make a bid to strike back against those who betrayed you."
    d "At a minimum, you plan to use us for security while you acquire other resources. No doubt you were pleased to meet Vehlis, though I doubt you would embrace Carchedon as a whole. No, I would guess that you intend to fund your own allies within Lundar, strike back against your betrayers before the matter can come down to legal process or all out war."
    d "Is that close?"
    show sabiaemo closed2 at left
    s "..."
    show sabiaemo normal at left
    s "More or less. You missed some key details, but I'm not going to explain them to you."
    d "Nor would I ask you to. I simply want to be clear that I understand you are making use of us. If this alliance is to be functional, you must be useful to me as well."
    s "And what exactly does that mean?"
    d "Our tribe needs change, but change is also likely to be what destroys it. You, in all you have done so far, are likely to be an agent of change. That change must not go too far."
    show sabiaemo closed1 at left
    s "Well, I respect that you're being straightforward with me. But not entirely: what exactly is it that you want?"
    d "The continued survival of the tribe, at minimum. But survival is not enough, we need to escape... our current situation."
    show sabiaemo eyebrow1 at left
    s "Why not just come out and say it? You're stagnating."
    show sabiaemo annoyed1 at left
    s "Personally, I don't get it. How can you all just sit here, acting like nothing is wrong, when the entire orc race is dying?"
    d "..."
    show dajrab normalclosed at right
    d "To understand that, you must understand the history of this tribe better, and of Warchief Groknak in particular."
    show sabiaemo normal at left
    s "..."
    show dajrab normalopen at right
    d "Groknak was not the first leader of this tribe. When he was a young man, his father was a strong Warchief, and his brother was in line before him. But they felt the attacks of Lundar and sought to fight back."
    d "His father sought to challenge Lundar and had some success... at first. But as legion after legion came, they soon captured him. He was killed in the center of the capital and his body was paraded in the orc campaigns for years to come."
    show dajrab normalclosed at right
    s "I don't remember that specifically, but there were a lot of things like that at the time. Don't pretend the orcs didn't do the same thing."
    show dajrab normalopen at right
    d "Did I say anything to suggest that?"
    s "..."
    d "Groknak's brother sought revenge, and built an impressive force of different tribes. But of course, by that point, it was much too late."
    d "After they were defeated, Lundar began targeting the tribes that had led the alliance, attempting to cripple us as a people. And you came rather close, in some parts of the country. In a matter of days, Groknak lost his brother, his mother, and two sisters."
    show dajrab normal at right
    d "And so he vowed never to let such a thing happen again."
    show sabiaemo surprised1 at left
    s "I... I see..."
    show dajrab normalopen at right
    d "Many warriors believe Warchief Groknak is old, tired, or simply foolish. Because they did not see what he saw, or learn the lessons of the war as thoroughly as he did."
    d "If not for his leadership, we would likely have been wiped out entirely. And so Groknak chose a partial surrender: he sent our women as hostages to the tribe of shamans. Since Lundar had an alliance with them, they could not be targeted."
    show dajrab normalclosed at right
    show sabiaemo surprised1 at left
    s "Lundar had an alliance with a tribe?"
    d "...this is news to you?"
    show sabiaemo normal at left
    s "I never fought on the orc front. They always said that orcs would eagerly fight their own kind, but I didn't imagine it would extend to an alliance..."
    d "Not a stable one, but yes. It was a major concession, but it allowed Groknak to take us from a state of total war to this present peace."
    show sabiaemo closed2 at left
    s "(I guess I bought into our own propaganda about how many orc women we'd killed. But I suppose given the current situation, that isn't all bad.)"
    show sabiaemo normal at left
    s "So, what's your point? Because just living like this dooms the orcs as much as attacking Lundar."
    d "Yes. Groknak has focused so much on one danger that he wanders perilously close to the threat on the other side. Likewise, the Captains who hope to replace him are focused on only one threat."
    show dajrab normalopen at right
    d "I seek to ensure that the tribe walks between both extremes. That is the only hope for our future."
    show dajrab normalclosed at right
    s "That's reasonable, but what's your ultimate plan? You don't think Lundar will make peace, do you?"
    d "No, but they might withdraw if they had higher priorities. You do not believe that Lundar stopped pushing into minotaur territory because everything was won, did you?"
    s "Well, the threat was broken, but there were obviously other factors involved. It wasn't worth it to keep fighting after they had been beaten."
    d "Precisely. Lundar would also enslave the rest of the elves and push out the catgirls from the continent, if it had its way, but no kingdom is omnipotent. All I must do is place the orcs far enough from their reach that it is not worth it to pursue us."
    show sabiaemo happy1 at left
    s "Have to admit, that's actually a rational plan. I think we can get along."
    d "And if your plan is successful, and you take back your former position... what path would you push Lundar toward?"
    show sabiaemo closed2 at left
    s "..."
    d "Groknak and the other Captains make the mistake of viewing Lundar as a single entity. Indeed, that is the image you project. But I know better - it is a mess of conflicting motives and goals, just as the orc tribes are."
    show sabiaemo normal at left
    s "You're right. And look, I'm not going to make any promises."
    show sabiaemo happy3 at left
    s "But... I no longer feel the orcs are necessarily an imminent threat."
    show dajrab happy at right
    d "Good."
    show dajrab normalclosed at right
    d "This tribe is fractured and no longer knows what it is. Likewise, I believe that Lundar does not truly know itself."
    d "In a thousand years, historians will identify what all of us were. But for now, I believe all we can do is try to bend things, in some small way, in a better direction."
    show sabiaemo normal at left
    s "You have a deal, Dajrab."
    "Not eager to return to the party outside, Sabia lingered a while longer and they chatted about lighter matters. Dajrab remained dour, but he reminded her in a way of some older warriors she had known. He wasn't bad conversation, if she was honest with herself."
    "When they were done talking, Sabia realized that the sky was beginning to grow lighter. Had so much time really passed so quickly?"
    "Of course, it didn't seem to be a surprise to Dajrab at all. No doubt he had planned his spectacle for the ideal time when the majority of the warriors were still sober to appreciate it, but late enough that it would leave a lasting final impression on their minds."
    "An absurd thought crept into Sabia's head: that her mother might have approved of Dajrab. In his orcish way, he understood the politics of appearance in a way that Sabia never had."
    "A moment later she realized how foolish that thought was: of course her mother could never look past Dajrab's race. The fact that Sabia could overlook it was a sign of just how much her frame of reference had shifted. Shaking her head, Sabia decided to focus on the present."
    s "So, the Horned God's Night is almost over, and everything went according to plan. Did you even need my help?"
    d "Need? No..."
    if orcfestivalscore >= 35:
        $ L_orcs += 5
        $ A_dajrab += 3
        $ Sabia.xp += 10
        $ dom += 1
        $ sub += 1
        d "But our feast was immensely improved by all of your work. I thank you for your assistance."
    elif orcfestivalscore >= 30:
        $ L_orcs += 4
        $ A_dajrab += 2
        $ Sabia.xp += 8
        d "But my feast was immensely improved by all of your work. I thank you for your assistance."
    elif orcfestivalscore >= 25:
        $ L_orcs += 3
        $ A_dajrab += 1
        $ Sabia.xp += 6
        d "But the feast was much improved by your efforts. Thank you for your work."
    elif orcfestivalscore >= 20:
        $ L_orcs += 2
        $ Sabia.xp += 4
        d "But the feast was improved by your efforts. Thank you for your work."
    elif orcfestivalscore >= 15:
        $ L_orcs += 1
        $ Sabia.xp += 2
        d "But you made an effort to help. Thank you for that."
    elif orcfestivalscore >= 10:
        $ L_orcs += 0
        $ A_dajrab -= 1
        d "But you have allied yourself with me. We will have to work together more closely in the future."
    else:
        $ L_orcs -= 2
        $ A_dajrab -= 3
        $ dom -= 1
        $ sub -= 1
        d "But your presence did make some difference and I thank you for your help, such as it was."
    s "Do you have anything else up your sleeve?"
    d "No, the time for action is past. Religious warriors will wait to greet the first rays of dawn, while many are already unconscious. They will sleep until it is time for blood."
    s "That sounds more ominous than I hope you intended."
    d "You will have time to learn of the arena soon enough, Sabia. For now, rest."
    jump HGNaftermath


label HGNlutvrog_dialogue:
    call sabiabase
    show lutvrogbase at right
    show lutvrogwraps at right
    show lutvrogwrists at right
    show lutvrogemo normal at right
    with dissolve
    "As Sabia looked around the campfire, she was glad to see Lutvrog present. He drank sparingly and sat somewhat apart from the other warriors, but whenever someone spoke to him, it was with respect."
    "His presence here was useful... and perhaps more importantly, Sabia was just glad to have him around. There was at least one orc who wanted nothing from her but what he said up front. Sabia smiled and moved to sit beside him."
    s "Enjoying yourself?"
    lut "More than Lutvrog expected, yes. Thank you for convincing me to come."
    s "Is this not usually your sort of thing?"
    lut "No. The \"strength\" this feast celebrates strikes Lutvrog as something more akin to \"luck.\" Lutvrog prefers the test of arms that will follow."
    s "I got a hint of that. What exactly is it?"
    lut "You will see soon enough. Perhaps we will speak with one another more at that time."
    s "Sounds good. I do have a lot on my mind right now."
    if orcalliance == "sabia":
        lut "Yes... you have chosen to take a step into orc politics."
        s "I could just be hosting a feast to let everyone get to know me."
        lut "Lutvrog is not a fool."
    else:
        lut "Yes... you have become entangled with the captains."
    s "You disapprove?"
    if orcalliance == "rokgrid":
        lut "Perhaps Rokgrid would be a good leader. He understands that there are many tools of war and will not waste orc lives idly."
    elif orcalliance == "tekrok":
        lut "Perhaps Tekrok could be a good leader. He certainly values strength, Lutvrog simply fears he desires a battle that is beyond him."
    elif orcalliance == "dajrab":
        lut "No. Dajrab strives to manipulate less than the others."
        s "But he's not purely neutral."
        lut "No. He cannot be, in his position. Lutvrog would not presume to guess what someone in that position is thinking."
    if orcalliance == "sabia":
        lut "Lutvrog has chosen not to engage with such things. You might be a purer warrior if you chose to avoid politics... but Lutvrog sees that you think that path is not available to you."
        s "No, it's not. I lost that chance when I was betrayed."
        "Lutvrog noted what she said and the bitterness in her voice, but didn't comment on it directly. Letting some emotion through had probably been a mistake, but Sabia shrugged it off. It didn't matter with Lutvrog."
        lut "To answer your question... Lutvrog does not disapprove. These things always endure, just as war endures. It is a part of life."
    else:
        s "..."
        lut "But it is no matter. These things always endure, just as war endures. It is a part of life."
    s "Well, maybe after this we can get to the parts of life you prefer."
    "She'd meant to tease him a little, and it seemed that she finally got through. Lutvrog's eyes, normally so disciplined, flickered over her, and she could imagine what he was thinking about. Definitely the same thing she was thinking about."
    lut "Sabia..."
    s "But perhaps not during the Horned God's Night."
    lut "No. There will be other chances."
    "Sabia wanted to lean closer to him, but there were plenty of eyes on her. Better not to start anything that could distract from the feast she had worked so hard to prepare."
    "But she felt hot, and it wasn't because of the fire. Sabia got up and moved on, but let her hand trail over the large muscles of Lutvrog's back as she walked away."
    hide lutvrogbase at right
    hide lutvrogwraps at right
    hide lutvrogwrists at right
    hide lutvrogemo normal at right
    with dissolve
    return


label HGNkulgan_dialogue:
    show orcbase at right
    show orcloincloth at right
    show orcpiercing at right
    show orcshoulder at right
    show orcstrap at right
    show orcwrap at right
    show orcbeard1 at right
    show orcemo normal at right
    with dissolve
    "Looking around the campfire, Sabia spotted Kulgan and clapped him on the shoulder in greeting. He gave her a respectful nod."
    kulgan "Thank you again for all you have done."
    s "Are you going to keep thanking me for that? I didn't think orcs had life debts."
    kulgan "It is not only that. Kulgan thanks you for ending the trial, and for bringing change to the tribe."
    s "Bringing change?"
    kulgan "Warchief Groknak protected us well when Lundar was attacking. But now, we need something new. Kulgan thinks you may lead it to happen."
    s "Huh... thank you for the trust in me, then."
    hide orcbase at right
    hide orcloincloth at right
    hide orcpiercing at right
    hide orcshoulder at right
    hide orcstrap at right
    hide orcwrap at right
    hide orcbeard1 at right
    hide orcemo normal at right
    with dissolve
    return


label HGNmaply_dialogue:
    s "Are you getting enough to eat? Don't let the orcs push you around."
    maply "Don't worry about me! I'm small, I don't need to eat as much as these huge orcs!"
    "Sabia noticed that Maply was drinking from a flask of her own and raised an eyebrow at it. Maply shook her head and grinned."
    maply "It's nothing special. Take a sniff."
    "She extended the flask and Sabia dutifully smelled it. Whatever the liquid was, it had a fruity smell and only the lightest sense of alcohol."
    maply "If catgirls drink alcohol for orcs or humans, we go out like a light."
    show maplyblush at right
    maply "Can't really hold our liquor, hehehe."
    s "Makes sense to me. This orc stuff is a little strong for me, too, and I'm a lot bigger than you."
    hide maplyblush at right
    maply "I think you could drink a lot if you tried, Saby!"
    s "That name again... why do you keep calling me that? You know my name is Sabia, right?"
    maply "Yeah, sure, but it feels really formal to call you that. You need a personal name, so... Saby!"
    s "Hmm... does that mean you have another name?"
    maply "Yup, my mother named me Maple! But I don't really like how it sounds - call me Maply!"
    s "So which one is your real name?"
    maply "They're all my names, Sabim!"
    s "Wait, what does that one mean?"
    maply "Not telling, hehehe!"
    s "Fine, I know better than to argue with you... you have any other names?"
    maply "Oh, a bunch. If I got famous enough, people might even call me Maplana!"
    s "So... \"Sabiana\" would be a good thing?"
    maply "Yup! That's for pretty serious things, though."
    "Maply took another drink from her flask cheerfully. Sabia chatted with her for a while longer before moving on."
    hide maply 3 at right
    hide maplyemo happy at right
    with dissolve
    return


label HGNjadk_dialogue:
    show jadkbase at right
    show jadkemo normal at right
    with dissolve
    "She found Jadk laughing with a group of older orcs, and he waved her over as soon as he saw her enter. Sabia jerked her head away, though, and he approached her with a more serious expression."
    jadk "Is something wrong?"
    s "Nothing serious. But..."
    "When she explained the situation, Jadk nodded, understanding immediately."
    if A_jadk >= 5:
        $ orcfestivalscore += 2
        jadk "That's how it goes - orcs love their booze, gwahaha!"
        s "I know it's an imposition, but could you lend me something...?"
        "Instead of answering, Jadk swung to look at the group of old orcs around his table."
        jadk "Boys! Sabia just invited us over to her party - anyone game?"
        "For a moment Sabia was horrified as the orcs chorused agreement and clambered to their feet. But then at Jadk's direction they began picking up casks of beer and carrying them toward her campfire."
        "As he joined them, Jadk gave her a wink over his shoulder, then he was gone. Sabia breathed a sigh of relief - one problem down."
    else:
        jadk "That's how it goes, gwahaha! Take a cask from the back, on the house!"
        s "Thank you so much!"
        "Grabbing a cask, Sabia managed to heft it over her shoulder and then headed back to her campfire. Thanks to Jadk's kindness, that was one problem down."
    return


label HGNwarchief_feast:
    "As expected, it was quite impressive. Quantity over quality, to her eye, but he certainly had quantity. Tons of orcs were tearing into pieces of meat while others were already laughing and wrestling drunkenly."
    "Avoiding those groups, Sabia instead approached the head of the hall, where the important people would be. It was easy to spot the Warchief due to his height, so Sabia zeroed in on him."
    show groknak happy at center
    show vehlis normal at right
    with dissolve
    "To her surprise, when she got close, she saw that he was talking to Vehlis. The Carchedonese merchant seemed undisturbed by being in the center of the raucous feasting. She was wearing the same clothes, but at least she hadn't brought her book along with her."
    g "But will they act? Surviving the desert is one thing, but marching over it is quite another."
    vehlis "That is the question, of course. Personally, I would bet that it won't go beyond this."
    call sabiabase
    "Whatever they had been talking about, they stopped as Sabia drew near. Both nodded to her politely, which she hoped would help her reputation. But Sabia set such thoughts aside and just focused on the conversation."
    s "You two seem to be getting along."
    g "Of course!"
    vehlis "I may have been away for some time, but the Bank of Talos has had a relationship with this tribe for some time. Of course we get along."
    "The idea of Carchedon treating a band of orcs as seriously as it did Lundar turned Sabia's stomach, but she set her emotions aside and just smiled at them both."
    s "I hope you can finish all the business you'd planned and more. I'm just surprised you'd attend a feast as wild as this without any concern for your safety."
    vehlis "Oh, but I'm here with the Warchief himself. I'm perfectly safe."
    g "Hah! No orc would be fool enough to harm a representative of the Bank of Talos."
    vehlis "Well, there were orcs that foolish once. Past tense."
    "Sabia believed that completely, as the Bank was notorious for retaliating against anyone who broke the terms of its agreements. Did Vehlis have to look so smug about it, though?"
    g "Our kind respects strength, Sabia. We understand that strength can be more than strength of arms."
    "Treating with Vehlis was supposed to have been her special edge, but Sabia realized that she'd failed to understand the full situation. She made polite conversation with the two of them before moving to mingle a little with the others in the main hall."
    "Though it didn't seem as large as the Captains' feasts, Sabia realized just how many people were passing through to pay their respects. Warchief Groknak might be a declining leader, but his power was not inconsiderable."
    "As she left the main hall, Sabia did her best to keep that in mind."
    scene bg silvertusknight
    call sabiabase
    show orcshaman normal at right
    with dissolve
    "On her way back, Sabia noticed the shaman had his own fire. It had a number of shrines and bowls for religious rituals, but seemed poorly attended. Sabia let herself feel a little smug, since she knew that she had done a lot of damage to his reputation."
    show orcshaman angry1 at right
    "Before Sabia could slip away, however, the shaman saw her and glared."
    orcshaman "Come to gloat, have you?"
    s "..."
    menu:
        "Domination: Mock him":
            $ dom += 1
            show sabiaemo eyebrow1 at left
            s "Are you sure you can afford to be so unkind? Your feast could use a warrior like me."
            show orcshaman angry1 at right
            orcshaman "Be gone, human wench! Do not profane the Horned God's Night with your filth!"
            "Smirking, Sabia took her leave. She had more important things to be doing than wasting time on him."
        "Submission: Try to make peace":
            $ sub += 1
            show sabiaemo happy1 at left
            s "I just figured I would stop by - shouldn't we be able to put our differences aside tonight of all nights?"
            orcshaman "No. Be gone, human filth."
            "Shaking her head, Sabia left his camp. She had more important things to be doing than wasting time on him."
        "Make a brief offering to the Horned God":
            $ L_orcs += 1
            s "Am I not allowed to make even a brief offering?"
            "The shaman looked uncomfortable, but didn't refuse her. Sabia knelt down before the fire with only a vague idea of what to do, but she'd seen a few other warriors kneel before it."
            "There was a bowl of fine powder set by the fire. Sabia took a pinch and threw it into the flames, which briefly crackled green. After a moment with her head bowed, she got up and left without acknowledging the shaman's glare."
            "She didn't give a shit about the Horned God, but the religious orcs near the fire had seen her give the offering and they seemed to approve. Best to help chip away at the shaman's authority a little more."
        "Ignore him":
            "Sabia simply rolled her eyes and left his feast. She had more important things to be doing than wasting time on him."
    return


label HGNneve_dialogue:
    "While Sabia scanned the fire, without warning a drink was placed into her hand. She discovered Neve standing beside her, smiling slightly."
    show neve1 at right
    show neveemo happy1 at right
    with dissolve
    if orcalliance == "sabia":
        n "For someone who's running the show, you're really not drinking very much."
    else:
        n "For someone who's helping run the show, you're really not drinking very much."
    "Sabia sipped the drink and discovered it was some kind of spiced wine, presumably something Neve brought herself. After another drink, she shook her head and gave a wry smile."
    s "Well, there's a lot at stake here. I have to stay focused."
    show neveemo closed1 at right
    n "That may be true. But if you never take a moment to relax, then what are you doing this all for?"
    s "Huh."
    show neveemo normal at right
    "Mulling that thought over, Sabia bought time by taking another sip."
    show sabiaemo sad1 at left
    s "You seem like the kind of person who can just enjoy herself, Neve. I'm not quite like that."
    n "What do you mean?"
    show sabiaemo closed4 at left
    s "I have to be moving in some direction. If I'm not aiming for something, then I can't really enjoy myself."
    show neveemo happy1 at right
    n "So you're saying the journey is more important than the destination?"
    show sabiaemo pout3 at left
    s "I guess I did just say that, but I still feel like it's not what I meant. The destination matters. It's what I'm looking toward. It's why I do everything I do."
    show neveemo normal at right
    n "And what is that destination? And don't say anything about your family. Past that, what do you really want?"
    show sabiaemo sad1 at left
    "Sighing, Sabia stared into the fire a while and drank a little more. Neve didn't pressure her, just taking a drink herself. After a while, Sabia took a deep breath."
    s "I'm really not sure. People have always been looking at me and expecting a lot... my mother, my commanders, even my sister... my goal has always been to measure up."
    show neveemo sad at right
    n "That sounds like a difficult way to live."
    show sabiaemo sad2 at left
    s "I envy you a little, you know. You seem... very free. You enjoy your life for what it is, not what you hope it might be. I'm not like that."
    show neveemo smirk1 at right
    n "You can't even compliment someone without comparing yourself? You really are bad at relaxing."
    show sabiaemo normal at left
    "Despite herself, Sabia smiled slightly at the teasing. It was impossible to be too upset with Neve."
    show neveemo happy2 at right
    n "Are you enjoying the wine, at least?"
    show sabiaemo happy1 at left
    s "Yes, I am. It's nice... so much of what the orcs drink is like hitting yourself in the face with a brick, this is soft by comparison."
    n "Hitting yourself in the face with a feather?"
    s "Heh."
    "The two of them talked longer than Sabia had planned, about nothing in particular. Neve didn't press her, just let her ramble about whatever she wanted. Though Sabia enjoyed herself, after a while she realized that she was entirely too relaxed."
    show sabiaemo irritated1 at left
    "She narrowed her eyes at the other woman, wondering if this was what she had planned. Get her relaxed and slightly drunk, loosen her tongue, get some information from her. Had that been her aim all along?"
    show sabiaemo normal at left
    "But when she looked carefully, Sabia couldn't see that at all. Neve was watching her with a pleasant smile on her face, her eyes dancing in enjoyment. She was doing this just because she wanted to."
    s "Neve..."
    n "Hmm?"
    show sabiaemo happy1 at left
    s "Thank you. This was fun."
    show neveemo happy3 at right
    n "Why the past tense? Is there anything so pressing that you absolutely have to leave?"
    "Just as Sabia started to answer, fate intervened. Two orcs got into a wrestling match that upended an entire table of food, sending it scattering over the fire and dirt. Though most who saw it laughed uproariously, that meant they were down an entire table of food."
    "Given the amount of time left in the night, that would be a problem. Sabia sighed, set down her drink, and got to her feet."
    scene bg tradinglodgenight
    call sabiabase
    show sabiaemo normal at left
    with dissolve
    s "Sorry, Neve. I need to go resupply or people will start wandering off."
    show neve1 at center
    show neveemo normal at center
    with moveinright
    "But as she tried to walk away, she wobbled a little. Her head was only pleasantly warm, but it seemed the wine had gone to her head a little. But before she could fall, Neve appeared beside her, an arm around her back, stabilizing her."
    n "Alright, where are we headed?"
    show sabiaemo sad1 at left
    s "You don't have to help, I'll be fine..."
    n "No, I want to. We were having fun, why should we stop now?"
    show sabiaemo normal at left
    "Recognizing that Neve was not to be denied, and not particularly wanting to deny her, Sabia shrugged and let herself lean against the other woman a little more."
    s "I have a deal with Vehlis to resupply, but I need to go collect it. Her servant is supposed to be in one of the central tents in the upper camp."
    show neveemo happy1 at center
    n "Off we go, then."
    s "I'm not really drunk... it's just been a while since I drank for fun."
    show neveemo smirk1 at center
    n "Yes, I can imagine that you usually knock back drinks with a scowl on your face."
    show sabiaemo happy1 at left
    s "Heh... really, though, social engagements become serious business when you get into the political side of things. I'm not very good at it, but I understand that. You can't just drink with friends like you're on the campaign trail."
    "Neve gave her a sympathetic look from the corner of her eyes and Sabia realized that she understood. She had no doubt encountered plenty of elven politics, and Neve obviously understood the value of a good casual drink."
    show sabiaemo happy3 at left
    s "Neve... thanks."
    "The other woman just smiled and squeezed her shoulders a little tighter, not ruining it by saying anything and for once not teasing her. The warm feeling in her head grew stronger as they came closer to the tent."
    "Once outside, though, Sabia pulled away from Neve."
    show sabiaemo normal at left
    s "I can't go in looking like I'm drunk. I'll be back in just a moment."
    n "I'll help you carry things back."
    hide neve1 at center
    hide neveemo normal at center
    with dissolve
    scene bg storeroom
    call sabiabase
    show alioch normal at right
    with dissolve
    "Sabia walked into the tent and found Alioch sorting through the supplies. They seemed to have been largely depleted, which meant Vehlis must have done good business. Hopefully there would be enough left for her to replace the food."
    alioch "There you are. I assume that you're in need of more supplies than planned?"
    show sabiaemo annoyed2 at left
    s "Orcs knocked some things over and I need another table of food. Go figure."
    alioch "Yes, we brought extra stock on the assumption that this might happen. Just sign here and we'll make all the arrangements after the fact."
    show sabiaemo normal at left
    s "This falls under our prior agreement, right? I th-"
    n "Sabia, wait!"
    show neve1 at center
    show neveemo irritated2 at center
    with moveinleft
    n "You can't trust these Arwan bastards. They'll promise you everything and leave you with nothing."
    show alioch angry at right
    alioch "This has nothing to do with you, Vegardan."
    n "Oh, but it does. I'm not going to let you cheat my friend."
    alioch "Is this true, Sabia? You're friends with this Vegardan filth?"
    show sabiaemo surprised2 at left
    s "Do... do you know Neve?"
    alioch "I know her kind. They've been backstabbers ever since they came to this continent. If she's pretending to be your friend, it's because she wants something from you."
    n "Oh, please. Arwa was almost overrun before we came and saved your hides. You paid back our sacrifice with betrayal."
    show alioch eyebrow1 at right
    alioch "You're very concerned with history, for a woman living in the camp of her people's mortal enemies. But I'm not surprised... as soon as you Vegardans lost your cities here, you threw yourselves to whoever would take you."
    show neveemo smirk1 at center
    n "And I'm not surprised to see you in a slave's collar."
    show sabiaemo surprised1 at left
    n "It's ridiculous for you to act so pompous when you just hide on your island. If you weren't a slave to the Bank of Talos, you wouldn't last a day here."
    n "The orcs may be rough brutes, but at least they're true warriors. You won't find them begging us to save them like Arwans. But you never could fight your battles, could you?"
    show alioch eyebrow2 at right
    alioch "Right, you're so noble, selling your sword to the orcs... or do you just sell them your body?"
    show neveemo happy2 at center
    show sabiaemo sad1 at left
    n "That's rich, coming from a pleasure slave. Tell me, does Vehlis even use your little cock, or does she strap something on and fuck your ass?"
    show alioch angry at right
    alioch "Mistress Vehlis is a woman of refinement. She has nothing to do with your pathetic fantasies."
    show neveemo happy3 at center
    n "Oh, yes, she obviously likes nice things... you had better hope she doesn't sleep with any orcs while she's here, or she'll trade up and leave you behind."
    show alioch eyebrow1 at right
    show sabiaemo closed2 at left
    alioch "That's laughable. The least of Carchedon's pleasure slaves would blow your whorish tricks out of the water."
    n "Insulting my people is one thing, but insulting my sexual technique? That cannot stand!"
    show alioch eyebrow2 at right
    alioch "You couldn't even get me ready for Mistress Vehlis, Vegardan."
    "Sabia had been watching in silence, filled with mixed feelings. Part of her saw it as proof of what Lundar always taught: elves were obsessed with petty divisions. Another part of her was irritated to see the two of them arguing, and more of her was just wondering where it would end."
    show neveemo happy3 at center
    "She didn't expect Neve to suddenly turn to her with a sultry look."
    n "We were just talking about how you needed to relax... you want to show this pompous bastard real sex?"
    show sabiaemo surprised1 at left
    show sabiaemo2 blush at left
    s "Wh-what? You two were serious?"
    n "Of course I am! We can't let him get away with insulting us like that!"
    show alioch eyebrow2 at right
    alioch "I have nothing against Sabia. But maybe if she joins in I'll actually get hard enough to feel anything inside your loose cunt."
    s "W-wait, this is moving too fast..."
    show neveemo smirk1 at center
    n "Let's make it a contest: if you come first, Sabia gets all the supplies for free!"
    alioch "Please, that's not even a risk."
    s "But..."
    menu:
        "Agree":
            $ A_neve += 1
            $ aliochnevesex = True
            "Her head was spinning and her body was still flushed. Sabia knew she wasn't that drunk, though, she was still in control of herself. It was the idea that was tantalizing her..."
            "She had already seen Alioch with Vehlis, and the idea of spending time with Neve was intriguing. After a moment, Sabia smiled and realized that she'd already made her decision."
            show sabiaemo happy3 at left
            s "I... okay..."
            call nevealiochsabia
            play music orccamp fadeout 2.0 fadein 2.0
            scene bg storeroom
            call sabiabase
            show sabiaemo happy3 at left
            show sabiaemo2 blush at left
            show nevenaked1 at center
            show neveemo happy3 at center
            show alioch happy at right
            with dissolve
            "The three of them pulled apart, still flushed and panting from their experience. Sabia scrambled for her clothes and Alioch had little to put back on, while Neve didn't bother, just standing nude in the center of the tent."
            "Sabia had never done anything quite like that, but it left her feeling incredible. Unfortunately, she didn't have long to bask in it before the realities of the situation returned to her."
            s "Uh... that ended inconclusively, didn't it? Do I still get the supplies for free?"
            alioch "Oh, they're covered under our previous agreement. It was never going to be a big deal."
            show sabiaemo surprised1 at left
            hide sabiaemo2 blush at left
            s "Wait, seriously? Neve, did you know all that?"
            n "No, I honestly came in to try to keep you from being cheated. You really can't trust Arwans."
            alioch "And you're still bandit scum, Vegardan."
            n "And you're still a degenerate horse-fondler. I apologize for the small dick comment and nothing else."
            s "Wait, horse-fondler? Did you just make that up, or...?"
            alioch "Might be easier not to meddle in elven business, Sabia. Let's get you those supplies, shall we?"
            show sabiaemo normal at left
            "Sabia did the minimal paperwork and then helped them carry her supplies back to the bonfire, contemplating everything that she'd heard."
            "She had always been under the impression that Arwan and Vegardan elves hated each other utterly, until they had joined the horde to attack Lundar. Now, she was beginning to think there was more to their factions than superficial differences."
            "Whatever had passed between the two groups, it went deep... and strange. Sabia shook her head and put it out of mind for the time being."
            s "Thanks for everything, Alioch. This... isn't going to be a problem with Vehlis, is it?"
            alioch "Oh, don't worry about that. Mistress Vehlis has kept me as her slave for over ten years, she isn't going to get upset about this."
            s "Alright, then. We'll talk more later."
            return
        "Stop it":
            $ dom += 1
            $ A_neve -= 1
            $ A_vehlis -= 1
            $ aliochnevesex = False
            hide sabiaemo2 blush at left
            show sabiaemo angry1 at left
            s "That's enough, both of you!"
            show sabiaemo closed2 at left
            s "You can have this stupid argument on your own time. Alioch, I need those supplies. Now."
            "The two of them saw that she wasn't going to take any more. They remained in sullen silence, occasionally shooting sharp glances at one another, while Alioch got her the supplies she needed."
            "Neve helped her take them back, then slipped away. Sabia just felt irritated by the whole waste of time."
            return


label HGNdajrab_dialogue:
    "The sound of the bonfires had been so constant that Sabia no longer heard it, but she did hear a rush of flame that sounded far louder. For a moment she feared that the entire camp might be set ablaze and her hand flew to her sword as her eyes flickered around her."
    "To her surprise, she saw a huge plume of green fire shoot into the air. That almost confirmed her fears that the camp was ablaze, but it seemed too controlled. Another burst of green flame temporarily blinded her, but Sabia began stumbling toward it."
    "There was an emerald bonfire in the distance, near the woods. Though it burned higher than the others, it seemed to be entirely under control. Sabia realized that it was coming from Dajrab's feast."
    show dajrab normalclosed at right with dissolve
    "She got close enough to see and stopped in her tracks. Dajrab knelt before the green bonfire, apparently praying. Three enormous altars to the Horned God loomed around it, lit up a surreal green by the flames. Three priests stood in front of them, adding powder to the fire that made it flare brighter green."
    "At least the orcs seemed just as astonished as she was. Many were actively gaping, while others began to be drawn into Dajrab's feast. She hadn't paid much attention, but his was really quite impressive."
    "And it seemed that he knew it. Dajrab slowly got to his feet, expression somber, and nodded to all those who had gathered to watch."
    d "Tonight is dedicated to the Horned God. Please, enjoy yourselves and renew your strength."
    "His voice was quiet, yet it carried to everyone. His expression remained calm, though she imagined that he must be smug as hell."
    "Sabia spotted Tekrok and Rokgrid, who had come to see and were now seething. Dajrab moved closer to them and spoke in an even lower voice, forcing Sabia to rush closer to hear what he said."
    d "-not have your vision, but Dajrab not weak. Remember this."
    "The other two captains looked irritated and Tekrok started to say something, but Dajrab cut him off."
    d "Dajrab has no interest in your struggle and will not be pulled into it. But if either of you wishes to lead, you must prove to Dajrab and to every warrior that your grand vision is truly best for the tribe."
    "Realizing that their presence at Dajrab's feast was only supporting his effort, the other two Captains soon departed. Sabia found herself lingering and she raised a glass to Dajrab in respect, but he only gave her a somber gaze."
    hide dajrab normalclosed at right with dissolve
    "It seemed that Dajrab was not content to stand back and do nothing. No, he aimed to make the neutral side a real power in orc politics. And after his stunt during the feast, it looked like he'd accomplished it."
    "She was impressed. Dajrab might not lead, but if he controlled the center, anyone who wanted to lead needed to take him seriously. And given how extreme Rokgrid and Tekrok were, she had to admit that it was probably a good thing."
    "Though it seemed he had gone all out with the food and drink to keep the orcs who had wandered to see his display, Dajrab's feast didn't hold Sabia for long. She had her own business to attend to, after all."
    "She walked away, the green flames on her back slowly fading to red."
    return


label HGNbadend:
    scene bg sabiatent
    call sabiabase
    with dissolve
    if orcalliance == "sabia":
        "Sabia realized too late that she hadn't built up enough of a base of support to try to pull off something like this. She'd botched her alliances and wasted the political capital that had taken her so much effort to generate."
    else:
        "Sabia realized too late that she had burned her last bridge. She'd botched her alliances and wasted the political capital that had taken her so much effort to generate."
    "It wasn't going to be possible to recover from this blow to her reputation. She was just some human female in the middle of an orc tribe now, disavowed by her family and with no real options."
    "Sabia told herself that she would never give up. But she knew that it was over."
    show gameover with dissolve
    pause 3
    $ renpy.full_restart()
    return


label HGNaftermath:
    if Inventory.has_item(Cheapfood) > 0:
        $ Inventory.rem_item(Cheapfood)
    if Inventory.has_item(Goodfood) > 0:
        $ Inventory.rem_item(Goodfood)
    if Inventory.has_item(Expensivefood) > 0:
        $ Inventory.rem_item(Expensivefood)
    if Inventory.has_item(HGNFood) > 0:
        $ Inventory.rem_item(HGNFood)
    if Inventory.has_item(HGNBeer) > 0:
        $ Inventory.rem_item(HGNBeer)
    if Inventory.has_item(HGNMead) > 0:
        $ Inventory.rem_item(HGNMead)
    if Inventory.has_item(HGNWine) > 0:
        $ Inventory.rem_item(HGNWine)
    if Inventory.has_item(Furnishings) > 0:
        $ Inventory.rem_item(Furnishings)
    if Inventory.has_item(HGNTent) > 0:
        $ Inventory.rem_item(HGNTent)
    $ orcfestivalquest = False
    if (orcalliance == "sabia" or orcalliance == "dajrab"):
        $ rokgridblock = True
        $ tekrokblock = True
    elif (orcalliance == "rokgrid"):
        $ tekrokblock = True
    else:
        $ rokgridblock = True
    call setscreen
    scene bg sabiatent
    call sabiabase
    with dissolve
    "Sabia sat alone in her own tent, looking toward the horizon. She wasn't entirely sure why."
    "She certainly didn't believe any of the nonsense about the Horned God's Night regenerating the world's strength. That was superstition at worst, ritual at best. The important part was everything she had been seen doing."
    "And yet, she stayed awake until she saw the first sliver of the sun break over the horizon, shafts of light flooding over the camp. It hurt her eyes, yet there was something satisfying about it."
    "For better or for worse, the first part of her return was over."
    "Crawling into her tent, Sabia dropped to her bed and was instantly asleep."
    $ Sabia.rest()
    jump ylvaintroduction1



label ylvaintroduction1:
    scene bg black with dissolve
    pause 3
    scene bg sabiatent
    call sabiabase
    with dissolve
    $ Elmyshop.stock(Firemoss,3)
    $ Elmyshop.stock(Steelshrooms,2)
    $ Elmyshop.stock(Vigorreeds,1)
    $ Elmyshop.stock(Obsidianbark,1)
    $ Elmyshop.stock(Hearttreesyrup,1)
    $ ElmyshopEnslaved.stock(Firemoss,3)
    $ ElmyshopEnslaved.stock(Steelshrooms,2)
    $ ElmyshopEnslaved.stock(Vigorreeds,1)
    $ ElmyshopEnslaved.stock(Obsidianbark,1)
    $ ElmyshopEnslaved.stock(Hearttreesyrup,1)
    $ shaman_name_revealed = True
    "The next morning Sabia woke up slowly, yawning and stretching under her thin blanket. She reprimanded herself for not snapping awake like a proper soldier, especially since it sounded like there was some kind of commotion outside her tent."
    "Getting up and fully equipped, Sabia was prepared to head out and investigate. But to her surprise, an orc saw her approach and stepped inside."
    show orcbase at right
    show orcloincloth at right
    show orcaxe at right
    show orcnecklace at right
    show orcemo normal at right
    with moveinright
    orc "Will you fight in the arena?"
    show sabiaemo happy1
    s "Of course!"
    "She didn't really have a choice, not if she wanted to build on what she'd been able to accomplish during the Horned God's Night."
    orc "Okay. We start as soon as the shaman arrives."
    show sabiaemo surprised1
    s "Wait, you mean right now? Already?"
    orc "Not Ornshakar. The council is sending another shaman to assist with the rituals. The arena must be performed properly."
    show sabiaemo closed2
    "That slimy shaman was named Ornshakar? Sabia hadn't cared to learn his name, and realized that was a political mistake she couldn't afford. Her mother would mock her for such a thing, being politically clumsy even among orcs."
    "Sabia realized that she was getting wrapped up in her own thoughts. She needed to catch this orc before he moved on, get what information she could from him."
    show sabiaemo normal
    s "When exactly will the new shaman arrive?"
    orc "She must have performed the Horned God's Night with the other shamans, so she will need to travel here. Three or four days, then the fights begin."
    show sabiaemo surprised2
    s "Wait, wait, {i}she{/i}?"
    show orcemo smile3
    orc "Yes, it is strange. Apparently she has Behar Vek's favor. That is strange, but it will be good to have a female in camp again."
    "Based on what Sabia had heard about orc females, she had a hard time imagining one being a shaman. But... they couldn't all be the mindless breeders that Lundari soldiers told stories of exterminating."
    show sabiaemo normal
    s "Do we know anything else about her?"
    show orcemo normal at right
    orc "Only stories. They say she is strong and fierce, as muscular as any male. A proper orc female. She may have been sent to breed as well as to officiate."
    s "To breed?"
    orc "It is a great honor for females to bear children, especially from strong males. She may pick a winning warrior to breed with, to increase her standing among the shamans."
    s "Hmm."
    orc "We will meet her soon. Be ready for the fights so that you do not shame us."
    hide orcbase at right
    hide orcloincloth at right
    hide orcaxe at right
    hide orcnecklace at right
    hide orcemo normal at right
    with moveoutright
    show sabiaemo closed2
    "After the orc left, Sabia spent a moment contemplating the idea of the female shaman. The whole thing sounded repulsive, and if she was an ally to Ornshakar... perhaps Sabia had another enemy."
    "Also, she was coming to represent the council of shamans. That was one of the few orc organizations that meant anything to Lundar, unlike these vermin tribes. Sabia would have to meet her, just to be sure of what she was dealing with."
    show sabiaemo normal
    "But no matter what, the arena meant that she would have to fight. Sabia didn't know the rules, but she was sure that she'd need to fight on a schedule in accordance with the orc rituals. That didn't leave a lot of room for failure."
    "From now on, she'd have to be very careful with her time in order to be prepared for all her fights. As Sabia stepped out of her tent, she began thinking about everything she could do to prepare..."
    $ arenatime = 1
    jump sabiahq2
    return







label ylvaintroduction2:
    $ RGAylvapresent = True
    $ a_list.append("Ylva")
    "That day Sabia woke early in order to keep preparing, but discovered that the few others already awake seemed distracted. Investigating the matter, Sabia heard rumors that the female shaman had been spotted outside camp."
    show backdrop
    scene bg countryside
    with dissolve
    "Heading to the outskirts, Sabia discovered that she could just see a figure approaching the camp. The shaman seemed to be walking alone at a good speed - had she really walked all the way here? She had arrived earlier than the orcs had told her."
    "Wanting a chance to scout the shaman before encountering her, Sabia slipped further back into a cluster of trees near the wall. It seemed the early arrival was unexpected, so their greeting party was unorganized. Sabia didn't see the local shaman anywhere yet."
    "Finally the female orc came close enough for Sabia to get a good look at her. She... wasn't what Sabia expected."
    show ylva normal at center
    show ylva2 arm2 at center
    with dissolve
    "She had well-defined muscles like a male orc, but Sabia was surprised how feminine she looked. And as she met the welcome party, Sabia was struck by how her intense purple eyes flickered over everyone. This one could be dangerous."
    if slavery >= freedom:
        if dom >= sub:
            $ A_ylva += 0
            "Sabia narrowed her eyes and evaluated the new threat. At best, this female orc might be a useful tool. At worst, she would be an enemy that Sabia needed to break."
        else:
            $ A_ylva += 1
            "Sabia found her gaze lingering over the orc, wondering if her mind was any different than the male brutes in camp. Perhaps she could offer something new."
    else:
        if dom >= sub:
            $ A_ylva += 1
            "Sabia watched carefully, wondering at the potential. Though she might prove as difficult as the local shaman, this female orc could also be a valuable ally if Sabia could turn her."
        else:
            $ A_ylva += 0
            "Sabia wondered just what this female orc represented. Was she bound by her people's laws, or trying to do something different? There was no way to come to any conclusion."
    "Setting aside her thoughts, Sabia drew closer while trying to stay in the shadows. Right now she was too far away to hear what they were saying, but as she crept closer she began to hear."
    orc "When can we begin the combat, Ylva?"
    "So her name was Ylva? Sabia wasn't sure what it meant, but it was less guttural than she'd expected. In any case, the female orc responded in a voice that was slightly husky but feminine."
    ylva "Ylva will need to speak with Shaman Ornshakar, but most likely the rituals will not take long."
    orc "Not too fast. Some are still recovering from the Horned God's Night."
    show ylva happy1 at center
    ylva "Me understand. Have no fear, we will not force the fights too quickly."
    show ylva normal at center
    "It seemed that they didn't have a lot of business aside from greeting her. Sabia had hoped to get more information about the council of shamans and if there was any deeper meaning to her arrival, but it didn't seem likely that she'd overhear anything like that."
    "As the female shaman broke from the group to enter camp, Sabia realized that she had a limited window of opportunity to speak to her now, before anything else got involved. However things went, she needed to take advantage of it, so Sabia headed out to intercept her."
    call sabiabase
    with moveinleft
    s "Hello there!"
    show ylva normal at right
    show ylva2 arm2 at right
    with moveinright
    "The female orc shifted back slightly, surprised by her presence. But her expression was neutral, not angry or shocked. After a moment, she smiled."
    show ylva happy1 at right
    ylva "Greetings. They told me about you."
    s "Oh, really?"
    if L_orcs >= 15:
        $ A_ylva += 2
        show ylva happy1 at right
        ylva "I was surprised to hear there was a human who somehow acquired such a fantastic reputation in camp. That's unusual."
        show sabiaemo happy3 at left
        s "Oh, I hope they didn't say anything embarrassing."
    elif L_orcs >= 10:
        $ A_ylva += 1
        show ylva happy1 at right
        ylva "I was surprised to hear there was a human who somehow acquired a good reputation in camp. That's unusual."
        show sabiaemo happy3 at left
        s "Oh, I hope they didn't say anything embarrassing."
    elif L_orcs >= 5:
        $ A_ylva += 0
        show ylva normal at right
        ylva "Yes, I heard you completed the membership rituals, and you've acquired a reputation for yourself since then."
        s "Yes, I've taken a strange path."
    elif L_orcs >= 0:
        $ A_ylva += 0
        show ylva normal at right
        ylva "Yes, I heard you completed the membership rituals. Surprising for a human."
        s "Yes, I've taken a strange path."
    else:
        $ A_ylva -= 1
        show ylva angry1 at right
        ylva "Yes, I heard you forced your way into the tribe and have been rampaging about with no respect for our traditions."
        show sabiaemo closed2 at left
        s "Hmph."
    show ylva normal at right
    show sabiaemo normal at left
    ylva "So, why did you come greet me?"
    show sabiaemo surprised1 at left
    s "Uh..."
    "She hadn't anticipated needing a reason, assuming that she did. Or maybe Ylva had intentionally asked the question to test her. She needed an answer fast..."
    show sabiaemo normal at left
    menu:
        "Domination: Do I need a reason?" if dom >= 3:
            $ A_ylva -= 1
            show ylva closednormal at right
            ylva "No, I suppose not."
        "Just wanted to help welcome you":
            $ A_ylva += 1
            show ylva happy1 at right
            ylva "The greeting is supposed to be a more formal occasion, but thank you for the thought."
        "I've never met a female orc before":
            show ylva sad at right
            ylva "Oh? Haven't you heard enough about us already?"
            menu:
                "You're not as hideous as I expected.":
                    $ A_ylva -= 1
                    show ylva closedangry at right
                    ylva "So glad to hear."
                "I wanted to see if the rumors were true":
                    $ A_ylva += 0
                    show ylva normal at right
                    ylva "I see."
                "Orcs: Yes, but many of the things I was taught were false" if L_orcs >= 10:
                    $ A_ylva += 1
                    show ylva happy1 at right
                    ylva "Ah, it's nice to hear of a human being so open-minded."
                "Domination: I'm not stupid enough to believe our own propaganda" if dom >= 10:
                    $ A_ylva += 2
                    show ylva happy2 at right
                    ylva "Well, well. I guess I shouldn't be surprised, given that you've joined this camp."
        "I wanted information about the arena fights":
            $ A_ylva += 0
            ylva "I'm afraid I can't say anything about those because they haven't been fully planned."
        "I just happened to be training outside":
            $ A_ylva += 0
            ylva "Well then, thank you for the greeting."
    show ylva normal at right
    ylva "It's interesting that you should come. I was actually sent t-"
    show orcshaman angry1 at center with moveinright
    "At that moment, Ornshakar stormed up between them, casting a vicious glare at Sabia. A moment later he turned to Ylva and changed his expression entirely."
    show orcshaman happy3 at center
    ornshakar "Shaman Ylva. Welcome to Warchief Groknak's camp."
    ylva "Ylva is grateful for your reception. Me has heard much of your work here."
    ornshakar "Come this way, we have much to discuss for the arena."
    "Though it seemed that Ylva was going to object, the shaman drew closer and said something too low for Sabia to hear. Ylva's expression became neutral, then she nodded politely to Sabia and moved with the shaman toward the camp."
    scene bg countryside with dissolve
    "Abruptly Sabia was alone again, wondering how she should take that. She hadn't had enough time to form a solid opinion of Ylva, so it was hard to judge this change. Still, given that Ornshakar was involved, it couldn't be a good thing."
    "The question was exactly what she should - or could - do about it. Maybe it was useless to even try and the shamans would always work together."
    "Trailing them from a distance, Sabia saw the two shamans briefly tour the camp. They seemed to be speaking of more than just the buildings, though. Perhaps just their rituals... but perhaps something more sinister."
    show ylva sad at right
    show ylva2 arm1 at right
    with dissolve
    "It was a whirlwind tour, but at the end of it, the shaman left to speak with Warchief Groknak. That left Ylva alone - she set her staff down respectfully and leaned back against the side of the building, taking a deep breath."
    "Her back was straight, but her shoulders slumped just slightly. It was a familiar stance to Sabia, and it looked so human that she decided not to write Ylva off. Smiling, Sabia approached."
    call sabiabase
    show sabiaemo happy1 at left
    with moveinleft
    s "Hello, Ylva! Hectic introduction, isn't it?"
    show ylva normal at right
    ylva "Hello again."
    show sabiaemo normal at left
    if A_ylva >= 1:
        "Much of the warmth had drained from her expression and voice, giving Sabia pause. She and Ylva had been speaking in a fairly friendly way before, what had changed?"
    else:
        "Much of the warmth had drained from her expression and voice, giving Sabia pause. Though she hadn't been friends with Ylva, there hadn't been much hostility. What had changed?"
    "Of course, she knew the answer as soon as she thought the question: the shaman had done this. But before Sabia could try to act on that, Ylva was speaking again."
    ylva "Shaman Ornshakar tells me that you were forced to come here by circumstance. You did not choose to join us, but joined the tribe as... a convenience."
    show sabiaemo eyebrow1 at left
    s "You think I'd voluntarily come out here to live in a fucking tent?"
    show sabiaemo sad2 at left
    show ylva closedangry at right
    "As soon as she said it, Sabia realized her mistake. She had expected Ornshakar to tell ridiculous lies about her, not... basically the truth. But not a convenient truth for her goals."
    ylva "I see."
    show sabiaemo sad1 at left
    s "I didn't mean it that way... look, surely you'd acknowledge that the standard of living is better in Lundar. This is rough for me, but that doesn't me-"
    show ylva angry1 at right
    ylva "Yes, because it's fair to compare an empire to the refugees of the people it has looted."
    show sabiaemo angry1 at left
    s "Hey! Don't pretend that Lundar hasn't earned most of what it has! You're the ones razing our villages!"
    show ylva angry2 at right
    ylva "Innocent defense, is it? That's why you tried to exterminate everyone like me?"
    show sabiaemo sad1 at left
    s "..."
    show ylva angry1 at right
    ylva "..."
    show sabiaemo closed2 at left
    s "(Well, that wasn't ideal. Not sure if I should just consider this a lost cause, or...)"
    s "Look... Ornshakar obviously told you a lot of things about me. But he just hates me because he tried to cheat during the membership ritual and he still failed."
    show ylva normal at right
    ylva "I have no doubt that he's biased. But it seems to me that he told the truth."
    show sabiaemo normal at left
    s "Truth isn't that simple. Don't just take his word for things, ask everyone else in camp."
    ylva "..."
    "That seemed to mollify her a little, but Sabia wasn't sure if she should keep pressing."
    menu:
        "Just ask about the arena and go":
            $ A_ylva -= 1
        "Change the subject":
            $ A_ylva += 0
            s "I hope you didn't have any trouble coming here. The roads have had real trouble with bandits in this region."
            ylva "So I observed, but I was able to avoid them."
        "Show great respect for orc culture":
            $ A_ylva -= 1
            show sabiaemo happy1 at left
            s "Actually, I have great respect for your people! So strong an-"
            show ylva angry1 at right
            ylva "Don't try."
        "Ask about her position":
            $ A_ylva += 0
            s "So, how were you chosen to come here? Is it an honor, a duty, something else?"
            ylva "An honor and a trial, but I would rather not speak of it now."
        "Mention the feast" if orcalliance == "sabia":
            $ A_ylva += 1
            s "If you really think I'm disrespecting the tribe, ask about the feast I hosted for the Horned God's Night."
            ylva "You... hosted a feast?"
            s "I can't claim it was perfect, but I did my best and the warriors seemed to enjoy it!"
            show ylva happy1 at right
            ylva "That surprises me, but not in a bad way."
        "Submission: Apologize" if sub >= 1:
            $ A_ylva += 2
            $ sub += 1
            show sabiaemo sad1 at left
            s "I... I'm sorry. I won't pretend that I'm not an arrogant bitch sometimes."
            show ylva normalnarrow at right
            ylva "..."
            s "And it's true that I've looked down on orcs in the past. I won't pretend everything's simple and friendly. But... I'm not here to fight with you."
            ylva "..."
            show ylva closedhappy at right
            ylva "Apology accepted, Sabia."
            show ylva happy1 at right
            ylva "I won't pretend I've forgotten everything you've said, but I understand you're in a difficult position. We need not be enemies."
    show sabiaemo normal at left
    s "So... I won't take up any more of your time, but I wanted to ask about the arena. Do you know when things will begin?"
    show ylva normal at right
    ylva "Though much remains to be decided, the basic form is always the same."
    show ylva closednormal at right
    ylva "Shaman Ornshakar and I will bless the arena and perform all the necessary rituals. That will take all day tomorrow, and the day after that, the Red God's Arena will begin."
    show ylva normal at right
    ylva "Everyone fights on the first day in order to qualify - I suggest you be fully prepared. If you make it through that match, then you will likely be able to choose how frequently you participate after that."
    s "Oh? I won't have to fight every day?"
    ylva "The goal is shows of strength before the Red God, not a simple tournament. There will be duels, trials, contests against beasts, and much more."
    s "I see. I'll do my best to participate honorably."
    ylva "Perhaps you will."
    scene bg countryside
    call sabiabase
    with dissolve
    "With that, Ylva took her staff and left. Sabia remained for a while longer, pondering what had been said."
    "She had two days until her first match. After that, she would just need to play things by ear and see how well she could do."
    return


label ylva1neve:
    $ ylva1nevetalk = True
    show backdrop
    show bg countryside
    show ylva happy1 at left
    show ylva2 arm1 at left
    show neve1 at right
    show neveemo normal at right
    with dissolve
    ylva "Hello! I've been meaning to speak with you."
    show neveemo happy2 at right
    n "Welcome to camp! Or am I not allowed to do the greeting?"
    ylva "You seem to have more ties here than I do, so why not? But I wanted to ask... do those faces represent Seros?"
    show neveemo normal at right
    n "..."
    show ylva normal at left
    ylva "Is it... improper to ask? I assure you, I am motivated only by curiosity. In my journey into elven lands, I got to see so little of your history."
    show neveemo happy1 at right
    n "I don't take offense, but there are some questions I'd rather not answer."
    show ylva closedsad at left
    ylva "Very well, I will restrain my curiosity."
    show ylva sad at left
    ylva "At the risk of offending you again... you seem very open with most orcs, but surprisingly hostile to that question."
    show neveemo normal at right
    n "The warriors here are alright. I can't say the same for authorities."
    ylva "Is there so little trust in the council of shamans? They may be self-serving, but no more than most politicians."
    show neveemo smirk1 at right
    n "Are you suggesting I should trust politicians?"
    show ylva happy2 at left
    ylva "Fair enough."
    show ylva happy1 at left
    ylva "I promise I won't pry, then, but let me ask a more neutral question. What do you think of the human warrior in camp?"
    if A_neve >= 5:
        $ A_ylva += 1
        show neveemo happy2 at right
        n "Ah, Sabia. She has her rough edges, but she's an interesting one..."
    else:
        $ A_ylva += 0
        show neveemo normal at right
        n "Yes, Sabia. I suppose I can tell you a few things..."
    scene bg black with dissolve
    pause 1
    return


label ylva1lutvrog:
    $ ylva1lutvrogtalk = True
    show bg traininggrounds
    show ylva normal at left
    show ylva2 arm1 at left
    with dissolve
    ylva "..."
    show lutvrogbase at right
    show lutvrogaxe at right
    show lutvrogwraps at right
    show lutvrogwrists at right
    show lutvrogemo normal at right
    with moveinright
    lut "Do you need something?"
    show ylva happy1 at left
    ylva "Ylva is just observing the warriors. Your tribe is strong."
    lut "Not as strong as it could be. Lutvrog works to improve himself and others."
    ylva "Lutvrog... ah, Warchief Groknak mentioned you! You're one of the tribe's only Kentarks, right?"
    lut "That is not a title we use often. With limited resources and the threat of Lundar, there is no need for anyone to lead expeditions."
    show ylva closednormal at left
    ylva "Believe me, Ylva knows. Ylva is actually a Kentark herself, but has led warriors only once."
    show lutvrogemo happy at right
    lut "Oh? You are a warrior, then?"
    show ylva closedhappy at left
    ylva "Ah... Ylva is not a warrior to meet your standards, Kentark Lutvrog."
    show lutvrogemo normal at right
    show ylva normal at left
    ylva "The path to becoming a shaman is unclear for a female. But the path to becoming a Kentark was my right, so Ylva used it to make shamanhood more acceptable."
    lut "Lutvrog understands. There is honor in this too... well met, Kentark Ylva."
    show ylva happy1 at left
    ylva "Ylva looks forward to seeing you fight in the arena!"
    show lutvrogemo happy at right
    lut "Lutvrog looks forward to it as well."
    ylva "But Ylva wishes to set up honorable matches... can she ask your opinion of the many warriors?"
    show lutvrogemo normal at right
    lut "Of course."
    scene bg black with dissolve
    if A_lutvrog >= 5:
        $ A_ylva += 1
    else:
        $ A_ylva += 0
    pause 1
    return


label ylva1jadk:
    $ ylva1jadktalk = True
    show bg silvertusk
    call sabiabase
    show jadkbase at right
    show jadkemo normal at right
    with dissolve
    s "Hello, Jadk. Has Ylva been through here?"
    jadk "I do not think we'll see her here."
    s "Why not?"
    show jadkemo happy2 at right
    jadk "Gwahaha, have you ever seen our shaman come in here?"
    s "Huh, I guess not. Is that a religious thing?"
    jadk "Shamans must always be prepared to commune with spirits. Alcohol only helps you commune with the floor, gwahaha!"
    s "Heh, noted."
    return


label ylva1maply:
    $ ylva1maplytalk = True
    show backdrop
    show bg countryside
    show ylva normal at left
    show ylva2 arm1 at left
    with dissolve
    ylva "..."
    show ylva normalnarrow at left
    ylva "You can come out now."
    show maply 1 at right
    show maplyemo happy at right
    with moveinright
    maply "Wow, how did you know I was watching you?"
    show ylva normal at left
    ylva "I studied your hunting techniques when I was with one of your tribes. I only learned a little, but I can spot you... especially when you're looking so intently."
    show maplyemo normal at right
    maply "Sorry, I was just really curious! I've never seen a female orc before!"
    ylva "Really?"
    maply "Yeah, all of the tribes in this area are the ones that sent their females away."
    show ylva closednormal at left
    ylva "I didn't realize it was so many... but in any case, perhaps you'd like to introduce yourself?"
    show maplyemo happy at right
    maply "Oh, hehe, I forgot. Hi, I'm Maply!"
    show ylva happy1 at left
    ylva "Pleased to meet you, Maply... or should I call you Maple?"
    maply "Maply is good!"
    show maplyemo normalopen at right
    maply "So you really do know a lot of things about catgirls! What were you doing with a tribe, anyway?"
    show ylva normal at left
    ylva "Part of my training is to gain a deeper understanding of all the races that live in this land."
    show maplyemo happy at right
    maply "Wow! So you know a lot about everybody?"
    ylva "Not yet. I've studied with elves and catgirls so far. Behar Vek sent me here to grow used to our own people in human lands, and to learn more of humans. I hope one day to journey west and learn of minotaurs as well."
    show maplyemo normal at right
    maply "That sounds neat! I've mostly traveled around this area, raiding the local orcs and humans..."
    if catgirlstatus == "enslaved":
        $ A_ylva -= 2
        show maplyemo angry1 at right
        maply "But not anymore. That awful human..."
        show ylva normalnarrow at left
        ylva "Sabia?"
        maply "Yes! She's awful, just awful..."
        ylva "Tell me what you know..."
        scene bg black with dissolve
        pause 1
    elif catgirlstatus == "free":
        $ A_ylva += 2
        show maplyemo happy at right
        maply "Well, until we got caught. Saby is too smart for us, heehee..."
        ylva "What's this? I heard there was an encounter, but I was surprised to see so many of you here."
        maply "Saby could have done something awful to us, but instead she set us free! Our caravan is kind of messed up, though, so we're sticking around here."
        ylva "Hmm. I will have to ask more of this, but not now."
        show ylva happy1 at left
        ylva "I'm afraid I'm very busy with the Red God's Arena, but I'm glad to meet you, Maply. Perhaps we can speak again later?"
        show maplyemo happy at right
        maply "Sure!"
    elif catgirlstatus == "recruited":
        $ A_ylva += 1
        show maplyemo eyebrows at right
        maply "Now, uh... now we've teamed up with the tribe, or something like that. It's weird."
        ylva "Yes, I heard of this. Strange, but there is a precedent for it."
        show maplyemo sad1 at right
        maply "I hope it's not like a war or anything."
        ylva "All of us hope not."
        show ylva happy1 at left
        ylva "I'm afraid I'm very busy with the Red God's Arena, but I'm glad to meet you, Maply. Perhaps we can speak again later?"
        show maplyemo happy at right
        maply "Sure!"
    else:
        $ A_ylva += 0
        show maplyemo eyebrows at right
        maply "We thought the orcs were going to kill us, but instead they, uh... just made us work off the debt. It's weird."
        ylva "Do you think that it's because of the human's influence?"
        maply "Sabia? I don't know..."
        ylva "Hmm."
        show ylva happy1 at left
        ylva "I'm afraid I'm very busy with the Red God's Arena, but I'm glad to meet you, Maply. Perhaps we can speak again later?"
        show maplyemo happy at right
        maply "Sure!"
    return


label ylvaconvo1:
    call sabiabase
    show ylva normal at right
    show ylva2 arm2 at right
    with dissolve
    if kiaprogression >= 9 and SUlakequest < 1:
        call SUylvalake1
    if ylvatalkintro == False:
        $ ylvatalkintro = True
        "Sabia approached cautiously, wondering if Ylva would turn her away. The orc woman watched her with a careful gaze, but after a moment gave a polite nod."
        ylva "Do you need something?"
        s "I just wanted to talk. Is that okay?"
        ylva "Yes, it's always fine to talk."
        if A_groknak >= 3:
            $ A_ylva += 1
            show ylva happy1 at right
            ylva "Warchief Groknak asked me to deal with you, actually. But I think he meant it in a positive way - he's not the friendliest sort, but I think he approves of you, to the degree he can approve of a human."
            s "Huh, wouldn't have expected that."
        elif A_groknak >= 0:
            $ A_ylva += 0
            ylva "When I asked Warchief Groknak about you, he didn't have anything insulting to say. Given his feelings about humans, that's not bad."
        else:
            $ A_ylva -= 1
            ylva "Warchief Groknak doesn't think much of you, but he did say that I should address you as a member of the tribe."
        show ylva normal at right
        ylva "Don't take this as an insult, but I've heard from around camp that you're very fond of questions. Some are suspicious that you want to use it for some malicious purpose."
        s "I'm not trying to do anything like that, but I do hope we can exchange information."
        ylva "Then let's make it an actual exchange. Every question you ask of me, I get to ask one about you."
        s "..."
        show sabiaemo happy1 at left
        s "Deal!"
    menu:
        "Can you offer any help for my troops?" if recruitmentopened == True and ylvaenchantmenthelp == False:
            $ ylvaenchantmenthelp = True
            if A_ylva < 5:
                if A_ylva < 3:
                    ylva "After everything, you dare to come and ask for my help? No. Not a chance."
                else:
                    ylva "I apologize, but I must stay neutral in such matters."
            else:
                $ Sabiasquad.magic += 1
                ylva "Yes, I'd heard that you began raiding. But what help do you think I can offer?"
                s "Shamans specialize in enchantment, right? I know you can't go with me, but can you do anything to give my troops a boost?"
                ylva "Hmm... while I cannot be seen to take a side in political conflicts, technically shamans do have the role of offering blessings of the spirits."
                ylva "Given the tribe's current shaman, this practice has mostly lapsed."
                ylva "While I don't want to spend all my time with this... if your orcs come to me for a blessing, it would be part of my duty to assist them."
                s "Great! Thanks, Ylva!"
                if A_ylva >= 10:
                    if kulganalive == True:
                        $ Kulganorcs.magic += 1
                        ylva "In addition, I heard you honorably assisted a warrior named Kulgan. Since his band is working for you, I can extend the blessing of the spirits to them as well."
                        s "Then thank you on two accounts!"
                        ylva "Please just use this power well."
                    else:
                        ylva "Please just use this power well."
                else:
                    ylva "Please just use this power well."
        "Can you help me with Kentark training?" if kentarktraining > 1 and kentarkylva == False:
            if A_ylva >= 10:
                ylva "I don't know if it would be proper for you to do the training, but I can help you with the preparations..."
                if A_ylva >= 25:
                    $ kentarktraining += 20
                    $ kentarkylva = True
                    "Having Ylva's assistance was immensely helpful, since she understood how humans thought and could explain things thoroughly to Sabia. Ylva was remarkably open with her knowledge and by the end Sabia felt much closer to prepared."
                else:
                    $ kentarktraining += 10
                    $ kentarkylva = True
                    "Having Ylva's assistance was immensely helpful, since she understood how humans thought and could explain things thoroughly to Sabia. Though Sabia thought she held back a little, by the end Ylva had taught her a great deal."
            else:
                ylva "I know much, but those are secrets that should not be revealed to outsiders."
        "What's next for the Red God's Arena?" if (arenatime < 20 and recruitmentopened == False):
            if arenatime == 3:
                ylva "We need to sanctify it with the formal ritual. It will need to start at dawn."
            elif arenatime == 4:
                ylva "It will take some time to finish the ritual today. Then tomorrow, all warriors will fight in the qualifying matches."
                if A_ylva >= 5:
                    ylva "You'll probably need to fight several battles in a row, so be prepared or bring something to heal."
            elif arenatime == 5:
                if A_ylva >= 5:
                    ylva "Congratulations on finishing the qualifying match! Tomorrow should be entirely matches of other warriors, so take the time to relax and prepare."
                else:
                    ylva "You finished the qualifying match, so you won't have to fight tomorrow."
            elif arenatime == 6:
                ylva "There will be a melee event tomorrow that's advised but not required."
                if A_ylva >= 5:
                    ylva "I suggest you go into it well-rested, they can be exhausting events."
            elif arenatime == 7:
                ylva "With the melee over, the next events will be fights to the death. You'd better be prepared for one tomorrow."
            elif arenatime == 8:
                ylva "Since you've finished your solo fight, you have a while to recover. But they're going to introduce the next major event tomorrow..."
            elif arenatime == 9:
                ylva "So you saw the hellhounds? We have a long tradition of working with them, but I have not been able to study them because so many are dead or wild."
            elif arenatime == 10:
                ylva "I'm impressed you managed to win your match against the hellhound! Your next fight will be to the death, but not for a few days."
            elif arenatime == 11:
                ylva "Don't forget you have a duel tomorrow. I hear your opponent is fond of lethal combination attacks, so best to find a way to interrupt him."
            elif arenatime == 12:
                ylva "Now that you've finished your duel, you won't have to fight individually again before the final event. But there's another melee tomorrow, be prepared if you plan to participate."
            elif arenatime == 13:
                ylva "We're getting something truly special tomorrow! I can't say anything, but be ready!"
            elif arenatime == 14:
                ylva "...I don't want to talk right now."
            elif arenatime == 15:
                ylva "The Makhor... no, it's nothing. Tomorrow will be a number of religious fights. You can't participate, but it would be good to attend."
            elif arenatime == 16:
                if ylvatalkcheating == True:
                    ylva "I'm troubled by Shaman Ornshakar's behavior, but I will have to contemplate it after all my duties for the Red God's Arena are complete."
                else:
                    ylva "Something was amiss about the ceremonial match, but I can't put my finger on what..."
                ylva "Anyway, tomorrow will be the final combat! Participation is optional, but you had best be as well prepared as possible."
            elif arenatime == 17:
                ylva "Your part in the Arena is over. We will formally close the Arena tomorrow, and after that..."
        "What do you think of the Captains?":
            ylva "Not only am I supposed to remain neutral on matters of war, I haven't had time to truly know them yet."
        "Why didn't you need to come for the Horned God's Night?" if ylvatalkHGN == False:
            $ ylvatalkHGN = True
            show ylva closedangry at right
            ylva "That is... more of a sore point than you could have known."
            s "Oh? What do you mean?"
            show ylva angry3 at right
            ylva "Let me guess: the warriors explained the basics to you, but it was basically just a night of eating and drinking?"
            show sabiaemo closed1 at left
            s "That's... accurate."
            show ylva angry1 at right
            ylva "Most mean well, but this was {i}not{/i} the true form of the ritual. In addition to not taking it very seriously, they miss the spirit of the event so many times..."
            show ylva closedangry at right
            ylva "For example, most tribes go around killing white hinds left and right. It's not just a hunt, it's supposed to be a single ritual sacrifice renewing the Horned God and bringing in the new year."
            show sabiaemo surprised1 at left
            s "Uh..."
            ylva "And while politics gets into everything, the war tribes make it especially bad. It should be a single feast of unity, not a scattered contest of gluttony."
            show sabiaemo closed2 at left
            s "Geez... maybe I should be glad you weren't here to see me take part..."
            show ylva sad at right
            ylva "Oh, I wasn't putting any blame on you. You couldn't have known any better."
            if orcalliance == "sabia":
                $ A_ylva += 1
                show ylva happy1 at right
                ylva "Actually, I heard you went to a lot of trouble to create your own feast. That's more than I would have expected a human to do."
                if antlers >= 4:
                    show ylva happy1 at right
                    $ A_ylva += 1
                    ylva "And from what I've heard, you put real effort into the Horned God's altar. I'm glad you showed respect, even if you didn't fully mean or understand it."
            elif orcalliance == "tekrok":
                $ A_ylva += 1
                show ylva normal at right
                ylva "Actually, the fact that you would participate in the Horned God's Night speaks well of you."
                show ylva happy1 at right
                ylva "And I heard you even acted as the the avatar of the Horned God in the ritual! That's impressive!"
                show sabiaemo normal at left
                s "So that's a real ritual? I was kind of worried they just made it up, to, uh..."
                ylva "No, not at all. Back in the day, it was a position of honor."
            elif orcalliance == "dajrab":
                show ylva normal at right
                ylva "Actually, the fact that you would participate in the Horned God's Night speaks well of you."
                if HGNdajrabagree == True:
                    $ A_ylva += 1
                    show ylva happy1 at right
                    ylva "And I heard you even acted as the the avatar of the Horned God in the ritual! That's impressive!"
                    show sabiaemo normal at left
                    s "So that's a real ritual? I was kind of worried they just made it up, to, uh..."
                    ylva "No, not at all. Back in the day, it was a position of honor."
            else:
                show ylva normal at right
                ylva "Actually, the fact that you would participate in the Horned God's Night speaks well of you."
            if orcfestivalscore >= 30:
                $ A_ylva += 1
                show ylva happy1 at right
                ylva "Everyone I spoke to said that you really put your heart into it. I had never imagined a human would even try, so it speaks well of you."
            show ylva happy2 at right
            ylva "Of course, I know you were just doing it to gain standing."
            show sabiaemo happy1 at left
            s "Not even going to deny it."
            show ylva happy1 at right
            ylva "That's fine. You respected the forms and honored the spirits - that's more than could be expected from many warriors."
            show sabiaemo happy1 at left
            s "Do I need to be concerned there are just as many pitfalls with the Red God's Arena?"
            show ylva normal at right
            ylva "In ancient times, the Arena was actually a ritualized demonstration of combat. But the war tribes have made it into the grandiose event that it is today."
            show ylva closednormal at right
            ylva "The council of shamans has... accepted this. The warriors want such challenges, and at least they are giving honor to the Red God, even if for themselves."
            show ylva normal at right
            ylva "For years they have been smaller events held locally. This is the first time in many years that we're using a proper arena, which is part of why I'm here. Hopefully it will go smoothly."
        "Tell me more about orc religion" if (ylvatalkHGN == True and A_ylva >= 10 and ylvatalkreligion == False):
            $ ylvatalkreligion = True
            $ A_ylva += 2
            show ylva happy1 at right
            ylva "Oh? Do you actually want to learn more?"
            s "I feel like I should, if I'm going to be here for a while."
            show ylva closednormal at right
            ylva "It's a more complex subject than humans give us credit for. But I can explain at least the basics."
            show ylva normal at right
            ylva "At the heart of life is the fact that all things have spirits within them. It would take too long to explain them all, but two spirits reign supreme: the sun and the moon."
            ylva "You actually know the spirit of the sun by another name: the Horned God. It manifests itself in many forms, including a stag."
            show sabiaemo eyebrow1 at left
            s "Just how many names and forms does this god have?"
            show ylva closedangry at right
            ylva "Great spirits are not simply people with some extra power. They are grand beings that encompass far more than our minds can understand."
            show ylva normal at right
            ylva "For example, the Horned God has many forms that are but its true nature seen from one angle. The sun in the sky, the warmth we can feel, the white hind, a horned figure in the forest, a female satyr embodying fertility... the list goes on and on."
            show sabiaemo normal at left
            s "Okay, fair enough. I probably can't learn all of those quickly. But one question: if the Horned God becomes the white hind, why do you kill and eat it?"
            ylva "A common question - even some warriors ask it. But the white hind is only a physical manifestation of the Horned God. When we sacrifice it, we help the sun to be born anew with renewed strength."
            s "Huh. You said there were two supreme spirits?"
            ylva "Yes. The second is the moon, the Toothed God, the eternal wolf, the cold wind. It does eternal battle with the Horned God."
            show sabiaemo happy1 at left
            s "Ah, so the rituals are about giving strength to the Horned God to help it beat the Toothed God?"
            show ylva sad at right
            ylva "No, not at all... if the battle were to end, that would be a terrible thing for the entire world."
            show sabiaemo closed2 at left
            s "Then I don't get it."
            show ylva normal at right
            ylva "The wolf chases the stag and helps it to grow strong. If the Toothed God were dead, the Horned God would grow weak, the sun would grow dim, and the world would grow as cold and barren as if the Toothed God slew the sun."
            show sabiaemo normal at left
            s "Huh."
            "It all sounded like ridiculous superstitious nonsense, but Sabia had the sense not to say that. There was at least a little internal logic to it."
            ylva "There are other spirits, of course - innumerable ones. For example, the Red God is normally a lesser god of violence, but it is popular among warriors in this age of war."
            s "That makes sense to me."
            show ylva happy1 at right
            ylva "Now... what can you tell me of the Order of Relona? I have been quite curious..."
            show sabiaemo closed2 at left
            s "I'm the wrong person to ask. The Order teaches that everyone has a different role in the world - I am a warrior, so I worship Relona through battle. And I do take it seriously, but I have never been too interested in all the details."
            show sabiaemo normal at left
            s "If you want theology, you need to ask a priest or priestess. Though they probably couldn't give you a straight answer, since everyone has their own opinion. There are a lot of factions in the Order."
            show ylva sad at right
            ylva "I see. A pity, but I suppose you have told me what you know."
        "What exactly does the symbol on your staff mean?" if ylvatalksymbol == False:
            $ ylvatalksymbol = True
            $ A_ylva += 1
            ylva "That's actually fairly esoteric, though it's not really a secret. It's a merger of several different symbols."
            s "I noticed that the warchief and the local shaman also have them, but theirs look a little different."
            ylva "Yes, that's related to the meaning."
            show ylva closednormal at right
            ylva "The circle represents both the sun, and the expanding of our people. It has been passed down from an age when we were expanding instead of contracting."
            show ylva normal at right
            ylva "I and most other shamans carry this form of it. But as our society fractured and warchiefs became more prominent, many took the same symbol - they added the axes to represent their military authority in contrast to the council of shamans."
            s "And Ornshakar gets axes because he's the main shaman for this warband?"
            ylva "That's right. Then you've probably already guessed that Warchief Groknak has gold because he is a leader."
            s "Do any top shamans get a gold symbol?"
            ylva "No, we don't have central leaders the way the warbands do. The council is a more robust system, but slower to act... hence the need for warchiefs."
            show ylva normal at right
            ylva "Now, I've been wanting to ask: what's the meaning behind the tattoo on your arm?"
            show sabiaemo happy1 at left
            s "You know you're the first person to ask me that here? I'm surprised how incurious everyone seems."
            show ylva happy2 at right
            ylva "Some orc women get tattoos for the purposes of beauty. I'm guessing human women aren't fond of skulls, though."
            show ylva normal at right
            s "Haha, no. This is the symbol of the squad I commanded on the minotaur front."
            show sabiaemo closed3 at left
            s "They were a great team of soldiers. Honestly, with the experience I've gained now, I can tell I wasn't anywhere near as strong as they were. But they didn't gain anything by letting me get their tattoo, so I'm honored they felt I was a good enough commander."
            show sabiaemo normal at left
            s "Sadly, all those soldiers were assigned to the Obsidian Ridge. It's good they're keeping an eye on the minotaurs, but I lost a base of support."
            ylva "So you fought on the minotaur front? That's a region I have yet to study, I'd like to know more... but I suppose that's beyond the bounds of my question."
        "What does it take to become a shaman?" if ylvatalkequipment == False:
            $ ylvatalkequipment = True
            $ A_ylva += 1
            ylva "There's no simple answer to that question. It's fundamentally a religious role, so the decision is in the hands of the spirits... and the orcs interpreting them, of course."
            show sabiaemo eyebrow1 at left
            s "So in the hands of orcs, then."
            show ylva closedangry at right
            ylva "Do you apply the same standards of skepticism to Relona?"
            show sabiaemo normal at left
            s "That's different... but I wouldn't deny that there's plenty of human influence in the Order of Relona. They're one of the main political forces in Lundar."
            show ylva normal at right
            ylva "It's the same for orcs. The decision is supposed to be spiritual, but of course it's a decision based on cultural values and political issues."
            show ylva happy1 at right
            ylva "Having said all that, there are certain standards. You need to have an honorable standing and the recommendation of a shaman. After that, you need to go through a training period to prove yourself. That's where I obtained my staff."
            show sabiaemo irritated2 at left
            s "Why doesn't Ornshakar have a staff?"
            show ylva closedangry at right
            ylva "Because it wasn't as difficult for him to become a shaman."
            show ylva normal at right
            ylva "No, I needed to go above and beyond. I carved my staff from stonewood while I was in elven lands."
            show sabiaemo surprised1 at left
            s "Stonewood? There's not a lot of that left anymore."
            ylva "It wasn't easy to find. Being able to locate it helped show I had the favor of the forest spirits."
            show ylva normal at right
            ylva "And before you criticize, of course I also spent a lot of time studying forest lore to track it down. That doesn't mean they didn't favor me."
            show sabiaemo happy1 at left
            s "Heck, I think it's impressive either way!"
            ylva "My furs were taken from a northern wolf I killed. Though I didn't spend as long in the north, combat with wolves is an old tradition for us."
            show sabiaemo normal at left
            s "So you really had to prove yourself to get this far. What now? Do you want to join the council, become a tribal shaman, or what?"
            show ylva closedhappy at right
            ylva "I think that's a separate question, my turn."
            show ylva normal at right
            ylva "What did you need to do to become a commander in the Lundari army?"
            show sabiaemo surprised1 at left
            s "I... human armies don't always work the same way."
            show ylva closednormal at right
            ylva "Was it because you were a noble?"
            show sabiaemo angry1 at left
            s "No! Well... not entirely. Lundar's armies promote based on merit, plenty of peasants have attained high rank!"
            show ylva normalnarrow at right
            ylva "How nice for the lowly peasants."
            show sabiaemo closed2 at left
            s "Hmph. It's not like I was just handed the position, I had to fight in multiple battles first. And I was a better commander than a soldier, anyway."
            show ylva normal at right
            ylva "That's a good point. Too often in warbands the strongest become chief, even if they aren't the best leaders."
            show sabiaemo annoyed2 at left
            s "Well, that happens for humans too."
        "Why do orcs speak in third person?" if ylvatalkthirdperson == False:
            $ ylvatalkthirdperson = True
            $ A_ylva += 1
            s "You must know it sounds idiotic, right? But it doesn't seem like it can be intelligence..."
            show ylva closedsad at right
            ylva "So judgmental... I guess I should be thankful you have the decency to ask the question."
            show ylva normal at right
            ylva "It's a custom inherited from our own language, though the language itself has mostly been lost to time. We had many different ways to refer to ourselves, pronouns with different implications."
            ylva "To refer to yourself directly was considered arrogant - declaring your opinion to be as meaningful as the laws of the gods. So in order to be polite, most orcs refer to themselves by name."
            show sabiaemo closed2 at left
            s "If you say so... but I hear a lot of orcs calling themselves \"me\"."
            ylva "Yes, we use that word in place of the more casual orcish pronoun. Using your name can get tiresome, after all."
            show sabiaemo annoyed1 at left
            s "Hmm... then do humans sound arrogant to orcs all the time?"
            show ylva closedhappy at right
            ylva "I think you already know the answer to that question."
            show ylva happy1 at right
            ylva "Of course, some of us understand that's not intended. That's why I speak like a human when I'm talking to you."
            show sabiaemo happy1 at left
            s "That makes sense. Thanks for explaining, Ylva."
            show ylva normal at right
            ylva "Honest question in return: does it not sound arrogant to you? Talking about yourself first instead of your people or your kingdom?"
            show sabiaemo eyebrow1 at left
            s "Lundar is strong because so many strong individuals are united, not because we all hold hands and sing songs."
            show ylva normalnarrow at right
            ylva "Hmm."
        "Have you noticed Ornshakar doing anything suspicious?" if (RGAnoticedcheating == True and ylvatalkcheating == False and recruitmentopened == False):
            $ ylvatalkcheating = True
            $ A_ylva -= 1
            show ylva normalnarrow at right
            ylva "Suspicious? What do you mean?"
            "Sabia quickly explained what she had seen. Ylva listened in silence, then shook her head."
            ylva "While it could have been magic involved with the match, magic is also used for many rituals. I doubt anything will come of it."
            s "Are you sure? Enhancement magic is your people's thing, it would be so easy to influence the result of a match..."
            show ylva angry1 at right
            ylva "Yes, because you know everything about my people. Speak no more of this, Sabia."
            show sabiaemo closed2 at left
            s "Ugh, sorry I brought it up."
            show ylva normalnarrow at right
            ylva "..."
        "Go back":
            return
    jump ylvaconvo1


label RGAdailyevents:
    if arenatime == 2:
        "Sabia woke up feeling a sense of tension, unlike over the past few days. She probably had a while before the female orc shaman arrived, but... she felt like she should prepare as much as possible. It was impossible to know how much time she had."
    elif arenatime == 3:
        call ylvaintroduction2
    elif arenatime == 4:
        call RGAinitiationritual
    elif arenatime == 5:
        call RGAqualificationround
    elif arenatime == 6:
        "Sabia woke up a little tired, but she couldn't let herself slow down: there were many events yet to go before the Red God's Arena would be complete."
        "Today, she didn't need to fight, as the arena would be used for some sort of grand spectacle. But tomorrow there was a melee event she could participate in, and the day after that, she'd be required to fight a public duel."
    elif arenatime == 7:
        "When Sabia woke, she took a moment to recall the day's events. There was some kind of large melee battle she could participate in, but it was optional and she had a major duel the next day."
        menu:
            "Participate":
                call RGAgeneralmelee
            "Skip it":
                "Deciding to save her strength, Sabia just began planning her day."
    elif arenatime == 8:
        call RGAsabiafight1
    elif arenatime == 9:
        call RGAhellhoundintro
    elif arenatime == 10:
        call RGAhellhoundmatch
    elif arenatime == 11:
        call RGAvehlis
    elif arenatime == 12:
        call RGAsabiafight2
    elif arenatime == 13:
        call RGAcaptainmelee
    elif arenatime == 14:
        call RGAmakhorintro
    elif arenatime == 15:
        call RGAmakhorchallenge2
    elif arenatime == 16:
        "Sabia woke with the knowledge that she had only one more day to prepare for the final fights of the Red God's Arena. For one day, however, all she needed to do was check on the fights of others."
        call RGAshamanevent
    elif arenatime == 17:
        call RGAsabiafight3
    elif arenatime == 18:
        call RGAfinalritual
    return


label RGAmiscevents:
    $ RGAdailycooldown = True
    if arenatime < 3:
        "Everything was still being set up. Orcs had begun to trade and spar, but the sands were empty."
    elif arenatime < 5:
        "The arena was still being sanctified and prepared for the event itself."
    elif arenatime == 6:
        $ L_orcs += 1
        "Sabia was surprised to see a grand battle taking place within the arena. Some orcs were wearing minotaur-like horns, others armor... she realized after a time that they were acting out a historical battle. Presumably one from the old wars, though she couldn't identify it."
        "She watched for a while, fascinated that they would do such a thing. She'd never heard soldiers speak of anything like this."
    elif arenatime == 9:
        "The theme of the day seemed to be animal fights: all manner of wild beasts had been brought into the arena. Some fought each other, others fought orcs, and the crowds seemed to enjoy it all. She suspected this was all nothing compared to the upcoming hellhound event, though."
    elif arenatime == 13:
        $ A_lutvrog += 1
        "Sabia looked over the matches in the arena, and to her surprise, Lutvrog was scheduled to fight. She made certain to come back in time for his fight."
        "Except it wasn't much of a fight."
        "The match appeared to be Lutvrog against three other orcs. They weren't weak, yet they went down one by one before Lutvrog's martial prowess."
        if lutvrogsex == True:
            "Sabia just watched, admiring the way the muscles of his body rippled and flexed as he moved. He was a brilliant combatant, but she was admiring more than just that."
        else:
            "Sabia watched him and could at least admire his raw skill. He was as good as any of the veterans in any force she'd ever commanded."
        "When the match was finally over, Lutvrog congratulated the other warriors and then departed. Sabia hurried to intercept him before he could completely leave the arena."
        call sabiabase
        show sabiaemo happy1 at left
        show lutvrogbase at right
        show lutvrogaxe at right
        show lutvrogwraps at right
        show lutvrogwrists at right
        show lutvrogemo normal at right
        with dissolve
        s "Great fight!"
        lut "Lutvrog would prefer to face a single worthy opponent. Matches such as this are too much like showing off."
        show sabiaemo normal at left
        s "You usually can't fight against a single opponent on a battlefield, though."
        lut "This is true. It is good to retain these skills as well."
        s "I'm guessing you're going to do well in plenty of matches. Does that mean you'll get a lot of the Red God's blessings?"
        lut "Though Lutvrog respects the spirits, Lutvrog does not know how much favor they have for mortals. It is better for us to trust in our own strength."
        s "You said it."
        if lutvrogsex == True:
            "Part of her wanted to prolong the conversation, if only to watch the sweat trickle down his sculpted chest, but Lutvrog had other business to attend to. Sabia gave a friendly nod and let him go on his way."
        else:
            "Part of her wanted to prolong the conversation, but Lutvrog had other business to attend to. Sabia gave a respectful nod and let him go on his way."
    else:
        $ temp1 = renpy.random.randint(1,4)
        if temp1 == 1:
            "Sabia glanced into the arena, but it was nothing but random orc thugs fighting each other. Nothing interesting there."
        elif temp1 == 2:
            "The arena was quiet, but it was only because Ornshakar and Ylva were performing some sort of ceremony. No doubt important to the shamans, but not particularly relevant to her."
        elif temp1 == 3:
            "For once, there was nothing really going on, just a few lowly orcs cleaning up in between events."
        elif temp1 == 4:
            "There was a duel to the death going on in the arena, but since it contained no one that Sabia knew, she decided that it wasn't worth watching."
    return


label RGAtraining:
    scene bg RGAbg2 with dissolve
    if RGAtrainingintro == False:
        $ RGAtrainingintro = True
        "When Sabia approached the arena, she was surprised to see that camps had grown up around it. Orcs from a variety of tribes had gathered - and they brought a wide variety of different things along with them."
        "There were many different styles of tents and clothing, but Sabia didn't really care about that. What mattered was that many of them were actively training. She spotted free weights, weighted practice swords, even a few magical training artifacts."
        "With access to all of these, she had new possibilities to train herself. Best to take advantage of it."
    "Sabia glanced around the training equipment, trying to decide what she should use."
    show screen infohud("left")
    menu:
        "Check in on the arena" if RGAdailycooldown == False:
            call RGAmiscevents
            jump RGAtraining
        "Spar with orcs (50 stamina)" if Sabia.hp >= 1:
            if Sabia.stamina >= 50:
                $ Sabia.stamina -= 50
                $ enemy_level = 7
                $ enemy_maxhp = 400
                $ enemy_hp = enemy_maxhp
                $ enemy_type = 1
                $ enemy_skills = [Enemyattack]
                $ enemy_attack = 65
                $ enemy_defense = 30
                $ enemy_magdefense = 0
                call randorc
                $ player = Sabia
                $ enemy = random_orc
                call duel
                if _return== "Victory":
                    "Sabia left her grumbling opponent with a smile on her face. There were no rewards for fights like these but the fights themselves... but she didn't get many chances to spar with orcs this skilled, so she wanted to take advantage of the opportunity."
                else:
                    "Sabia winced and picked herself up carefully. If that had been a real battle, she would have been dead."
                play music orccamp fadeout 2.0 fadein 2.0
                jump RGAtraining
            else:
                "Sabia was too tired to spar."
                jump RGAtraining
        "Stamina training (75 stamina) ([RGAstamina]%%)" if (RGAstamina < 100 and RGAstaminapoint == False):
            if Sabia.stamina < 75:
                "Sabia was too tired to train."
                jump RGAtraining
            $ RGAstamina += 20
            $ Sabia.stamina -= 75
            if RGAstamina >= 100:
                $ Sabia.maxstamina += 20
                $ RGAstaminapoint = True
                "At the end of training, Sabia was gasping for breath, but she felt like she'd made a real difference. She'd be able to fight longer than before... once she rested up a bit."
            else:
                "Sabia did her best to train her stamina. She felt like she had improved, but she'd need to put in a lot more work to make a breakthrough."
            jump RGAtraining
        "Offense training (75 stamina) ([RGAattack]%%)" if (RGAattack < 100 and RGAattackpoint == False):
            if Sabia.stamina < 75:
                "Sabia was too tired to train."
                jump RGAtraining
            $ RGAattack += 20
            $ Sabia.stamina -= 75
            if RGAattack >= 100:
                $ Sabia.add_str(1)
                $ RGAattackpoint = True
                "To Sabia's surprise, her wooden practice sword hacked through the practice dummy. Her hands were aching and she'd been practicing a long time, but she never imagined she'd actually break it. She really was getting stronger."
            else:
                "Sabia did her best to train her offensive skills. She felt like she had improved, but she'd need to put in a lot more work to make a breakthrough."
            jump RGAtraining
        "Defense training (75 stamina) ([RGAdefense]%%)" if (RGAdefense < 100 and RGAdefensepoint == False):
            if Sabia.stamina < 75:
                "Sabia was too tired to train."
                jump RGAtraining
            $ RGAdefense += 20
            $ Sabia.stamina -= 75
            if RGAdefense >= 100:
                $ Sabia.add_con(1)
                $ RGAdefensepoint = True
                "Usually Sabia finished sparring with a few bruises, but that day she felt fine. She'd gotten a lot better at rolling with the blows and avoiding real injury."
            else:
                "Sabia did her best to train her defensive skills. She felt like she had improved, but she'd need to put in a lot more work to make a breakthrough."
            jump RGAtraining
        "Dodging training (150 stamina)" if RGAdodgetraining == False:
            if Sabia.stamina < 150:
                "Sabia was too tired to train."
                jump RGAtraining
            $ RGAdodgetraining = True
            $ Sabia.stamina -= 150
            "Though Sabia wasn't sure if she'd need to participate, it was obvious from all the beasts that had been brought that some of the matches would be against wild animals. That required a completely different style of fighting than dueling other opponents."
            "But it wasn't so different than she remembered from the minotaur front. With opponents that were so massive, dodging was always advised over blocking, even for men in plate armor. She remembered many of the techniques they had used and tried to practice them now."
            "The same techniques would have to be useful against monsters, or at least Sabia hoped so. Minotaurs were actually intelligent and could adapt better, so presumably they'd be even more effective against simple beasts."
            "But those beasts had nasty fangs and claws... Sabia intended to keep far away from them. The orcs seemed to find her training bizarre and a few laughed, but she'd get the last laugh when she survived."
            "By the end of her time, she thought she'd managed the basics. Maybe not the dodging skills of a master, but they should work against large beasts."
            jump RGAtraining
        "Skill training: Centering (250 stamina)" if centeringlearned == False:
            if Sabia.stamina < 250:
                "Sabia was too tired to train."
                jump RGAtraining
            $ centeringlearned = True
            $ Sabia.stamina -= 250
            $ Sabia.actives.append(Centering)
            "Sabia focused her attention on mastering a skill that she had once been taught, but never been able to use consistently in combat."
            "The technique of \"Centering\" was an old skill that allowed someone to refocus, regain their footing, and shake off shock. It was excellent against opponents who tried to debilitate their target before going in for a killing blow."
            "In the past, she'd been able to do it in practice sessions, but never in actual combat. She felt the pain too acutely, was too focused on threats, and generally ended up just hesitating instead of centering herself."
            "She was surprised how much more easily it came to her now. At the end of her long sparring session, Sabia felt as though she could use the skill consistently in actual combat."
            jump RGAtraining
        "Skill training: Interrupting Blow (250 stamina)" if interruptingblowlearned == False:
            if Sabia.stamina < 250:
                "Sabia was too tired to train."
                jump RGAtraining
            $ interruptingblowlearned = True
            $ Sabia.stamina -= 250
            $ Sabia.actives.append(Interruptingblow)
            "Sabia focused all her attention on trying to develop something new: a technique to interrupt an opponent's preparation."
            "The best interruption, of course, was killing the enemy. But she had to admit that now that she wasn't fighting lowly opponents, there would be times when it just wouldn't be possible for her to do so."
            "In the end, she mastered something she thought would work: a swift attack that might not kill, but would definitely force the opponent to pour energy into defending against it."
            jump RGAtraining
        "Skill training: Defense Breaker (125 stamina)" if (RGAlutvrogtrain == True and defensebreakerlearned == False):
            if Sabia.stamina < 125:
                "Sabia was too tired to train."
                jump RGAtraining
            $ defensebreakerlearned = True
            $ Sabia.stamina -= 125
            $ Sabia.actives.append(Defensebreaker)
            "Sabia set to working on the skill that Lutvrog had attempted to teach her. In theory, she could strike her opponents and throw them off balance, setting up for a stronger attack in the future."
            "After a long day of practice, Sabia succeeded in pulling off the skill reliably. It was ready for use in combat, and she was sure she'd get a chance soon."
            jump RGAtraining
        "Preparation: Armor Upgrades" if gotheavyleather == False:
            if Inventory.has_item(Leatherarmor) > 0 or Sabia.armor == Leatherarmor:
                "There was a tent set up beside the arena where orcs from another tribe were selling and upgrading equipment. Their weapons looked shitty, but their armor wasn't bad. They told Sabia they could upgrade her leather armor for a fee."
            else:
                "There was a tent set up beside the arena where orcs from another tribe were selling and upgrading equipment. Their weapons looked shitty, but their armor wasn't bad. Unfortunately, they said Sabia didn't have anything they could upgrade."
                jump RGAtraining
            menu:
                "Upgrade (25 Lundils)":
                    if money < 25:
                        "Sabia didn't have enough money."
                        jump RGAtraining
                    $ gotheavyleather = True
                    $ money -= 25
                    $ Sabia.unequip(Sabia.armor, inventory="yes")
                    $ Sabia.equip(Heavyleatherarmor)
                    $ Inventory.rem_item(Leatherarmor)
                    "Handing over the money, Sabia watched nervously while the orcs tinkered with her armor. She'd been afraid they'd ruin it, but though they added a lot to the weight, she thought the end results would provide better protection."
                    "If she couldn't purchase decent equipment, Sabia considered that she might need to upgrade what she had. Hopefully on her own terms instead of handing it over to orcs, but that was a matter to consider in the future."
                    "For now, she tried on her new armor. It looked decent and it seemed stronger, so she was pleased."
                    jump RGAtraining
                "Not now":
                    jump RGAtraining
        "Preparation: Makhor Poison (20 Lundils)" if (RGAobservedmakhor == True and money >= 20 and RGAmakhorpoison == False and arenatime < 15):
            $ RGAmakhorpoison = True
            $ dom += 1
            $ money -= 20
            "Though Sabia had mixed feelings about it, she'd seen the size of the Makhor and needed every advantage she could get to prepare to face it."
            "It took her a while to figure it out, eventually she spotted an area beside the holding cell for the Makhor. Within they had a number of strange items, including a tail that looked like the Makhor's... smaller, though, which puzzled Sabia a little."
            "From the tail, there were orcs extracting the anti-Makhor poison. Sabia had to pay 20 Lundils to get a single application of it, but the orcs promised it would make all the difference when it was time to fight."
            "Sabia shifted the vial in her hand as she left. It was small, but it felt extremely heavy."
            jump RGAtraining
        "Special training with someone (100 stamina)" if (RGAtraincooldown == False and RGAlutvrognevescene == False):
            if Sabia.stamina < 100:
                "Sabia was too tired to train."
                jump RGAtraining
            menu:
                "Training with Lutvrog" if (A_lutvrog >= 5 and RGAlutvrogtrain == False):
                    $ RGAtraincooldown = True
                    $ Sabia.stamina -= 100
                    hide screen infohud
                    call RGAlutvrogtraining
                    jump sabiahq2
                "Training with Neve" if (A_neve >= 5 and RGAnevetrain == False and maplytortured == False):
                    $ RGAtraincooldown = True
                    $ Sabia.stamina -= 100
                    hide screen infohud
                    call RGAnevetraining
                    jump sabiahq2
                "Training with Neve and Lutvrog" if (RGAlutvrogtrain == True and RGAnevetrain == True and RGAlutvrognevescene == False):
                    $ RGAtraincooldown = True
                    $ Sabia.stamina -= 100
                    hide screen infohud
                    call RGAnevelutvrogtraining
                    jump sabiahq2
                "Don't train":
                    jump RGAtraining
        "Investigate arena between matches" if (arenatime >= 6 and RGAnoticedcheating == False):
            call RGAshamancheating
            jump RGAtraining
        "Investigate strange cluster of orcs" if (arenatime >= 6 and RGAbettingdone == False):
            call RGAbetting
            jump RGAtraining
        "Investigate Makhor preparations" if (arenatime >= 14 and RGAobservedmakhor == False):
            call RGAmakhorchallenge1
            jump RGAtraining
        "Leave":
            hide screen infohud
            jump lowerorccamp
    return


label RGAlutvrogtraining:
    $ RGAlutvrogtrain = True
    scene bg countryside
    call sabiabase
    show lutvrogbase at right
    show lutvrogwraps at right
    show lutvrogwrists at right
    show lutvrogaxe at right
    show lutvrogemo normal at right
    with dissolve
    s "It's really not too much trouble to come train with me?"
    lut "Not at all. Lutvrog has good sparring partners, but few are as interesting as you."
    s "Well, I'll see if I can't live up to your expectations. Normal sparring, then?"
    lut "To start. Lutvrog has an idea."
    scene bg black with dissolve
    pause 1
    scene bg countryside
    call sabiabase
    show sabiaemo happy1 at left
    show lutvrogbase at right
    show lutvrogwraps at right
    show lutvrogwrists at right
    show lutvrogaxe at right
    show lutvrogemo normal at right
    with dissolve
    s "Whew! I can't keep up with you when you're serious."
    lut "No, you did well. Lutvrog believes you may be able to learn a useful technique."
    show sabiaemo normal at left
    s "A technique?"
    lut "Lutvrog has deciphered a text describing a special throw designed for smaller orcs. It was meant to reduce the difference in strength, and may be appropriate for you."
    s "Sounds great, I'll do my best!"
    scene bg countryside
    "Though Sabia was able to learn the basics of the technique while they sparred, she didn't feel ready to use it in combat. She would need to finish training the skill on her own later."
    "Still, it was something she never would have thought to do on her own, and training with Lutvrog always left her feeling better. Once she had time to reflect on their sparring, she was sure she'd be stronger."
    if lutvrogsex == True:
        "Sabia almost propositioned Lutvrog, imagining how good it would feel to fuck with sweat dripping down their bodies... but he seemed focused on the Red God's Arena and she did need to take it seriously, so in the end she just thanked him and returned to camp."
    else:
        "Lutvrog nodded respectfully as they left and Sabia returned to camp, considering what she should do next."
    $ A_lutvrog += 1
    $ Sabia.xp += 5
    $ RGAattack += 20
    $ RGAstamina += 10
    if RGAattack >= 100:
        $ RGAattack = 99
    if RGAdefense >= 100:
        $ RGAdefense = 99
    if RGAstamina >= 100:
        $ RGAstamina = 99
    return


label RGAnevetraining:
    $ RGAnevetrain = True
    scene bg countryside
    call sabiabase
    show neve1 at right
    show neveemo normal at right
    with dissolve
    "Neve led Sabia out of camp... surprisingly far out of camp. The other woman just seemed to be enjoying the walk, but abruptly when they reached an area that seemed the same as all the rest, Neve stopped and stretched."
    show neveemo happy2 at right
    n "This will do just fine. You ready to train?"
    show sabiaemo happy1 at left
    s "Sure! Did you have something in particular in mind?"
    show neveemo happy1 at right
    n "I realized that the two of us haven't actually sparred. Thought we could have fun with the basics... I guarantee I can provide something different than you get from your average orc!"
    show sabiaemo normal at left
    "That seemed good enough to Sabia, so they began sparring. Neve proved to be as skilled as Sabia had expected, using her short blades like an artist."
    "If she'd been aiming to kill Sabia, she definitely could have done so, yet strangely Sabia didn't feel threatened at all. Even when Neve had a blade to her throat, she had a wry smile that suggested they were just playing. And her control meant that Sabia didn't need to fear getting accidentally cut."
    "What Neve had said earlier was true: this really was different than fighting orcs. Except for fighting Maply, Sabia had become too accustomed to fighting opponents who were bigger than she was. She was completely unprepared for Neve's quick strikes, even if they didn't have much force behind them compared to an orc's strength."
    show neveemo normal at right
    "But just when Sabia was getting comfortable and feeling like she was learning a lot, Neve became distracted. It annoyed Sabia at first, then she decided that she needed to say something."
    show sabiaemo closed2 at left
    s "Can't you take this more seriously? I may not b-"
    n "Quiet... no, it's too late for that. Get back."
    show sabiaemo surprised1 at left
    "Before Sabia could object, Neve grabbed her arm, then tossed her to the side, where Sabia tangled in the boughs of a tree. She was shocked by how easily Neve had done it... but realized there was something much more serious."
    scene bg countryside
    show neve1 at center
    show neveemo normal at center
    with dissolve
    "Orcs were emerging from hiding places around them in a ring. Sabia worried that she'd lost her sword, but they seemed entirely focused on Neve."
    show orcbase2:
        xanchor 0.0 xpos 1.0
    show orcloincloth2:
        xanchor 0.0 xpos 1.0
    show orcemo2 normal:
        xanchor 0.0 xpos 1.0
    show orcbaseL:
        xanchor 1.0 xpos 0.0
    show orcloinclothL:
        xanchor 1.0 xpos 0.0
    show orcemo normalL:
        xanchor 1.0 xpos 0.0
    pause(0.01)
    show orcbase2 behind neve1 at right
    show orcloincloth2 behind neve1 at right
    show orcemo2 normal behind neve1 at right
    show orcbaseL behind neve1 at left
    show orcloinclothL behind neve1 at left
    show orcemo normalL behind neve1 at left
    with move
    "Soon they had Neve surrounded, while Sabia could only watch. She was fairly sure that none of the warriors were from Groknak's tribe, but that didn't explain what they were doing. Horny orcs might gang up on a woman, but not in a serious ambush like this."
    stop music fadeout 2.0
    show neveemo happy2 at center
    n "Hello, boys! Get lost on your way to camp?"
    show orcemo2 normalopen at right
    orc "Come with us, Vegardan, and it will be easier for you."
    n "Come with you where? Surely we can do everything we need right here..."
    show orcemo normalopenL at left
    orc "We're not playing games. Surrender and you won't get hurt."
    show neveemo happy1 at center
    n "It's considerate of you to use non-lethal weapons. So whoever sent you wants to capture me, huh?"
    "The orcs shifted uncomfortably at that, and Sabia realized that it was true. Though many of the orcs carried axes, none of them was currently wielding them. Instead, they mostly had clubs and nets."
    orc "This is mistake. We need hit her fast."
    n "So, you're not going to stand down, huh? Then I suggest you all draw your real weapons."
    show orcemo2 angry at right
    orc "Stupid elf. You think you can die instead of get fucked?"
    show neveemo normal at center
    n "You misunderstand. I didn't suggest that for my sake."
    play music "<from 1.2>music/killers.mp3"
    hide neveemo normal at center
    show neve3 at center
    show neveemo battle1 at center
    with Dissolve(1)
    hide neve1
    n "I thought you might want to die like warriors."
    "Crimson light shone from Neve's armor, and a moment later she was gone, a shadow in the wind."
    hide neveemo battle1
    hide neve3
    show expression "database/actors/neve/neve3.png" as nevebody at center:
        alpha 0.3
    show expression "database/actors/neve/expressions/battle1.png" as neveface at center:
        alpha 0.4
    show neve3 at center:
        alpha 0.3
    show neveemo battle1 at center:
        alpha 0.4
    pause(0.01)
    show neve3 behind orcbase2 at right
    show neveemo battle1 behind orcbase2 at right
    with move
    $ renpy.show("orcbase2mask", at_list=[right], what=AlphaBlend(Transform("orcbase2", alpha=0.9), "orcbase2", bloodhit_effect, alpha=True))
    pause(0.01)
    hide orcbase2 at right
    hide orcloincloth2 at right
    hide orcemo2 angry at right
    hide orcbase2mask
    hide nevebody
    hide neveface
    show neve3 at right:
        linear 0.5 alpha 1.0
    show neveemo battle1 at right:
        linear 0.5 alpha 1.0
    with Dissolve(1)
    "That shadow blurred to one side and suddenly one of the orcs was decapitated, body seeming to crumple slowly compared to Neve."
    show expression "database/actors/neve/neve3.png" as nevebody at right:
        alpha 0.3
    show expression "database/actors/neve/expressions/battle1.png" as neveface at right:
        alpha 0.4
    show neve3 at right:
        alpha 0.3
    show neveemo battle1 at right:
        alpha 0.4
    pause(0.01)
    show neve3 behind orcbaseL at left
    show neveemo battle1 behind orcbaseL at left
    with move
    show neve3 behind orcbaseL at left:
        xzoom -1
    show neveemo battle1 behind orcbaseL at left:
        xzoom -1
    $ renpy.show("orcbaseLmask", at_list=[left], what=AlphaBlend(Transform("orcbaseL", alpha=0.9), "orcbaseL", bloodhit_effect, alpha=True))
    pause(0.01)
    hide orcbaseL at left
    hide orcloinclothL at left
    hide orcemo normalL at left
    hide orcbaseLmask
    hide nevebody
    hide neveface
    show neve3 at left:
        linear 0.5 alpha 1.0
    show neveemo battle1 at left:
        linear 0.5 alpha 1.0
    with Dissolve(1)
    "She flashed in the other direction next, a dagger going through the heart of another orc. With a smooth motion, Neve tossed him to the side, flinging him from her blade like trash."
    "The orcs recovered faster than Sabia did, beginning to throw their nets and trying to use their numbers against Neve."
    hide neve3
    hide neveemo battle1
    show neve3 at center
    show neveemo battle1 at center
    with dissolve
    "It didn't matter."
    "Neve moved among them as a shadowy blur, leaving a trail of glowing red streaks where she passed. Orcs fell everywhere she went, one of them even split in half at the waist. Neve was already on to her next target before his upper body had fallen to the ground."
    "Earlier Sabia had harbored ideas of coming to help, but now those seemed futile. She had never seen anyone kill so easily. There had to be magical enhancement... Neve's short blades were cutting orcs in half as if they were made of silk. At one point she reversed her grip and struck an orc with her fist instead, and the blow sent the orc tumbling head over heels, its head caved in."
    "Though it seemed like a long time that Sabia could only watch in shock, it didn't even last a minute. Soon it was just Neve standing on a field of corpses. No, it seemed she had missed one, crawling away with only a severed leg."
    show neveemo battle2 at center
    "Then Neve began walking after him, and Sabia realized that Neve had not missed."
    scene bg countryside with dissolve
    "Sabia climbed down from the tree shakily, trying not to listen. The orc shouted at first, but soon began begging and pleading. Whatever Neve was saying, her words were too soft to hear."
    call sabiabase
    show sabiaemo surprised1 at left
    with moveinleft
    "Back on her feet, Sabia still felt unsteady. Should she run? This was obviously one of Neve's secrets, and she might kill to keep it. Not that it would do any good to run away, given her speed."
    "Sabia tried to comfort herself with the fact that Neve had moved her out of the way first. She wouldn't have done that if she'd planned to kill her later."
    show sabiaemo surprised3 at left
    "That wasn't much comfort when Neve finished with the orc: she brought her foot down on the orc's skull, pulverizing it with a sickening crunch. And then she turned back toward Sabia."
    show neve3 at center
    show neveemo battle1 at center
    with moveinright
    n "..."
    s "Neve... I..."
    show neveemo closed1 at center
    n "Seros, thy child offers this blood. Seros, thy child thanks thee. Seros, thy child walks with thee."
    play music orccamp fadeout 2.0 fadein 2.0
    show neve1
    hide neveemo closed1 at center
    show neveemo closed1 at center
    with dissolve
    n "..."
    show sabiaemo closed2 at left
    "Something departed from the air and Sabia found herself taking a deep breath instinctively. Her body suddenly felt drained and nearly ready to collapse, but she kept herself upright, staring at Neve. She looked like she was back to normal, even the blood on her knives gone."
    show neveemo normal at center
    n "Well, that didn't go quite how I planned. I knew we were being followed, but I expected it to just be some spies."
    s "..."
    show neveemo happy3 at center
    n "Something the matter, Sabia? You look a little pale."
    show sabiaemo surprised2 at left
    s "What the hell was that?"
    show neveemo happy1 at center
    show sabiaemo surprised1 at left
    n "If you were anyone else, I might answer that with a blade. But since you've proven yourself better than I expected..."
    show neveemo closed1 at center
    n "This armor is called the Faces of Seros. I don't know if you've ever paid attention to Vegardan legends, but it's said to be cursed armor that kills whoever wears it."
    show neveemo smirk1 at center
    n "That part turns out to be... negotiable."
    show sabiaemo closed2 at left
    "Finally believing that Neve wasn't going to harm her, Sabia managed to calm down, but her heart was still pounding."
    s "Alright, I'll accept that answer. We all have our secrets, and I'll keep yours."
    n "How sweet of you."
    show sabiaemo normal at left
    s "I'm actually downright impressed, but I'll contain myself. What now? Was this all just a pretext to lure them out?"
    show neveemo happy2 at center
    n "No, I really did want to spar with you. And I had fun. Working on skill is more enjoyable than using my full strength."
    s "What did you find out from the last one? Just who were they?"
    show neveemo closed3 at center
    n "Unfortunately, the person who hired them was no fool. They didn't know much beyond the reward they were offered, though they did imply a few facts."
    show neveemo normal at center
    n "They were sworn to secrecy, and paid a considerable amount just for this. They had some warning about me, but not enough. So I know that I was specifically targeted, and by someone very cautious. Presumably high in orc leadership, but not this tribe."
    s "Have you ever dealt with anything like this before?"
    n "No, this is a first. I'll have to investigate things."
    s "I see."
    show neveemo happy3 at center
    n "So, you want to go back to sparring?"
    show sabiaemo surprised1 at left
    s "Maybe, uh, maybe let's do a lighter form of training..."
    scene bg countryside with dissolve
    "Neve chuckled but complied, instead helping Sabia work through improved defensive stances. The simple training helped Sabia recover a little from the experience, though it was hard to forget with all the corpses lying around them."
    "In the end, Neve stayed back to deal with them, while Sabia headed back to camp. She still wasn't sure what to think, but she'd definitely remember this when making future plans."
    $ A_neve += 1
    $ Sabia.xp += 5
    $ RGAdefense += 20
    $ RGAstamina += 10
    if RGAattack >= 100:
        $ RGAattack = 99
    if RGAdefense >= 100:
        $ RGAdefense = 99
    if RGAstamina >= 100:
        $ RGAstamina = 99
    return


label RGAnevelutvrogtraining:
    $ RGAlutvrognevescene = True
    scene bg countryside
    call sabiabase
    show lutvrogbase at right
    show lutvrogwraps at right
    show lutvrogwrists at right
    show lutvrogaxe at right
    show lutvrogemo normal at right
    show neve1 at center
    show neveemo normal at center
    with dissolve
    "Sabia had been uncertain if it would work out, but to her surprise both Neve and Lutvrog had agreed to come with her surprisingly easily. They seemed a little reserved, but nothing compared to how awkward it could potentially have been."
    "Setting aside memories of fucking Lutvrog and of Neve slaughtering orcs, Sabia tried to just view them as fellow warriors she needed to learn from."
    s "I'm rusty on fighting multiple opponents at once, and I might need to for the arena. Now, either of you could beat me alone, but I hope you won't go too easy on me."
    lut "Lutvrog respects this goal and hopes we can have a productive training session."
    show neveemo happy2 at center
    n "No problem. And maybe we can make it a three-way fight later, hmm?"
    show neveemo happy3 at center
    "Had Neve meant that as innuendo? Her tone sounded serious, but her eyes were playful... Sabia hastily pushed the images that brought to mind aside and focused fully on training."
    "As expected, training with the two of them at once was brutal. Each was capable of attacking from so many angles, when they managed to flank Sabia she had basically no defense against them."
    "But as the day wore on, she started to gain some. Not that she could stand up to them for real, but she avoided flanking, managed to ward off some blows, and generally embarrassed herself less."
    "She was surprised how well Neve and Lutvrog seemed to work together, but perhaps that was just their skill as warriors. When they switched to an even fight between the three of them, Neve grinned at Lutvrog and he nodded respectfully to her."
    "Though Sabia had expected to feel useless, it actually wasn't like that. Though Lutvrog and Neve focused on each other, she wasn't so weak that they could brush her aside - she could take advantage of their distraction and try to break up their dueling."
    "That was with both of them holding back, though. Sabia found herself wondering who would win if they fought for real. Though Lutvrog seemed to have the slight upper hand, Neve's eyes never glowed red. Given how much stronger she could be... it would depend on how much strength Lutvrog had yet to show."
    "When they finished, Sabia sprawled back on the ground, chest heaving as she caught her breath. Lutvrog and Neve at least had the decency to sit down on either side of her and breathe deeply, though they could have kept fighting."
    if dom >= 10:
        "Oddly, they seemed to be glancing at one another over her. Sabia realized what they were planning a moment before they acted..."
        menu:
            "Take charge":
                $ dom += 1
                call RGAnevelutvrogD
            "Follow Neve's lead":
                $ sub += 1
                call RGAnevelutvrogS
    else:
        "Oddly, they seemed to be glancing at one another over her, but when Sabia looked more carefully it was too late."
        call RGAnevelutvrogS
    scene bg countryside
    show lutvrogbase at right
    show lutvrogemo happy at right
    show nevenaked1 at left
    show neveemo happy3 at left
    with dissolve
    n "Ahh, that was satisfying. How have we not done this before, Lutvrog?"
    lut "Lutvrog was under the impression you did not like him."
    n "Actually, my question was rhetorical. This was my fault, because I had the wrong impression of you."
    show lutvrogemo normal at right
    lut "How so? Lutvrog tries to be direct."
    n "Yes, but that made it easy for me to make assumptions. Consummate warriors like you tend to fall into a few stereotypes. For example, I thought you might demand that we be life-bonded mates and a warrior pair or something."
    show neveemo eyeroll1 at left
    n "Like he who shall not be named. I can't get on board with such a cheesy dream of racial unity, much less serving as a figurehead."
    lut "Ah. Lutvrog understands your concern, but Lutvrog does not have such grand ambitions."
    show neveemo closed2 at left
    n "It was either that or you'd get all worked up over the fact that I was strong and want to break me. The first few orcs to think that way were funny, but I just get so bored of them."
    lut "That does not interest Lutvrog either. Pleasure shared is pleasure shared, and no more."
    show neveemo happy2 at left
    n "Yeah, I see that you get that. I had you wrong, Lutvrog, sorry about that."
    show neveemo happy3 at left
    n "Honestly, you may be a little too romantic for me. I like it rough sometimes, too."
    show lutvrogemo happy at right
    lut "Lutvrog is not certain he will hold your interest. But perhaps we can continue having fun with our... mutual friend."
    n "Heh, she's a cutie, isn't she? I'm really interested to see what she'll become..."
    play music orccamp fadeout 2.0 fadein 2.0
    scene bg black
    with dissolve
    "Sabia woke up in her tent, wrapped in a blanket. Her body ached from the training, but she actually didn't feel exhausted - the sex and the nap left her surprisingly refreshed."
    $ Sabia.xp += 5
    $ RGAstamina += 20
    $ Sabia.stamina += 40
    if Sabia.stamina > Sabia.maxstamina:
        $ Sabia.stamina = Sabia.maxstamina
    if RGAattack >= 100:
        $ RGAattack = 99
    if RGAdefense >= 100:
        $ RGAdefense = 99
    if RGAstamina >= 100:
        $ RGAstamina = 99
    return


label RGAbetting:
    $ RGAbettingdone = True
    scene bg RGAbg2
    call sabiabase
    "As Sabia explored near the arena, she spotted a band of orcs clustered around something. Mostly Groknak's warriors, so she decided to approach and see what was going on."
    "When they saw her they immediately grew quiet, but it was too late, Sabia had overheard them. They were betting on the outcome of the matches that day. Sabia glanced toward the orc managing the bets and raised an eyebrow."
    hide orcbase2 at right
    hide orcloincloth2 at right
    hide orcstomach2 at right
    hide orcemo normal2 at right
    show sabiaemo eyebrow1 at left
    s "Having fun, are we?"
    orc "Come on, we're just havin' a little wager..."
    show sabiaemo normal at left
    "Sabia wasn't sure about the rules of gambling on the Red God's Arena, but judging from their guilt, it was probably frowned upon. That didn't mean that she needed to be harsh about it, though. Sabia considered her options..."
    menu:
        "Let it go":
            $ L_orcs -= 1
            show sabiaemo happy1 at left
            s "I'm not here to condemn anyone. What you do on your own time is your own business."
            "The orcs nodded approvingly, glad their fun hadn't been interrupted. Sabia left, having given them a slightly better impression of her. One lesson she'd learned as a commander was that there was no point being a hardass when your authority wasn't being challenged."
        "Condemn them harshly":
            $ L_orcs -= 1
            $ dom += 1
            $ A_ylva += 1
            show sabiaemo angry1 at left
            s "This is a disgrace! Mocking the Red God like this..."
            "It seemed that her feigned anger was effective, because the orcs slunk off. Sabia didn't really care, but hopefully she'd benefit from acting pious and following the rules."
        "Join them":
            show sabiaemo happy1 at left
            s "No worries, boys, I just wanted to get in on this. What's the starting bid?"
            orc "Ummm... okay, me explain rules..."
            "It turned out to be a pretty simple odds system on each fight. Not much less complex than human soldiers liked to spend time with, actually. Sabia had avoided such things with her own troops, but since she'd already lowered herself to work with orcs, she figured she might as well bet."
            if L_orcs >= 10:
                $ L_orcs += 1
                if L_orcs >= 20:
                    $ money += 20
                    "Several rounds later, Sabia was up 20 Lundils. Her battle experience and familiarity with orcs had made it easy to take the right risks. The orcs grumbled at her taking their money, mostly but not entirely good-naturedly."
                else:
                    $ money += 10
                    "Several rounds later, Sabia was up 10 Lundils. She'd judged a few orcs wrong, but otherwise her experience had served her well. The orcs grumbled at her taking their money, mostly but not entirely good-naturedly."
                "Sabia paused between rounds, wondering if she should continue. She'd proved herself not uptight by participating, continuing to take their money might work against her. It was pathetically small amounts, anyway..."
                menu:
                    "Domination: Take them for all they're worth":
                        $ dom += 1
                        $ money += 25
                        $ L_orcs -= 1
                        "Grinning, Sabia decided to give them no mercy. By the time the betting group disbanded, they were all grumbling, but Sabia was up 25 more Lundils."
                    "Finish playing":
                        "Deciding that she'd done enough, Sabia bowed out before they could win their money back. Best to finish things quick and give them a positive impression of her."
                    "Submission: Pretend to lose gracefully":
                        $ sub += 1
                        $ money -= 5
                        $ L_orcs += 1
                        "Deciding that giving a positive impression was more important than losing a pathetic amount of money, Sabia started losing more matches, occasionally losing big and cursing when she did so."
                        "She let herself win occasionally, though, and in total she was only down 5 Lundils from her former position. But letting them take some of their money back put the orcs in a better mood, since it didn't seem like she was fleecing them."
                        "When she'd had enough, Sabia left the group a little richer and with a better reputation. She should have done this with her old soldiers..."
            else:
                $ L_orcs += 1
                "Sabia did her best to bet on the outcome of the current fights, but to her surprise found that she wasn't very good at judging the victors. She could gauge warriors fairly well, but wasn't familiar enough with details particular to orcs."
                "In the end, she barely made back the money she'd started with. It wasn't a complete loss, though - soldiers liked graceful losers, and by the time she left, she'd given them a slightly better impression of her."
    return


label RGAshamancheating:
    $ RGAnoticedcheating = True
    "Sabia happened to amble through the arena at a quiet moment, in between matches. A few orcs were cleaning off the sands, while Ornshakar was apparently blessing the grounds."
    "Normally, Sabia would be content to ignore him and be thankful she avoided an encounter. But this time... there was something odd about his rituals. He was sprinkling metal dust in the arena, and she had a feeling she knew what metal it was."
    "Getting closer to feel if there was any magic would be impossible, so Sabia instead stayed to watch the next match. It was unremarkable... but the winning warrior was wearing a crown with two antlers, similar to Ornshakar."
    "Sabia looked after the shaman as he left, then headed down to the sands. The metal dust had long been kicked away, but Sabia could have sworn that some kind of magic had been in play there. Was something shady going on?"
    "That seemed almost certain. But without a way to determine exactly what it was, Sabia didn't know how to take advantage of it."
    return


label RGAinitiationritual:
    "When Sabia awoke, she heard the sound of deep drums booming from the edge of camp. She quickly woke up, got her equipment, and headed out to the arena."
    scene bg RGAbg2 with dissolve
    "Though the foundation and walls had been pre-built some distance from camp, it was surprising how quickly the orcs had built the palisade around it and made the whole thing look like a proper arena."
    if L_orcs < 10:
        "Sabia rolled her eyes. Of course they were willing to put in effort when it came to a barbaric rituals like this."
    "Not all orcs had woken up either, so it seemed Sabia was early. She found a place to sit where she wouldn't be jostled too much and set about watching."
    "Ylva and Ornshakar were doing some final ritual down on the sands, kneeling in opposite corners of the arena and apparently meditating. Sabia didn't feel any kind of magic coming from them, but didn't really trust her impressions from this distance. After a while, they moved to sit in the remaining two corners, still opposite one another."
    scene bg RGAbg4 with dissolve
    "By the time they were finished, the stands were mostly filled as well. The shamans moved to one wall of the arena, as if waiting. A moment later Sabia understood, as Warchief Groknak strode out onto the sands."
    show groknak normalopen at center
    with moveinright
    g "Warriors! At the dawn of the new year, we give thanks to the Red God! Now we shall offer sweat and blood!"
    "That was all he said, but as his voice boomed out over the stands, the orcs let out a wild cheer. Sabia decided to stay silent, since her voice would be drowned out regardless. With that, Groknak stalked away to a large chair that had been prepared for him."
    hide groknak normalopen at center
    with moveoutright
    show ylva normal at left
    show ylva2 arm2 at left
    show orcshaman normal at right
    with dissolve
    "Now the two shamans reached the center of the arena. They began a low chant that seemed ritualistic - a few orcs even chanted along. Sabia shifted uncomfortably in her seat as it went on and on."
    "Other than the chanting, the orcs had quieted down for this. It felt like religious respect, leaving Sabia discomforted. She'd tried to study about the orc front, but had never read about this."
    "If she had started to feel something within her, she would have been horrified. But no... there was no sense of transcendent peace that Sabia had often felt in the Order of Relona. This was just a cultural ritual, not a true religion."
    "Finally, both shamans raised small knives over their heads. Each made a cut on their arm, then raised a fist forward, letting blood dribble down onto the sands."
    "This released the tension, orcs roaring and leaping down into the sands. Some went to speak to the shamans, where Ornshakar was revealing a paper of some kind. Others began eating and drinking, others even began wrestling."
    scene bg RGAbg4
    call sabiabase
    with dissolve
    "It was chaos. Not sure what to do and definitely not wanting to go down there, Sabia remained in her seat. But was she supposed to be doing something now? Surely the arena was going to be more than this."
    show jadkbase at right
    show jadkemo closedhappy at right
    with moveinright
    jadk "Gwahaha, everyone's having fun!"
    s "Is this the actual start? I didn't think it would be like this."
    jadk "This is just the opening ceremony! We need to make sure the Red God is drawn down to observe us."
    s "So they'll use the arena for other things, right? I've heard stories about duels, melees, fighting animals, that sort of thing."
    jadk "That and more, gwahaha!"
    show jadkemo happy2 at right
    jadk "Jadk thinks that you may be too serious for this part. Today, there are no great challenges. But tomorrow, you must be ready."
    show jadkemo normal at right
    jadk "Tomorrow there will be many battles to see who is worthy of fighting before the Red God. All must fight, and many will fail. And there is real dishonor in failing, better not to try."
    s "So not fighting is an option?"
    show jadkemo closedhappy at right
    jadk "Of course! Gwahaha, you think Jadk is going to drag his old bones out there?"
    show jadkemo happy2 at right
    jadk "Especially because for many rounds, only the most basic of equipment is allowed. You can wear what you like for duels, but events are meant to be tests of pure brawn and skill."
    jadk "The shamans are announcing what events will take place over the days of the Red God's Arena. You could go listen... or you could listen to Jadk."
    show sabiaemo happy1 at left
    s "Oh? You know what the events are going to be?"
    show sabiaemo normal at left
    jadk "The details are always secret, but we know the basic form. Every day there will be many duels - you will probably need to fight only every few days."
    jadk "But you will also want to participate in the main events. First is the opening ceremony. Second is the hellhound taming."
    show sabiaemo surprised1 at left
    s "Hellhounds, really? I've been wondering about them..."
    show sabiaemo normal at left
    show jadkemo normal at right
    jadk "There have been problems with the kennels, but Jadk does not know all the details."
    show jadkemo happy2 at right
    jadk "Second, there will be a grand event, something different. Not just beasts, but monsters of some kind. Jadk does not know this secret."
    jadk "Third, for the final day, the elite warriors who have earned the most honor will do battle. This is an important part of the arena."
    s "Do I have any chance of fighting during that part?"
    jadk "You will not be set against the elites, but you may earn a fight. If so, it would be a great honor even to attempt."
    show jadkemo closedhappy at right
    jadk "Anyway, after that, there's only the closing ceremony of the Red God's blessing!"
    show sabiaemo happy1 at left
    s "You seem happy. Have you been to a lot of these?"
    jadk "More than Jadk can remember, gwahaha! But this is the first time in years we're doing it in the real arena and have a lot of tribes coming together!"
    show jadkemo sad at right
    jadk "But truthfully, the Red God's Arena has changed much, even in Jadk's memory. Once, this was a call to war. Now, raiding would be foolish, so it is like a cruel joke."
    show sabiaemo normal at left
    s "But warriors will be restless, right?"
    jadk "Aye."
    show sabiaemo closed2 at left
    s "(Then this will be my chance. If I can earn enough honor here, I can finally take advantage of all this work I've been doing, maybe get enough orcs for me to travel outside the camp.)"
    s "(I just need to survive the arena.)"
    return


label RGAvehlis:
    scene bg sabiatent
    call sabiabase
    "When Sabia woke up, she had barely gotten started on her morning routine when she heard someone outside her tent - someone who didn't seem inclined to wait."
    if orcalliance == "tekrok":
        show tekrok normal at right
        t "Human. Tekrok has a task for you."
        s "Alright, what?"
        t "Vehlis has returned from her travels. Tekrok needs a shipment of weapons delivered, but it is not a Captain's role to handle such matters."
        s "Fine, I'll do it."
        "Tekrok shoved a paper at Sabia, on which had been scrawled a list. Nothing too exceptional, but it was an unusual shipment and many decisions would need to be made about where the metals would be sourced. That explained why he couldn't just deliver it via some orc."
    elif orcalliance == "rokgrid":
        show rokgrid happy2 at right
        r "Hello there, Sabia! So good to see you participating in our customs! I do wish you good luck in the arena!"
        s "Hello, Rokgrid. Since this is the first I've seen of you since the feast, I assume you need something?"
        r "Yes, I fear I must ask your assistance. We Captains are all building up our armaments, and the best source is Vehlis. But due to the demand, it is not a simple matter of simply ordering weapons... I fear there are many details, and I am not so skilled in dealing with human merchants..."
        s "Alright, I get it. Explain what you need and I'll take care of things."
        "Rokgrid showed her some papers that had extensive plans - his statement about being unskilled seemed like it might be false modesty. That, or he wanted to see how well she could do. In any case, details would need to be worked out, but it wouldn't be onerous."
        "Just before he left, Rokgrid tossed her a surprisingly heavy sack of coins."
        $ money += 50
        r "50 Lundils. Payment for services rendered."
        s "Thank you, Rokgrid."
    elif orcalliance == "dajrab":
        show dajrab normalclosed at right
        d "Sabia, I would ask something of you. It will not take much of your preparation time."
        s "I'm listening."
        d "Traditionally, our warriors begin raiding after the Red God's Arena. Actual raiding may be few, but this is still a time for resupply, and to that end, we require a wide variety of supplies from Vehlis."
        s "Oh, is she back?"
        d "Yes, and this first day back would be the best time to negotiate with her. Unfortunately, I am required in the arena and cannot go myself. Can you go in my stead?"
        s "Just give me all the details, then."
        "Dajrab did so, giving them all verbally, without rushing but also without slowing. Sabia felt like she barely kept up memorizing all of them, but could manage. It was no simple order, so she understood why Dajrab didn't want to give the task to a minor subordinate."
        "He nodded to her and left without saying anything else. Well, at least he probably wasn't lying about the task taking up little of her time."
    elif orcalliance == "sabia":
        show jadkbase at right
        show jadkemo happy2 at right
        jadk "Morning, Sabia! You rest well?"
        s "Well enough. Something wrong, Jadk?"
        jadk "Nothing wrong, but... Vehlis is back in camp, and everyone is going to be making purchases from her soon. Old Jadk can't get away from the bar long enough to order what he needs..."
        s "You want me to do it, then? I know Vehlis, I could ask her quick."
        jadk "That'd be right kind of you, gwahaha!"
        "Jadk gave her a rough list of the things his bar needed. Some of the items were ambiguous and would need to be discussed with Vehlis, which explained why he didn't hand it off to a random orc, but Sabia didn't think it would take too long to do the negotiations."
        "After they concluded that, Jadk stuck around a while longer to chat, then left her to her business."
    scene bg mainhall with dissolve
    "Sabia left her tent and headed straight to the main hall. There was no reason not to just get this out of the way quickly, then she could spend the rest of her day on training for the Red God's Arena."
    "The main hall was mostly empty, given how many warriors were focused on the arena. Sabia wandered toward the back rooms where Vehlis usually stayed and knocked on the outer door."
    s "Vehlis? Are you in here?"
    "There was no response. Sabia considered raising her voice more, but didn't want to draw attention and felt like that might irritate Vehlis. So she walked further inside the building, checking for signs of the banker."
    "An open shop ledger suggested that Alioch had been in the foyer, probably fielding orcs who might disturb her, but he seemed to have stepped away for the moment. Just as well, she could go straight to Vehlis."
    "Sabia walked into her innermost room... and froze."
    $ hentai_scene(1,"RGAvehlissex",dissolve)
    "Vehlis lay sprawled on the bed, completely naked and unconcerned about it, idly flipping through a thick book of some kind. She glanced over her shoulder briefly."
    $ hentai_scene(2)
    vehlis "Do you need something?"
    "Determined not to be embarrassed this time, Sabia squared her shoulders and pretended that nothing was unusual."
    s "Alright, we have some business to discuss."
    if orcalliance == "tekrok":
        "Sabia went over Tekrok's order, not trying to negotiate too hard - it wasn't her money, and it was important to establish good relations with Vehlis."
    elif orcalliance == "rokgrid":
        "Sabia went over Rokgrid's order, not trying to negotiate too hard - it wasn't her money, and it was important to establish good relations with Vehlis."
    elif orcalliance == "dajrab":
        "Sabia went over Dajrab's business, not trying to negotiate too hard - it wasn't her money, and it was important to establish good relations with Vehlis."
    elif orcalliance == "sabia":
        "Sabia went over Jadk's business, negotiating enough that the old orc got a decent deal. It was more important to establish good relations with Vehlis, though."
    "Vehlis was shrewd but not too hardnosed, leaving them with a deal that seemed fair. Sabia tucked the concluding papers under her arm for delivery as she left the hall, but didn't leave immediately."
    $ hentai_scene(3)
    vehlis "Is there something else, Sabia?"
    $ hentai_scene(1)
    "Though she had done what she wanted, Sabia found herself distracted by the sight of Vehlis naked like that. She could stay and see where things went, or stick to business..."
    menu:
        "See where things go":
            $ A_vehlis += 1
        "Stick to business":
            "Sabia decided to stay focused and just left, since she had what she wanted."
            return
    if dom >= 10:
        "The sight of Vehlis naked, right next to those toys... it was too good an opportunity to waste. Grinning, Sabia moved forward and picked up one of them."
        if A_vehlis >= 5:
            $ A_vehlis += 2
            $ Sabia.stamina += 25
            if Sabia.stamina >= Sabia.maxstamina:
                $ Sabia.stamina = Sabia.maxstamina
            $ hentai_scene(5)
            "Vehlis glanced back at her with a coy smile."
            vehlis "What's this? Curious about the merchandise, are you?"
            s "What exactly is this thing?"
            $ hentai_scene(6)
            vehlis "Ah, that... I had to bargain hard to get them at a reasonable price, but I'm not sure why the elves wanted to sell them so expensively."
            s "So, it's a strap-on? I guess you can't use it yourself..."
            $ hentai_scene(3)
            vehlis "I put it on, but it didn't feel unusual in any way."
            s "Were you alone? Maybe it needs two people..."
            "Sabia started to wrap the bands around her hips, smiling. Vehlis raised her eyebrow higher, but Sabia didn't back down."
            s "What, is that a problem?"
            $ hentai_scene(7)
            vehlis "I guess not. Let's see what you can do..."
            call RGAvehlissex
            "Feeling much more relaxed than before, Sabia left Vehlis to continue with her work... if she was really working. Either way, Sabia didn't mind."
            play music orccamp fadeout 2.0 fadein 2.0 
        else:
            $ A_vehlis -= 1
            $ hentai_scene(4)
            "Immediately Vehlis looked back at her, gaze piercing."
            vehlis "Do you know what kind of protections the Bank of Talos places on its agents? You should think very carefully about the fact that I'm relaxing like this in the middle of an orc camp."
            s "Oh, come on. I was just going to have a bit of fun."
            vehlis "No, I don't think it would have been fun for you at all. Set that down and get out."
            "Sabia scowled, but decided there was no point in fighting this battle. She wasn't in the mood anymore, anyway."
    else:
        $ A_vehlis += 1
        "Vehlis looked delicious like that... but the thought made Sabia flush and shrink back. No, there was no way she could do such a thing."
        "Sabia left the room in a hurry and thought she might have heard a chuckle from Vehlis as she fled."
    return


label RGAqualificationround:
    if RGAqualsintro == False:
        $ RGAqualsintro = True
        scene bg RGAbg2
        call sabiabase
        with dissolve
        "When Sabia entered the arena, she discovered a surprisingly chaotic mix of orcs. Warriors from different tribes were organizing, some were fighting, a few were already leaving in anger. It seemed this stage was less organized than she'd thought."
        show orcbase at right
        show orcloincloth at right
        show orcemo normal at right
        "An overworked orc stood behind a table, glancing up at her when she approached and grunting."
        orc "We didn't expect this many warriors. Gotta kick out a lot in the first round."
        s "So, how does it actually work?"
        orc "You need to win three fights, then you're in. Lose and you're out."
        s "Well, that's straightforward. So I come here and sign up for three fights?"
        orc "Basically."
        show screen infohud("left")
    scene bg RGAbg2 with dissolve
    play music orccamp fadeout 2.0 fadein 2.0
    $ healthpotions = Inventory.has_item(Healthpotion)
    menu:
        "Sign up for a fight ([RGAqualfights] won)" if (RGAdisqualified == False and RGAqualfights < 3):
            call sabiabase
            "There was no point wasting any more time, Sabia got signed up at one of the tables and soon found herself in a small room at the side of the arena, facing off with an orc."
            if RGAqualfights == 0:
                $ enemy_level = 5
                $ enemy_maxhp = 500
                $ enemy_hp = enemy_maxhp
                $ enemy_type = 1
                $ enemy_skills = [Enemyattack,Enemyattack,Enemyquickattack]
                $ enemy_attack = 65
                $ enemy_defense = 0
                $ enemy_magdefense = 0
                $ GenericOrc1.face = "normal"
                $ GenericOrc1.extras = ["Loincloth", "Axe"]
                $ player = Sabia
                $ enemy = GenericOrc1
                call duel
                if _return == "Victory":
                    $ RGAqualfights += 1
                    scene bg RGAbg2
                    "Victorious, Sabia rolled her shoulders and headed back into the arena. That was one fight down, two to go."
                else:
                    if (sub < 3 or sexworktimes < 3) and money < 50:
                        "She had {i}lost{/i}? Sabia refused to believe that it was over that quickly, her chances at the arena suddenly gone. And yet it was true."
                        "She had too few resources and no viable options. Her journey was over..."
                        show gameover with dissolve
                        pause 3
                        $ renpy.full_restart()
                    $ RGAdisqualified = True
                    if RGAsexbribe == 0:
                        "She had {i}lost{/i}? Sabia refused to believe that it was over that quickly, her chances at the arena suddenly gone. Surely there was something that could still be done..."
                        scene bg RGAbg2
                        call sabiabase
                        show orcbase at right
                        show orcloincloth at right
                        show orcemo normal at right
                        with dissolve
                        "She headed back to the overworked orc managing the fights. He seemed to have been notified that she had been defeated and shook his head."
                        orc "Too bad. You're done."
                        show sabiaemo closed2 at left
                        s "Come on... surely there's something that can be done."
                        orc "Everyone must win three fights. Is rule."
                        show sabiaemo sad2 at left
                        s "Please... I need to get into the Red God's Arena... are you sure we can't talk about this?"
                        "The orc eyed her for a long moment, then grunted."
                        orc "Cannot change rules. But if you must argue, meet me in side room."
                        "He gestured to an obscure door beside the arena, then went back to his work as if nothing had happened. Sabia paused a moment, then smiled. Based on the subtext, she had a chance after all."
                    elif RGAsexbribe == 3:
                        "Sabia was out of options. Her journey was over..."
                        show gameover with dissolve
                        pause 3
                        $ renpy.full_restart()
                    else:
                        "Sabia couldn't believe she had lost again, it was as if she had been taken over by a spirit of incompetence. At least she still had options..."
            elif RGAqualfights == 1:
                $ enemy_level = 6
                $ enemy_maxhp = 500
                $ enemy_hp = enemy_maxhp
                $ enemy_type = 1
                $ enemy_skills = [Enemyattack,Enemyquickattack,Enemyquickattack]
                $ enemy_attack = 65
                $ enemy_defense = 0
                $ enemy_magdefense = 0
                $ GenericOrc2.face = "normal"
                $ GenericOrc2.extras = ["Loincloth", "Strap", "Shoulder", "Axe"]
                $ player = Sabia
                $ enemy = GenericOrc2
                call duel
                if _return == "Victory":
                    $ RGAqualfights += 1
                    scene bg RGAbg2
                    "Victorious, Sabia rolled her shoulders and headed back into the arena. Just one fight left and she was done.."
                else:
                    if (sub < 3 or sexworktimes < 3) and money < 50:
                        "She had {i}lost{/i}? Sabia refused to believe that it was over that quickly, her chances at the arena suddenly gone. And yet it was true."
                        "She had too few resources and no viable options. Her journey was over..."
                        show gameover with dissolve
                        pause 3
                        $ renpy.full_restart()
                    $ RGAdisqualified = True
                    if RGAsexbribe == 0:
                        "She had {i}lost{/i}? Sabia refused to believe that it was over that quickly, her chances at the arena suddenly gone. Surely there was something that could still be done..."
                        scene bg RGAbg2
                        call sabiabase
                        show orcbase at right
                        show orcloincloth at right
                        show orcemo normal at right
                        with dissolve
                        "She headed back to the overworked orc managing the fights. He seemed to have been notified that she had been defeated and shook his head."
                        orc "Too bad. You're done."
                        show sabiaemo closed2 at left
                        s "Come on... surely there's something that can be done."
                        orc "Everyone must win three fights. Is rule."
                        show sabiaemo sad2 at left
                        s "Please... I need to get into the Red God's Arena... are you sure we can't talk about this?"
                        "The orc eyed her for a long moment, then grunted."
                        orc "Cannot change rules. But if you must argue, meet me in side room."
                        "He gestured to an obscure door beside the arena, then went back to his work as if nothing had happened. Sabia paused a moment, then smiled. Based on the subtext, she had a chance after all."
                    elif RGAsexbribe == 3:
                        "Sabia was out of options. Her journey was over..."
                        show gameover with dissolve
                        pause 3
                        $ renpy.full_restart()
                    else:
                        "Sabia couldn't believe she had lost again, it was as if she had been taken over by a spirit of incompetence. At least she still had options..."
            elif RGAqualfights == 2:
                show orcbase at right
                show orcloincloth at right
                show orchelmet at right
                show orcshoulder at right
                show orcaxe at right
                show orcemo normal at right
                with dissolve
                $ enemy_level = 7
                $ enemy_maxhp = 550
                $ enemy_hp = enemy_maxhp
                $ enemy_type = 1
                $ enemy_skills = [Enemyattack,Enemyquickattack]
                $ enemy_attack = 65
                $ enemy_defense = 0
                $ enemy_magdefense = 0
                $ GenericOrc1.face = "normal"
                $ GenericOrc1.extras = ["Loincloth", "Helmet", "Shoulder", "Axe"]
                $ player = Sabia
                $ enemy = GenericOrc1
                call duel
                if _return == "Victory":
                    $ RGAqualfights += 1
                    scene bg RGAbg2
                else:
                    if (sub < 3 or sexworktimes < 3) and money < 50:
                        "She had {i}lost{/i}? Sabia refused to believe that it was over that quickly, her chances at the arena suddenly gone. And yet it was true."
                        "She had too few resources and no viable options. Her journey was over..."
                        show gameover with dissolve
                        pause 3
                        $ renpy.full_restart()
                    $ RGAdisqualified = True
                    if RGAsexbribe == 0:
                        "She had {i}lost{/i}? Sabia refused to believe that it was over that quickly, her chances at the arena suddenly gone. Surely there was something that could still be done..."
                        scene bg RGAbg2
                        call sabiabase
                        show orcbase at right
                        show orcloincloth at right
                        show orcemo normal at right
                        with dissolve
                        "She headed back to the overworked orc managing the fights. He seemed to have been notified that she had been defeated and shook his head."
                        orc "Too bad. You're done."
                        show sabiaemo closed2 at left
                        s "Come on... surely there's something that can be arranged."
                        orc "Everyone must win three fights. Is rule."
                        show sabiaemo sad2 at left
                        s "Please... I need to get into the Red God's Arena... are you sure we can't talk about this?"
                        "The orc eyed her for a long moment, then grunted."
                        orc "Cannot change rules. But if you must argue, meet me in side room."
                        "He gestured to an obscure door beside the arena, then went back to his work as if nothing had happened. Sabia paused a moment, then smiled. Based on the subtext, she had a chance after all."
                    elif RGAsexbribe == 3:
                        "Sabia was out of options. Her journey was over..."
                        show gameover with dissolve
                        pause 3
                        $ renpy.full_restart()
                    else:
                        "Sabia couldn't believe she had lost again, it was as if she had been taken over by a spirit of incompetence. At least she still had options..."
            jump RGAqualificationround
        "Bargain for another chance" if RGAdisqualified == True:
            scene bg RGAint
            call sabiabase
            show orcbase at right
            show orcloincloth at right
            show orcemo normal at right
            with dissolve
            if RGAdisqualintro == False:
                $ RGAdisqualintro = True
                "When there was a quiet moment between matches, Sabia headed to the obscure door and slipped inside. The orc joined her shortly after, but folded his arms and frowned."
                s "Alright, what can we do to turn that loss into a win?"
                orc "Cannot change rules. Is sacred law of Red God."
                show sabiaemo eyebrow1 at left
                s "Come on, I can tell that you don't really believe that. Some orcs might be religious, but you're sure as hell not."
                show sabiaemo closed4 at left
                s "I've seen lots of orcs cheating, and you didn't give a shit. The orc fighting me was fighting dirty anyway, pushing me into the other fights, shouldn't that disqualify the round?"
                show orcemo suspicious at right
                orc "...Warchief Groknak would have my head. Is risk."
                show sabiaemo normalopen at left
                s "I know that, which is why I'm asking what needs to be done in order to compensate you for that risk."
                "Sabia swung her hips to the side, which made her money pouch clink a little. She saw the orc's eyes follow both the pouch and her hips, but he didn't respond immediately."
                orc "..."
                show sabiaemo happy1 at left
                s "Alright, how about this: instead of giving me a win, you just won't record my loss. How does that sound?"
                show orcemo smile3 at right
                orc "Hu... maybe. Is only bending the rules, hard to prove."
                s "I'm glad we could reach an agreement."
                show orcemo smile1 at right
                orc "But what are you offering?"
            else:
                "Knowing that she didn't have many options, Sabia headed to meet the organizer in the secret room. He raised an eyebrow expectantly."
            menu:
                "Bribe him to ignore the loss":
                    orc "Want 50 Lundils."
                    if money >= 50:
                        $ money -= 50
                        $ RGAdisqualified = False
                        $ RGAarenascore -= 1
                        show sabiaemo closed2 at left
                        "Sabia had no choice but to pay, handing over the Lundils. The orc at least slipped her a bit of potion so her next chance meant something, but she resented having to take that step."
                        $ Sabia.hp = Sabia.maxhp
                    else:
                        show sabiaemo angry1 at left
                        s "Shit, I don't have enough..."
                "Flirt with him" if (sub >= 3 and sexworktimes >= 3):
                    $ RGAsexbribe += 1
                    $ RGAdisqualified = False
                    $ Sabia.stamina -= 20
                    $ sub += 1
                    if RGAsexbribe == 1:
                        $ sub += 1
                        $ RGAarenascore -= 1
                        $ L_orcs -= 2
                        show sabiaemo lick2 at left
                        s "Surely there's something I can do for you, to make you forget about this..."
                        show orcemo smile2 at right
                        orc "Oh, me have idea... slut."
                        s "My mouth used to be quite popular in the tents... I give you the best blowjob of your life and you erase the loss. Deal?"
                        show orcemo angry at right
                        orc "No! Fuck or no deal!"
                        show sabiaemo angry1 at left
                        s "Guh... fine."
                        show orcemo smile2 at right
                        orc "Then strip like a good slut!"
                        call RGAdisqualification1
                        "Irritated that things had gone this way, Sabia headed back out to the arena. At least she'd gotten a quick potion so that she was healed for her next chance."
                        $ Sabia.hp = Sabia.maxhp
                    elif RGAsexbribe == 2:
                        $ sub += 1
                        $ RGAarenascore -= 1
                        $ L_orcs -= 2
                        "Sabia stormed into the room in a foul mood, tired and frustrated that she had lost."
                        show orcemo smile2 at right
                        orc "So you're back."
                        show sabiaemo closed2 at left
                        s "Same deal as last time?"
                        show orcemo smile1 at right
                        orc "No. Guard saw you lose, must bribe him too."
                        show sabiaemo angry1 at left
                        s "Guh... are you serious?"
                        show orcemo smile2 at right
                        orc "If he see you fighting again, could report you. Report me. No, must bribe."
                        s "Dammit..."
                        call RGAdisqualification2
                        "Irritated that things had gone this way, Sabia headed back out to the arena. At least she'd gotten a quick potion so that she was healed for her next chance."
                        $ Sabia.hp = Sabia.maxhp
                    elif RGAsexbribe == 3:
                        $ sub += 1
                        $ RGAarenascore -= 1
                        $ L_orcs -= 2
                        show orcemo smile3 at right
                        orc "Huhuhu... you losing on purpose? What went wrong this time?"
                        show sabiaemo angry1 at left
                        s "Cut the crap! ...look, just tell me what I need to do to keep fighting this time."
                        show orcemo smile2 at right
                        orc "Guard was watching you again. Waiting for you to lose."
                        show sabiaemo closed2 at left
                        s "Dammit..."
                        orc "This is getting risky for me. Me have friend, me owe a lot of money... but fucking you worth much money."
                        show sabiaemo closed4 at left
                        s "Well, I don't really have a choice, do I?"
                        call RGAdisqualification3
                        scene bg RGAint
                        call sabiabase
                        show sabiaemo closed2 at left
                        show orcemo angry at right
                        with dissolve
                        orc "This is the last time, slut. Me tired of you, need do job. Win or quit."
                        "Irritated that things had gone this way, Sabia headed back out to the arena. At least she'd gotten a quick potion so that she was healed for her next chance. He'd sounded serious, this really was her last chance."
                        $ Sabia.hp = Sabia.maxhp
            jump RGAqualificationround
        "Investigate area" if RGAqualhealthpotion == False:
            "Investigating the chaos of the qualification matches more carefully, Sabia spotted an orc selling healing potions to tired orcs in between fights. It looked like he had several varieties, at least one of which would work on her."
            "It was a potentially useful asset, since three fights in a row could be quite tiring. There was some kind of limit of one per person, though. Sabia considered her options carefully..."
            menu:
                "Approach now":
                    "When Sabia approached, she found out that the orc merchant indeed had applicable potions, it was just a question of how to get one..."
                    menu:
                        "Pay for potion" if money >= 10:
                            $ RGAqualhealthpotion = True
                            $ Sabia.hp = Sabia.maxhp
                            $ money -= 10
                            "Not wanting to waste time, Sabia paid for the potion and drank it down quickly and headed back to the arena."
                        "Submission: Flirt for potion" if sub >= 5:
                            $ RGAqualhealthpotion = True
                            $ Sabia.hp = Sabia.maxhp
                            "Not wanting to waste money, Sabia flirted with the orc a little until she convinced him to hand over a potion for her. Fully healed, she headed back to the arena."
                        "Domination: Investigate distribution" if dom >= 10:
                            $ RGAqualhealthpotion = True
                            $ L_orcs += 2
                            s "Do you have permission from the Warchief to sell potions here?"
                            orc "Of course! Me get job to distribute potions!"
                            s "Did he say to sell them, though? Seems odd."
                            orc "Uh..."
                            s "And what's this sign about only one per person? If you're a merchant, shouldn't you want to sell as many as possible?"
                            orc "Look, this isn't... me was supposed to distribute, just wanted extra money..."
                            s "Hear that, boys? I think we have a cheat on our hands!"
                            $ Sabia.hp = Sabia.maxhp
                            "The orcs roared irritably and rushed past the scheming merchant to claim their potions. Some took more than one, but Sabia didn't have many to choose from. Besides, the orcs clearly approved of what she'd done, and she got a potion for herself. Sabia quaffing it with satisfaction and headed back to the arena."
                        "Go back":
                            jump RGAqualificationround
                    jump RGAqualificationround
                "Wait until later":
                    jump RGAqualificationround
        "Drink health potion ([healthpotions])" if healthpotions >= 1:
            $ Sabia.hp = Sabia.maxhp
            $ healthpotions -= 1
            $ Inventory.rem_item(Healthpotion)
            "Drank a Health Potion."
            jump RGAqualificationround
        "Finish the qualification round" if RGAqualfights >= 3:
            $ Sabia.stamina -= 50
            "That was three! Sabia felt exhausted, but incredibly satisfied. After confirming that she'd successfully qualified to participate in the rest of the Red God's Arena, Sabia headed back to her tent."
            scene bg sabiatent
            "There, Sabia took a moment to recover and clean herself off. There was nothing else she needed to do for the day, but she could do more if she felt up for it..."
            hide screen infohud
            jump sabiahq2
    return


label RGAhellhoundintro:
    "That morning when Sabia went outside to train, she heard a strange sound. The brutish sounds of the orc camp had become familiar to her, but this was something she'd never heard before. Tracking the source, Sabia wandered toward the kennels."
    scene bg kennels
    call sabiabase
    with dissolve
    "The hellhound kennels had been locked up tight since she'd arrived, and Sabia had almost wondered if something was wrong. She'd heard sounds of the warbeasts inside, but there had been few enough that she'd been left curious."
    "None of that was true now."
    "As she approached, she could hear growls, snarls, and roars. Some of them were from orcs, along with the occasional sound of pain that she wasn't sure was orc or animal. More orcs were milling around, and they didn't stop her when she entered."
    "Inside, she found the kennels filled with hellhounds. They struck out at their cages as if they weren't used to captivity... and Sabia realized that they might actually be untamed. The orcs seemed to be sizing them up, and Sabia could only guess that this had to do with the Red God's Arena."
    "Not certain how to proceed, Sabia looked around until she spotted someone worth talking to."
    show lutvrogbase at right
    show lutvrogwraps at right
    show lutvrogwrists at right
    show lutvrogemo normal at right
    with dissolve
    show sabiaemo happy1 at left
    s "What exactly is going on here, Lutvrog?"
    lut "One of the most ancient parts of the Red God's trials. All warriors must prove their worth against the hounds."
    show sabiaemo normal at left
    s "Are these beasts wild? They certainly seem... angry."
    "As if to punctuate her point, the hellhound in the cage nearest them roared and slammed against the bars, which almost seemed to shake. Lutvrog didn't so much as glance toward it, and Sabia managed to hold back her instinctive flinch."
    lut "Yes, these hounds have never known commands."
    s "What exactly does it mean to \"prove your worth\" against them?"
    lut "In ancient times, it is said that warriors fought until they chose their mount. Today, we ride only trained hounds - but it is still important to be able to face one."
    show sabiaemo surprised1 at left
    s "In combat? Because I might be able to kill one with my old equipment, but now..."
    lut "No. You cannot bring any permanent harm to the hound. The goal is to make them acknowledge you - they will drop low to the ground and flatten their wings."
    lut "Many accomplish this by force, though it is more honorable if the hound chooses to do so. Finally, merely surviving until the end of the time is better than failure."
    show sabiaemo normal at left
    "Even that sounded incredibly dangerous, but at least not impossible. Sabia took a deep breath and started looking over all the hellhounds more carefully."
    s "So, the warriors are all choosing which one they'll face? Should I be picking one too?"
    lut "Yes. You would lose respect if you did not participate."
    lut "The confident attempt to choose the largest hounds. Weaker warriors will choose weaker hounds, or pick popular hounds and hope they have grown exhausted by the time it is their turn."
    s "What about you? You already picked one out?"
    lut "Lutvrog has not taken the path of bonding to hounds. But Lutvrog will defeat one in the Red God's Arena for the sake of honor."
    s "Good luck... but I think I need it more in this case."
    hide lutvrogbase at right
    hide lutvrogwraps at right
    hide lutvrogwrists at right
    hide lutvrogemo normal at right
    with moveoutright
    "Lutvrog nodded and moved away, observing the cages carefully. Sabia suspected that he was monitoring for any that might break free, but she didn't have time to look at him. She needed to figure out what she was going to do."
    "It was a small comfort that many of the orcs didn't seem confident either. Oh, they were filled with bravado, but she could see their hesitation. Hellhounds were extremely dangerous beasts, so some would no doubt die in this event."
    "Sabia didn't intend to be one of them, she needed to pass. But how was she going to survive against something that much larger than her?"
    "Lutvrog had told her about strategies the orcs used, and as she looked around, Sabia saw many of them in use. Some orcs went for the largest, but others seemed to be searching for those that were smaller or weakened."
    "As she watched, Sabia even saw an orc strike one of the hellhounds with his club through the bars. Surely that was cheating... but no one seemed to object. If that kind of manipulation was allowed, then she probably had more options."
    "That didn't mean it was going to be easy. The room was filled with snarling monsters, like something out of a nightmare. Beasts like this had terrorized villages, both in the wild and as the mounts of orcs. How the hell was she supposed to choose?"
    "At that moment, one of the hellhounds caught her eye. It was larger than average, yet wasn't getting any attention because it was much quieter than the others. Sabia found herself wandering closer."
    "Was there something different about this one? It did seem calm... but though it sat back, the pose was of a wolf, not a trained dog. Surprisingly, its eyes tracked her as she approached. There was a glimmer of something there."
    "Taking a deep breath, Sabia extended her hand and touched the bars. The hellhound sat motionless, just watching her."
    "She extended her hand between the bars, arm trembling with the tension, slowly reaching toward the beast's head."
    "Without so much as a growl, the hellhound lunged forward, vicious jaws slamming down on where her arm had been an instant ago."
    "Sabia wrung her hand from where it had struck the cage, watching the hellhound. She hadn't been so stupid as to actually trust it, but this proved her theory: this one was smarter than the others. It didn't waste strength hitting the cage, it tried to take her entire arm."
    "Though Sabia had never been particularly interested in dogs, her father had instructed her a little in their keeping. That family tradition had been abandoned thanks to her mother, but the memories came back to her now."
    "Did any of them apply to this situation? This was a monster, not a domesticated animal. Yet as the hellhound sat back and watched her, Sabia was certain that it wasn't just a stupid beast. The question was whether that was a liability for her."
    show sabiaemo closed2 at left
    "Sabia took a deep breath and considered her options..."
    menu:
        "Choose an easier hellhound":
            $ hellhoundchoice = "easy"
            show sabiaemo normal at left
            "After watching the hellhound stare at her suspiciously, Sabia decided that it wasn't worth it. Instead she observed the orcs to see which ones they gravitated towards."
            "Choosing a popular beast and hoping that it would get worn out was too much randomness for her, so Sabia tried to pick one that she thought she could outlast regardless, but still had plenty of other warriors interested."
            "Finishing the challenge that way might not earn her any honor, but she wouldn't risk serious injury. Plus, she had the rest of the day to prepare for the other challenges."
            "It looked like there was a fairly straightforward process to pick your hellhound, just announcing it to an orc standing near the entrance and keeping lists. He looked a little surprised, but wrote down Sabia's name without objecting."
            "Sabia left the kennels focusing on her other objectives."
        "Find a way to drug the hellhound":
            $ hellhoundchoice = "drug"
            $ dom += 1
            $ sub += 1
            show sabiaemo normal at left
            "Since it was obvious that no one else was going to play fair, Sabia decided that she shouldn't either. Except she was sure that she could do better than just hitting the hellhound she intended to face."
            "No, better to give it some kind of drug to make it slower and more pliable. Sabia had a few simple ideas that worked on domestic animals, but there was nothing that she could do for now, not with so many orcs here."
            "It looked like there was a fairly straightforward process to pick your hellhound, just announcing it to an orc standing near the entrance and keeping lists. He looked a little surprised, but wrote down Sabia's name without objecting."
            "Sabia left the kennels planning to return that night. Until then, she had other work to do."
        "Submission: Find a way to pacify the hellhound" if (sub >= 2 and sexworktimes >= 3):
            $ sub += 1
            $ hellhoundchoice = "sub"
            show sabiaemo normal at left
            "Since hellhounds could be domesticated, Sabia figured that they must be similar to dogs or wolves in some ways. It was watching her... trying to decide if she was a threat, prey, or something else."
            "Sabia opted for \"something else.\""
            "Though the hellhound seemed angry to be imprisoned like this, it didn't seem filled with hatred. It just watched her with animal curiosity, perhaps able to see that she was different than all the orcs around them. Could she use that?"
            "Not with the hall flooded with noisy warriors. But if she returned when things were quieter, she'd see if she couldn't make better progress."
            "It looked like there was a fairly straightforward process to pick your hellhound, just announcing it to an orc standing near the entrance and keeping lists. He looked a little surprised, but wrote down Sabia's name without objecting."
            "Sabia left the kennels planning to return that night. Until then, she had other work to do."
        "Domination: Intimidate the hellhound" if dom >= 10:
            $ dom += 2
            $ hellhoundchoice = "dom"
            show sabiaemo normal at left
            "Since hellhounds could be domesticated, Sabia figured that they must be similar to dogs or wolves in some ways. It was watching her... trying to decide if she was a threat, prey, or something else."
            "Sabia opted for \"something else.\""
            "The hellhound wouldn't be baited so easily again, just growling at her hand when it neared the bars. Sabia glowered back, refusing to back down."
            "Lower in the cell there were a few cracked bones, teeth marks visible from obvious gnawing. Normally Sabia would want to stay as tall as possible, but she bent down, extending her hand as if to take one of the bones."
            "Just as she extended, the hellhound lunged forward again. It would have caught her arm if she hadn't been planning just that. Sabia yanked it back, but simultaneously lunged against the bars, her right hand reaching out and grasping one of the hellhound's wings."
            "It pulled back on instinct, and though the leathery wing hurt her hand, Sabia held on. The hellhound let out a yelp of pain and flinched, but it was going to twist and bite at her soon."
            "Before it could do so, Sabia pulled as hard as she could, tugging the wing through the bars. Seeking to relieve pressure, the hellhound fell forward with her, which put it in a compromised position where it couldn't use its full strength. Even so, its paws scratching at the ground nearly threw her back."
            "Sabia kept a firm hold and glared down at the hellhound. When it growled, she twisted its wing, producing a soft whimper."
            s "No. Do you understand?"
            "Sabia bent closer, so near those monstrous jaws, and tried to suppress anything but pure dominance. After a moment staring at her, the hellhound huddled down further."
            "Her hand was aching, so Sabia let go of the wing. Immediately the hellhound pulled back as far as it could, sitting back in a small ball on the other end of the cell and staring at her."
            "When Sabia reached down to grasp the bone again, it gave a soft growl but didn't move. Sabia picked it up... but then tossed it to the hellhound so it clattered in front of its nose. The hellhound just stared at her."
            "Had that been enough? Facing it in the arena would be a very different experience, of course. Sabia watched it a while longer, then walked away. It didn't seem like anyone had paid her too much attention, not compared to all the other, noisier dogs."
            "For now, that was enough. Sabia would just have to prepare to face the hellhound tomorrow by the usual methods."
            "It looked like there was a fairly straightforward process to pick your hellhound, just announcing it to an orc standing near the entrance and keeping lists. He looked a little surprised, but wrote down Sabia's name without objecting."
            "Sabia left the kennels focusing on her other objectives."
    return


label RGAhellhounddrug:
    "That night, Sabia set about gathering what she needed for the hellhound. She gathered some raw meat and booze, which were still plentiful in the camp after the Horned God's Night. With an animal this large, the alcohol should just act as a sedative. And if it was like a wolf, the more it had eaten, the calmer it would be the next day."
    "Once she was done, she sneaked out to the hellhound kennels with some meat in tow. She had been concerned that they might be heavily guarded or more orcs might be milling around, but most were gone. It was simple enough to evade those few on guard to get inside."
    "Why so light a guard? Were the orcs too stupid to try something like this? Or was it so dishonorable that they wouldn't try? Sabia set the question aside and crouched by the back door, listening."
    "She'd been concerned that her arrival might set off the whole group, but they growled and howled at each other plenty already. When Sabia slipped inside, a few whined for the meat she was carrying, but they weren't too loud."
    "The hellhound she had targeted sat calmly in its cage, watching her. It seemed to recognize her, then cocked its head to the side in a very doggish movement."
    "Smiling despite herself, Sabia drew closer to the bars. Since it seemed calm, she didn't want to taunt it again. Instead, she began by throwing the first piece of meat into the cell near the edge."
    "The hellhound stared at it, and at her, as if suspecting some trick. But when nothing happened, it prowled forward, sniffed the meat, and then wolfed it down in a few bites. It really was gruesome to see the thing eat, she didn't want to imagine what those jaws would do to a body..."
    "That was irrelevant to her goal, though. The hellhound was now watching her eagerly, hoping for more food. Instead, Sabia raised her hand some distance away from the bars."
    "After looking at her cautiously, the hellhound stuck its nose through the bars, but like she had hoped it couldn't reach her hand. But it was close enough to snuffle at her, taking in her scent."
    s "That's right... I'm not here to hurt you..."
    "When she spoke, the hellhound pulled back slightly and cocked its head strangely. Was it really so surprised to hear her voice? Then again, she probably sounded very different than the rough orcs that had surrounded it before now."
    "Actually, she realized that it was probably a mistake that she hadn't spoken before now. Some animals could understand your intent, she should have remembered that. So as Sabia stretched her hand in, she kept talking."
    s "Good, uh, hellhound... let's not bite, just listen to my voice..."
    "To her surprise, the hellhound let her touch its head. The red fur was thicker than she expected, rough on the exterior but softer underneath."
    "When the hellhound twitched Sabia almost screamed, because her hand was too close to pull back in time. But it was just shifting its head to make her scratch a place near the edges of the bony plate on its head. When Sabia complied, it gave a low, happy growl."
    s "Good hellhound... I'm not like them... so don't try to eat me, okay?"
    "She tossed the next piece of meat into the cell just behind the bars and the hellhound quickly gobbled it up as well while she kept scratching its head. This was easier than she had expected - these hellhounds must be more like wild dogs than true wolves."
    "The third piece of meat, the hellhound actually snapped up in the air before it hit the ground. She pulled back in surprise and it gave a triumphant bark, then nosed her hand insistently, wanting more."
    "So Sabia spent a large part of the night feeding the hellhound while petting it and speaking in soft tones. By the time she ran out of meat, the hellhound seemed sleepy and calm. It gave a loud yawn that showed off its terrifying teeth, but followed by licking her hand and then curling up to sleep."
    "Sabia got to her feet and looked down at it, satisfied with herself. Part of her was surprised she had done something this dangerous, but another part thought it was only reasonable. If a bunch of orcs could domesticate hellhounds, it made sense that it wasn't beyond her, either."
    "Of course, she was going to be facing the hellhound in the arena tomorrow. She'd have to hope that the progress she'd made had been enough."
    return


label RGAhellhoundhandjob:
    "That night, Sabia sneaked out to the hellhound kennels with some meat in tow. She had been concerned that they might be heavily guarded or more orcs might be milling around, but most were gone. It was simple enough to evade those few on guard to get inside."
    "Why so light a guard? Were the orcs too stupid to try something like this? Or was it so dishonorable that they wouldn't try? Sabia set the question aside and crouched by the back door, listening."
    "She'd been concerned that her arrival might set off the whole group, but they growled and howled at each other plenty already. When Sabia slipped inside, a few growled at her, but most ignored her."
    "Not her target. The hellhound she had targeted sat calmly in its cage, watching her. It seemed to recognize her, then cocked its head to the side in a very doggish movement."
    "Smiling despite herself, Sabia drew closer to the bars. Since it seemed calm, she didn't want to taunt it again. Instead, she began by throwing the piece of meat into the cell near the edge."
    "The hellhound stared at it, and at her, as if suspecting some trick. But when nothing happened, it prowled forward, sniffed the meat, and then wolfed it down in a few bites. It really was gruesome to see the thing eat, she didn't want to imagine what those jaws would do to a body..."
    "That was irrelevant to her goal, though. The hellhound was now watching her eagerly, hoping for more food. Instead, Sabia raised her hand some distance away from the bars."
    "After looking at her cautiously, the hellhound stuck its nose through the bars, but like she had hoped it couldn't reach her hand. But it was close enough to snuffle at her, taking in her scent."
    s "That's right... I'm not here to hurt you..."
    "When she spoke, the hellhound pulled back slightly and cocked its head strangely. Was it really so surprised to hear her voice? Then again, she probably sounded very different than the rough orcs that had surrounded it before now."
    "Actually, she realized that it was probably a mistake that she hadn't spoken before now. Some animals could understand your intent, she should have remembered that. So as Sabia stretched her hand in, she kept talking."
    s "Good, uh, hellhound... let's not bite, just listen to my voice..."
    "To her surprise, the hellhound let her touch its head. The red fur was thicker than she expected, rough on the exterior but softer underneath."
    "When the hellhound twitched Sabia almost screamed, because her hand was too close to pull back in time. But it was just shifting its head to make her scratch a place near the edges of the bony plate on its head. When Sabia complied, it gave a low, happy growl."
    s "Good hellhound... I'm not like them... so don't try to eat me, okay?"
    "As she spoke, though, Sabia wondered where exactly she could go from here. Maybe it would be possible to slowly gain a hellhound's trust... but not when it was being held by brutal orcs and she needed to have a fight with it literally tomorrow."
    "None of the cells were properly locked... Sabia took a deep breath, hoping she wasn't being suicidal. She kept scratching the hellhound's head while she undid the latch, just a little, then slipped inside."
    "Almost immediately she regretted it - the lack of bars between them reminded her just how huge the hellhound was. It looked at her strangely, then pushed its head forward harder, urging her to keep petting it."
    "All of this had gone rather easily... at that moment, Sabia looked down and saw that the animal's cock had emerged from its sheath, throbbing bright red."
    "She scowled in revulsion, wondering if that was just the beast's nature or if it was somehow focused on her. The hellhound gave an insistent whine and pushed forward, flattening her against the side of the cell and demanding more from her hand. Yet its hips were wiggling back and forth slightly..."
    if sub >= 5:
        "Though Sabia's mind told her that she could have gone back to her other plan, fed the hellhound sedatives, she found that her body didn't cooperate. When the hellhound pulled back, Sabia dropped to the ground beneath it."
        call hellhoundsabiaA
        play music orccamp fadeout 2.0 fadein 2.0
        "As she got out of the cell, for a moment Sabia had been terrified that someone would have approached while she was distracted. But no, the kennels were no different than before. She was filthy, though."
        "Sabia quickly cleaned herself off, the thick spunk giving her surprising trouble, then headed out to get some sleep. This had better pay off tomorrow."
    else:
        menu:
            "Change to the sedative plan":
                $ hellhoundchoice = "drug"
                $ dom += 1
                "Shaking herself, Sabia decided that staying in the cell was too dangerous. She needed to switch to a better plan."
                "After scratching the hellhound's head vigorously, she pulled back out of the cell quickly and latched it again. The door didn't give space for the hellhound to get out, but she was grateful that it didn't try."
                "Sabia left and gathered some raw meat and booze, which were still plentiful in the camp after the Horned God's Night. With an animal this large, the alcohol should just act as a sedative. And if it was like a wolf, the more it had eaten, the calmer it would be the next day."
                "So Sabia fed the hellhound plenty, petting it and speaking in soft tones. This was easier than she had expected - these hellhounds must be more like wild dogs than true wolves."
                "By the time she ran out of meat, the hellhound seemed sleepy and calm. It gave a loud yawn that showed off its terrifying teeth, but followed by licking her hand and then curling up to sleep."
                "That was all very well... except she had spent the entire time trying not to look at the creature's throbbing cock. Sabia tried to forget about it as she left the kennels, hoping this would be enough to slow down the hellhound the next day."
            "Submission: Give the hellhound some relief":
                $ sub += 1
                "Though part of Sabia's mind told her that she could have gone back to her other plan, fed the hellhound sedatives, in the end she chose to slide to the ground beneath the hellhound. Running away now might trigger a hunting instinct in it, after all."
                "When she found herself beneath the hellhound, Sabia had a final moment of hesitation, wondering if she was really going to do this. Yet if she had come this far..."
                call hellhoundsabiaA
                play music orccamp fadeout 2.0 fadein 2.0
                "As she got out of the cell, for a moment Sabia had been terrified that someone would have approached while she was distracted. But no, the kennels were no different than before. She was filthy, though."
                "Sabia quickly cleaned herself off, the thick spunk giving her surprising trouble, then headed out to get some sleep. This had better pay off tomorrow."
    return


label RGAhellhoundmatch:
    scene bg RGAhellhound1 with dissolve
    "The hellhound challenge began on a good note, a powerful warrior taking on a huge beast. They darted back and forth, roaring in dominance, before the hellhound finally leapt. The orc was prepared for this, using the hellhound's momentum against it to throw it to the ground."
    "Immediately he leapt over the beast's neck to pin it to the ground. Though it was too large for him to do properly, his grip around its neck didn't waver even as he was thrown from side to side."
    "Eventually the hellhound lowered its head, flattened its wings, and whined, prompting a huge roar of approval from the crowd. A good start."
    scene bg RGAhellhound2 with dissolve
    "The second orc tried to do something similar, but was knocked off his feet and mauled nearly to death before the guards could catch the hellhound with nets and drag it back. This also got a huge roar of approval from the crowd."
    scene bg RGAbg4 with dissolve
    "Fortunately, the random lots didn't require Sabia to go soon, so she had plenty of time to watch the others fight. Some just fled or did their best to survive until the gong rang, others brought blunt weapons. Sabia wasn't sure exactly how the crowd's approval varied, other than that they seemed to view success in stupid strategies favorably."
    if hellhoundchoice == "easy":
        "Of course, she wasn't going to use the same strategies - that would be suicide given how much smaller she was than the orcs. But watching, Sabia was able to learn a lot about how the hellhounds behaved."
        "Sabia spotted the intelligent-looking hellhound in a previous match, where it tore out the throat of the orc attacking it. Yes, she'd made the right choice not choosing that one."
    elif hellhoundchoice == "drug":
        "Of course, she wasn't going to use the same strategies - that would be suicide given how much smaller she was than the orcs. Hopefully her sedated hound would make things easier for her."
        "She actually had a moment of panic when another orc went out against her chosen hellhound, but fortunately no one seemed to notice. The beast did seem more sluggish than normal, and Sabia felt more confident about her upcoming match."
    elif hellhoundchoice == "dom":
        "Of course, she wasn't going to use the same strategies - that would be suicide given how much smaller she was than the orcs. Hopefully she had put enough of an impression on the beast that she would have an edge."
        "Her hellhound certainly didn't seem cowed when it tore out the throat of the first orc that it went up against. Sabia folded her arms and scowled, watching as it was recaptured and planning her own match."
    else:
        "Of course, she wasn't going to use the same strategies - that would be suicide given how much smaller she was than the orcs. But she'd already used a very different tactic the previous night... she had to hope that would make it view her more favorably."
        "Her hellhound certainly didn't seem pliable when it tore out the throat of the first orc that it went up against. Sabia took a deep breath and hoped that she hadn't made a mistake."
    "About half-way through the event, Sabia's tile was finally drawn. She swallowed, but got to her feet just as attention turned toward her. Judging from the looks she received, many hadn't expected her to take part in this hellhound challenge."
    "Sabia headed down to the sands of the arena, hoping that all would go well. Ornshakar glowered at her and for a moment she feared that there would be some underhanded attempt, or that she would be set against a different hellhound than the one she had chosen."
    if hellhoundchoice == "easy":
        scene bg RGAhellhound3 with dissolve
        "But no, it was the hellhound she'd picked out before, looking suitably exhausted from the previous fights."
        "Despite that, as soon as it was released from its bonds, it snarled and lunged at the orcs that had held it. They warded it back with long poles, but it took a few blows before it turned on Sabia."
        "It was weakened, disoriented, and slow... but it was still terrifying when the hellhound barreled down on her."
        "Only Sabia's discipline as a soldier allowed her to push down the animal fear and dodge out of the way instead of bolt. The hellhound plunged into the sand where she had been standing moments ago, sending it scattering in all directions."
        "The beast scrabbled for a moment, trying to get its footing but obviously not at its best. Seeing it struggle like that brought Sabia to her senses. All her preparations had been worth it: this was something she could do. She set about her plan."
        if Sabia.level >= 5:
            $ RGAarenascore += 2
            $ Sabia.hp -= 5
            $ Sabia.stamina -= 50
            $ Sabia.xp += 2
            $ L_orcs += 1
            "It was an exhausting fight, but in the end Sabia managed to twist the hellhound's fragile wings and pin it down. That wasn't a very orcish way of doing things, but based on the audience's reaction, Sabia didn't think she'd embarrassed herself."
        elif Sabia.level == 4:
            $ RGAarenascore += 1
            $ Sabia.hp -= 10
            $ Sabia.stamina -= 100
            $ Sabia.xp += 1
            $ L_orcs += 1
            "It was just as difficult as Sabia had expected, but eventually Sabia managed to twist the hellhound's fragile wings and pin it down. Though she nursed a scratch on her side and felt exhausted, based on the audience's reaction, Sabia didn't think she'd embarrassed herself."
        else:
            $ RGAarenascore += 1
            $ Sabia.hp -= 15
            $ Sabia.stamina -= 150
            $ Sabia.xp += 1
            $ L_orcs += 0
            "It was more difficult than Sabia had expected, barely making it through the allotted time. Though she nursed a nasty scratch on her side and felt exhausted, based on the audience's reaction, Sabia didn't think she'd embarrassed herself."
        "Having expected a more significant confrontation, Sabia found herself wondering if she should have chosen differently. But she couldn't know what might have happened, and she was just glad to have made it through the event."
        "Sabia raised her fist in triumph to acknowledge the crowds, then headed out. It looked confident, but actually she was just exhausted."
        "When she got back to her tent, Sabia finally let herself drop. She was too tired to think about anything, and fortunately sleep claimed her almost immediately."
        return
    else:
        scene bg RGAhellhound4 with dissolve
        "But no, it was the sharp-eyed hellhound she'd picked out before."
    if hellhoundchoice == "drug":
        "The beast was showing signs of sluggishness and wobbled slightly as it was released. But when it saw her, to her surprise it seemed to perk up."
    elif hellhoundchoice == "dom":
        "The beast burst away from its handlers, snarling wildly. When it saw her, to Sabia's surprise it stopped, back rising as if to inflate itself. Had she gone too far?"
    else:
        "The beast snapped at the orcs around it, but suddenly seemed to smell something. When it saw her, it ignored the orcs entirely, ears perking up."
        "For a moment Sabia worried the hellhound would attempt to pick up where they had left off, but it rushed at her with a roar."
    "Sabia felt a surge of raw animal fear at the sight of the hellhound barreling toward her. Only the discipline drilled into her as a soldier allowed her to overcome it and move aside."
    "The hellhound turned swiftly, eyes burning, muscles bulging, tongue hanging. It took a slight lunge toward her but stopped short. Sabia had been prepared to dodge and aim for its wings, but hadn't expected this abortive attack."
    "She pushed aside her confusion and stayed focused, but the hellhound was lunging and retreating, hopping from side to side as it roared. Some kind of trick? She'd never heard of hellhounds fighting this way, but..."
    "No. Abruptly Sabia realized what was happening."
    "The hellhound was {i}playing{/i} with her. Though it was a vicious monster that far outweighed her, the movements were familiar. It was the false attacking and taunting of many domestic hounds."
    "Of course, it was still a fucking hellhound. When it lunged toward her and swiped playfully, there was a very real chance that it would eviscerate her. Sabia dodged backward, then gave a lunging growl of her own. The hellhound responded by dancing back and then roaring again."
    if hellhoundchoice == "drug":
        "Yes, its movements were sluggish, but not nearly as much as Sabia had expected given how much sedative she'd fed the hellhound. On one hand, that meant the battle looked completely authentic. On the other hand, she was in real danger."
        "And where the hell had this playfulness come from? Was the fact that she had fed it so much more important than the sedative itself? That idea irritated Sabia, but she forced herself to stay focused."
    elif hellhoundchoice == "dom":
        "Though it was playing, it was playing aggressively. Sabia didn't see any hatred from how she had treated it... instead, it seemed to view her as a rival to be defeated. At least, that was what she hoped she saw in its eyes."
        "The hellhound lunged forward, jaws snapping near her face. Sabia lashed out with her sword, striking the flat against the beast's face. Though she didn't have enough strength to really harm it, the beast dropped back."
        "Opening its jaws, it gave an eager roar and made another playful lunge. This time when she dodged, it was more to meet its challenge than for her life. The hellhound wasn't willing to accept her so easily, but she'd had an effect."
    else:
        "When the hellhound rushed her, Sabia's mind wandered to what had happened the previous night for just a moment. That was long enough that the hellhound nearly hit her, knocking her off her feet. It tried to dive on top of her, but Sabia rolled away and managed to get to her feet with some distance between them."
        "It was jumping about even more playfully now. She doubted that it would kill her... but wondered if it might try to do something to her here in front of everyone. That was one outcome she definitely had to avoid."
        "At least its playing was still aggressive, and the crowd probably thought it was trying to drop her in order to get a killing blow. So long as Sabia stayed on her toes, she could get through the challenge successfully."
    "The next time the hellhound rushed at her and then pulled back, Sabia followed and struck it with the flat of her blade. Off-balance, the hellhound slipped backward, almost as if she'd knocked it back. That drew gasps from the audience."
    "The hellhound looked surprised too, as if it hadn't known that was allowed. It released a loud bark, then leapt at her."
    "Though Sabia had been prepared to retreat, her heel slipped on some of the sand and she lost her footing. Instead of dodging cleanly, she ended up slammed onto her back."
    "A moment later, the hellhound loomed over her, biting down. Only the fact that she had predicted it let her duck out of the way of the huge jaws, but that left her in a compromised position."
    if hellhoundchoice == "drug":
        "The hellhound released another bark she interpreted as happy, now threatening to slobber over her face. It seemed to have calmed down now, excitement finally wearing down and letting the sedative work. That meant that the fight might stop looking realistic soon."
        "Sabia dodged around a half-hearted swipe at her head, then scrambled to the side and leapt onto the hellhound's back. She'd intended to grab its wings for dear life, but to her surprise the hellhound gave a lazy roar and then dropped to the ground heavily."
        "She had planned to pretend to twist its wings, but the hellhound had already dropped them into flattened position. She could only hope the fight had looked realistic enough that no one suspected that she had cheated."
        "Soon the gong rang, declaring her match over in any case. Sabia tried to move away quickly, only barely avoiding the hellhound licking her face before the handler orcs prodded it back to its cage."
    elif hellhoundchoice == "dom":
        "Fortunately, she'd kept her sword in her hands even as she fell. Sabia nearly stabbed the hellhound in the stomach, only reining in her instinct at the last second. The wound would just enrage it, and the hellhound was more useful to her alive."
        "Her delay meant that it had a chance to swipe at her, nearly crushing her chest with an enormous paw. It didn't try to use its claw, but it definitely wanted to pin her down and prove itself superior."
        "She couldn't let that happen. Sabia reversed her blade and jabbed upward, hitting the hellhound with the pommel directly in the throat."
        "The blow would have been fatal normally, but the hellhound's thickly muscled body repelled it. But even the beast couldn't just ignore a blow like that, falling backward and giving her time to scramble up."
        "Sabia dodged aside of its lunging charge and grabbed hold of the beast's wing. The hellhound's own momentum made its wing jerk painfully, and though her fingernails felt like they might tear off, the hellhound howled as well."
        "To her surprise, she didn't need to twist. The hellhound dropped low, flattening its wings in subservient position, staring up at her and no longer trying to attack. Sabia stared a moment, then let go of its wing."
        "Her body ached, but she didn't dare show the slightest weakness. If it had finally acknowledged her as dominant, she needed to make sure it stuck."
    else:
        "Beneath the hellhound's body, Sabia moved on instinct to avoid its paws, but her focus wavered. She could see that the hellhound's cock was engorged and throbbing."
        "Would it really mount her here in the arena if it could? Though right now it seemed more playful than anything, it was very easy to imagine..."
        "Sabia shook herself, dispelling the thought. Fortunately, the hellhound seemed distracted as well, more interested in pinning her to the ground than in actually striking her."
        "The next time it tried to bite at her, Sabia lunged toward the hellhound's back legs and grabbed its cock. She had planned to twist, yet when the throbbing girth filled her hand, she found herself hesitating."
        "To her surprise, the hellhound let out a howl and dropped onto its side. It stared at her, hoping that she would jerk it off again, and Sabia felt her cheeks flush with shame."
        "Yet as she heard the crowds, Sabia realized that to them, it had looked like she'd disabled the creature by hitting it in the cock. Apparently the orcs could respect that."
    "The crowds were still cheering, but Sabia barely heard them. She watched the hellhound as it was herded away, wondering just what that had been."
    "She had thought that one had potential, but only as a target for one round of the Red God's Arena. Yet sparring with it had been exhilarating, and it kept trying to look back at her... no, she couldn't think about this now."
    "Sabia raised her fist in triumph to acknowledge the crowds, then headed out. It looked confident, but actually she was just exhausted."
    if Sabia.level >= 5:
        $ RGAarenascore += 3
        $ Sabia.hp -= 0
        $ Sabia.stamina -= 25
        $ Sabia.xp += 3
        $ L_orcs += 3
        "Though she wasn't sure how she'd have fared in a real fight, Sabia thought she'd done a good job of faking it. Plenty of orcs had shown weaker matches, so this one should bring her some respect."
    elif Sabia.level == 4:
        $ RGAarenascore += 2
        $ Sabia.hp -= 5
        $ Sabia.stamina -= 50
        $ Sabia.xp += 2
        $ L_orcs += 2
        "Though it wasn't as good as a real match, Sabia thought her faked match wasn't bad. No doubt a few wondered if it was going easy on her, but she'd been able to put some effort into making it look real."
    else:
        $ RGAarenascore += 1
        $ Sabia.hp -= 10
        $ Sabia.stamina -= 75
        $ Sabia.xp += 1
        $ L_orcs += 1
        "Though the match had probably looked suspicious, Sabia hadn't been able to make it look any more realistic without endangering herself. Other orcs had cheated, so it would have to be enough that she'd performed well."
    "When she got back to her tent, Sabia finally let herself drop. She was too tired to think about anything, and fortunately sleep claimed her almost immediately."
    return


label RGAgeneralmelee:
    $ RGAgeneralmeleeparticipated = True
    $ RGAarenascore += 2
    $ Sabia.xp += 3
    scene bg RGAmelee1 with dissolve
    "It had been a long time since Sabia had fought in a large mass - honestly, considering that she'd usually been commanding well-disciplined troops, it was far longer than she wanted to admit. The thick of battles had always struck her as so chaotic, strength and skill mattered less than dumb luck."
    "She made herself put aside such doubts as she walked down onto the sands with many other warriors. This wouldn't be as lethal as a real battlefield. Though it was expected that some might die, they were using blunted weapons."
    "That didn't mean she was comfortable to be standing in the midst of so many orcs. It brought to mind the moment she had been captured, which she preferred to forget. Of course, things were different now. The orcs weren't focused on her, instead watching Ylva and Ornshakar as they began the event with an official ritual."
    "It was obvious that wasn't the heart of it, though. Everyone was here for the chaos of the fight."
    show screen infohud("left")
    "When the gong was rung, Sabia drew her sword along with everyone else. The combined sound was ominous, but not as ominous as everyone in the arena beginning to turn on one another."
    "Sabia quickly backpedaled to get her back to a wall. Orcs might prize foolishly wading into the battle, but she needed to fight smart if she was going to make it. Anyone who was still standing when the gong rang again would gain honor, so that was her goal more than taking down endless opponents."
    "Of course, she was going to need to do that as well. Several orcs began moving toward her, not attacking each other. So they planned to eliminate her right away, perhaps because they hated her or perhaps just because she looked like easy prey..."
    if dom > sub:
        "Seeing no other choice, Sabia started aggressively. She advanced on one of the orcs, her sword raised, waiting for the inevitable attack from the one on her flank."
        "When he went for a massive overhand swing, she ignored her initial target and lunged at him, the end of her blade slamming into his throat. The orc crumpled, gasping for breath, and the other two flinched."
    else:
        "Sabia lowered her sword, pretending to be afraid of their tactic. The orcs smirked but didn't attack too recklessly, instead closing the distance and then preparing to assault her at once."
        "She took a step back, pretended to slip on the sand... and then ducked underneath their assault, dodging to the side. That put her in the perfect position to hit one of the orcs in the back of the neck, her blow striking true and dropping him."
        "The other two turned on her slowly, only now realizing that her weakness had been a ruse. That gave her a little more time."
    if Sabia.level >= 5:
        $ Sabia.hp -= 5
        $ Sabia.stamina -= 10
        "While they hesitated, Sabia managed to strike the second over the head. She wasn't sure if he would drop, but fortunately, he did."
    elif Sabia.level >= 4:
        $ Sabia.hp -= 10
        $ Sabia.stamina -= 20
        "While they hesitated, Sabia managed to strike the second over the head. She wasn't sure if he would drop, but fortunately, he did."
    else:
        $ Sabia.hp -= 15
        $ Sabia.stamina -= 50
        "While they hesitated, Sabia managed to strike the second over the head. She struck true, but couldn't put enough power into her blow to drop him."
        "That necessitated a desperate fight trying to keep the two from flanking her, Sabia only barely triumphing against both, winded and with a few scrapes and cuts."
    "Just as Sabia started to feel accomplished, the tide of the main battle hit her and suddenly she was surrounded by a dozen different fights, weapons flying in every direction."
    if RGAlutvrognevescene:
        $ Sabia.hp -= 5
        $ Sabia.stamina -= 25
        "The chaos of it was far more intense than she had expected - only her training with Lutvrog and Neve let Sabia keep on her feet - barely. She still took a bit of a beating before she managed to retreat to the edge."
        "One of the orcs rushed after her and Sabia hit him directly in the face. The blow knocked him out, but didn't stop his momentum and he crashed on top of her."
        "When Sabia pushed him off and saw that the battle had moved on, she realized that was actually an advantage. Now she had a bit of freedom to decide how she would spend the rest of the time."
    else:
        $ Sabia.hp -= 15
        $ Sabia.stamina -= 50
        "She was completely unprepared for the roughness of the melee. Sabia managed to survive, but she took a serious beating. In the end she only made it through the rush because she got knocked down and another orc fell on top of her."
        "In the end, though, she crawled from beneath his body before the gong rang. She wasn't eliminated yet, so she had a choice of how she would spend the rest of her time."
    menu:
        "All out assault":
            $ RGAarenascore += 2
            $ Sabia.hp -= 20
            $ Sabia.stamina -= 100
            if Sabia.stamina < 0:
                $ Sabia.stamina = 0
                $ RGAarenascore -= 1
            if Sabia.hp <= 0:
                $ RGAarenascore -= 2
                "Though Sabia did her best to fight, her injuries took too much of a toll. After a blow with a club, she hit the sands of the arena and blacked out for a time."
                "It wasn't long until she came to, but when she did, the match was over. Sabia grimaced and tried to shake off her injuries, hoping that just participating had earned her some reputation."
                hide screen infohud
                return
            if Sabia.stamina <= 10:
                $ RGAarenascore -= 2
                "Though Sabia did her best to defend herself, the battle wore her down too much. She lost focus and then out of nowhere a club caught her on the side of the head. She hit the sands of the arena and blacked out for a time."
                "It wasn't long until she came to, but when she did, the match was over. Sabia grimaced and tried to shake off her exhaustion, hoping that just participating had earned her some reputation."
                hide screen infohud
                return
            "Sabia decided to throw everything she had into the fight, attacking the mass of orcs from behind and taking down as many as she could."
            "Her muscles burned with exhaustion and she was bleeding from multiple minor wounds, but Sabia managed to take down several warriors as time ran out."
        "Focused offensive":
            $ RGAarenascore += 1
            $ Sabia.hp -= 20
            if Sabia.hp <= 0:
                $ RGAarenascore -= 2
                "Though Sabia did her best to fight, her injuries took too much of a toll. After a blow with a club, she hit the sands of the arena and blacked out for a time."
                "It wasn't long until she came to, but when she did, the match was over. Sabia grimaced and tried to shake off her injuries, hoping that just participating had earned her some reputation."
                hide screen infohud
                return
            "Sabia decided that it was most important to be seen getting into the fight, so she traded blows with an isolated orc. She received several painful cuts before she managed to take him down, but hoped the blood would earn her a little respect."
        "Focused defensive":
            $ RGAarenascore += 1
            $ Sabia.stamina -= 100
            if Sabia.stamina <= 10:
                $ RGAarenascore -= 2
                "Though Sabia did her best to defend herself, the battle wore her down too much. She lost focus and then out of nowhere a club caught her on the side of the head. She hit the sands of the arena and blacked out for a time."
                "It wasn't long until she came to, but when she did, the match was over. Sabia grimaced and tried to shake off her exhaustion, hoping that just participating had earned her some reputation."
                hide screen infohud
                return
            "Sabia decided that it was more important to look like she was fighting than take down any opponents, so she got into the melee but focused entirely on defense. She didn't take down any other warriors, but everyone would see her in the thick of things."
        "Full retreat":
            $ RGAarenascore += 0
            "Deciding not to take any chances, Sabia just stayed out of it until the gong finally sounded. She might not gain any honor that way, but it was more important to make it through the melee."
    hide screen infohud
    "When the gong finally sounded, a few orcs kept flailing at each other, but most stopped. Sabia breathed a sigh of relief and looked over the arena. More than half had fallen during the short fight, she was fortunate that she was one of those still standing."
    "But with that, the fight was over. Presumably the Red God was pleased, or something. Vaguely disgusted with orc senselessness, Sabia headed out."
    return


label RGAcaptainmelee:
    scene bg sabiatent
    call sabiabase
    if orcalliance == "tekrok":
        "Sabia was under the impression that there was only another optional melee that day. But when she emerged from her tent, she didn't manage to go anywhere before she was intercepted."
        show tekrok normal at right with moveinright
        t "You're fighting today."
        s "In the melee? Why?"
        t "All the Captains are sending their best warriors to represent them."
        show sabiaemo eyebrow1 at left
        s "Doesn't sending a human to fight for you undermine your message?"
        show tekrok angry1 at right
        t "Shut up, human. Tekrok requires victory before ideological purity."
        show sabiaemo normal at left
        s "Alright, I'll do my part. The goal is just to win?"
        t "As with all melees, there are no explicit victors. But our goal is to take down as many opponents as possible to earn the most honor."
        s "Got it."
        t "You'd better. Tekrok will be watching."
    elif orcalliance == "rokgrid":
        "Sabia was under the impression that there was only another optional melee that day. But when she emerged from her tent, she didn't manage to go anywhere before she was intercepted."
        show rokgrid happy2 at right with moveinright
        r "Sabia! I'm sorry to disturb you, but I must request your assistance!"
        s "What is it?"
        r "The melee battle today is somewhat of a contest between warriors loyal to the Captains. I had made arrangements to fight it without troubling you, so that you could pursue your own ends. Unfortunately, things have become more troublesome."
        show rokgrid normal at right
        r "Tekrok has brought in warriors from outside the tribe, meaning that his forces now outnumber mine."
        s "So you want me to fight with your warriors? I guess I can do that."
        r "Actually... not just that. One of the warriors Tekrok has brought in is a criminal who will cause even more trouble. I want you to fight, yes, but to specifically target him."
        s "That's... okay, can do. Which one?"
        r "You'll know him because he'll be the only warrior wielding an axe in each hand. Make sure he doesn't survive."
        show rokgrid happy2 at right
        r "Thanks so much for helping out, Sabia!"
    elif orcalliance == "dajrab":
        "Sabia was under the impression that there was only another optional melee that day. But when she emerged from her tent, she didn't manage to go anywhere before she was intercepted."
        show dajrab normalclosed at right with moveinright
        d "Sabia, I have a request to make of you."
        s "What is it?"
        d "As I hope you know, today's melee has become a contest between proxies of the Captains. It has grown larger than I expected, so I hope you will assist my warriors."
        s "I was considering participating anyway, so it's not too much of an imposition. It's taking a risk, though."
        d "I need to say a word about our goals. Warriors of Tekrok and Rokgrid will throw great strength into eliminating the other side. My goal is for every warrior aligned with me to be standing at the end of the melee."
        s "Hmm. I guess that wouldn't be too much trouble."
        d "I gave you little forewarning, though, and it is still your choice. Will you assist?"
        menu:
            "Participate":
                $ Sabia.xp += 3
                show sabiaemo happy1 at left
                s "Sure, I'll help out!"
                d "Thank you, Sabia. My warriors will make themselves known to you when the match starts."
            "Skip it":
                $ A_dajrab -= 1
                show sabiaemo closed2 at left
                s "Sorry, Dajrab, but I have business of my own I need to take care of."
                d "Very well, it is your choice."
                hide dajrab normalclosed at right with moveoutright
                "With that, he left swiftly. Sabia was a little surprised it had been that easy, but thought this was for the best. She could leave the Captains to their squabbling and spend the entire day preparing for the end of the Red God's Arena."
                return
    elif orcalliance == "sabia":
        "Sabia woke up already considering her options for the day. There was a melee that was supposed to be different from the normal ones - allegedly this one would have warriors chosen by the Captains participating, and more honor was on the line. That meant the warriors would likely be better than average."
        "Normally, she might avoid such a thing, but Sabia found herself wondering what it would mean if she participated. Would she be representing herself as a rival? Would that be going too far, or an appropriate step forward?"
        "The better question might be if she could afford to get herself beaten up when she had other things to be preparing for. The event started early, though, so she needed to make a decision soon..."
        menu:
            "Participate":
                "Deciding that she should keep pressing matters, Sabia equipped herself and headed down to the arena. If she was standing aside from all three Captains, that meant she needed to prove that she had the strength to stand up to them, too."
            "Skip it":
                "Sabia decided to leave the Captains to their squabbling. She could ignore the melee and spend the entire day preparing for the end of the Red God's Arena."
                return
    scene bg RGAbg4 with dissolve
    "Sabia took her time preparing before she headed to the arena herself. She was a little worried about the difficulty of this match - while the most elite of warriors would probably not be participating, the orcs there would still be stronger than those she was used to dealing with."
    if orcalliance == "sabia":
        "Once she was down on the sands, Sabia tried to seem completely confident as more and more warriors entered. If she had been aligned with a Captain, she would have allies, but like this... she would be fighting alone in a match devoted to teams."
    else:
        "Once she was down on the sands, Sabia tried to seem completely confident as more and more warriors entered. At least a decent number of them were her allies - those naturally gravitated toward her, presumably because she was the most distinctive part of their Captain's group."
    scene bg RGAmelee2 with dissolve
    "Ornshakar was alone to begin this match, going through a surprisingly ornate ceremony before the gong could be struck. Sabia spotted all three Captains watching carefully, as well as Warchief Groknak."
    "It was obvious that few cared about the ceremony, though Sabia saw a few of Dajrab's soldiers touch a blade to their foreheads. Most were just waiting for the gong."
    show screen infohud("left")
    "It sounded, and the battle closed immediately."
    if orcalliance == "sabia":
        $ Sabia.hp -= 5
        $ Sabia.stamina -= 25
        "There was a vicious clash before any sides formed, and despite Sabia's best efforts, she took a rough blow. Eventually, though, she managed to pull back from the main fray."
        if RGAgeneralmeleeparticipated:
            $ Sabia.hp -= 5
            $ Sabia.stamina -= 20
            "Once she had a little distance, Sabia was able to maintain control of the flow of battle around her. Everyone was much more highly skilled than in the first melee, but her instincts were ready for the chaotic challenge."
        else:
            $ Sabia.hp -= 15
            $ Sabia.stamina -= 50
            "Even on the margins, Sabia struggled to keep up. Truthfully, it had been a long time since she'd fought in a melee like this and a lot of her instincts were rusty."
    else:
        $ Sabia.hp -= 5
        $ Sabia.stamina -= 25
        "There was a vicious clash before any sides formed, and despite Sabia's best efforts, she took a rough blow. Eventually, though, she managed to pull back with allied orcs."
        if RGAgeneralmeleeparticipated:
            $ Sabia.hp -= 5
            $ Sabia.stamina -= 20
            "Once she had people on either side of her, Sabia was back in more familiar territory. Unlike the last melee, she had allies, so all her combat instincts worked together smoothly."
        else:
            $ Sabia.hp -= 15
            $ Sabia.stamina -= 50
            "Even with allies on either side, Sabia struggled to keep up. Truthfully, it had been a long time since she'd fought in a melee like this and a lot of her instincts were rusty."
    "For a while, the battle raged chaotically and it was the most Sabia could do to hold her own. There were no changing sides or opportunistic blows, every side was determined to win."
    "She had expected there to be three main groups, one for each Captain, but to her surprise, there seemed to be five factions. Groups from outside Groknak's tribe, she presumed, as she didn't recognize any of them."
    $ Sabia.hp -= 5
    "Without warning, the swing of a warhammer clipped Sabia. She managed to avoid the main force of the blow, but it still knocked her away."
    "She scrambled to her feet and realized that she had orcs attacking her from two sides. She couldn't take both and had only a split second to act..."
    menu:
        "Attack the larger one":
            $ Sabia.hp -= 10
            $ Sabia.stamina -= 25
            $ Sabia.xp += 2
            "Knowing she needed to focus her attention, Sabia threw herself against the larger orc to use her speed against him. He was slow... but not as slow as he should have been, given his size."
            "Sabia barely managed to knock him back when the second orc was coming after her, slicing a cut in her upper arm before the tide of battle struck them and Sabia had an opportunity to withdraw."
        "Attack the faster one":
            $ Sabia.hp -= 5
            $ Sabia.stamina -= 50
            $ Sabia.xp += 2
            "Knowing she needed to focus her attention, Sabia threw herself against the faster one, who wouldn't have a strength advantage over her. When he parried her blow, though, Sabia grunted and fell back - he was still damn strong."
            "Worse, the larger orc was getting into range to attack her. Sabia retreated from both, weaving a careful defense as she went. She managed to get away with only a few bruises, but felt exhausted."
        "Retreat":
            $ Sabia.hp -= 5
            $ Sabia.stamina -= 20
            $ RGAarenascore -= 1
            "Not wanting to take any risks, Sabia backpedaled to a safer position as fast as she could. They pressed her so seriously that she was still exhausted and bruised by the time she got away, but it was better than taking a major risk."
        "Use their strength against each other" if RGAlutvrognevescene:
            $ RGAarenascore += 1
            $ Sabia.stamina -= 35
            $ Sabia.xp += 2
            "Recalling her training against Neve and Lutvrog, Sabia ducked away, just close enough to draw both of the orcs into range against each other. They had to fear the other's blows, and she immediately struck against them."
            "They were good, but nothing like her previous sparring mates. Sabia managed to knock out the smaller one with a lucky blow to the head, and battered at the larger one until the tide of the melee hit them and he had to retreat."
    "Several orcs surged at Sabia, fighting both her and each other. Sabia had no time for strategy, no time for anything but a desperate defense. She had to roll backward through the sand, leaving her disoriented and covered in it."
    if Sabia.level >= 5:
        $ Sabia.stamina -= 10
        "Fortunately, it looked like she'd managed to ward off her attackers, so her escape had been successful. She was free of immediate threats for now."
    elif Sabia.level >= 4:
        $ Sabia.stamina -= 20
        "Fortunately, it looked like she'd managed to ward off her attackers, so her escape had been successful. She was free of immediate threats for now."
    else:
        $ Sabia.hp -= 5
        $ Sabia.stamina -= 50
        "Unfortunately, she hadn't been able to ward them off fast enough, and she'd taken a nasty cut before she could roll. Still, she was free of immediate threats for now."
    "After such hectic fighting, the moment when Sabia found herself standing alone without an opponent was almost startling. It wouldn't last long, so she needed to seize the opportunity to make an impact..."
    menu:
        "Take down as many orcs as possible":
            $ RGAarenascore += 1
            $ Sabia.hp -= 10
            $ Sabia.stamina -= 50
            $ Sabia.xp += 2
            if orcalliance == "tekrok":
                $ RGAcaptainapproval = True
            "Since time was running out, Sabia went on the offensive, attacking with everything she had left. Though she came dangerously close to being taken out by a club, she dealt more damage than she took."
        "Assist allied orcs" if orcalliance != "sabia":
            $ Sabia.hp -= 5
            $ Sabia.stamina -= 10
            $ L_orcs += 1
            $ Sabia.xp += 1
            if orcalliance == "dajrab":
                $ RGAcaptainapproval = True
            "Deciding to play it safe, Sabia retreated to allied orcs and stood firm with them. She was gratified to be part of their defensive formation, which actually wasn't an embarrassment."
        "Take on one of the stronger looking orcs" if orcalliance != "rokgrid":
            $ RGAarenascore += 1
            $ Sabia.hp -= 10
            $ Sabia.stamina -= 35
            $ Sabia.xp += 3
            "Since she needed to make a show in the final moments, Sabia looked for someone she could take down and spotted her target: an orc viciously wielding two axes that looked only slightly blunted."
            "Sabia rushed him without hesitating, nearly getting decapitated by the first swing. But as strong as his offense was, the orc weakened his defense by using a weapon in each hand."
            "She knocked aside his secondary blow and hit him straight in the throat. He took another wild swing at her before he crumpled."
        "Take down the orc wielding two axes" if orcalliance == "rokgrid":
            $ RGAarenascore += 1
            $ Sabia.hp -= 10
            $ Sabia.stamina -= 35
            $ Sabia.xp += 3
            if orcalliance == "rokgrid":
                $ RGAcaptainapproval = True
            "Remembering Rokgrid's task, Sabia looked around and fortunately spotted her target: he was definitely distinctive, viciously wielding two axes that looked only slightly blunted."
            "Sabia rushed him without hesitating, nearly getting decapitated by the first swing. But as strong as his offense was, the orc weakened his defense by using a weapon in each hand."
            "She knocked aside his secondary blow and hit him straight in the throat. He took another wild swing at her before he crumpled."
            "Still in the same movement, Sabia went down after him. Bracing her sword with both hands, she brought it down hard on his throat, crushing his windpipe. She got up to keep fighting as if it was a normal blow, leaving him to suffocate."
        "Take on foreign orcs" if orcalliance == "sabia":
            $ RGAarenascore += 1
            $ L_orcs += 1
            $ Sabia.hp -= 5
            $ Sabia.stamina -= 25
            $ Sabia.xp += 2
            "Deciding that she might as well play to the home crowd, Sabia struck at the orcs she didn't recognize. They underestimated her completely, practically sneering at the human female, and she made them pay dearly for it."
    hide screen infohud
    "Then, without warning, the gong rang. Everyone slowed to a halt, realizing that the frenzy of violence was suddenly over. The crowd was cheering, but she realized it only slowly as her ears recovered from the clash."
    if Sabia.hp >= 1:
        $ RGAarenascore += 1
        "Sabia had a few injuries, but many orcs had worse. She shrugged off the pain and stood tall, letting everyone watching see that she'd made it through."
    else:
        "Sabia was covered in more blood than she expected, too much of it hers. Compared to many of the orcs, she'd fared poorly."
    if Sabia.stamina >= 1:
        $ RGAarenascore += 1
        "Though she was exhausted, Sabia had paced herself right, using up the last of her strength in the final moments. She'd done everything she could."
    else:
        "She was absolutely exhausted, though. Toward the end she'd gotten tired and sloppy, and she wished that she could have done more."
    "Once the cheering was over, though, the battle simply resolved. Unlike in real war, there were no victors, no aftermath... no point, really. Sabia had to suppress a scowl as she came down from the battle high and began to leave the arena."
    scene bg RGAbg4
    call sabiabase
    with dissolve
    if orcalliance == "tekrok":
        "As she left the arena, however, she didn't go far before she was intercepted by Tekrok. That was the reason she'd gone to the trouble, after all."
        show tekrok normal at right with moveinright
        t "It could have been worse. Good enough for a human."
        if RGAcaptainapproval == True:
            $ A_tekrok += 3
            t "Many warriors fell at your hands. Good to see a human who can follow orders."
            s "I just did what I needed to."
            t "As you were commanded. Tekrok will remember this."
        else:
            t "But you fought like a fearful human instead of bringing down warriors. You disobeyed Tekrok."
            s "Next time you're in the middle of a melee, you can do a better job."
            t "Hmph. You must do better."
        "With that, Tekrok stomped away. Sabia stood for a moment before heading back to her tent. She really needed the rest."
    elif orcalliance == "rokgrid":
        "As she left the arena, however, she didn't go far before Rokgrid came out to greet her. That was the reason she'd gone to the trouble, after all."
        show rokgrid happy2 at right with moveinright
        r "Ah, Sabia! Well done, well done indeed!"
        s "Thanks, I did my best."
        if RGAcaptainapproval == True:
            $ A_rokgrid += 3
            r "Indeed you did! I was quite happy to see that you were able to take care of the little matter we discussed - our camp will be safer with that criminal gone."
        else:
            r "Ah, I'm certain you did. I was disappointed that you let that criminal roam free, but I will find another way to deal with it."
        r "Thank you for fighting, Sabia! Perhaps soon, I can be of assistance to you!"
        "With that, Rokgrid headed off to greet his other warriors. Sabia stood for a moment before heading back to her tent. She really needed the rest."
    elif orcalliance == "dajrab":
        "As she left the arena, however, she didn't go far before Dajrab emerged and nodded to her. That was the reason she'd gone to the trouble, after all."
        show dajrab normalclosed at right with moveinright
        if RGAcaptainapproval == True:
            $ A_dajrab += 3
            d "Thank you for fighting with us, Sabia. It is good to see that you were able to fight alongside orcs as allies."
            s "They did a good job guarding my back too."
            d "Nonetheless, I am glad you assisted with the overall strategy. We showed ourselves to be stable where other factions are reckless."
            s "So that's what it was about."
            d "Yes. Stability will be very important in the coming days... as we will all learn."
        else:
            d "Thank you for fighting with us, Sabia. I wish that you could have cooperated more with my warriors, but your assistance is appreciated nonetheless."
            s "I did the best I could, okay?"
            d "In a sense, that is universally true."
        "With that, Dajrab faded back to his own tent. Sabia stood for a moment before heading back to her tent. She really needed the rest."
    elif orcalliance == "sabia":
        $ dom += 1
        "Still, this was the kind of thing that mattered to orcs. Sabia did her best to set aside her scorn so she could take advantage of the opportunity."
        "She didn't spend long in the arena before heading back into camp, though. She was very glad this was the last melee event."
    return


label RGAshamanevent:
    scene bg RGAbg3 with dissolve
    "Down at the arena, Sabia discovered that this fight had a strange tone compared to the others. There were orcs dressed with stag horns on their heads, others with wolf pelts, and others with red hats. They were preparing to fight, but instead of crude practice weapons they held complex-looking ceremonial ones."
    "Both Ylva and Ornshakar were there, presiding over what was obviously a partially ceremonial fight. Ylva was taking a more general position, while Ornshakar spent most of his time working with the orcs that wore horns similar to his."
    "Sabia had no idea what any of it meant, but decided that she was rooting against the stag warriors."
    "Both shamans withdrew, and the battle began. It was no chaotic melee, but neither was it a purely ceremonial affair. Each group fought the others viciously, their weapons shedding a great deal of blood but not dealing lethal blows. Lots of orcs were going to have missing eyes or nasty scars once it was done."
    if ylvatalkcheating == True:
        $ A_ylva += 3
        "As the match went on, the horned warriors began to flag. That was not so surprising, but Sabia watched Ornshakar become more and more irritated. He kept eyeing the sands of the arena strangely, as if looking for something, but nothing came of it."
        "Instead, he stood there furiously as his warriors were taken down. The wolf pelt group fought to a stalemate with the red hat group, then both bowed to one another and the match was over."
        "Though she had zero idea what the ritual meant, and wasn't sure about what exactly had happened, Sabia found herself smiling. If things hadn't gone how the shaman wanted, she was happy with that."
        "But on that note, when Sabia started to leave the arena, she found Ylva waiting for her."
        call sabiabase
        show ylva closednormal at right
        show ylva2 arm2 at right
        with dissolve
        ylva "I... need to apologize for earlier."
        s "So he was cheating after all?"
        show ylva normal at right
        ylva "Yes. I haven't unraveled his reasons, but he seems to be trying to increase his standing by proving he has the favor of the spirits. Which he then ensures via magic."
        s "Didn't seem to work out, though."
        show ylva angry3 at right
        ylva "Yes, it seems someone interfered with his enhancement magic. How strange."
        s "You don't need to apologize, Ylva. I'm just glad to see him fail. Did it ruin the ritual, though?"
        show ylva angry1 at right
        ylva "This was a travesty, but... truthfully, this whole fight was a perversion of what it was meant to be. Traditionally, the warriors would enact a mock battle between the spirits, to teach lessons to the entire tribe."
        s "They still did, just different lessons."
        show ylva closedangry at right
        ylva "Thank you for informing me of what was going on, but... forgive me, I'm frustrated about all this. I must go."
        hide ylva closedangry at right
        hide ylva2 arm2 at right
        with moveoutright
        "With that, Ylva headed away. Sabia was sorry to see her upset, but couldn't really hide the smile from her face. So she'd managed to undercut Ornshakar after all. This had gone well as far as she was concerned."
        "Since she had nothing else she was obligated to do for the day, Sabia headed back to her tent considering her options..."
    else:
        "The horned warriors quickly gained the upper hand, fighting with a strange ferocious energy. As far as Sabia could tell, Ornshakar wasn't doing anything, but he had such a smug look on his face that she was sure he was cheating somehow."
        "There wasn't much she could do about it from here, though, so Sabia had to watch in irritation as the horned group won the event and was officially acknowledged in another ceremony."
        "Ylva looked troubled, but said nothing, merely played her part in the ceremony. Though Sabia considered speaking to her, she vanished quickly after the match was over."
        "Irritated by the whole experience, Sabia headed back to her tent, trying to put it out of her mind. It was just some stupid orc ritual - she had more important things to worry about."
    return


label RGAsabiafight1:
    scene bg RGAbg
    call sabiabase
    $ Sabia.stamina -= 50
    "Sabia headed to the arena, not entirely sure what to expect. She had been told that some of these fights were sacred and to the death, which made her a little nervous that she'd run into someone important."
    "But as it happened, she ended up facing off against an orc she'd never met before. He just sneered at her when she got close, which put her in the mood for a fight to the death."
    "With the crowd watching, Sabia raised her sword and waited for the gong to signal the start of the fight."
    $ enemy_level = 8
    $ enemy_maxhp = 600
    $ enemy_hp = enemy_maxhp
    $ enemy_type = 1
    $ enemy_skills = [Enemyattack,Enemyquickattack]
    $ enemy_attack = 70
    $ enemy_defense = 20
    $ enemy_magdefense = 10
    $ GenericOrc2.face = "normal"
    $ GenericOrc2.extras = ["Loincloth", "Helmet", "Strap", "Shoulder", "Wrists", "Axe"]
    $ player = Sabia
    $ enemy = GenericOrc2
    call duel
    if _return == "Victory":
        scene bg RGAbg
        call sabiabase
        play music orccamp fadeout 2.0 fadein 2.0
        "Victorious, Sabia wiped her weapon off on the orc corpse and looked up to see what was next. But it seemed that she was truly done, having risked her life once, so she was allowed to go."
        "That made sense, as they couldn't afford to have constant battles to the death or their numbers would soon be vastly diminished. That meant she had the rest of the day to prepare."
    else:
        show gameover with dissolve
        pause 3
        $ renpy.full_restart()
    return


label RGAsabiafight2:
    scene bg RGAbg
    call sabiabase
    $ Sabia.stamina -= 50
    "Sabia headed to the arena for her second duel to the death. This time she faced an unfamiliar warrior from Groknak's camp, someone she didn't know the loyalties of."
    "He listened to Ornshakar very seriously as the shaman began the match, then raised his weapon to his forehead respectfully. This was a religious thing to him, then, some kind of sacrifice to the Red God."
    "Well, Sabia had strong theological opinions about who should be sacrificed."
    $ enemy_level = 8
    $ enemy_maxhp = 500
    $ enemy_hp = enemy_maxhp
    $ enemy_type = 1
    $ enemy_skills = [Enemyattack,Enemyquickattack,Bumrush]
    $ enemy_attack = 70
    $ enemy_defense = 20
    $ enemy_magdefense = 0
    $ GenericOrc2.face = "normal"
    $ GenericOrc2.extras = ["Loincloth", "Helmet", "Strap", "Shoulder", "Wrists", "Axe"]
    $ player = Sabia
    $ enemy = GenericOrc2
    call duel
    if _return == "Victory":
        scene bg RGAbg
        call sabiabase
        play music orccamp fadeout 2.0 fadein 2.0
        "Once the orc was dead, Sabia waited long enough that she didn't look disrespectful, then left the arena."
    else:
        show gameover with dissolve
        pause 3
        $ renpy.full_restart()
    return


label RGAsabiafight3:
    scene bg RGAbg
    call sabiabase
    with dissolve
    $ healthpotionsdisabled = True
    "Sabia wasn't entirely sure what to expect when she headed toward the Red God's Arena for the final day of combat. Allegedly this penultimate day was the true challenge for the most honorable warriors, and it was fortunate that she'd qualified."
    "No one would battle to the death today - all of them had received the Red God's blessing. Everyone would be given healing in between the matches as well but healing potions were forbidden during matches, so that there was only a contest of strength."
    "But the winners would be permanently declared champions and no longer required to participate in future Arenas for honor. Allegedly the Warchief and Captains had won before. So had Lutvrog, but he chose to continue participating."
    "That was all Sabia knew. She hoped that she was ready."
    "At the entrance, she paused for just a moment. If she walked inside, she would be facing a brutal gauntlet of fights, no doubt ending in her defeat. Was that what she wanted?"
    if sub >= 5:
        menu:
            "Enter":
                "Though Sabia thought she could slip out of it, she saw no reason not to push forward. She'd gained enough honor just by making it this far, anything else she managed was just a bonus."
            "Submission: Concede gracefully":
                $ RGAarenascore += 1
                $ L_orcs += 1
                $ A_lutvrog -= 1
                "Deciding to focus on the long term instead of just this event, Sabia instead spoke to the warriors, saying that she wouldn't compete. She gave a lot of compliments and talked about how she was honored just to have made it this far."
                "It seemed to work, the warriors accepting her concession without scorn. She thought she spotted a slight frown on Lutvrog's face, but that was to be expected. She had better ways of making him happy, anyway."
                "And with that, it was over. Sabia left the arena for the last time and leaned against the wall outside, just listening as battles went on within."
                jump RGArewards
    else:
        "It didn't matter what she wanted, of course. Sabia could see no way of bowing out of the fights without losing a lot of face. So she grimly headed inward."
    "Sabia strode forward into the sands and took up a place in one corner. Others were already fighting, so it was only a matter of time before it was her turn..."


label RGAsabiafight3loop:
    scene bg RGAbg
    call sabiabase
    $ Sabia.hp = Sabia.maxhp
    $ healthpotionsdisabled = True
    menu:
        "Next match":
            if RGAchallengefights == 0:
                $ GenericOrc2.face = "normal"
                $ GenericOrc2.extras = ["Loincloth", "Wrists", "Axe"]
                $ enemy_skills = [Disablingblow]
                $ enemy_level = 9
                $ enemy_maxhp = 600
                $ enemy_hp = enemy_maxhp
                $ enemy_type = 1
                $ enemy_attack = 75
                $ enemy_defense = 50
                $ enemy_magdefense = -5
                $ player = Sabia
                $ enemy = GenericOrc2
                call duel
                if _return == "Victory":
                    $ RGAchallengefights += 1
                    $ RGAarenascore += 1
                    "One opponent down, and with that the group of remaining fighters had been cut in half. The losers remained in the arena, though no one cheered for them."
                    scene bg RGAbg
                    jump RGAsabiafight3loop
                else:
                    "Sabia slumped to the ground, her vision briefly going black, but she could feel healing magic surging toward her..."
                    jump RGArewards
            elif RGAchallengefights == 1:
                $ GenericOrc1.face = "normal"
                $ GenericOrc1.extras = ["Loincloth", "Helmet", "Wrists", "Axe"]
                $ enemy_skills = [Slowingstrike]
                $ enemy_level = 10
                $ enemy_maxhp = 625
                $ enemy_hp = enemy_maxhp
                $ enemy_ep = 10
                $ enemy_type = 1
                $ enemy_attack = 65
                $ enemy_defense = 20
                $ enemy_magdefense = 0
                $ player = Sabia
                $ enemy = GenericOrc1
                call duel
                if _return == "Victory":
                    $ RGAchallengefights += 1
                    $ RGAarenascore += 2
                    "Trying not to stumble as she moved away from the battlefield, Sabia gratefully drank the potion she was offered. Her body might be fine, but she also needed to clear her mind and settle her nerves for the next fight."
                    scene bg RGAbg
                    jump RGAsabiafight3loop
                else:
                    "Sabia slumped to the ground, her vision briefly going black, but she could feel healing magic surging toward her..."
                    jump RGArewards
            elif RGAchallengefights == 2:
                $ GenericOrc1.face = "normal"
                $ GenericOrc1.extras = ["Loincloth", "Axe"]
                $ enemy_skills = [Preparation, PreparedstrikeI, Enemyattack]
                $ enemy_level = 11
                $ enemy_maxhp = 500
                $ enemy_hp = enemy_maxhp
                $ enemy_type = 2
                $ enemy_attack = 80
                $ enemy_defense = 0
                $ enemy_magdefense = 20
                $ player = Sabia
                $ enemy = GenericOrc1
                call duel
                if _return == "Victory":
                    $ RGAchallengefights += 1
                    $ RGAarenascore += 2
                    "Sabia leaned back against one of the walls, shaking her wrists to try to get feeling back into them. That battle had been rough, her opponents' blows sending ripples of force through her. But now she was done and in even more elite company."
                    scene bg RGAbg
                    jump RGAsabiafight3loop
                else:
                    "Sabia slumped to the ground, her vision briefly going black, but she could feel healing magic surging toward her..."
                    jump RGArewards
            elif RGAchallengefights == 3:
                $ GenericOrc2.face = "normal"
                $ GenericOrc2.extras = ["Loincloth", "Helmet", "Strap", "Shoulder", "Wrists", "Axe"]
                $ enemy_skills = [Enemyenchantedattack]
                $ enemy_level = 12
                $ enemy_maxhp = 650
                $ enemy_hp = enemy_maxhp
                $ enemy_type = 1
                $ enemy_attack = 65
                $ enemy_defense = 20
                $ enemy_magdefense = 0
                $ player = Sabia
                $ enemy = GenericOrc2
                call duel
                if _return == "Victory":
                    $ RGAchallengefights += 1
                    $ RGAarenascore += 2
                    "Sabia was a little surprised herself to find that she'd won. Even if she didn't get further than this, she was damn satisfied with herself."
                    scene bg RGAbg
                    jump RGAsabiafight3loop
                else:
                    "Sabia slumped to the ground, her vision briefly going black, but she could feel healing magic surging toward her..."
                    jump RGArewards
            elif RGAchallengefights == 4:
                "Sabia walked out onto the sands and found Lutvrog facing her. She'd known it would come to this ever since she'd seen that he was participating and knew that she couldn't win."
                "That didn't mean she was going to make it easy for him. She began the battle by lunging at him with a roar, trying to take him out before he could get started."
                if RGAlutvrogtrain:
                    $ RGAarenascore += 1
                    "His axe swung straight at her and would have bashed her momentum to the side, if she hadn't seen the move multiple times while fighting him. Sabia managed to avoid being thrown off balance and even managed to strike back, though he pulled away and avoided her cut."
                    "Knowing she couldn't last in an extended match, Sabia decided to pour everything she had into a brief fight. At least that way she'd look good doing it."
                    if RGAlutvrognevescene:
                        $ RGAarenascore += 1
                        "To her surprise, she kept up with him for a brief while, even forced him to take a step back."
                        "The blood rushing in her ears quieted for a moment as she had a chance to breathe, and Sabia realized that orcs were cheering for her. She was the underdog, so she was earning approval just by lasting this long."
                        "To her surprise, she actually spotted Neve watching from high in the stands, a smile on her face. Sabia wondered if she was thinking about what the three of them had done ear-"
                        "Her momentary distraction was all Lutvrog needed, his axe hooking her leg and driving her to the ground."
                    else:
                        "But though her plan worked, Sabia only made it through a few exchanges of blows before she started to slow down. And that was all Lutvrog needed, his axe hooking her leg and driving her to the ground."
                else:
                    "It didn't work, of course. Lutvrog expertly used her momentum against her, then leveraged his superior strength."
                    "She kept up with him for one exchange of blows, even a second, then she was flattened to the ground with his axe biting into the sands beside her head."
                "Though she had lost, Sabia didn't mind. She just found herself smiling up at Lutvrog, who nodded respectfully and helped her to her feet."
                "There were a few more rounds after that, Lutvrog winning all those that remained. Sabia just sat and recovered. Eventually the gong sounded, indicating that the final match was over."
                jump RGArewards
        "Check next opponent":
            if RGAchallengefights == 0:
                "Sabia's first opponent looked cautious, avoiding dangerous blows from his opponents and sliding through their own defenses."
            elif RGAchallengefights == 1:
                "Sabia's next opponent had won the previous match by ruthlessly disabling his opponents before going for the finishing blow."
            elif RGAchallengefights == 2:
                "Sabia's next opponent held back, then unleashed vicious attacks once he was prepared."
            elif RGAchallengefights == 3:
                "Sabia's next opponent was a monstrous orc wearing heavy armor. His previous opponent had barely managed to scratch him. Both his weapons and armor were thick with orcish enchantments."
            elif RGAchallengefights == 4:
                "Sabia's next opponent... was Lutvrog. Though Sabia intended to give him the best fight she could, she had a feeling the result was inevitable."
        "Change Equipment":
            hide screen infohud
            $ actor = Sabia
            call statsscreen
            while Sabia.armor == "None":
                $ Sabia.face = "closed2"
                s "I really don't want to walk around a bunch of orcs naked like this."
                call statsscreen
            $ Sabia.face = "normal"
            show screen infohud("left")
        "Help from Jadk (1)" if (RGAjadkhelp == False and A_jadk >= 5):
            $ RGAjadkhelp = True
            call sabiabase
            show jadkbase at right
            show jadkemo closedhappy at right
            jadk "You're doing pretty well! Better than old Jadk, gwahaha!"
            s "Thanks. It's getting rough out there, though, there aren't any weaklings left."
            jadk "You look tired. Have a stiff drink on Jadk!"
            "He handed a mug toward her and Sabia took it on instinct. She wasn't sure if this was really the time for a drink... but the liquid smelled strange, not just like the usual orc beer. After some thought, Sabia started drinking."
            "As she drank, she felt a strange numbness spread from her throat. Sabia frowned and wiggled her fingers, but they felt just as agile as before. Yet when she poked herself, she barely felt it."
            s "That wasn't just beer, was it?"
            jadk "Let's call it Jadk's special brew!"
            s "Is that... allowed?"
            jadk "Gwahaha, Jadk doesn't see anyone stopping us!"
            $ Sabia.add_buff("Jadk's Brew", 5)
        "Help from Maply (1)" if (RGAmaplyhelp == False and A_maply >= 5):
            $ RGAmaplyhelp = True
            call sabiabase
            show maply 1 at right
            show maplyemo normal at right
            maply "Hey there, Saby!"
            show sabiaemo happy1 at left
            s "Come to watch, Maply?"
            maply "I think it's so amazing that you've gotten this far!"
            show maplyemo happy at right
            maply "But I'm also here to help a bit! Here, chew this!"
            show sabiaemo normal at left
            "Maply handed Sabia a leaf, which she eyed skeptically. With anyone else, she might have thought it was intended to mock her, but Maply seemed so earnest... Sabia put it in her mouth and began to chew."
            "It tasted foul... but it also left a strange tingling sensation in her mouth. Sabia kept chewing, eyebrows rising, and felt her entire body start to tingle."
            maply "We use those to perk ourselves up on long scouting missions! You should be able to move a little faster and hit a little harder!"
            show sabiaemo happy1 at left
            s "Yes, I can feel it... thanks, Maply!"
            maply "Good luck!"
            $ Sabia.add_buff("Maply's Leaf", 5)
    jump RGAsabiafight3loop


label RGArewards:
    $ healthpotionsdisabled = False
    play music orccamp fadeout 2.0 fadein 2.0
    "Sabia actually breathed a sigh of relief, since that meant all the tension was over. She was done, at least for now."
    scene bg countryside with dissolve
    "In the end, Sabia felt more tired than anything else. She wasn't the champion, so why were they making her stick around? Her chance to ask Ylva slipped away too quickly when she gestured for her to follow the other honored warriors outside the arena."
    "She hadn't been sure what to expect, but it hadn't been this: Warchief Groknak stood between a builder dismantling part of the arena wall and a bunch of uprooted saplings, their roots roughly bagged as if for planting."
    show groknak normalopen at center with dissolve
    g "All of you have fought well, to endure to the end of the Red God's Arena. Your sweat and blood have been accepted by the Red God."
    show groknak normal at center
    if RGAarenascore < 5:
        $ L_orcs -= 1
        "And with that brief speech, Sabia was escorted away with some of the other orcs who hadn't done as well. That was {i}it{/i}? Sabia shook her head and left - she should have known better than to expect anything more from orcs."
        "Sabia headed back to camp - she had a day left to relax before the closing ceremony, but wasn't sure how to spend it..."
        return
    else:
        "That seemed to be his main speech, which struck Sabia as laughably short. Yet the orcs bowed their head as if it was some great honor. Maybe they really were religious."
        if A_ylva >= 5:
            "Feeling like the whole thing was going to be a waste of time, Sabia considered leaving. She stopped only because Ylva approached and seemed to be taking things seriously."
        else:
            "Feeling like the whole thing was going to be a waste of time, Sabia considered leaving. She stopped only because Ornshakar had come up behind them and might use it against her somehow."
    show orcshaman normal at right with moveinright
    show ylva normal at left
    show ylva2 arm2 at left
    with moveinleft
    g "The shamans will now include your names in their chant, so that the Red God might remember you in your next battle."
    "With that, Ylva and Ornshakar began a slow, meditative chant, alternating lines between them. The orcs seemed to be taking it surprisingly seriously, even the ones she'd taken as simple brute warriors. Perhaps the Red God was the only spirit they cared about."
    "Since it was all gibberish to Sabia, she just stayed quiet and listened for her name. And... that was it. Sabia felt pretty underwhelmed, but kept that to herself."
    if RGAarenascore >= 20:
        $ A_groknak += 3
        $ A_tekrok += 4
        $ A_rokgrid += 4
        $ A_dajrab += 2
        $ A_ylva += 2
        $ A_lutvrog += 3
        $ L_orcs += 8
        $ dom += 2
        $ sub += 2
        "After the chant was done, Sabia shifted impatiently, but it still wasn't over. Ylva stepped forward and raised her staff in front of her."
        ylva "All of you have honored the memory of our ancestors and earned a symbol of that honor. First, choose a tree to be your Memory of Redkor."
        "The orcs immediately surged for the trees and Sabia joined them awkwardly. To her surprise, the orcs took to the activity eagerly, trying to find the trees they thought would be biggest and strongest. They jockeyed for position a little, but didn't fight and were oddly respectful."
        g "Inscribe your name at the base of the tree to join your memory to our history. It will be planted outside the camp and grow strong, as you grow strong."
        "Sabia obeyed, now even more uncertain than before. Orcs planting trees? And viewing it as an honor? Yet they all seemed so solemn as they carved their names that Sabia felt like she knew less than at any moment since reaching the camp."
        "Some of the orcs departed at that time, giving their trees to the care of Ornshakar. But Ylva shook her head when Sabia started to go with them, so apparently it still wasn't over."
        ylva "Second, those of you who have endured to the end... come forward and take a symbol of the Memory of Aedre."
        "The orcs surged toward the builder as if they had been waiting for that moment. The old orc had taken down a section of the wall and left only a pile of rubble. Now he began handing out pieces of the stone."
        "Sabia's skepticism about the whole event was being worn down by how seriously the orcs took receiving their rocks. Normally she might joke to herself about orcs valuing rocks, yet she found herself accepting the stone carefully."
        "It was old and heavy, worn by time. Sabia weighed it in her hands as she waited - most of the orcs were dismissed, leaving only her and a small number remaining. Though the whole ceremony was a bit primitive, Sabia was a little proud to have endured all the way to this elite group."
        ornshakar "The Red God's Arena is worn down by the world, but born anew by our worship."
        ylva "Step forward and join your blood to the Memory of Baldar, the foundation of the arena itself."
        "Sabia noticed that the builder had a pile of bricks that looked new, ready to be placed into the section of the wall that had been taken down. The highest ranked warrior stepped forward and waited reverentially."
        "The builder took the largest stone and set it as part of the foundation. The warrior made a small cut on his arm, letting his blood drop down on top of the stone. Immediately the builder spread mortar over it, laying the first stone in place."
        "One by one, the orcs joined their blood to the foundation of the arena itself. It wasn't just words and petty rituals - this was a deep symbol of everything they believed. Sabia stood quiet and still."
        "Eventually, it came to be her turn. She didn't merit one of the larger stones, but hers was still part of the foundation. Sabia didn't hesitate in opening a cut and adding her blood to the mortar."
        g "It is done. Go and spend today remembering. Tomorrow we will return to feast and celebrate."
        "And with that, it was over. The builder didn't look like he was going to keep working on the wall and the shamans left. Sabia had expected the orcs to snap back to normal, joking or fighting with each other as they returned."
        "Instead, they returned to camp in silence, many holding their stones tightly. Sabia joined them, having trouble shifting her thoughts from the strange ceremony."
        "She had a day left to relax before the closing ceremony, but wasn't sure how to spend it..."
    elif RGAarenascore >= 15:
        $ A_groknak += 2
        $ A_tekrok += 3
        $ A_rokgrid += 3
        $ A_dajrab += 2
        $ A_ylva += 2
        $ A_lutvrog += 1
        $ L_orcs += 6
        $ dom += 1
        $ sub += 1
        "After the chant was done, Sabia shifted impatiently, but it still wasn't over. Ylva stepped forward and raised her staff in front of her."
        ylva "All of you have honored the memory of our ancestors and earned a symbol of that honor. First, choose a tree to be your Memory of Redkor."
        "The orcs immediately surged for the trees and Sabia joined them awkwardly. To her surprise, the orcs took to the activity eagerly, trying to find the trees they thought would be biggest and strongest. They jockeyed for position a little, but didn't fight and were oddly respectful."
        g "Inscribe your name at the base of the tree to join your memory to our history. It will be planted outside the camp and grow strong, as you grow strong."
        "Sabia obeyed, now even more uncertain than before. Orcs planting trees? And viewing it as an honor? Yet they all seemed so solemn as they carved their names that Sabia felt like she knew less than at any moment since reaching the camp."
        "Some of the orcs departed at that time, giving their trees to the care of Ornshakar. But Ylva shook her head when Sabia started to go with them, so apparently it still wasn't over."
        ylva "Second, those of you who have endured to the end... come forward and take a symbol of the Memory of Aedre."
        "The orcs surged toward the builder as if they had been waiting for that moment. The old orc had taken down a section of the wall and left only a pile of rubble. Now he began handing out pieces of the stone."
        "Sabia's skepticism about the whole event was being worn down by how seriously the orcs took receiving their rocks. Normally she might joke to herself about orcs valuing rocks, yet she found herself accepting the stone carefully."
        "It was old and heavy, worn by time. Sabia weighed it in her hands as she and most of the other orcs were sent away. She kept running her fingers over it as she walked away."
        "Sabia headed back to camp - she had a day left to relax before the closing ceremony, but wasn't sure how to spend it..."
    elif RGAarenascore >= 10:
        $ A_groknak += 1
        $ A_tekrok += 2
        $ A_rokgrid += 2
        $ A_dajrab += 1
        $ A_ylva += 1
        $ A_lutvrog += 1
        $ L_orcs += 4
        "After the chant was done, Sabia shifted impatiently, but it still wasn't over. Ylva stepped forward and raised her staff in front of her."
        ylva "All of you have honored the memory of our ancestors and earned a symbol of that honor. First, choose a tree to be your Memory of Redkor."
        "The orcs immediately surged for the trees and Sabia joined them awkwardly. To her surprise, the orcs took to the activity eagerly, trying to find the trees they thought would be biggest and strongest. They jockeyed for position a little, but didn't fight and were oddly respectful."
        g "Inscribe your name at the base of the tree to join your memory to our history. It will be planted outside the camp and grow strong, as you grow strong."
        "Sabia obeyed, now even more uncertain than before. Orcs planting trees? And viewing it as an honor? Yet they all seemed so solemn as they carved their names that Sabia felt like she knew less than at any moment since reaching the camp."
        "Their trees were taken away, and at that time Sabia was dismissed along with some of the orcs. She found herself wondering what the other \"memories\" were, but went quietly since she didn't want to disturb the orderliness of the event."
        "Sabia headed back to camp - she had a day left to relax before the closing ceremony, but wasn't sure how to spend it..."
    elif RGAarenascore >= 5:
        $ A_groknak += 0
        $ A_tekrok += 1
        $ A_rokgrid += 1
        $ A_dajrab += 1
        $ A_ylva += 1
        $ A_lutvrog += 1
        $ L_orcs += 2
        "After the chant was done, Sabia and several other warriors were sent away. Sabia was irritated that she didn't get to find out what the builder and the trees were about, but it was probably just more orc nonsense."
        "Sabia headed back to camp - she had a day left to relax before the closing ceremony, but wasn't sure how to spend it..."
    jump lowerorccamp


label RGAmakhorintro:
    "The sound of a terrible roar shook Sabia from her sleep. She scrambled up to see what was happening, what could possibly make a noise that drowned out all the orcs and even the hellhounds."
    scene bg RGAmakhor0
    call sabiabase
    show sabiaemo surprised1 at left
    with dissolve
    "She reached the arena in time to see the monstrous creature, which for a moment simply astonished her. But slowly, as she took in the form, Sabia realized exactly what it was."
    s "There's no way it can be traditional to have a Makhor in the arena. They're far too rare, practically extinct..."
    show ylva happy1 at right
    show ylva2 arm2 at right
    with moveinright
    ylva "Oh, this is the first time I've ever heard of this happening! It's traditional to have some sort of grand spectacle, but this is something special!"
    show sabiaemo closed2 at left
    s "Surely they're not just going to fight it. A creature like that..."
    show ylva normal at right
    ylva "No, they won't kill or injure it. It's being brought to the council of shamans."
    show sabiaemo irritated1 at left
    s "And first they're letting a bunch of orcs use it for games? How does that make any sense?"
    show ylva normal at right
    ylva "I'm not sure about the details, but there's more to it than that. Makhor naturally have powerful magic that runs in cycles. They may need to exhaust that energy before it can be used."
    show sabiaemo angry2 at left
    s "Used? I can't believe you've found a Makhor and you're treating it like this..."
    show ylva angry1 at right
    ylva "And humans would do any better? Wouldn't you just kill it the first time it ate anything on your lands?"
    show sabiaemo angry1 at left
    s "Of course not! The royal family of Lundar has issued a decree that no Makhor are to be harmed. Any peasant who finds one and reported it would be granted a fortune!"
    show ylva normalnarrow at right
    ylva "Really?"
    show sabiaemo closed2 at left
    s "The Makhor is a noble creature, a symbol of Lundar! Of course we wouldn't just massacre it like some beast!"
    show ylva angry1 at right
    ylva "Like me."
    show sabiaemo sad1 at left
    s "Wait, Ylva, I didn't mea-"
    show ylva angry3 at right
    ylva "Oh, I think you said exactly what you meant."
    show sabiaemo sad2 at left
    s "..."
    show ylva angry1 at right
    ylva "Maybe Lundar was symbolically a Makhor back when it was a new nation trying to fight the entire world. Now, it's a bunch of savages clubbing every last Makhor to death."
    hide ylva angry1 at right
    hide ylva2 arm2 at right
    with moveoutright
    show sabiaemo closed2 at left
    s "..."
    s "(Well, I fucked that up... but I'm not sure what I should have done instead...)"
    menu:
        "Orcs will be a problem unless I start viewing them as allies":
            $ dom += 1
            $ freedom += 1
            show sabiaemo angry2 at left
            s "(If I want orcs to work under me, I need to think about these things more carefully. Human prejudices will only get in my way.)"
        "Orcs will be a problem unless I figure out how to manipulate them":
            $ dom += 1
            $ slavery += 1
            show sabiaemo angry2 at left
            s "(I guess I need to think about fragile orc egos, at least for now. Once I obtain more power I can give them what they actually deserve.)"
        "I need a softer touch if I'm going to have orcs as allies":
            $ sub += 1
            $ freedom += 1
            show sabiaemo sad1 at left
            s "(I feel bad about being so insensitive... if I'm going to work with orcs, I need to do better in the future.)"
        "I need a softer touch to effectively manipulate orcs":
            $ sub += 1
            $ slavery += 1
            show sabiaemo sad1 at left
            s "(Maybe some female orcs deserved that, but not Ylva... I feel bad now, I need to do better to pull this off...)"
    show sabiaemo closed2 at left
    s "(On a practical level, I didn't find out what they're planning to do with the Makhor. Most likely it will be part of the event tomorrow, too.)"
    s "(I guess all I can do is prepare in a general way and hope it's enough.)"
    return


label RGAmakhorchallenge1:
    $ RGAobservedmakhor = True
    $ A_ylva += 2
    "After the argument with Ylva, Sabia hadn't wanted to talk to her, and thus hadn't gained any specific information about what the event involving the Makhor would be. She collected her equipment and headed to the arena to find out."
    scene bg RGAmakhor0a
    call sabiabase
    with dissolve
    "She discovered that the preparations had already been made, the arena blocked off by new gates to prevent the Makhor from escaping. The animal itself was sitting in the center of the arena, very still."
    "When she had been a child, Sabia had played with a carved wooden Makhor and always thought it looked impressive. Seeing one in real life was simultaneously wonderful and horrible."
    "Her first impression was that the Makhor was absolutely massive. Its muscular forearms were larger than her entire body - compared to them, she and the largest orc were equally weak. Though it wasn't moving, she could tell that real power coursed through its body."
    "The characteristic spikes from the head, the broad mane, the proud tail... it was a majestic beast."
    show sabiaemo sad1 at left
    "But the Makhor had obviously been poorly treated. There were recently healed wounds on its hide, its mane was unkempt, and there was a strange look in its eyes. They shifted around, unfocused. Was the Makhor drugged? Sabia had no other way of explaining why it was staying in the center of the arena instead of tugging on its chains."
    "Keeping her distance, Sabia shifted around to get a better view. From the stands, she was able to see that the Makhor wasn't just sitting: it was curled around something. She peered closer and saw that it was crouched around a large pile of bones."
    "The remains of food? The corpses of orcs that had gotten too close? Sabia's best guesses fell away as she noticed that the bones looked old, and some of them were much larger than even herd animals it might have been fed."
    ylva "They're Makhor bones."
    show ylva closedsad at right
    show ylva2 arm1 at right
    with moveinright
    "Ylva's voice came softly from behind Sabia, startling her. She managed to suppress her reaction, saying nothing as the orc shaman came up to stand beside her. They watched in silence as an orc got too close and the Makhor snapped at it, then retreated to the pile."
    s "You seem surprised."
    ylva "I knew they captured the Makhor in the lands south of here, but I didn't know how."
    show ylva sad at right
    ylva "They lured it into a trap with the bones of a dead Makhor. Shamans revived the scent so that this one believed it was alive, then they fell upon it when it came close."
    show sabiaemo closed2 at left
    s "..."
    show ylva angry1 at right
    ylva "I see you're swallowing your comments about our brutishness."
    show sabiaemo sad1 at left
    s "I'm not. Honestly, I'm just feeling sorry for it... those are the same bones, right? It's protecting them?"
    show ylva sad at right
    ylva "I'm not sure what it thinks. They drugged it heavily to try to make it more docile, so it may be confused and disoriented now. But I also think Makhor may mourn their dead."
    show sabiaemo closed2 at left
    s "I don't mean this to cause offense, but... why do they have to do all this?"
    ylva "I don't know. Vek always said that the Makhor was the key to our future, that we needed to study them."
    show ylva normal at right
    ylva "As for the drugs... Makhor are too intelligent to be easily held captive. On top of that, they have some kind of transformation magic that's not really understood. There has to be a way to neutralize it, or it would change size and escape the shackles and kill everyone nearby."
    show sabiaemo angry1 at left
    s "It doesn't look like it wants to hurt anyone to me. It just wants to be left in peace with the bones of its friend."
    show ylva sad at right
    ylva "..."
    show sabiaemo closed2 at left
    s "You know this is cruel, don't you? Surely you won't deny it."
    show ylva closedangry at right
    ylva "I... believe that sometimes sacrifices are necessary for the greater good. But..."
    show ylva sad at right
    ylva "The challenge will be for teams to steal the bones from the Makhor. All weapons are permitted."
    show sabiaemo sad1 at left
    s "Oh..."
    show sabiaemo closed2 at left
    s "You already know what I think of this. But you didn't have anything to do with it, did you?"
    ylva "..."
    show sabiaemo sad1 at left
    "Beneath them, the Makhor released a rumbling growl. Yet realizing the beast's position, Sabia realized that it sounded more pained than anything. It was alone and confused and possibly grieving, if an animal could do such a thing."
    "While Sabia watched, the Makhor picked up one of the bones and rubbed its face against it with a low whine. Though its arm ended in an enormous claw, it was surprisingly agile, able to grasp the bone almost like a human. The sight of that hand gripping the bones of the dead Makhor hit Sabia and she winced."
    "Part of her tried to convince herself that it was just an animal. And that was true. There were more important matters in the broad scheme of things. But still..."
    ylva "I shouldn't tell you this, but... most of the successful teams will be using weapons lined with poison from the dead Makhor. A great deal was harvested from the dead Makhor's tail."
    s "I see. That's the \"solution\" to this trial, is it?"
    ylva "Without that, drawing close to it would be suicidal. And yet, I can only imagine what it must think, to feel that poison..."
    show sabiaemo angry1 at left
    s "I don't suppose I can refuse to participate?"
    show ylva closedsad at right
    ylva "You could, but..."
    show sabiaemo closed2 at left
    s "It would reflect poorly on me. I know. There's nothing we can really do, is there?"
    ylva "..."
    show ylva normal at right
    ylva "I'm sorry, I need to go."
    hide ylva normal
    hide ylva2 arm1
    with moveoutright
    s "(I'm on my own, then.)"
    s "(Well, I'm not willing to sacrifice everything I've worked for just to help the beast. But... maybe I could finish the trial without harming it so much. It would be a risk, but...)"
    show sabiaemo normal at left
    s "(I can't let this opportunity pass me by. Letting the orcs get information from the Makhor is unacceptable, and if I could get information about it... that could even be a good bargaining chip with my mother.)"
    s "(But how to proceed...?)"
    return


label RGAmakhorchallenge2:
    "When the day of the Makhor event finally came, Sabia went to the arena with a sense of grim inevitability. She didn't have much of a choice but to participate, and while she'd prepared, she hadn't come up with any brilliant solution."
    scene bg RGAmakhor1 with dissolve
    "The match went about like she had expected. The Makhor huddled in the center of the arena, trying to protect the bones, while the orcs harried it from all sides. Many of their blows glanced off the thick hide, but when one bit deep, the Makhor let out a moaning roar and convulsed with a surprising amount of pain."
    "One orc managed to retrieve a bone this time, rushing in and then scrambling away. The Makhor let out a pained roar and lunged after him, but was warded back by the others waving weapons."
    "It retreated back to the center of the arena, curling around the pile of bones and whimpering. The next blows to strike it also made it convulse, but the Makhor recovered more quickly this time."
    "When its jaws closed over an orc's head and crushed it, Sabia found herself cheering internally. She had to suppress that reaction, because as much as the orcs liked bloodshed, she doubted they'd appreciate her rooting for the monster."
    "The sight of the noble beast, surrounded by savages... once it would have been a clear metaphor to her, but now Sabia found herself more conflicted."
    "By the time the gong rang, only three orcs had succeeded in stealing one of the bones. There were only two more chances in the day, so it looked like this challenge might involve a lot of potential honor. Especially since Sabia didn't have anyone working with her on this one."
    scene bg RGAmakhor0d with dissolve
    "There was a long break in between matches, but Sabia remained in the arena, pondering. To her surprise, she saw Ylva emerge in the arena and prepare some concoction in a large basin of water. It was then pushed into range of the Makhor via a long spear."
    "The Makhor growled at it for a while, but it had drank nothing the entire day. After a time, it leaned forward and lapped up the liquid. The wounds on its body began to close slowly, presumably due to a potion mixed into the water."
    "So that was how they kept the three matches fair. It made Sabia wonder what else might be possible, but she was running out of time. She would have to compete next, potentially risking her life."
    "Sabia closed her eyes and sighed. What was she going to do?"
    menu:
        "Participate":
            $ Sabia.xp += 2
            $ RGAarenascore += 1
            "There wasn't really a choice - she couldn't undermine everything she'd done so far. Sabia headed down to the sands for the event."
        "Don't participate":
            $ A_kia += 1
            $ RGAarenascore -= 3
            $ makhorfightpeace = True
            "Shaking her head, Sabia pulled back. She knew backing out of the challenge would be bad for her reputation, but her heart wasn't into it. She didn't want to harm the poor Makhor."
            "Sabia left the arena without fanfare, trying to ignore the sounds of the Makhor crying out in pain and confusion."
            return
    if RGAmakhorpoison:
        "Sabia toyed with the small vial of poison in one hand as the event formally started. The poison greatly increased her chances, but it obviously caused the Makhor pain and distress..."
        menu:
            "Use the poison":
                $ RGAarenascore -= 1
                $ usedmakhorpoison = True
                $ RGAmakhorfight += 3
                $ A_kia -= 2
                "This was no time for half-measures. Sabia carefully coated the edge of her blade with the poison, careful not to get it on her skin."
            "Don't use it":
                "After considering for a long time, Sabia didn't use the poison. It was the kind choice, and she could only hope it wouldn't get her killed."
    scene bg RGAmakhor2 with dissolve
    "The orcs were gathering in the arena, trying to figure out their best approach. The Makhor was growling and snapping any time one of them started to get close, hunching up further as it realized it was under attack again. Sabia stepped up and took a deep breath."
    "It was too late to back down now. Sabia had considered trying to do this without harming the Makhor, but seeing it looming over her made that seem foolish. She didn't have long to make her choice..."
    if Inventory.has_item(Silverblade) > 0 or Sabia.weapon == Silverblade:
        $ RGAmakhorfight += 1
    elif Inventory.has_item(Orcaxe) > 0 or Sabia.weapon == Orcaxe:
        $ RGAmakhorfight += 1
    if Inventory.has_item(Heavyleatherarmor) > 0 or Sabia.armor == Heavyleatherarmor:
        $ RGAmakhorfight += 2
    if RGAdodgetraining == True:
        $ RGAmakhorfight += 2
    if Sabia.level >= 5:
        $ RGAmakhorfight += 1
    if Sabia.con >= 2:
        $ RGAmakhorfight += 1
    if Sabia.maxstamina >= 280:
        $ RGAmakhorfight += 1
    if Sabia.stamina >= 200:
        $ RGAmakhorfight += 1
    menu:
        "Attack as much as necessary":
            $ RGAmakhorfight += 6
            $ A_kia -= 1
            $ dom += 1
            $ RGAwonbone = True
            "Sabia drew her sword and charged, vowing to set aside her feelings and do as much damage as she needed in order to win."
            "The orcs stared in surprise as she advanced alone, the Makhor's attention soon shifting to her. It certainly seemed insane, but she needed to do this herself. Hopefully she wouldn't just provide a distraction for others to take advantage of."
            "The Makhor lunged out, one enormous claw swiping where she had been a moment ago. But Sabia had watched carefully and knew it attacked like that - she ducked beneath and slashed the arm as it passed."
            "Reeling back in pain, the Makhor gave her a moment to get closer, almost reaching the pile of bones. But a moment later, its other claw came slamming down. She knew it was coming and dodged aside, but when it struck, the ground itself shuddered, making her lose her balance."
            if RGAmakhorfight >= 12:
                $ RGAarenascore += 3
                $ Sabia.stamina -= 100
                "Managing to keep her feet beneath her, Sabia was able to duck forward underneath a snapping bite and grab one of the bones from the pile. It was heavier than she expected, for a moment she feared that would be a fatal flaw, but then she managed to escape backward."
                "The Makhor made another attempt at her, crying in anguish, but she had enough time to react and then she was safely out of its range. The orcs in both the arena and the stands were staring at her."
                "Setting aside her doubts, Sabia gave a triumphant grin and raised her trophy over her head. They'd remember this one."
                "Of course, the match had to go on. All the other orcs still had time to steal a bone, and so the crowd's attention soon drifted from her. Just as well, because she was tired of it all."
                "As she left the arena, Sabia felt the bone becoming heavier and heavier. She would need to decide what to do about this..."
            elif RGAmakhorfight >= 9:
                $ RGAarenascore += 2
                $ Sabia.stamina = 0
                $ Sabia.hp = 1
                "Throwing herself to the side, Sabia just barely dodged the snapping bite. That got her close enough to the bones to grab one. It was heavier than she expected, for a moment she feared that would be a fatal flaw, but then she managed to escape backward."
                "Except that the Makhor's jaws were rushing toward her."
                "Sabia was able to throw herself back enough to avoid the deadly bite, but the Makhor's movement slammed its head into her. She still hadn't recovered from the pain when her back slammed into stone and she crumpled to the ground."
                "Knowing that everyone must be watching her, Sabia struggled through the pain. What the hell had happened? As she got up, aching all over, it slowly dawned on her."
                "The Makhor's blow had sent her flying like a toy, all the way until she slammed into one of the arena walls. Her sword lay in the sand half-way between them... but she was still gripping the bone she'd stolen tightly."
                "Though she wanted to lie down and whimper, Sabia forced herself to climb to her feet and raise the trophy over her head. The orcs cheered approvingly."
                "Of course, the match had to go on. All the other orcs still had time to steal a bone, and so the crowd's attention soon drifted from her. Just as well, because her body was going to give out soon."
                "As she left the arena, Sabia felt the bone becoming heavier and heavier, and not just because of her exhaustion. She would need to decide what to do about this..."
            else:
                "Sabia tried to dodge, but her footing was too unsteady. She barely even saw the Makhor's head lunge down, then there was only searing pain as it tore her apart."
                show gameover with dissolve
                pause 3
                $ renpy.full_restart()
        "Cause minimal injuries":
            $ RGAmakhorfight += 3
            $ A_kia += 0
            $ RGAwonbone = True
            "Sabia drew her sword carefully and advanced. She didn't want to cause unnecessary harm, but she wouldn't put her own life at risk."
            "The orcs stared in surprise as she advanced alone, the Makhor's attention soon shifting to her. It certainly seemed insane, but she needed to do this herself. Hopefully she wouldn't just provide a distraction for others to take advantage of."
            "The Makhor lunged out, one enormous claw swiping where she had been a moment ago. But Sabia had watched carefully and knew it attacked like that - she ducked beneath the slash and lunged forward."
            "Her movement seemed to surprise the Makhor, but it only paused for a moment before slamming its other claw down at her. This one Sabia barely dodged, her legs shaking as the shockwave ran through them."
            "The thick arm beside her was too good a target to ignore - Sabia cut as hard as she could, her blade scoring along the Makhor's arm. It reeled backward in pain, giving her enough time to reach the pile of bones."
            if RGAmakhorfight >= 12:
                $ RGAarenascore += 3
                $ Sabia.stamina -= 100
                "Managing to keep her feet beneath her, Sabia was able to duck forward underneath a snapping bite and grab one of the bones from the pile. It was heavier than she expected, for a moment she feared that would be a fatal flaw, but then she managed to escape backward."
                "The Makhor made another attempt at her, crying in anguish, but she had enough time to react and then she was safely out of its range. The orcs in both the arena and the stands were staring at her."
                "Setting aside her doubts, Sabia gave a triumphant grin and raised her trophy over her head. They'd remember this one."
                "Of course, the match had to go on. All the other orcs still had time to steal a bone, and so the crowd's attention soon drifted from her. Just as well, because she was tired of it all."
                "As she left the arena, Sabia felt the bone becoming heavier and heavier. She would need to decide what to do about this..."
            elif RGAmakhorfight >= 9:
                $ RGAarenascore += 2
                $ Sabia.stamina = 0
                $ Sabia.hp = 1
                "Throwing herself to the side, Sabia just barely dodged the snapping bite. That got her close enough to the bones to grab one. It was heavier than she expected, for a moment she feared that would be a fatal flaw, but then she managed to escape backward."
                "Except that the Makhor's jaws were rushing toward her."
                "Sabia was able to throw herself back enough to avoid the deadly bite, but the Makhor's movement slammed its head into her. She still hadn't recovered from the pain when her back slammed into stone and she crumpled to the ground."
                "Knowing that everyone must be watching her, Sabia struggled through the pain. What the hell had happened? As she got up, aching all over, it slowly dawned on her."
                "The Makhor's blow had sent her flying like a toy, all the way until she slammed into one of the arena walls. Her sword lay in the sand half-way between them... but she was still gripping the bone she'd stolen tightly."
                "Though she wanted to lie down and whimper, Sabia forced herself to climb to her feet and raise the trophy over her head. The orcs cheered approvingly."
                "Of course, the match had to go on. All the other orcs still had time to steal a bone, and so the crowd's attention soon drifted from her. Just as well, because her body was going to give out soon."
                "As she left the arena, Sabia felt the bone becoming heavier and heavier, and not just because of her exhaustion. She would need to decide what to do about this..."
            else:
                "Sabia tried to dodge, but her footing was too unsteady. She barely even saw the Makhor's head lunge down, then there was only searing pain as it tore her apart."
                show gameover with dissolve
                pause 3
                $ renpy.full_restart()
        "Try not to hurt the Makhor" if usedmakhorpoison == False:
            $ RGAmakhorfight += 0
            $ A_kia += 3
            $ RGAwonbone = True
            $ makhorfightpeace = True
            "Sabia drew her sword, but kept it held in a low defensive position. It might be risky, but she would see if she couldn't avoid harming the Makhor."
            "The orcs stared in surprise as she advanced alone, the Makhor's attention soon shifting to her. It certainly seemed insane, but she needed to do this herself. Hopefully she wouldn't just provide a distraction for others to take advantage of."
            "The Makhor lunged out, one enormous claw swiping where she had been a moment ago. But Sabia had watched carefully and knew it attacked like that - she ducked beneath the slash and lunged forward."
            "Her movement seemed to surprise the Makhor, but it only paused for a moment before slamming its other claw down at her. This one Sabia barely dodged, her legs shaking as the shockwave ran through them."
            "This would have been a perfect opportunity to inflict a wound - Sabia ignored it and instead tried to dart forward, reaching the bone pile but realizing that the Makhor was fully focused down on her."
            if RGAmakhorfight >= 9:
                $ RGAarenascore += 2
                "Throwing herself to the side, Sabia just barely dodged the snapping bite. That got her close enough to the bones to grab one. It was heavier than she expected, for a moment she feared that would be a fatal flaw, but then she managed to escape backward."
                "Except that the Makhor's jaws were rushing toward her."
                $ Sabia.stamina = 0
                $ Sabia.hp = 1
                "Sabia was able to throw herself back enough to avoid the deadly bite, but the Makhor's movement slammed its head into her. She still hadn't recovered from the pain when her back slammed into stone and she crumpled to the ground."
                "Knowing that everyone must be watching her, Sabia struggled through the pain. What the hell had happened? As she got up, aching all over, it slowly dawned on her."
                "The Makhor's blow had sent her flying like a toy, all the way until she slammed into one of the arena walls. Her sword lay in the sand half-way between them... but she was still gripping the bone she'd stolen tightly."
                "Though she wanted to lie down and whimper, Sabia forced herself to climb to her feet and raise the trophy over her head. The orcs cheered approvingly."
                "Of course, the match had to go on. All the other orcs still had time to steal a bone, and so the crowd's attention soon drifted from her. Just as well, because her body was going to give out soon."
                "As she left the arena, Sabia felt the bone becoming heavier and heavier, and not just because of her exhaustion. She would need to decide what to do about this..."
            else:
                "Sabia tried to dodge, but her footing was too unsteady. She barely even saw the Makhor's head lunge down, then there was only searing pain as it tore her apart."
                show gameover with dissolve
                pause 3
                $ renpy.full_restart()
    return


label RGAfinalritual:
    scene bg RGAbg
    call sabiabase
    with dissolve
    "After the Red God's Arena had consumed her waking hours for so long, the end felt anticlimactic. Sabia sat in the stands, surrounded by others, yet she barely noticed them or heard what was being said."
    "The rituals being done on the sands meant nothing to her. She didn't care about the feasting that took place. There was definitely no sense of camaraderie."
    "She'd done all of this for revenge?"
    "Sabia felt hollow."
    "No, the concept of revenge couldn't sustain her. She definitely planned to have her revenge, but this was about more than that. Her sister had eroded her base of support, and the whole experience had taught her just how lacking she was in many ways."
    "Before the betrayal had thrown her life off track, Sabia had wanted to make a name for herself. To guide Lundar to a better place. That was still her true goal."
    "And as bitter as her experiences had been, they'd made her stronger. There were many subjects she'd need to think about more clearly, and her old ideas about what Lundar should be felt simplistic to her now."
    "Exactly how far she could go, Sabia wasn't sure. Yet as the rituals officially ended, Sabia found herself smiling."
    if orcalliance == "tekrok":
        show tekrok normal at right with moveinright
        t "Come this way."
        s "What is it now?"
        t "Just come."
        scene bg HGNtekrok2
        call sabiabase
        show tekrok normal at right
        with dissolve
        "Sabia had been prepared for some sort of ridiculous demand, but to her surprise she was taken back to Tekrok's feast hall."
        if RGAarenascore >= 15:
            "She was even more surprised when she was met by a thunderous cheer. The orcs welcomed her with much backslapping and none of them even tried to grope her."
        elif RGAarenascore >= 5:
            "She was even more surprised when she was met by a raucous cheer. The orcs welcomed her with much backslapping and only a few tried to grope her."
        else:
            "She was even more surprised when she was met by a cheer. She thought it was for Tekrok at first, but apparently all warriors honored in the Red God's Arena received such a welcome. Many orcs still eyed her lustfully, but there was respect in their eyes as well."
        t "You... could have done worse, human. You must speak with Tekrok about what comes next... later. Go."
        "With that, he stomped away, leaving her to be pulled into the feast. The orcs were their usual loud, rough selves... yet she could sense that something had changed."
        "They saw her differently after the Red God's Arena. As she heard them speak about it, not just about the bloodshed but about the honors granted to the top warriors, Sabia realized that it was more than some primitive festival of bloodshed."
        "Exactly what she would do with that, Sabia wasn't sure. But she let herself relax a little and enjoy the feast."
        "Once she was full, Sabia left the hall and headed into camp, contemplating the questions that the celebrations had pushed aside."
        scene bg centralcamp
        call sabiabase
        with dissolve
        "Sabia knew she would have to deal with Tekrok's demands eventually, but she had always been aiming higher than just dealing with him. How was she actually going to proceed?"
    elif orcalliance == "rokgrid":
        show rokgrid happy2 at right with moveinright
        r "Sabia! Right this way!"
        s "Is something wrong?"
        r "Far from it! Everyone honored in the Red God's Arena is feasting now, and you deserve to be among them!"
        scene bg HGNrokgrid2
        call sabiabase
        show rokgrid happy2 at right
        with dissolve
        "Sabia had been prepared for some new task, but to her surprise, Rokgrid escorted her to his feast hall."
        if RGAarenascore >= 15:
            "She was even more surprised when she was met by a thunderous cheer. The orcs welcomed her eagerly, many coming forward to shake her hand in the human style and urging her to come and join them."
        elif RGAarenascore >= 5:
            "She was even more surprised when she was met by a raucous cheer. The orcs welcomed her eagerly, many coming forward to shake her hand in the human style."
        else:
            "She was even more surprised when she was met by a cheer. She thought it was for Rokgrid at first, but apparently all warriors honored in the Red God's Arena received such a welcome. Many orcs still eyed her lustfully, but there was respect in their eyes as well."
        r "You did well, Sabia. We have much work to do, but for today... relax and enjoy the honor you are due!"
        "With that, he headed to his own table, leaving her to be pulled into the feast. The orcs were their usual loud, rough selves... yet she could sense that something had changed."
        "They saw her differently after the Red God's Arena. As she heard them speak about it, not just about the bloodshed but about the honors granted to the top warriors, Sabia realized that it was more than some primitive festival of bloodshed."
        "Exactly what she would do with that, Sabia wasn't sure. But she let herself relax a little and enjoy the feast."
        "Once she was full, Sabia left the hall and headed into camp, contemplating the questions that the celebrations had pushed aside."
        scene bg centralcamp
        call sabiabase
        with dissolve
        "Sabia knew she would have to strike a clearer agreement with Rokgrid eventually, but she had always been aiming higher than just dealing with him. How was she actually going to proceed?"
    elif orcalliance == "dajrab":
        show dajrab normalclosed at right with moveinright
        d "All warriors aligned with me who gained honor in the Red God's Arena are feasting. You are welcome to join them."
        s "Another feast already? Well, alright."
        scene bg HGNdajrab2
        call sabiabase
        show dajrab normalclosed at right
        with dissolve
        "It seemed too easy after all the challenges, but to Sabia's surprise she was indeed taken to Dajrab's feasting hall."
        if RGAarenascore >= 15:
            "She was even more surprised when she was met by a thunderous cheer. Dajrab's orcs were reserved, but they gave her respectful nods and a few clasped her arm as she entered."
        elif RGAarenascore >= 5:
            "She was even more surprised when she was met by a raucous cheer. Many of the orcs gave her respectful nods."
        else:
            "She was even more surprised when she was met by a cheer. She thought it was for Dajrab at first, but apparently all warriors honored in the Red God's Arena received such a welcome. Many orcs still eyed her lustfully, but there was respect in their eyes as well."
        d "Tomorrow, the schemes and politics will begin again. For today, you can relax."
        "With that, Dajrab headed back out of the building, leaving her to be pulled into the feast. The orcs were their usual loud, rough selves... yet she could sense that something had changed."
        "They saw her differently after the Red God's Arena. As she heard them speak about it, not just about the bloodshed but about the honors granted to the top warriors, Sabia realized that it was more than some primitive festival of bloodshed."
        "Exactly what she would do with that, Sabia wasn't sure. But she let herself relax a little and enjoy the feast."
        "Once she was full, Sabia left the hall and headed into camp, contemplating the questions that the celebrations had pushed aside."
        scene bg centralcamp
        call sabiabase
        with dissolve
        "Sabia knew she would have to figure out Dajrab's angle eventually, but she had always been aiming higher than just dealing with him. How was she actually going to proceed?"
    else:
        scene bg centralcamp
        call sabiabase
        with dissolve
        if RGAarenascore >= 15:
            "Though pleased with herself, Sabia wandered into the center of camp with some uncertainty. To her surprise, many orcs gave her respectful nods and some even asked to look at the stone she had received, staring at it reverentially."
        else:
            "Though pleased with herself, Sabia wandered into the center of camp with some uncertainty. To her surprise, many orcs gave her respectful nods."
        "All of that felt odd, and it only exacerbated her central question: how was she actually going to proceed?"
    show sabiaemo closed2 at left
    "Soon she would need to move beyond the orc camp, but that still raised various problems. She could travel on her own, but her ability to enforce her will once she arrived was limited."
    show sabiaemo irritated2 at left
    "It was a vexing problem, and Sabia found herself irritated when several orcs wandered close to her. Yet instead of snapping at them, she looked up, and to her surprise, they seemed to be waiting for her."
    show orcbase at right
    show orcloincloth at right
    show orcaxe at right
    show orcnecklace at right
    show orcemo normal at right
    with moveinright
    orc "We're tired of sitting around camp. You may be human, but you're the first person to really shake things up."
    s "And...?"
    orc "You need muscles for something, right? We volunteer."
    show sabiaemo happy1 at left
    s "Is that so? Then keep your axes sharp, because I have some ideas..."
    "She managed to keep herself calm, but when Sabia headed back to her tent, she found herself grinning. Things were about to get more interesting."
    jump RGAmakhorending


label RGAmakhorending:
    scene bg sabiatent
    call sabiabase
    with dissolve
    "Though Sabia would have been happy to sleep for a week to recover from the Red God's Arena, she found her instincts forcing her awake. There was someone outside her tent..."
    show ylva normal at right
    show ylva2 arm1 at right
    with moveinright
    if A_ylva >= 10:
        show ylva closednormal at right
        "Though Sabia hadn't expected Ylva to enter her tent, she was glad to see the shaman. The other woman seemed subdued, but focused on something."
        ylva "Sabia... there's something we need to do, and I need your help."
        show sabiaemo happy1 at left
        s "What is it? I'll do what I can!"
        show ylva normal at right
        ylva "It's about the Makhor. I agree with what you said - it shouldn't be in captivity like this."
    elif A_ylva >= 3:
        show ylva closedsad at right
        "To Sabia's surprise, Ylva entered her tent. It was odd, but the orc shaman seemed to have a specific purpose."
        ylva "I'm not sure if you'll hear me out on this, but... I hope you will. I don't have many options."
        s "I'm willing to hear you out. What is it?"
        show ylva normal at right
        ylva "It's about the Makhor. I agree with what you said - it shouldn't be in captivity like this."
    else:
        show ylva angry1 at right
        "To Sabia's shock, Ylva entered her tent. She gave a brief scowl, but she seemed subdued."
        ylva "I don't like you, but... I don't know who else to turn to and I can't do this alone."
        show sabiaemo closed2 at left
        s "Hmph, I'll at least hear you out."
        show ylva normal at right
        ylva "It's about the Makhor. I agree with what you said - it shouldn't be in captivity like this."
        show sabiaemo sad1 at left
        s "Oh..."
    ylva "I'm not sure what the council of shamans needs the Makhor for, but I have my doubts that this is truly in accordance with the spirits. I trust Behar Vek absolutely, but many others are politicians who may have ulterior motives."
    show sabiaemo normal at left
    s "Sounds familiar. So what are we going to do about it?"
    ylva "You saw the potion I used to keep the Makhor healthy? It was also supposed to have an agent derived from their poison that dulled the mind... but I have been changing the ingredients."
    show ylva closednormal at right
    ylva "The Makhor is much healthier than it is supposed to be now, and its mind less clouded. Tonight, we have a chance to make it look like it escaped its bonds."
    show sabiaemo surprised1 at left
    s "Oh!"
    show sabiaemo closed2 at left
    s "I don't want to see it harmed either, but won't it just kill us once it's free?"
    show ylva normal at right
    ylva "...I hope not. I've been near it, Sabia, and I think it's much smarter than anyone has given it credit for. Smarter than any animal I've ever worked with."
    s "(I think I have to take this chance. The council of shamans can't be allowed to get the Makhor, and having it free could be an advantage for me. The risk is high, but...)"
    show sabiaemo happy1 at left
    s "Alright, I'll do it! What do you need from me?"
    scene bg sabiatent
    with dissolve
    if RGAwonbone == True:
        "As they left the tent, Sabia grabbing her prize from earlier, Ylva explained that the Makhor was mostly healthy, but the chains still kept it bound. They needed to give it a special potion that would help restore its natural magic, but it had to be delivered directly, not diluted in water."
    else:
        "As they left the tent, Ylva explained that the Makhor was mostly healthy, but the chains still kept it bound. They needed to give it a special potion that would help restore its natural magic, but it had to be delivered directly, not diluted in water."
    "So she was going to get even closer to the beast than before. Hopefully this wasn't a mistake..."
    scene bg RGAkia0 with dissolve
    "For the night, the Makhor had been chained up in one corner of the arena. The reinforced black steel chains fit tight and looked tough, Sabia immediately understood why Ylva hadn't considered trying to break them. Even magic might have a hard time with chains like that - the orcs weren't taking any chances."
    "Of course, the bigger problem was the Makhor itself. Though it appeared to be sleeping fitfully, when they approached its eyes winked open, shining in the night as if lit by some inner fire."
    ylva "Hello again... do you remember me?"
    "At the sound of Ylva's voice, the Makhor released a heavy breath. Much less aggressive than it had ever been in the past... but then its nose twitched, its eyes focused on Sabia and it let out a low growl."
    "Sabia froze on instinct, though they were still outside the beast's range. If Ylva was already on good terms with it, why had she even asked Sabia to come? Just as Sabia was about to say the same, she saw how still Ylva was holding herself."
    "The orc shaman might be ambitious, but she was still young. Far from invincible. Though she carried herself well, it was a very different thing to imagine approaching a nearly legendary beast. Not to mention going against her own people."
    "She could take the lead, then. Sabia stepped a little closer to the line of claw marks in the sand, swallowed, and tried to speak in a soothing voice."
    if makhorfightpeace == True:
        if RGAwonbone == True:
            s "Come on, big guy... I didn't hurt you at all, remember? Surely that's worth something..."
            "The Makhor gave no sign that it understood her at all and continued growling. Which was really what she should have expected. Sabia hesitated, then decided she had to do it."
            s "I'm sorry I took this from you, okay? Can I give it back?"
            "Sabia revealed the bone she had won in the contest. The monstrous creature froze for a moment, sniffed a few times, then settled low on the ground. It could have been a less aggressive posture... or preparing to pounce."
            "Deciding not to risk it, Sabia tossed the bone onto the sand just in front of the Makhor. It sniffed suspiciously, waited a moment, then abruptly snatched the bone closer."
            "Clutching the bone, the Makhor gave a low whine and rubbed it against its face. Now that it wasn't enraged and its eyes looked clearer, Sabia was sure that she saw real sorrow there."
        else:
            s "Hey, hey... calm down... we're not here to hurt you..."
            "The Makhor gave no sign that it understood her at all and continued growling. Which was really what she should have expected."
    else:
        if RGAwonbone == True:
            s "Sorry, big guy... I didn't want to hurt you, but I didn't have a choice..."
            "The Makhor gave no sign that it understood her at all and continued growling. Which was really what she should have expected. Sabia hesitated, then decided she had to do it."
            s "I'm sorry I took this from you, okay? Can I give it back?"
            "Sabia revealed the bone she had won in the contest. The monstrous creature froze for a moment, sniffed a few times, then settled low on the ground. It could have been a less aggressive posture... or preparing to pounce."
            "Deciding not to risk it, Sabia tossed the bone onto the sand just in front of the Makhor. It sniffed suspiciously, waited a moment, then abruptly snatched the bone closer."
            "They waited as the Makhor gave a low whine and rubbed the bone against its face. Now that it wasn't enraged and its eyes looked clearer, Sabia was sure that she saw real sorrow there."
        else:
            s "Hey, hey... calm down... we're not here to hurt you..."
            "The Makhor gave no sign that it understood her at all and continued growling. Which was really what she should have expected."
    "As they watched, the Makhor settled lower in the sand of the arena, watching them quietly. Though from a distance its eyes had glowed ominously, now they no longer caught the light in the same way. They were large and... strangely soft."
    "Staring at the beast before her, Sabia felt that it must understand her on some level. Even domestic animals could comprehend human emotions, but when she stared into the Makhor's eyes, Sabia thought she saw something much deeper there."
    s "I... Ylva, I think you should feed it the potion directly."
    ylva "Me? I... thought you would throw it into its mouth, or something..."
    s "I think it understands how it's been mistreated... it might be smart enough to spit it out."
    ylva "Do you think it's smart enough to pretend to be calm, then hurt us once we get close?"
    "That idea had definitely occurred to Sabia, but she'd hoped that Ylva wasn't thinking so suspiciously. Still, she thought it was unlikely. The Makhor seemed too pure to deceive, to be anything other than the majestic beast that it was."
    s "It's possible. I'm not saying run up and hug it. But let's see what happens if we get closer."
    "With a little more encouragement from her, Ylva stepped closer. The Makhor got up slowly, then began padding toward them. After so many charging roars in the arena, it was scary to watch it move so silently."
    "When it finally got near to Ylva, both of them held their breath. Then, to Sabia's surprise, the Makhor lowered itself so that its head was against the ground and inched forward, as if trying not to tower over them."
    "If that had been a ruse, it might have worked, but fortunately the Makhor didn't seem malicious. Instead, when it reached Ylva, it..."
    "Bumped its face against her? The Makhor bumped into her so hard she nearly fell, then began rubbing back and forth. A low rumbling came from deep within its body, vibrating through Sabia, but she realized that it was a happy sound."
    ylva "Do you... remember me?"
    "Ylva did her best to embrace the enormous head, which continued to nearly knock her over in its rough display of affection."
    ylva "That's right, I just help heal you... I'm not here to hurt you..."
    "Slowly, Ylva slid the potion from a pack at her side. In her place, Sabia would have got it into the Makhor's mouth as soon as possible, but Ylva instead uncapped it and held it up near the Makhor's nose."
    "It drew back slightly in surprise, then pushed forward, sniffing the concoction. The breath from its nostrils was so forceful that Sabia could see Ylva's braids waving slightly. Fortunately, it seemed like the Makhor wasn't offended by the potion."
    ylva "This isn't working... I couldn't open its mouth even if I tried. Sabia, can you get the basin?"
    "At first that made no sense to her at all, then Sabia put it together. She ran to the side of the arena and quickly found the basin that had been used to give the Makhor water before. Whether or not this would work, she had no idea, but she was willing to cooperate."
    ylva "You need to drink this. Just like before. Do you understand?"
    "Ylva waved the vial and pointed at the basin. The Makhor's vast head swung back and forth between the two, then it blinked several times. After a moment it bumped into Ylva again and gave another rumbling purr."
    "Sabia sighed and shook her head. It did seem smart enough to understand they were trying to communicate, but it had no idea what they meant. This was probably a waste of time."
    "But it seemed Ylva wasn't willing to give up so quickly. After several more attempts, she gestured for Sabia to pull the basin closer."
    ylva "I have something else I want to try. Bring it over here."
    "Sabia wasn't so sure the Makhor would react to her as positively, but... she'd been the one to encourage Ylva to risk herself, it would be cowardice to refuse to do so herself. Sabia squared her shoulders and pulled the basin closer to them."
    if A_kia >= 3:
        "When Sabia drew closer the Makhor moved forward, bumping her lightly with its nose and taking a deep sniff. It then shifted back and returned to purring. That was a good sign, though Sabia still stood further away than Ylva once the basin was in position."
    elif A_kia >= 1:
        "The Makhor sniffed at her suspiciously, then after a moment it calmed down and just watched as she pulled the basin closer. Sabia got it in place then took a step back."
    else:
        "The Makhor gave an ominous growl and stared at her, but it didn't attack. Sabia pulled the basin close and then quickly retreated, not wanting to push her luck. It obviously held a grudge."
    ylva "We need you to drink this... it will help you."
    "Ylva poured the potion into the basin, forming a pool that looked pathetically small. The Makhor stared at it, stared at Ylva, and then cocked its head, uncomprehending."
    ylva "That's all there is this time... come on, drink it."
    "Just when Sabia was starting to think it was useless, the Makhor bent down and licked at the basin. The first lick must have taken most of the liquid, but it made the Makhor pause. It sat still for a moment, then began licking aggressively, all over the basin, sending it tumbling over the sands."
    "When all possible traces of liquid were gone, the Makhor began rumbling much louder. Its eyes nearly closed in an expression Sabia couldn't help but interpret as happy satisfaction. But that was all it did."
    s "Uh... what now?"
    ylva "I don't know... the injuries, confusion, and drugs were suppressing its magic, and we should have helped. But we don't know enough about the Makhor in the first place."
    s "Maybe it takes a while to have an effect? Should we let it sleep it off?"
    ylva "Based on what I was told, I didn't think so... but maybe you're right."
    "They moved away and the Makhor didn't object, lying there with its eyes half-closed. Sabia replaced the basin so that nothing would look amiss, then returned to Ylva."
    ylva "If... if this doesn't work, what do we do?"
    if A_ylva >= 5:
        s "We can try something else next. We're in this one together, right?"
        "Ylva cast her a slight smile of appreciation, as if she had still been uncertain. Sabia found that she didn't even mind seeing the other woman's fangs bared by that smile."
    else:
        s "Nothing. We made a good effort, but that doesn't mean we need to work together again."
        "Ylva cast her a sad glance, but nodded. They might not be enemies, but they were very far from friends."
    scene bg RGAkia1
    call shake ("v")
    "Just when it seemed like Ylva was about to say something, a pulse of power passed through them both. It was like nothing Sabia had ever felt before - like magic, yet it was far stranger than the difference between human and orc magic."
    scene bg RGAkia2
    call shake ("v")
    "They looked back to find the Makhor's body shifting and shrinking on itself, colors bleeding into the air and swirling slowly as it changed..."
    scene bg RGAkia3
    call shake ("v")
    call shake ("h")
    "Into the shape of a woman? Sabia had a moment to glimpse a feminine form with a spiked tail and a mane of hair like the Makhor. She looked down over herself, flexing her hands and rolling her shoulders."
    "Though her form was roughly human, there was something distinctly animal about her movements. Even just shifting her weight, she moved like a beast - and with a hint of the majesty of a Makhor."
    "Then, without warning, she burst into a flurry of movement, grabbing up the bones scattered around her. Once she had them all, she crouched low and then leapt high into the air."
    scene bg RGAkia4
    call shake ("v")
    "In a single bound it reached the top of the arena wall and crouched there, staring at both of them. Then with another leap it reached the top of one of the horns, then flashed away into the night like a shadow."
    scene bg RGAkia5 with dissolve
    "The two of them were left staring, wondering if they could actually have seen what they'd just witnessed. Yet the steel chains lay on the floor of the arena, empty."
    s "Did... did you know anything about that?"
    ylva "No... I had assumed that if the stories about it transforming weren't myths, they were just a small change of form... we speculated it could change its size..."
    s "Then..."
    ylva "This is fascinating... if the magic was so potent, it explains why they needed to keep her drugged and confused... but why wouldn't it have happened instinctually?"
    s "Ylva, we don't have time for this. We need to get the hell away from here before anyone suspects us."
    "Though it looked like Ylva might object, after a moment she nodded. With the chains undamaged and the locks binding them to the arena wall still locked, this would be hard to pin on anyone... but not if someone saw them."
    "They split up to avoid suspicion and headed back to their tents. The exhaustion from the tension and from the entire arena started to catch up to Sabia, yet though she was tired, she found herself wide awake."
    "She had gained the ability to travel away from the camp, but she had no idea where she was going to go next."
    scene bg black with dissolve
    pause 3
    call RGAlastsceneintro
    call RGAlastscene
    scene bg black with dissolve
    $ hentai_scene(1,"tyratalk",dissolve)
    show lynn1 at right
    with dissolve
    l "Are you finally done, Mother? I don't understand why you toy with our assets like that."
    ty "Pleasure can be a more effective tool than pain, Lynn. That's a lesson you need to learn better."
    hide lynn1 at right
    show lynn2 at right
    l "Maybe. What should I do with them?"
    ty "For the elf... I haven't decided yet. Cute little thing, I should give her to someone gentle."
    l "And the minotaur?"
    $ hentai_scene(4)
    hide lynn2 at right
    show lynn2 at right
    ty "Give him to Archmage Shannar, or whoever is supervising the work right now. That's all he's good for."
    hide lynn2 at right
    show lynn1 at right
    l "Very well, Mother. But are you sure we should be encouraging their faction?"
    ty "Thanks to that idiot minotaur's failing, we needed to rely on the Order of Relona to keep the minotaurs back. We need an edge soon, before that conflict goes hot."
    l "The conflict with the Order, you mean."
    $ hentai_scene(1)
    show lynn1 at right
    ty "Of course. Unless the Crown decides to make trouble, there are no other real concerns."
    l "I'll see it done, then, and be back to discuss our other plans."
    ty "Of course."
    $ hentai_scene(5,effect=dissolve)
    "Tyra was already looking back down to her papers, considering her other plans. She sent a brief surge of magic to clean the floor where she'd forced the two to fuck, then she forgot about it."
    play music orccamp fadeout 2.0 fadein 2.0
    scene bg black with dissolve
    pause 3
    jump raidingintro


label orccampphase2_end:
    $ orccampphase = 3
    scene bg centralcamp
    call sabiabase
    "For just a moment, Sabia thought she was back in the middle of the minotaur war."
    "There was a sense of tension and unease, a knot in her belly as she woke up. And the sounds of people in disarray."
    "But the moment passed, and she remembered where she was."
    "The camp was, however, in disarray."
    "As she parted the flaps of her tent, several orcs rushed by. Their faces were a mix of concern and confusion."
    "Two orcs straggled behind."
    show sabiaemo angry1 at left
    s "Hey! You two!"
    show GenericOrc1 at right
    show GenericOrc2 at center
    with moveinright
    show sabiaemo angry2 at left
    $ GenericOrc1.face = "angry"
    orc1 "What?!"
    show sabiaemo normalopen at left
    s "What's going on? The camp's a mess, everyone is distracted and hurried."
    show sabiaemo surprised1 at left
    $ GenericOrc2.face = "normalopen"
    orc2 "Camp under attack! Lundar coming!"
    show sabiaemo closed2 at left
    $ GenericOrc1.face = "normalopen"
    $ GenericOrc2.face = "suspicious"
    orc1 "No, you idiot. Not Lundar! Is filthy raiding Elves!"
    show sabiaemo annoyed2 at left
    $ GenericOrc2.face = "normalopen"
    orc2 "Elves? Why you think it's Elves?"
    $ GenericOrc1.face = "smile1"
    $ GenericOrc2.face = "suspicious"
    orc1 "'Cause when they get captured, we can fuck 'em and they might be as hot as Neve hahaha!"
    show sabiaemo normalopen at left
    s "...just because you want it to be Elves, doesn't mean it is Elves."
    $ GenericOrc1.face = "angry"
    orc1 "Hmph. Whatever, Orokgar going to make sure Orokgar ready for the tight Elves."
    $ GenericOrc2.face = "angry"
    orc2 "Not Elves, idiot!"
    hide GenericOrc1
    hide GenericOrc2
    with moveoutright
    show sabiaemo closed4 at left
    s "Well... I doubt it's either Lundar or Elves attacking Grok og Dar."
    show sabiaemo normalopen at left
    s "But there is certainly something happening. I'll need to look into this and find out what's going on. Quickly."
    if orcalliance == "sabia":
        s "I imagine one... or even all of the captains might know something about what's going on."
        s "Unfortunately I've made it clear that I don't want to ally with them."
        s "Maybe Jadk might know something...?"
    jump lowerorccamp
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
