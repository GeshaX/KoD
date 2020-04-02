



image bg hcmbrothel = "bg/human city mid/brothel inside.jpg"
image bg hcmcastle = "bg/human city mid/castle inside.jpg"
image bg hcmhouses = "bg/human city mid/houses inside.jpg"
image bg hcmmarket = "bg/human city mid/market inside.jpg"
image bg hcmslums = "bg/human city mid/slums inside.jpg"
image bg hcmstables = "bg/human city mid/stable inside.jpg"
image bg hcmtavern = "bg/human city mid/tavern inside.jpg"
image bg hcmtemple = "bg/human city mid/temple inside.jpg"
image bg hcmtsquare = "bg/human city mid/town square inside.jpg"





init -1:

    transform human_castle_hover:
        "imagebuttons/human/mid/castle 2.png"
        pause 0.25
        "imagebuttons/human/mid/castle 3.png"
        pause 0.25
        "imagebuttons/human/mid/castle 4.png"
        pause 0.25
        "imagebuttons/human/mid/castle 3.png"
        pause 0.25
        repeat
    image animated_human_castle_hover:
        contains human_castle_hover

    transform human_brothel_hover:
        "imagebuttons/human/mid/brothel 2.png"
        pause 0.25
        "imagebuttons/human/mid/brothel 3.png"
        pause 0.25
        "imagebuttons/human/mid/brothel 4.png"
        pause 0.25
        "imagebuttons/human/mid/brothel 3.png"
        pause 0.25
        repeat
    image animated_human_brothel_hover:
        contains human_brothel_hover

    transform human_temple_hover:
        "imagebuttons/human/mid/temple 2.png"
        pause 0.25
        "imagebuttons/human/mid/temple 3.png"
        pause 0.25
        "imagebuttons/human/mid/temple 4.png"
        pause 0.25
        "imagebuttons/human/mid/temple 3.png"
        pause 0.25
        repeat
    image animated_human_temple_hover:
        contains human_temple_hover

    transform human_stable_hover:
        "imagebuttons/human/mid/stable 2.png"
        pause 0.25
        "imagebuttons/human/mid/stable 3.png"
        pause 0.25
        "imagebuttons/human/mid/stable 4.png"
        pause 0.25
        "imagebuttons/human/mid/stable 3.png"
        pause 0.25
        repeat
    image animated_human_stable_hover:
        contains human_stable_hover

    transform human_market_hover:
        "imagebuttons/human/mid/market 2.png"
        pause 0.25
        "imagebuttons/human/mid/market 3.png"
        pause 0.25
        "imagebuttons/human/mid/market 4.png"
        pause 0.25
        "imagebuttons/human/mid/market 3.png"
        pause 0.25
        repeat
    image animated_human_market_hover:
        contains human_market_hover

    transform human_square_hover:
        "imagebuttons/human/mid/town square 2.png"
        pause 0.25
        "imagebuttons/human/mid/town square 3.png"
        pause 0.25
        "imagebuttons/human/mid/town square 4.png"
        pause 0.25
        "imagebuttons/human/mid/town square 3.png"
        pause 0.25
        repeat
    image animated_human_square_hover:
        contains human_square_hover

    transform human_tavern_hover:
        "imagebuttons/human/mid/tavern 2.png"
        pause 0.25
        "imagebuttons/human/mid/tavern 3.png"
        pause 0.25
        "imagebuttons/human/mid/tavern 4.png"
        pause 0.25
        "imagebuttons/human/mid/tavern 3.png"
        pause 0.25
        repeat
    image animated_human_tavern_hover:
        contains human_tavern_hover

    transform human_houses_hover:
        "imagebuttons/human/mid/houses 2.png"
        pause 0.25
        "imagebuttons/human/mid/houses 3.png"
        pause 0.25
        "imagebuttons/human/mid/houses 4.png"
        pause 0.25
        "imagebuttons/human/mid/houses 3.png"
        pause 0.25
        repeat
    image animated_human_houses_hover:
        contains human_houses_hover

    transform human_slums_hover:
        "imagebuttons/human/mid/slums 2.png"
        pause 0.25
        "imagebuttons/human/mid/slums 3.png"
        pause 0.25
        "imagebuttons/human/mid/slums 4.png"
        pause 0.25
        "imagebuttons/human/mid/slums 3.png"
        pause 0.25
        repeat
    image animated_human_slums_hover:
        contains human_slums_hover

screen avartonscreen:
    $ renpy.block_rollback()
    default mouse_clicked = False
    add "imagebuttons/human/mid/base.jpg" xalign 0.0 yalign 0.0
    imagebutton focus_mask True idle "imagebuttons/human/mid/castle 1.png" hover "animated_human_castle_hover" action [Hide("avartonscreen"), Jump("avarton_castle")] pos 265,295 anchor (0.5,0.5)
    imagebutton focus_mask True idle "imagebuttons/human/mid/brothel 1.png" hover "animated_human_brothel_hover" action [Hide("avartonscreen"), Jump("avarton_brothel")] pos 150,420 anchor (0.5,0.5)
    imagebutton focus_mask True idle "imagebuttons/human/mid/temple 1.png" hover "animated_human_temple_hover" action [Hide("avartonscreen"), Jump("avarton_temple")] pos 661,270 anchor (0.5,0.5)
    imagebutton focus_mask True idle "imagebuttons/human/mid/stable 1.png" hover "animated_human_stable_hover" action [Hide("avartonscreen"), Jump("avarton_stables")] pos 977,360 anchor (0.5,0.5)
    imagebutton focus_mask True idle "imagebuttons/human/mid/market 1.png" hover "animated_human_market_hover" action [Hide("avartonscreen"), Jump("avarton_market")] pos 815,490 anchor (0.5,0.5)
    imagebutton focus_mask True idle "imagebuttons/human/mid/town square 1.png" hover "animated_human_square_hover" action [Hide("avartonscreen"), Jump("avarton_tsquare")] pos 428,488 anchor (0.5,0.5)
    imagebutton focus_mask True idle "imagebuttons/human/mid/tavern 1.png" hover "animated_human_tavern_hover" action [Hide("avartonscreen"), Jump("avarton_tavern")] pos 937,690 anchor (0.5,0.5)
    imagebutton focus_mask True idle "imagebuttons/human/mid/houses 1.png" hover "animated_human_houses_hover" action [Hide("avartonscreen"), Jump("avarton_houses")] pos 185,675 anchor (0.5,0.5)
    imagebutton focus_mask True idle "imagebuttons/human/mid/slums 1.png" hover "animated_human_slums_hover" action [Hide("avartonscreen"), Jump("avarton_slums")] pos 575,731 anchor (0.5,0.5)
    fixed at KeymapTransform([('mousedown_1', SetScreenVariable('mouse_clicked', True)), ('mouseup_1', SetScreenVariable('mouse_clicked', False))]):
        imagebutton idle "imagebuttons/leave_idle.png" hover ("imagebuttons/leave_clicked.png" if mouse_clicked else "imagebuttons/leave_hover.png") xpos 50 ypos 0 focus_mask True action [Hide("avartonscreen"), Jump("eastern_frontier_map")]
    use infohud("center")


label avarton_town:
    if avarton_first_visit == False:
        $ avarton_first_visit = True
        scene bg hcsstsquare
        $ Sabia.face = "normal"
        show Sabia at left
        with dissolve
        "Avarton was much larger than the smaller villages on the outskirts."
        "The keep that loomed over the rest of the buildings provided enough soldiers and security to encourage a town to continue growing."
        "Sabia watched a hubbard of people, some going this way and others going that way."
        "Most of them ignored each other. There was a sense of anonymity in a place like this. Not everyone knew each other."
        "Sabia spent a bit walking through the town. It was about the same as any human town she could expect."
        "A tavern, a temple to Relona, a fountain. The brothel seemed busy enough. Soldiers coming in and out, a few of the girls half-dressed hanging from the balcony."
        "A trading hall that seemed more promising to Sabia than some of the smaller villages - as well as stables."
        "The farther Sabia went from the town's fountain center, the more run down the houses were."
        "Cracked windows, chimneys that crumbled as she watched; doors that didn't quite close and piles of roof tiles smashed on the ground."
    scene bg black
    $ renpy.choice_for_skipping()
    while True:
        show screen avartonscreen
        $ renpy.pause(hard=True)


label avarton_castle:
    scene bg hcmcastle
    show screen infohud("left")
    if avarton_first_visit_keep == False:
        $ avarton_first_visit_keep = True
        $ Sabia.face = "normal"
        show Sabia at left
        "The road up to the keep was wide enough for two carriages side-by-side."
        "Small depressions in the path made it an uneven walk, but nothing too bad."
        "The portcullis to the inside of the keep was open, and a few guards flanked the sides."
        "But merchants, citizens and soldiers alike were exiting and entering as needed - it was not blocked off to anyone."
        "Sabia knew there would be rooms and sections of the keep that were truly locked off except for permitted people."
        "But a sizable keep in a larger town like Avarton was more open, and the town and keep sort of mixed together."
        "She spotted a training grounds with some young soldiers participating in drills, and a cart set up next to several boiling pots over fire, serving a thick stew."
        $ Sabia.face = "normalopen"
        s "Hmm. I haven't fought a lot of humans lately. Orcs and catgirls fight differently. It might be worth my time to try and get a bit of practice in later."
    menu:
        "Train.":
            if Sabia.armor == Rags or Sabia.armor == Orcslavearmor:
                $ Sabia.face = "normal"
                $ Humansoldier.face = "normal"
                show Sabia at left
                show Humansoldier at right
                soldier "..."
                soldier "I don't think you're training here, or a soldier. Go back to the brothel - Madame Fennasil will feed you, I'm sure."
                "Sabia frowned. It probably wasn't worth arguing - at least not while she was wearing clothes that did make her look like a whore..."
                jump avarton_castle

            $ Sabia.face = "normalopen"
            show Sabia at left
            s "I really should sharpen up my skills against a human opponent."
            $ Sabia.face = "normal"
            "Sabia went over to the training area. It was large and open, and a multitude of people were either already mid combat, or milling about waiting."
            "There were some soldiers that looked almost as big as an orc, and some that were more lean. A few looked well-scarred and well-trained, and others looked fresh."
            menu avarton_training_menu1:
                "Challenge lean warrior." if avarton_training_lean == False:
                    $ avarton_training_lean = True
                    "Sabia approached one of the leaner looking men, asking to fight."
                    show Humansoldier at right with dissolve
                    "Grinning and making a few jokes about her wanting his sword, he agreed with a cocky smirk."
                    "Sabia expected him to be a bit faster than he was. Some of his strikes were sloppy, and his foot movement was slow."
                    "There was no strength behind a lot of his attacks either. It wasn't long before Sabia had him landing with a thud on the ground."
                    call shake ("h")
                    hide Humansoldier with dissolve
                    "She didn't say anything as she took a few steps back out of the combat area, though the solider was red-faced."
                    jump avarton_training_menu1
                "Challenge large warrior." if avarton_training_large == False:
                    $ avarton_training_large = True
                    show Humansoldier at right with dissolve
                    "Sabia approached one of the larger looking warriors there, and asked to fight. It took a small amount of persuasion before he agreed to fight her."
                    "The fight was over quickly. He fought more like one of the unskilled orcs in Grok og Dar, all brawl and muscle, and little finesse."
                    "It was an easy fight, and he seemed surprised he had lost; several of the nearby warriors laughed uproariously at his loss."
                    hide Humansoldier with dissolve
                    jump avarton_training_menu1
                "Challenge grizzled veteran." if avarton_training == 0:
                    $ avarton_training = 1
                    $ Sabia.face = "normalopen"
                    s "Might as well go with one of them that looks like they might actually test me, I suppose."
                    $ Sabia.face = "normal"
                    show Humansoldier at right with dissolve
                    "She approached one of the grizzled veterans, asking for a practice bout. Surprisingly, he agreed readily."
                    $ Sabia.face = "sad1"
                    "It was quickly made apparent to Sabia that she had lost some of her edge when it came to fighting against humans."
                    "His strikes and movements kept catching her off guard, and she was quickly out of breath and forced to yield."
                    $ Humansoldier.face = "happy"
                    veteran "Hmm. Not bad - better than I expected. It does feel like you're trying to put weight you don't have behind some of your strikes, though."
                    $ Humansoldier.face = "normal"
                    veteran "Come back to fight again, if you want."
                    $ Sabia.face = "normalopen"
                    s "I might take you up on that."
                    $ Sabia.face = "normal"
                    $ Humansoldier.face = "happy"
                    red "Name's Red, if you can't find me."
                    $ Sabia.face = "normalopen"
                    $ Humansoldier.face = "normal"
                    s "Red? How'd you get that name?"
                    $ Sabia.face = "normal"
                    "He shrugged."
                    $ Humansoldier.face = "sad"
                    red "Blood. Used to get a lot of it on me."
                    $ Humansoldier.face = "normal"
                    red "Not so much anymore."
                    $ Sabia.face = "happy3"
                    s "Heh, I can see why. I might take you up on that offer sometime soon."
                    if avarton_training_large == True and avarton_training_lean == True:
                        $ Sabia.face = "normalopen"
                        s "Some of the other soldiers around here don't seem as skilled as you."
                        $ Sabia.face = "normal"
                        red "They're alright. But I'd wager you're better than a lot of them already."
                        red "See you around...?"
                        $ Sabia.face = "happy3"
                        $ Humansoldier.face = "happy"
                        s "Sabia."
                        $ Sabia.face = "normal"
                        red "Sabia."
                    jump avarton_training_menu1
                "Challenge grizzled veteran." if avarton_training == 1:
                    if avarton_training_large == True and avarton_training_lean == True:
                        $ Humansoldier.face = "normal"
                        show Humansoldier at right with dissolve
                        red "You want another round?"
                        $ Sabia.face = "normalopen"
                        s "Yeah. I think I'm up for it."
                        $ Sabia.face = "normal"
                        $ Humansoldier.face = "happy"
                        red "Alright. Maybe we can teach some of those other oafs a thing or two, huh?"
                        $ Humansoldier.face = "normal"
                        "Sabia and Red had a few rounds of combat. At the end, Sabia felt like she was getting a bit more used to fighting a more refined human opponent."
                        jump avarton_training_menu1
                    else:
                        $ Humansoldier.face = "normal"
                        show Humansoldier at right with dissolve
                        red "You want another round?"
                        $ Sabia.face = "normalopen"
                        s "Yeah. I think I'm up for it."
                        $ Sabia.face = "irritated2"
                        red "Hmm. Sure you don't want to try a bout with some of the others around?"
                        $ Sabia.face = "normalopen"
                        $ Humansoldier.face = "happy"
                        s "Maybe another time. I think my time is better spent training with you, though."
                        $ Sabia.face = "normal"
                        $ Humansoldier.face = "normal"
                        "Sabia and Red had a few rounds of combat. At the end, Sabia felt like she was getting a bit more used to fighting a more refined human opponent."
                        jump avarton_training_menu1
                "Leave.":
                    jump avarton_castle
        "Walk around.":

            $ Sabia.face = "normal"
            show Sabia at left
            "Sabia spent some time wandering around Avarton's keep and listening. It was like a town-within-a-town, everyone busy and running errands."
            $ temp = renpy.random.randint(1,4)
            if temp == 1:
                soldier1 "I don't think Andian's gonna hold out much longer. What, with that mage showing up? We'll be part of Lundar any week now."
                soldier2 "Maybe. I ain't got nothing against Lundar. Maybe they'll finally deal with that spoiled brat Barrin."
                soldier1 "One can only hope, eh?"
            elif temp == 2:
                soldier1 "One day I'll knock you on your back, Red."
                red "Hah! One day, when I'm old and sore, and can't swing a sword - maybe you'll have a chance then."
            elif temp == 3:
                soldier1 "I could have taken her."
                soldier2 "No."
                soldier1 "Yeah, could have."
                soldier2 "You taking on a Lustrator? Your head would be caved in with that monstrous hammer before you even saw it swinging toward you."
                soldier2 "Stop talking out of your ass."
            else:
                soldier1 "I'm glad that Lustrator didn't stick around for long..."
                soldier2 "Why? You don't worship Relona?"
                soldier1 "Of course I do!"
                soldier1 "But those Lustrators... they're terrifying. All grim and blank. You just know they're judging you..."
                soldier2 "I don't think they're judging everyone..."
                soldier1 "How would you fucking know? You wouldn't! At least, not until you're on a pyre or your bones have been crushed from their hammer."
            jump avarton_castle
        "Eat something.":


            if Sabia.armor == Rags or Sabia.armor == Orcslavearmor:
                $ Sabia.face = "normal"
                $ Humansoldier.face = "normal"
                show Sabia at left
                show Humansoldier at right
                chef "..."
                $ Humansoldier.face = "sad"
                chef "I don't think you're training here, or a soldier. Go back to the brothel - Madame Fennasil will feed you, I'm sure."
                "Sabia frowned. It probably wasn't worth arguing - at least not while she was wearing clothes that did make her look like a whore..."
                jump avarton_castle
            else:
                $ Sabia.face = "normal"
                show Sabia at left
                "Sabia grabbed a bowl and some stew from the open kitchen near the courtyard."
                "She took a seat and decided to see if she could overhear anything."
                $ temp = renpy.random.randint(1,3)
                if temp == 1:
                    soldier1 "Fuck me, it's fucking vegetable stew again?"
                    soldier2 "Well, it's what happens when you're not in the capital."
                    soldier1 "I tell you, I'm getting fucking tired of this. I bet those bandits don't fucking have to eat stew every day."
                    soldier2 "Yeah, but they get executed if caught..."
                elif temp == 2:
                    soldier1 "I tell you, I'm getting sick of seeing the filth from the slums sneaking in here for free meals."
                    soldier2 "They're just hungry."
                    soldier1 "They ain't fucking fighting for it, putting their life on the line. If they want food, they should enlist."
                else:
                    soldier1 "Do you think trade's going to open up properly again with Lundar?"
                    soldier2 "Maybe after Andian annexes with Lundar."
                    soldier1 "Eh, I'm not sold on that. If I wanted to live in Lundar, I would have moved there already."
                    soldier1 "I'm not a fan of their mages..."
                    soldier2 "Yeah? I'd keep that to yourself. I heard one of them was in Whitecrest... she probably has eyes and ears everywhere."
                    s "(He's not wrong... Lynn probably does have agents around.)"
                jump avarton_castle

        "Talk to the Cook." if v10lynn_quest_done == False and v10lynn_quest_amelia == True:
            $ Sabia.face = "normal"
            $ Dirtycook.face = "normal"
            show Sabia at left
            show Dirtycook at right
            with dissolve
            menu:
                "Ask about Hal." if v10lynn_quest_cook_hal == False:
                    $ v10lynn_quest_cook_hal = True
                    $ v10lynn_quest_hal_quarters = True
                    $ Dirtycook.face = "normalopen"
                    cook "Hal, eh?"
                    $ Dirtycook.face = "normal"
                    "The cook frowned, leaning on the edge of her pot, one hand stirring the perpetual stew."
                    $ Dirtycook.face = "normalopen"
                    cook "Why's a nice girl like you looking for a soldier like that?"
                    $ Sabia.face = "normalopen"
                    $ Dirtycook.face = "normal"
                    s "Reasons are my own. Can you point me in his direction, or not?"
                    $ Sabia.face = "normal"
                    $ Dirtycook.face = "normalopen"
                    cook "Well, he's only been here for little bit. Can't say I'm a fan of him. Doesn't seem that pleasant to talk to, y'know?"
                    cook "But his quarters are in the east wing."
                    $ Dirtycook.face = "normal"
                    "The cook gave Sabia directions to the quarters. She was sure she could find it herself now."
                    $ Sabia.face = "normalopen"
                    s "Thanks."
                    $ Sabia.face = "normal"
                    $ Dirtycook.face = "normalopen"
                    cook "No worries. You might not be able to find him if he's on duty that day, though."
                    scene bg black with dissolve
                    jump avarton_castle
                "Ask about Hal." if v10lynn_quest_cook_hal == True:
                    $ Dirtycook.face = "normalopen"
                    cook "Look, as pleasant as it is to be talking to a nice for once instead of an arrogant, rude soldier - I've got work to do."
                    $ Sabia.face = "sad2"
                    cook "And you're holding up the line too much."
                    $ Dirtycook.face = "normal"
                    "Those behind her growled their frustrations, and Sabia nodded, moving on."
                    scene bg black with dissolve
                    jump avarton_castle
                "Ask where Hal is now." if v10lynn_quest_cook_hal == True:
                    "The cook grimaced, brandishing a half full ladle of soup in Sabia's direction."
                    $ Sabia.face = "sad2"
                    $ Dirtycook.face = "angry"
                    cook "Do I look like the fucking commander to you?"
                    cook "I'm ladling soup. I don't know where the fucking soldiers are every day of the week. You want him? Go find him y'self."
                    $ Dirtycook.face = "normal"
                    scene bg black with dissolve
                    jump avarton_castle
                "Ask about William." if v10lynn_quest_cook_william == False:
                    $ v10lynn_quest_cook_william = True
                    $ Dirtycook.face = "normalopen"
                    cook "Huh? William? I dunno much about him. He's barely around."
                    $ Sabia.face = "irritated2"
                    cook "Feels like I only really see him every few days, and the rest..."
                    $ Dirtycook.face = "normal"
                    "The cook shrugged."
                    $ Dirtycook.face = "normalopen"
                    cook "The rest I don't see him much."
                    $ Sabia.face = "irritated1"
                    cook "Ask someone else. But for now you're holding up the line."
                    scene bg black with dissolve
                    jump avarton_castle
                "Ask about William." if v10lynn_quest_cook_william == True:
                    $ v10lynn_quest_william_quarters = True
                    $ Dirtycook.face = "normalopen"
                    cook "Look, as pleasant as it is to be talking to a nice girl for once instead of an arrogant, rude soldier - I've got work to do."
                    $ Dirtycook.face = "angry"
                    $ Sabia.face = "irritated2"
                    cook "If you want to try and talk to William, go find his quarters in the north wing. Third door on the left. Now get out of the way."
                    "Those behind her growled their frustrations, and Sabia nodded, moving on."
                    scene bg black with dissolve
                    jump avarton_castle
                "Ask about Robert." if v10lynn_quest_cook_robert == False:
                    $ v10lynn_quest_cook_robert = True
                    $ Dirtycook.face = "normalopen"
                    cook "Hah! You're trying to find him here? Good luck."
                    $ Dirtycook.face = "normal"
                    $ Sabia.face = "normalopen"
                    s "What do you mean?"
                    $ Sabia.face = "irritated2"
                    $ Dirtycook.face = "normalopen"
                    cook "Ain't no whores around here."
                    $ Sabia.face = "angry2"
                    cook "...unless?"
                    $ Dirtycook.face = "normal"
                    "She raised his eyebrows inquisitively."
                    $ Sabia.face = "angry1"
                    s "Not me."
                    "The cook shrugged."
                    $ Sabia.face = "irritated1"
                    $ Dirtycook.face = "normalopen"
                    cook "Then I'm not sure if I can help you if you're looking for him."
                    scene bg black with dissolve
                    jump avarton_castle
                "Ask about Robert." if v10lynn_quest_cook_robert == True:
                    $ v10lynn_quest_robert_quarters = True
                    $ Dirtycook.face = "normalopen"
                    cook "Look, as pleasant as is to be talking to a nice girl for once instead of an arrogant, rude soldier - I've got work to do."
                    $ Dirtycook.face = "angry"
                    cook "If you really want to talk to him that bad, his quarters are in the west wing. Now shove off, you're holding up the line too much."
                    $ Dirtycook.face = "normal"
                    "Those behind her growled their frustrations, and Sabia nodded, moving on."
                    scene bg black with dissolve
                    jump avarton_castle

        "Talk to Red." if v10lynn_quest_done == False and v10lynn_quest_amelia == True and avarton_training > 0:
            $ Sabia.face = "normal"
            $ Humansoldier.face = "normal"
            show Sabia at left
            show Humansoldier at right
            with dissolve
            menu v10lynn_red_menu:
                "Ask about Hal." if v10lynn_quest_red_hal == False:
                    $ v10lynn_quest_red_hal = True
                    $ Humansoldier.face = "sad"
                    red "Can't say I know too much about him."
                    red "Keeps to himself mostly."
                    if v10lynn_quest_cook_hal == True:
                        $ Sabia.face = "normalopen"
                        $ Humansoldier.face = "normal"
                        s "I heard that he's only been here for a little bit?"
                        $ Sabia.face = "normal"
                        "Red nodded."
                        red "That's right, he was stationed here a little while ago. I don't really keep track of the time for those things though, Sabia."
                    $ Sabia.face = "normalopen"
                    s "I see."
                    $ Humansoldier.face = "sad"
                    s "Do you have anything else about him you could let me know?"
                    $ Sabia.face = "normal"
                    $ Humansoldier.face = "normal"
                    red "Well, not sure. Like I said, he mostly keeps to himself. Doesn't really come to practice much. Not something you want in a fellow soldier, you know?"
                    red "Preferable that you are familiar with your fellow men."
                    $ Sabia.face = "normalopen"
                    s "Agreed. You want to be comfortable with them and be able to trust them."
                    $ Sabia.face = "normal"
                    "Red inclined his head."
                    $ Humansoldier.face = "sad"
                    red "Not sure how much more help I can be about him, sorry."
                    $ Sabia.face = "happy3"
                    $ Humansoldier.face = "normal"
                    s "That's fine, thanks Red."
                    jump v10lynn_red_menu
                "Ask where Hal is now." if v10lynn_quest_red_hal == True:
                    $ Sabia.face = "sad1"
                    $ Humansoldier.face = "sad"
                    red "Couldn't help you sorry, Sabia."
                    red "Could be training somewhere around the keep, or in his quarters. Keeps to himself, as I said."
                    jump v10lynn_red_menu
                "Ask about William." if v10lynn_quest_red_william == False:
                    $ v10lynn_quest_red_william = True
                    $ Humansoldier.face = "sad"
                    red "William?"
                    $ Sabia.face = "irritated2"
                    red "What about him? He's barely a soldier right now. Too mopey, in my opinion."
                    $ Humansoldier.face = "happy"
                    red "But, ah. I suppose he's young."
                    $ Sabia.face = "normalopen"
                    $ Humansoldier.face = "normal"
                    s "Why do you say that about him?"
                    $ Sabia.face = "normal"
                    red "Always complaining about not being stationed closer to Whitecrest."
                    $ Sabia.face = "normalopen"
                    s "Oh?"
                    $ Sabia.face = "normal"
                    $ Humansoldier.face = "sad"
                    "Red shrugged."
                    red "Whitecrest is a popular place for sodiers. It's easy, lax, the pay is good and there's not much fighting."
                    $ Sabia.face = "irritated2"
                    red "Getting stationed there is difficult. William has a wife in Whitecrest, but has employment that stops her from moving."
                    $ Humansoldier.face = "normal"
                    "He shrugged again."
                    red "Or something to that effect."
                    $ Sabia.face = "normalopen"
                    s "I see. So he mostly just... travels back to Whitecrest to see his wife?"
                    $ Sabia.face = "normal"
                    $ Humansoldier.face = "happy"
                    red "So he says. I never had cause to doubt him. He seems like a good kid."
                    $ Humansoldier.face = "normal"
                    "Sabia nodded."
                    $ Sabia.face = "normalopen"
                    s "Thanks, Red."
                    jump v10lynn_red_menu




                "Ask where William is now." if v10lynn_quest_red_william == True:
                    if v10lynn_william_location == "quarters":
                        $ Humansoldier.face = "normal"
                        red "Think he's staying at his quarters today."
                    else:
                        $ Humansoldier.face = "normal"
                        red "Think he left for Whitecrest this morning. Should be gone for the rest of the day."
                    jump v10lynn_red_menu
                "Ask about Robert." if v10lynn_quest_red_robert == False:
                    $ v10lynn_quest_red_robert = True
                    $ Humansoldier.face = "angry"
                    "Red wrinkled his nose, and spat on the ground in disgust."
                    red "Ah, that one."
                    $ Sabia.face = "normalopen"
                    s "It doesn't seem like you like him all that much...?"
                    $ Sabia.face = "normal"
                    red "He spends more time in the whorehouse than he does with a sword in his hand."
                    $ Humansoldier.face = "sad"
                    red "Truth be told, not sure why he hasn't been stripped of his rank and discharged."
                    $ Sabia.face = "normalopen"
                    s "Is visting the brothel that big of an issue?"
                    $ Sabia.face = "normal"
                    "Red frowned."
                    $ Humansoldier.face = "normal"
                    red "Well, no. And I've spent a few nights there meself, you know? An old man gets lonely."
                    $ Humansoldier.face = "angry"
                    red "But when he's gone more than he's present. That rankles me."
                    $ Sabia.face = "normalopen"
                    s "I can understand that."
                    $ Sabia.face = "normal"
                    red "And from what I've heard, he's been using some of the girls at Fennasil's to gather information and use it as blackmail."
                    "Red spat on the ground again."
                    $ Sabia.face = "irritated2"
                    $ Humansoldier.face = "sad"
                    red "If I were a younger, more eager man... I might try to do something about it."
                    red "But I think I have done my part for Whitecrest in my years."
                    $ Sabia.face = "normalopen"
                    $ Humansoldier.face = "normal"
                    s "You can't do everything yourself, Red. It doesn't sound like it is your responsibility at all, anyway."
                    $ Sabia.face = "normal"
                    red "Very true. It is what it is. I hope I was able to help you learn what you needed, Sabia."
                    $ Sabia.face = "normalopen"
                    s "Maybe, Red. Maybe."
                    jump v10lynn_red_menu
                "Go back.":
                    jump avarton_castle

        "Consider gathered information." if v10lynn_quest_done == False and v10lynn_quest_amelia == True:
            $ Sabia.face = "normal"
            show Sabia at left with dissolve
            $ temp1 = 0
            if v10lynn_quest_hal_quarters == True:
                $ temp1 += 1
            if v10lynn_quest_william_quarters == True:
                $ temp1 += 1
            if v10lynn_quest_robert_quarters == True:
                $ temp1 += 1
            $ temp2 = 0
            if v10lynn_quest_cook_hal:
                $ temp2 += 1
            if v10lynn_quest_cook_william:
                $ temp2 += 1
            if v10lynn_quest_cook_robert:
                $ temp2 += 1
            if v10lynn_quest_madame_hal:
                $ temp2 += 1
            if v10lynn_quest_madame_william:
                $ temp2 += 1
            if v10lynn_quest_madame_robert:
                $ temp2 += 1
            if v10lynn_quest_red_hal:
                $ temp2 += 1
            if v10lynn_quest_red_william:
                $ temp2 += 1
            if v10lynn_quest_red_robert:
                $ temp2 += 1

            if temp1 == 0:
                $ Sabia.face = "normalopen"
                s "It would be best if I try and find out where each of the potential targets live."
                s "Being able to investigate their quarters if possible would be good. It might let me know who exactly I should be after."
                s "I should ask around and see if I can find out where their quarters are."
            elif temp1 > 0 and temp1 < 3:
                $ Sabia.face = "normalopen"
                s "I at least have a location of quarters, if not for all of the potential targets."
                s "I could try breaking in and seeing what information I can get from their quarters, but it might be beneficial to keep asking around and seeing what else I can find out first."
            elif temp1 == 3 and temp2 < 9:
                $ v10lynn_quest_unlocked_quarters = True
                $ Sabia.face = "normalopen"
                s "I at least know where each of my... targets lives. I could check their quarters out and scope around. I might be able to glean some information that can help me decide."
                s "I would need to be careful though. I could ask around a bit more and see if I can get any additional information."
            else:
                $ v10lynn_quest_unlocked_quarters = True
                $ Sabia.face = "normalopen"
                s "I don't think asking around any more is going to turn up any additional information."
                s "I think the only thing that will do so is actually interrogating the correct person, or seeing what I can find in their quarters when they are gone."
                $ Sabia.face = "closed4"
                s "Robert seems to match what Dajrab said most... but Hal is behaving as if he is scared. I can imagine anyone having dealt with Lynn being... very scared."
                $ Sabia.face = "closed2"
                s "William looks as if he is a husband that misses his wife... but it's a good cover to be traveling back and forth."
                $ Sabia.face = "normalopen"
                s "I'll have to pick carefully. I've been asking around a bit, and snooping around in the actual wings of the keep might spook the other two before I get a chance to confront them if I pick incorrectly."
            jump avarton_castle

        "Check quarters." if v10lynn_quest_unlocked_quarters == True and v10lynn_quest_done == False:
            $ Sabia.face = "normal"
            show Sabia at left with dissolve
            if v10lynn_quest_quarters_first_visit == False:
                $ v10lynn_quest_quarters_first_visit = True
                $ Sabia.face = "normalopen"
                s "Hmm. It might not be safe. I don't know if he is there or not. I might want to ask around to ensure that their quarters will be empty."
                $ Sabia.face = "normal"
            menu:
                "Visit Hal's quarters." if v10lynn_hal_cleared == False and v10lynn_robert_cleared == False:
                    $ v10lynn_hal_cleared = True
                    if v10lynn_william_cleared == False and v10lynn_robert_cleared == False:
                        "Sabia followed the directions towards Hal's quarters, and stood at the door for a brief second with a raised hand."
                        $ Sabia.face = "closed2"
                        s "(Knocking seems pointless...)"
                        $ Sabia.face = "normal"
                        "Shaking her head to herself, she opened the door."
                        scene bg black with dissolve
                        pause (0.1)
                        scene bg hcmcastle
                        $ Humansoldier.face = "surprised"
                        show Humansoldier at right
                        with dissolve
                        pause (0.1)
                        $ Sabia.face = "irritated2"
                        show Sabia at left with moveinleft
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
                        "Sabia passed him back his sword."
                        $ Sabia.face = "normalopen"
                        s "Look, I'm going to need that information."
                        menu v10lynn_hal_menu:
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
                            "Offer 150 lundils.":
                                if money < 150:
                                    s "(Unfortunately I don't have enough money to bribe him. I need to think of something else.)"
                                    jump v10lynn_hal_menu
                                $ v10lynn_hal_deal = "bribe"
                                $ money -= 150
                                $ Sabia.face = "angry1"
                                $ Humansoldier.face = "sad"
                                s "And I don't have time to argue this and that and try to convince you. I'll pay you. Enough that you'll be able to get out of Whitecrest and Lundar's borders."
                                s "Head south to Carchedone if you want. Or north to Erxia - though I wouldn't recommend going through Whitecrest or Lundar to do so."
                                $ Sabia.face = "normalopen"
                                $ Humansoldier.face = "surprised"
                                s "One hundred and fifty lundils, along with what you have here. That should get you out. You're not going to get a better offer."
                                $ Sabia.face = "irritated2"
                                $ Humansoldier.face = "sad"
                                "Sabia watched him considering. She was sure he was trying to decide whether the risk of revealing anything was worth the potential of escaping with enough coin to make for another region."
                                "She also suspected he was wondering if he were going to be betrayed after."
                                "Sabia was not sure what he was going to decide, before he finally nodded reluctantly."
                                $ Sabia.face = "normal"
                                $ Humansoldier.face = "normal"
                                hal "Fine... if you have the coin. Deal."
                                jump v10lynn_information
                    else:
                        "Sabia followed the directions towards Hal's quarters, and stood at the door for a brief second with a raised hand."
                        $ Sabia.face = "closed2"
                        s "(Knocking seems pointless...)"
                        $ Sabia.face = "normal"
                        "Shaking her head to herself, she opened the door."
                        scene bg black with dissolve
                        pause (0.1)
                        scene bg hcmcastle
                        with dissolve
                        pause (0.1)
                        show Sabia at left with moveinleft
                        "The room was empty. Mostly stripped bare, draws open and empty."
                        "Cabinet door swinging open on its hinges."
                        $ Sabia.face = "normalopen"
                        s "This must have been who I was after... it looks like he must have bailed when he saw me looking into the other quarters."
                        s "Fuck."
                        $ Sabia.face = "closed2"
                        s "..."
                        $ Sabia.face = "normalopen"
                        s "...maybe I could ask Amelia if she's happened to see anything?"
                        s "She does seem to be quite... knowledgeable of the goings on in Avarton. Guess it comes with being the barkeep in that sort of establishment."
                        s "Hopefully she has heard something."
                        $ Sabia.face = "irritated2"
                        "Frustrated, Sabia closed the door behind her harsh enough for it to slam loudly."
                        jump v10lynn_rogue_fight

                "Visit William's quarters." if v10lynn_william_cleared == False:
                    $ v10lynn_william_cleared = True
                    if v10lynn_william_location == "quarters":
                        "Sabia followed the directions towards William's quarters, and stood at the door for a brief second with a raised hand."
                        $ Sabia.face = "closed2"
                        s "(Knocking seems pointless...)"
                        $ Sabia.face = "normal"
                        "Shaking her head to herself, she opened the door."
                        scene bg black with dissolve
                        pause (0.1)
                        scene bg hcmcastle
                        $ Humansoldier.face = "angry"
                        show Humansoldier at right
                        with dissolve
                        pause (0.1)
                        show Sabia at left with moveinleft
                        william "Uh... excuse me?"
                        $ Sabia.face = "sad3"
                        "Sabia whirled about and saw a confused look on William's face, a hand gripping the hilt of his sword hesitantly."
                        $ Sabia.face = "happy3"
                        $ Humansoldier.face = "normal"
                        s "Oh, I was uh, sent here by Red."
                        $ Sabia.face = "normal"
                        "He noticeably relaxed, letting his hand full from the weapon."
                        william "Oh. What does Red want? Drills? Little else with him, eh?"
                        $ Sabia.face = "happy2"
                        s "Uh, I think so."
                        s "He didn't really say. Just said I might have trouble getting you to go down..."
                        $ Sabia.face = "normal"
                        $ Humansoldier.face = "sad"
                        william "Well, he's not wrong."
                        william "I haven't seen Violet for a week."
                        $ Sabia.face = "normalopen"
                        s "Violet?"
                        $ Sabia.face = "normal"
                        $ Humansoldier.face = "happy"
                        william "My Wife. She lives in Whitecrest."
                        $ Sabia.face = "irritated2"
                        william "Tell Red I'll be damned if I'm putting that off for more of his drills."
                        $ Sabia.face = "normalopen"
                        $ Humansoldier.face = "sad"
                        s "Won't that incur some sort of... penalty? Like more drills?"
                        $ Sabia.face = "irritated2"
                        $ Humansoldier.face = "happy"
                        william "Probably. But it's worth it to see the smile on Violet's face, and to hear her laugh."
                        william "You understand, don't you?"
                        $ Humansoldier.face = "sad"
                        "William sighed."
                        william "Tell Red I'll make it up to him. He's not going to make me wait to see Violet."
                        $ Sabia.face = "closed2"
                        $ Humansoldier.face = "normal"
                        s "(...he's nothing more than a lovesick soldier. I've seen a hundred of them in my time.)"
                        s "(I doubt he knows anything relevant. This isn't the man I am looking for.)"
                        $ Sabia.face = "normalopen"
                        s "Well, I'll let Red know that but I'm sure he won't be pleased."
                        $ Sabia.face = "normal"
                        $ Humansoldier.face = "happy"
                        william "He'll have to live with it."
                        scene bg black with dissolve
                        jump avarton_castle
                    else:
                        "Sabia followed the directions towards William's quarters, and stood at the door for a brief second with a raised hand."
                        $ Sabia.face = "closed2"
                        s "(Knocking seems pointless...)"
                        $ Sabia.face = "normal"
                        "Shaking her head to herself, she opened the door."
                        "The room was mostly bare. Across from the entrance was a large set of drawers."
                        $ Sabia.face = "irritated2"
                        "Several painted portraits of who Sabia assumed must be the man's wife decorated the top of it."
                        "She spent a few minutes rifling through the drawers themselves and looking around."
                        $ Sabia.face = "normal"
                        "There was nothing here to indicate that the man was anything other than a very homesick husband."
                        $ Sabia.face = "normalopen"
                        s "I guess William probably has little information to give after all."
                        $ Sabia.face = "normal"
                        "Placing everything back as best as she could, she quietly left the room."
                        scene bg black with dissolve
                        jump avarton_castle

                "Visit Robert's quarters." if v10lynn_robert_cleared == False:
                    $ v10lynn_robert_cleared = True
                    if v10lynn_robert_location == "quarters":
                        "Sabia followed the directions towards Robert's quarters, and stood at the door for a brief second with a raised hand."
                        $ Sabia.face = "closed2"
                        s "(Knocking seems pointless...)"
                        $ Sabia.face = "normal"
                        "Shaking her head to herself, she opened the door."
                        scene bg black with dissolve
                        pause (0.1)
                        scene bg hcmcastle
                        $ Humansoldier.face = "happy"
                        show Humansoldier at right
                        with dissolve
                        pause (0.1)
                        show Sabia at left with moveinleft
                        robert "Ah, good."
                        $ Sabia.face = "sad3"
                        "Sabia jumped in surprise, the words coming from the darkness of the room."
                        $ Sabia.face = "normalopen"
                        $ Humansoldier.face = "angry"
                        s "Sorry, I must have-"
                        $ Sabia.face = "normal"
                        robert "No. You're in the right room."
                        robert "About time, as well."
                        $ Sabia.face = "irritated1"
                        $ Humansoldier.face = "happy"
                        robert "Saves me the time of having to track you down. Meddling whore."
                        $ Sabia.face = "happy3"
                        s "I think you might have me confused with someone else - I, well, I think I came into the wrong room by accident!"
                        $ Sabia.face = "angry2"
                        $ Humansoldier.face = "angry"
                        "He clicked his tongue, leaping to his feet."
                        jump v10lynn_rogue_fight
                    else:
                        "Sabia followed the directions towards Robert's quarters, and stood at the door for a brief second with a raised hand."
                        $ Sabia.face = "closed2"
                        s "(Knocking seems pointless...)"
                        $ Sabia.face = "normal"
                        "Shaking her head to herself, she opened the door."
                        scene bg black with dissolve
                        pause (0.1)
                        scene bg hcmcastle
                        show backdrop
                        with dissolve
                        pause (0.1)
                        show Sabia at left with moveinleft
                        "Looking in, it was difficult to see. The room was dark, the blinds pulled closed and were tight against the frame of the windows."
                        hide backdrop with dissolve
                        "Sabia moved across the room, and pulled the blinds up just enough to let a few streaks of light spill in."
                        "The room seemed clean, but something about it irked her."
                        "She rifled through the cabinet in the corner and quickly found multiple notes and pieces of blackmail material of people in Avarton."
                        $ Sabia.face = "irritated2"
                        "Signed contracts, some jewels, more lundils than a soldier in his station should have."
                        "She continued looking through the documents. There was information on a lot of people, but nothing about Lynn. Nothing on anyone that might even deal with Lynn."
                        $ Sabia.face = "normalopen"
                        s "I thought for sure... but I suppose this isn't the man I am after."
                        $ Sabia.face = "angry1"
                        s "He's up to nothing good... but not the particular kind of nothing good I was looking for."
                        $ Sabia.face = "irritated2"
                        "Putting back the items as best she could, Sabia left the room and closed the door behind her."
                        jump v10lynn_rogue_fight
                "Leave.":

                    scene bg black with dissolve
                    jump avarton_castle
        "Go back":

            scene bg black with dissolve
            jump avarton_town


label v10lynn_rogue_fight:
    $ Humansoldier.face = "angry"
    show Humansoldier at center with moveinright
    call shake ("h")
    "Sabia hissed, drawing her sword quickly and parrying the strike."
    "She had barely caught the glimpse of glinting steel in time."
    robert "You ask too many questions!"
    if v10lynn_hal_deal != "":
        $ Sabia.face = "angry1"
        s "I've found what I need, it has nothing to do with you-"
    else:
        robert "I have spent months building myself here, only for you to come snooping and trying to barge in on my territory!"
        $ Sabia.face = "angry1"
        s "I'm not after your territory or anything, I'm just trying to find some information about a mage that-"
        $ Sabia.face = "angry2"
        robert "Do you think I'm an idiot?"
        robert "I steer clear of mages. And you should have steered clear of me."
    $ enemy_level = 8
    $ enemy_maxhp = 450
    $ enemy_hp = enemy_maxhp
    $ enemy_type = 1
    $ enemy_skills = [Enemyattack,Enemyquickattack,Enemyquickattack]
    $ enemy_attack = 65
    $ enemy_defense = 0
    $ enemy_magdefense = 0
    $ Humansoldier.face = "angry"
    $ player = Sabia
    $ enemy = Humansoldier
    call duel
    if _return == "Victory":
        scene bg hcmcastle
        show Sabia at left
        with dissolve
        $ v10lynn_robert_dead = True
        $ Sabia.face = "normalopen"
        s "Hmph. Well... maybe Fennasil might be pleased to learn that that... issue of hers is resolved."
        s "Not really what I had intended."
    else:
        scene bg black with dissolve
        "Sabia woke up several hours later, shoved into a small closet in a corner."
        scene bg hcmcastle
        show Sabia at left
        show Humansoldier at right
        with dissolve
        $ Sabia.face = "closed2"
        $ money = 0
        "Her head throbbed painfully, and thought she still had all of her items, she could tell her coin purse was much lighter."
        $ Sabia.face = "normal"
        robert "Don't move in on my territory. One warning."
        scene bg black with dissolve
        scene bg hcmcastle
        show Sabia at left
        $ Sabia.face = "irritated2"
        with dissolve
        s "Hmph."
        $ Sabia.face = "normalopen"
        s "I have no intention of doing so, probably best to simply leave it for now. I doubt I'd be able to find him without some effort for the next few days, anyway."
        s "He probably went to ground."
        $ Sabia.face = "normal"
        "Sabia shuffled to her feet and gathered herself."
    if v10lynn_hal_deal != "":
        "Regardless, I should let Dajrab know what I have learned."
    else:
        $ v10lynn_hal_chase = 1
        if v10lynn_hal_cleared == False:
            "Deciding to scout out the other quarters, William's seemed undisturbed, but Hal's door was wide open, and the room a mess. It looked as if someone had fled. Quickly."
        $ Sabia.face = "normalopen"
        s "Well, at least I know who I am after now, I suppose..."
        s "But now I have to find him all again."
        $ Sabia.face = "irritated2"
        s "..."
        $ Sabia.face = "normalopen"
        s "Maybe I can see if Amelia can help again, since she pointed me in the right direction..."
        $ Sabia.face = "normal"
    scene bg black with dissolve
    jump avarton_town


label v10lynn_information:
    $ v10lynn_information_acquired = True
    $ Humansoldier.face = "sad"
    hal "Okay... look."
    hal "There was so much..."
    s "So much what?"
    $ Humansoldier.face = "surprised"
    hal "Gold! Money! Lundils!"
    $ Humansoldier.face = "sad"
    hal "I took... a tiny little bit. They barely paid me enough to make ends meet... and not long after I took it, they sent people looking and-"
    s "That's not what I'm after. I want to know what Lynn is doing. Why has she come to Whitecrest? What is she up to there?"
    hal "...I don't know everything. I was just a guard there."
    $ Humansoldier.face = "surprised"
    hal "But from what I did... and what I overheard, it sounds like Lynn is cleaning house."
    $ Humansoldier.face = "sad"
    hal "Trying to tie up some loose ends with her bandit connections-"
    s "Bandits?"
    hal "Yeah. She had something to do with some bandits south of Whitecrest... I'm not really sure, honestly. But I was delivering some gold to them..."
    $ Humansoldier.face = "surprised"
    hal "I just couldn't help it. There was so much. I didn't think they'd notice, I figured the bandits would just be happy about it..."
    $ Humansoldier.face = "sad"
    s "But they did notice."
    hal "Well. Not the bandits themselves... that apprentice Lynn had with her that sent to go with the bandits. She knew."
    s "(Lynn is funding the bandits...? I guess that makes sense... I wouldn't put it past her. Putting more and more pressure on Whitecrest, and Barrin as well.)"
    hal "But that's all I know, I swear!"
    s "Are you sure? What about who Lynn spent time with in Whitecrest? What she did?"
    "Hal shook his head."
    hal "No. Wait... well, I mean it's not really anything, but she spent a lot of time with Andian's wife."
    $ Humansoldier.face = "surprised"
    hal "But I figured they were just friends."
    $ Humansoldier.face = "sad"
    s "(Lynn? Friends? Hmph. Not likely.)"
    hal "Please. That's all I know. I need to get out of here. I need to pack!"
    s "Fine, thanks for the information. If you make it to Carchedon or something... try not to steal. You might last a bit longer."
    $ Humansoldier.face = "surprised"
    hal "...yeah. I've learned my lesson."
    $ Humansoldier.face = "sad"
    "Sabia left Hal to his devices. Whether he would take her advice or not, she supposed it was not her issue anymore."
    scene bg black with dissolve
    pause (0.1)
    scene bg hcmcastle
    $ Sabia.face = "normal"
    show Sabia at left
    with dissolve
    "She had learned a few things she would need to ponder over in the coming days."
    if orcalliance == "sabia":
        $ v10lynn_quest_done = True
    if orcalliance == "dajrab":
        "She would also have to report to Dajrab."
    elif orcalliance == "rokgrid":
        "She would also have to report to Rokgrid."
    if v10lynn_hal_deal == "threat":
        $ Sabia.face = "closed2"
        "...hmm. Maybe I should pretend to be a mage more often. I do have the look if I lean into it a bit, I suppose..."
        "Sabia closed the door behind her. She had learned a few things she would need to ponder over in the coming days."
    if v10lynn_hal_deal == "":
        jump rogue_fight
    scene bg black with dissolve
    jump avarton_town


label avarton_brothel:
    scene bg hcmbrothel
    show screen infohud("left")
    if avarton_first_visit_brothel == False:
        $ avarton_first_visit_brothel = True
        $ Sabia.face = "normal"
        show Sabia at left
        "The smell of sex hit Sabia as she walked in. Heavy, strong, and almost overbearing."
        "Sounds of heavy thuds, raw moans and high squeaks echoed around the building."
        "The common room was filled with men and women. The girls were mostly naked; loose-fitting clothes that shifted and moved with every step, enough to see everything."
        "It didn't bother any of the patrons, of course. Sabia caught a few of them leering at her as well."
        if Sabia.armor == Orcslavearmor:
            $ Fennasil.face = "happy"
            show Fennasil at right with moveinright
            madame "Oh, hello there, sweet. You're certainly not one of my girls. Looking for work? You can call me Madame Fennasil."
            $ Fennasil.face = "normal"
            "She wrapped a hand around Sabia's arm."
            $ Sabia.face = "irritated1"
            $ Fennasil.face = "happy"
            madame "Come! We can start you off right away - I know just the man who will love those tits, and that purple hair, he's just-"
            $ Sabia.face = "angry1"
            $ Fennasil.face = "normal"
            s "Hey! I'm not here to work. I'm not a whore."
            $ Sabia.face = "angry2"
            "The woman blinked, taking a step back."
            $ Fennasil.face = "browsopen"
            madame "Ah. My apologies... but..."
            $ Fennasil.face = "normal"
            "She waved her hands in Sabia's direction."
            $ Fennasil.face = "normalopen"
            madame "Wearing that in here... you can see my confusion, yes?"
            $ Fennasil.face = "normal"
            $ Sabia.face = "irritated1"
            $ Fennasil.face = "normalopen"
            madame "If you're not here to work, why would you be in here, dressed like? Seems a bit... hmm."
            $ Fennasil.face = "normal"
            menu:
                "I like dressing like this.":
                    $ sub += 1
                    $ Sabia.face = "angry1"
                    s "I like wearing this..."
                    $ Sabia.face = "normalopen"
                    s "It's just that..."
                    $ Sabia.face = "closed2"
                    s "..."
                    $ Sabia.face = "angry1"
                    s "Well, I like wearing it!"
                    $ Sabia.face = "irritated1"
                    $ Fennasil.face = "browsopen"
                    madame "Okay, that's fine, sweet. Just maybe change out of it if you're visiting here, okay? Unless you want some attention."
                    $ Fennasil.face = "normalopen"
                    madame "The bar does have a strict no touching policy... but I can't promise no verbal attention. And there are a few that like to break the rules, of course..."
                    $ Fennasil.face = "normal"
                    "Sabia nodded her thanks and let the Madame get back to work."
                    hide Fennasil
                "I forgot I was wearing it.":
                    $ Sabia.face = "normalopen"
                    s "Uh. I forgot I was wearing it, to be honest. It was... uhm, necessary, for something."
                    $ Sabia.face = "normal"
                    "The madame pursed her lips, frowning."
                    $ Sabia.face = "irritated1"
                    madame "If you say so..."
                    madame "Well, you are welcome to browse, but I would suggest maybe wearing something else unless you want a lot of attention."
                    $ Fennasil.face = "normalopen"
                    madame "The bar does have a strict no touching policy... but I can't promise no verbal attention. And there are a few that like to break the rules, of course..."
                    $ Fennasil.face = "normal"
                    "Sabia nodded her thanks and let the Madame get back to work."
                    hide Fennasil
        elif Sabia.armor == Rags:
            $ Fennasil.face = "browsopen"
            show Fennasil at right with moveinright
            madame "Oh... oh dear. Hello there, sweetie... do you need some food?"
            $ Fennasil.face = "normal"
            $ Sabia.face = "normalopen"
            s "Huh?"
            $ Sabia.face = "irritated2"
            $ Fennasil.face = "browsopen"
            madame "If you're here to work... we can see about that after getting you fixed up, alright?"
            $ Fennasil.face = "normal"
            $ Sabia.face = "normalopen"
            s "What are you talking about?"
            $ Sabia.face = "irritated1"
            $ Fennasil.face = "browsopen"
            madame "Uhmm..."
            "The woman gestured up and down Sabia's body."
            $ Sabia.face = "normal"
            madame "Those rags you have on, dear?"
            $ Fennasil.face = "normal"
            $ Sabia.face = "normalopen"
            s "Oh!"
            s "I'm not poor. It was just necessary to wear these for something."
            $ Sabia.face = "normal"
            $ Fennasil.face = "browsopen"
            madame "And you didn't think to change after...? Well, no matter! As long as you know."
            $ Fennasil.face = "normalopen"
            madame "Well, if you're not looking for work, I would suggest coming back a bit more clothed unless you like the attention."
            madame "If you're so inclined, we do have a bar that way as well... we have a strict rule about touching and propositioning there..."
            $ Fennasil.face = "normal"
            $ Sabia.face = "irritated2"
            "Her gaze flickered up and down Sabia once more."
            $ Fennasil.face = "normalopen"
            madame "But I can't promise you won't get some verbal attention. Or some that like to break rules."
            hide Fennasil
        else:
            $ Fennasil.face = "happy"
            show Fennasil at right with moveinright
            madame "Hmm. I think I have the girl for you - three hundred lundils an hour. Though I don't think you'll need longer than that."
            $ Sabia.face = "surprised1"
            madame "Come along, then!"
            $ Fennasil.face = "normal"
            "The woman wrapped her hand around Sabia, and started to pull her towards the stairs."
            $ Sabia.face = "normalopen"
            s "Uh, what?"
            $ Sabia.face = "normal"
            $ Fennasil.face = "browsopen"
            madame "Well, you're far too pretty to not find a man easily. And you don't look like you're after any work."
            $ Sabia.face = "irritated2"
            $ Fennasil.face = "happy"
            madame "Which means you must be here for a girl. We have just the girl - you'll love her. Very cute."
            madame "Young, blonde, tight body and a {i}very{/i} talented tongue!"
            $ Fennasil.face = "normal"
            $ Sabia.face = "normalopen"
            s "I'm not after any girls!"
            $ Sabia.face = "irritated1"
            $ Fennasil.face = "happy"
            madame "Oh, you are after a man, then? Okay, well, we have those too! But the choice is a bit more limited-"
            $ Sabia.face = "normalopen"
            $ Fennasil.face = "normal"
            s "I'm not after any men, either!"
            $ Sabia.face = "irritated1"
            "The woman paused for a moment, frowning."
            $ Sabia.face = "irritated2"
            $ Fennasil.face = "normalopen"
            madame "Then, dear, what are you doing in my establishment?"
            $ Sabia.face = "normalopen"
            $ Fennasil.face = "normal"
            s "I was just checking it out. Looking doesn't cost, does it?"
            $ Sabia.face = "irritated1"
            $ Fennasil.face = "normalopen"
            madame "Not here, no... but you'll excuse me of course. When someone comes in here, naturally I assume they're after a girl."
            madame "You're free to look around, of course. My girls and I are very proud of ourselves. There's a bar that way, if you're so inclined."
            $ Fennasil.face = "normal"
            $ Sabia.face = "irritated2"
            $ Fennasil.face = "normalopen"
            madame "We have a strict rule about touching and propositioning in the bar - but you might still get a bit of verbal attention. And there are those who like to break the rules, of course."
            $ Fennasil.face = "happy"
            madame "But I don't think you'll have to worry too much, dressed sensibly like that!"
            $ Fennasil.face = "normal"
            madame "There's always the Stone Lion on the other side of the town center, if you would rather have a drink in peace."
            $ Sabia.face = "normal"
            "Sabia nodded, thanking Fennasil for her help."
            hide Fennasil

    if orcalliance == "sabia" and v10lynn_quest_done == False and (v10lynn_quest_madame_hal == True or v10lynn_quest_madame_william == True or v10lynn_quest_madame_robert == True) and v10lynn_amelia_post_talk == False:
        $ v10lynn_amelia_post_talk = True
        $ Amelia.face = "browshappy"
        $ Sabia.face = "pout2"
        show Sabia at left
        show Amelia at right
        with dissolve
        amelia "Well! I guess you were a little more interested than you let on, huh?"
        $ Amelia.face = "normal"
        $ Sabia.face = "pout3"
        s "..."
        $ Sabia.face = "normalopen"
        s "A bit."
        s "I'll be honest, I'm after some information and I think one of the characters you described might be useful."
        $ Amelia.face = "happy"
        $ Sabia.face = "normal"
        amelia "Well, Sabia, gosh!"
        $ Sabia.face = "irritated1"
        amelia "You should have just told me that to start with, instead of dancing around!"
        $ Amelia.face = "look"
        amelia "..."
        $ Amelia.face = "normal"
        s "..."
        $ Sabia.face = "normal"
        $ Amelia.face = "browshappy"
        amelia "Though I think I'd like to see you dancing around sometime!"
        $ Amelia.face = "happy"
        amelia "But anyway, you should have just told me. I would have been happy to help!"
        $ Amelia.face = "normal"
        "Sabia gave a nod and smiled."
        $ Sabia.face = "happy2"
        s "I'll keep that in mind, Amelia. Thanks."
        $ Sabia.face = "normal"
        $ Amelia.face = "browshappy"
        amelia "Sure, cute stuff. Come back some time to say 'thanks'?"
        $ Amelia.face = "normal"
        $ Sabia.face = "normalopen"
        s "Maybe, Amelia! I'll see you later."
        $ Sabia.face = "normal"
        "Amelia gave a pout as Sabia left."
        jump avarton_brothel

    if (v10lynn_quest_done == True or v10tekrok_quest_done == True) and v10amelia_prompt == False:
        $ v10amelia_prompt = True
        $ v10amelia_days = 1
        $ Sabia.face = "normal"
        $ Amelia.face = "happy"
        show Sabia at left
        show Amelia at right
        with dissolve
        amelia "Hey Sabia!"
        $ Sabia.face = "irritated2"
        amelia "I'm afraid I'm going to call in a favor, after all the help I've given you."
        $ Amelia.face = "normal"
        $ Sabia.face = "normalopen"
        s "What sort of favor...?"
        $ Sabia.face = "question1"
        $ Amelia.face = "happy"
        amelia "Giving me the privilege of your pretty company, of course!"
        $ Amelia.face = "normal"
        s "..."
        $ Sabia.face = "irritated2"
        "Sabia narrowed her eyes."
        $ Sabia.face = "normalopen"
        s "And what exactly does this involve?"
        $ Sabia.face = "normal"
        $ Amelia.face = "happy"
        amelia "Oh, nothing like that, silly!"
        amelia "I'd never be so coy about {i}that{/i}."
        amelia "Have you ever seen The Radiant Dawn?"
        $ Amelia.face = "normal"
        $ Sabia.face = "normalopen"
        s "...The Radiant Dawn?"
        s "Isn't that the title of a Lustrator?"
        $ Sabia.face = "normal"
        "Amelia nodded emphatically."
        $ Amelia.face = "happy"
        amelia "Uh-huh!"
        $ Amelia.face = "normal"
        $ Sabia.face = "normalopen"
        s "What about her?"
        $ Sabia.face = "normal"
        $ Amelia.face = "happy"
        amelia "Well! I heard some whispers that she is a nearby town. I don't think I've ever seen a Lustrator!"
        $ Sabia.face = "normalopen"
        $ Amelia.face = "normal"
        s "You want to go and meet a Lustrator?"
        $ Sabia.face = "normal"
        $ Amelia.face = "sadopen"
        amelia "Oh, meet... no, no."
        amelia "I wouldn't want to waste her time."
        $ Amelia.face = "happy"
        amelia "But it would be wonderful to go and at least see a Lustrator, especially The Radiant Dawn!"
        $ Amelia.face = "normal"
        $ Sabia.face = "normalopen"
        s "Hmm, I see."
        $ Sabia.face = "normal"
        $ Amelia.face = "sadopen"
        amelia "You'll come, of course?"
        $ Amelia.face = "normal"
        $ Sabia.face = "happy2"
        s "Well, can I really say no after how nice you are to me all the time?"
        $ Sabia.face = "normal"
        "Amelia grinned."
        $ Amelia.face = "happy"
        amelia "Of course not, cutie."
        amelia "Come back when you are ready to go! But don't be too long. We should go today or tomorrow at the latest!"
        jump avarton_brothel

    menu:
        "Grab a drink.":
            if money < 10:
                $ Sabia.face = "normal"
                show Sabia at left
                s "(Drinks are 10 lundils. I don't have enough on me right now.)"
                jump avarton_brothel
            if avarton_drinks == 0:
                $ avarton_drinks = 1
                $ Sabia.face = "normal"
                show Sabia at left
                "Sabia took a seat at the brothel's bar."
                show Amelia at right with moveinright
                $ Amelia.face = "happy"
                bartender "Huh. Hey there, cutie. What'll it be?"
                $ Amelia.face = "normal"
                $ Sabia.face = "normalopen"
                s "Uh, just some... ale?"
                $ Sabia.face = "normal"
                $ Amelia.face = "happy"
                bartender "Sure. Ten lundils."
                $ Sabia.face = "surprised1"
                $ Amelia.face = "browshappy"
                bartender "Or on the house if you take that top off."
                $ Amelia.face = "normal"
                $ Sabia.face = "surprised2"
                s "I - what?"
                $ Sabia.face = "sad1"
                "The bartender shrugged."
                $ Sabia.face = "normal"
                $ Amelia.face = "happy"
                bartender "I think you're cute. And I want to get a look."
                $ Amelia.face = "normal"
                menu:
                    "Sure.":
                        $ showed_tits_amelia = True
                        $ met_amelia = True
                        $ sub += 1
                        $ A_amelia +=1
                        $ Sabia.face = "normalopen"
                        s "Uh. Yeah, I suppose. I mean, it is a brothel. It's not out of the ordinary."
                        $ Sabia.face = "normal"
                        "Sabia could see no less than seven other women with literally {i}no{/i} clothes on."
                        bartender "Right?!"
                        $ Tpanel.extras = []
                        $ Tpanel.expression = "normal (2)"
                        $ Tpanel.armor = "Nude"
                        show Tpanel at right, menu_right
                        $ Amelia.face = "browshappy"
                        bartender "Nice!"
                        hide Tpanel
                        "Grinning widely, she slid a mug of ale over the counter to Sabia."
                        $ Amelia.face = "normal"
                        $ Sabia.face = "normalopen"
                        s "If you like girls so much... it seems like you wouldn't need to ask me to show off for you, though?"
                        $ Sabia.face = "normal"
                        $ Amelia.face = "browshappy"
                        bartender "I get to see them anytime. It's more fun when it's someone that doesn't work in a brothel."
                        $ Amelia.face = "happy"
                        bartender "Besides, your tits are great. Maybe you could sit just a little lower on the stool-"
                        patron "Amelia!"
                        $ Amelia.face = "normalopen"
                        bartender "-so that they're resting there? That'd be a nice sight, and I can tell you that-"
                        $ Amelia.face = "look"
                        patron "Amelia!"
                        $ Amelia.face = "angryopen"
                        amelia "What, Jerrad?!"
                        $ Sabia.face = "irritated1"
                        $ Amelia.face = "angry"
                        patron "Can I get some fucking service?"
                        $ Sabia.face = "irritated2"
                        $ Amelia.face = "angryopen"
                        amelia "Yeah. You're in a whorehouse. Fucking service is the whole idea."
                        $ Amelia.face = "angry"
                        patron "Do I need to fucking get your boss again? Stop hitting on that slut and come serve us."
                        $ Sabia.face = "normal"
                        $ Amelia.face = "normal"
                        "The bartender turned back to Sabia."
                        $ Amelia.face = "normalopen"
                        amelia "Sorry, cutie. But I've got to go back to work. You've got my name now - what's yours?"
                        $ Amelia.face = "normal"
                        $ Sabia.face = "normalopen"
                        s "Sabia."
                        $ Sabia.face = "normal"
                        amelia "Mmm."
                        $ Amelia.face = "happy"
                        amelia "Hope to see you around a bit more."
                        $ Amelia.face = "normal"
                        "Amelia turned and stormed down towards the yelling patron, slamming a mug on the bench hard enough that half the drink sloshed out over the top."
                        "Sabia shrugged. She put her top back on and finished the drink before heading off."
                        jump avarton_brothel
                    "Here's ten lundils.":
                        $ money -= 10
                        $ Amelia.face = "wicked"
                        "The bartender gave a pouting frown."
                        $ Amelia.face = "sadopen"
                        bartender "Fi{i}iii{/}ine. Here's your ale."
                        jump avarton_brothel

            elif avarton_drinks == 1:
                $ Sabia.face = "normal"
                show Sabia at left
                if showed_tits_amelia == True:
                    $ Amelia.face = "happy"
                    show Amelia at right with moveinright
                    amelia "Hey, you. You're back."
                    $ Amelia.face = "normal"
                    "Amelia grinned, leaning forward and planting her elbows on the countertop, resting her chin in her hands."
                    "Her ass stuck out behind her just enough to be seen. She made sure it was seen with a little wiggle."
                    $ Sabia.face = "normalopen"
                    s "Hi, Amelia."
                    $ Sabia.face = "normal"
                    $ Amelia.face = "happy"
                    amelia "So what'll it be?"
                    $ Amelia.face = "normal"
                    $ Sabia.face = "normalopen"
                    s "Just a drink."
                    $ Sabia.face = "question1"
                    $ Amelia.face = "happy"
                    amelia "And how're you paying, cutie?"
                    menu:
                        "With lundils.":
                            $ money -= 10
                            $ Sabia.face = "normal"
                            $ Amelia.face = "brows"
                            "Sabia placed ten lundils on the bench."
                            $ Sabia.face = "normalopen"
                            s "Just with lundils this time."
                            $ Sabia.face = "normal"
                            $ Amelia.face = "sadopen"
                            amelia "Aww. Too bad..."
                            $ Amelia.face = "brows"
                            "Frowning, Amelia slid a drink down to Sabia."
                            jump avarton_brothel
                        "With tits.":
                            $ sub += 1
                            "Amelia grinned widely, nibbling a nail lightly in the corner of her mouth."
                            $ Amelia.face = "happy"
                            amelia "Sorry, you can't pay for booze with tits here."
                            $ Sabia.face = "angry1"
                            $ Amelia.face = "normal"
                            s "What! You're the one that wanted me to do that last time, and-"
                            $ Sabia.face = "irritated2"
                            $ Amelia.face = "browshappy"
                            amelia "Well, yes. {i}Last{/i} time. But costs go up, you know."
                            $ Amelia.face = "happy"
                            amelia "Now you have to show me that ass!"
                            $ Amelia.face = "normal"
                            menu amelia_ale_bargain_menu:
                                "Alright...":
                                    $ avarton_drinks = 2
                                    $ showed_ass_amelia = True
                                    $ Sabia.face = "closed2"
                                    s "..."
                                    $ Sabia.face = "normalopen"
                                    s "Alright then, but only because I really want that drink."
                                    $ Sabia.face = "irritated2"
                                    $ Amelia.face = "happy"
                                    amelia "Mmhmm, mhm! I think you just like showing off. But that's alright, I like looking! Go on!"
                                    $ Sabia.face = "normal"
                                    $ Amelia.face = "normal"
                                    "Sabia didn't want to correct Amelia. It was less showing off, and more that she kind of liked following the bossy bartender's requests."
                                    $ Sabia.face = "irritated1"
                                    $ Amelia.face = "brows"
                                    "Standing up, Sabia was met with a worried gasp from Amelia."
                                    $ Sabia.face = "normal"
                                    $ Amelia.face = "browshappy"
                                    amelia "Hey, hey, hey! Not there. I won't see properly! Come down to the end... just around the bar. That way no one else gets to see either."
                                    $ Sabia.face = "happy2"
                                    $ Amelia.face = "normal"
                                    s "That's a better idea."
                                    $ Sabia.face = "normal"
                                    "Sabia nodded, and walked down. Their conversation had gone unheard in the brothel's din."
                                    "Amelia grabbed at Sabia's hand and yanked her through the little swinging door."
                                    scene bg black with dissolve
                                    pause(1)
                                    scene bg hcmbrothel
                                    show Sabia at left
                                    show Amelia at right
                                    with dissolve
                                    "Sabia started to wriggle out of her leggings."
                                    $ Sabia.face = "surprised1"
                                    $ Bpanel.armor = "Nude"
                                    $ Bpanel.extras = []
                                    show Bpanel at right, menu_right
                                    "She was only halfway there before Amelia made a clicking sound with her tongue, hand darting out and yanking the clothing down."
                                    amelia "Nice!"
                                    $ Sabia.blush = "true"
                                    call shake ("h")
                                    $ Amelia.face = "angrysmile"
                                    "Amelia's hand pulled back and slapped down on Sabia's ass hard enough to make her jump."
                                    $ Sabia.face = "normalopen"
                                    hide Bpanel
                                    s "We never said anything about touching!"
                                    $ Sabia.face = "normal"
                                    $ Amelia.face = "browshappy"
                                    amelia "Hehe, well I guess I'll slide you an extra drink then, huh, cutie?"
                                    $ Sabia.face = "pout1"
                                    amelia "Put your pants back on and get back around before someone thinks I'm using the wares!"
                                    $ Amelia.face = "normal"
                                    $ Sabia.face = "normalopen"
                                    s "The wares...?"
                                    s "Maybe I should have just paid you the lundils."
                                    $ Sabia.face = "normal"
                                    $ Amelia.face = "browshappy"
                                    amelia "Aww, don't be like that. I'm just having a bit of fun! You like fun, right?"
                                    $ Sabia.face = "pout3"
                                    $ Amelia.face = "happy"
                                    amelia "Of course you do. Or you wouldn't have gone along with me."
                                    $ Amelia.face = "normal"
                                    "Amelia giggled to herself, eminently pleased. She slid two drinks along the bench, down to Sabia's seat."
                                    $ Sabia.face = "normal"
                                    "For the rest of the evening Amelia was mainly serving, and didn't get to chat too much to Sabia."
                                    jump avarton_brothel
                                "If you take off your top." if amelia_asked_to_show_tits == False:
                                    $ amelia_asked_to_show_tits = True
                                    $ Amelia.face = "happy"
                                    amelia "Oh, I like your thinking! But I can't. See, people will think I'm one of the girls working on their back, if I do that, right?"
                                    amelia "And then, it makes it hard to serve drinks! Because all the other girls can be had, but I'm the one that can't!"
                                    $ Amelia.face = "browshappy"
                                    amelia "So, naturally {i}everyone{/i} wants to have a go with me - so it'll be mayhem!"
                                    jump amelia_ale_bargain_menu
                                "No!":
                                    s "..."
                                    $ Sabia.face = "normalopen"
                                    $ Amelia.face = "angry"
                                    s "I'm not going to do that!"
                                    $ Sabia.face = "normal"
                                    "Amelia pouted, shifting her hips and putting her weight onto one foot."
                                    $ Amelia.face = "normalopen"
                                    amelia "Oh? What's that? I just heard someone asking for service. Byeee!"
                                    $ Sabia.face = "irritated1"
                                    $ Amelia.face = "normal"
                                    "She gave a coy wave to Sabia before walking a few feet down the bench."
                                    s "..."
                                    $ Sabia.face = "normalopen"
                                    s "I guess I'm not getting served tonight, then..."
                                    jump avarton_brothel
                else:
                    $ Amelia.face = "normalopen"
                    show Amelia at right with moveinright
                    bartender "Hey, you're back!"
                    $ Sabia.face = "irritated1"
                    bartender "Gonna show me those tits yet, cutie?"
                    $ Amelia.face = "happy"
                    bartender "It's not out of the ordinary here anyway - no one will even notice, I bet!"
                    $ Amelia.face = "normal"
                    menu:
                        "Show tits.":
                            $ showed_tits_amelia = True
                            $ met_amelia = True
                            $ sub += 1
                            $ A_amelia +=1
                            $ Sabia.face = "normalopen"
                            s "Uh. Yeah, I suppose. I mean, it is a brothel. It's not out of the ordinary."
                            $ Sabia.face = "normal"
                            "Sabia could see no less than seven other women with literally {i}no{/i} clothes on."
                            $ Amelia.face = "browshappy"
                            bartender "Right?!"
                            $ Amelia.face = "happy"
                            $ Tpanel.extras = []
                            $ Tpanel.expression = "normal (2)"
                            $ Tpanel.armor = "Nude"
                            show Tpanel at right, menu_right
                            bartender "Nice!"
                            hide Tpanel
                            "Grinning widely, she slid a mug of ale over the counter to Sabia."
                            $ Sabia.face = "normalopen"
                            $ Amelia.face = "normal"
                            s "If you like girls so much... it seems like you wouldn't need to ask me to show off for you, though?"
                            $ Sabia.face = "normal"
                            $ Amelia.face = "normalopen"
                            bartender "I get to see them anytime. It's more fun when it's someone that doesn't work in a brothel."
                            $ Amelia.face = "happy"
                            bartender "Besides, your tits are great. Maybe you could sit just a little lower on the stool-"
                            patron "Amelia!"
                            bartender "-so that they're resting there? That'd be a nice sight, and I can tell you that-"
                            $ Amelia.face = "look"
                            patron "Amelia!"
                            $ Amelia.face = "angryopen"
                            amelia "What, Jerrad?!"
                            $ Amelia.face = "angry"
                            $ Sabia.face = "irritated1"
                            patron "Can I get some fucking service?"
                            $ Sabia.face = "irritated2"
                            $ Amelia.face = "angryopen"
                            amelia "Yeah. You're in a whorehouse. Fucking service is the whole idea."
                            $ Amelia.face = "angry"
                            patron "Do I need to fucking get your boss again? Stop hitting on that slut and come serve us."
                            $ Sabia.face = "normal"
                            $ Amelia.face = "normal"
                            "The bartender turned back to Sabia."
                            $ Amelia.face = "browshappy"
                            amelia "Sorry, cutie. But I've got to go back to work. You've got my name now - what's yours?"
                            $ Amelia.face = "normal"
                            $ Sabia.face = "normalopen"
                            s "Sabia."
                            $ Sabia.face = "normal"
                            amelia "Mmm."
                            $ Amelia.face = "happy"
                            amelia "Hope to see you around a bit more."
                            $ Amelia.face = "angry"
                            "Amelia turned and stormed down towards the yelling patron, slamming a mug on the bench hard enough that half the drink sloshed out over the top."
                            "Sabia shrugged. She put her top back on and finished the drink before heading off."
                            jump avarton_brothel
                        "Here's ten lundils.":
                            $ money -= 10
                            $ Amelia.face = "brows"
                            "The bartender gave a pouting frown."
                            $ Amelia.face = "sadopen"
                            bartender "Fine. Here's your ale."
                            jump avarton_brothel

            elif avarton_drinks == 2:
                $ avarton_drinks = 3
                $ Sabia.face = "normal"
                show Sabia at left
                $ Amelia.face = "happy"
                show Amelia at right with moveinright
                amelia "Heeeey! It's my favorite customer."
                $ Sabia.face = "happy2"
                $ Amelia.face = "normal"
                s "Favorite already?"
                $ Sabia.face = "normal"
                $ Amelia.face = "browshappy"
                amelia "Of course... even if you weren't, I'd have to say that anyway."
                $ Amelia.face = "normal"
                $ Sabia.face = "normalopen"
                s "Then how can I trust you?"
                $ Sabia.face = "question1"
                $ Amelia.face = "happy"
                amelia "I wouldn't be asking you to flash me so much if you weren't."
                s "..."
                $ Amelia.face = "look"
                $ Sabia.face = "normalopen"
                s "I don't know if I can believe that."
                $ Amelia.face = "browshappy"
                $ Sabia.face = "normal"
                amelia "Mmm... I wouldn't."
                $ Amelia.face = "normal"
                "Amelia smirked coyly, sauntering off to serve another patron."
                "Sabia expected her to return at some point... but for the most part Amelia simply did her job."
                "Albeit, with a few stolen glances every now and then."
                jump avarton_brothel

            elif avarton_drinks == 3:
                $ Sabia.face = "normal"
                show Sabia at left
                $ Sabia.face = "irritated2"
                $ Amelia.face = "happy"
                show Amelia at right with moveinright
                $ money -= 5
                amelia "Aww, come back to see me again cutie? You'll have to wait for another time, I'm afraid!"
                $ Amelia.face = "sadopen"
                amelia "It's too busy tonight for you to get all my attention!"
                $ Sabia.face = "normalopen"
                $ Amelia.face = "normal"
                s "Well, can I grab a drink at least?"
                $ Sabia.face = "normal"
                $ Amelia.face = "browshappy"
                amelia "Of course! Five lundils for you!"
                $ Amelia.face = "normal"
                "Sabia slid the coin across the table, and took the drink from Amelia before the bartender slid down to some other drunk patrons."
                jump avarton_brothel
        "Watch for a bit.":

            $ Sabia.face = "normal"
            show Sabia at left
            "Sabia took a seat at one of the tables a bit farther from the bar."
            if Sabia.armor == Orcslavearmor or Sabia.armor == Rags:
                if met_amelia == True and amelia_brothel_talk == False:
                    $ amelia_brothel_talk = True
                    show Humansoldier at right with dissolve
                    $ Humansoldier.face = "happy"
                    patron "Well, hello there."
                    $ Sabia.face = "irritated2"
                    "His lips were curled up in an almost-slimey grin as he took a seat next to Sabia, squeezing himself up against her."
                    $ Humansoldier.face = "normal"
                    "He wrapped an arm around Sabia's shoulder, and his hand moved down a little bit, fingers running along the uncovered flesh of Sabia's breast."
                    "He was so quick and practiced, that Sabia had barely blinked before she felt his hand on her."
                    menu:
                        "Get. Off.":
                            $ Sabia.face = "angry1"
                            $ Humansoldier.face = "angry"
                            s "What do you think you're doing?"
                            $ Sabia.face = "angry2"
                            "Sabia growled her anger, and twisted his arm back and pushed him off of her."
                            patron "Argh, fuck!"
                            $ Humansoldier.face = "surprised"
                            "She couldn't help a small vicious grin of satisfaction spread as she pushed him off the seat, and he landed with a thud on the ground."
                            $ Sabia.face = "angry1"
                            s "This is the bar. Keep your hands to yourself, unless you want me to break them next time."
                            $ Sabia.face = "angry2"
                            "He clambered to his feet, grunting and flustered."
                            $ Sabia.face = "annoyed2"
                            $ Humansoldier.face = "angry"
                            patron "You don't have to be such a fucking cunt about it. Like I wanted to talk to you anyway. Slut."
                            "Sabia rolled her eyes."
                        "Say hello.":
                            $ sub += 1
                            $ A_amelia += 1
                            "Sabia wriggled a little bit under his grip, but she didn't move or try to push him away."
                            $ Sabia.face = "normalopen"
                            $ Humansoldier.face = "happy"
                            s "Uh, hi there..."
                            $ Sabia.face = "sad1"
                            patron "So... when's a hot thing like you heading back to work, huh? I got a pocket full of coin, and trousers full of cock."
                            "He licked his lips a bit more, squeezing up tighter against Sabia."
                            "With his free hand, he leaned over and placed it on Sabia's thigh, fingers slipping between her legs."
                            $ Sabia.face = "sad3"
                            $ Humansoldier.face = "angry"
                            s "Isn't there... uhm - isn't there a no-touching thing in the bar?"
                            $ Sabia.face = "sad1"
                            $ Humansoldier.face = "normal"
                            patron "Yeah, sure..."
                            patron "But that's alright, isn't it? C'mon, spread those legs a bit more, baby."
                            $ Sabia.face = "sad3"
                            s "Yeah... I guess that's fine."
                            $ Sabia.face = "sad1"
                            $ Humansoldier.face = "happy"
                            "The man smirked. He leaned farther over, pressing his lips up against Sabia's cheek."
                            patron "Mmm..."
                            "Slowly, he ran his tongue up the side of her face slowly, the tip dragging from just above her chin, all the way to the tip of her earlobe."
                            show Amelia at right with moveinright

                            $ Amelia.face = "angryopen"
                            $ Humansoldier.face = "angry"
                            bartender "Oi! Shove off! No touching in the bar. You should know better. If you want a girl, go give Fennasil some lundils!"
                            $ Amelia.face = "angry"
                            $ Sabia.blush = "true"
                            patron "It's alright. She likes it, right?"
                            $ Amelia.face = "angryopen"
                            bartender "Doesn't matter. Shove off. Or I'll get Fennasil in here and see about banning you!"
                            $ Amelia.face = "angry"
                            $ Humansoldier.face = "normal"
                            patron "Ugh. Fine."
                            $ Sabia.face = "surprised1"
                            "His voice was angry, and he made sure to grope harshly at Sabia's tits as he stumbled to his feet."
                            $ Humansoldier.face = "happy"
                            $ Tpanel.expression = "meek (1)"
                            $ Tpanel.extras = []
                            $ Tpanel.armor = "Nude"
                            show Tpanel at right, menu_right
                            patron "Heh..."
                            "His hand yanked her top down, letting her tits spill out as he walked off."


                            hide Tpanel
                            $ Amelia.face = "browshappy"
                            $ Sabia.face = "closed1"
                            bartender "You know, if you like that stuff, I'll be happy to treat you like that, cutie."
                            $ Sabia.face = "sad3"
                            $ Amelia.face = "normal"
                            s "Uh, it's not so much that I like it. It's more that I just, hmmm..."
                            $ Sabia.face = "sad1"
                            $ Amelia.face = "happy"
                            bartender "Uh-huh. Well, keep it in mind, alright?"
                            "Amelia winked slyly before walking off."
                    jump avarton_brothel

                $ temp = renpy.random.randint(1,3)
                if temp == 1:
                    show Humansoldier at right with dissolve
                    $ Humansoldier.face = "happy"
                    patron "Fuck, you'd look good with my cock inside you. How much are you?"
                    $ Sabia.face = "angry1"
                    s "I'm not a whore, I'm just sitting."
                    $ Sabia.face = "angry2"
                    $ Humansoldier.face = "angry"
                    patron "What? You're not a whore dressed like that? Whatever, I didn't want to fuck you anyway!"
                    $ Sabia.face = "irritated1"
                    "He stumbled off with a drunken gait."
                elif temp == 2:
                    show Humansoldier at right with dissolve
                    $ Sabia.face = "irritated1"
                    $ Humansoldier.face = "happy"
                    patron "Hey... bitch... where's your... where's your leash? Heh!"
                    "He stuttered his words, and the alcohol was heavy on his breath."
                    $ Sabia.face = "annoyed1"
                    $ Humansoldier.face = "angry"
                    s "Well, if I had one - you wouldn't be holding it."
                    $ Sabia.face = "annoyed2"
                    patron "Pff. Whatever!"
                else:
                    show Humansoldier at right with dissolve
                    $ Sabia.face = "normalopen"
                    $ Humansoldier.face = "angry"
                    s "Keep walking. I'm just sitting here."
                    $ Sabia.face = "normal"
                    patron "Fuck me, I didn't even fucking say anything, fucking slut!"
                jump avarton_brothel
            else:

                "She earned a few glances and leers. Not that she expected anything else in a brothel."
                "But they were mostly cursory - why bother looking at Sabia, when there were many more willing women already naked?"
                "After a while, Sabia decided she would head off."
                jump avarton_brothel

        "Chat with Amelia." if met_amelia == True:
            show Sabia at left
            show Amelia at right
            if amelia_chat == 0:
                $ amelia_chat = 1
                $ Sabia.face = "annoyed2"
                $ Amelia.face = "happy"
                show Sabia at left
                show Amelia at right
                amelia "It's my favourite cutestomer!"
                $ Sabia.face = "closed2"
                $ Amelia.face = "normal"
                s "..."
                $ Sabia.face = "happy2"
                s "That's awful."
                $ Amelia.face = "brows"
                "Still, Sabia couldn't help a wry grin appearing."
                $ Sabia.face = "normal"
                $ Amelia.face = "browshappy"
                amelia "With that smile, how could I call you anything else?"
                $ Amelia.face = "normal"
                "Amelia did her best to chat to Sabia, but a steady influx of customers made it more and more difficult."
                "Sabia decided to leave."
            elif amelia_chat == 1 and saw_amelia_temple == True:
                $ amelia_chat = 2
                $ Sabia.face = "normalopen"
                s "I saw you in the temple earlier. I didn't know you were so devout."
                $ Sabia.face = "normal"
                $ Amelia.face = "happy"
                amelia "Oh, cutie. You don't know the half of it."
                amelia "I try to live my life as close to what Relona and her sisters teach us as possible."
                $ Amelia.face = "normal"
                $ Sabia.face = "normalopen"
                s "I'm surprised."
                $ Sabia.face = "normal"
                $ Amelia.face = "normalopen"
                amelia "Why do you say that? Because I work at a brothel?"
                $ Amelia.face = "browshappy"
                amelia "A girl's gotta make money. And I'd rather serve drinks than spread my legs for cock."
                if A_amelia >= 2:
                    $ Sabia.blush = "true"
                    $ Sabia.face = "pout1"
                    $ Amelia.face = "happy"
                    amelia "But for you...?"
                    $ Amelia.face = "normal"
                    s "..."
                    "Amelia laughed prettily."
                    $ Sabia.face = "normal"
                    $ Sabia.blush = "false"
                    $ Amelia.face = "browshappy"
                    amelia "Relax, cutie."
                $ Amelia.face = "look"
                "Amelia's next words were cut off by a shouted order for some more booze."
                $ Amelia.face = "normal"
                $ Sabia.face = "normalopen"
                s "Go ahead, gotta make money as you said."
                $ Sabia.face = "normal"
                "Amelia gave an apologetic smile and moved down the counter."
                "Business picked up and Sabia soon left, not able to chat with Amelia anymore."
            else:
                "Amelia was pleased to see Sabia, and did her best to carry on a conversation in between work."
                "As the night dragged on, it got busier and Amelia was less able to chat. Sabia decided to head off."
            jump avarton_brothel

        "Check on Amelia." if rommel_quest_done == True and orcalliance == "sabia" and v10lynn_quest_prompt == False and v10introscene == True and v10maply_quest_done == True:
            $ v10lynn_quest = 1
            $ v10lynn_quest_prompt = True
            $ Sabia.face = "normal"
            show Sabia at left with dissolve
            "Amelia was leaning on the counter, running a finger through a small puddle of water on the benchtop."
            "With no one hanging around the counter at this time of day, it seemed the excitable bartender was a little bored."
            "Amelia's eyes lit up as she saw Sabia heading over."
            $ Amelia.face = "happy"
            show Amelia at right with dissolve
            amelia "Sabia! Thank Relona you're here!"
            $ Amelia.face = "brows"
            $ Sabia.face = "normalopen"
            s "What? Why?"
            $ Amelia.face = "sadopen"
            $ Sabia.face = "irritated2"
            amelia "Because I was {i}bored{/i}."
            $ Amelia.face = "happy"
            $ Sabia.face = "normal"
            amelia "I dunno about you, cute stuff, but when I'm bored I am usually pretty happy when a friend comes by that I can talk to."
            $ Amelia.face = "normal"
            $ Sabia.face = "happy3"
            s "Good point! It's usually pretty busy though, here."
            $ Sabia.face = "normal"
            "Amelia shrugged."
            $ Amelia.face = "normalopen"
            amelia "What can you do?"
            $ Amelia.face = "happy"
            $ Sabia.face = "irritated2"
            amelia "So. Let's talk about you."
            $ Amelia.face = "normal"
            $ Sabia.face = "normalopen"
            s "Me?"
            $ Amelia.face = "happy"
            $ Sabia.face = "question1"
            amelia "Yes, silly. {i}You{/i}."
            $ Amelia.face = "normal"
            $ Sabia.face = "normalopen"
            s "What about me?"
            $ Sabia.face = "irritated2"
            "Amelia reached out and tapped Sabia's nose lightly with a finger."
            $ Amelia.face = "happy"
            amelia "Where're you from?"
            $ Amelia.face = "normal"
            $ Sabia.face = "normalopen"
            s "From?"
            $ Amelia.face = "happy"
            $ Sabia.face = "normal"
            amelia "Yes! I mean, where did you grow up?"
            $ Amelia.face = "normal"
            $ Sabia.face = "normalopen"
            s "Uh, I'm from Lundar."
            $ Sabia.face = "normal"
            "Amelia rolled her eyes."
            $ Amelia.face = "happy"
            amelia "Lundar is a big place, with lots of smaller, more distinct places!"
            $ Amelia.face = "normal"
            $ Sabia.face = "normalopen"
            s "Hmm, my father was from Traus."
            s "But I spent a decent amount of time in the capital growing up."
            $ Sabia.face = "happy2"
            s "Where're you from, Amelia?"
            $ Sabia.face = "normal"
            $ Amelia.face = "happy"
            amelia "In the capital?! Huh. I bet you've seen a bunch of powerful mages, maybe even a Lustrator!"
            $ Amelia.face = "brows"
            $ Sabia.face = "normalopen"
            s "Well... I did see a Lustrator once. Certainly a few mages..."
            $ Amelia.face = "sadopen"
            $ Sabia.face = "irritated2"
            amelia "Oh... do you not like mages?"
            $ Amelia.face = "brows"
            s "..."
            $ Sabia.face = "annoyed1"
            s "Not lately."
            $ Amelia.face = "sadopen"
            $ Sabia.face = "irritated2"
            amelia "Really? Sorry to hear that, Sabia."
            $ Amelia.face = "normal"
            $ Sabia.face = "normalopen"
            s "You're not going to tell me you're secretly a mage, are you?"
            $ Amelia.face = "browshappy"
            $ Sabia.face = "normal"
            amelia "Of course not! I'm not a mage. Don't be silly!"
            $ Amelia.face = "happy"
            amelia "Maybe you should avoid Whitecrest for a little bit then! I heard there's a pretty powerful mage there visiting. Lynnal or something."
            $ Sabia.face = "irritated2"
            amelia "Lynn, actually, I think it was!"
            $ Amelia.face = "normal"
            $ Sabia.face = "normalopen"
            s "Don't think I've heard of her."
            $ Amelia.face = "happy"
            $ Sabia.face = "irritated1"
            amelia "Really?! I heard she is a powerful Archmage! Well, at least that's the rumors I've been hearing around town. There's a few people that seem to have picked up some information on this Lynn character!"
            $ Amelia.face = "normal"
            s "..."
            $ Sabia.face = "normalopen"
            s "Really?"
            $ Amelia.face = "happy"
            $ Sabia.face = "normal"
            amelia "Are you {i}suuure{/i} you're not interested in mages, even a little bit?"
            amelia "I can let you know who has been going around to Whitecrest if you were interested!"
            $ Amelia.face = "browshappy"
            amelia "It's not like we get Archmages visiting every day, it's pretty exciting!"
            $ Amelia.face = "normal"
            $ Sabia.face = "normalopen"
            s "Yeah, I suppose not. It is a bit exciting. Hmm, I guess I can get those names? I mean, if I happen to have nothing going on and I'm a bit bored, maybe they have some interesting stories!"
            $ Sabia.face = "normal"
            $ Amelia.face = "happy"
            amelia "Sure, cutie!"
            amelia "Hal, William and Robert."
            $ Amelia.face = "normalopen"
            amelia "All of them are soldiers and live in the keep. They often wander about, and meet people in the brothel on occasion."
            amelia "I would suggest that you make sure you are sure of which one has what you seek, before confronting him though. If you get it wrong, you might spook your target."
            $ Sabia.face = "irritated2"
            amelia "I think they're a bit hard to track down, you might have to ask around for them though!"
            $ Sabia.face = "normalopen"
            $ Amelia.face = "normal"
            s "Okay, I might well do that. Thanks, Amelia."
            $ Amelia.face = "browshappy"
            $ Sabia.face = "question1"
            amelia "Of course, cutie. Why don't you stay for a little bit and have a drink with me?"
            $ Amelia.face = "normal"
            menu:
                "Sure.":
                    $ A_amelia += 1
                    $ Sabia.face = "happy3"
                    s "I think that's the least I could do to say thanks!"
                    $ Sabia.face = "normal"
                    "Sabia had a drink (on the house!) with Amelia, staying to chat for a bit longer after the drink had been all downed before deciding to leave."
                "Maybe later.":
                    $ A_amelia -= 1
                    $ Sabia.face = "normalopen"
                    $ Amelia.face = "sad"
                    s "Maybe later. I should start working on this now."
                    $ Sabia.face = "normal"
                    "Amelia frowned and gave a reluctant nod as Sabia left."
            hide Amelia with moveoutright
            $ Sabia.face = "normalopen"
            s "Well, that was fortunate. I'll never turn down information on what Lynn is up to... I should look into this."
            s "But I should be careful. If anyone knows anything actually relevant... they're not going to want to give up anything easily. I should investigate before trying to talk to any of them."
            $ Sabia.face = "annoyed1"
            s "Knowing Lynn, this potential information might be in the form of someone ready to bolt if they think Archmage Lynn is looking into anything they might know..."
            jump avarton_brothel

        "Ask Amelia for information." if v10lynn_quest == 1 and v10lynn_quest_amelia == False and met_amelia == True:
            if orcalliance == "rokgrid" and v10lynn_rokgrid_contact == False:
                $ Sabia.face = "normal"
                show Sabia at left with dissolve
                "Sabia noticed that Amelia was busy at the moment and started going out of the brothel."
                "Out of the corner of her eye, she caught a glimpse of Rokgrid's contact."
                "It may be a good opportunity to talk to him while she waits for Amelia to be done with her work."
                jump avarton_brothel
            $ v10lynn_quest_amelia = True
            $ Sabia.face = "normal"
            $ Amelia.face = "normal"
            show Sabia at left
            show Amelia at right
            with dissolve
            $ Amelia.face = "happy"
            amelia "What can I do for you today, Sabia?"
            $ Amelia.face = "normal"
            "Amelia had an easy grin on her face as she asked the question, though she made little effort at hiding her gaze roaming up and down Sabia's body."
            $ Amelia.face = "browshappy"
            amelia "Or maybe you can do something for me?"
            $ Amelia.face = "brows"
            $ Sabia.face = "normalopen"
            s "The first one."
            s "I'm looking for someone in Avarton."
            $ Sabia.face = "normal"
            $ Amelia.face = "happy"
            amelia "There are a lot of someones here, cutie. You'll have to be more specific."
            $ Sabia.face = "normalopen"
            $ Amelia.face = "normal"
            s "I don't know who I'm looking for. I only know that it's someone that deals in information, and is likely selling things they learn to people that they shouldn't be."
            $ Sabia.face = "normal"
            $ Amelia.face = "angry"
            "Amelia frowned."
            $ Amelia.face = "sadopen"
            amelia "I'm afraid that's no uncommon job in bigger towns like this."
            amelia "Though if I had to, I suppose I could narrow it down to a few shady men that I know of."
            $ Amelia.face = "normal"
            $ Sabia.face = "happy3"
            s "That would be a big help."
            $ Sabia.face = "normal"
            $ Amelia.face = "normalopen"
            amelia "Why are you after this mysterious person anyway - what do they have that you need? What are you trying to find?"
            $ Amelia.face = "normal"
            $ Sabia.face = "normalopen"
            s "Information."
            $ Sabia.face = "normal"
            $ Amelia.face = "browshappy"
            amelia "Of course information, cutie!"
            amelia "But what sort of information?"
            $ Sabia.face = "normalopen"
            $ Amelia.face = "normal"
            s "That mage that is visting Whitecrest. Information about her. And the mage that came with her as well."
            $ Sabia.face = "normal"
            amelia "Hmm."
            "Amelia tapped her lips with a finger."
            $ Sabia.face = "pout1"
            $ Amelia.face = "normalopen"
            amelia "Skilled you might be with a weapon, but I'm not sure it's a good idea to tangle with a mage. I'd hate to see your good looks ruined, Sabia."
            $ Sabia.face = "pout2"
            $ Amelia.face = "browshappy"
            amelia "Before I get a chance to enjoy them, of course."
            $ Amelia.face = "normal"
            $ Sabia.face = "normalopen"
            s "Thanks for the concern, but I can handle myself well enough around a mage. I haven't always lived in an orc camp."
            $ Sabia.face = "normal"
            "Amelia chortled softly, nodding."
            $ Amelia.face = "happy"
            amelia "I imagine not!"
            amelia "Very well, let me think for a moment."
            $ Amelia.face = "normal"
            scene bg black with dissolve
            "Sabia took a seat and watched a few men coming and going, and some girls bustling about the tables with drinks and food while Amelia served a few patrons."
            "Amelia's moment dragged on a bit longer than Sabia had anticipated, but eventually she sauntered back over to Sabia and placed her elbows on the counter and rested her chin in her hands."
            scene bg hcmbrothel
            show Sabia at left
            with dissolve
            $ Amelia.face = "normalopen"
            show Amelia at center with moveinright
            amelia "I think I can point you to three that might be the one you're after."
            $ Sabia.face = "pout1"
            $ Amelia.face = "browshappy"
            "Amelia bit her lip, reaching out and running her hand down Sabia's cheek."
            amelia "I should make you pay for this, you know."
            $ Sabia.face = "pout2"
            amelia "But you're too cute, especially when you pout like that."
            $ Amelia.face = "normal"
            $ Sabia.face = "pout3"
            s "Hmph..."
            $ Sabia.face = "normalopen"
            s "So, the people?"
            $ Sabia.face = "normal"
            $ Amelia.face = "normalopen"
            amelia "Hal, William and Robert."
            amelia "All of them are soldiers and live in the keep. They often wander about, and meet people in the brothel on occassion."
            amelia "I would suggest that you make sure you are sure of which one has what you seek, before confronting him though. If you get it wrong, you might spook your target."
            $ Sabia.face = "normalopen"
            $ Amelia.face = "normal"
            s "Do you have any recommendation of which within those choices?"
            $ Sabia.face = "normal"
            $ Amelia.face = "normalopen"
            amelia "Hm. Well, Hal has only recently been transferred to this keep, though he was often in between."
            amelia "William is often in and out of both Avarton and Whitecrest, though he has always been stationed in Avarton."
            amelia "The last one is often in here somewhere. People talk when they're happy, and drunk."
            $ Amelia.face = "normal"
            $ Sabia.face = "normalopen"
            s "Here? Well, wouldn't you know enough about-"
            $ Sabia.face = "normal"
            $ Amelia.face = "sadopen"
            amelia "Sweetie, I just run the bar. Selling drinks is all I do, I'm afraid I can only point you in the right direction."
            $ Amelia.face = "normal"
            "Sabia nodded."
            $ Sabia.face = "normalopen"
            s "I understand."
            $ Sabia.face = "happy3"
            s "Thanks so much, Amelia. This is a massive help."
            $ Sabia.face = "normal"
            $ Amelia.face = "browshappy"
            amelia "Of course, cutie. Why don't you stay for a little bit and have a drink with me?"
            menu:
                "Sure.":
                    $ A_amelia += 1
                    $ Sabia.face = "happy3"
                    s "I think that's the least I could do to say thanks!"
                    $ Sabia.face = "normal"
                    "Sabia had a drink (on the house!) with Amelia, staying to chat for a bit longer after the drink had been all downed before deciding to leave."
                "Maybe later.":
                    $ A_amelia -= 1
                    $ Sabia.face = "normalopen"
                    $ Amelia.face = "sad"
                    s "Maybe later. I should start working on this now."
                    $ Sabia.face = "normal"
                    "Amelia frowned and gave a reluctant nod as Sabia left."
            hide Amelia with dissolve
            $ Sabia.face = "normalopen"
            s "Well, it seems I have a lead. Leads, I suppose. It's likely my best bet is heading over to the keep."
            scene bg black with dissolve
            jump avarton_town

        "Ask Amelia about Hal." if v10lynn_hal_chase == 1:
            $ v10lynn_hal_chase = 2
            $ Sabia.face = "normal"
            $ Amelia.face = "happy"
            show Sabia at left
            show Amelia at right
            with dissolve
            "Amelia wiggled her eyebrows as she spotted Sabia heading over toward her."
            $ Amelia.face = "happy"
            amelia "Sabia! How can I do you today?"
            $ Amelia.face = "browshappy"
            amelia "I mean... what can I do for you today! Sometimes you just distract my thoughts, you know!"
            $ Amelia.face = "normal"
            $ Sabia.face = "normalopen"
            s "Well, uh, I was wanting some more help."
            $ Sabia.face = "pout3"
            $ Amelia.face = "happy"
            amelia "I'm sure I can offer all sorts of help for you, cutie."
            $ Sabia.face = "normalopen"
            s "I'm after help finding Hal. I think that's who I am after, and I think I spooked him and he has fled Avarton."
            $ Sabia.face = "normal"
            "Amelia's face fell a little bit."
            $ Sabia.face = "irritated2"
            $ Amelia.face = "sadopen"
            amelia "I can't say I've heard anything or seen him."
            amelia "But sometimes tongues take a little bit of time to loosen before being able to find what you want."
            $ Sabia.face = "normal"
            $ Amelia.face = "normalopen"
            amelia "I'll keep an ear out for you Sabia. Come back tomorrow."
            $ Amelia.face = "happy"
            amelia "It'll be the highlight of my shift, I'm sure. Wear something cute for me?"
            menu:
                "Sure!":
                    $ A_amelia += 1
                    $ Sabia.face = "happy3"
                    $ Amelia.face = "brows"
                    s "Sure, I think I can manage that!"
                    $ Sabia.face = "normal"
                    "Amelia smiled, licking her lips."
                    $ Amelia.face = "browshappy"
                    amelia "Can't wait, cutie."
                    jump avarton_brothel
                "I'll think about it.":
                    $ Sabia.face = "normalopen"
                    $ Amelia.face = "brows"
                    s "I'll... think about it, Amelia. Not sure if that is conducive to my task at hand."
                    $ Sabia.face = "normal"
                    amelia "Maybe one day I can convince you to be fun, Sabia!"
                    jump avarton_brothel

        "Ask Amelia about Hal." if v10lynn_hal_chase == 3:
            $ v10lynn_hal_chase = 4
            $ Sabia.face = "normal"
            $ Amelia.face = "happy"
            show Sabia at left
            show Amelia at right
            with dissolve
            if Sabia.armor == Orcslavearmor or Sabia.armor == Barmaidclothes:
                $ A_amelia += 1
                $ Amelia.face = "happy"
                "Amelia's smile was from ear to ear as she saw Sabia walking over."
                amelia "Oh, gosh. That's so good on you! I {i}love it{/i}."
                "She clapped her hands together, eyes greedily drinking in Sabia's form."
                $ Amelia.face = "browshappy"
                $ Sabia.face = "normalopen"
                s "Glad you like it... decided to dress up for you since you helped me, after all."
                $ Sabia.face = "normal"
                $ Amelia.face = "happy"
                amelia "Oh, is that the only reason?"
                menu:
                    "No.":
                        $ A_amelia += 1
                        "Amelia's smirk grew wider if possible."
                        $ Amelia.face = "browshappy"
                        amelia "Good!"
                        $ Sabia.blush == True
                        $ Sabia.face = "pout2"
                        $ Amelia.face = "angrysmile"
                        amelia "Maybe next time I can convince you to do something... mm, a bit more!"
                        s "I-"
                        $ Sabia.face = "pout3"
                        $ Amelia.face = "normalopen"
                        amelia "You wanted informabout about Hal, right?"
                        $ Amelia.face = "brows"
                        "Amelia smirked as she cut Sabia's words off."
                    "Yes.":
                        $ Sabia.face = "normalopen"
                        s "Well, yes-"
                        $ Sabia.face = "normal"
                        "Amelia leaned over the counter, her breasts threatening to spill from their confines as they smooshed against the wet bartop."
                        "She held a finger against Sabia's lips and shook her head."
                        $ Sabia.face = "irritated2"
                        $ Amelia.face = "sadopen"
                        amelia "Uh, uh. I don't think either of us believe that, do we?"
                        $ Amelia.face = "browshappy"
                        amelia "But that's alright, cutie. As long as you wore it, I'm happy! Even if you won't admit why!"
                        $ Amelia.face = "happy"
                        amelia "So! Information about that Hal fellow."
                        $ Amelia.face = "normal"
                $ Sabia.face = "normalopen"
                s "Yeah... do you know where he went?"
                $ Sabia.face = "normal"
                $ Amelia.face = "happy"
                amelia "Well, you're lucky that you know me, Sabia."
                amelia "And you're lucky that I like you so much as well, of course."
                $ Sabia.blush == False
                amelia "I did hear where he went. He was heading south-east out of Avarton. So I assume making for the coast? One of the booze merchants mentioned they saw a guy lingering around not too far. Few miles, maybe?"
                $ Amelia.face = "normal"
                $ Sabia.face = "happy3"
                s "Few miles? That's still pretty close. Thank you so much, Amelia!"
                $ Sabia.face = "normal"
                "Amelia winked."
                $ Amelia.face = "browshappy"
                amelia "Anything for you, Sabia."
                jump avarton_brothel
            else:
                $ A_amelia -= 1
                $ Amelia.face = "angry"
                "Amelia looked over Sabia's attire, frowning."
                amelia "Hmph."
                $ Sabia.face = "irritated2"
                $ Amelia.face = "angryopen"
                amelia "It's a shame you don't wear something more... exciting or cute, you know?"
                $ Sabia.face = "pout2"
                $ Amelia.face = "normalopen"
                amelia "You could definitely pull it off!"
                $ Sabia.face = "normalopen"
                $ Amelia.face = "angry"
                s "I'm sure, but wearing something like that in here isn't exactly... the most enjoyable."
                $ Sabia.face = "normal"
                $ Amelia.face = "normal"
                "Amelia nodded understandingly."
                $ Amelia.face = "normalopen"
                amelia "So! Information about that Hal fellow."
                $ Amelia.face = "normal"
                $ Sabia.face = "normalopen"
                s "Yeah... do you know where he went?"
                $ Sabia.face = "normal"
                $ Amelia.face = "happy"
                amelia "Well, you're lucky that you know me, Sabia."
                $ Amelia.face = "browshappy"
                amelia "And you're lucky that I like you so much as well, of course."
                $ Amelia.face = "normalopen"
                amelia "I did hear where he went. He was heading south-east out of Avarton. So I assume making for the coast? One of the booze merchants mentioned they saw a guy lingering around not too far. Few miles, maybe?"
                $ Sabia.face = "happy3"
                $ Amelia.face = "normal"
                s "Few miles? That's still pretty close. Thank you so much, Amelia!"
                $ Sabia.face = "normal"
                "Amelia winked."
                $ Amelia.face = "browshappy"
                amelia "Anything for you, Sabia."
                jump avarton_brothel

        "Talk to Madame Fennasil." if v10lynn_quest_done == False and v10lynn_quest_amelia == True:
            $ Sabia.face = "normal"
            $ Fennasil.face = "normal"
            show Sabia at left
            show Fennasil at right
            with dissolve
            if v10lynn_quest_madame_cd == True:
                "Fennasil was too busy to take a moment to chat with Sabia."
                scene bg black with dissolve
                jump avarton_brothel
            menu:
                "Ask about Hal." if v10lynn_quest_madame_hal == False:
                    $ v10lynn_quest_madame_cd = True
                    $ v10lynn_quest_madame_hal = True
                    $ Fennasil.face = "happy"
                    madame "Hal? Dear, I'm afraid I don't know who you're talking about!"
                    $ Fennasil.face = "normal"
                    $ Sabia.face = "normalopen"
                    s "Surely you know everyone in Avarton, though?"
                    $ Sabia.face = "normal"
                    "Fennasil pursed her lips, glancing down the hallway where a small bustle was beginning to break out between a patron and one of her girls."
                    $ Fennasil.face = "happy"
                    madame "Everyone that comes through my establishment, most certainly!"
                    madame "Those that don't, I'm less familiar with."
                    madame "I'm afraid I really must attend to this!"
                    hide Fennasil with moveoutright
                    "She was still speaking as she rushed over towards the growing disturbance."
                    $ Sabia.face = "normalopen"
                    s "Well... if I want to ask Fennasil about the others, I will have to come back another day I suppose."
                    jump avarton_brothel
                "Ask about William." if v10lynn_quest_madame_william == False:
                    $ v10lynn_quest_madame_cd = True
                    $ v10lynn_quest_madame_william = True
                    $ Fennasil.face = "angry"
                    madame "Hmph!"
                    $ Sabia.face = "question1"
                    $ Fennasil.face = "normalopen"
                    madame "I do know William - but it is poor practice to relay things heard between the sheets!"
                    $ Sabia.face = "normalopen"
                    $ Fennasil.face = "angry"
                    s "Does that mean... he's been - with you?"
                    $ Sabia.face = "normal"
                    $ Fennasil.face = "normalopen"
                    madame "No, of course not! Don't be silly. Those days are behind me!"
                    $ Sabia.face = "normalopen"
                    $ Fennasil.face = "normal"
                    s "So someone else has relayed things to you from between the sheets?"
                    $ Sabia.face = "irritated2"
                    $ Fennasil.face = "normalopen"
                    madame "Madame's priviledge."
                    $ Fennasil.face = "normal"
                    $ Sabia.face = "normalopen"
                    s "I see."
                    $ Sabia.face = "normal"
                    menu:
                        "Offer 50 lundils." if money >= 50:
                            $ money -= 50
                            $ Sabia.face = "normalopen"
                            s "Would fifty lundils help at all?"
                            $ Sabia.face = "normal"
                            $ Fennasil.face = "happy"
                            madame "Hmm... they might."
                            "Sabia paid Fennasil 50 lundils."
                            $ Fennasil.face = "normal"
                            $ Sabia.face = "normalopen"
                            s "So, what can you tell me?"
                            $ Sabia.face = "irritated2"
                            $ Fennasil.face = "normalopen"
                            madame "I can tell you that he is not as devoted to his wife as his frequent trips to Whitecrest would have you imagine!"
                            $ Fennasil.face = "normal"
                            $ Sabia.face = "normalopen"
                            s "He has a wife in Whitecrest?"
                            $ Sabia.face = "normal"
                            $ Fennasil.face = "normalopen"
                            madame "He does. Quite beautiful, if I'm to believe what I've heard."
                            $ Fennasil.face = "normal"
                            $ Sabia.face = "irritated2"
                            $ Fennasil.face = "normalopen"
                            madame "But... well, some ladies don't do the things that the girls in my establishment are happy to do."
                            madame "I'm afraid that's all I can help you with though. I have business to attend to."
                            hide Fennasil with moveoutright
                            $ Sabia.face = "normalopen"
                            s "I'm not sure if that helps me at all. It seems like William might just... be into things his wife isn't."
                            s "But, frequent trips to Whitecrest..."
                            $ Sabia.face = "irritated2"
                            "Sabia frowned, unsure. She felt she might need more information."
                            jump avarton_brothel
                        "Leave.":
                            $ Sabia.face = "normalopen"
                            s "Alright then, thank you for your time."
                            $ Sabia.face = "normal"
                            hide Fennasil with moveoutright
                            "Fennasil gave a kindly nod before heading off to attend to some business."
                            $ Sabia.face = "normalopen"
                            s "Not sure if this is my guy. Seems like he might just like indulging himself here."
                            s "...in between seeing his wife."
                            $ Sabia.face = "irritated2"
                            "Sabia frowned to herself."
                            $ Sabia.face = "normalopen"
                            s "If he is seeing his wife, that is."
                            $ Sabia.face = "normal"
                            "Sabia felt she might need more information."
                            jump avarton_brothel
                "Ask about Robert." if v10lynn_quest_madame_robert == False:
                    $ v10lynn_quest_madame_cd = True
                    $ v10lynn_quest_madame_robert = True
                    $ Fennasil.face = "angryopen"
                    madame "Robert?"
                    "Fennasil glowered."
                    $ Fennasil.face = "normal"
                    $ Sabia.face = "normalopen"
                    s "I take it that you... don't particularly like him?"
                    $ Sabia.face = "sad1"
                    $ Fennasil.face = "normalopen"
                    madame "I wouldn't particularly mind if he turned up a little less {i}alive{/i}."
                    $ Fennasil.face = "normal"
                    $ Sabia.face = "sad2"
                    s "Why is that?"
                    $ Sabia.face = "sad1"
                    "Fennasil frowned, pursing her lips."
                    $ Fennasil.face = "normalopen"
                    madame "In almost every similar establishment, you will find one or two patrons that like to... {i}collect{/i} information."
                    madame "They worm their way in with some of the girls, and find a way to sink their fangs into them, and keep draining them of useful tidbits and things heard in passing."
                    $ Fennasil.face = "normal"
                    $ Sabia.face = "normalopen"
                    s "And I'm guessing you're not very fond of them doing that, or having things over some of your girls?"
                    $ Sabia.face = "normal"
                    "Fennasil nodded."
                    $ Sabia.face = "normalopen"
                    s "Why not simply ban him?"
                    $ Sabia.face = "normal"
                    $ Fennasil.face = "normalopen"
                    madame "To what end? Whether he comes or not, he'll still get what he wants at this point."
                    $ Fennasil.face = "normal"
                    "Sabia paused for a moment, considering."
                    $ Sabia.face = "normalopen"
                    s "And I'm guessing you'd rather he didn't have any cause to talk."
                    $ Sabia.face = "normal"
                    $ Fennasil.face = "normalopen"
                    madame "Hmph."
                    madame "I think I see one of my girls needing some help with something."
                    hide Fennasil with moveoutright
                    "Fennasil swiftly left Sabia."
                    $ Sabia.face = "normalopen"
                    s "Well... Robert certainly seems like a promising candidate for having information..."
                    $ Sabia.face = "closed4"
                    s "But, it doesn't seem like he really leaves Avarton that much, and his field is... narrower than dealing with mages."
                    $ Sabia.face = "normalopen"
                    s "I would need more information before deciding if this is my target."
                    jump avarton_brothel
                "Ask where Robert is now." if v10lynn_quest_madame_robert == True:
                    "Fennasil pursed her lips."
                    $ Fennasil.face = "normalopen"
                    if v10lynn_robert_location == "quarters":
                        madame "I suspect he is at his quarters. I haven't seen him all day."
                    else:
                        madame "Down in one of the rooms."
                        madame "I suspect he will be here for the rest of the day. Unfortunately."
                    $ Fennasil.face = "normal"
                    $ Sabia.face = "normalopen"
                    s "Thank you, good to know."
                    $ Sabia.face = "normal"
                    "Sabia gave Fennasil a thankful nod before leaving."
                    jump avarton_brothel
                "Tell Madame Fennasil about Robert's demise." if v10lynn_robert_dead == True and v10lynn_robert_dead_madame == False:
                    $ v10lynn_robert_dead_madame = True
                    $ money += 100
                    $ A_fennasil += 2
                    $ Sabia.face = "normalopen"
                    s "Oh, that... annoyance you had that was slithering around here?"
                    $ Sabia.face = "normal"
                    $ Fennasil.face = "browsopen"
                    "Fennasil placed a hand on her hip and raised her eyebrows."
                    $ Fennasil.face = "normalopen"
                    fennasil "Yes?"
                    $ Sabia.face = "happy3"
                    $ Fennasil.face = "happy"
                    s "Not a problem anymore."
                    $ Sabia.face = "normal"
                    fennasil "Really? That's a relief to here! Though I suspect one or two of the girls might be upset to find that they'll not be receiving- ahem."
                    fennasil "That's not your problem. Thanks for that Sabia. I don't have much free cashflow, but I can offer a small thanks!"
                    $ Fennasil.face = "normal"
                    "Sabia received 100 lundils."
                    jump avarton_brothel
                "Go back.":
                    jump avarton_brothel

        "Talk to Rokgrid's contact." if v10lynn_quest == 1 and v10lynn_rokgrid_contact == False:
            $ v10lynn_rokgrid_contact = True
            $ Sabia.face = "normal"
            $ Humansoldier.face = "normal"
            show Sabia at left
            show Humansoldier at right
            with dissolve
            "Sabia spotted Rokgrid's contact drinking at the back, leering seedily at several of the girls walking past as he downed a few gulps of ale at a time."
            "He gave a lazy nod as she sat down opposite him."
            $ Sabia.face = "irritated2"
            soldier "Been a while."
            $ Sabia.face = "normalopen"
            $ Humansoldier.face = "normal"
            s "So, Rokgrid said you have some information about that mage in Whitecrest?"
            soldier "Nah."
            $ Sabia.face = "irritated1"
            s "..."
            $ Sabia.face = "normalopen"
            s "Then why did I come-"
            $ Sabia.face = "irritated1"
            $ Humansoldier.face = "happy"
            soldier "Calm down, calm down. Fuck me, you need to relax a bit."
            soldier "Sure you don't want to have a drink with me?"
            $ Humansoldier.face = "sad"
            $ Sabia.face = "normalopen"
            s "I'm sure."
            $ Sabia.face = "irritated2"
            $ Humansoldier.face = "normal"
            soldier "Anyways, as I was {i}going{/i} to say... I only heard some whispers between a few people, and some between that cute bar wench over there, and the whore that runs this place."
            $ Sabia.face = "normalopen"
            s "Amelia and Fennasil?"
            $ Sabia.face = "irritated2"
            "He shrugged."
            $ Humansoldier.face = "happy"
            $ Sabia.face = "irritated1"
            soldier "Can't say I'm interested in their names."
            $ Humansoldier.face = "normal"
            soldier "But that seems right."
            soldier "Look, all I know is that a couple of the soldiers hanging around Avarton visit or have come from Whitecrest."
            soldier "You'll have to ask around yourself. Rokgrid ain't paying me for this. I've done this out of the kindness of my heart, for an old friend."
            $ Sabia.face = "annoyed1"
            s "I'm sure that's why."
            $ Sabia.face = "irritated2"
            "He glared at Sabia."
            $ Humansoldier.face = "happy"
            $ Sabia.face = "angry2"
            soldier "Well, I said what I have to say. Unless you're gonna get under my table and suck my cock, you should probably head off."
            $ Humansoldier.face = "normal"
            "Sabia glowered at him, before pushing her chair back from the table with a loud screech, and leaving him there."
            hide Humansoldier with dissolve
            $ Sabia.face = "normalopen"
            s "Well, that's not much information. Amelia always seems to know a fair bit about what is going on. I should ask her first."
            jump avarton_brothel

        "Go see The Radiant Dawn with Amelia." if v10amelia_prompt == True and v10amelia_done == False:
            $ Amelia.face = "happy"
            $ Sabia.face = "normal"
            show Sabia at left
            show Amelia at right
            with dissolve
            amelia "Yay! Okay, let me just resolve a couple of things here, and then we will be on our way."
            hide Amelia with moveoutright
            "Sabia took a seat, waiting as Amelia shuffled about the brothel, talking to a few girls here and there. After a few moments she walked back toward Sabia."
            scene bg black with dissolve
            "Nodding to Sabia, the two of them left and headed for the nearby village. It didn't take too long before they were there."
            jump v10town
        "Go back":

            scene bg black with dissolve
            jump avarton_town


label avarton_temple:
    scene bg hcmtemple
    show screen infohud("left")
    if avarton_first_visit_temple == False:
        $ avarton_first_visit_temple = True
        $ Sabia.face = "normal"
        show Sabia at left
        "The smell of dripping animal fat and meat was heavy in the temple as Sabia entered."
        "A group of worshippers were at the base of a fire, the portions of meat dedicated to Relona and her sisters placed reverently aside."
        "Sabia had always thought it a bit odd that the gods accepted the bad cuts of meat, while their worshippers ate the best parts of the animal."
        $ Sabia.face = "normalopen"
        s "Tradition, I suppose."
        $ Sabia.face = "normal"
        "Great pillars, three times as wide as Sabia with an ornate base that held them just above the temple's floor lined the building."
        "Up above, looking down on anyone who entered was a magnificent mosaic. The winged sisters looking down in protection."
    menu:
        "Pray.":
            $ Sabia.face = "normalopen"
            show Sabia at left
            s "Not normally one to pray... but if I'm here I may as well offer my respects."
            $ Sabia.face = "normal"
            "Sabia moved a bit closer to the large figure of Relona in the center, surrounded by her sisters."
            $ Sabia.face = "closed1"
            "She offered a short prayer with eyes closed before leaving quietly."
            jump avarton_temple
        "Offer worship.":
            $ Sabia.face = "normal"
            show Sabia at left
            $ temp = renpy.random.randint(1,3)
            if temp == 1:
                "Sabia approached the large effigy in the temple, and silently said a few short words of worship."
            elif temp == 2:
                if met_amelia == True:
                    $ saw_amelia_temple = True
                    "Sabia spotted Amelia deep in worship, performing some of the simpler rituals that she remembered the commoners doing from her childhood."
                else:
                    "Sabia spotted the bartender from the brothel deep in worship, performing some of the simpler rituals that she remembered the commoners doing from her childhood."
            else:
                "The space around Relona's figure was limited. A large group of young, dark-haired women were crowded about, deep in the midst of rituals and prayer."
                "It was hard to find a spot close to Relona. Sabia offered her prayers where she was, before leaving."
            jump avarton_temple
        "Go back":
            jump avarton_town


label avarton_stables:
    scene bg hcmstables
    show screen infohud("left")
    if avarton_first_visit_stables == False:
        $ avarton_first_visit_stables = True
        $ Sabia.face = "normal"
        show Sabia at left

        "The stable master didn't look up from his chair as Sabia entered. His arms were crossed, his head leaning back and eyes closed."
        sm "Ten lundils a night. Stable 'em yourself, or it costs you ten."
        $ Sabia.face = "normalopen"
        s "I was just looking around."
        $ Sabia.face = "normal"
        sm "Not much point. Got no horses to sell."
        "The stable master peeked through closed eyelids, saw Sabia and sighed. He closed his eyes again, trying to nod back to sleep."
        $ Sabia.face = "normalopen"
        s "Well, alright then..."
















    menu:
        "Go back":
            jump avarton_town


label avarton_market:
    scene bg hcmmarket
    show screen infohud("left")
    if avarton_first_visit_market == False:
        $ avarton_first_visit_market = True
        $ Sabia.face = "normal"
        show Sabia at left
        "Sabia could barely get a step in as she entered the hall."
        "It was filled with people - young, old, men and women; soldiers and civilians."
        "The walls were lined with merchants hawking their wares with voices that had long since given way to a raspy crackle."
        $ Sabia.face = "normalopen"
        s "I'll have to have a look around later, and see if there's anything that will be useful to me."
        $ Sabia.face = "irritated2"
        "Sabia gave a cursory glance around the hall as best she could with how busy it was."
        $ Sabia.face = "normalopen"
        s "Maybe not."
        $ Sabia.face = "normal"
        "It looked like it was mostly every day items. Ornaments for your home, cooking utensils, and other stuff that held no use for Sabia."
    menu:
        "Go back":
            jump avarton_town


label avarton_tsquare:
    scene bg hcmtsquare
    show screen infohud("left")
    if avarton_first_visit_tsquare == False:
        $ avarton_first_visit_tsquare = True
        $ Sabia.face = "normal"
        show Sabia at left
        "People rushed by the fountain, busy with errands and tasks."
        "No one seemed to have the time to stop and enjoy the day; the water was dirtier than the small towns Sabia had visited in Andian's territory anyway."
    menu:
        "Sit for a while.":
            if met_amelia == True and amelia_tsquare_talk == False:
                $ amelia_tsquare_talk = True
                $ Amelia.face = "happy"
                show Amelia at right with moveinright
                amelia "Hey, cutie."
                $ Amelia.face = "normal"
                $ Sabia.face = "normalopen"
                s "Ah, Amelia. Hi."
                $ Sabia.face = "normal"
                "Amelia breathed in deeply, taking a seat next to Sabia on the edge of the fountain."
                $ Sabia.face = "question1"
                $ Amelia.face = "browshappy"
                amelia "It's nice, isn't it?"
                $ Sabia.face = "normalopen"
                $ Amelia.face = "normal"
                s "Hmm?"
                $ Amelia.face = "happy"
                $ Sabia.face = "normal"
                amelia "Sitting here, with Relona so close? It always makes me feel... safe. Content."
                amelia "Do you feel the same?"
                $ Amelia.face = "normal"
                $ Sabia.face = "normalopen"
                s "Well, I suppose a bit. The running water is always relaxing."
                s "I've never been too devout though."
                $ Sabia.face = "normal"
                $ Amelia.face = "normalopen"
                amelia "Ah. Well, I think there's a spot for Relona in everyone, even if they're not as devout as the next."
                $ Amelia.face = "happy"
                amelia "I'll see you around. Don't be a stranger, cutie. It's a nice night when I see you in at work."
                $ Amelia.face = "normal"
                menu:
                    "Sure.":
                        $ Sabia.face = "happy3"
                        s "I'll try and make some time, sure."
                        $ A_amelia += 1
                    "Maybe.":
                        $ Sabia.face = "normal"
                        s "The brothel isn't my scene too much, but maybe..."
                "Amelia gave a smile as Sabia left."
                jump avarton_tsquare
            else:
                "Sabia watched Avarton's folk walk past during their day."
                "Some of them stopped for a few minutes at the fountain, others a bit longer."
                "After a while Sabia left as well."
                jump avarton_tsquare
        "Go back":
            jump avarton_town


label avarton_tavern:
    scene bg hcmtavern
    show screen infohud("left")
    if avarton_first_visit_tavern == False:
        $ avarton_first_visit_tavern = True
        $ Sabia.face = "normal"
        show Sabia at left
        "Sabia wrinkled her nose as she entered the tavern."
        "The din of so many conversations rumbled about the walls. There were a fair few soldiers by the looks of it."
        $ Sabia.face = "irritated1"
        "It also smelled like they needed to clean themselves."
        $ Sabia.face = "closed2"
        s "..."
        $ Sabia.face = "normalopen"
        s "Maybe it's just the tavern."
        $ Sabia.face = "normal"
        "Sabia lifted her feet up and down a few times, grimacing at the sticky squelch they made."
        "Still, she could see over at the bar that they had a large selection of booze, and the place was packed."
        "It would certainly be hard to be overheard in here."

    menu:
        "Grab a drink.":
            $ Sabia.face = "normal"
            show Sabia at left
            "Sabia paid a few lundils and had a drink of ale at the bar."
            "Even though the tavern was packed with civilians and soldiers, she could still pick out a few nearby conversations."
            jump avarton_tavern
        "Go back":
            jump avarton_town


label avarton_houses:
    scene bg hcmhouses
    show screen infohud("left")
    if avarton_first_visit_houses == False:
        $ avarton_first_visit_houses = True
        $ Sabia.face = "normal"
        show Sabia at left
        "A bigger military presence brought with it a more affluent class of people."
        "Wealthier people, with more to risk were more interested in settling somewhere with protection - unlike the outskirt villages that had to make do with skeleton crews and threats of attack."
        "As Sabia strolled through the homes of Avarton's centre, she saw well-tended gardens - some with expensive and exotic plants and fruits."
        "Well-dressed and well-mannered (for the most part), Sabia nodded to herself. This is what she remembered."
        "Of course, her home had been several steps above this - Mother would accept nothing but the best."
        "Still, it was similar enough to have her remembering back fondly."
        $ Sabia.face = "normalopen"
        s "Hmm. I wonder how many dark secrets are floating about these streets, as well?"
        s "I can't imagine there'd be as much as in the capital, but I'm sure there are still some..."
    menu:
        "Roam around.":
            $ Sabia.face = "normal"
            show Sabia at left
            "Sabia spent a little bit walking around the more affluent area of Avarton."
            $ temp = renpy.random.randint(1,3)
            if temp == 1:
                "People hurried this way and that; mostly everyone ignored each other, focusing only on their own tasks or errands."
            else:
                "She overheard a few of the town's inhabitants talking."
                $ temp1 = renpy.random.randint(1,3)
                if temp1 == 1:
                    citizen1 "Did you hear about Lord Andian's wife?"
                    citizen2 "No, what happened?"
                    citizen1 "I heard she was caught with a lover... that wasn't Andian."
                    citizen2 "How the fuck did you hear that? That's false, if I've ever heard a tale before!"
                    "The first citizen grinned, tapping the side of his nose."
                elif temp1 == 2:
                    citizen1 "Supposedly the annexation is meant to finalize soon."
                    citizen2 "Can't happen fast enough. Fucking sick of the bandits and everything else."
                    citizen2 "Maybe if we're part of Lundar, Andian will actually have to lead properly - or someone from Lundar will do it for him."
                    citizen1 "Yeah... hopefully. Though it's been taking a long time..."
                else:
                    citizen1 "You think Barrin's gonna annex as well?"
                    citizen2 "Fuck Barrin, who cares? I never liked Barrin."
            jump avarton_houses
        "Go back":

            jump avarton_town


label avarton_slums:
    scene bg hcmslums
    show screen infohud("left")
    if avarton_first_visit_slums == False:
        $ avarton_first_visit_slums = True
        $ Sabia.face = "normal"
        show Sabia at left
        "Sabia moved out from Avarton's town center. The farther she strayed, the more dilapidated and run down the houses were."
        "Well tended gardens and affluent people gave way to weeds, crumbling buildings and starving people."
        "The children seemed as happy as any child, but Sabia saw worry and concern on the faces of adults."
        "A few homeless people were passed out, leaning against the walls of some of the homes."
        "All in all, it was a fairly common sight in a city, or even town of this size that Sabia had seen many times before."
    menu:
        "Roam around.":
            $ Sabia.face = "normal"
            show Sabia at left
            "Sabia spent a while walking around the edges of Avarton."
            $ temp = renpy.random.randint(1,3)
            if temp == 1:
                "Other than seeing a lot of poor folk and crumbling buildings, nothing much happened."
            else:
                $ temp1 = renpy.random.randint(1,3)
                "She overheard a few of the town's inhabitants talking."
                if temp1 == 1:
                    child "Daddy... when are we going to get dinner again?"
                    citizen1 "Soon sweetie... soon. We just have to wait for the next shipment of food to come in... the last one sold out too quickly."
                    child "That's what you said yesterday Daddy! I'm hungry NOW!"
                elif temp1 == 2:
                    woman "Hey... want some fun? Only five lundils... way cheaper than the brothel..."
                    citizen1 "..."
                    citizen1 "No thanks..."
                else:
                    citizen1 "I don't know how much longer we can keep going... we can barely eat!"
                    citizen2 "Relona will provide for us, if we have faith!"
                    citizen1 "...we go to temple every day, and Relona hasn't given us any food."
                    citizen2 "We just have to keep going. It's a test... we have to have faith in her and her sisters..."
            jump avarton_slums
        "Go back":
            jump avarton_town


label v10town:
    $ Amelia.face = "sadopen"
    $ Sabia.face = "normal"
    pause(3)
    scene bg hcsstsquare
    show Sabia at left
    show Amelia at right
    with dissolve
    "The town seemed a bit in disarray. The ever present slums seemed to extend farther here than the other Whitecrest villages Sabia had visited."
    "But that made sense, the farther you went from the capital, the less well-off it seemed the settlement would be."
    amelia "Oh..."
    $ Sabia.face = "normalopen"
    s "What's wrong?"
    $ Sabia.face = "normal"
    $ Amelia.face = "normalopen"
    amelia "It doesn't seem like there is any Lustrator here!"
    $ Amelia.face = "sadopen"
    amelia "I was so excited... I'm not sure I'd be cheered up even if you stripped right now, Sabia!"
    $ Amelia.face = "normal"
    s "..."
    $ Sabia.face = "normalopen"
    s "Well, I don't think I'm going to strip right here, so it's probably good that you don't need that to be cheered up."
    s "Should we ask around at least?"
    $ Sabia.face = "normal"
    "Amelia gave a nod."
    $ Amelia.face = "happy"
    amelia "Sure, let's do that! Came all this way, might as well ask! I mean, even hearing some first hand stories about a Lustrator is bound to be exciting!"
    $ Amelia.face = "normal"
    "The two of them walked through the small village for a little bit, before deciding to go and find a few people to talk to."
    menu v10town_menu:
        "Keep." if v10amelia_rguard == False or v10amelia_lguard == False:
            scene bg hcsstower with dissolve
            menu v10town_menu_keep:
                "Talk to guard to the right." if v10amelia_rguard == False:
                    $ v10amelia_rguard = True
                    $ Humansoldier.face = "angry"
                    show Sabia at left
                    show Amelia at center
                    show Humansoldier at right
                    with dissolve
                    guard1 "Sorry. Can't go in there. Off-limits."
                    $ Humansoldier.face = "normal"
                    $ Sabia.face = "normalopen"
                    s "Oh, we didn't want to, we were just wanting to ask about that Lustrator that came through."
                    $ Sabia.face = "normal"
                    $ Humansoldier.face = "sad"
                    guard1 "That Lustrator? Well, I was on duty at the time... so I can't tell you much."
                    $ Humansoldier.face = "normal"
                    guard1 "But I can tell you that we haven't had any bandit issues since she came through. And that's fine by me."
                    $ Amelia.face = "sadopen"
                    amelia "Oh... okay."
                    $ Amelia.face = "normal"
                    "Amelia frowned a little bit, before accepting that he didn't much want to talk about it."
                    scene bg hcsstower with dissolve
                    jump v10town_menu_keep

                "Talk to guard to the left." if v10amelia_lguard == False:
                    $ v10amelia_lguard = True
                    show Sabia at center
                    show Amelia at right
                    show Humansoldier at left
                    with dissolve
                    $ Humansoldier.face = "angry"
                    guard2 "Sorry. Can't go in there. Off-limits."
                    $ Humansoldier.face = "normal"
                    $ Sabia.face = "normalopen"
                    s "Oh, we didn't want to, we were just wanting to ask about that Lustrator that came through."
                    $ Sabia.face = "normal"
                    $ Humansoldier.face = "surprised"
                    guard2 "Wow. That's all I can say. Like a force 'o nature."
                    $ Humansoldier.face = "normal"
                    $ Amelia.face = "normalopen"
                    amelia "Whatcha mean? What'd she do to make you say that! Oh, I'm so sad I missed seeing her."
                    $ Amelia.face = "sadopen"
                    amelia "I've never seen one in person..."
                    $ Amelia.face = "normal"
                    $ Sabia.face = "happy2"
                    s "Amelia is very devout, you see."
                    $ Sabia.face = "normal"
                    "The guard nodded."
                    $ Humansoldier.face = "happy"
                    guard2 "Well, she cleansed the town of corruption."
                    $ Sabia.face = "surprised1"
                    $ Amelia.face = "brows"
                    guard2 "It took her only a day to do that. New mayor, new high priest. The works. No bandits."
                    $ Sabia.face = "normalopen"
                    $ Humansoldier.face = "normal"
                    s "All in one day?"
                    $ Sabia.face = "normal"
                    guard2 "Like I said, force 'o nature."
                    guard2 "I saw her fight some of the bandits as well."
                    guard2 "They didn't stand a chance. It was like a sapling in a hurricane..."
                    $ Amelia.face = "happy"
                    amelia "It must have been a sight!"
                    $ Amelia.face = "normal"
                    $ Humansoldier.face = "sad"
                    guard2 "It was... though I admit I didn't quite have the stomach for what that hammer did, and the fire after..."
                    $ Sabia.face = "normalopen"
                    s "What do you mean?"
                    $ Sabia.face = "normal"
                    "The guard shook his head."
                    guard2 "I'd rather not bring it up, sorry."
                    $ Humansoldier.face = "normal"
                    $ Amelia.face = "sadopen"
                    amelia "Wow. She must be quite frightening."
                    $ Amelia.face = "normal"
                    guard2 "As long as you're not corrupt or doing anything like banditing... then you're fine."
                    "He gave a curt nod, as if he had nothing else to say."
                    $ Sabia.face = "happy3"
                    s "Thanks for talking to us!"
                    $ Sabia.face = "irritated2"
                    $ Humansoldier.face = "happy"
                    guard2 "No problem. Not every day I get two beautiful women coming to talk to me on my shift."
                    $ Amelia.face = "happy"
                    amelia "Aww, isn't he cute? Now I almost feel bad leaving!"
                    amelia "But, you know, we can't stay here all day!"
                    $ Amelia.face = "normal"
                    scene bg hcsstower with dissolve
                    jump v10town_menu_keep
                "Go back.":

                    scene bg hcsstsquare with dissolve
                    jump v10town_menu

        "Town Hall." if v10amelia_mayor == False:
            scene bg hcsshouse1 with dissolve
            menu:
                "Talk to Mayor.":
                    $ v10amelia_mayor = True
                    show Sabia at left
                    show Amelia at center
                    show Priscilla at right
                    with dissolve
                    $ Priscilla.face = "normalsmile"
                    mayor "Hello there. I haven't seen you two before!"
                    $ Priscilla.face = "normal"
                    $ Amelia.face = "happy"
                    amelia "No, no! We are from Avarton!"
                    $ Amelia.face = "normal"
                    $ Sabia.face = "normalopen"
                    s "We heard that there was a Lustrator in your town, and Amelia here would have loved to see one."
                    $ Sabia.face = "normal"
                    $ Priscilla.face = "normalopen"
                    mayor "Ah, I'm afraid Rhea has left already."
                    mayor "But the sight of that fire, that's something I will remember forever."
                    $ Priscilla.face = "normal"
                    $ Amelia.face = "normalopen"
                    amelia "Fire?"
                    $ Amelia.face = "normal"
                    "The mayor nodded solemnly."
                    $ Sabia.face = "irritated2"
                    $ Priscilla.face = "normalopen"
                    mayor "It was a blaze that reached into the sky... erupting from the Lustrator's weapon."
                    mayor "The last Mayor and High Priest... their screams could be heard for miles, I'm sure."
                    mayor "They burned with the bandits."
                    $ Priscilla.face = "normal"
                    $ Sabia.face = "normalopen"
                    s "Do you have bandit issues here as well?"
                    $ Sabia.face = "normal"
                    $ Priscilla.face = "normalopen"
                    mayor "No."
                    $ Sabia.face = "irritated2"
                    $ Priscilla.face = "normalsmile"
                    mayor "Not anymore."
                    $ Priscilla.face = "normal"
                    $ Amelia.face = "happy"
                    amelia "Wow, this one Lustrator got rid of all your bandit problems?!"
                    $ Priscilla.face = "normalopen"
                    $ Amelia.face = "normal"
                    mayor "It may have only been one... but that did not matter."
                    $ Priscilla.face = "normal"
                    "The mayor shuddered."
                    $ Priscilla.face = "normalopen"
                    mayor "It's not something I would have liked to see... but I am thankful that at least we no longer have to deal with corrupt leaders in league with bandits."
                    $ Priscilla.face = "normal"
                    $ Sabia.face = "normalopen"
                    $ Amelia.face = "brows"
                    s "I'm starting to see why you were so interested in this Lustrator, Amelia."
                    $ Sabia.face = "normal"
                    $ Amelia.face = "sadopen"
                    amelia "It would have been nice to see such a high servant of Relona and her sisters in person..."
                    $ Amelia.face = "normal"
                    $ Priscilla.face = "normalopen"
                    mayor "I'm not sure you would share that sentiment if you had been here... at least not entirely."
                    mayor "I do hope you enjoy your stay here, but I do have business to attend to. Ever since this position dropped in my lap, I've not had more than two moments peace."
                    $ Priscilla.face = "normal"
                    $ Amelia.face = "happy"
                    amelia "Of course, thanks for the story!"
                    "Amelia bounced forward and wrapped her arms around the surprised Mayor, giving her a hug before they left."
                    $ Amelia.face = "normal"
                    scene bg hcsstsquare with dissolve
                    jump v10town_menu
                "Go back.":

                    scene bg hcsstsquare with dissolve
                    jump v10town_menu

        "Temple." if v10amelia_worshipper == False:
            scene bg hcsstemple with dissolve
            menu:
                "Talk to worshipper.":
                    $ v10amelia_worshipper = True
                    $ Tavernkeep.face = "happy"
                    show Sabia at left
                    show Amelia at center
                    show Tavernkeep at right
                    with dissolve
                    worshipper "Hello! Have you two come to pray at our temple? It has been blessed recently! By The Radiant Dawn herself!"
                    $ Tavernkeep.face = "normal"
                    $ Amelia.face = "happy"
                    amelia "Really?!"
                    amelia "The Radiant Dawn came here and blessed this temple?"
                    $ Amelia.face = "normal"
                    $ Tavernkeep.face = "happy"
                    "The devotee smiled and nodded."
                    worshipper "The town was cleansed, the unrighteous burned and the temple blessed."
                    worshipper "It is a wonderful day!"
                    $ Sabia.face = "irritated2"
                    worshipper "A true blessing to have been able to witness The Radiant Dawn perform such righteous actions... and to see Cro'mors."
                    $ Tavernkeep.face = "normal"
                    $ Sabia.face = "normalopen"
                    s "Cro'mors?"
                    $ Sabia.face = "normal"
                    $ Amelia.face = "happy"
                    amelia "The weapon that The Radiant Dawn uses!"
                    $ Amelia.face = "normal"
                    "The worshipper nodded, smiling."
                    $ Tavernkeep.face = "happy"
                    worshipper "Indeed. To see the fire of Anestra, erupting from Cro'mors... it was a beautiful sight."
                    $ Sabia.face = "normalopen"
                    $ Tavernkeep.face = "normal"
                    s "Should I leave you here for a little bit, Amelia? I know you're quite devout..."
                    $ Sabia.face = "normal"
                    $ Amelia.face = "happy"
                    amelia "You wouldn't mind, Sabia?"
                    $ Amelia.face = "normal"
                    $ Sabia.face = "normalopen"
                    s "I'll manage. I'll wait outside for a little bit."
                    $ Sabia.face = "normal"
                    $ Amelia.face = "browshappy"
                    amelia "Cute {i}and{/i} thoughtful!"
                    $ Amelia.face = "normal"
                    $ Sabia.face = "irritated2"
                    $ Tavernkeep.face = "normalopen"
                    worshipper "You don't wish to join?"
                    $ Tavernkeep.face = "normal"
                    $ Sabia.face = "normalopen"
                    s "I follow Relona and her sisters, but I am not quite as devout as some."
                    $ Sabia.face = "irritated1"
                    "The woman nodded, if a bit curtly."
                    scene bg black with dissolve
                    "Sabia spent a little bit of time outside, until Amelia was finished."
                    scene bg hcsstsquare with dissolve
                    jump v10town_menu
                "Go back.":

                    scene bg hcsstsquare with dissolve
                    jump v10town_menu

        "Market." if v10amelia_merchant == False:
            scene bg hcssmarket with dissolve
            menu:
                "Talk to merchant.":
                    $ v10amelia_merchant = True
                    $ Elliah.face = "normalopen"
                    show Sabia at left
                    show Amelia at center
                    show Elliah at right
                    with dissolve
                    merchant "You looking to buy something? If so, can't help you, sorry."
                    merchant "Still waiting for the first delivery... but once it gets here, at least there won't be any more bandits."
                    $ Elliah.face = "normal"
                    $ Amelia.face = "normalopen"
                    amelia "The Lustrator?"
                    $ Amelia.face = "normal"
                    "The merchant nodded."
                    $ Elliah.face = "normalopen"
                    merchant "Yeah, that's right."
                    $ Elliah.face = "normal"
                    $ Amelia.face = "normalopen"
                    amelia "What was it like seeing her? It's so rare to see a Lustrator. I've never seen on! I got so excited to come here and see The Radiant Dawn... but she was already gone."
                    $ Sabia.face = "happy2"
                    $ Amelia.face = "normal"
                    s "I can vouch for that. Amelia was, in fact, {i}very{/i} excited."
                    $ Sabia.face = "normal"
                    $ Elliah.face = "normalopen"
                    merchant "Look, I ain't gonna lie."
                    merchant "I'm not much one for religion."
                    $ Elliah.face = "happy"
                    merchant "But I can tell you that those bandits getting burned serves them right. No more 'protection' fees to deal with."
                    $ Elliah.face = "normal"
                    $ Sabia.face = "normalopen"
                    s "I take it the protection fees were... not quite that protective."
                    $ Sabia.face = "normal"
                    $ Amelia.face = "normalopen"
                    amelia "And probably quite a high fee?"
                    $ Amelia.face = "normal"
                    "The merchant tapped the side of her nose."
                    $ Elliah.face = "normalopen"
                    merchant "She dragged back what remained of them to show that the task had been done. And I guess to make sure no one wanted to take up their position."
                    $ Sabia.face = "irritated2"
                    merchant "Wasn't much left."
                    $ Elliah.face = "normal"
                    amelia "..."
                    $ Sabia.face = "sad2"
                    $ Amelia.face = "sadopen"
                    amelia "Well... maybe next time I will get to see a Lustrator..."
                    "Amelia gave another pout as they left the merchant."
                    $ Amelia.face = "normal"
                    scene bg hcsstsquare with dissolve
                    jump v10town_menu
                "Go back.":

                    scene bg hcsstsquare with dissolve
                    jump v10town_menu

        "Slums." if v10amelia_children == False:
            scene bg hcsshouse4 with dissolve
            menu:
                "Talk to children.":
                    $ v10amelia_children = True
                    "Sabia and Amelia tried asking the children that were running about what they had seen, but it seemed that they were more interested in re-enacting their own version of the Lustrator's adventures that talking to them."
                    scene bg hcsstsquare with dissolve
                    jump v10town_menu
                "Go back.":
                    scene bg hcsstsquare with dissolve
                    jump v10town_menu


        "Go back to Avarton." if v10amelia_rguard == True and v10amelia_lguard == True and v10amelia_mayor == True and v10amelia_worshipper == True and v10amelia_merchant == True and v10amelia_children == True:
            $ v10amelia_done = True
            $ Sabia.face = "sad3"
            show Sabia at left
            show Amelia at right
            with dissolve
            s "Sorry Amelia... I guess we didn't come fast enough."
            $ Sabia.face = "sad1"
            $ Amelia.face = "normalopen"
            amelia "Well... I guess at least I got to hear a lot of stories."
            amelia "It would have been nice to see The Radiant Dawn and Cro'mors..."
            $ Sabia.face = "sad3"
            $ Amelia.face = "normal"
            s "I'm sure you will get to see a Lustrator one day, Amelia."
            $ Sabia.face = "happy3"
            s "And I'm sure they will be happy to speak to such a devout follower of Relona!"
            $ Sabia.face = "normal"
            $ Amelia.face = "happy"
            amelia "Well, I don't know about that. But one can hope!"
            $ Amelia.face = "normal"
            $ Sabia.face = "normalopen"
            s "Mmm. I am sorry, Amelia."
            $ Sabia.face = "normal"
            $ Amelia.face = "happy"
            amelia "That's okay, Sabia. At least I got to spend some time with my favorite, cutest friend!"
            amelia "Let's head back!"
            scene bg black with dissolve
            "Sabia and Amelia left the town, and made their way back to Avarton, Amelia heading back to her bar in the brothel."
            pause(3)
            jump avarton_town
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
