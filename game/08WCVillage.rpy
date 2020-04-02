



image bg hcsshouse1 = "bg/human city small stables/house1 inside.jpg"
image bg hcsshouse2 = "bg/human city small stables/house2 inside.jpg"
image bg hcsshouse3 = "bg/human city small stables/house3 inside.jpg"
image bg hcsshouse4 = "bg/human city small stables/house4 inside.jpg"
image bg hcssmarket = "bg/human city small stables/market inside.jpg"
image bg hcsstemple = "bg/human city small stables/temple inside.jpg"
image bg hcsstower = "bg/human city small stables/tower inside.jpg"
image bg hcsstsquare = "bg/human city small stables/town square inside.jpg"
image bg hcssstables = "bg/human city small stables/stable inside.jpg"






init -1:

    transform hcs_house1_hover:
        "imagebuttons/human/small/house1 2.png"
        pause 0.25
        "imagebuttons/human/small/house1 3.png"
        pause 0.25
        "imagebuttons/human/small/house1 4.png"
        pause 0.25
        "imagebuttons/human/small/house1 3.png"
        pause 0.25
        repeat
    image animated_hcs_house1_hover:
        contains hcs_house1_hover

    transform hcs_house2_hover:
        "imagebuttons/human/small/house2 2.png"
        pause 0.25
        "imagebuttons/human/small/house2 3.png"
        pause 0.25
        "imagebuttons/human/small/house2 4.png"
        pause 0.25
        "imagebuttons/human/small/house2 3.png"
        pause 0.25
        repeat
    image animated_hcs_house2_hover:
        contains hcs_house2_hover

    transform hcs_house3_hover:
        "imagebuttons/human/small/house3 2.png"
        pause 0.25
        "imagebuttons/human/small/house3 3.png"
        pause 0.25
        "imagebuttons/human/small/house3 4.png"
        pause 0.25
        "imagebuttons/human/small/house3 3.png"
        pause 0.25
        repeat
    image animated_hcs_house3_hover:
        contains hcs_house3_hover

    transform hcs_house4_hover:
        "imagebuttons/human/small/house4 2.png"
        pause 0.25
        "imagebuttons/human/small/house4 3.png"
        pause 0.25
        "imagebuttons/human/small/house4 4.png"
        pause 0.25
        "imagebuttons/human/small/house4 3.png"
        pause 0.25
        repeat
    image animated_hcs_house4_hover:
        contains hcs_house4_hover

    transform hcs_market_hover:
        "imagebuttons/human/small/market 2.png"
        pause 0.25
        "imagebuttons/human/small/market 3.png"
        pause 0.25
        "imagebuttons/human/small/market 4.png"
        pause 0.25
        "imagebuttons/human/small/market 3.png"
        pause 0.25
        repeat
    image animated_hcs_market_hover:
        contains hcs_market_hover

    transform hcs_stable_hover:
        "imagebuttons/human/small/stable 2.png"
        pause 0.25
        "imagebuttons/human/small/stable 3.png"
        pause 0.25
        "imagebuttons/human/small/stable 4.png"
        pause 0.25
        "imagebuttons/human/small/stable 3.png"
        pause 0.25
        repeat
    image animated_hcs_stable_hover:
        contains hcs_stable_hover

    transform hcs_temple_hover:
        "imagebuttons/human/small/temple 2.png"
        pause 0.25
        "imagebuttons/human/small/temple 3.png"
        pause 0.25
        "imagebuttons/human/small/temple 4.png"
        pause 0.25
        "imagebuttons/human/small/temple 3.png"
        pause 0.25
        repeat
    image animated_hcs_temple_hover:
        contains hcs_temple_hover

    transform hcs_tower_hover:
        "imagebuttons/human/small/tower 2.png"
        pause 0.25
        "imagebuttons/human/small/tower 3.png"
        pause 0.25
        "imagebuttons/human/small/tower 4.png"
        pause 0.25
        "imagebuttons/human/small/tower 3.png"
        pause 0.25
        repeat
    image animated_hcs_tower_hover:
        contains hcs_tower_hover

    transform hcs_square_hover:
        "imagebuttons/human/small/town square 2.png"
        pause 0.25
        "imagebuttons/human/small/town square 3.png"
        pause 0.25
        "imagebuttons/human/small/town square 4.png"
        pause 0.25
        "imagebuttons/human/small/town square 3.png"
        pause 0.25
        repeat
    image animated_hcs_square_hover:
        contains hcs_square_hover



screen wcvillagescreen:
    $ renpy.block_rollback()
    default mouse_clicked = False
    add "imagebuttons/human/small/basestables.jpg" xalign 0.0 yalign 0.0
    imagebutton focus_mask True idle "imagebuttons/human/small/house1 1.png" hover "animated_hcs_house1_hover" action [Hide("wcvillagescreen"), Jump("wcvillage_tavern")] pos 145,386 anchor (0.5,0.5)
    imagebutton focus_mask True idle "imagebuttons/human/small/house2 1.png" hover "animated_hcs_house2_hover" action [Hide("wcvillagescreen"), Jump("wcvillage_house2")] pos 953,705 anchor (0.5,0.5)
    imagebutton focus_mask True idle "imagebuttons/human/small/house3 1.png" hover "animated_hcs_house3_hover" action [Hide("wcvillagescreen"), Jump("wcvillage_house3")] pos 190,641 anchor (0.5,0.5)
    imagebutton focus_mask True idle "imagebuttons/human/small/house4 1.png" hover "animated_hcs_house4_hover" action [Hide("wcvillagescreen"), Jump("wcvillage_house4")] pos 753,743 anchor (0.5,0.5)
    imagebutton focus_mask True idle "imagebuttons/human/small/stable 1.png" hover "animated_hcs_stable_hover" action [Hide("wcvillagescreen"), Jump("wcvillage_stables")] pos 948,295 anchor (0.5,0.5)
    imagebutton focus_mask True idle "imagebuttons/human/small/market 1.png" hover "animated_hcs_market_hover" action [Hide("wcvillagescreen"), Jump("wcvillage_market")] pos 912,486 anchor (0.5,0.5)
    imagebutton focus_mask True idle "imagebuttons/human/small/temple 1.png" hover "animated_hcs_temple_hover" action [Hide("wcvillagescreen"), Jump("wcvillage_temple")] pos 700,268 anchor (0.5,0.5)
    imagebutton focus_mask True idle "imagebuttons/human/small/tower 1.png" hover "animated_hcs_tower_hover" action [Hide("wcvillagescreen"), Jump("wcvillage_tower")] pos 365,187 anchor (0.5,0.5)
    imagebutton focus_mask True idle "imagebuttons/human/small/town square 1.png" hover "animated_hcs_square_hover" action [Hide("wcvillagescreen"), Jump("wcvillage_tsquare")] pos 434,489 anchor (0.5,0.5)
    fixed at KeymapTransform([('mousedown_1', SetScreenVariable('mouse_clicked', True)), ('mouseup_1', SetScreenVariable('mouse_clicked', False))]):
        imagebutton idle "imagebuttons/leave_idle.png" hover ("imagebuttons/leave_clicked.png" if mouse_clicked else "imagebuttons/leave_hover.png") xpos 50 ypos 0 focus_mask True action [Hide("wcvillagescreen"), Jump("eastern_frontier_map")]
    use infohud("center")

label wcvillage:
    scene bg black
    $ renpy.choice_for_skipping()
    while True:
        show screen wcvillagescreen
        $ renpy.pause(hard=True)


label wcvillage_tavern:
    scene bg hcsshouse1
    show screen infohud("left")
    if wcvillage_first_visit_tavern == False:
        $ wcvillage_first_visit_tavern = True
        $ Sabia.face = "normalopen"
        show Sabia at left
        s "I can smell the sloshed ale from here."
        $ Sabia.face = "normal"
        "Most settlements had a tavern - a place for the townsfolk to gather after a day of work to relax and let their worries or sorrows drown in a mug."
        "There were the exceptions of course - but this village didn't break the mold."
        $ Sabia.face = "normalopen"
        s "Hey."
        $ Sabia.face = "normal"
        show Tavernkeep at right with moveinright
        "The barkeep stopped wiping down a glass with a dirty cloth and looked up."
        $ Tavernkeep.face = "happy"
        tk "Whoa. We don't get too many pretty faces like that 'round here. I'm usually the prettiest."
        tk "What can I do for you? Whiskey? Ale?"
        $ Tavernkeep.face = "normal"
        $ Sabia.face = "normalopen"
        s "No drinks, thanks."
        $ Sabia.face = "normal"
        $ Tavernkeep.face = "worried"
        tk "Oh..."
        $ Tavernkeep.face = "normal"
        $ Sabia.face = "normalopen"
        s "I'm looking for some merchants."
        $ Sabia.face = "normal"
        $ Tavernkeep.face = "normalopen"
        tk "We got a few of those 'round these parts."
        $ Sabia.face = "normalopen"
        $ Tavernkeep.face = "normal"
        s "Specifically, ones that supply most of the alcohol for Grok og Dar?"
        $ Sabia.face = "normal"
        $ Tavernkeep.face = "normalopen"
        tk "Grok og Dar? I dunno which orc village is which to be honest with you, but you want Reina and Elliah over there. Nice old couple they are."
        $ Tavernkeep.face = "normal"
        "She pointed at a pair of women drinking at one of the far tables."
        $ Sabia.face = "normalopen"
        s "Thanks."
        $ Sabia.face = "normal"
        jump wcvillage_tavern
    else:
        menu:
            "Tavernkeeper.":
                $ Sabia.face = "normal"
                show Sabia at left
                $ Tavernkeep.face = "normalopen"
                show Tavernkeep at right
                tk "What can I do for you?"
                $ Tavernkeep.face = "normal"
                menu:
                    "Chat.":
                        if vsq_done == True and vsq_wcv_tavern_chat == False and wcv_tavernkeep_chat > 0:
                            $ vsq_wcv_tavern_chat = True
                            $ Tavernkeep.face = "happy"
                            tk "Hey - how about the night on the house? Not sure how you managed it."
                            if vsq_solution == "kira":
                                $ Tavernkeep.face = "normalopen"
                                tk "Or if you even had anything to do with it - I find it hard to imagine anyone convincing that... Elf of anything."
                                $ Tavernkeep.face = "happy"
                                tk "But hell, either way business is picking up again and you said you were going to look into it."
                            if vsq_solution == "orcs":
                                $ Tavernkeep.face = "sad"
                                tk "I've tried asking some of the orcs before if they'd escort. They never said yes."
                                $ Tavernkeep.face = "normal"
                                "Sabia shrugged."
                                $ Sabia.face = "normalopen"
                                $ Tavernkeep.face = "sad"
                                s "I guess they never saw it as needed until they stopped getting their drinks."
                                $ Sabia.face = "normal"
                                $ Tavernkeep.face = "happy"
                                tk "Either way, business is picking up again and you're who we have to thank."
                            $ Tavernkeep.face = "sad"
                            tk "Not that all our problems are solved. Andian really needs to step up, in my opinion."
                            $ Tavernkeep.face = "normalopen"
                            tk "But, one thing at a time I guess."
                            $ Tavernkeep.face = "worried"
                            "She sighed, wiping one of the mugs with a rag."
                            $ Tavernkeep.face = "normalopen"
                            tk "Anyway, enjoy. Drinks on me tonight."
                            $ Sabia.face = "happy3"
                            $ Tavernkeep.face = "normal"
                            s "Thanks, I appreciate it."
                            $ Sabia.face = "normal"

                            "Sabia paced herself, and by the time she was finished drinking she was a bit intoxicated, but nothing over the top."
                            jump wcvillage_tavern

                        if wcv_tavernkeep_chat == 0:
                            $ wcv_tavernkeep_chat = 1
                            $ Sabia.face = "normalopen"
                            s "So how's business down this far?"
                            $ Sabia.face = "normal"
                            $ Tavernkeep.face = "worried"
                            "The woman sighed, rubbing her brow."
                            $ Tavernkeep.face = "sad"
                            tk "Not the best lately."
                            tk "Most of my business are those coming through as the last stop before trading with the few orc tribes they deal with."
                            $ Tavernkeep.face = "normal"
                            $ Sabia.face = "normalopen"
                            s "Ah. Bandits."
                            $ Sabia.face = "normal"
                            $ Tavernkeep.face = "sad"
                            tk "Bandits. They're not helping at all. With how small the shipments usually are, most of the merchants have decided they'd rather deal a bit closer to Whitecrest."
                            $ Tavernkeep.face = "normalopen"
                            tk "It's a bit more secure there."
                            $ Tavernkeep.face = "normal"
                            $ Sabia.face = "normalopen"
                            s "Can't imagine that's doing well for the rest of the town either."
                            $ Sabia.face = "normal"
                            $ Tavernkeep.face = "sad"
                            tk "I can't say that it is, no."
                            $ Tavernkeep.face = "normal"
                            $ Sabia.face = "normalopen"
                            s "Shouldn't the Lord of Whitecrest be doing something about that?"
                            $ Sabia.face = "normal"
                            $ Tavernkeep.face = "normalopen"
                            tk "You'd think so. I've heard he talks a big deal and seems to most a genuine sort of fellow."
                            $ Tavernkeep.face = "sad"
                            tk "But it doesn't change the fact that not much is happening to help out on the outskirts here."
                            $ Tavernkeep.face = "normal"
                            $ Sabia.face = "normalopen"
                            s "I've heard about Andian. I wouldn't expect him to not be concerned about it..."
                            $ Sabia.face = "normal"
                            $ Tavernkeep.face = "normalopen"
                            tk "I think you're right, but I'm no noble or Lady."
                            $ Sabia.face = "normalopen"
                            $ Tavernkeep.face = "normal"
                            s "Maybe he's hamstrung by something else, who knows?"
                            $ Sabia.face = "normal"
                            $ Tavernkeep.face = "sad"
                            tk "What's the point of being a lord if you can't do what you want or need?"
                            $ Sabia.face = "normalopen"
                            $ Tavernkeep.face = "normal"
                            s "There's a bit more to it than just doing what you want. There are responsibilities and pressures from other parties and factions."
                            $ Sabia.face = "happy3"
                            s "...I assume."
                            $ Sabia.face = "normal"
                            "The woman shrugged."
                            $ Tavernkeep.face = "sad"
                            tk "Could be. Doesn't change our need for a bit less bandits, though."
                            $ Tavernkeep.face = "normal"
                            $ Sabia.face = "normalopen"
                            s "I'll drink to that."
                            $ Sabia.face = "normal"
                            "They both downed a drink, Sabia a few lundils lighter."
                            $ Sabia.face = "normalopen"
                            s "I'll let you get back to the other few patrons you have here."
                            $ Sabia.face = "normal"
                            $ Tavernkeep.face = "normal"
                            tk "Sure. Feel free to stop by for a chat."
                            $ Tavernkeep.face = "worried"
                            "She barked a wry laugh."
                            $ Sabia.face = "sad1"
                            jump wcvillage_tavern

                        if wcv_tavernkeep_chat == 1:
                            $ temp = renpy.random.randint(1,4)
                            if temp == 1:
                                $ Tavernkeep.face = "happy"
                                tk "Hey Sabia, bit too busy to chat tonight, sorry."
                                $ Sabia.face = "normalopen"
                                $ Tavernkeep.face = "normal"
                                s "Understandable. Glad to see it's busy."
                                $ Sabia.face = "normal"
                                "The tavernkeeper gave her a nod, before heading back to work."
                                jump wcvillage_tavern
                            elif temp == 2:
                                $ Sabia.face = "normalopen"
                                s "How's business, tonight?"
                                $ Sabia.face = "normal"
                                $ Tavernkeep.face = "normalopen"
                                tk "Bit slower than it has been, but still busier than before you showed up."
                                $ Tavernkeep.face = "happy"
                                tk "It'll pick up tomorrow."
                                $ Tavernkeep.face = "normal"
                                $ Sabia.face = "happy2"
                                s "Can't say I mind it being a bit quieter, though I'm sure you'd rather have it busy."
                                $ Sabia.face = "normal"
                                $ Tavernkeep.face = "happy"
                                tk "Sometimes a quiet night is good too, so long as it's in between busy."
                                jump wcvillage_tavern
                            else:
                                if wcv_tavernkeep_chat_booze == False:
                                    $ wcv_tavernkeep_chat = True
                                    $ Sabia.face = "happy2"
                                    s "So how does one end up owning a tavern in a small village like this?"
                                    $ Sabia.face = "normal"
                                    $ Tavernkeep.face = "normalopen"
                                    tk "Hmm. Pretty easily, to be fair."
                                    tk "Used to be a booze merchant. Had some contacts. Was sick of traveling around."
                                    tk "So I decided to set up here. At the time, it was mostly an outpost that had a few traders stop by before heading on."
                                    $ Tavernkeep.face = "sad"
                                    tk "I've lost my contacts over the years, so now I depend on other merchants. But it's still more stable, and less traveling."
                                    $ Tavernkeep.face = "normal"
                                    $ Sabia.face = "normalopen"
                                    s "Hmm, I see. I suppose that makes sense, I've never done any trading, or worked in a place like this."
                                    s "It seems the town has popped up well enough over the years then, from when you started."
                                    $ Sabia.face = "normal"
                                    $ Tavernkeep.face = "normalopen"
                                    tk "Towns tend to do that. S'long as there's a place to stay, warm food, and some drink. People are happy to call that place home."
                                    $ Tavernkeep.face = "normal"
                                    "Sabia nodded."
                                    jump wcvillage_tavern
                                else:
                                    $ Tavernkeep.face = "normalopen"
                                    tk "I've got the time."
                                    $ Tavernkeep.face = "normal"
                                    "Sabia had a chat with the tavern keeper for a little bit."
                                    "She didn't have much of interest to tell Sabia."
                                    jump wcvillage_tavern

                    "Ask about Tijana." if wcv_tavernkeep_tijana == False and wcv_stables_door_locked == True and vsq_gothorse == False:
                        $ wcv_tavernkeep_tijana = True
                        $ Sabia.face = "normalopen"
                        $ Tavernkeep.face = "happy"
                        s "So I tried speaking to Tijana and-"
                        $ Sabia.face = "irritated2"
                        tk "Hmph."
                        tk "Good luck with that."
                        $ Tavernkeep.face = "normal"
                        $ Sabia.face = "normalopen"
                        s "Yeah... she wasn't really the most forthcoming person I've met."
                        $ Sabia.face = "normal"
                        $ Tavernkeep.face = "normalopen"
                        tk "About all she wants to tell you is to get out."
                        $ Sabia.face = "normalopen"
                        $ Tavernkeep.face = "normal"
                        s "How can she run her business if she's doing that?"
                        $ Sabia.face = "normal"
                        $ Tavernkeep.face = "normalopen"
                        tk "Business? She doesn't run a business. She showed up a few years back."
                        tk "Had enough coin to organize a building, and she's been there since. Doesn't talk to anyone if she can help it."
                        $ Tavernkeep.face = "normal"
                        $ Sabia.face = "normalopen"
                        s "I see."
                        s "Well, that's not too helpful..."
                        $ Sabia.face = "normal"
                        $ Tavernkeep.face = "sad"
                        tk "Tell me about it."
                        $ Sabia.face = "irritated2"
                        tk "There have been many times when someone has needed a horse and offered good money to rent, but every time she says no."
                        $ Tavernkeep.face = "normalopen"
                        tk "Gotta get back to work, though."
                        jump wcvillage_tavern

                    "Ask about well-off villager." if wcv_big_house_talk == True and wcv_tavernkeep_priscilla == False:
                        $ wcv_tavernkeep_priscilla = True
                        $ priscilla_name = "{image=system/priscilla.png}"
                        $ met_priscilla = True
                        $ Sabia.face = "normalopen"
                        s "What's the deal with that stuck up woman over there?"
                        $ Sabia.face = "normal"
                        hide Sabia
                        $ Priscilla.face = "normal"
                        show Priscilla at right
                        with dissolve
                        "Sabia jabbed a finger in the direction of the woman."
                        hide Priscilla
                        show Sabia at left
                        with dissolve
                        $ Tavernkeep.face = "normalopen"
                        tk "Oh. That's Priscilla vander Sarallan."
                        $ Sabia.face = "annoyed1"
                        $ Tavernkeep.face = "happy"
                        s "Even her name sounds obnoxiously pretentious."
                        $ Sabia.face = "irritated2"
                        $ Tavernkeep.face = "normalopen"
                        tk "Heh. Yeah, I hear that a fair bit. She used to be married to someone in the aristocracy. Not sure where, up north somewhere."
                        $ Sabia.face = "happy2"
                        $ Tavernkeep.face = "happy"
                        s "So what happened, did her husband realize how much of a mistake he'd made, and let her go?"
                        $ Sabia.face = "normal"
                        "The tavern keeper grinned widely."
                        $ Tavernkeep.face = "normalopen"
                        tk "Yeah. Pretty much, from what we've been able to tell. She came about as far from him as she could manage."
                        tk "She doesn't have nearly as much coin as she did then, but it's still more than most of us here. She likes showing it off when she can."
                        $ Sabia.face = "normalopen"
                        $ Tavernkeep.face = "normal"
                        s "I've noticed. She's a bit stuck up."
                        $ Sabia.face = "normal"
                        "She shrugged."
                        $ Tavernkeep.face = "normalopen"
                        tk "Yeah, but what are you going to do about it? We usually just let her be moody. She doesn't hurt anyone."
                        $ Sabia.face = "normalopen"
                        $ Tavernkeep.face = "normal"
                        s "I guess so."
                        if slavery > freedom:
                            $ Sabia.face = "closed2"
                            s "(...wouldn't mind throwing her in the tents, though. That'd sort out her attitude, I bet.)"
                        jump wcvillage_tavern

            "Approach Reina and Elliah." if met_elliah_reina == False:
                $ met_elliah_reina = True
                $ Sabia.face = "normal"
                $ Reina.face = "normal"
                $ Elliah.face = "normal"
                show Reina at center
                show Elliah at right
                with dissolve
                "The two merchants didn't look anything special to Sabia."
                "Middle aged - or more likely, younger but with an aged look due to their time on the road."
                show Sabia at left with moveinleft
                "Sabia pulled up a seat next to them."
                $ Sabia.face = "happy3"
                s "Hey. You two mind if I take a seat?"
                $ Sabia.face = "normal"
                "They looked at each other, and then back at Sabia."
                $ Reina.face = "normalopen"
                reina "No, that's alright."
                $ Reina.face = "normal"
                $ Elliah.face = "normalopen"
                elliah "But you don't usually pull up a chair at a table with some strangers. At least not older-looking folk like us."
                $ Sabia.face = "normalopen"
                $ Elliah.face = "normal"
                s "I'm here representing Vehlis."
                $ Sabia.face = "irritated2"
                $ Reina.face = "normalopen"
                reina "Vehlis? I'm afraid I don't recognize the name, dear."
                $ Sabia.face = "normalopen"
                $ Reina.face = "happy"
                $ Elliah.face = "happy"
                s "About the shipments of alcohol? To Grok og Dar?"
                $ Sabia.face = "normal"
                reina "Oh! For Jadk? He's a lovely old orc, isn't he? So polite, and always happy!"
                elliah "Why didn't you say you knew Jadk!"
                $ Elliah.face = "normal"
                $ Reina.face = "normal"
                $ Sabia.face = "normalopen"
                s "Well, Jadk's taken over as temporary Warchief in Grok og Dar - and Vehlis is dealing with this shipment."
                $ Sabia.face = "annoyed2"
                $ Reina.face = "happy"
                reina "Yes, the shipments! Of course, of course!"
                $ Sabia.face = "irritated1"
                $ Reina.face = "normalopen"
                reina "I'm afraid we can't help there, dear."
                $ Sabia.face = "normal"
                $ Reina.face = "normal"
                $ Elliah.face = "normalopen"
                elliah "Definitely not. Our last workhorse was unfortunately... taken by some bandits."
                $ Reina.face = "normalopen"
                $ Elliah.face = "normal"
                reina "And of course Elliah and I aren't too fond of the idea of bandits ourselves!"
                $ Sabia.face = "normalopen"
                $ Reina.face = "normal"
                s "I see."
                s "That's understandable. But I need the shipments to continue."
                $ Sabia.face = "normal"
                $ Reina.face = "normalopen"
                reina "Without a horse, and with those bandits around - I just can't see us making the trip dear. Sorry."
                $ Sabia.face = "happy3"
                s "So if I were to organize a work animal and someone to ship it down? Would you let the shipment be taken, then?"
                $ Sabia.face = "normal"
                $ Reina.face = "normalopen"
                reina "Well, possibly... though there is a risk of those bandits. If they steal it, we would be out a lot of money!"
                reina "And I'm not sure where you're going to get a workhorse anywhere nearby..."
                $ Reina.face = "happy"
                $ Elliah.face = "angry"
                reina "Well, there is that young lady in the stables... but I think you would have better luck seeing Elliah here doing gymnastics in the capital in front of the Princess than getting her to help!"
                $ Sabia.face = "irritated2"
                $ Reina.face = "normal"
                $ Elliah.face = "normalopen"
                elliah "And let me tell you young lady! That's not going to happen at all. She's a nasty piece of work, that Tijana. Always so moody and brooding."
                $ Sabia.face = "normalopen"
                $ Elliah.face = "normal"
                s "I'll see what I can do."
                $ Sabia.face = "normal"
                $ Reina.face = "happy"
                reina "Well, you know where we are, dear."
                hide Reina
                hide Elliah
                with dissolve
                $ Sabia.face = "normalopen"
                s "Well, given bandits are an issue, I'm in a good position to look into that. I'll ask around Kira's camp about targets, I suppose."
                $ Sabia.face = "closed2"
                s "I should also go talk to the girl in the stables."
                $ Sabia.face = "normalopen"
                s "I'm sure I can make a plan after getting a bit more information."
                jump wcvillage
            "Chat with patrons.":

                menu:
                    "Ask Elliah and Reina about Tijana." if wcv_stables_door_locked == True and wcv_tijana_at_market == False and vsq_gothorse == False:
                        $ wcv_tijana_at_market = True
                        $ Sabia.face = "normal"
                        $ Reina.face = "normal"
                        $ Elliah.face = "normal"
                        show Reina at center
                        show Elliah at right
                        with dissolve
                        $ Sabia.face = "normalopen"
                        show Sabia at left
                        s "Could you two tell me a bit more about Tijana?"
                        s "It seems hard to get to her. The stables are locked, and won't let me enter. I get quite a resounding 'go away'."
                        $ Sabia.face = "normal"
                        $ Reina.face = "normalopen"
                        reina "A bit more? Oh... hmm... Elliah?"
                        $ Reina.face = "normal"
                        $ Elliah.face = "normalopen"
                        elliah "Well, I'm not all that sure there's much else to tell..."
                        elliah "We tried asking her for a workhorse one time... but she sort of just shoved us out the door!"
                        $ Reina.face = "normalopen"
                        $ Elliah.face = "angry"
                        reina "She was a bit curt, yes."
                        $ Reina.face = "normal"
                        $ Sabia.face = "irritated2"
                        $ Elliah.face = "normalopen"
                        elliah "A bit more than curt, don't you think, dear?"
                        $ Reina.face = "normalopen"
                        $ Elliah.face = "normal"
                        reina "Well, maybe a little..."
                        $ Reina.face = "normal"
                        $ Sabia.face = "normal"
                        $ Elliah.face = "happy"
                        elliah "Thankfully she stays to herself mostly, and in the stables as well!"
                        $ Reina.face = "normalopen"
                        $ Elliah.face = "normal"
                        reina "Sometimes she goes to the markets, of course. There's always a wide berth around her!"
                        $ Reina.face = "normal"
                        "Elliah nodded her agreement."
                        $ Sabia.face = "normalopen"
                        s "Hmm, alright. Thanks for the information."
                        jump wcvillage_tavern

                    "Elliah and Reina." if vsq_done == False and vsq_gothorse == True and vsq_solution == "":
                        $ Sabia.face = "normal"
                        $ Reina.face = "normal"
                        $ Elliah.face = "normal"
                        show Reina at center
                        show Elliah at right
                        show Sabia at left
                        with dissolve
                        $ Reina.face = "normalopen"
                        reina "Oh, hello dear."
                        $ Reina.face = "normal"
                        $ Elliah.face = "normalopen"
                        elliah "Any luck, yet?"
                        $ Sabia.face = "normalopen"
                        $ Elliah.face = "normal"
                        s "Yes, I've managed to convince Tijana to lend me a horse. She didn't make it easy.."
                        $ Sabia.face = "normal"
                        $ Reina.face = "happy"
                        reina "Well... I can imagine that dear!"
                        $ Reina.face = "normal"
                        $ Elliah.face = "normalopen"
                        elliah "Have you organized any safety precautions yet?"
                        $ Sabia.face = "normalopen"
                        $ Elliah.face = "normal"
                        s "Not yet, I still need to do that."
                        $ Sabia.face = "normal"
                        $ Reina.face = "normalopen"
                        reina "If you can do that soon, dear."
                        $ Reina.face = "normal"
                        "Sabia nodded. She would have to either make sure that they were satisfied there would be no bandit issue, or hire some orcs to reassure them."
                        jump wcvillage_tavern

                    "Elliah and Reina: Issues resolved." if vsq_done == False and vsq_gothorse == True and vsq_solution == "kira" and vsq_delivery_done == False:
                        $ Sabia.face = "normal"
                        $ Reina.face = "normal"
                        $ Elliah.face = "normal"
                        show Reina at center
                        show Elliah at right
                        with dissolve
                        "Sabia caught Reina and Elliah sitting down to a mutton dinner. She grabbed a chair and sat with them."
                        $ Reina.face = "happy"
                        reina "Oh, it's you again, dear!"
                        $ Sabia.face = "normalopen"
                        $ Reina.face = "normal"
                        s "I don't want to interrupt your meal too much - I'll get straight to the point."
                        s "I heard that the issues with the bandits and your shipments have been resolved?"
                        $ Sabia.face = "normal"
                        $ Reina.face = "normal"
                        $ Elliah.face = "worried"
                        "The two merchants had a worried, fearful glance at each other before turning back to Sabia."
                        $ Elliah.face = "normalopen"
                        elliah "Uhm... yes. It seems it is resolved, but..."
                        $ Sabia.face = "irritated1"
                        $ Elliah.face = "worried"
                        $ Reina.face = "normalopen"
                        reina "We have to admit, we're just still a bit too worried about bandits... having one of them show up did little to calm our nerves, I'm afraid."
                        $ Reina.face = "normal"
                        $ Elliah.face = "normalopen"
                        elliah "Yes, that's exactly it, dear."
                        $ Sabia.face = "normal"
                        $ Elliah.face = "normal"
                        $ Reina.face = "normalopen"
                        reina "But... we have thought about it, and we're tentatively willing to risk a shipment... if someone else does it."
                        $ Sabia.face = "normalopen"
                        $ Reina.face = "normal"
                        s "Excellent. I can do that... but you won't keep shipments coming?"
                        $ Sabia.face = "normal"
                        $ Elliah.face = "normalopen"
                        elliah "I'm afraid not... at least while those bandits are around..."
                        $ Elliah.face = "normal"
                        "Sabia nodded her understanding."
                        s "Well, I can take this shipment now, at least."
                        $ Reina.face = "normalopen"
                        $ Elliah.face = "worried"
                        reina "Oh... are you sure dear? Will you be fine if bandits attack?"
                        $ Reina.face = "normal"
                        $ Elliah.face = "normalopen"
                        elliah "I'm not sure we should let another young lady like you risk that!"
                        $ Elliah.face = "worried"
                        s "Don't worry. I can handle myself. Most of the bandits around here aren't skilled, and are more than a little malnourished."
                        $ Reina.face = "normalopen"
                        reina "Mmm... if you say so, dear. I suppose you do look a bit warrior-ish!"
                        $ Reina.face = "normal"
                        $ Elliah.face = "normalopen"
                        elliah "Alright, then... we'll organize the shipment on the cart if you bring the horse around."
                        $ Elliah.face = "normal"
                        "Sabia nodded."
                        jump vsq_caravan_delivery

                    "Elliah and Reina: Issues resolved." if vsq_done == False and vsq_gothorse == True and vsq_solution == "orcs" and vsq_delivery_done == False:
                        $ Sabia.face = "normal"
                        $ Reina.face = "normal"
                        $ Elliah.face = "normal"
                        show Reina at center
                        show Elliah at right
                        with dissolve
                        $ Reina.face = "happy"
                        reina "Hello dear! You're back!"
                        $ Reina.face = "normal"
                        s "I am. I think I've solved your problem."
                        $ Elliah.face = "happy"
                        elliah "Truly? How have you done that?"
                        $ Elliah.face = "normal"
                        s "I've got two adept orcs from Grok og Dar that will serve as an escort."
                        s "They're particularly fond of the drink, so they've a vested interest in protecting it."
                        $ Reina.face = "happy"
                        reina "Oh my. I must say, I have not thought of an orc escort before!"
                        $ Reina.face = "smile"
                        $ Elliah.face = "normalopen"
                        elliah "Hmm. No... but still. I'm not sure if Reina and I want to really be taking shipments that far out of Andian's territory..."
                        elliah "Even with two orcs escorting us."
                        $ Elliah.face = "normal"
                        "Reina looked thoughtful, nodding to her partner's words."
                        $ Elliah.face = "worried"
                        s "But... what? I just organized everything for it - and now you're telling me that-"
                        $ Elliah.face = "normalopen"
                        elliah "Reina and I were talking earlier - and we both agreed that we like you. We are happy to have you be in charge of the shipment, and the orcs can escort you."
                        $ Reina.face = "normalopen"
                        $ Elliah.face = "normal"
                        reina "Does that work for you, dear?"
                        $ Reina.face = "normal"
                        s "..."
                        $ Reina.face = "smile"
                        s "Yes, I suppose that will work."
                        $ Reina.face = "happy"
                        reina "Wonderful! Thank you, dear."
                        $ Reina.face = "smile"
                        "Elliah bowed her head a little bit."
                        hide Reina
                        hide Elliah
                        with dissolve
                        s "Well, that's organized."
                        jump vsq_caravan_delivery

                    "Elliah and Reina." if vsq_done == True:
                        $ Sabia.face = "normal"
                        $ Reina.face = "normal"
                        $ Elliah.face = "normal"
                        show Reina at center
                        show Elliah at right
                        with dissolve
                        if elliah_reina_day_counter < 7 and elliah_reina_post_vsq == False:
                            $ elliah_reina_post_vsq = True
                            $ Elliah.face = "happy"
                            elliah "Sabia, hello!"
                            elliah "We do have to thank you again for helping out earlier."
                            $ Elliah.face = "normal"
                            if vsq_solution == "kira":
                                $ Reina.face = "normalopen"
                                reina "I'm still not so sure it was a good idea to let this nice young lady take the shipment, though."
                                $ Elliah.face = "worried"
                                reina "Even if that awful Elf did come in and say she wasn't going to attack anymore... I'm not sure it was right of us to let young Sabia risk that."
                                $ Reina.face = "normal"
                                $ Sabia.face = "normalopen"
                                s "I appreciate the concern, but I'm more capable than you might think."
                                $ Elliah.face = "normal"
                                s "There were no incidents, at any rate."
                                $ Sabia.face = "normal"
                                $ Elliah.face = "normalopen"
                                elliah "I wonder why she might have done that, though? The village had only finished repairing from the last raid just over a month ago..."
                                $ Reina.face = "happy"
                                $ Elliah.face = "normal"
                                reina "Perhaps Andian is finally starting to deal with some of the issues, dear?"
                                $ Reina.face = "smile"
                                $ Elliah.face = "normalopen"
                                elliah "Well, any thing's possible, I suppose..."
                                $ Elliah.face = "happy"
                                elliah "At any rate, we are thankful you did help us, Sabia. We hope to organize something in the future so the shipments can continue."
                                $ Elliah.face = "normal"
                                "Reina nodded."
                                $ Reina.face = "normalopen"
                                reina "I'm afraid we're just not up to the risk ourselves."
                                $ Reina.face = "normal"
                                "Sabia nodded agreeably before taking her leave from the two merchants."
                                jump wcvillage_tavern
                            else:

                                $ Reina.face = "normalopen"
                                reina "I never thought the orcs would agree to help us out..."
                                $ Reina.face = "normal"
                                $ Elliah.face = "normalopen"
                                elliah "But why not, love? The shipments are usually for them, anyway."
                                elliah "We should have considered it earlier."
                                $ Elliah.face = "normal"
                                $ Sabia.face = "happy2"
                                s "Everyone drinks, after all. They'll just be happy to get their mead and ale, I'm sure."
                                $ Sabia.face = "normal"
                                $ Reina.face = "normalopen"
                                reina "I just didn't think they liked dealing with humans at the best of times... I didn't think that they'd want to escort a human!"
                                $ Reina.face = "normal"
                                $ Sabia.face = "normalopen"
                                s "I think you'd be surprised. There are some orcs like that, but there are some that don't mind humans."
                                $ Sabia.face = "happy3"
                                s "And some that like us."
                                $ Sabia.face = "normal"
                                $ Reina.face = "happy"
                                reina "That may be true. That Jadk always seemed pleasant, didn't he, dear?"
                                $ Reina.face = "normal"
                                $ Elliah.face = "happy"
                                elliah "Yes, love, he did."
                                $ Elliah.face = "normal"
                                "Sabia nodded agreeably before taking her leave from the two merchants."
                                jump wcvillage_tavern
                        else:
                            $ Elliah.face = "happy"
                            elliah "Hello!"
                            $ Elliah.face = "normal"
                            $ Reina.face = "happy"
                            reina "Hi, dear."
                            $ Reina.face = "normal"
                            "Sabia sat down with the elderly traders. They had a pleasant chat."
                            jump wcvillage_tavern
                    "Take a seat.":

                        $ temp = renpy.random.randint(1,3)
                        if temp == 1:
                            if wcv_tavern_patron_talk == 0:
                                $ wcv_tavern_patron_talk = 1
                                $ Sabia.face = "normal"
                                show Sabia at left
                                $ Humansoldier.face = "happy"
                                patron "Huh, what's this? Me lucky day? How's it going, darlin'?"
                                $ Sabia.face = "normalopen"
                                s "Just here to grab a drink."
                                $ Sabia.face = "normal"
                                $ Humansoldier.face = "normal"
                                patron "Oh? Too bad."
                                $ Sabia.face = "irritated1"
                                patron "Ain't no whorehouse here, so it's a bit of a dead stop."
                                "Sabia ignored the comments, taking a draught of her ale."
                                $ Humansoldier.face = "angry"
                                "The man grumbled, getting up and leaving."
                                jump wcvillage_tavern
                            else:
                                $ Sabia.face = "irritated1"
                                show Sabia at left
                                "Sabia took a seat in the tavern. The old, lecherous merchant was there."
                                "After a little bit, Sabia got tired of his obvious leers and left early."
                                jump wcvillage_tavern
                        elif temp == 2 and vsq_done == True:
                            $ Sabia.face = "normal"
                            $ Humansoldier.face = "normal"
                            show Sabia at left
                            show Humansoldier at right
                            with dissolve
                            menu:
                                "Keep to yourself.":
                                    "Sabia drank in peace, leaving the guard to himself."
                                    jump wcvillage_tavern
                                "Try talking to him." if wcv_tavern_guard_talk == False:
                                    $ wcv_tavern_guard_talk = True
                                    $ met_roland = True
                                    "Sabia took a seat at the same table, opposite the guard."
                                    $ Sabia.face = "normalopen"
                                    s "How's your night?"
                                    $ Sabia.face = "normal"
                                    "The guard looked up. His glower wasn't there. He shrugged."
                                    guard "S'fine as it can be, I suppose. Would be better if I weren't so fucking tired."
                                    $ Sabia.face = "happy2"
                                    $ Humansoldier.face = "sad"
                                    s "Try having a bit of sleep instead of drinking?"
                                    $ Sabia.face = "irritated2"
                                    guard "Hmph. Funny."
                                    $ Sabia.face = "normalopen"
                                    $ Humansoldier.face = "normal"
                                    s "Just trying to lighten the mood a bit."
                                    $ Sabia.face = "normal"
                                    guard "Bit hard to do that. Maybe if you get get Andian to send a few more soldiers down here."
                                    guard "We're nothing more than a skeleton crew."
                                    $ Sabia.face = "normalopen"
                                    s "Should you really be telling anyone that?"
                                    $ Sabia.face = "normal"
                                    $ Humansoldier.face = "sad"
                                    guard "What's it matter? Everyone knows."
                                    guard "At least there's more people coming through lately though. Makes it a little less boring."
                                    $ Sabia.face = "normalopen"
                                    $ Humansoldier.face = "normal"
                                    s "A village that doesn't see much trade stagnates pretty quickly."
                                    $ Sabia.face = "happy3"
                                    s "I'm glad that it's picking up."
                                    $ Sabia.face = "normalopen"
                                    s "What did you mean about Andian, though? Does he have a shortage of men?"
                                    $ Sabia.face = "normal"
                                    $ Humansoldier.face = "sad"
                                    guard "Honestly? I got no idea."
                                    $ Humansoldier.face = "normal"
                                    guard "All I know is, I'm sure hoping that the Lundar thing goes through. Maybe then we'll finally be able to get enough people to do the job."
                                    $ Sabia.face = "normalopen"
                                    s "I know a little bit about Andian, and I would have been sure he would have done his best to make sure all of his settlements are protected."
                                    $ Humansoldier.face = "sad"
                                    $ Sabia.face = "normal"
                                    "The guard shrugged."
                                    guard "Look, so did I. But here we are, eh?"
                                    $ Humansoldier.face = "happy"
                                    guard "Anyway, you mind if we cut the Andian and work chat? I just want to relax with a pint, and, hopefully, a nice view."
                                    "He grinned at Sabia."
                                    menu:
                                        "Sure.":
                                            $ L_humans += 1
                                            $ Sabia.face = "happy3"
                                            s "Sure, why not? The name's Sabia, by the way."
                                            $ Sabia.face = "normal"
                                            $ Humansoldier.face = "happy"
                                            roland "Roland."
                                            "Sabia spent a few hours having drinks with Roland - his shout."
                                            jump wcvillage_tavern
                                        "I'll leave you to it.":
                                            $ Sabia.face = "normalopen"
                                            $ Humansoldier.face = "sad"
                                            s "Actually I think I'm going to head in. Thanks for the chat, though."
                                            $ Humansoldier.face = "normal"
                                            s "My name's Sabia, by the way."
                                            $ Sabia.face = "normal"
                                            $ Humansoldier.face = "happy"
                                            roland "Roland."
                                            jump wcvillage_tavern
                                "Sit with Roland." if met_roland == True:
                                    "Sabia took a seat next to Roland, who seemed pleased to see her."
                                    "The two spent some time having a drink"
                                    jump wcvillage_tavern
                        else:

                            if wcv_big_house_talk == True:
                                if wcv_tavern_pria_talk == 0:
                                    $ wcv_tavern_pria_talk = 1
                                    $ Sabia.face = "irritated1"
                                    show Sabia at left
                                    show Priscilla at right
                                    with dissolve
                                    $ Priscilla.face = "normalopen"
                                    pria "Oh. It's you. Did someone say you could sit there?"
                                    $ Sabia.face = "angry1"
                                    $ Priscilla.face = "exnormal"
                                    s "It's a public bar."
                                    $ Sabia.face = "irritated1"
                                    $ Priscilla.face = "eyesgrit"
                                    pria "Hmph."
                                    $ Priscilla.face = "eyesopen"
                                    pria "Public or not, one would imagine you might ask first."
                                    $ Priscilla.face = "eyesgrit"
                                    s "..."
                                    $ Sabia.face = "angry1"
                                    s "If it's such a problem for you, I'll get up and-"
                                    $ Sabia.face = "irritated1"
                                    $ Priscilla.face = "eyesopen"
                                    pria "No. Don't bother. I'll leave."
                                    hide Priscilla with moveoutright
                                    "Sabia rolled her eyes."
                                    jump wcvillage_tavern
                                else:
                                    show Sabia at left
                                    "The well-off villager had already spotted Sabia, and was on her way out before Sabia was halfway to the seat."
                                    $ Sabia.face = "normalopen"
                                    s "Hmph. Bit stuck up for living this far out on the edge of human territory."
                                    jump wcvillage_tavern
                            else:
                                show Sabia at left
                                show Priscilla at right
                                with dissolve
                                "Sabia went to take a seat next to a well-dressed woman, with mug in hand."
                                "The woman looked over Sabia with a disparaging glance before getting up and walking off."
                                hide Priscilla with moveoutright
                                "Sabia spent a few hours having a couple of drinks in peace."
                                jump wcvillage_tavern
            "Go back.":

                jump wcvillage


label vsq_caravan_delivery:
    $ vsq_delivery_done = True
    scene bg black with dissolve
    pause(3)
    if vsq_solution == "orcs":
        "Grazzag and Yregh were already waiting just outside of town. Sabia quickly readied everything, and they started their way back to Grok og Dar."
    "Tijana still seemed reticent when Sabia arrived to borrow the horse, but at least she held up her end of the bargain."
    "With the help of Reina and Elliah, Sabia readied the cart and horse before leaving by herself to trek it back to Grok og Dar."
    "Like imagined, the trip was unevently and safe."
    "Elmy - and moreso the orcs - were thrilled to have the new shipment of booze in."
    if vsq_solution == "kira":
        "With the delivery of Reina and Elliah's shipment complete, the next task Sabia had was returning the horse back to Tijana."
    else:
        "With the booze delivered, it seemed impossible to get either of the orcs out of The Silvertusk long enough to help return Tijana's horse."
    scene bg roadcaravan
    $ Sabia.face = "normal"
    show Sabia at left
    with dissolve
    "Without the caravan loaded up with different alcohol, the journey back was faster than the journey to Grok og Dar."
    "Even on the way there though, the animal had proved more than admirable - strong, powerful, and pulling the caravan as if it had been as empty as it was now."
    $ Kira.face = "normalopen"
    show Kira at right with moveinright
    kira "Hmm... my dear Sabia. And what is this?"
    $ Kira.face = "normal"
    "Sabia hadn't heard anything before Kira was in front of her, already asking the question."
    $ Sabia.face = "sad2"
    s "(Shit... how can I play this off? I could say I'm running an errand for a friend... but Kira might ask more. Maybe I could just say I'm fattening up the village for more raids?)"
    menu:
        "Errand for a friend.":
            $ Sabia.face = "normalopen"
            $ Kira.face = "angry"
            s "I have a couple of friends in some villages, and they asked me if I could help them with a job."
            $ Sabia.face = "normal"
            kira "..."
            $ Sabia.face = "sad1"
            $ Kira.face = "angryopen"
            kira "But... Sabia. Your job is with {i}me{/i}."
            kira "I don't... {i}like{/i} it at all when those in my command go off and... hmm. Do their own thing."
            $ Kira.face = "angry"
            $ Sabia.face = "sad3"
            s "I didn't-"
            $ Sabia.face = "sad1"
            $ Kira.face = "normalopen"
            kira "That's not to say I'm... entirely against it."
            kira "Being a wandering bandit... it's about freedom, isn't it, Sabia?"
            $ Kira.face = "normal"
            "Sabia nodded her agreement."
            $ Kira.face = "normalopen"
            kira "...still..."
            kira "Next time you should inform me... so that I don't have to find out from a scout."
            $ Kira.face = "normal"
        "Fattening up the village.":

            $ A_kira += 1
            $ Sabia.face = "normalopen"
            $ Kira.face = "browsbite"
            s "Doing my best to fatten up one of the villages..."
            $ Sabia.face = "normal"
            $ Kira.face = "browsopen"
            kira "Oh? Do tell more, Sabia..."
            $ Sabia.face = "normalopen"
            $ Kira.face = "browsbite"
            s "Well, I figured their value as a raid is much smaller if they aren't trading and have a good supply of useful commodities."
            s "Helping jump-start their dwindling trade is like... hmm. I suppose it's like a farmer, sowing some seeds. "
            $ Kira.face = "normalopen"
            $ Sabia.face = "normal"
            "Kira grinned. A wicked, cruel smirk that was unsettling to Sabia."
            kira "And then they shall be reaped..."
            "Sabia nodded."
            $ Kira.face = "angryopen"
            kira "Still... next time you should include me in the plan..."
            kira "I'm not fond of learning these things from a scout."

    $ Sabia.face = "sad3"
    s "I'll make sure I do that next time."
    $ Sabia.face = "normal"
    $ Kira.face = "normalopen"
    kira "This horse though... what a specimen! Beautiful..."
    $ Kira.face = "normalbite"
    "Kira's spear whistled through the air as she turned it about, driving the point into the ground."
    "She walked about the horse, her hands patting at his muscles, inspecting him."
    $ Sabia.face = "sad2"
    "Sabia could feel the tension in the beast."
    $ Kira.face = "normalopen"
    kira "My...! This is truly a specimen. I don't think I've seen a horse this well built in..."
    $ Kira.face = "normal"
    "Kira pondered."
    $ Sabia.face = "sad1"
    $ Kira.face = "sadopen"
    kira "I was sure my scout had been mistaken... hmm. I almost regret the punishment I gave, now..."
    $ Kira.face = "normalopen"
    kira "Where did you get him?"
    $ Sabia.face = "normalopen"
    $ Kira.face = "normal"
    s "I'm borrowing him from one of the villages."
    $ Sabia.face = "normal"
    "Kira gave another pass over the horse, the beast whinnying nervously."
    $ Sabia.face = "sad2"
    $ Kira.face = "normalopen"
    kira "Take him to camp."
    "Sabia winced. She would have to be delicate."
    $ Kira.face = "angry"
    $ Sabia.face = "normalopen"
    s "The stablemaster who kept this horse... she did not think well of the village - and they're short on beasts of burden."
    s "If we take this... she might not let anyone rent any more, and their trade will be stifled..."
    $ Sabia.face = "normal"
    $ Kira.face = "normalopen"
    kira "A stablemaster... does this woman have more beasts of this caliber? He is... magnificent."
    $ Kira.face = "normalbite"
    "Kira ran her hands over the horse's muscles again in appreciation."
    $ Sabia.face = "normalopen"
    s "Yes, several more."
    $ Sabia.face = "sad2"
    $ Kira.face = "normalopen"
    kira "This horse alone is worth more than what a backwater village has to offer... and you say there are more?"
    kira "Steal them all, bring them to me."
    $ Kira.face = "angry"
    $ Sabia.face = "sad3"
    s "But-"
    $ Sabia.face = "surprised1"
    kira "..."
    $ Kira.face = "angrygrit"
    show Kira behind Sabia at center with move
    "The tip of Kira's spear was pressing against Sabia's skin in a flash."
    $ Kira.face = "angryopen"
    kira "I must admit... my patience for you has grown, my sweet Sabia... but it has its limits."
    $ Sabia.face = "sad2"
    $ Kira.face = "angrygrit"
    "Kira pulled the weapon back."
    $ Kira.face = "angryopen"
    kira "Bring them, or bring... yourself."
    $ Kira.face = "normal"
    show Kira:
        xpos 0.35
    with move
    "Kira took a step forward. She leaned in, her nose brushing Sabia's cheek. She inhaled the scent of Sabia's hair."
    $ Sabia.face = "sad3"
    s "Uh... okay. I'll see what I can do."
    $ Sabia.face = "sad1"
    $ Kira.face = "normalopen"
    kira "Good!"
    $ Kira.face = "normalbite"
    "Kira's mood did an instant reversal. She gave a pleased smiled, wandering off into the forest just off the road."
    hide Kira with moveoutleft
    s "..."
    $ Sabia.face = "normalopen"
    s "Well, that's not ideal..."
    s "If I want to keep in Kira's graces - and I still need the information she has - I suppose I'll have to do it..."
    $ Sabia.face = "normal"
    "Sabia frowned, and spent the rest of the trip back to the village deep in thought."
    scene bg black with dissolve
    pause (1)
    scene bg hcsshouse1
    show Sabia at left
    with dissolve
    "Sabia dropped off the caravan back at the tavern, informing Elliah and Reina and giving them their cut of the payment."
    "She then took the now-unburdened horse back to Tijana."
    scene bg black with dissolve
    pause(0.1)
    scene bg hcssstables
    $ Tijana.face = "normal"
    $ Neve.face = "normal"
    show Neve at center
    show Tijana at right
    show Sabia at left
    with dissolve
    "Tijana was practically on top of Sabia as she returned the horse back to one of the stalls. The redheaded stablemaster said no words as she immediately began to inspect every inch of her horse."
    $ Neve.face = "happy1"
    n "Everything go smoothly, then?"
    $ Sabia.face = "normalopen"
    s "Uh, sort of."
    $ Sabia.face = "normal"
    $ Neve.face = "irritated1"
    "Neve raised an eyebrow in query."
    $ Sabia.face = "normalopen"
    $ Neve.face = "normal"
    s "I'll tell you after."
    $ Sabia.face = "normal"
    "After what seemed like another several minutes, Tijana's inspection came to an apparent close. She gave a curt nod."
    $ Tijana.face = "normalopen"
    tijana "Alright, then."
    $ Tijana.face = "normal"
    "Tijana sunk into a glare. Sabia and Neve left the stables."
    scene bg black with dissolve
    pause (0.1)
    scene bg hcsstsquare
    show Sabia at left
    show Neve at right
    with dissolve
    $ Neve.face = "irritated1"
    n "So, what happened, then?"
    $ Sabia.face = "normalopen"
    $ Neve.face = "sad"
    s "Well, I ran into Kira on the way back."
    $ Sabia.face = "normal"
    n "That can't be good."
    $ Sabia.face = "normalopen"
    $ Neve.face = "irritated1"
    s "No... I managed to convince her that what I was doing would benefit her... but then she said to steal the rest of the horses. That she hasn't seen a horse so magnificent."
    $ Sabia.face = "normal"
    n "Steal from Tijana? I'm not so sure that's a good idea."
    $ Sabia.face = "normalopen"
    $ Neve.face = "normal"
    s "Well, I'm not all that interested in stealing horses either, but as soon as we resolve the issue we could return them?"
    $ Sabia.face = "irritated2"
    $ Neve.face = "sad"
    n "No. That's not what I mean."
    $ Sabia.face = "normalopen"
    $ Neve.face = "normal"
    s "What are you talking about, then?"
    $ Sabia.face = "normal"
    $ Neve.face = "happy1"
    n "While you were gone, Tijana and I ended up having quite a good conversation about some... mutual interests."
    $ Sabia.face = "surprised1"
    $ Neve.face = "smirk1"
    n "Let's put it this way - if I had the choice to fight Kira or Tijana, I'd rather fight Kira."
    $ Sabia.face = "closed2"
    s "..."
    $ Sabia.face = "normalopen"
    $ Neve.face = "irritated2"
    s "You think Tijana is dangerous?"
    $ Sabia.face = "normal"
    n "Very."
    s "..."
    $ Sabia.face = "normalopen"
    $ Neve.face = "normal"
    s "I'm not sure I'm in a position to have a choice."
    $ Sabia.face = "normal"
    "Neve shrugged."
    $ Sabia.face = "normalopen"
    s "We'll see, I suppose."
    $ Sabia.face = "normal"
    $ Neve.face = "happy1"
    n "Perhaps. I'll catch up with you back at camp, or Grok og Dar."
    hide Neve with moveoutright
    $ Sabia.face = "normalopen"
    s "I should let Vehlis know her problem is resolved. At least, for now. She'll have to look at a more permanent solution in the future."
    jump wcvillage


label wcvillage_house2:
    scene bg hcsshouse2
    show screen infohud("left")
    if wcvillage_first_visit_tavern == False:
        $ Sabia.face = "normalopen"
        show Sabia at left
        s "I better head to the tavern first. That's the most likely place to get information that can help me with Vehlis' request."
        s "I can have a look around town after."
        jump wcvillage
    if wcvillage_first_visit_small == False:
        $ Sabia.face = "normal"
        show Sabia at left
        $ wcvillage_first_visit_small = True
        "Like every settlement - orc, human or otherwise - people had to live somewhere."
        "In this village, there were a few rows of small homes that served that purpose."
        "A few children smiled at the newcomer as Sabia walked through, though their parents looked less approving."
    menu:
        "Wander around.":
            $ Sabia.face = "normal"
            show Sabia at left
            if wcv_big_house_talk == True:
                $ Sabia.face = "normalopen"
                s "I wonder why that woman was so stuck up. It doesn't seem like she's that much more prosperous than anyone else in this village."
                $ Sabia.face = "normal"
            if small_blue_house_wander == 0:
                $ small_blue_house_wander = 1
                "A few children ran down the muddy paths, rounding the corner and almost knocking Sabia over."
                "They only giggled as they ran, not even slowing down."
                "Turning to look back at the small house, she saw an idol of Relona above the frame of the door."
                $ Sabia.face = "normalopen"
                s "They are more devout out here, after all."
            else:
                "Sabia narrowly dodged a few playing children as they barreled down the pathway."
                "She shook her head wryly."
            jump wcvillage_house2
        "Go back":

            jump wcvillage


label wcvillage_house3:
    scene bg hcsshouse3
    show screen infohud("left")
    if wcvillage_first_visit_tavern == False:
        $ Sabia.face = "normalopen"
        show Sabia at left
        s "I better head to the tavern first. That's the most likely place to get information that can help me with Vehlis' request."
        s "I can have a look around town after."
        jump wcvillage
    if wcvillage_first_visit_bighouse == False:
        $ wcvillage_first_visit_bighouse = True
        $ Sabia.face = "normalopen"
        show Sabia at left
        s "Hmm. Always at least one, isn't there?"
        $ Sabia.face = "normal"
        "Every village, town or city always had at least one person or family who had to have something bigger, better than the rest."
        "Whether to show off their wealth, or to demonstrate their power or any other reason - it was almost a universal constant."
        "Out here in the fringes of human territory though, it was little more than a larger house than the rest of the town had."
        $ Sabia.face = "normalopen"
        s "Maybe I could introduce myself later. Sometimes those sorts of people like to make sure they know what's going on."
        $ Sabia.face = "normal"
    menu:
        "Talk to someone." if wcv_big_house_talk == False:
            $ wcv_big_house_talk = True
            $ Sabia.face = "normalopen"
            show Sabia at left
            s "Hello there!"
            $ Sabia.face = "normal"
            "Sabia called out to one of the villagers she was walking past."
            "She paused for a moment, looking like she was debating whether to keep walking or not before she stopped."
            $ Priscilla.face = "eyesopen"
            show Priscilla at right with dissolve
            woman "Yes?"
            $ Priscilla.face = "normal"
            $ Sabia.face = "irritated2"
            "The woman looked over Sabia disapprovingly."
            if Sabia.armor == Orcslavearmor:
                $ Sabia.face = "irritated1"
                $ Priscilla.face = "exopen"
                woman "I'm afraid we don't have any brothels here. You'll have to head to Avarton for work."
                $ Sabia.face = "normalopen"
                $ Priscilla.face = "eyesnormal"
                s "I'm - what? I'm not a whore."
                $ Sabia.face = "normal"
                $ Priscilla.face = "eyesopen"
                woman "You could have fooled me with those clothes."
            elif Sabia.armor == Rags:
                woman "..."
                $ Sabia.face = "irritated1"
                $ Priscilla.face = "eyesopen"
                woman "I think you'll find some of... your people living over there."
                $ Priscilla.face = "eyesnormal"
                "The woman waved her hand toward the less ostentatious homes."
                $ Sabia.face = "irritated2"
                $ Priscilla.face = "eyesopen"
                woman "At least {i}try{/i} wearing something presentable if you're going to talk to me."
            woman "What do you want?"
            $ Priscilla.face = "normal"
            menu:
                "Don't worry about it.":
                    $ Sabia.face = "normalopen"
                    s "Never mind, don't worry."
                    $ Priscilla.face = "exfrown"
                    s "I can see you're not in the mood to talk."
                    jump wcvillage_house3
                "Ask about village.":
                    $ Sabia.face = "normalopen"
                    $ Priscilla.face = "exfrown"
                    s "I was just wondering what you could tell me about the village. This is my first time here."
                    $ Priscilla.face = "normal"
                    $ Sabia.face = "normal"
                    "The woman gave Sabia a flat stare."
                    $ Sabia.face = "irritated2"
                    $ Priscilla.face = "normalopen"
                    pria "It's a village."
                    pria "What do you think I could tell you about it? People live here. Sometimes merchants come through. Sometimes we get hit by bandits."
                    $ Priscilla.face = "eyesopen"
                    pria "Now if you don't mind, I have things to do."
                    hide Priscilla with moveoutright
                    $ Sabia.face = "normalopen"
                    s "I suppose it's not like I'm used to well-off people that are a bit full of themselves."
                    jump wcvillage_house3

        "Ask Priscilla about Tijana." if met_priscilla == True and wcv_stables_door_locked == True and wcv_tijana_at_market == False and vsq_gothorse == False and A_priscilla >= 0:
            $ Sabia.face = "normal"
            $ Priscilla.face = "eyesopen"
            show Sabia at left
            show Priscilla at right
            pria "Ex{i}cuse{/i} me? Can't you see I'm trying to attend to my own issues? What do you want?"
            $ Sabia.face = "normalopen"
            $ Priscilla.face = "exfrown"
            s "Uh, you're just standing around..."
            $ Sabia.face = "normal"
            $ Priscilla.face = "eyesopen"
            pria "Hmph. Someone like you {i}would{/i} think that, wouldn't you?"
            $ Sabia.face = "irritated1"
            $ Priscilla.face = "normal"
            "Sabia opened her mouth to speak and caught herself short, shaking her head slightly to herself in surprised disbelief."
            $ Sabia.face = "annoyed1"
            $ Priscilla.face = "exfrown"
            s "Whatever. Look, do you know anything about Tijana or not?"
            $ Sabia.face = "normal"
            s "(I could also appeal to her sense of importance... or maybe call her out on being such a stuck-up bitch...)"
            menu:
                "Call her out.":
                    $ Sabia.face = "happy2"
                    $ Priscilla.face = "eyesgrit"
                    s "Since it seems like you're a stuck-up bitch, like Tijana, I thought you two might be friends."
                    $ A_priscilla -= 3
                    $ Sabia.face = "normal"
                    $ Priscilla.face = "eyesopen"
                    pria "EXCUSE ME?"
                    pria "How dare you!"
                    pria "Did your mother not teach you any manners?"
                    $ Priscilla.face = "eyesnormal"
                    $ Sabia.face = "annoyed1"
                    s "You're one to talk."
                    $ Sabia.face = "normal"
                    $ Priscilla.face = "eyesopen"
                    pria "I have nothing more to say. Get off my property."
                    $ Priscilla.face = "eyesnormal"
                    $ Sabia.face = "normalopen"
                    s "Gladly."
                    jump wcvillage
                "Appeal to sense of importance.":
                    $ wcv_tijana_at_market = True
                    $ A_priscilla += 2
                    $ Sabia.face = "normalopen"
                    $ Priscilla.face = "pleasant"
                    s "It just seemed like you're fairly well-off and important here, I thought you might know more than the average inhabitant."
                    $ Sabia.face = "normal"
                    pria "Hmm..."
                    $ Priscilla.face = "normalopen"
                    pria "Well, it's true that I do happen to know a fair bit about everyone."
                    $ Sabia.face = "annoyed2"
                    $ Priscilla.face = "normalsmile"
                    pria "And I {i}am{/i} rather important!"
                    $ Sabia.face = "normal"
                    $ Priscilla.face = "pleasant"
                    "She said it as smugly as an orc after a tent-girl."
                    $ Sabia.face = "normalopen"
                    s "So, can you tell me anything about Tijana, then?"
                    $ Sabia.face = "irritated2"
                    $ Priscilla.face = "normalopen"
                    pria "No."
                    $ Sabia.face = "normalopen"
                    $ Priscilla.face = "normal"
                    s "But-"
                    $ Sabia.face = "irritated1"
                    s "..."
                    $ Priscilla.face = "normalopen"
                    pria "Well, she doesn't talk to me. And she doesn't talk to anyone else really. She goes to the market for supplies - rarely - but that's about it."
                    $ Priscilla.face = "eyesopen"
                    pria "Now, if you don't mind - I have important things to attend to."
                    jump wcvillage_house3
        "Wander around.":

            $ Sabia.face = "normal"
            show Sabia at left
            "Sabia spent a little bit wandering through the larger set of homes."
            if wcv_big_house_wander == False:
                $ wcv_big_house_wander = True
                "It was clear that the lack of business wasn't affecting them as much as the rest of the village."
                "They seemed much more carefree and relaxed, though Sabia knew that they'd start feeling it as well, if things did not improve."
            jump wcvillage_house3
        "Go back":

            jump wcvillage


label wcvillage_house4:
    scene bg hcsshouse4
    show screen infohud("left")
    if wcvillage_first_visit_tavern == False:
        $ Sabia.face = "normalopen"
        show Sabia at left
        s "I better head to the tavern first. That's the most likely place to get information that can help me with Vehlis' request."
        s "I can have a look around town after."
        jump wcvillage
    if wcvillage_first_visit_small == False:
        $ Sabia.face = "normal"
        show Sabia at left
        $ wcvillage_first_visit_small = True
        "Like every settlement - orc, human or otherwise - people had to live somewhere."
        "In this village, there were a few rows of small homes that served that purpose."
        "A few children smiled at the newcomer as Sabia walked through, though their parents looked less approving."
    menu:
        "Wander around.":
            $ Sabia.face = "normal"
            show Sabia at left
            if wcv_big_house_talk == True:
                $ Sabia.face = "normalopen"
                s "I wonder why that woman was so stuck up. It doesn't seem like she's that much more prosperous than anyone else in this village."
                $ Sabia.face = "normal"
            if small_yellow_house_wander == 0:
                $ small_yellow_house_wander = 1
                "An elderly man sat on the porch of one of the houses. The wood overhead had seen better days."
                "Not affluent by any means, but the home seemed in good standing for village on the outskirts."
                "The man gave Sabia a grin as she passed, and she returned with a nod."
            else:
                "Sabia gave the old man a nod. She could see some other folk through the window."
                "She left them to their day."
            jump wcvillage_house2
        "Go back":
            jump wcvillage


label wcvillage_stables:
    scene bg hcssstables
    show screen infohud("left")
    if wcvillage_first_visit_tavern == False:
        $ Sabia.face = "normalopen"
        show Sabia at left
        s "I better head to the tavern first. That's the most likely place to get information that can help me with Vehlis' request."
        s "I can have a look around town after."
        jump wcvillage
    if met_elliah_reina == False or (met_elliah_reina == True and wcv_tijana_market == False) or wcv_herb_quest < 4:
        $ wcv_stables_door_locked = True
        "The door to the stables was clearly locked."
        "Knocking on the door only earned her a few gruff words of 'go away, closed!'"
        if wcv_herb_quest > 0:
            "Sabia could hear Tijana's audible frustration from outside the locked door."
            s "It's probably better if I keep clear of her if I don't have the herbs she needs."
        jump wcvillage

    elif wcvillage_first_visit_stables == True:
        $ Sabia.face = "normal"
        $ Tijana.face = "normal"
        show Sabia at left
        show Tijana at right
        with dissolve
        "Tijana gave Sabia a curt nod, but still seemed far from interested in talking."
        jump wcvillage
    else:
        menu:
            "Go back":
                jump wcvillage


label wcvillage_market:
    scene bg hcssmarket
    show screen infohud("left")
    if wcvillage_first_visit_tavern == False:
        $ Sabia.face = "normalopen"
        show Sabia at left
        s "I better head to the tavern first. That's the most likely place to get information that can help me with Vehlis' request."
        s "I can have a look around town after."
        jump wcvillage
    if wcvillage_first_visit_market == False:
        $ wcvillage_first_visit_market = True
        show Sabia at left
        "Entering the town's artisan hall was oddly almost the same as Grok og Dar's trading hall."
        "People were bartering, haggling - and most of all - yelling at each other, trying to get the best price possible."
        "Still, the items and inventory they had were distinctly different from Grok og Dar, and much more familiar to Sabia."
        "It might be worth having a closer look around and seeing what was available."
        jump wcvillage
    elif wcvillage_first_visit_market == True and wcvillage_market == 0:
        $ wcvillage_market = 1
        $ Sabia.face = "normalopen"
        show Sabia at left
        s "I can definitely tell the impact that Kira has had on this village by coming in here..."
        $ Sabia.face = "normal"
        "Sabia frowned a little bit."
        "It should have been busier even in a smaller village like this, and especially one that serves as the last stop before destinations for minor merchants."
        "Instead of every inch being packed with vendors and prospective buyers, it was almost empty."
        "A blacksmith with a half-bare table and an unfired forge was in the corner, dozing on his seat."
        "There was a butcher as well, though her wares were as sparse as the blacksmith's."
    elif wcvillage_market == 1 and vsq_done == True:
        $ wcvillage_market = 2
        $ Sabia.face = "normalopen"
        show Sabia at left
        "The small hall was abuzz with much more life."
        if vsq_solution == "kira":
            "With the threat of Kira and her bandits not quite lifted, but at least abated, merchants had begun travelling to and from the village again."
        else:
            "Sabia had heard that the orcs had rather enjoyed the job, and expanded out a little bit; they provided an escort for other travelling merchants as well."
        "The result was that the small village was beginning to thrive once more."
        "A few more pople were milling about. Some selling, some buying. The blacksmith and butcher seemed much busier than before."

    if wcv_tijana_at_market == True and wcv_tijana_market == False:
        jump wcvillage_market_tijana

    menu:
        "Apothecary.":
            $ Sabia.face = "normal"
            $ Apothecary.face = "normal"
            show Apothecary at right
            show Sabia at left
            ap "Hey there. Can I interest you in anything?"
            if wcv_tijana_market == True and wcv_herb_quest_done == False:
                menu:
                    "Tijana." if wcv_herb_quest == 0:
                        $ wcv_herb_quest = 1
                        $ Sabia.face = "normalopen"
                        s "I heard you arguing with Tijana about something earlier."
                        $ Sabia.face = "normal"
                        $ Apothecary.face = "normalopen"
                        ap "Yeah? What's it to you?"
                        $ Apothecary.face = "normal"
                        $ Sabia.face = "normalopen"
                        s "What was she after?"
                        $ Sabia.face = "normal"
                        $ Apothecary.face = "normalopen"
                        ap "Some medicinal herbs for her horse. Apparently he's dying."
                        $ Apothecary.face = "sad"
                        "The apothecary looked Sabia up and down."
                        $ Apothecary.face = "normalopen"
                        ap "What, you want it so you can go give it to her?"
                        $ Sabia.face = "irritated2"
                        $ Apothecary.face = "angryopen"
                        ap "Not a chance. She's a bitch, and I hope she chokes on her misfortune. She's dug the grave herself."
                        $ Sabia.face = "normalopen"
                        $ Apothecary.face = "angry"
                        s "I need to use one of her horses. Maybe she might be more forthcoming with help if I get those herbs for her."
                        $ Sabia.face = "normal"
                        $ Apothecary.face = "normalopen"
                        ap "Pff. You'd think that, wouldn't you? But she'd probably just kick your ass on the way out."
                        $ Sabia.face = "normalopen"
                        $ Apothecary.face = "normal"
                        s "Well, can I purchase them and try?"
                        $ Sabia.face = "normal"
                        $ Apothecary.face = "normalopen"
                        ap "Absolutely not. Like I said, she's given me and others more than enough trouble with her selfish ways."
                        ap "She's been in this village for years - and you know how often she's helped anyone? Or anyone has been able to make use of her horses?"
                        $ Apothecary.face = "angryopen"
                        $ Sabia.face = "irritated1"
                        ap "Not once."
                        $ Apothecary.face = "sad"
                        $ Sabia.face = "normalopen"
                        s "But I need it to help out someone in the village... Elliah and Reina can't undertake any business if they don't have a workhorse to carry their caravan shipments."
                        $ Sabia.face = "normal"
                        $ Apothecary.face = "sadopen"
                        ap "Hmm."
                        $ Sabia.face = "normalopen"
                        $ Apothecary.face = "sad"
                        s "They seem very friendly. I can't imagine anyone in town wanting to impact them negatively?"
                        $ Sabia.face = "normal"
                        $ Apothecary.face = "sadopen"
                        ap "Well..."
                        ap "I do like Elliah and Reina.... they usually will pick up some extra small stuff for us in the markets, if they can..."
                        $ Apothecary.face = "sad"
                        $ Sabia.face = "irritated1"
                        "The apothecary groaned, rubbing her chin."
                        $ Apothecary.face = "angryopen"
                        ap "But still... it grates at me that I would be giving in to Tijana - especially after that shouting match we had."
                        $ Sabia.face = "normalopen"
                        $ Apothecary.face = "normal"
                        s "Well, what if I just say I stole it, or tricked you? That way she won't know."
                        $ Sabia.face = "normal"
                        $ Apothecary.face = "normalopen"
                        ap "I mean... I suppose I'm not entirely against that."
                        $ Sabia.face = "irritated1"
                        ap "Look. I'll think about it. Come back tomorrow."
                        $ Apothecary.face = "normal"
                        $ Sabia.face = "angry1"
                        s "What if the horse gets too sick?"
                        $ Sabia.face = "irritated1"
                        $ Apothecary.face = "normalopen"
                        ap "As much as I hate the reclusive bitch, I have to admit she knows, and loves those horses. There's no way she would let them get more sick than needed before swallowing any pride and trying to get a remedy."
                        ap "Any symptoms would have just started today, I would bet."
                        $ Apothecary.face = "normal"
                        s "..."
                        $ Sabia.face = "normalopen"
                        s "Alright. I'll be back tomorrow."
                        jump wcvillage_market

                    "Tijana." if wcv_herb_quest == 2:
                        $ wcv_herb_quest = 3
                        $ Apothecary.face = "normalopen"
                        ap "You're back. Alright, fine. I talked to Elliah and Reina, and I've decided I'll give you the damn herbs. Elliah already paid."
                        $ Apothecary.face = "angryopen"
                        ap "But I swear to Relona, don't let it be known that I went out of my way to help Tijana."
                        $ Sabia.face = "normalopen"
                        $ Apothecary.face = "angry"
                        s "But, surely she might be more pleasant to deal with if she knew-"
                        $ Sabia.face = "irritated1"
                        $ Apothecary.face = "angryopen"
                        ap "Look. I'm asking one thing. Do you want the fucking herbs or not?"
                        $ Sabia.face = "normalopen"
                        $ Apothecary.face = "angry"
                        s "Yes, I want them."
                        $ Sabia.face = "normal"
                        $ Apothecary.face = "normalopen"
                        ap "Fine. Here."
                        $ Apothecary.face = "normal"
                        "Sabia received the medicinal herbs."
                        $ Sabia.face = "angry2"
                        $ Apothecary.face = "normalopen"
                        ap "And look. I didn't let on to Tijana, but I don't have everything she needs."
                        $ Sabia.face = "angry1"
                        $ Apothecary.face = "normal"
                        s "What?! You're just telling me this {i}now{/i}?!"
                        $ Sabia.face = "angry2"
                        "She shrugged."
                        $ Apothecary.face = "normalopen"
                        ap "Truth be told I wasn't planning on handing them over, until I talked to Elliah and Reina."
                        $ Sabia.face = "irritated1"
                        ap "If you want to get in Tijana's good books, you'll need some obscure herb as well. Grows on the coast. Good luck getting it though, it's in the middle of Vegardan lands."
                        ap "It's called rotteral."
                        $ Apothecary.face = "normal"
                        s "..."
                        $ Sabia.face = "closed2"
                        $ Apothecary.face = "angryopen"
                        ap "What? I gave you what you asked for. It's not my fault you didn't know what you needed."
                        $ Sabia.face = "normalopen"
                        $ Apothecary.face = "normal"
                        s "Thanks, I guess."
                        $ Sabia.face = "irritated1"
                        $ Apothecary.face = "normalopen"
                        ap "You're welcome. Now move on, I have business to conduct."

                        $ Sabia.face = "normalopen"
                        s "Well... thankfully I happen to know two Vegardans. I'll try asking Neve. I don't want to be in any more debt to Kira than possible."
                        jump wcvillage_market
                    "Leave.":

                        "Sabia spotted a myriad of bottles and oils, but nothing that really caught her eye."
                        jump wcvillage_market
            else:

                "Sabia spotted a myriad of bottles and oils, but nothing that really caught her eye."
                jump wcvillage_market
        "Blacksmith.":

            "Sabia had a look over the blacksmith's wares. No weapons, nothing of use to her."
            "The blacksmith looked apologetic and suggested another time he might have more useful items."








            jump wcvillage_market
        "Butcher.":
            "The butcher seemed no more well supplied than any of the other stalls in the market."
            "Possibly even less. A few {i}very{/i} aged pieces of meat, and some other fresher cuts with some flies buzzing around dissuaded Sabia from any purchases."
            "Maybe another time."












            jump wcvillage_market
        "Leave.":
            jump wcvillage


label wcvillage_market_tijana:
    $ wcv_tijana_market = True
    $ Sabia.face = "normal"
    show Sabia at left
    "Entering the Market Hall, Sabia could see the red hair of Tijana. Her raised voice filled the market hall."
    hide Sabia
    show Tijana at center
    show Apothecary at right
    with dissolve
    $ Tijana.face = "angryopen"
    $ Apothecary.face = "angry"
    tijana "Are you fucking serious?!"
    $ Tijana.face = "angrygrit"
    $ Apothecary.face = "angryopen"
    ap "Of course I am."
    $ Apothecary.face = "normal"
    $ Tijana.face = "angryopen"
    tijana "You're going to refuse service?"
    $ Tijana.face = "angrygrit"
    $ Apothecary.face = "happy"
    ap "I'm surprised you need to ask if that's what I'm doing. You seem so familiar with the concept."
    $ Tijana.face = "angryopen"
    $ Apothecary.face = "angry"
    tijana "My horse {i}needs{/i} that mix. It's the only thing to deal with that sickness."
    $ Tijana.face = "angrygrit"
    $ Apothecary.face = "angryopen"
    ap "I know. I {i}am{/i} an apothecary, you know."
    $ Apothecary.face = "angry"
    "Sabia held her breath. It looked like Tijana was going to knock the apothecary's head off."
    show Sabia at left with moveinleft
    "Moving closer, she could spot the tightness of Tijana's fist, and the the short breaths of anger."
    $ Apothecary.face = "angryopen"
    ap "What? You're going to hit me, with everyone here watching?"
    ap "Remember that last time I came to you? Or any other time someone else did?"
    $ Apothecary.face = "angry"
    "Tijana did not say a word. She just stood there, fuming."
    $ Tijana.face = "angryopen"
    $ Apothecary.face = "angryopen"
    ap "Yeah. You told everyone to get lost."
    $ Tijana.face = "angrygrit"
    ap "So. Get lost."
    $ Apothecary.face = "angry"
    call shake ("h")
    "Tijana's nostrils flared, and she kicked one of the displays over."
    "Bottles smashed, oils and concoctions spilled."
    $ Apothecary.face = "angryopen"
    ap "Well fuck me, I really want to help you now!"
    hide Tijana with moveoutleft
    $ Apothecary.face = "angry"
    "Tijana turned around and stormed off. She knocked into Sabia as she did so, and Sabia caught a hint of a tear in the corner of the woman's eye."
    jump wcvillage


label wcvillage_temple:
    scene bg hcsstemple
    show screen infohud("left")
    if wcvillage_first_visit_tavern == False:
        $ Sabia.face = "normalopen"
        show Sabia at left
        s "I better head to the tavern first. That's the most likely place to get information that can help me with Vehlis' request."
        s "I can have a look around town after."
        jump wcvillage
    if wcvillage_first_visit_temple == False:
        $ wcvillage_first_visit_temple = True
        $ Sabia.face = "normal"
        show Sabia at left
        "Several groups of praying and worshiping people milled about the large temple."
        "Sabia had noted over the years that the smaller villages on the outskirts always had more faith than those that lived in a larger city."
        "The fire at the base of Relona's impressive statue was not burning."
        "But Sabia could spot a few still-glowing embers amongst the ashen wood, along with the glistening coat of animal fat from offerings."
        "She made her way to the base of Relona's statue, and offered her own small prayer before leaving the temple to the more devout followers."

    menu:
        "Look around.":
            $ Sabia.face = "normal"
            show Sabia at left
            $ temp = renpy.random.randint(1,3)
            if temp == 1:
                "The temple was silent, except for a little draft that blew about the large columns that held the roof up."
                "There were few people showing their faith to Relona and her sisters today."
                "Sabia left them to their prayers."
                jump wcvillage_temple
            elif temp == 2:
                "There was some merriment in the temple today. Wine poured onto the ground in front of Relona and fire licking at cuts of meat."
                "The smell of revelry was heavy in the temple."
                "Sabia left it to the more devout followers."
                jump wcvillage_temple
            else:
                "A group of young women were gathered around Relona's statue, praying and worshiping."
                if wcv_devout_observation == False:
                    $ wcv_devout_observation = True
                    $ Sabia.face = "normalopen"
                    s "It seems like the villages on the outskirts are much more religious and devout than closer to the capital."
                jump wcvillage_temple
        "Go back":

            jump wcvillage


label wcvillage_tower:
    scene bg hcsstower
    show screen infohud("left")
    if wcvillage_first_visit_tavern == False:
        $ Sabia.face = "normalopen"
        show Sabia at left
        s "I better head to the tavern first. That's the most likely place to get information that can help me with Vehlis' request."
        s "I can have a look around town after."
        jump wcvillage
    if wcvillage_first_visit_tower == False:
        $ wcvillage_first_visit_tower = True
        $ Sabia.face = "normal"
        show Sabia at left
        "Sabia raised her eyes, following the outline of the tower as it jut skyward."
        "Memories of time spent with her father rushed back to her. Martial buildings like this had been her home..."
        "Much more than any aristocratic environment with Tyra, at least."
        "Two guards flanked either side of the entrance, glowering at Sabia as she approached."
        $ Sabia.face = "normalopen"
        s "They're not going to let me in, and I don't really need to go in either."
        s "Might as well just steer clear, for now."
        $ Sabia.face = "normal"


    menu:
        "Look around.":
            if met_roland == True:
                $ Sabia.face = "normal"
                $ Humansoldier.face = "normal"
                show Sabia at left
                show Humansoldier at center
                show Humansoldier as Humansoldier2 at right
                with dissolve
                "Sabia spotted the small grin on Roland's face as she headed toward him and the other guard."
                $ Humansoldier.face = "happy"
                roland "Hey, Sabia. I was just - uh..."
                $ Sabia.face = "irritated2"
                "The other guard gave an angry glower in Roland's direction."
                $ Humansoldier.face = "normal"
                roland "Sorry, better not be talking too much while working."
                $ Sabia.face = "normal"
                "Sabia understood that better than he probably realized. She gave him a nod and left."
            else:
                $ Sabia.face = "normal"
                $ Humansoldier.face = "angry"
                show Sabia at left
                show Humansoldier at center
                show Humansoldier as Humansoldier2 at right
                with dissolve
                guard1 "What do you want? We're already under enough stress trying to do our jobs when Whitecrest won't send any relief."
                guard2 "Shove off."
                $ Sabia.face = "irritated2"
                s "..."
                $ Sabia.face = "normal"
                $ Humansoldier.face = "normal"
                s "(No point in antagonizing them, I guess.)"
                "Sabia shrugged, and left the two guards alone."
            jump wcvillage_tower
        "Go back":
            jump wcvillage


label wcvillage_tsquare:
    scene bg hcsstsquare
    show screen infohud("left")
    if wcvillage_first_visit_tavern == False:
        $ Sabia.face = "normalopen"
        show Sabia at left
        s "I better head to the tavern first. That's the most likely place to get information that can help me with Vehlis' request."
        s "I can have a look around town after."
        jump wcvillage
    if wcvillage_first_visit_tsquare == False:
        $ wcvillage_first_visit_tsquare = True
        $ Sabia.face = "normal"
        show Sabia at left
        "Sabia gave the fountain a fond smile, the gentle trickle of running water over the edge of the fountain into the larger pool below."
        "She had some fond memories of spending time at a fountain like this in her younger days, with Relona watching over those that were visiting."
        "There was a young child sitting on the edge, splashing and giggling."
        "A bit farther around the rim of the fountain, a couple were kissing, their hands wrapped around each other."
        "Sabia felt she could spend a few minutes sitting with the others and enjoy the comforting presence of Relona."
    menu:
        "Sit.":
            $ Sabia.stamina += 10
            if Sabia.stamina > Sabia.maxstamina:
                $ Sabia.stamina = Sabia.maxstamina
            $ Sabia.face = "normalopen"
            show Sabia at left
            s "I'm sure I can take a few minutes to just enjoy the fountain."
            $ Sabia.face = "normal"
            "The short rest next to the Relonan fountain was relaxing, and Sabia felt a little refreshed."
            jump wcvillage_tsquare
        "Throw some lundils in.":

            $ Sabia.face = "normal"
            show Sabia at left
            if money < 5:
                s "(I don't have enough lundils on me unfortunately.)"
                jump wcvillage_tsquare
            if wcv_fountain_lundils == False:
                $ wcv_fountain_lundils = True
                $ money -= 5
                "Sabia thumbed a lundil, looking into the gently bubbling water."
                "After a few seconds, she tossed the lundil into the fountain."
                "The water parted and accepted it as it sunk to the bottom quickly."
                "She spotted one of the children glancing over slyly from the corner of his eyes."
                $ Sabia.face = "normalopen"
                s "I suspect that's not going to be there for long..."
                $ Sabia.face = "normal"
                "Shrugging, Sabia tossed another couple of lundils in."
                jump wcvillage_tsquare
            else:
                $ money -= 5
                "Sabia tossed a few lundils into the fountain. They'd be gone by tomorrow."
                jump wcvillage_tsquare
        "Give children a few lundils.":

            $ Sabia.face = "normal"
            show Sabia at left
            if money < 10:
                s "(I don't have enough lundils on me unfortunately.)"
                jump wcvillage_tsquare
            $ wcv_children_charity = True
            $ money -= 10
            "Sabia beckoned the gaggle of children over and gave them a few lundils each."
            "Their faces lit up and they offered a quick thanks before running off."
            jump wcvillage_tsquare
        "Go back":

            jump wcvillage
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
