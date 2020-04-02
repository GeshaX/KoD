






screen infohud(position):
    if position == "left":
        $ x = 0.01
        $ y = 0.01
    elif position == "center":
        $ x= 0.5
        $ y = 0.01
    frame align (x,y):
        background "battle/frame.png"
        has vbox
        null height 5
        hbox:
            null width 5
            bar:
                style "bar_hp"
                xmaximum 130
                value Sabia.hp
                range Sabia.maxhp
                left_gutter 0
                right_gutter 0
                thumb None
                thumb_shadow None
            null width 5
            text "[Sabia.hp] / [Sabia.maxhp]" size 16
        hbox:
            null width 5
            bar:
                style "bar_ep"
                xmaximum 130
                value Sabia.stamina
                range Sabia.maxstamina
                left_gutter 0
                right_gutter 0
                thumb None
                thumb_shadow None
            null width 5
            text "[Sabia.stamina] / [Sabia.maxstamina]" size 16
        hbox:
            null width 5
            text "Lundils: [money]"


screen lowerorccampscreen1:
    $ renpy.block_rollback()
    default mouse_clicked = False
    add "imagebuttons/orccamp1bg.png" xalign 0.0 yalign 0.0
    imagebutton auto "imagebuttons/sabiatent_%s.png" action [Hide("lowerorccampscreen1"), Jump("sabiahq1")] xpos 433 ypos 112 focus_mask True
    imagebutton auto "imagebuttons/centralcamp_%s.png" action [Hide("lowerorccampscreen1"), Jump("centralcamp1")] xpos 166 ypos 132 focus_mask True
    imagebutton auto "imagebuttons/silvertusk_%s.png" action [Hide("lowerorccampscreen1"), Jump("silvertusk1")] xpos 647 ypos 72 focus_mask True
    imagebutton auto "imagebuttons/traininggrounds_%s.png" action [Hide("lowerorccampscreen1"), Jump("traininggrounds1")] xpos 614 ypos 400 focus_mask True
    imagebutton auto "imagebuttons/kennels_%s.png" action [Hide("lowerorccampscreen1"), Jump("hellhoundkennels1")] xpos 0 ypos 100 focus_mask True
    imagebutton auto "imagebuttons/relieftents_%s.png" action [Hide("lowerorccampscreen1"), Jump("relieftents1")] xpos 0 ypos 512 focus_mask True
    imagebutton auto "imagebuttons/orcoutskirts_%s.png" action [Hide("lowerorccampscreen1"), Jump("eastern_frontier_map")] xpos 142 ypos 0 focus_mask True
    fixed at KeymapTransform([('mousedown_1', SetScreenVariable('mouse_clicked', True)), ('mouseup_1', SetScreenVariable('mouse_clicked', False))]):
        imagebutton idle "imagebuttons/upper_idle.png" hover ("imagebuttons/upper_clicked.png" if mouse_clicked else "imagebuttons/upper_hover.png") xpos 965 ypos 0 focus_mask True action [Hide("lowerorccampscreen1"), Jump("upperorccamp")]
    use infohud("center")



screen upperorccampscreen1:
    $ renpy.block_rollback()
    default mouse_clicked = False
    add "imagebuttons/orccamp2bg.png" xalign 0.0 yalign 0.0
    imagebutton auto "imagebuttons/mainhall_%s.png" action [Hide("upperorccampscreen1"), Jump("mainhall1")] xpos 0 ypos 0 focus_mask True
    imagebutton auto "imagebuttons/tekrok_%s.png" action [Hide("upperorccampscreen1"), Jump("tekroktent1")] xpos 597 ypos 333 focus_mask True
    imagebutton auto "imagebuttons/rokgrid_%s.png" action [Hide("upperorccampscreen1"), Jump("rokgridtent1")] xpos 0 ypos 456 focus_mask True
    imagebutton auto "imagebuttons/dajrab_%s.png" action [Hide("upperorccampscreen1"), Jump("dajrabtent1")] xpos 962 ypos 255 focus_mask True
    imagebutton auto "imagebuttons/tradinglodge_%s.png" action [Hide("upperorccampscreen1"), Jump("tradinglodge1")] xpos 223 ypos 370 focus_mask True
    imagebutton auto "imagebuttons/orctents_%s.png" action [Hide("upperorccampscreen1"), Jump("orctents1")] xpos 593 ypos 648 focus_mask True
    fixed at KeymapTransform([('mousedown_1', SetScreenVariable('mouse_clicked', True)), ('mouseup_1', SetScreenVariable('mouse_clicked', False))]):
        imagebutton idle "imagebuttons/lower_idle.png" hover ("imagebuttons/lower_clicked.png" if mouse_clicked else "imagebuttons/lower_hover.png") xpos 0 ypos 0 focus_mask True action [Hide("upperorccampscreen1"), Jump("lowerorccamp")]
    use infohud("center")


label lowerorccamp:
    scene bg black
    $ renpy.choice_for_skipping()
    while True:
        if orccampphase == 1:
            show screen lowerorccampscreen1
        elif orccampphase == 2:
            show screen lowerorccampscreen2
        elif orccampphase == 3:
            show screen lowerorccampscreen3
        $ renpy.pause(hard=True)


label upperorccamp:
    scene bg black
    $ renpy.choice_for_skipping()
    while True:
        if orccampphase == 1:
            show screen upperorccampscreen1
        elif orccampphase == 2:
            show screen upperorccampscreen2
        elif orccampphase == 3:
            show screen upperorccampscreen3
        $ renpy.pause(hard=True)





label sabiahq1:
    scene bg sabiatent
    show screen infohud("left")
    call sabiabase
    $ renpy.block_rollback()
    if sabiahq1intro == False:
        $ sabiahq1intro = True
        s "This is a shitty tent, but I can use it to change and sleep."
        s "I deserve better than this, but I can't afford to waste anything on luxury. I'll tough it out as if I'm on the campaign trail until I get a base established."
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
            jump sabiahq1
        "Check progression":
            call progressionscreen
            jump sabiahq1
        "View world map":
            menu:
                "Geographical map":
                    $ worldmap = "maps/Aleria_with_names.jpg"
                "Colored countries":
                    $ worldmap = "maps/Aleria_with_colors.jpg"
            call screen worldmap
            jump sabiahq1
        "Rest":
            scene bg black
            if Sabia.stamina > 150:
                "Sabia wasn't too sleepy, but she lay down and, after tossing and turning for a while, managed to sleep."
            elif Sabia.stamina > 50:
                "Wanting to wake up fresh the next day, Sabia lay down and managed to get in a good night of rest."
            else:
                "Sabia lay down, exhausted, and was almost instantly asleep. Despite the roughness of the ground, she slept hard and woke up refreshed."
            $ Sabia.rest()
            $ trialtime += 1
            if trialtime == 5:
                hide screen infohud
                jump captainsintro
            if trialtime == 11:
                "Sabia was woken up by orcs shouting about something. She got outside too late to see it happen, but it sounded like several orcs had been declared guilty and been executed."
                "The fate of a few orc vermin didn't matter to her, but it was a grim reminder that the trial continued while she worked. They needed her to end it, but that didn't mean it had stopped."
                "Not that it changed what Sabia had to do. All she could do was keep preparing."
            if trialtime == 18:
                "When Sabia woke up, she discovered a large number of orcs were arguing about whether or not a specific orc would be executed for treason that day. Apparently the trial was about to move forward again - if she wanted to get involved, she needed to act as soon as possible."
            if trialtime == 19:
                "Sabia woke to find the camp in a contentious mood. Apparently there was a lot of disagreement about the orc that had been executed that morning."
                "It was stupid of them to get so worked up about it now, when it was too late for them to do anything. Sabia scoffed under her breath and vowed to focus on the things within her power to change."
            if trialtime == 1:
                s "It's been [trialtime] day since I came to this filthy place."
            elif trialtime == 3:
                s "It's been [trialtime] day since I came to this filthy place. I'm really here for the long term..."
            elif trialtime >= 100:
                s "Holy shit, I've been here more than 100 days and still haven't joined the tribe? What the fuck am I doing with my life?"
            elif trialtime >= 19:
                s "It's actually been [trialtime] days... this place is starting to feel normal."
            elif trialtime >= 18:
                pass
            elif trialtime >= 12:
                s "I've been living in the orc camp for [trialtime] days."
            elif trialtime >= 6:
                s "It's been [trialtime] days since I arrived."
            elif trialtime >= 1:
                s "It's been [trialtime] days since I came to this filthy place."
            else:
                s "It's been [trialtime] days since I came here."
            hide screen infohud
            jump lowerorccamp
        "Back to camp":
            hide screen infohud
            jump lowerorccamp
    jump sabiahq1


label captainsintro:
    "Orc voices jolted Sabia from her sleep. She would have leapt up, but her waking left her lethargic, and in that moment she remembered what had happened to her. No, fighting would be useless."
    "Besides, the voices weren't angry, they seemed to be discussing something calmly. Sabia pretended to shift in her sleep and opened her eyes just a sliver to see who was standing outside her tent."
    scene bg centralcamp
    show rokgrid normal at left
    show tekrok normal at center
    show dajrab normalclosed at right
    with dissolve
    "To her shock, she immediately saw three of the largest orcs she had seen so far. They weren't looking at her at the moment, but it was clear they had come to see her. Sabia lay still and tried to keep her breathing under control."
    show dajrab normal at right
    d "You two aren't going to give me a moment's peace, are you?"
    show tekrok angry2 at center
    t "You're the one who came to inspect the human slut. What are you scheming, Dajrab?"
    show dajrab normalclosed at right
    d "Dajrab is merely curious as to why she remains."
    show tekrok happy1 at center
    t "Sure you are."
    show rokgrid normalclosed at left
    r "They say that she is working in the camp. It is indeed quite unusual, for one who was allegedly so highly ranked."
    show tekrok angry2 at center
    t "\"They say\" - is that what you're going with? We all know you're behind this."
    show rokgrid happy2 at left
    r "To the contrary, Tekrok, I had heard nothing about her until just recently. Though her cooperativeness so far does make one think that perhaps further cooperation is possible."
    show tekrok happy2 at center
    t "You're a fucking idiot, Rokgrid. If anything, she's staying to spy on us."
    show dajrab normalclosed at right
    d "Dajrab is not sure we have enough evidence to decide either way."
    show rokgrid happy3 at left
    r "Ah yes, evidence is indeed the question here. If anyone could tell us more about the rogue war party, it might be her."
    show tekrok angry2 at center
    t "Is that your scheme, then? You're delaying the trial so you can coach some pet human to support you?"
    show rokgrid happy5 at left
    r "Delay? Far from it, I merely hope to ensure that justice is done. So many soldiers were drawn in, after all, many of the accusations must be spurious."
    show tekrok angry1 at center
    t "We all know you sent that party, you bastard. The only question is if you'll slip out of it."
    show rokgrid happy3 at left
    r "We all know, do we? We'll see what the Warchief knows once he's seen all the evidence."
    show dajrab normalopen at right
    d "...she is awake."
    show dajrab normal at right
    s "!!!"
    show tekrok angry2 at center
    t "Fah, disgusting creature. Tekrok wants nothing more to do with this."
    hide tekrok angry2 with moveoutleft
    show rokgrid happy2 at left
    r "Good morning, human. We apologize for disturbing your slumber."
    s "..."
    show rokgrid happy3 at left
    r "Perhaps at another time we can speak further, yes? I bid you good day."
    hide rokgrid happy3 with moveoutleft
    show dajrab normalclosed at right
    d "..."
    hide dajrab normalclosed with moveoutright
    s "..."
    call sabiabase
    s "(Well, I obviously got their attention. Now I just have to hope that's a good thing.)"
    show sabiaemo closed1 at left
    s "(I thought this might be easy, but there are clearly more political games going on here than I would have expected. This is no ordinary orc camp.)"
    show sabiaemo normal at left
    s "(Despite their bluffing, I think Neve was right: they need me as evidence. I just wish I knew more about the Captains. Perhaps I can learn more in camp.)"
    s "(The Captains are probably my best way of getting ahead, but I should be very careful how I approach them...)"
    $ captainsintro = True
    $ a_list.append("Dajrab")
    $ a_list.append("Tekrok")
    $ a_list.append("Rokgrid")
    jump lowerorccamp


label centralcamp1:
    scene bg centralcamp
    $ renpy.block_rollback()
    if trashintro == True and workunlocked == False:
        s "(This place is still filthy. I should go sign up for cleaning duty on the other side of camp.)"
        jump lowerorccamp
    if trashintro == False:
        $ trashintro = True
        call sabiabase
        s "This place is absolutely filthy. I suppose I should have expected as much..."
        s "Then again, some areas of the orc camp are clean. Why is this one so disgusting?"
        show orcbase2 at right
        show orcloincloth2 at right
        show orchair2 at right
        show orcstomach2 at right
        show orcemo2 normalopen at right
        with moveinright
        orc "You don't like it, you clean it."
        show sabiaemo angry2 at left
        s "What? You presume to give {i}me{/i} an order?"
        show orcemo2 angry at right
        orc "Nope. It's just that everyone likes to bitch about it, but no one does a damn thing. Me tired of it."
        show sabiaemo annoyed1 at left
        s "Then isn't that your fault too? If you hate it, change something."
        show orcemo2 normal at right
        orc "Already have. There's money on the table for anyone willing to clean all this shit up - hell, me even give you some. But no one take it."
        menu:
            "But you won't clean it up yourself.":
                show orcemo2 normalopen at right
                orc "Me not a warrior, me an organizer. Need to have some pride in my job or never get any respect."
                show sabiaemo surprised2 at left
                s "Orcs have administrators?"
                show orcemo2 suspicious at right
                orc "..."
            "Doesn't reflect well on orcs, does it?":
                $ L_orcs -= 1
                show orcemo2 smile2 at right
                orc "Yeah, well, you don't see important humans cleaning anything either."
                s "Yes, but we hire maids instead of living in filth."
                show orcemo2 angry at right
                orc "Hmph. More like you have enslaved elves do your dirty work."
                show sabiaemo happy2 at left
                s "It's obvious having orcs do it wouldn't work, would it?"
                show orcemo2 suspicious at right
                orc "..."
            "If everyone dislikes it, why doesn't it stay clean?":
                $ L_orcs += 1
                show orcemo2 smile1 at right
                orc "Huh. Expected you to keep calling us disgusting pigs."
                s "I expected all of you to live like this, but the nicer parts of camp are actually pretty clean. I'm just trying to figure out the reason."
                show orcemo2 angry at right
                orc "It's because of this damn war camp. Everyone thinks temporary, no one cares. Except when they bitch about how dirty it is."
                show sabiaemo closed2 at left
                s "Hmm... a similar thing occurs with grazing lands in Lundar. Your problem would be solved if your Warchief owned the whole thing and commanded lesser orcs to manage it."
                show orcemo2 suspicious at right
                orc "Hmph. Orcs not like humans."
                show sabiaemo normal at left
                s "..."
        show orcemo2 normal at right
        orc "Well, whatever. You want to be paid to clean, have to sign up. Go to trading lodge."
        show sabiaemo pout2 at left
        s "(The very idea is disgraceful, but... I don't have a lot of options right now. If I have to claw my way to revenge one piece of trash at a time, I will.)"
        jump lowerorccamp
    menu:
        "Pick up trash (30 stamina)" if workunlocked:
            if Sabia.stamina >= 30:
                $ Sabia.stamina -= 30
                $ money += 1
                $ cleaningtimes += 1
                if cleaningtimes <= 3:
                    $ Sabia.stamina -= 30
                    "Unused to the manual labor, Sabia found herself much more tired than she had expected."
                    if Sabia.stamina >= 0:
                        "Sabia's inexperience consumed an additional 30 stamina."
                    else:
                        "Sabia's inexperience consumed an additional 30 stamina."
                        "Going beyond her limits left Sabia exhausted and she wondered if she would require several days to fully recover."
                if cleaningtimes == 3:
                    "After hard hours of work, Sabia received a single Lundil. She stared down at the coin in her hand, wondering how she had gotten so much dirt under her fingernails."
                    "This was miserable. And humiliating - no more than peasants' work."
                    "She was willing to do anything to get her revenge, but this would wear her down. How much longer could she subject herself to it?"
                    "At that moment, her thoughts were interrupted by an orc roaring in pleasure. She didn't want to see, but instinctively looked toward the relief tents."
                    "An orc had been fucking a woman's face, out in the open like a savage. He had just blown his load, and threw her some money before turning away, cock swinging."
                    "Sabia felt a moment of revulsion toward the prostitute... but also noticed just how much money had been thrown to the ground. The woman was collecting it swiftly, but... it was at least a dozen Lundils."
                    "She realized that she was gripping the single coin in her palm very tightly."
                    "The woman looked roughly used, but it seemed to have been over quickly. The orc just used her mouth, then paid so much money."
                    "Was she seriously considering it? As horrible as the idea seemed to her, Sabia realized that she could. It would be distasteful, but..."
                    "She was willing to do whatever it took to get her revenge. Even this."
                    $ reliefunlocked = True
                else:
                    "Sabia spent a while cleaning up trash and received 1 Lundil."
                    s "My hands are so filthy... this is beneath me..."
            else:
                "Sabia was too tired to clean."
            jump centralcamp1
        "Clean using broom (15 stamina)" if (workunlocked == True and Inventory.has_item(Broom) > 0):
            if Sabia.stamina >= 15:
                $ Sabia.stamina -= 15
                $ money += 1
                $ cleaningtimes += 1
                if cleaningtimes <= 3:
                    $ Sabia.stamina -= 30
                    "Unused to the manual labor, Sabia found herself much more tired than she had expected."
                    if Sabia.stamina >= 0:
                        "Sabia's inexperience consumed an additional 30 stamina."
                    else:
                        "Sabia's inexperience consumed an additional 30 stamina."
                        "Going beyond her limits left Sabia exhausted and she wondered if she would require several days to fully recover."
                if cleaningtimes == 3:
                    "After hard hours of work, Sabia received a single Lundil. She stared down at the coin in her hand, wondering how she had gotten so much dirt under her fingernails."
                    "This was miserable. And humiliating - no more than peasants' work."
                    "She was willing to do anything to get her revenge, but this would wear her down. How much longer could she subject herself to it?"
                    "At that moment, her thoughts were interrupted by an orc roaring in pleasure. She didn't want to see, but instinctively looked toward the relief tents."
                    "An orc had been fucking a woman's face, out in the open like a savage. He had just blown his load, and threw her some money before turning away, cock swinging."
                    "Sabia felt a moment of revulsion toward the prostitute... but also noticed just how much money had been thrown to the ground. The woman was collecting it swiftly, but... it was at least a dozen Lundils."
                    "She realized that she was gripping the single coin in her palm very tightly."
                    "The woman looked roughly used, but it seemed to have been over quickly. The orc just used her mouth, then paid so much money."
                    "Was she seriously considering it? As horrible as the idea seemed to her, Sabia realized that she could. It would be distasteful, but..."
                    "She was willing to do whatever it took to get her revenge. Even this."
                    $ reliefunlocked = True
                else:
                    if cleaningtimes == 5:
                        $ Inventory.add_item(Firemoss)
                        "While cleaning, Sabia noticed a patch of fire moss underneath a bit of trash. She recognized it as a useful and somewhat uncommon ingredient, so instead of sweeping it away, she carefully gathered it."
                        "At the end of her work, she received 1 Lundil."
                    else:
                        "Sabia spent a while sweeping up trash and received 1 Lundil."
            else:
                "Sabia was too tired to clean."
            jump centralcamp1
        "Go back":
            jump lowerorccamp
    jump lowerorccamp


label silvertusk1:
    scene bg silvertusk
    $ renpy.block_rollback()
    if silvertuskintro == False:
        call silvertusk_intro
    menu:
        "Buy a drink":
            call sabiabase
            show sabiaemo closed1 at left
            s "(I've never been one for drinking alone, and I'm sure as hell not getting drunk in a bar full of orcs.)"
            jump silvertusk1
        "Talk to Jadk":
            call sabiabase
            show jadkbase at right
            show jadkemo closedhappy at right
            jadk "Pull up a stool, then!"
            menu silvertusk1_jadk:
                "Chat":
                    "Sabia and Jadk chatted about nothing in particular."
                    jump silvertusk1_jadk
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
                    jump silvertusk1_jadk
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
                        jump silvertusk1_jadk
                    else:
                        show jadkemo normal at right
                        jadk "No story behind it, Jadk just likes the name."
                        show sabiaemo closed1 at left
                        s "(That's the first thing he's said that sounds like a lie.)"
                        jump silvertusk1_jadk
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
                    jump silvertusk1_jadk
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
                    jump silvertusk1_jadk
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
                    jump silvertusk1_jadk
                "Why do orcs speak in third person?":
                    show jadkemo happy2 at right
                    jadk "Gwahaha, you should ask someone smarter than Jadk."
                    show jadkemo normal at right
                    jadk "For Jadk to say \"I\"... it would not be right. This is not our way."
                    show jadkemo happy2 at right
                    jadk "But some orcs speak like you humans, gwahaha! So don't listen to Jadk too much!"
                    jump silvertusk1_jadk
                "Where could I find venomnettle?" if nettlequest == False:
                    show jadkemo normal at right
                    jadk "Oh, Jadk bets it's growing all around the edges of camp, just poke around near the outskirts."
                    jadk "It's damn tough, though. You look like you got some muscle on ya, but you still might need something to help you out."
                    jump silvertusk1_jadk
                "Go back":
                    jump silvertusk1
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
                jump silvertusk1
            else:
                s "(I should harvest some venomnettle, Jadk might pay well for it.)"
                jump silvertusk1
        "Work at the bar (50 stamina)" if nettlequest == True:
            if Sabia.armor == Barmaidclothes:
                if Sabia.stamina >= 50:
                    $ Sabia.stamina -= 50
                    $ money += 4
                    $ bartimes += 1
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
                    jump silvertusk1
                else:
                    "Sabia was too tired to work at the bar."
            else:
                jadk "Sorry, as sweet as you look, you'll need an outfit that shows you're working at the bar..."
        "Go back":
            jump lowerorccamp
    jump lowerorccamp


label silvertusk_intro:
    $ silvertuskintro = True
    call sabiabase
    $ a_list.append("Jadk")
    "Sabia hadn't gone near the large, loud building yet, but decided she needed to investigate. When she got nearer, she was surprised to see it actually had a sign."
    "A lot of orcs couldn't read or write, but Sabia had learned their ugly script as a precaution during the war. The scratchings said \"Silvertusk's Bar\" - though no hand could make the ugly orc letters look good, these were at least carefully written."
    "When she entered, every eye in the bar turned toward her. There were a lot of orcs drinking at the rough tables, and as they stared at her Sabia began to wonder if she'd made a mistake."
    "Voice" "Well? Are you going to come in, or just stand there?"
    show jadkbase at right
    show jadkemo normal at right
    with dissolve
    "An old orc sat behind the main bar, and his call immediately drew attention. When he waved her in, most of the orcs returned to their drinks or conversations. Sabia steeled herself and headed toward him."
    jadk "Can't say this is the nicest bar, but Jadk likes to think anyone can drink here."
    s "So, does that make you Silvertusk?"
    show jadkemo closednormal at right
    jadk "You can read? Huh."
    show jadkemo closedhappy at right
    jadk "Anyway, this one's name is Jadk. Come on in!"
    s "Who is Silvertusk, then?"
    show jadkemo happy2 at right
    jadk "Nobody. It's just the name of the bar, gwahaha!"
    show sabiaemo eyebrow1 at left
    s "Huh. Did \"Jadik's Bar\" not sound right?"
    show jadkemo happy1 at right
    jadk "It's Jadk."
    show sabiaemo irritated2 at left
    s "Jadik?"
    jadk "Ja{i}dk{/i}."
    show sabiaemo closed4 at left
    s "...that's going to kill my throat, I think I'm just not going to try."
    show jadkemo happy2 at right
    jadk "Suit yourself, gwaha. You want a drink?"
    show sabiaemo normal at left
    s "Not now. But thanks, I guess."
    show sabiaemo annoyed2 at left
    s "(I wonder what the chances are he intends to drug me, or at least get me drunk. He seems nice enough... too nice, I can't trust him.)"
    show jadkemo normal at right
    jadk "So, what brings you here? Human women don't usually come wandering around here, Jadk thinks sure you understand, especially ones as good-looking as you."
    show sabiaemo normal at left
    s "You don't know who I am? The rogue band captured me."
    show jadkemo happy1 at right
    jadk "All that information is being kept locked up for the trial, so nope, that's news to Jadk. Good to know."
    show sabiaemo closed2 at left
    s "(Dammit, is he going to be telling people now? I've lost an advantage I didn't even realize I had... unless he's planning to blackmail me now. Shit, if h-)"
    show jadkemo closedsad at right
    jadk "Calm down. Jadk has seen eyes like yours before, so Jadk knows you probably won't believe him, but Jadk doesn't play those games. Jadk just runs the bar."
    show sabiaemo normal at left
    s "..."
    show sabiaemo closed1 at left
    s "I'm not really here to drink, but... do you need any help at the bar?"
    show jadkemo happy2 at right
    jadk "Oh, sure! But Jadk is thinking you mean help Jadk is willing to pay for, yeah?"
    show sabiaemo irritated2 at left
    s "Yes. Obviously."
    show jadkemo normal at right
    jadk "Hmm... well, Jadk likes to brew a bit of venomnettle into the beer, house specialty. But Jadk is getting a little old to be gathering it anymore..."
    show sabiaemo normal at left
    s "Venomnettle? I only know it as a weed... and a hard one to deal with."
    show jadkemo closedhappy at right
    jadk "Oh, sure, it's a real pain. But it's got just the right bite if you know how to work it."
    s "And you'll pay for it?"
    show jadkemo happy2 at right
    jadk "Hell, for a sweet little thing like you, Jadk will throw in some extra!"
    show sabiaemo at left
    s "Good. I'll see what I can do."
    return


label traininggrounds1:
    scene bg traininggrounds
    $ renpy.block_rollback()
    if traininggroundsintro == False:
        $ traininggroundsintro = True
        call sabiabase
        "When Sabia began to wander toward the fenced-in training area, she found her way quickly blocked by several massive orcs. They didn't even bother to say anything, just getting in her way sent a clear enough message."
        "Just as she was about to back away, to her surprise she saw a familiar orc turn and see her."
        show lutvrogbase at right
        show lutvrogaxe at right
        show lutvrogwraps at right
        show lutvrogwrists at right
        show lutvrogemo normal at right
        with dissolve
        lut "Let her through. This is the one Lutvrog met."
        "The orcs moved to comply - not quite like they were following orders, Sabia thought, but simply because they respected the orc. Despite herself, she remembered his name."
        lut "You recover quickly, human."
        if startcondition == "sex":
            show sabiaemo annoyed1 at left
            s "No thanks to you, beating me like that."
            show lutvrogemo happy at right
            lut "It was a well-fought duel. Lutvrog wanted to save your equipment for you, but..."
        elif startcondition == "unconscious":
            show sabiaemo annoyed1 at left
            s "No thanks to your orcs, knocking me out like that."
            show lutvrogemo normal at right
            lut "It was the easiest way to deal with you. If it's any comfort, Neve was the one to change you and take your equipment."
        elif startcondition == "gangbang":
            show sabiaemo closed2 at left
            s "I saw you in the group that came afterward. I... suppose I should thank you for preventing them from doing worse to me."
            show lutvrogemo happy at right
            lut "Lutvrog regrets that he did not arrive earlier. Your equipment..."
        show sabiaemo normal at left
        s "Where exactly is my equipment now?"
        show lutvrogemo normal at right
        lut "Seized by the warriors investigating the incident. When the trial is over, some of it may be given as loot, but you're not likely to see it again."
        show sabiaemo irritated1 at left
        s "(Tch... that equipment had strong enchantments, I won't be able to replace it easily.)"
        lut "Now, are you here to say hello, or did you want to use the training grounds?"
        show sabiaemo normal at left
        s "Is that what these are? I wondered."
        show lutvrogemo suspicious at right
        lut "We don't normally allow outsiders here, but... you're still here for a reason, aren't you?"
        show sabiaemo closed1 at left
        s "...yes. I want to be involved in the trial, s-"
        show sabiaemo normal at left
        show lutvrogemo normal at right
        lut "No need to say more. Lutvrog tries not to get involved in politics."
        s "I see. May I use the training grounds?"
        show lutvrogemo normalopen at right
        lut "Lutvrog will allow it, but is afraid no one will loan you any equipment. If you can find your own, at least a weapon, then Lutvrog is certain some here would be willing to train you."
        s "Understood."
        show lutvrogemo happy at right
        lut "If you are staying... Lutvrog looks forward to a match between us."
        jump traininggrounds1
    menu:
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
                jump traininggrounds1
            jump traininggrounds1
        "Purchase training":
            if gotanysword == True:
                menu:
                    "Purchase offensive training (50 Lundils, 50 stamina)" if orcattacktraining == False:
                        if Sabia.stamina < 50:
                            "Sabia was too tired to train."
                            jump traininggrounds1
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
                            jump traininggrounds1
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
                            jump traininggrounds1
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
                            jump traininggrounds1
                        if hunttrainingopen:
                            $ orchuntingtraining = True
                            $ Sabia.stamina -= 50
                            $ huntingcost -= 20
                            $ Sabia.maxstamina += 10
                            "Hunting Orc" "Ah, there you are. Normally only experienced hunters get this training, but I think you're close enough. Won't even charge you for it."
                            s "Thanks, I guess."
                            "Hunting Orc" "But in return I expect you to bring me back a lot of game, okay?"
                            "He took her out into the forest and they went on a surprisingly rigorous journey covering all the local animals and areas."
                            "As much as Sabia hated to admit it, the orc knew what he was doing as well as any human hunter. Since she had no choice but to work for her money now, she did her best to listen to everything he said."
                            "When they finally finished Sabia was tired, but felt a little stronger and much better able to hunt in the area."
                        else:
                            "To her surprise, the orcs just shook their heads. Apparently hunting was only for experienced members of the tribe."
                    "Don't train":
                        jump traininggrounds1
                jump traininggrounds1
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
                            "Examining it, Sabia realized that it was bottled vigor reeds. Orcs just chewed them, but she remembered them as being useful for potions. Something to keep for future use."
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
            jump traininggrounds1
        "Talk to Lutvrog":
            call sabiabase
            show lutvrogbase at right
            show lutvrogaxe at right
            show lutvrogwraps at right
            show lutvrogwrists at right
            show lutvrogemo normal at right
            with dissolve
            menu traininggrounds1_lutvrog:
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
                "Ask about equipment":
                    s "Is there any place around here I can get some decent equipment?"
                    show lutvrogemo normalopen at right
                    lut "Unfortunately for you, orc bands have a tradition of everyone bringing their own equipment."
                    show lutvrogemo normal at right
                    lut "You will be able to acquire equipment from the trading lodge, but Lutvrog would not call it decent."
                    lut "Better weapons and armor exist, but they are not on the market. You are better off finding a human merchant."
                    show sabiaemo closed2 at left
                    s "(That's not an option right now, though...)"
                "Ask about tribe's initiation rituals":
                    show lutvrogemo normalopen at right
                    lut "Before one can become a full member of the tribe, they need an official recommendation from one of the three Captains."
                    show lutvrogemo normal at right
                    lut "Usually this is obtained by family members. Given your situation, you will likely need to get a recommendation directly from one of them."
                    s "And what do the rituals themselves involve?"
                    show lutvrogemo normal at right
                    lut "Though we are forbidden to speak of specifics, every orc knows a few basics."
                    lut "There are three challenges you must complete. A challenge of skill, a challenge of combat, and a challenge of pain."
                    show sabiaemo closed3 at left
                    s "Hmm..."
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
                "Ask to spar" if Sabia.hp >= 1:
                    if lutvrogsex == True:
                        show lutvrogemo happy at right
                        lut "As much as Lutvrog enjoyed our... match, Lutvrog thinks we have sparred enough for now. You should focus on the trial."
                        jump traininggrounds1_lutvrog
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
                                jump traininggrounds1
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
                    jump traininggrounds1
                "Go back":
                    jump traininggrounds1
            jump traininggrounds1_lutvrog
        "Attempt the Membership Ritual" if triberec:
            show lutvrogbase at right
            show lutvrogemo normalopen at right
            lut "Hmm, it seems you do have permission to attempt the ritual. Under normal conditions, this would be done before the entire tribe, but it will be much smaller in your case."
            show lutvrogemo normal at right
            lut "Still, this is nothing to attempt trivially. Are you sure you want to attempt the ritual now?"
            menu:
                "Yes":
                    if Sabia.hp < 10:
                        lut "Though you may be prepared, you are rather weak at the moment. Get some rest first."
                        jump traininggrounds1
                    lut "Then Lutvrog can only wish you strength and focus in the challenges ahead."
                    jump orcmembershiptrials
                "Not now":
                    jump traininggrounds1
        "Go back":
            jump lowerorccamp
    jump lowerorccamp


label lutvrogprescene:
    call sabiabase
    show sabiaemo happy3 at left
    show lutvrogbase at right
    show lutvrogaxe at right
    show lutvrogwraps at right
    show lutvrogwrists at right
    show lutvrogemo normal at right
    with dissolve
    "Sabia stared down, surprised that she had won. True, Lutvrog wasn't fully equipped, and she hadn't done much damage, but she had still won."
    show lutvrogemo happy at right
    lut "Congratulations, Sabia. You have fought well."
    show lutvrogemo normal at right
    "Though Lutvrog returned to his feet and squared his shoulders, she noticed that he favored one leg and frowned. In the heat of the battle she hadn't even thought about potential injuries, but now she hoped she hadn't hurt him."
    show sabiaemo sad1 at left
    s "That cut on your thigh is deeper than I thought..."
    lut "It is no matter. Give Lutvrog a moment to dress it."
    "He moved away toward the building beside the sparring ground, but Sabia kept pace with him. She was moving on instinct, not entirely sure why."
    show sabiaemo normal at left
    s "No, I should take a look at it. This isn't the cleanest of blades, we shouldn't risk infection."
    show lutvrogemo suspicious at right
    lut "..."
    show lutvrogemo normal at right
    "Lutvrog didn't object or reply, which gave her an uncomfortable moment alone with her thoughts."
    menu:
        "Contemplate the idea":
            pass
        "Get out":
            $ lutvrogsex = False
            $ A_lutvrog -= 3
            $ L_orcs -= 1
            "Sabia shook her head, realizing that the camp was starting to get to her. She gave Lutvrog superficial help with bandages and left before her judgment could worsen."
            return
    show sabiaemo happy1 at left
    show sabiaemo2 blush at left
    "Sabia was still flushed and catching her breath from the fight. She told herself that was the only reason she was eyeing the muscles in Lutvrog's back... and his ass."
    "Fuck, she was seriously ogling an orc. Sabia swallowed, but didn't turn back as they entered a small room. It seemed like it had bandages and other healing supplies."
    "Still ignoring her, Lutvrog sat down and began to clean and dress his wound. Sabia swallowed as the movement shifted his loincloth, giving her a hint of the girth behind it."
    show sabiaemo closed2 at left
    "Sabia closed her eyes a moment, wondering if she was really going to do this."
    "The adrenaline was still rushing through her veins, and she wanted to fuck so badly. But... an orc?"
    "Yet Lutvrog had been nothing but honorable to her so far. Even though she'd managed to win, she knew he was stronger than her and maybe even a little more skilled. It had been a long time since another warrior had excited her."
    show sabiaemo lick2 at left
    "He wasn't so awful-looking, for an orc. Not perfectly clean, but he exuded a masculine odor that went straight to her head. If she could ignore the orcishness of him, he had a powerful body she wanted to feel."
    show sabiaemo lick3 at left
    "She wanted to fuck, dammit."
    show sabiaemo happy1 at left
    s "Need some help with that?"
    show lutvrogemo normalopen at right
    lut "Uh... Lutvrog is familiar with bandaging wou-"
    "She interrupted him by bending closer, taking the bandage from him, and finishing wrapping it around his thigh herself. Her fingers trailed over the powerful muscle and she gave a little shiver."
    show lutvrogemo normal at right
    "Fortunately, so did he. A tent was growing in Lutvrog's loincloth."
    show sabiaemo lick2 at left
    s "Oh, good. I was afraid you were only interested in fighting."
    lut "Lut... Lutvrog is a warrior first, but still an orc."
    show sabiaemo happy1 at left
    s "What you are is my prize. I won, right? I think orc tradition gives me ownership of your body now."
    "There was a look in his eye that suggested that orc tradition said no such thing, but Lutvrog kept his mouth shut. He wasn't an idiot, after all - Sabia was stripped out of her clothes and moving to straddle his lap."
    call lutvrogscene
    play music orccamp fadeout 2.0 fadein 2.0
    return


label hellhoundkennels1:
    scene bg kennels
    $ renpy.block_rollback()
    if hellhoundkennelsintro == False:
        $ hellhoundkennelsintro = True
        call sabiabase
        "Hearing strange sounds while searching through camp, Sabia began to hone in on them. She identified them as the deep growls and barks that could only come from hellhounds, but where was the source?"
        show orcbase at right
        show orcloincloth at right
        show orcshoulder at right
        show orcwrap at right
        show orcstrap at right
        show orcemo normal at right
        with dissolve
        "She eventually spotted a closed-off area, but when she got near, an orc immediately moved to block her path."
        orc "Only qualified members of the tribe can enter the kennels. And you aren't either."
        show sabiaemo surprised2 at left
        s "You have kennels? I always th-"
        show orcemo angry at right
        orc "Out, if you value your hide! Don't let me catch you lurking around here again."
        show sabiaemo closed2 at left
        s "(This is surprising. The theory was that orcs naturally attracted their wardogs, but... are they raising the hellhounds here?)"
        show sabiaemo normal at left
        s "(Impossible. They must keep them in the camp, but there's no way they've actually domesticated an animal.)"
        jump lowerorccamp
    else:
        "Since the kennels were still closed to her and guarded, Sabia stayed away from them."
    jump lowerorccamp


label relieftents1:
    scene bg relieftents
    $ renpy.block_rollback()
    if relieftentintro == False:
        $ relieftentintro = True
        call sabiabase
        "Sabia headed to investigate an enclosure that held a number of tents. Many of them were closed up and the area looked to be in worse repair than the rest of the camp."
        show sabiaemo surprised1 at left
        "She got closer to one of the open tents... and the smell of sex hit her like a wall. She stumbled and resisted the urge to hold her nose, but the scent of semen and pussy juice was overpowering."
        "Though the tents muffled sound, when she got close she could hear thumping, moans, and sucking sounds. Soon enough she heard a roar of pleasure, then a short while later an orc emerged from the tent, tugging at his loincloth."
        show sabiaemo irritated1 at left
        "So this was where their filthy debauchery took place. Sabia scowled and observed more closely. There were a number of tents, but not many were occupied at the moment. There was also a guard standing nearby, and he was watching her."
        show orcbase2 at right
        show orcloincloth2 at right
        show orcaxe2 at right
        show orchelmet2 at right
        show orcaxe2 at right
        show orcpiercing2 at right
        show orcwrists2 at right
        show orcemo2 normalopen at right
        with dissolve
        orc "You here to work?"
        show sabiaemo angry2 at left
        s "What? How dare you ask such a thing?"
        show orcemo2 normal at right
        "The orc shrugged, her outburst having no effect. A second later, Sabia realized uncomfortably that it wasn't such an unreasonable assumption. This was what she had been reduced to, after all. But more importantly..."
        show sabiaemo annoyed1 at left
        s "What do you mean \"work\"? Don't you have to know all the slaves here?"
        "The orc stared at her for a moment, then gave a sigh."
        show orcemo2 sad2 at right
        orc "Whatever. Not worth explaining to a human."
        show sabiaemo normal at left
        s "I'm going to stay until you do."
        show orcemo2 angry at right
        orc "Bah, stupid human. Me hate explaining, keep annoying and me hurt you."
        s "..."
        show orcemo2 normal at right
        orc "These slaves not same as human slaves."
        show sabiaemo annoyed2 at left
        s "How, exactly?"
        show orcemo2 sad2 at right
        orc "...bah, me don't want to explain."
        show sabiaemo normal at left
        s "..."
        show orcemo2 normal at right
        orc "Whatever. Humans can't understand."
        s "If they're actually working here, does that mean they get paid?"
        orc "Depends on slave. You can work for gold if want."
        show sabiaemo closed4 at left
        s "What an absurd idea."
        show orcemo2 suspicious at right
        orc "...feh."
    menu:
        "Work in the relief tents (100 stamina)" if reliefunlocked:
            if Sabia.stamina < 100:
                "Sabia was too tired to work in the relief tents."
                jump relieftents1
            if relieftrainsopen == True:
                menu:
                    "Blowjob":
                        $ Sabia.stamina -= 100
                        $ sexworktimes += 1
                        call orcbj
                        jump relieftents1
                    "Tekrok's Crew: Drunk Orcs" if relieftrain1:
                        if Sabia.stamina >= 200:
                            if tekrokcrewscene1 == True:
                                $ tekrokcrewscene = True
                            $ tekrokcrewscene1 = True
                            $ relieftrain1 = False
                            if Sabia.armor != Barmaidclothes:
                                s "I'd better quickly change to cater to this group..."
                            $ Sabia.stamina -= 200
                            $ sexworktimes += 1
                            call tekrokcrew1
                            $ money += 25
                            "After fucking most of Tekrok's crew, Sabia received 25 Lundils."
                            jump relieftents1
                        else:
                            s "I better be at my best to take all of them..."
                    "Tekrok's Crew: Zealous Orcs" if relieftrain2:
                        if Sabia.stamina >= 200:
                            if tekrokcrewscene1 == True:
                                $ tekrokcrewscene = True
                            $ tekrokcrewscene1 = True
                            $ relieftrain2 = False
                            if Sabia.armor != Orcslavearmor:
                                s "I'd better quickly change to cater to this group..."
                            $ Sabia.stamina -= 200
                            $ sexworktimes += 1
                            call tekrokcrew2
                            $ money += 25
                            "After fucking most of Tekrok's crew, Sabia received 25 Lundils."
                            jump relieftents1
                        else:
                            s "I better be at my best to take all of them..."
                    "Never mind":
                        jump relieftents1
                jump relieftents1
            else:
                if tekrokgroup2:
                    if tekrokgroup3:
                        $ relieftrainsopen = True
                        $ relieftrain1 = True
                        $ relieftrain2 = True
                        call sabiabase
                        show orcbase2 at right
                        show orcloincloth2 at right
                        show orcaxe2 at right
                        show orchelmet2 at right
                        show orcaxe2 at right
                        show orcpiercing2 at right
                        show orcwrists2 at right
                        show orcemo2 normalopen at right
                        with dissolve
                        orc "You know, an awful lot of Tekrok's boys have been asking for you."
                        show sabiaemo closed2 at left
                        s "(Took them long enough.)"
                        show sabiaemo normal at left
                        s "What do they want?"
                        orc "They want to hire you out for a whole group. If you can take them all, it'd pay really well."
                        show sabiaemo closed2 at left
                        s "I'll keep it in mind."
                        orc "Just let me know if you want to take a whole group of them."
                        jump relieftents1
                $ Sabia.stamina -= 100
                $ sexworktimes += 1
                call orcbj
                jump relieftents1
            jump relieftents1
        "Talk to guard orc":
            call sabiabase
            show orcbase2 at right
            show orcloincloth2 at right
            show orcaxe2 at right
            show orchelmet2 at right
            show orcaxe2 at right
            show orcpiercing2 at right
            show orcwrists2 at right
            show orcemo2 normalopen at right
            with dissolve
            menu:
                "How many women do you have here?":
                    show orcemo2 suspicious at right
                    orc "Seriously? Me guard, not some... slut counting person. Me just do my job, and want do it without your stupid questions."
                "Do all the orcs come here?":
                    show orcemo2 normal at right
                    orc "These are only relief tents, if that's what you mean."
                    show orcemo2 smile1 at right
                    orc "But obviously, the Warchief and Captains don't come around here. They call sluts to them."
                    show orcemo2 normal at right
                    orc "A lot of the richest orcs work for them, so you have to work hard to get their attention."
                "You don't have any female orcs here?":
                    show orcemo2 angry at right
                    orc "You know we don't, bitch."
                    show sabiaemo closed4 at left
                    s "No, it was an honest question. We've always assumed that some female orcs survived the extermination campaigns."
                    orc "Well, you humans did your job really fucking well. Haven't seen a real female in years."
                    show sabiaemo closed2 at left
                    s "..."
                "Does Neve ever work here?":
                    show orcemo2 smile1 at right
                    orc "Fuck, me {i}wish{/i}. We'd make so much fucking money..."
                    show orcemo2 normal at right
                    orc "Neve don't fuck for pay. Only a few lucky bastards get to be with her."
                "What do you think of the Captains?" if captainsintro:
                    show orcemo2 normalopen at right
                    orc "It's all the same to me, me work directly under Warchief Groknak. Can't have any Captains gathering support via pussy."
                    s "You must have {i}some{/i} thoughts."
                    show orcemo2 normal at right
                    orc "None of them come by much, really. Tekrok has his own women. Rokgrid wants to pick a mate. Me don't know what Dajrab's deal is."
                "Go back":
                    jump relieftents1
            jump relieftents1
        "Go back":
            jump lowerorccamp
    jump lowerorccamp


label orcbj:
    play music sex1 fadeout 2.0 fadein 2.0
    if firstorcbj == False:
        $ firstorcbj = True
        call sabiafirstbj
    else:
        $ bjexp = 0
        if sexworktimes >= 3:
            $ bjexp += 1
        if sexworktimes >= 6:
            $ bjexp += 1
        if neveadvicebj == True:
            $ bjexp += 1
        if nevebjadvice:
            if bjexp >= 3:
                $ nevebjadvicetook = True
                call sabiatent4
                $ money += 12
                "After finishing her work, Sabia received 12 Lundils."
            else:
                $ neveadvicebj = True
                call sabiatent3
                if bjexp > 2:
                    $ money += 11
                    "After finishing her work, Sabia received 11 Lundils."
                elif bjexp > 1:
                    $ money += 9
                    "After finishing her work, Sabia received 9 Lundils."
                else:
                    $ money += 7
                    "After finishing her work, Sabia received 7 Lundils."
        else:
            if bjexp >= 1:
                call sabiatent2
                $ money += 6
                "Sabia received 6 Lundils."
            else:
                call sabiatent1
    play music orccamp fadeout 2.0 fadein 2.0
    return


label orcoutskirts1:
    scene bg countryside
    $ renpy.block_rollback()
    if orcoutskirtsintro == False:
        $ orcoutskirtsintro = True
        "At the edge of camp there were a few guards posted, but they didn't seem to care about her. Maybe because she was just a human woman, maybe because they didn't care about anyone trying to get {i}out{/i}."
        "An area had been cleared for staging battles, but at the moment it was mostly empty. Sabia spotted Neve leaning against a tree, but otherwise the Outskirts were desolate."
    menu:
        "Leave camp":
            s "(No, it wouldn't be safe to wander far. Ridiculous as it sounds, I'm safer in the orc camp than in human lands.)"
            jump orcoutskirts1
        "Talk to Neve":
            show backdrop
            call sabiabase
            show neve1 at right
            show neveemo normal at right
            n "Sabia."
            menu orcoutskirts1_neve:
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
                    jump orcoutskirts1_neve
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
                    jump orcoutskirts1_neve
                "Why are you here in the orc camp?":
                    show neveemo closed3 at right
                    n "Let's just say it's more interesting than the alternatives."
                    jump orcoutskirts1_neve
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
                    jump orcoutskirts1_neve
                "Are orcs really that good at sex?" if (dajraberrand >= 3 and nevesexconvo == False):
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
                    jump orcoutskirts1_neve
                "How can I get more money at the relief tents?" if (sexworktimes >= 1 and nevebjadvice == False):
                    $ nevebjadvice = True
                    $ A_neve += 1
                    show sabiaemo sad2 at left
                    show sabiaemo2 blush at left
                    s "...I can't believe I'm asking that, but..."
                    show neveemo smirk1 at right
                    n "Heh. Awkward question, isn't it?"
                    show sabiaemo irritated2 at left
                    s "You don't need to tell {i}me{/i} that. But if I'm putting my body on the line, I need these brutes to pay me more."
                    show neveemo normal at right
                    n "I can guess what you're doing wrong. Most orcs don't really care if you're having a good time, but they need you to be a little enthusiastic. Unresisting mouths aren't hard to find."
                    n "Their cocks are pretty tough, so no need to be gentle. But that doesn't mean you need to rush: give them some tongue attention first. And make some eye contact."
                    show sabiaemo closed2 at left
                    s "Guh..."
                    show neveemo smirk1 at right
                    n "What, you're saying you loved blowing orcs except for the eye contact?"
                    show sabiaemo irritated1 at left
                    s "No, no, it's good advice, I'll just have to steel myself for it."
                    show neveemo sad at right
                    n "A shame you're starting out like this, though. Blowjobs can be fun, I hope you don't get turned off the experience because of this."
                    hide sabiaemo2 blush
                    s "..."
                    jump orcoutskirts1_neve
                "What do you think of the Captains?" if captainsintro:
                    show neveemo closed1 at right
                    n "I try not to get involved, honestly."
                    s "But surely you have some thoughts about them."
                    show neveemo normal at right
                    n "Let me see... Rokgrid has always been polite, but we haven't really talked much."
                    show neveemo closed1 at right
                    n "Dajrab... I've always done right by him and he's always done right by me, but let's just say I wouldn't want to find out what he'd be like if I backstabbed him."
                    show neveemo irritated2 at right
                    n "Tekrok... is Tekrok. Don't really want to talk about him."
                    show sabiaemo annoyed1 at left
                    s "You two have some kind of history?"
                    show neveemo irritated1 at right
                    n "..."
                    show sabiaemo closed1 at left
                    s "Signal received, backing off."
                    jump orcoutskirts1_neve
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
                    jump orcoutskirts1_neve
                "Go back":
                    jump orcoutskirts1
        "Harvest venomnettle (10 stamina)" if (gotvenomnettle == False and silvertuskintro == True):
            if Inventory.has_item(Knife) > 0:
                if Sabia.stamina < 10:
                    "Sabia was too tired to harvest any venomnettle."
                    jump orcoutskirts1
                $ gotvenomnettle = True
                "Using her knife, Sabia was able to cut through the venomnettle at the root and harvest an adequate amount."
                s "(Alright, now I just need to take that back to Jadk!)"
                jump orcoutskirts1
            else:
                if Sabia.stamina < 10:
                    "Sabia was too tired to harvest any venomnettle."
                    jump orcoutskirts1
                $ Sabia.stamina -= 10
                "Sabia found some venomnettle and tried to pull it, but the tough plants refused to be uprooted and only hurt her hands."
                s "They're too low to the ground to use a sword on, I'd need something smaller..."
                jump orcoutskirts1
        "Go back":
            jump eastern_frontier_map
    jump lowerorccamp



label mainhall1:
    scene bg mainhall
    "Sabia didn't even get close before she was blocked by guards. It seemed the Warchief's hall was firmly off limits."
    jump upperorccamp


label tekroktent1:
    scene bg tekroktent
    $ renpy.block_rollback()
    if captainsintro:
        if tekrokintro:
            menu:
                "Impress drunk orcs" if tekrokalliance:
                    if bjexp < 2:
                        "Though she knew what she had to do, when Sabia thought about trying to impress the orcs her stomach turned. There was no way she could bring herself to do that."
                        jump tekroktent1
                    if tekrokgroup2:
                        "Sabia didn't bother going near, having already gotten that group's attention."
                        jump tekroktent1
                    if Sabia.armor == Barmaidclothes:
                        if tekrokgroup2 == False:
                            $ tekrokgroup2 = True
                            show orcbaseL at left
                            show orcloinclothL at left
                            show orcemo smile2L at left
                            show orcbase2 at right
                            show orcloincloth2 at right
                            show orcemo2 smile2 at right
                            show basesimple at center
                            show baroutfit1 at center
                            show sabiaemo closed2 at center
                            show sabiaemo2 blush at center
                            with dissolve
                            "Sabia pulled her barmaid outfit a little lower. She usually didn't wear it for attention, but now she needed the group to notice her."
                            "Notice her they did, yelling out drunken propositions as she passed. Several of them stumbled after her as she went."
                            "Sabia had a feeling she'd be seeing a lot of them soon if she went to the relief tents."
                        else:
                            "Sabia didn't bother going near, having already gotten that group's attention."
                    elif Sabia.armor == Rags:
                        "The orcs didn't even look at Sabia, apparently used to seeing slaves in rags."
                        s "If I wanted to interest them like Tekrok implied, I'll need to catch their attention somehow..."
                    else:
                        "A few of the orcs glanced at Sabia, but her outfit didn't attract much attention."
                        s "Looks like this group carried a bunch of alcohol from the bar, maybe I can catch their attention with something related to that..."
                    jump tekroktent1
                "Impress zealous orcs" if tekrokalliance:
                    if bjexp < 2:
                        "Though she knew what she had to do, when Sabia thought about trying to impress the orcs her stomach turned. There was no way she could bring herself to do that."
                        jump tekroktent1
                    if tekrokgroup3:
                        "Sabia didn't bother going near, having already gotten that group's attention."
                        jump tekroktent1
                    if Sabia.armor == Orcslavearmor:
                        if tekrokgroup3 == False:
                            $ tekrokgroup3 = True
                            show orcbaseL at left
                            show orcloinclothL at left
                            show orcemo smile2L at left
                            show orcaxeL at left
                            show orcbase2 at right
                            show orcloincloth2 at right
                            show orcemo2 smile2 at right
                            show orcaxe2 smile2 at right
                            show basesimple at center
                            show orcslave1 at center
                            show sabiaemo closed2 at center
                            show sabiaemo2 blush at center
                            with dissolve
                            "This group noticed immediately when she moved past wearing Tekrok's armor. Judging from their leers, they knew exactly what it meant."
                            "She'd expected them to yell out insults, but instead they just stared at her possessively. As if she was really theirs, just like the armor she wore implied."
                            "Sabia had a feeling she'd be seeing a lot of them soon if she went to the relief tents."
                        else:
                            "Sabia didn't bother going near, having already gotten that group's attention."
                    elif Sabia.armor == Rags:
                        "The orcs didn't even look at Sabia, apparently used to seeing slaves in rags."
                        s "If I wanted to interest them like Tekrok implied, I'll need to catch their attention somehow..."
                    else:
                        "A few of the orcs glanced at Sabia, but her outfit didn't attract much attention."
                        s "Based on their conversation, these orcs are real hardline nationalists. Maybe that outfit Tekrok gave me would suit them better..."
                    jump tekroktent1
                "Talk to Tekrok":
                    s "I don't want to piss Tekrok off by bothering him, I'd better stay away."
                    jump tekroktent1
                "Go back":
                    jump upperorccamp
        else:
            jump tekrokintro
    else:
        s "The orcs here could not look more hostile. Better stay away unless I have a good reason to talk to the Captains."
    jump upperorccamp


label tekrokintro:
    $ tekrokintro = True
    call sabiabase
    show tekrok angry2 at right
    t "What the fuck are you doing here, human?"
    s "..."
    show tekrok happy1 at right
    t "Get out, boys! Let Tekrok show this bitch a thing or two!"
    "The orcs lounging around crowded out, laughing and leering at Sabia, many of them nudging each other. She stood very still, wondering if she hadn't made a huge mistake."
    show sabiaemo angry1 at left
    s "...if you're thinking of attacking me, you should kn-"
    show tekrok normal at right
    t "Relax. Tekrok hates you, but Tekrok is not an idiot."
    show sabiaemo closed2 at left
    s "..."
    show tekrok happy1 at right
    t "You're here because you're fucked without help, right? And you think you can strike a deal with Tekrok to gain an advantage."
    show tekrok normal at right
    t "Well, you're right. Tekrok despises your kind, but this trial is too important to let that get in the way."
    show sabiaemo happy1 at left
    s "Good. What are you offering?"
    t "To answer that, Tekrok needs to know what you want."
    show sabiaemo normal at left
    s "The rogue orcs who captured me were paid by my rivals. I can't get my revenge without assistance."
    t "Hmph. Tekrok can understand that, at least."
    show tekrok happy1 at right
    t "Look, Tekrok will offer you this: help Tekrok out now, and Tekrok's boys will be happy to raid whoever you want. They've been wanting a chance to attack Lundar anyway."
    show sabiaemo eyebrow1 at left
    s "And what are you asking for?"
    show tekrok normal at right
    t "These rogue orcs working for humans have gotten everyone riled up. Now, most likely they were drunk or greedy or just stupid. But this is the perfect chance."
    show tekrok angry2 at right
    t "Tekrok's got a rival problem of his own: Rokgrid. Some warriors like his ideas about peace between orcs and humans, but they'd turn on him if they believed he was behind the rogue orcs."
    show sabiaemo closed2 at left
    s "So you want me to implicate him during the trial? I can say whatever you want, but I don't know how much evidence I can offer."
    show tekrok happy1 at right
    t "This trial is bitterly contested, so anything will help. Tekrok will give you lies to tell, don't worry about that part."
    show tekrok normal at right
    t "But first, you need to become a member of the tribe."
    show sabiaemo normal at left
    s "So I heard. It's not obvious to me how that happens."
    t "You have to endure three rituals, and just to make the attempt, you need a recommendation from a ranking officer."
    t "Now, Tekrok sure as hell can't give you Tekrok's recommendation. But Tekrok can talk to someone and make sure you can take the trial."
    show sabiaemo happy1 at left
    s "I see. Thank y-"
    show tekrok angry1 at right
    show sabiaemo normal at left
    t "Not so fast. That's only if you swear to Tekrok that you'll back Tekrok in the trial."
    show tekrok angry2 at right
    t "Well, human? You can make this easier for yourself by agreeing... but if you betray Tekrok now, you'll live to regret it."
    menu:
        "Form alliance":
            $ tekrokalliance = True
            $ triberec = True
            show tekrok happy1 at right
            t "You're not an idiot, then. Tekrok is the future of the orc tribe, and you don't want to be on Tekrok's bad side."
            show sabiaemo closed2 at left
            s "..."
            show tekrok normal at right
            t "Now, getting a human like you through the challenge won't be easy. Tekrok can't support you directly, but Tekrok does need you to make it to the trial."
            t "For a start, take this."
            $ Inventory.add_item(Orcslavearmor)
            show sabiaemo surprised2 at left
            s "What... what kind of armor is this? It barely covers anything!"
            show tekrok happy1 at right
            t "That's what captive warriors would wear, if Tekrok had his way. But make no mistake, it'll protect you better than those rags."
            show sabiaemo pout3 at left
            s "..."
            show tekrok happy2 at right
            t "Plus, it won't upset the warriors. Before, you looked like the humans that attacked us. Now, you look like a human that belongs to us."
            show sabiaemo closed4 at left
            s "(That's a disgusting idea, but there was more thought behind his choice than I thought. I shouldn't underestimate him.)"
            show tekrok normal at right
            t "Well, it's up to you if you wear it. But it might help you impressing Tekrok's boys."
            show sabiaemo annoyed1 at left
            s "Your boys?"
            t "If you want to work with Tekrok long term, you'll need the orcs that follow Tekrok to not hate you."
            show tekrok happy1 at right
            t "The way Tekrok sees it, the only way you could pull that off is to fuck them. They hate humans, but they love human sluts."
            show sabiaemo angry2 at left
            s "Guh..."
            show tekrok normal at right
            t "It's up to you, all Tekrok needs from you is your word during the trial. But if you want them to back you afterward, you'd better put your body on the line."
            hide tekrok normal with fade
            s "(What a vile orc. But at least his motives are clear, and this armor is stronger than it looks. Perhaps I can use him.)"
        "Refuse":
            $ tekrokreject = True
            show tekrok angry1 at right
            t "Bah, Tekrok should have known. Maybe Tekrok should just kill you now..."
            show sabiaemo surprised3 at left
            s "..."
            show tekrok normal at right
            t "No, Rokgrid might be able to make it look like an admission of guilt. But Tekrok expects more from you in the future, human."
            hide tekrok normal with fade
            show sabiaemo angry2 at left
            s "(What a vile orc. Every single one like him should be eradicated.)"
    jump upperorccamp


label rokgridtent1:
    scene bg rokgridtent
    $ renpy.block_rollback()
    if captainsintro:
        if rokgridintro:
            s "I've said all I need to with Rokgrid for now, so I should stay away."
        else:
            jump rokgridintro
    else:
        s "This must be a Captain's tent, judging from the heavy guard. Better not to get too close before I've attracted their attention."
    jump upperorccamp


label rokgridintro:
    $ rokgridintro = True
    call sabiabase
    show rokgrid happy2 at right
    r "Ah, Sabia. I am ever so glad you decided to speak with me."
    s "I'm not here to make friends. But I think we might have some of the same goals."
    show rokgrid normal at right
    r "I would rather be friends with my allies... but I understand the necessity of an alliance of convenience."
    show sabiaemo normalopen at left
    s "I know you want my support in the trial. I think we should make a deal."
    show rokgrid happy3 at right
    show sabiaemo normal at left
    r "I believe you'll soon see that helping me is in your best interest as well."
    show rokgrid normal at right
    r "What you need to understand is that there is a civil war at the heart of our tribe. Tekrok would prefer we become the savages you humans believe we are, whereas I would like to elevate orcs to a more refined civilization."
    show sabiaemo annoyed1 at left
    s "If you think Lundar is going to welcome you with open arms, you're a fool."
    show rokgrid happy4 at right
    r "Believe me, I quite understand your kingdom's attitudes. But tell me, would you rather have violent raiders on your borders, or tribes you can negotiate with?"
    show sabiaemo closed2 at left
    s "..."
    show rokgrid normalclosed at right
    show sabiaemo normal at left
    r "Regardless of who is behind the actions of the rogue orcs who captured you, Tekrok would like to pin the blame on me."
    show rokgrid angry1 at right
    r "That would make all my work go to waste, and I cannot allow that to happen. Hence, I would like you to testify to everything you know and make sure the truth is revealed during the trial."
    show rokgrid happy2 at right
    r "But I understand that you want to make a deal... so what exactly are you asking?"
    show sabiaemo closed1 at left
    s "I need to take revenge against the ones who did this to me. And if what you've said about your goals is true, then you want me to succeed."
    show sabiaemo happy1 at left
    s "I have no love for orcs, but the humans who will take over now were the ones behind the worst exterminations. Trust me, you would rather I be in charge."
    show sabiaemo closed2 at left
    s "(Hopefully he'll buy that. Truth is, Lynn doesn't give a shit about orcs, whereas after this, I'd rather kill them all.)"
    show rokgrid happy4 at right
    show sabiaemo normal at left
    r "Yes, that does seem agreeable. Indeed, I would hope we could form a longer lasting alliance, but we should not get ahead of ourselves."
    show rokgrid happy2 at right
    r "Sabia, will you take my side and make sure that justice is done in this trial?"
    menu:
        "Form alliance":
            $ rokgridalliance = True
            $ huntingopen = True
            $ ef_forest2_unlocked = True
            $ triberec = True
            show rokgrid happy5 at right
            r "Wonderful! Now, I trust you are aware that you will need to become a provisional member of our tribe in order to testify during the trial?"
            s "Yeah, I know."
            show rokgrid happy2 at right
            r "Well, you have my whole-hearted recommendation, which is enough to allow you to undergo the ritual. However, I suggest that you wait a little longer to prepare, for it is not an easy one."
            $ money += 20
            r "Please allow me to assist you with a few tokens of appreciation for your statement of goodwill. For a start, I hope these 20 Lundils will assist you in your efforts."
            show rokgrid normal at right
            r "But orcs do not respect those who succeed based on what they are given. I would also like to make it easier for you to earn their respect."
            r "To that end, I will grant you permission to hunt for wild beasts in the surrounding forests. It is respected, many warriors build their skills this way, but not so important that it will upset traditionalists."
            s "Hmm, I see."
            show rokgrid happy2 at right
            r "I suggest you develop your skills hunting, then take the challenge to become a member. I feel confident you can do both in time for the trial."
            s "And then what do you want me to say?"
            show rokgrid normalclosed at right
            r "Only the truth. However, there are a few orcs who have been implicated who I have no doubt are innocent. If you could make sure they go free, I would be grateful."
            s "I'll see what I can do."
            show rokgrid happy2 at right
            r "Very good. Now, we cannot be seen together too frequently, so I can only hope my support will be enough for you to join us. And I do hope that you will join us, Sabia."
            show sabiaemo happy1 at left
            s "I look forward to it!"
            hide rokgrid happy2 with fade
            show sabiaemo irritated1 at left
            s "(Ugh, an orc pretending to be a human. Sickening. But at least he seems reasonable enough, perhaps this alliance will work in my favor.)"
        "Refuse":
            $ rokgridreject = True
            show rokgrid sad1 at right
            r "That is... very disappointing to hear. I hope it is merely that you cannot bring yourself to trust orcs."
            show rokgrid normal at right
            r "But it is your choice. I can only hope you will choose to tell the truth during the trial. If you do, perhaps we can still work together."
            hide rokgrid normal with fade
            show sabiaemo irritated1 at left
            s "(Ugh, an orc pretending to be a human. Sickening. He seems reasonable, but I'm not going to get anywhere allying with a spineless orc like that.)"
    jump upperorccamp


label dajrabtent1:
    scene bg dajrabtent
    $ renpy.block_rollback()
    if captainsintro == True:
        if dajrabintro == True:
            if dajraberrand == 5:
                s "Dajrab said we'd talk again before the trial, I shouldn't bother him before then."
            elif dajraberrand == 4:
                $ dajraberrand += 1
                $ A_dajrab += 1
                call sabiabase
                show dajrab normalclosed at right
                "Sabia moved past the guards, who nodded politely to her. Inside the tent, she found Dajrab seated silently as if waiting for her."
                s "It's done."
                d "Good. No questions?"
                show sabiaemo irritated2 at left
                s "Do you want me to ask any?"
                d "No."
                show sabiaemo eyebrow1 at left
                s "Then I don't have any questions. You said there would be a reward?"
                if dajrabtookmoney == True:
                    "Dajrab stared at her a long moment, then nodded."
                elif dajrablookedpackage == True:
                    "Dajrab stared at her a moment, then nodded."
                show dajrab normalopen at right
                show sabiaemo normal at left
                d "Thank you for completing the errand. As promised, you will be compensated for your work."
                $ Inventory.add_item(Orcring)
                show dajrab normalclosed at right
                "He extended one large hand and to Sabia's surprise, there was a dark red ring inside it. The crafting was simple, but she could feel a tingle of magic when she took it from his hand."
                d "Wear this and you should be better prepared for the tribal challenge. Good luck."
                s "...thank you."
                "Sabia had never imagined she would receive an artifact of any kind. She desperately wanted to ask how he had gotten it, but suspected questions would only lower his opinion of her. So instead, she merely nodded."
                show sabiaemo closed2 at left
                s "We will speak again before the trial."
                d "Yes."
            elif dajraberrand >= 1:
                s "I shouldn't go back until I've finished Dajrab's errand."
            else:
                s "No, I better not bother Dajrab again."
        else:
            jump dajrabintro
    else:
        "Unlike many of the others, this tent was heavily guarded. Sabia decided it was better not to approach without a good reason."
    jump upperorccamp


label dajrabintro:
    $ dajrabintro = True
    call sabiabase
    show dajrab normalclosed at right
    d "..."
    show sabiaemo irritated1 at left
    s "..."
    d "..."
    show sabiaemo irritated2 at left
    s "You're not going to say anything?"
    show dajrab normalopen at right
    d "You're the one who entered my tent."
    show sabiaemo annoyed1 at left
    s "Don't play like that. You were there watching me too. And you're one of only three Captains in this tribe - there's no way you've kept your position without having some schemes."
    show dajrab normalclosed at right
    d "Do you see these scars? I earned my position battle by battle, not through schemes."
    show sabiaemo sad1 at left
    s "(I hadn't realized just how many scars he had... and some look bad. Honestly, I don't know any veterans who have survived that many injuries. He must have incredible stamina.)"
    show sabiaemo normal at left
    d "But you are correct that I have some interest in these events. As you may know, Tekrok and Rokgrid want to pull this tribe in very different directions."
    d "I seek to be a... moderating force."
    s "You don't have your own vision for the tribe?"
    show dajrab normalopen at right
    d "I lack the vision to be Warchief. All I seek is to make sure the tribe makes the best choice, not the choice of the one who schemes better."
    show sabiaemo closed2 at left
    s "..."
    show dajrab normalclosed at right
    d "Disappointed? I have little against you or humans, but I also need little, so I fear I cannot offer you any deal."
    show sabiaemo happy2 at left
    s "Saw through me, huh? Well, I suppose there aren't that many reasons I would be coming here."
    show sabiaemo happy1 at left
    s "But I think you're wrong: I do have something you want. Both the other Captains will probably try to get me to attack the other. Wouldn't you rather I took a middle path and made sure things stay the way they are?"
    d "...do you believe I will grant you some advantage now?"
    show sabiaemo normal at left
    s "Seems obvious you won't. But I don't care about this trial, what I need is an ally to help me take revenge on the ones who put me here."
    s "Keeping you orcs stable and not fighting each other sounds like a good start."
    $ triberec = True
    show dajrab happy at right
    d "Heh. I can respect that. Very well, I will give you my recommendation for the membership ritual. Let's see how you manage the challenges."
    show sabiaemo irritated2 at left
    s "That's all? We can't come to any agreement?"
    show dajrab normalclosed at right
    d "..."
    show dajrab normal at right
    d "You want to prove yourself trustworthy? You can only do that by your words during the trial."
    show dajrab normalclosed at right
    d "But if you want to earn my trust now, I would have an... errand for you."
    show sabiaemo normal at left
    s "An errand?"
    d "But I will only speak of it more if you promise to complete the task, and not to say anything of it to anyone. Do I have your word?"
    menu:
        "Yes":
            $ dajraberrand = 1
            $ ef_mountains1_unlocked = True
            show dajrab normalopen at right
            d "In that case... I have a task for you that requires discretion, but involves no danger."
            d "Listen very carefully, because I'm only going to say this once."
            s "..."
            show dajrab normalclosed at right
            d "First, you need to go to the Trading Lodge. You will receive a letter directing you to a specific location."
            d "Go to that location and you will receive a package. Don't look inside or tamper with it."
            d "You need to take that package to the mountains north of camp and bury it. That is all."
            d "Don't speak to anyone about any of these details. No one should ask you any questions at any step of the process."
            d "Does that make sense to you?"
            show sabiaemo happy1 at left
            s "Got it."
            show sabiaemo closed2 at left
            s "(Suspicious as hell, but I got it. Get the package from the Trading Hut, then bury it outside camp.)"
            d "Return here once you are done and I will offer you payment. Otherwise, we can discuss matters further before the trial."
            hide dajrab normalclosed with fade
            show sabiaemo closed4 at left
            s "(He's a brute, but I'd rather not get on his bad side. I should make sure to complete this errand.)"
        "No":
            show dajrab happy at right
            d "I respect someone who does not make agreements they do not intend to keep. We shall see what you do during the trial."
            hide dajrab happy with fade
            show sabiaemo closed4 at left
            s "(He's a brute, but I don't think I can manipulate him. Maybe he'll stand aside and let me work.)"
    jump upperorccamp


label tradinglodge1:
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
            jump tradinglodge1
        "Purchase clothing":
            call openshop (Orcclothshop)
            jump tradinglodge1
        "Purchase general goods":
            call openshop (Orcgeneralshop)
            jump tradinglodge1
        "Eavesdrop on random orcs":
            $ tempnum = renpy.random.randint(1,6)
            if tempnum == 1:
                "First Orc" "Where's that human with the huge tits?"
                "Second Orc" "Went back to a town to buy more, I think."
                "First Orc" "Dammit, I wanted to have something to watch while I worked. Wouldn't mind fucking her, either."
                "Second Orc" "Don't be an idiot. It took us long enough to get a merchant to sell us things we can't make."
                "First Orc" "I know, I know..."
            if tempnum == 2:
                "First Orc" "When are you getting more stock? This is shit."
                "Second Orc" "Still waitin' on a shipment of human supplies."
            if tempnum == 3:
                "First Orc" "These furs are worth twice that. Fuck your offer!"
                "Second Orc" "Fuck {i}you{/i}!"
                "First Orc" "No, fuck {i}you{/i}!"
                "Second Orc" "No, fuck YOU!"
                "First Orc" "FUCK, FUCK YOU!"
                call sabiabase
                show sabiaemo pout3 at left
                with dissolve
                s "..."
            if tempnum == 4:
                orc "Wait, didn't we have more than this? If those fucking catgirls managed to steal some again, I swear..."
            if tempnum == 5:
                "First Orc" "Where the hell did you get something this nice?"
                "Second Orc" "Bought it from minotaur raiders a while back."
                "First Orc" "Those damn cows are annoying, but I admit they're better at getting away with raids."
                "Second Orc" "No, you just watch, the humans are gonna bring the hammer down on them soon."
            if tempnum == 6:
                "First Orc" "Are Tekrok and Rokgrid still holding up the trial? Damn, those two fight each other more than the humans..."
                "Second Orc" "They're serious this time, I hear heads might be on the line."
            jump tradinglodge1
        "Sign up for cleaning duty" if (trashintro == True and workunlocked == False):
            call sabiabase
            show orcbase at right
            show orcloincloth at right
            show orcbeard1 at right
            show orcnecklace at right
            show orcwrap at right
            show orcemo normal at right
            with dissolve
            $ workunlocked = True
            "There was an orc drinking at a table, but there were several rough signs set up in front of him. One of them said something about trash, so Sabia approached."
            s "I heard you could get paid for cleaning trash?"
            orc "Huh. We've needed a few good slaves to clean up all this shit."
            s "I'm not doing it unless I get paid."
            orc "Yeah, okay. Me sign you up - bring trash, we pay."
            s "How much?"
            orc "Depends how much trash."
            show sabiaemo irritated1 at left
            s "(Dammit. But this might be my only way of earning money, at least until I can work my way up to something better.)"
            s "(At the very least, I should get a broom so I'm not scrabbling with my hands like an animal.)"
            jump tradinglodge1
        "Receive letter" if dajraberrand == 1:
            $ dajraberrand += 1
            show orcbase at right
            show orcloincloth at right
            show orchelmet at right
            show orcshoulder at right
            show orcstrap at right
            show orcwrists at right
            show orcemo normal at right
            with moveinright
            "While Sabia walked through the trading lodge, an orc strode quickly in her direction, not looking at her."
            "She realized too late that he wouldn't stop and they hit each other, sending Sabia stumbling away. She was about to curse his carelessness when she realized that something had been pushed into her hands."
            hide orcbase at right
            hide orcloincloth at right
            hide orchelmet at right
            hide orcshoulder at right
            hide orcstrap at right
            hide orcwrists at right
            hide orcemo normal at right
            with moveoutright
            "A letter."
            s "(So, this must be what Dajrab meant. Let me see what it says...)"
            s "(Hmm, a crude map of the tents, with one marked. And that scrawl... it says to meet at midnight, I think?)"
            s "(I'll have to go there tonight, where hopefully they'll just give me a normal package.)"
            s "(If that's a euphemism I will {i}kill{/i} Dajrab.)"
            jump upperorccamp
        "Go back":
            jump upperorccamp


label orctents1:
    scene bg orctents
    $ renpy.block_rollback()
    if dajraberrand == 2:
        $ dajraberrand += 1
        "That night, Sabia moved cautiously through the orc tents. She knew what some might do if they caught her, but didn't have a choice if she wanted to finish Dajrab's errand."
        "Eventually Sabia found the tent that was marked on the map. She peered inside... and couldn't believe her eyes."
        call neveorctravelers
        scene bg orctents
        call sabiabase
        show sabiaemo surprised1 at left
        show nevenaked1 at right
        show neveemo smirk1 at right
        with dissolve
        "As Sabia gave a startled sound and jerked back, Neve hopped off of the two exhausted orcs and flashed a quick smile."
        n "Getting a good eyeful, were you?"
        s "I..."
        n "Are you actually the one I'm supposed to meet? Sorry, I didn't expect you to arrive so quickly."
        call sabiabase
        show sabiaemo surprised2 at left
        show sabiaemo2 blush at left
        s "What exactly is going on here?"
        show neveemo smirk1 at right
        n "We were fucking. You see, sometimes people want t-"
        show sabiaemo angry1 at left
        hide sabiaemo2 blush
        s "I know what you were doing. Why?"
        show neveemo happy1 at right
        n "Oh, that was just for fun. These two travel around the countryside, so they have interesting stories. I often hook up with them when they visit."
        show sabiaemo irritated2 at left
        s "I... see. I guess I just assumed you didn't fuck orcs."
        show neveemo irritated1 at right
        n "I like orcs just fine. Unless they're way too serious about it, like a certain Captain I could name..."
        s "Who?"
        show neveemo closed1 at right
        n "Hmm, maybe I shouldn't say? Not that it's much of a secret, but..."
        show neveemo normal at right
        n "Anyway, unless you are wandering aimlessly, I assume you're here for the package?"
        show sabiaemo normal at left
        s "You have one? The letter sa-"
        show neveemo closed1 at right
        n "I don't want to know any details. I've already been paid, that's enough for me. Here you go."
        "Neve handed Sabia a wrapped package carelessly, but when Sabia took it she nearly dropped it. The package was surprisingly heavy, despite how easily Neve had been handling it."
        show neveemo happy1 at right
        n "I don't care what you do with it, either. We're done here, right?"
        s "I suppose our business is done, but I would like t-"
        show neveemo happy3 at right
        n "We can talk about that later. These two might be up for another round, I don't want to miss that!"
        show sabiaemo irritated1 at left
        s "..."
        "With no other choice, Sabia retreated from the tent."
    else:
        "Sabia wandered near the tents where most of the orcs rested. They stared at her, but didn't move. With no reason to be there, Sabia quickly left."
    jump upperorccamp



label orcmembershiptrials:
    scene bg RGAbg4
    play music orcritual fadeout 2.0 fadein 2.0
    call sabiabase
    with dissolve
    "Not many orcs had come to watch, but there were still quite a few of them. Watching her. Probably waiting for her to fail."
    "Sabia took a deep breath and tried to focus. This was her only chance to impress them, to gain their support. Not just for the trial, but for her revenge against her sister."
    show orcshaman normal at right
    with dissolve
    "An orc wearing several fetishes emerged and made several shamanistic gestures. Sabia didn't feel any magic, but knew he would start the trials."
    show orcshaman sad2 at right
    orcshaman "We now begin the challenges for this human warrior. Do you, truly, wish to join the Tribe of Groknak?"
    s "I do."
    show orcshaman angry1 at right
    play sound gong
    orcshaman "So be it. Let the Challenge of Skill begin."
    hide orcshaman angry1
    with moveoutright
    "Sabia was given a large log and instructed to carry it on her shoulders to the other end of the arena without falling. It struck her as more a trial of strength than anything, before she realized that obstacles had been set in the arena before her."
    "There were low snares she needed to leap over, poles to catch the log on her shoulders, even vines drooping from the trees overhead. Getting through while carrying the log would not be easy."
    show sabiaemo irritated1 at left
    "Taking a deep breath, Sabia centered the log over her shoulders and then moved forward."
    if Sabia.stamina >= 150:
        if Sabia.level >= 2:
            "Sabia easily leapt the first few obstacles and dodged around the others. She felt strong, she could easily carry the log all the way to the end."
            "A few times the log tapped against one of the obstacles, but that wasn't enough to make her fall."
            show sabiaemo happy3 at left
            "Abruptly she found herself on the other side of the arena, no more obstacles in front of her. Sabia threw the log off her shoulders triumphantly and turned to the crowd."
            show sabiaemo normal at left
            "The orcs didn't look too happy, but at least they weren't yelling at her. It seemed like a few more had come to watch her, too."
        else:
            "Sabia easily leapt the first few obstacles and dodged around the others. She felt strong, she could easily carry the log all the way to the end."
            show sabiaemo surprised3 at left
            "But just when she was getting near, she didn't move smoothly enough and the log on her shoulders clipped one of the obstacles. She tried to correct, but she was off balance and tumbled to the ground."
            jump orctrialfailure
    else:
        "Sabia easily leapt the first few obstacles and dodged around the others. But with each one, she found herself moving a little slower. She was wearing out."
        show sabiaemo surprised3 at left
        "Then without warning, she didn't move smoothly enough. The log on her shoulders clipped one of the obstacles and sent her tumbling to the ground."
        jump orctrialfailure
    show orcshaman normal at right
    with moveinright
    play sound gong
    orcshaman "The Challenge of Skill is complete. The Challenge of Strength will begin immediately."
    hide orcshaman normal
    with moveoutright
    pause 1
    show orcbase2 at right
    show orcloincloth2 at right
    show orchelmet2 at right
    show orcshoulder2 at right
    show orcstrap2 at right
    show orcwrists2 at right
    show orcaxe2 at right
    show orcemo2 normal at right
    with moveinright
    "The shaman was replaced with a muscular orc wielding a heavy axe. He looked tough... but he wasn't their best. Sabia turned to get her sword and one of the orcs handed it to her."
    "It seemed he wasn't going to yell any challenges. All they had to do was fight."
    scene bg RGAbg4
    $ enemy_type = 1
    $ enemy_skills = [Enemyattack]
    $ enemy_level = 5
    $ enemy_maxhp = 550
    $ enemy_hp = enemy_maxhp
    $ enemy_attack = 70
    $ enemy_defense = 0
    $ enemy_magdefense = 0
    $ GenericOrc2.extras = ["Loincloth", "Helmet", "Strap", "Shoulder", "Wrists", "Axe"]
    $ GenericOrc2.face = "normal"
    $ player = Sabia
    $ enemy = GenericOrc2
    call duel
    if _return == "Victory":
        $ L_orcs += 1
        scene bg RGAbg4
        call sabiabase
        show sabiaemo angry2 at left
        with dissolve
        play music orcritual fadeout 2.0 fadein 2.0
        "Sabia finally took down the huge brute and cast the audience a defiant look. But to her surprise, they didn't appear resentful."
        show sabiaemo surprised2 at left
        "Some of the orcs were even smiling. There were more of them now, watching intently. Did they actually... want her to succeed?"
        show sabiaemo normal at left
        "She couldn't imagine humans doing anything like that, but then, orcs and humans could hardly be more different. Since it helped her, she wasn't going to complain."
    else:
        play music orccamp fadeout 2.0 fadein 2.0
        jump orctrialfailure
    show orcshaman normal at right
    with moveinright
    play sound gong
    orcshaman "The Challenge of Strength is complete. Now there is only the Challenge of Pain."
    show sabiaemo normal at left
    s "..."
    show orcshaman angry2 at right
    orcshaman "Challenger... you must place your hand within this pot and hold it there for a full minute."
    show sabiaemo irritated2 at left
    s "What's inside?"
    show sabiaemo normal at left
    orcshaman "Extracted venom of the scorpion ant. It cannot kill, but the pain has made some warriors go mad."
    show orcshaman happy1 at right
    orcshaman "If you do go mad, we will put you down mercifully out of respect for your successes so far."
    show orcshaman sad2 at right
    orcshaman "But if you can endure until the sand in this glass has run out, then you will be a provisional member of our tribe."
    show orcshaman normal at right
    "The shaman handed a crude hourglass to one of the nearby orcs, then lifted the pot into the air. It contained a clear liquid that looked harmless, but he handled it extremely carefully."
    "He stood completely still, holding the pot tilted toward her. Now there was nothing but this challenge between her and the next step."
    "Sabia took a moment to let her heart rate return to normal, then plunged her hand directly into the liquid."
    show sabiaemo surprised2 at left
    s "Aaaauuuugh!"
    show sabiaemo surprised3 at left
    "She nearly collapsed in the first moment, the pain almost driving her to her knees. It was as if her arm was on fire, and that fire was spreading through her entire body."
    "If she had tried to stick her hand in slowly, she would never have managed it. The intense pain would have made her jerk her hand away immediately."
    show sabiaemo closed2 at left
    "But thrusting her hand in, now the pain almost locked her in place. Every muscle in her body was clenched in agony, but in a perverse way that kept her from withdrawing her hand."
    "Yet her muscles could only clench for so long. Eventually the agony evolved into a deeper ache, as if a stone was grinding away her entire body. Now she felt loose and ready to collapse."
    "Sabia gritted her teeth and resolved to force her way through the last few seconds. She looked to the hourglass to count the final grains..."
    show sabiaemo surprised1 at left
    "Less than a third of it had fallen."
    s "(Impossible... that can't be... it has to be a trick, or... or...)"
    "But as she watched, the sand continued to flow normally. It was nothing but her mind, wrenched out of time by the agony that still shot through her."
    show sabiaemo surprised2 at left
    "Dragging her gaze away from the hourglass, Sabia instead closed her eyes, clenched her own arm, and resolved to suffer through it."
    show sabiaemo closed2 at left
    "First she tried to tell herself that it was only illusory pain, it couldn't harm her if she kept her mind firm."
    "But the pain was so intense, it shredded through any comfort offered by that fact. Sabia started to pull her hand back..."
    show sabiaemo surprised3 at left
    "She forced herself to stop, then instead pushed her hand further in. The poison crept up to part of her wrist it hadn't touched before and her arm partially locked up again, even as the pain intensified."
    s "(Fuck... I've never felt anything this painful...)"
    show sabiaemo angry2 at left
    s "(If barbarian orcs can endure this, I can too! Animals don't know the meaning of self-discipline!)"
    show sabiaemo surprised3 at left
    "But that rationale didn't last very long either, soon she was thinking about how stupid they must be to have a ritual like this. She couldn't last, she couldn't..."
    "Sabia looked at the hourglass, and fortunately saw only a small amount of sand left. Just a little longer."
    "But the sand seemed to flow so slowly, and the pain was getting worse. The fire had gotten inside her bones now, tearing her apart even as she burned."
    "There was blood in her mouth, she must have bitten herself but she didn't remember when. Just another layer of pain added to the others."
    "She couldn't watch the hourglass any longer, that just made it worse. Sabia stared at her hand instead."
    show sabiaemo angry2 at left
    "Everything was stripped away... except her anger. When the agony had destroyed everything, Sabia was left with nothing but raw hatred."
    "Her sister would pay for this. They would all pay. Just as soon as the time ended..."
    show orcshaman happy3 at right
    show sabiaemo surprised2 at left
    "Shocked that it wasn't finished, Sabia looked up... and saw the shaman smirking at her."
    "All the sand had already passed through the hourglass, but he hadn't told her. He just stood there, letting the human suffer agony, enjoying her pain and waiting for her to give up."
    show sabiaemo angry2 at left
    show orcshaman angry3 at right
    play music intense fadeout 3.0 fadein 1.0
    "Anger flooded from deep inside her, eclipsing even the pain. Sabia spat blood out of her mouth, straight into his face."
    show sabiaemo angry1 at left
    s "You think I'm going to give up?"
    show orcshaman surprised at right
    show sabiaemo angry2 at left
    call shake ("h")
    "She shoved her hand deeper into the pot, actually pushing the shaman back a step. She took a step as well, eyes still locked on his."
    show sabiaemo angry1 at left
    s "Never. I will never, {i}ever{/i} give up."
    hide orcshaman surprised
    with moveoutright
    show sabiaemo surprised2 at left
    "The shaman stumbled backward, falling into the sand. The jar went with him, and suddenly her hand was free. Yet there was still a heavy coating of the poison on her hand, and with air flowing over it, the pain was almost worse."
    show sabiaemo closed2 at left
    "She stood there, not sure why she had done something so stupid. It felt like forever, but it was probably only a few seconds before an orc stepped up and used a cloth to wipe off her hand."
    "Sabia almost shouted at him to get away, scorning his pity... but that was when she realized that the orcs were cheering."
    show sabiaemo surprised2 at left
    "All around her, the watching orcs were roaring their approval. She could only stare at them numbly."
    "The removal of the pain was almost worse than the pain itself, her body snapping away from the agony violently. She was suddenly aware of so many smaller pains and an exhaustion that nearly made her collapse."
    play sound gong
    orcshaman "This human... this human is now acknowledged as a member of the tribe!"
    show sabiaemo closed2 at left
    "And with those words, it was done. Sabia wanted to collapse, but couldn't let herself do so. Not while they were still watching her."
    "She spotted the Captains now, further back with their retinues. She knew they had plans for her, but she was too worn out to think about that."
    "Challenges over, the orcs began to disperse. Were they just going to walk off, leave her here?"
    show neve2 at center
    show neveemo happy1 at center
    with moveinleft
    "Just when Sabia was beginning to think she really would collapse, Neve came up beside her, taking her arm in a friendly way that still kept her up."
    show neveemo happy2 at center
    n "Hah! I knew I was right to be interested in you."
    show sabiaemo normal at left
    "Sabia tried to speak, but her jaw seemed locked in place."
    show neveemo happy3 at center
    n "And you should have seen their faces at the end! Heh. A lot of them were skeptical at first, but you won over a lot of them there."
    show sabiaemo closed2 at left
    s "Should I... worry that... I angered the shaman?"
    show neveemo happy2 at center
    n "Oh, you don't need to be worried about that. Orcs have a strange relationship to their shamans."
    show neveemo closed2 at center
    n "If you'd failed due to his cheating, they would have approved of it. He'd have gotten a lot of beers tonight."
    show neveemo happy2 at center
    n "But since you won... well, now he's just a cheater. That will win you more respect."
    show sabiaemo happy3 at left
    s "Then... the trial...?"
    show neveemo normal at center
    n "I'm glad to see you keep your eye on the real goal. Yes, you can definitely be a witness in the trial now."
    show neveemo happy1 at center
    n "I recommend that you rest up, then you should head to the trial as soon as you can."
    "Sabia didn't answer. Sleep seemed like a good idea, so she stumbled to her tent and fell unconscious on top of her sheets."
    scene bg black
    play music orccamp fadeout 2.0 fadein 2.0
    pause 3
    $ L_orcs += 5
    scene bg tent
    call sabiabase
    show sabiaemo closed2 at left
    $ Sabia.hp = Sabia.maxhp
    $ Sabia.stamina = Sabia.maxstamina
    s "(Ugh... did all of that really happen? It seems so insane now...)"
    show sabiaemo irritated2 at left
    s "(But this means I'm an honorary orc... ugh, is that really what I've been reduced to?)"
    show sabiaemo normal at left
    s "(That means the first step is done, though. Now I just need to get through the trial...)"
    jump orctrial


label orctrialfailure:
    call sabiabase
    show sabiaemo surprised3 at left
    "Sabia collapsed backward, failure washing over her as she saw all the eyes on her."
    "She could technically take the trial again, yes. But she knew that it would mean nothing: the orcs had seen her failure and formed their opinions of her."
    "Even if she succeeded a second time, she would never have their respect. Not enough of it to earn the power she needed."
    show orcshaman happy3 at right with moveinright
    orcshaman "So, human. You have failed."
    s "..."
    orcshaman "Though you could attempt the rituals again, you would not get the results you seek."
    orcshaman "There is... another way. Join the order of shamanic warriors and take the extended rituals."
    s "I could do that?"
    orcshaman "Not as you are, humans are too weak. But if you drink this, perhaps you could pass the ritual."
    s "..."
    orcshaman "Well, it is up to you. After your failure, you won't get a better offer."
    hide orcshaman happy3 with moveoutright
    "When the shaman left, Sabia stared at the potion he had handed her for a long time. Honestly, she was desperate..."
    s "..."
    menu:
        "Trust him":
            "Deciding that she had no other choice, Sabia took a sip of the potion. It seemed normal, maybe some crude magic, so she drank the rest."
            "For a while, Sabia noticed no changes. But after long enough had passed, a heat started growing in her body, sliding lower."
            "The next day, she decided to go to the orc tents to earn money. Just part of her plan to work her way back up."
            "Or so she told herself..."
            call badendorctent
            $ renpy.full_restart()
        "Don't trust him":
            "Sabia tossed the potion aside, certain that she couldn't trust the tribe's shaman."
            "But she didn't see any other options. The blow to her reputation was too much."
            "Sabia told herself that she would never give up. But she knew that it was over."
            show gameover with dissolve
            pause 3
            $ renpy.full_restart()


label orctrial:
    if sexworktimes == 0:
        $ dom += 2
    scene bg tent
    call sabiabase
    "Now that she could participate in the trial, Sabia didn't want to waste any time. But when orcs came to take her to another tent as a witness, she realized that she wouldn't have a choice."
    "For a while, Sabia sat there and squirmed. She was getting what she wanted, and she was being treated with more respect now, but in some ways she had even less control. She'd have to play the trial carefully to establish how things would go in the future."
    "When someone entered the tent, Sabia immediately turned to look at them."
    if rokgridalliance == True:
        show rokgrid happy3 at right with moveinright
        r "Well, here we are!"
        show rokgrid happy2 at right
        r "You've done well, Sabia, well indeed. Everyone was quite impressed with your performance at the ritual - if you can gain more respect here, you'll be well on your way to your goal."
        s "Gain respect?"
        show rokgrid normal at right
        r "This trial was already the most important event in our tribe, and your arrival just made it more interesting. I think everyone will be watching your performance closely."
        show sabiaemo closed2 at left
        s "..."
        show rokgrid happy2 at right
        show sabiaemo normal at left
        r "Anyway! I'm sure these ridiculous charges against me will be set aside soon, and you'll play a role in that."
        show rokgrid normal at right
        r "My concern now is for innocents who might be caught in the conflict. Particularly, a humble orc merchant who is being blamed for supplying the group of rogue orcs."
        show sabiaemo annoyed1 at left
        s "And they can just get away with that?"
        show rokgrid sad2 at right
        r "Well, I must admit there is a... rather large amount of evidence that seems to implicate him."
        show rokgrid happy4 at right
        r "But he is quite innocent, I assure you, and he has been a loyal follower of mine."
        show sabiaemo annoyed2 at left
        s "..."
        show rokgrid happy2 at right
        r "All you need to do is say that the party of rogue orcs focused on taking your soldiers' supplies. Well-supplied orcs would not be so desperate."
        show sabiaemo normal at left
        s "I understand."
        if tekrokreject == True:
            $ A_rokgrid += 2
            show rokgrid happy3 at right
            r "Also... I was quite glad to hear that you refused to work with Tekrok. That was a wise choice: he would have all your people in chains."
            r "Perhaps by working together, the two of us can make this tribe into something impressive, hmm?"
        show rokgrid happy2 at right
        r "Well, I wish you all the best during the upcoming trial!"
        hide rokgrid happy2 with moveoutright
    s "..."
    if tekrokalliance == True:
        show tekrok angry2 at right with moveinright
        t "You had better not be thinking of betraying Tekrok, human."
        show sabiaemo irritated2 at left
        s "I'm not an idiot. We made an agreement, didn't we?"
        show tekrok happy1 at right
        t "And now it is time for you to pay Tekrok back. During the trial, you must present this."
        show sabiaemo surprised1 at left
        s "Huh? This cloth... what exactly is this symbol?"
        t "It originates from Rokgrid's clan... and Tekrok wants to make sure everyone knows it was found at the scene of the rogue orcs' attack."
        show sabiaemo eyebrow1 at left
        s "Which it wasn't."
        show tekrok happy1 at right
        t "Yes, it was, after you show it to everyone during the trial."
        show sabiaemo closed1 at left
        s "...fine."
        show tekrok angry2 at right
        t "You had better be on your best behavior, human. This trial is your only chance with Warchief Groknak."
        show sabiaemo normal at left
        s "The Warchief will be there?"
        show tekrok happy1 at right
        t "Who else would make the final decision? The Warchief governs all matters of life and death."
        show tekrok normal at right
        t "Groknak is a traditionalist above all. He will not argue with the ritual, but your presence does {i}not{/i} please him."
        show sabiaemo pout3 at left
        s "..."
        t "But Tekrok thinks this is your chance. Speak strongly, stay in control, and he may not oppose you."
        show sabiaemo normal at left
        s "I'll keep that in mind."
        if rokgridreject == True:
            $ A_tekrok += 2
            show tekrok happy1 at right
            t "Tekrok heard that you refused to work with that weakling Rokgrid. This is good."
            t "Perhaps with this trial we can finally cut out the diseased flesh from the orc tribe!"
            show sabiaemo closed2 at left
            s "..."
        show tekrok normal at right
        show sabiaemo normal at left
        t "Remember, present the cloth during trial. You would regret betraying Tekrok."
        hide tekrok normal with moveoutright
    s "..."
    if dajrabintro == True:
        show dajrab normalclosed at right with moveinright
        if rokgridalliance == True:
            if tekrokalliance == True:
                d "So, you have chosen to play both Tekrok and Rokgrid against each other? A dangerous game indeed."
                s "..."
                d "I will be interested to see what you intend to do. Surely you do not think you can maintain such a ruse for long."
                show sabiaemo irritated2 at left
                s "That's my business and not yours, isn't it?"
            else:
                d "So, you have chosen to throw your lot in with Rokgrid. Interesting."
                show sabiaemo irritated2 at left
                s "What, you have a problem with that?"
                d "I am merely an observer in this conflict. Whoever becomes Warchief, I will remain as a counselor to the tribe."
        elif tekrokalliance == True:
            d "So, you have chosen to throw your lot in with Tekrok. Interesting."
            show sabiaemo irritated2 at left
            s "What, you have a problem with that?"
            d "I am merely an observer in this conflict. Whoever becomes Warchief, I will remain as a counselor to the tribe."
        else:
            d "So, you have chosen to stand aside from orc politics. A valid choice, if a curious one."
            show sabiaemo irritated2 at left
            s "You have a problem with that?"
            d "I like to take the measure of everyone around me. You have made that somewhat more difficult."
            show sabiaemo normal at left
            s "..."
            menu:
                "Say nothing":
                    s "..."
                "I'm only out for myself":
                    $ dom += 1
                    d "Yes, so it seems."
                "Maybe I'm not interested in such unsubtle leaders":
                    $ A_dajrab += 1
                    d "...that's not particularly subtle, either, but I take your meaning. We shall see what you can accomplish in this trial."
        if dajraberrand > 0:
            if dajraberrand >= 4:
                if dajrabtookmoney == True:
                    d "Your decisions have been... interesting. I will be watching you closely."
                else:
                    $ dajrabtrialtip = True
                    show dajrab happy at right
                    d "In any case, you did accomplish the task I set for you. I approve of your efficacy, if nothing else."
                    show dajrab normalclosed at right
                    s "..."
                    show dajrab normalopen at right
                    d "As a token of my regard, I will offer a suggestion for the upcoming trial."
                    d "Our shaman was humiliated during your ritual. He will not forget this, and most likely he will attempt to discredit you during the trial."
                    d "If he attempts to discredit your performance, resist the urge to refute his charges."
                    show dajrab normalclosed at right
                    show sabiaemo eyebrow1 at left
                    s "What, is he going to say I somehow cheated in a ritual I'd never seen before?"
                    d "The facts matter less than the assault. I suggest you return insult for insult - perhaps you could suggest he was unable to gather a strong enough poison."
                    show sabiaemo closed2 at left
                    s "Hmm."
            else:
                $ A_dajrab -= 1
                d "I hope you do not think I will forget that you agreed to my task and then ignored it. An intentional deception? Too distracted to complete it? Unable to do so?"
                s "I ju-"
                d "Actions, not words. I will continue to watch what you choose to do."
        if trialtime <= 18:
            d "One last thing... your presence in the trial has delayed the execution of a warrior. You will likely have a chance to decide his fate."
            d "It does not matter to me whether he lives or dies. I will not tell you who would be pleased by his death, but I will tell you that he is innocent."
            show sabiaemo annoyed1 at left
            s "Why are you telling me this?"
            show dajrab normalopen at right
            d "I am curious about how you will react, that is all."
        show dajrab normalclosed at right
        show sabiaemo normal at left
        d "The trial is almost upon us. I shall be watching, Sabia."
        hide dajrab normalclosed with moveoutright
    s "..."
    "At last, it seemed that Sabia had waited long enough. Two burly orcs stepped into the tent and escorted her directly to the main hall atop the cliff."
    scene bg mainhall
    play music orctrial fadeout 2.0 fadein 2.0
    "As she entered, Sabia tried to hide her reactions. The hall was simple but massive, the ceiling high overhead and lined with many exotic skulls. But the most intimidating thing was the sheer number of orcs in the room, stamping and muttering to each other."
    "Sabia had seen a few peasant trials and knew human crowds could be rowdy as well. But those crowds were rarely this large or this well-armed. She squared her shoulders and resolved to do the best she could."
    show groknak normal at right with dissolve
    "At the far end of the hall sat one of the largest orcs Sabia had ever seen. It could only be Warchief Groknak."
    $ a_list.append("Groknak")
    show groknak normalopen at right
    g "Silence!"
    show groknak normal at right
    "The Warchief's bellow drowned out all of the noise in the hall. Though the orcs did not become silent, not by human standards, they did get a lot quieter."
    play sound gong
    "Once things had become relatively quiet, a gong rang throughout the hall. Sabia traced the sound to one corner, where she saw the tribe's shaman had struck it. He had officially set things off, but there was no question that the real authority lay with Warchief Groknak."
    show groknak normalopen at right
    g "We resume with questioning the witnesses. Hagbak, come forth!"
    hide groknak normalopen with dissolve
    "Sabia blinked in surprise as some random orc came to the center of the room and began to be interrogated by Groknak. It was no one she recognized, either from the attack or from around camp."
    "If they were just going to do something else, why had they brought her here? The orcs that had been escorting her left her at one side of the room, still just confused."
    call sabiabase
    with dissolve
    show neve1 at center
    show neveemo happy2 at center
    with moveinright
    "Just when she was beginning to consider whether or not she needed to take action, Neve slid up beside her."
    n "Feeling rested?"
    show sabiaemo annoyed1 at left
    s "I'm fine. But what is all this? I thought I was supposed to be a dramatic key witness..."
    show sabiaemo normal at left
    show neveemo normal at center
    n "Oh, you are... for the Captains. Not for the Warchief."
    n "He's making you wait to show that he's in control, that you aren't the most important person here. And it's true that whatever he decides will be law here, so don't get on his bad side."
    show neveemo closed1 at center
    n "But he won't drag it on too long - he's not an idiot, he knows most of the orcs are only here because they expect you to force a final decision."
    s "So that's the guy I have to impress, huh?"
    show neveemo happy1 at center
    n "Yes, but the tribe might be more important, depending on what you actually want."
    show sabiaemo closed2 at left
    s "Hmm..."
    if A_neve >= 5:
        $ nevetrialtip = True
        show neveemo happy2 at center
        n "By the way, a little tip? There's been a lot of argument about how many orcs were killed in the attack. A larger number implies a less organized attack, you see."
        show neveemo normal at center
        n "You can manipulate that part of the debate if you want, but I'd advise staying out of it. Just emphasize your own role."
        s "Noted. Thanks, Neve."
        show neveemo happy2 at center
        n "No problem. Have fun out there!"
    else:
        n "Well, do your best, okay? Everybody has high expectations after your membership ritual."
    show neveemo happy1 at center
    hide neve1
    hide neveemo happy1
    with moveoutright
    show sabiaemo normal at left
    "After Neve slipped away, Sabia leaned back against the wall and just watched the trial. Maybe she could learn something about how this would go."
    "Orc jurisprudence seemed to involve a lot of shouting."
    "Though the orcs apparently believed in some kind of shared tribal law, they seemed to think absolutely anyone could shout out their opinion about it."
    "If humans allowed any filthy peasant to do such a thing, they'd be... well, as much of a mess as the orcs."
    "Soon, however, Sabia learned to tune out all the unnecessary shouting and focus on the political movements that mattered. And there was definitely politics going on, more than she would have given orcs credit for."
    if rokgridalliance == True:
        if tekrokalliance == True:
            "Throughout the entire trial, Tekrok was using his subordinate to try to pin charges on Rokgrid. And though he was on the defensive, Rokgrid was trying to frame Tekrok as attacking fellow orcs for personal gain."
            "Sabia sighed and looked between them, wondering who she should support. Pretty soon, she'd need to have made a decision."
        else:
            "Sabia focused on Rokgrid. He was cleverly deflecting Tekrok's attempts to cast suspicion on him, while using each attempt to demonstrate that Tekrok was just out for political gain."
    elif tekrokalliance == True:
        "Sabia focused on Tekrok. He kept trying to get a charge to stick to Rokgrid or his subordinates, but Rokgrid managed to evade them with that same damn smile on his face."
    else:
        "Tekrok and Rokgrid were going at it, trying to blame each other. Sabia's gaze wandered through the crowd and found Dajrab, who watched without participating."
    if trialtime <= 18:
        show orcbase at right
        show orcloincloth at right
        show orcpiercing at right
        show orcshoulder at right
        show orcstrap at right
        show orcwrap at right
        show orcbeard1 at right
        show orcemo normal at right
        with dissolve
        "Their argument seemed to be over the fate of an orc named Kulgan, who didn't seem upset that they were discussing his potential execution. But he was just some minor warrior, so Sabia ignored him."
        "Instead, she tried to figure out what was at stake. Rokgrid didn't seem too interested in defending him, while Tekrok only pushed for his execution as part of his general aggressive tactic."
        "And, then, abruptly, Kulgan turned to face her."
        show orcemo smile3 at right
        orc "Human, please - tell them Kulgan was not among those who attacked you!"
        "Abruptly all eyes were on Sabia. She forced herself not to back down, using the chorus of shouting as a moment to catch her breath. What was she going to do?"
        menu:
            "Say he was absent":
                $ kulganalive = True
                $ A_dajrab += 1
                $ L_orcs += 1
                s "I saw most of the orcs who attacked us, and I didn't see him anywhere."
                show orcemo normal at right
                "Kulgan looked incredibly relieved for a moment before he hid the expression behind a stoic mask. Many of the orcs yelled about her answer, but Groknak just considered quietly for a moment."
                g "Very well. Warchief Groknak finds you not guilty. Be gone from here."
                hide orcbase at right
                hide orcloincloth at right
                hide orcpiercing at right
                hide orcshoulder at right
                hide orcstrap at right
                hide orcwrap at right
                hide orcbeard1 at right
                hide orcemo normal at right
                with moveoutright
                "The result didn't seem to matter too much to the Captains, but it was a popular answer with the common orcs, and she saw Kulgan shoot her a grateful glance as he left."
            "Give no answer":
                $ trialapproval += 1
                $ L_orcs += 2
                s "I have no idea whether or not you were there, I was busy fighting."
                show orcemo angry at right
                "That set off another huge round of arguments. Sabia couldn't follow the exact details, but it was clear that her response had been a popular one with many orcs."
                hide orcbase at right
                hide orcloincloth at right
                hide orcpiercing at right
                hide orcshoulder at right
                hide orcstrap at right
                hide orcwrap at right
                hide orcbeard1 at right
                hide orcemo normal at right
                with moveoutright
                "In the end, Warchief Groknak chose to execute the orc. As he was led away, finally struggling and shouting, Sabia wondered if she should feel guilty. She didn't."
            "Say he was present":
                $ trialtekrok += 1
                $ trialapproval += 2
                s "You want me to lie? I saw you there with all the other traitors."
                show orcemo angry at right
                "Her blunt answer set off a clamor of shouts, mostly of approval. Sabia also saw Tekrok give her a brief nod, satisfaction in his eyes."
                hide orcbase at right
                hide orcloincloth at right
                hide orcpiercing at right
                hide orcshoulder at right
                hide orcstrap at right
                hide orcwrap at right
                hide orcbeard1 at right
                hide orcemo normal at right
                with moveoutright
                "After some more shouting, Warchief Groknak chose to execute the orc. As he was led away, finally struggling and shouting, Sabia wondered if she should feel guilty. She didn't."
        "Now that attention had fallen on her, there would be no more delaying. Sabia realized that it was time."
    else:
        "The current argument seemed to involved the execution of an orc named Kulgan. Whatever the issues were, Sabia didn't figure them out before Groknak declared that his judgment would stand..."
        "And then his eyes turned toward her and Sabia realized that it was time."
    "Trying not to show any weakness, Sabia walked through the orcs to stand in the marked circle in front of Warchief Groknak."
    show groknak normal at right with dissolve
    "He glowered down at her, more to show his authority than anything else. Sabia stared back, trying to take his measure. She saw an orc who was more cautious than he appeared, a shrewdness lurking deep within his eyes."
    g "Human. Warchief Groknak accepts you into our tribe, but you came to us as an enemy."
    s "No, you came to me."
    show groknak angry3 at right
    "She wondered if responding so bluntly had been a mistake, but Groknak only growled, while the watching orcs seemed to give approving shouts. Then again, maybe they just approved of fighting in general."
    show groknak normalopen at right
    g "And what exactly were you humans doing?"
    menu:
        "That's none of your business":
            $ trialapproval += 1
            $ A_groknak -= 1
            show groknak suspicious2 at right
            "Most of the orcs seemed to find this answer hilarious, but Groknak glowered fiercely. When the room quieted down, he gave a low growl."
            g "Do not mock Warchief Groknak. But it doesn't matter, not as much as what happened next."
        "Attempting to secure a valuable ruin":
            $ trialapproval -= 1
            show groknak normal at right
            "To her surprise, the orcs responded with laughter. Sabia had decided to go with the truth in case they had some other source of information, but they seemed to find it hilarious."
            "As her ears burned, Sabia realized that they didn't believe her. Something like that was just a joke to them."
            "Not to the Warchief, however, who seemed to accept it. He would have more experience with humans, after all."
        "Patrolling the borders of Lundar":
            $ trialapproval += 0
            show groknak normal at right
            "This answer prompted mixed shouting from the audience. Some approved, some disapproved, Sabia just watched for what the Warchief would do next."
        "Hunting for bandits":
            $ trialapproval += 1
            show groknak normal at right
            "The orcs around her stamped and shouted in approval. Sabia thought she saw a little skepticism in Warchief Groknak's eyes, but the answer played well and he didn't question it."
        "Attempting to contact the noble orc people":
            $ trialapproval -= 2
            show groknak normal at right
            "As soon as she said the words, Sabia realized she'd made a mistake. The orcs jeered at her, seeing straight through her ploy. Okay, so they weren't as stupid as she thought."
            show groknak angry1 at right
            g "How generous of you. Warchief Groknak is glad you were able to contact us."
            "Sabia glowered at him and after a while, Groknak let the jeers die down and then moved on with the trial."
        "Going to exterminate orcs":
            $ trialapproval -= 5
            $ A_groknak -= 1
            "Sabia didn't try to hide her distaste as she sneered at the orcs. A few chuckled at her audacity, but more just seemed angry. Groknak scowled briefly, then shook his head."
    show groknak normal at right
    g "Whatever the reason, you were attacked dishonorably by rogue orcs from our tribe."
    show groknak normalopen at right
    s "I understand they were traitors. I'm here to make sure justice is done."
    show groknak normal at right
    g "Those who were clearly involved have been executed, but some may have slipped back. To that end, Warchief Groknak asks you to tell us what you can of those who attacked you."
    menu:
        "Describe them as strong":
            $ trialapproval -= 1
            $ trialtekrok += 1
            s "They set upon us furiously, cutting down my warriors left and right. The fighting was fierce but short."
        "Describe them as weak":
            $ trialapproval -= 1
            $ trialrokgrid += 1
            s "They came upon us in great numbers, but they were much weaker than the warriors I have seen here. My own fighters were overwhelmed by their numbers."
        "Describe them as sneaky":
            $ trialapproval += 1
            $ trialrokgrid += 1
            s "Our scouts had detected the presence of some orcs, but we did not think they would set upon us in such a cowardly fashion. Many of my men were cut down before they could pick up their swords."
        "Describe them as pathetic vermin":
            $ trialapproval -= 5
            $ A_groknak -= 1
            s "They were as pathetic as most orcs. Without their numbers and cowardly tactics, we would have cut them apart."
            "That earned her a vicious glare from Warchief Groknak, but a moment later he suppressed the emotion, simply staring at her coldly."
        "Show Tekrok's fake evidence" if tekrokalliance == True:
            $ showedevidence = True
            $ trialapproval += 1
            $ trialtekrok += 2
            s "There is little I can tell you that you do not already know. But I can show you this."
            "Sabia held up the cloth that Tekrok had given her and the audience reacted immediately. She pretended to ignore their roars and spoke as soon as she had the chance."
            s "I tore this from one of the orcs who assaulted me. What to make of it, I leave to you."
            show groknak suspicious1 at right
            g "Hnnh."
            "Groknak took the piece of cloth from her, examined it carefully, then set it aside. Sabia wasn't sure if that was good or bad. She wanted to glance at Tekrok, but that might seem suspicious, so she just stared back at the Warchief."
    show groknak normal at right
    g "Warchief Groknak wishes to hear more of the battle. By the time our scouts came to the site of the battle, humans had already come and gone."
    "That was potentially valuable information, but Sabia had no chance to ask for more. Had allies followed to check on her? Or was it something else entirely?"
    g "Those we have executed described your band of warriors as very small. Is this true?"
    menu:
        "Yes, it was small.":
            $ trialrokgrid += 1
            "The orcs murmured in response and Sabia saw Rokgrid smile slightly from the corner of her eyes."
        "No, it was large.":
            $ trialtekrok += 1
            "The orcs murmured in response and Sabia saw Tekrok nod from the corner of her eyes."
        "We were small and poorly equipped. The attackers would not have done well against a real force." if nevetrialtip == True:
            $ trialrokgrid += 2
            "The orcs shouted so much in response that Sabia thought she might have overdone it."
            "But no, she saw Rokgrid give a satisfied smile, so it must have been effective."
        "We were strong and well-equipped. It is surprising the attackers were able to defeat us." if nevetrialtip == True:
            $ trialtekrok += 2
            "The orcs shouted so much in response that Sabia thought she might have overdone it."
            "But no, she saw Tekrok smirk, so it must have been effective."
        "The battle began too quickly for me to tell. All I can say is that I fought until I was alone." if nevetrialtip == True:
            $ trialapproval += 1
            $ L_orcs += 1
            "That prompted a roar of approval from the surrounding crowd. Both Rokgrid and Tekrok only watched speculatively, but Sabia didn't really care."
            "The sound of so many orcs shouting approval like that... it was a remarkable feeling. Sabia liked being in command, but all her positions had been granted her by her family's position. This..."
            "No, she couldn't entertain such thoughts. Sabia refocused on the trial and did her best to filter out the shouting."
    "Warchief Groknak, meanwhile, kept his response hidden. Either he truly didn't care, or he kept his emotions far better controlled than she had given him credit for."
    g "And when the battle was over... what happened then?"
    if startcondition == "gangbang":
        "The thought of the rogue orcs defeating her made Sabia hesitate for a moment. Telling the truth would definitely not play well with this audience..."
    elif startcondition == "sex":
        "Sabia hesitated, thinking of how the second band had defeated her. Was the truth really the best answer in this scenario?"
    else:
        "Sabia wondered if talking her way out of the situation would play well with this crowd. There weren't many alive to say otherwise..."

    menu:
        "The rogue orcs defeated me":
            "That answer prompted more than a few angry comments, but also some rumblings of discontent. Sabia stood tall and tried to ignore them."
            $ trialapproval -= 1
            if startcondition == "gangbang":
                $ A_lutvrog += 1
            elif startcondition == "sex":
                $ A_lutvrog -= 1
                $ lutvrogtriallie = True
            else:
                $ A_lutvrog -= 1
                $ lutvrogtriallie = True
        "The band of orcs you sent defeated me":
            "That answer prompted a few angry comments and loud rumblings of discontent. Sabia stood tall and tried to ignore them."
            $ trialapproval -= 2
            if startcondition == "gangbang":
                $ A_lutvrog -= 1
                $ lutvrogtriallie = True
            elif startcondition == "sex":
                $ A_lutvrog -= 1
                $ lutvrogtriallie = True
            else:
                $ A_lutvrog -= 1
                $ lutvrogtriallie = True
        "I lost a duel to your band of orcs":
            "That answer prompted a chorus of shouts, some kind of argument she didn't exactly follow. It seemed quite contentious, but only among the lesser orcs."
            "It was something about the rights of warrior challenges, but in the end Groknak dismissed them and shouted until they all shut up."
            $ trialapproval += 0
            if startcondition == "gangbang":
                $ A_lutvrog -= 1
                $ lutvrogtriallie = True
            elif startcondition == "sex":
                $ A_lutvrog += 1
            else:
                $ A_lutvrog -= 1
                $ lutvrogtriallie = True
        "I held them off until I was knocked unconscious by your band of orcs":
            "The orcs were mostly quiet at this, but a few did give approving grunts."
            $ trialapproval += 1
            if startcondition == "gangbang":
                $ A_lutvrog -= 1
                $ lutvrogtriallie = True
            elif startcondition == "sex":
                $ A_lutvrog -= 1
                $ lutvrogtriallie = True
            else:
                $ A_lutvrog += 1
    show groknak normal at right
    g "There is one more charge Warchief Groknak wishes to ask about. Look at these."
    "He gestured to another orc and a cloth was opened nearby, resulting in several helmets clanging onto the floor. Many had stains of blood and tufts of hair still on them."
    show groknak angry1 at right
    g "These are the helmets of other traitors. Warchief Groknak asks if these are the same as those who attacked you."
    show groknak normal at right
    show sabiaemo surprised1 at left
    "Blinking, Sabia pretended to examine them while desperately thinking on her feet. What exactly was this supposed to mean?"
    show sabiaemo closed2 at left
    "In terms of the truth, she had absolutely no idea. All orc helmets looked equally ugly and crude to her. But the truth wouldn't get her anywhere, so she needed to decide what lie was best."
    if rokgridalliance == True:
        "She caught a glimpse of Rokgrid looking anxious and made the connection. Most likely these helms would implicate his merchant somehow."
    else:
        "But after examining them for a while, Sabia didn't gain any particular insight. She would just have to trust her instincts."
    show sabiaemo normal at left
    menu:
        "I'm not sure.":
            $ trialapproval += 1
            "Her answer made the gathered orcs rumble in disapproval, but she saw the Captains glower at each other. It had been a neutral response, at least."
            "The issue didn't seem to matter to Warchief Groknak at all. He irritably gestured for the helms to be taken away and instead turned his full attention on her."
        "They look exactly the same.":
            $ trialtekrok += 2
            "The answer prompted a roar, and she spotted Tekrok cast a smug glance toward Rokgrid."
            "The issue didn't seem to matter to Warchief Groknak at all. He irritably gestured for the helms to be taken away and instead turned his full attention on her."
        "They look completely different.":
            $ trialrokgrid += 1
            "The answer prompted a roar, and though Tekrok glared at Rokgrid, the other Captain refused to change his expression from one of simple calm."
            "The issue didn't seem to matter to Warchief Groknak at all. He irritably gestured for the helms to be taken away and instead turned his full attention on her."
        "The orcs were trying to steal supplies, including helmets" if rokgridalliance == True:
            $ rokgriddeal = True
            $ trialrokgrid += 2
            "This seemed like a controversial answer. Sabia judged that the crowd was too mixed to go one way or the other, while Warchief Groknak frowned thoughtfully."
            "Rokgrid, however, gave her a slight nod of thanks."
        "All orc filth looks the same to me.":
            $ trialapproval -= 5
            $ A_groknak -= 1
            "The answer prompted a roar of anger, and Groknak's eyes flashed furiously."
    show groknak normalopen at right
    g "Warrior Sabia. Do you swear you have told the complete truth before the tribe?"
    s "Of course."
    if A_groknak <= -2:
        if lutvrogtriallie == True:
            "The Warchief growled deep in his throat and Sabia flinched. For the first time, she saw raw fury burn in his eyes."
            g "You come into our camp, scorn us at every turn... and now you lie before Warchief Groknak?"
            "Sabia realized that she had overstepped, knew that she should apologize, but she couldn't. The idea of groveling in apology to these savages was more than she could bear."
            g "Warriors! Step forward and cast judgment on this human!"
            "With no idea what was going on, Sabia could only stand and wait as orcs came forward to speak about her. Many condemned her, a few spoke in her favor, but she suspected that all that mattered was Groknak's furious glare."
            "Lutvrog gave her an apologetic look, but told them that she had been dishonest about how the battle took place. Meanwhile, the shaman went out of his way to portray her as untrustworthy, smirking at her the entire time."
            "In response, Sabia couldn't help but sneer. These primitive orcs thought they had the moral high ground to pass judgment on her? Her?"
            "At last, it was over, and the Warchief stood to his feet."
            g "Judgment has been passed. Human, you are a warrior no longer."
            s "As if I'd want to be anything in your miserable littl-"
            "A club took her in the back of the head and everything went black."
            scene bg black
            pause 3
            call badendorctrial
            $ renpy.full_restart()
        else:
            "That one was the easiest lie of all. The answer seemed to satisfy Warchief Groknak enough, so he nodded and stepped back."
    else:
        "That one was the easiest lie of all. The answer seemed to satisfy Warchief Groknak enough, so he nodded and stepped back."
    hide groknak normalopen with moveoutright
    "That left Sabia standing awkwardly in the circle. Was she supposed to go back? Was staying here making some kind of mistake?"
    show orcshaman normal at right with moveinright
    "But before she could agonize over the decision for too long, the shaman approached her. He thumped his chest a few times for silence, then began speaking."
    show orcshaman angry1 at right
    orcshaman "This human may have completed our rituals, but that does not mean she is a good witness."
    show sabiaemo annoyed1 at left
    s "What? I'm basically the only witness!"
    show orcshaman angry3 at right
    orcshaman "Orcs, speak... if something was stolen from the tribe, would the only person there at the time be a trustworthy witness?"
    show sabiaemo surprised1 at left
    "Sabia's eyes widened as she realized what he intended to do. Proving herself could be difficult, especially if the Captains didn't help, but she had to try."
    show sabiaemo angry1 at left
    s "You can't possibly think I could be behind the rogue orcs."
    show orcshaman happy1 at right
    orcshaman "No. But you have not proved that you are trustworthy enough to tell us about them."
    show orcshaman angry3 at right
    orcshaman "Orcs, speak: what is to stop this filthy human from saying anything for a few coins?"
    orcshaman "You've seen her here, scrabbling in the filth, cheating her way through the rituals..."
    show sabiaemo angry2 at left
    s "Grr..."
    menu:
        "I'm more trustworthy than you!":
            $ trialapproval += 0
            "That set off a shouting match among all the listening orcs. Sabia was surprised how many of them seemed to be on her side, but it was utter chaos that completely stopped the room's momentum."
        "I didn't have any other options!":
            $ trialapproval -= 1
            "That set off a shouting match among all the listening orcs. Some of them even seemed to be on her side, it was utter chaos that completely stopped the room's momentum."
        "I didn't cheat!":
            $ trialapproval -= 1
            "That set off a shouting match among all the listening orcs. Some of them even seemed to be on her side, it was utter chaos that completely stopped the room's momentum."
        "You're the one who cheated!":
            $ trialapproval += 0
            "That set off a shouting match among all the listening orcs. Sabia was surprised how many of them seemed to be on her side, but it was utter chaos that completely stopped the room's momentum."
        "You're just angry because you couldn't do the ritual right." if dajrabtrialtip == True:
            $ trialapproval += 2
            show sabiaemo eyebrow1 at left
            "Sabia did her best to sneer, and she was pretty damn good at sneering. There was a pause for a moment as the orcs seemed surprised, then laughter and jeering."
            "It wasn't all in support of her, but judging from the shaman's rage, it hadn't gone his way either. She'd simply thrown his accusation back at him as if it wasn't worthy of her attention."
            "Since she doubted she could control a room this rowdy, Sabia just stood with her arms crossed and didn't back down as the orcs shouted all around them."
    g "Enough!"
    show sabiaemo normal at left
    "The Warchief's voice quieted the room quickly. He sighed and fixed them both with a glare."
    g "Shaman, the ritual is done. If you have an objection, state it clearly."
    show orcshaman angry3 at right
    orcshaman "To be a witness, one must be a member of the tribe... and be in good standing. Is this {i}human{/i} in good standing?"
    hide orcshaman angry3 with moveoutright
    "With that, he backed away, as if he had made his point. Judging from the way the orcs reacted, he seemed to have started something, but Sabia wasn't sure what."
    scene bg mainhall with dissolve
    "Sabia was pushed aside to clear the circle. Still not certain what was going on, she followed directions and watched to try to figure out her angle on things."
    "One by one, orcs began to come forward and speak. Most she didn't even recognize, and they just gave their approval or disapproval of her."
    "Did orcs really decide approval by mass opinion like this? What an utterly absurd system. There didn't seem to be any voting, it was just shouting, and occasional attempts to persuade."
    "And Warchief Groknak just sat back and watched the entire thing. It was little better than mob rule."
    "Before it could go on too long, an older orc stepped forward and raised his hands. He actually got silence and the crowd began listening to him."
    if L_orcs >= 10:
        if L_orcs >= 20:
            $ dom += 1
            $ sub += 1
            $ trialapproval += 1
            $ A_groknak += 1
            $ A_tekrok += 1
            $ A_rokgrid += 1
            $ A_dajrab += 1
        $ trialapproval += 3
        orc "Since she has come here, Sabia has proven she is not like the rest of her kind. We should listen to her."
        "This prompted a surprisingly large chorus of agreement. Sabia did her best not to show anything on her face, but she couldn't help feeling a little smug. She could do this."
    elif L_orcs >= 5:
        $ trialapproval += 1
        orc "Once, we were all skeptical of this human. But she has been civil, has respected our ways. She should be able to speak."
        "This prompted a chorus of agreement, though some disagreed. Sabia pretended to ignore both and just watched impassively."
    else:
        $ trialapproval -= 1
        orc "The human has showed nothing but contempt for our ways. She has no place here."
        "Apparently the old fool's voice held some weight, because many orcs shouted in agreement. Sabia scowled, but doubted she could have done any better at respecting the savages' filthy ways."
    if L_orcs >= 5:
        if sparrespect >= 5:
            $ trialapproval += 1
            "A warrior Sabia recognized from the training grounds stood up and nodded."
            orc "Yes. This one has fought bravely against many warriors - she has more right to speak here than many listening."
            "That prompted a few jeers, but Sabia didn't think they were directed at her. She had a hard time gauging the crowd, but it seemed mostly on her side."
    else:
        if sparrespect >= 5:
            $ trialapproval += 1
            "A warrior Sabia recognized from the training grounds stood up and shook his head."
            orc "No. This one has fought bravely against many warriors. She should speak."
            "That prompted a mixed and very loud reaction. Sabia had a hard time gauging the crowd and hoped things would go in her favor."
    $ temp1 = foresthunting
    $ temp1 += bartimes
    if temp1 <= cleaningtimes:
        $ trialapproval -= 1
        "Another orc stood up to speak, and Sabia recognized with annoyance the one who ran the cleaning on the main grounds."
        orc "This female is no warrior. Every day, she does nothing but clean up our waste."
        "He left after that, apparently just wanting to take the opportunity to heap scorn on her. It seemed like a few of the orcs listening disapproved as well."
        "Sabia marked that orc for death later and did her best to ignore it. There were a lot of opinions, his was only one. She'd done what she had to do."
    if tekrokcrewscene == True:
        $ trialapproval += 2
        "To Sabia's surprise, a large number of orcs spoke in her favor in a row, saying surprisingly positive things about her. They looked familiar, Sabia tried to puzzle it out..."
        "Abruptly she realized that they were all among Tekrok's men, specifically the ones that had fucked her in the tents. Just as she realized it, one of the orcs turning away gave her a sly wink."
        "She blushed and glowered at no one in particular. Well, if she was using her body to get ahead, at least she was getting what she wanted."
    "For a while, only random orcs came to speak. If she'd had any scrap of respect for their method of government, it was rapidly burning away."
    if foresthunting >= 5:
        $ trialapproval += 1
        "To Sabia's surprise, the orc in charge of hunting testified that she'd contributed food to the tribe in return for the normal compensation of any orc. "
    if bartimes >= 5:
        $ trialapproval += 1
        "Just as Sabia was starting to get bored, she recognized a few of the orcs who frequented the Silvertusk Bar. They couldn't say too much in her favor, and one just talked about her outfit, but at least they weren't voicing negative opinions."
    if sexworktimes >= 10:
        $ trialapproval += 1
        "As speakers began to become less frequent, it seemed things were about to end. But before they did, one more orc came to speak. He was one of the main guards at the relief tents, so Sabia knew him well."
        orc "This human is one of the hardest workers we have ever seen. She does more than those of you who sit on your asses in camp."
        "With that, he stomped away. Sabia blinked, having expected him to mock her for her work there. Well, it seemed like she'd misjudged him."
        "That, or he just hoped to get a free blowjob later."
    elif sexworktimes >= 3:
        $ trialapproval -= 1
        "As speakers began to become less frequent, it seemed things were about to end. But before they did, one more orc came to speak. Sabia recognized him as one of the guards from the relief tents."
        orc "This human will sell her body for a few coins. Will she not sell the truth as well?"
        "With that, he cast her a glance of disgust and stomped away. Sabia scowled, wanting to argue back, but just let him go."
    elif sexworktimes == 0:
        $ trialapproval += 1
        "As speakers began to become less frequent, it seemed things were about to end. But before they did, one more orc came to speak. Sabia thought she vaguely recognized him as one of the guards from the relief tents."
        orc "This human is not like the other sluts. She could have earned more by selling herself, but did not. I do not believe she will sell the truth, either."
        "With that, he stomped away. Sabia stared at his sloped brow, shocked that he could put together such a coherent sentence. Well, she'd misjudged him."
    "With that, it seemed that the time for speaking had finally wound down. Warchief Groknak rose to his feet again and folded his powerful arms."
    show groknak normalopen at left
    show orcshaman normal at right
    with dissolve
    g "Orcs? Who do you support?"
    show groknak normal at left
    if trialapproval >= 10:
        "The response was immediate: almost all the orcs in the hall roared together as one:"
    elif trialapproval >= 5:
        "After a brief pause, the shouting of the crowds came together in a single chant."
    else:
        "There was an uncomfortably long period where the orcs shouted against each other, but eventually their voices came together as one."
    show orcshaman surprised at right
    "Sabia! Sabia! Sabia!"
    "A chill went down Sabia's spine at the sound of so many rough voices shouting her name. If there had been any doubt she had won, it was eliminated by the sour look on the shaman's face."
    "He looked like he was going to slink away in defeat, but Sabia noticed that some orcs were starting to look in her direction again. Maybe she could speak now - if so, this was her last chance to influence them, but it would be hard to make an impact over all the noise."
    menu:
        "Submission: So, am I in good standing?" if sub >= 2:
            $ trialapproval += 1
            "Sabia gave the shaman her sweetest smile. The orcs might have been brutes, but they knew mockery when they saw it and roared in laughter."
        "(Ignore him.)":
            "Deciding he was beneath her attention, Sabia pointedly pretended not to look at him."
        "Get out of here!":
            "It might not have accomplished anything, but Sabia felt a huge rush of satisfaction to dismiss the shaman to his face."
        "Domination: Bring a stronger poison next time!" if dom >= 2:
            $ trialapproval += 1
            "The orcs roared in approval at her mockery, one near her even slapping her on the back violently."
    show orcshaman angry2 at right
    "The shaman just stared at her for a moment, then walked away."
    hide orcshaman with moveoutright
    "He couldn't afford to challenge her directly, not after she had bested him twice in a row. But that did not mean he couldn't get in her way. Sabia resolved to keep an eye on him."
    show groknak normalopen at right with moveinright
    call sabiabase
    with dissolve
    g "Thank you, warrior. Your role in this trial is over, you may go."
    show groknak normal at right
    "Sabia was surprised it was over that quickly, but she nodded and walked away."
    hide groknak normal with dissolve
    "Not out of the hall entirely, though. For one, she wanted to see what would happen next. For another, she wasn't sure she could get that far."
    "When she got near the back wall, her legs were trembling. Sabia leaned back against the wall, trying to look casual, but she felt exhausted."
    "It was nowhere near as complex as the political games played in Lundar, but the trial had still taken a lot out of her. It was all so... forceful. So rough and loud, yet there were still lies and games here she needed to focus on."
    d "Dajrab has not been involved with such activities, but Dajrab has seen much contraband pass through the camp..."
    "Dajrab was on the stand next? Sabia managed to focus on him for a while, determining that he was talking about secondary matters. It was dry, maybe Groknak wanted to bring things back down after her intense questioning."
    "Her head ached too much for her to pay attention. She listened for her name or anything critical while she let her eyes wander over the hall idly, just resting a little."
    show lutvrogbase at right
    show lutvrogemo normal at right
    with dissolve
    "Sabia was broken from her reverie when Lutvrog appeared in the central ring. Obviously he was going to be called in a trial like this, but his appearance still put her on edge."
    "Fortunately, Lutvrog was carefully neutral with every word. As she'd hoped, he took no part in the conflicts between Captains."
    if lutvrogtriallie == True:
        $ trialapproval -= 2
        "Just when she was beginning to think it was fine, Lutvrog paused, then glanced toward her briefly."
        show lutvrogemo suspicious at right
        lut "There is one more thing Lutvrog must say. Warrior Sabia has spoken well, but her account of the accident differed in one crucial way."
        "And with that, he set about describing what had actually happened in humiliating detail. The orcs seemed to disapprove strongly of her lie, but Sabia found herself more bothered by Lutvrog."
        "His eyes radiated stern disapproval. Not for anything that had happened, but for the fact that she had lied about it. As if she had failed some moral code."
        "Sabia didn't flinch or turn away. Let him disapprove if he wanted, she would do what she had to do."
    else:
        if lutvrogsex == True:
            $ A_lutvrog += 1
            "Once he had said his piece, Lutvrog nodded to the Warchief and left."
            "Sabia found herself conflicted about what he had said. Part of her wanted him to have spoken up for her - hadn't she beaten him and given him a great fuck?"
            "But another part of her was pleased he was so carefully neutral. He wasn't like the other orcs, wasn't like a lot of humans. She might need to play games of deceit, but she could respect his honor."
        else:
            "Once he had said his piece, Lutvrog nodded to the Warchief, then walked away. The warriors of the tribe parted enough to let him through and she saw several nod to him in respect."
    show lutvrogemo normal at right
    hide lutvrogbase
    hide lutvrogemo normal
    with moveoutright
    "With Lutvrog's questioning done, it seemed that the trial was truly ending. The orcs all stared at the Warchief, who considered for a moment before shaking his head."
    g "One hour. Warchief Groknak will consider all that has been said and then decide."
    "A surprisingly large number of orcs whooped in response. That must mean his decision was actually going to be the final one. This trial had been the major event in the camp for a long time, but it seemed her testimony had brought it to an end."
    "At least, it would be over in an hour."
    scene bg mainhall
    call sabiabase
    "Sabia was taken back to the exterior of the building to wait. Most of the other orcs dispersed as well, many going back to camp. No one told her she needed to stay, but Sabia decided to wait for the decision."
    "The wait let her get off her feet and rest a little, which was welcome. Once the tension drained away, though, Sabia actually felt stronger than before."
    "She wasn't sure how well she had accomplished the manipulations she wanted, but none of that really mattered. What she needed was to prove herself as a witness and take another step toward using these orcs for her revenge."
    "Whatever else had happened, she was completely confident that she had accomplished that. The Captains and all the others could die for all she cared, so long as she could use the tribe."
    show groknak normal at right with moveinright
    "And then, without warning, the Warchief appeared."
    "Sabia almost tried to reach for a weapon before realizing that was idiocy. It wasn't like the Warchief of the whole tribe had any need to attack her."
    "He was a fearsome orc up close, though. Though he looked brutish to her compared to the Captains or the other orcs she'd come to know, Sabia reminded herself that to stay Warchief, he had to be skilled and at least somewhat smart."
    show groknak normalopen at right
    g "What are you doing, human?"
    show groknak normal at right
    "He sounded different. His voice was still deep and rough, but there was a subtle change. Now he was just talking to her, not speaking to the tribe, and he knew the difference between those two."
    g "We've captured humans before. Groknak has seen many. Some die, some run, some work in the tents."
    show groknak angry3 at right
    g "But not you. You have come here and upset the balance Groknak has worked so hard to keep."
    show sabiaemo annoyed1 at left
    s "I upset the balance? But don't you make the final decision?"
    show groknak normal at right
    g "Groknak is the voice of the tribe. Groknak can only see the evidence and express their will."
    show sabiaemo normal at left
    s "And...?"
    show groknak suspicious1 at right
    g "Groknak has decided."
    if trialtekrok > trialrokgrid:
        $ trialoutcome = "tekrok"
        show groknak suspicious2 at right
        g "Clearly, Rokgrid was up to something. But the evidence is not there, and Groknak does not accuse without evidence."
        g "All orcs under suspicion will be executed, so that Rokgrid will not attempt such trickery again."
    else:
        $ trialoutcome = "rokgrid"
        show groknak suspicious2 at right
        g "Clearly, Tekrok was attempting to manipulate the tribe's justice. This is no crime, but Groknak will remember."
        g "Groknak will pardon the remaining orcs, even those Groknak thinks may have known. Tekrok should not do such things."
    show sabiaemo closed1 at left
    s "So... what is your final decision, then?"
    show groknak normal at right
    g "Many decisions are already final. The traitors are executed. Those who collaborated with them have been punished."
    g "The Captains... will continue to scheme. That is the way of the tribe. Groknak knows this."
    show sabiaemo normal at left
    s "I see. What do-"
    show groknak angry3 at right
    g "But Groknak does not know you, human."
    if trialapproval >= 12:
        $ A_groknak += 4
        $ L_orcs += 3
        $ groknakimpressed = True
        g "You managed to manipulate the entire trial. Effortlessly. There is something about you..."
    elif trialapproval >= 10:
        $ A_groknak += 3
        $ L_orcs += 2
        $ groknakimpressed = True
        g "You managed to manipulate the entire trial. There is something about you..."
    elif trialapproval >= 8:
        $ A_groknak += 2
        $ L_orcs += 1
        g "You influenced more orcs than Groknak believed any human could. There is something about you..."
    elif trialapproval >= 4:
        $ A_groknak += 1
        g "You actually had some influence on the tribe. Groknak would not have believed it possible. There is something about you..."
    elif trialapproval >= 0:
        g "Despite everything, you had an impact on the trial. There is something about you..."
    else:
        g "You may not have done well in the trial... but you should not have been here at all. There is something about you..."
    show sabiaemo closed2 at left
    s "I have no interest in the tribe's battles. But I was betrayed by my own, just as the rogue band betrayed the tribe. Now I have no choice but to work from here."
    show groknak angry2 at right
    g "You think you can use the tribe for your wars? Do not be a fool, human."
    show sabiaemo normal at left
    s "I didn't say that. I just need to use the camp as a base if I'm going to recover."
    if lutvrogtriallie == True:
        $ A_groknak -= 2
        g "And do not think Groknak will forget that you lied. You swore you told the truth, but Lutvrog said otherwise. A human who lies once, even about a small thing, will lie again."
    else:
        show groknak normal at right
        g "So you say. Groknak will wait, and watch."
    s "..."
    show groknak suspicious1 at right
    g "It would be best for both of us if Groknak never hears your name again. Do what you will here, human, you are one of us. But not all that can be done should be done."
    hide groknak suspicious1 with moveoutright
    play sound gong
    "With that, the Warchief departed. The gong sounded again and the orcs began to filter back into the main hall, but Sabia didn't join them."
    "She'd heard the decision straight from Warchief Groknak, after all. At this stage, all that mattered was what the orcs thought about it."
    scene bg tent
    call sabiabase
    "Sabia headed back to her tent and waited. It wasn't long before someone arrived."
    if showedevidence == True:
        if rokgriddeal == True:
            $ tekrokalliance = False
            $ rokgridalliance = False
            $ A_tekrok -= 3
            $ A_rokgrid -= 3
            show tekrok angry1 at center
            show rokgrid angry1 at right
            with moveinright
            t "What the hell, human?"
            r "Yes, this is most disturbing."
            show sabiaemo angry2 at left
            s "...shit."
            show rokgrid angry2 at right
            r "Did you truly believe us so full of hate that we would not realize you were trying to play us both?"
            show rokgrid angry1 at right
            show tekrok angry2 at center
            t "Tekrok may despise this one, but he is no fool."
            show sabiaemo closed3 at left
            s "Both of you asked me to do something. I did both things. Is it my fault if you wanted me to participate in your little schemes?"
            show sabiaemo normal at left
            show tekrok angry1 at center
            t "Hmph. You will regret this, human!"
            r "Technically, you are correct. But I hope you do not expect any great reward from us."
            hide tekrok angry1
            hide rokgrid angry1
            with moveoutright
            show sabiaemo angry1 at left
            s "...bah. If I can get enough influence with the orcs, I won't need either of them."
            jump trialaftermath
    if tekrokalliance == True:
        show tekrok normal at right with moveinright
        if showedevidence == True:
            $ A_tekrok += 2
            t "Hmph. That wasn't what Tekrok wanted, but Tekrok cannot blame you."
            t "Tekrok asked you to show the evidence and you did. Rokgrid is too slippery."
            show sabiaemo happy1 at left
            s "So, do we have a deal? You'll fight who I want?"
            show tekrok happy2 at right
            show sabiaemo irritated1 at left
            t "Did you really think it would be so simple, human? You cannot control Tekrok so easily."
            if trialoutcome == "tekrok":
                $ A_tekrok += 2
                show tekrok happy1 at right
                t "But... you have been very useful. Much suspicion was cast on Rokgrid, and Tekrok approves."
                t "Tekrok owes you a favor, human. Continue being useful, and perhaps you will have what you want."
            else:
                $ A_tekrok -= 1
                show tekrok angry2 at right
                t "You presented the evidence, but the trial still went against Tekrok. In the future, you must do better."
                show sabiaemo angry1 at left
                s "That's not fair!"
                t "Nothing is fair. But Tekrok will give you a chance to try again, human."
        else:
            $ A_tekrok -= 2
            show tekrok angry1 at right
            t "What the hell was that? We had an agreement!"
            show sabiaemo closed1 at left
            s "I... thought I would get another chance to show the cloth."
            show tekrok angry2 at right
            t "Tekrok thinks you lie."
            show sabiaemo irritated1 at left
            s "..."
            t "It is your fault that Rokgrid still lives. Tekrok will remember this!"
        show tekrok normal at right
        hide tekrok normal with moveoutright
        show sabiaemo angry1 at left
        s "Bastard... but I knew something like this was likely to happen. It's still a step in the right direction."
    if rokgridalliance == True:
        show rokgrid normal at right
        if rokgriddeal == True:
            $ A_rokgrid += 2
            show rokgrid happy3 at right
            r "Sabia! Truly, you are an honorable warrior!"
            show sabiaemo happy1 at left
            s "You got everything you wanted, right?"
            show rokgrid happy2 at right
            r "Well, there is a great deal I would have wanted. But an innocent merchant is still alive thanks to your testimony."
            if trialoutcome == "rokgrid":
                $ A_rokgrid += 2
                show sabiaemo happy1 at left
                s "And the trial went in your favor overall, right?"
                show rokgrid happy3 at right
                r "Yes, the result was excellent. All of Tekrok's lies have been turned aside and for once justice has prevailed."
            else:
                $ A_rokgrid -= 1
                show rokgrid sad1 at right
                r "Unfortunately, the trial as a whole led Warchief Groknak to support some of Tekrok's suspicions. That will be... a difficulty for me."
            show rokgrid normal at right
            r "We will have much to discuss in the coming days."
            s "Starting with using your warriors like you promised?"
            r "And I still hope to fulfill my promises. But to use orc warriors for such things, we will need to take a great many more steps."
            show rokgrid happy2 at right
            r "Fare well, Sabia. I am sure we will speak again soon."
        else:
            $ A_rokgrid -= 1
            show rokgrid sad2 at right
            r "I am very disappointed in you, Sabia. I had hoped you could save the life of that poor merchant."
            show sabiaemo surprised2 at left
            s "Was that what the helmets were about? You should have told me!"
            show rokgrid sad1 at right
            r "It was impossible to know exactly what would happen. I understand how you might have been confused, but... I am still disappointed."
            if trialoutcome == "rokgrid":
                $ A_rokgrid += 1
                show sabiaemo irritated1 at left
                s "I did the best I could. The trial went in your favor, didn't it?"
                show rokgrid normal at right
                show sabiaemo normal at left
                r "Overall, yes. And I will remember that as well, Sabia, make no mistake."
            else:
                show rokgrid sad1 at right
                r "And to make everything worse, the trial as a whole led Warchief Groknak to support some of Tekrok's suspicions. That will be... a difficulty for me."
            show rokgrid normal at right
            show sabiaemo closed2 at left
            r "We will have much to discuss in the coming days."
            s "Starting with using your warriors like you promised?"
            r "It is no small thing, to use orc warriors for such purposes. Given this setback, I do not know how helpful I can be to you."
            r "Fare well, Sabia. I am sure we will speak again soon."
        show rokgrid normal at right
        hide rokgrid normal with moveoutright
        show sabiaemo closed1 at left
        s "I should have known he wouldn't just let me use him so easily. It doesn't matter, this is still a step closer to my goal."


label trialaftermath:
    show neve1 at right
    show neveemo normal at right
    with moveinright
    show sabiaemo normal at left
    n "So, I bet you're pleased with yourself."
    n "I wasn't planning on visiting you until you'd gotten some rest, but it seems you managed to avoid getting too involved with orc politics."
    show sabiaemo happy2 at left
    s "Oh, I wouldn't say that. But I'm not taking any of these irrelevant sides, this conflict is just a problem I have to deal with."
    show neveemo closed1 at right
    show sabiaemo normal at left
    n "There... is one other thing. The location where your soldiers were supposedly searching for ruins..."
    show sabiaemo surprised1 at left
    s "How do you know that?"
    show neveemo normal at right
    n "I have my ways. But I was more struck by the odd fact that there don't seem to be any ruins there at all."
    show sabiaemo surprised2 at left
    s "What? It was a large area, how can you be sure you didn't just miss them?"
    show neveemo closed4 at right
    n "I have somewhat of an interest in ruins myself, Sabia. And believe me, I am certain there was nothing in that region. Makes one wonder if you were telling the truth about why your patrol was there in the first place..."
    show sabiaemo closed2 at left
    s "..."
    show sabiaemo irritated1 at left
    s "The real question is if you're lying to me. And if you aren't... why someone else would lie to me."
    show neveemo happy3 at right
    n "Oh? That sounds like a rather interesting question... but I will leave that to you, Sabia. I'll be watching with interest."
    hide neve1
    hide neveemo happy3
    with moveoutright


label tyralynn1:
    s "There's no way I can just go back. By the time I returned, Lynn would have too much control."
    s "Most likely I'll be declared fallen in the battle. If I go back without proof of my identity, I'd never be able to mount a real challenge to her."
    s "Especially since I don't know how deep the betrayal goes. At the very best, Lynn is manipulating our mother, and that puts me in a terrible position."
    s "Shit... I thought Lynn would move against the Order of Relona long before she tried to eliminate me. I guess she got the upper hand on me here."
    s "But you made a mistake, Lynn. I'm still alive."
    s "And I'm coming for you."
    scene bg black with dissolve
    pause 1
    call lynnintroscene
    play music lundar fadeout 2.0 fadein 2.0
    scene bg black with dissolve
    pause 1
    scene bg throne
    show expression "database/actors/lynn/lynn1.png" as lynn at right
    show expression "database/actors/tyra/tyra1.jpg" as tyra behind lynn
    with dissolve
    l "It's just as my mages saw, Mother: the soldiers who were with Sabia are dead and there are enough orc corpses to make the battle clear."
    show expression "database/actors/tyra/tyra2.jpg" as tyra behind lynn
    ty "..."
    l "I made sure the scouts were unaffiliated with us, and they'll return with the bodies soon. No one will suspect we had anything to do with Sabia's death."
    show expression "database/actors/tyra/tyra1.jpg" as tyra behind lynn
    ty "Was her body found?"
    l "No, but it's not as if she could have escaped. I was monitoring her life force and I saw it overwhelmed as the orcs attacked."
    show expression "database/actors/lynn/lynn2.png" as lynn at right
    l "Maybe she's an orc whore now, but most likely those savages killed her after they had their fun."
    ty "...let's disavow her mission. Claim that she was disobeying orders by going off on her own."
    show expression "database/actors/lynn/lynn3.png" as lynn at right
    l "Mother? You must know that will make the soldiers with her traitors as well, that will upset their families... and some of them have a little influence in court."
    l "You really think there's any chance Sabia could be a problem? I told you, she's almost certainly dead or broken."
    show expression "database/actors/tyra/tyra3.jpg" as tyra behind lynn
    show expression "database/actors/lynn/lynn1.png" as lynn at right
    ty "She may have become an obstacle, but she is still my daughter. We should take every precaution in removing her."
    l "...as you command, Mother. We'll lose a little support, but I suppose that's a good way to keep anyone from analyzing her false mission."
    show expression "database/actors/tyra/tyra2.jpg" as tyra behind lynn
    ty "..."
    l "That is done, then, we can begin consolidating our control of the army. What next?"
    show expression "database/actors/tyra/tyra1.jpg" as tyra behind lynn
    ty "I am more concerned about the Order of Relona. I believe they... no longer have the best interest of the Kingdom of Lundar in mind."
    show expression "database/actors/lynn/lynn3.png" as lynn at right
    l "Why would they move now? They have as much to gain from stability as the rest of us!"
    ty "Their base of support is larger than I'd like. Human settlements beyond the borders Lundar can currently control may resent the army, but they still embrace religion."
    show expression "database/actors/lynn/lynn2.png" as lynn at right
    l "This is absurd. Why does everyone heap so much praise on the army and the Order when it was mages who won the war?"
    show expression "database/actors/tyra/tyra2.jpg" as tyra behind lynn
    ty "Vulgar as commoners may be, they should not be underestimated. No, now that Sabia is removed, I believe it is time to move to the next phase of the plan..."
    scene bg black with dissolve
    play music orccamp fadeout 2.0 fadein 2.0
    "Sabia awoke slowly from a deep, dreamless slumber. The events of the trial seemed like memories of another life, but slowly she came back to herself."
    scene bg sabiatent
    $ Sabia.face = "normal"
    show Sabia at left
    s "(Alright. I'm not going to starve or get killed by bandits anymore. Orcs aren't the allies I'd have wanted, but they're better than nothing.)"
    $ Sabia.face = "closed2"
    s "(The question now is how I go from here to getting revenge. I need better equipment, subordinates, political leverage against Lynn...)"
    s "(Those things aren't going to be just handed to me. I need to look for opportunities and exploit them for all they're worth.)"
    scene bg centralcamp with dissolve
    "Resolved, Sabia left her tent and headed out into the orc camp. Though most of it was peaceful and little-changed after the trial, she noticed a group of orcs arguing in the central area."
    "Drawing closer, she managed to hear the basic details. Apparently a shipment of steel the orcs needed for their weapons had been stolen by a local caravan of catgirls. Everyone seemed to be taking the theft very seriously."
    $ Sabia.face = "closed2"
    show Sabia at left
    s "(The way they're bickering about this, they won't get anything accomplished. Why can't these savages live up to what potential they have?)"
    $ Sabia.face = "closed1"
    s "(Well, catgirls are nothing serious. I should be able to catch them easily and get some resources...)"
    $ orccampphase = 2
    $ catgirlraidperformance = 0
    $ catgirlraidquest = True
    $ shamanmiracles1prime = True
    play music orccamp fadeout 2.0 fadein 2.0
    $ Sabia.face = "normal"
    jump sabiahq2
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
