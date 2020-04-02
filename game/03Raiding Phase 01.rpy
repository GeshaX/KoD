


label raidingintro:
    scene bg mainhall
    with dissolve
    "It took several days for the Red God's Arena to wind down after the official festivities had ended. Many of the orcs from other tribes lingered, plus it took a while to dismantle the temporary structures."
    "Sabia didn't mind at all, using that time to gather the orcs that had volunteered to work under her and put together an actual raiding force. They had their own equipment and training, though it wasn't always as good as she'd hoped and they were terribly disorganized."
    "Still, it was something to work with, and she could get support from other factions like the catgirls. Just when Sabia was beginning to think she could venture out, she discovered that she had a new problem: all raiding required permission from the Warchief."
    call sabiabase
    with dissolve
    "As she headed to the main hall to get permission, Sabia didn't anticipate any problems. She had no plans of heading west or antagonizing Lundar. No, her targets would be local bandits no one liked, and when possible, settlements to the north that weren't affiliated with Lundar."
    show groknak suspicious1 at center with dissolve
    "But when she approached Warchief Groknak, she saw his scowl and wondered if she wasn't mistaken. Maybe he just didn't want to see her, but..."
    show groknak suspicious2 at center
    g "No, human. Warchief Groknak forbids it."
    show sabiaemo angry1 at left
    s "You haven't even heard what I was going to request!"
    show groknak suspicious1 at center
    g "Shaman Ornshakar stands opposed to you being given the freedom of raiding. Given the danger of Lundar, Warchief Groknak agrees it is best to forbid you."
    s "But..."
    show sabiaemo irritated1 at left
    "Looking more carefully, Sabia spotted Ornshakar near the entrance. He was speaking to someone else, but the way he smirked at her suggested that he was here solely to get in her way. He hadn't managed to get revenge in any other way, so this was his next scheme?"
    show sabiaemo irritated2 at left
    s "And he can just object and stop me? I don't believe he has that much power - surely I can object to his opposition."
    g "You can object, yes."
    show orcshaman normal at right with moveinright
    "Groknak gestured, and Ornshakar hurried to join them. He'd made his expression less smug, but she still saw an infuriating glint in his eyes."
    show groknak suspicious2 at center
    g "Warrior Sabia seeks to go raiding, just as you said. You still stand opposed to her?"
    show groknak suspicious1 at center
    show orcshaman angry3 at right
    ornshakar "Yes! She will bring destruction down upon us all!"
    g "Warrior Sabia... you have earned much honor for yourself, but Warchief Groknak does not trust in your judgment. Given the threat of Lundar, War-"
    show sabiaemo angry1 at left
    s "This isn't about him, is it? Are you just that cowardly?"
    show groknak suspicious1 at center
    "Groknak glared at her, but didn't contradict it or even get that angry. Was he really a coward, then? Sabia had just been intending to shame him into changing the decision, but that was the wrong strategy."
    show groknak suspicious2 at center
    g "If that is all, Groknak will be going."
    hide groknak suspicious1 with moveoutright
    show orcshaman happy1 at right
    show sabiaemo closed2 at left
    "He left and the shaman smirked. Could it really be decided that easily, despite all the work she'd done? Sabia knew this was the moment to act, but wasn't sure what the right choice was."
    if orcalliance == "tekrok":
        show tekrok angry1 at center with moveinleft
        show orcshaman surprised at right
        show sabiaemo normal at left
        "Just when Sabia was starting to think she had a serious problem, Tekrok stormed into the hall, his gaze murderous."
        show tekrok angry2 at center
        t "You still haven't gone raiding yet? Why are you wasting Tekrok's time, human?"
        show sabiaemo normal at left
        show tekrok angry1 at center
        "Sabia was about to snap back at him, but she saw something different in Tekrok's eyes. He was angry, yes, but not at her. Thinking quickly, Sabia decided there was only one likely situation here."
        show sabiaemo irritated2 at left
        s "I'm trying, Captain, but the shaman here is standing in my way."
        show tekrok angry2 at center
        "Just as she'd hoped, Tekrok wheeled on Ornshakar, his fury palpable. The shaman took a step backwards on instinct before steeling himself."
        t "What are you doing, fool? Tekrok has no time for your cheap rituals!"
        show orcshaman angry3 at right
        ornshakar "Would you defy the will of the spirits, Tekrok?"
        show tekrok happy1 at center
        t "If you have any spirits looking down on you, surely they are disgusted by your cowardice!"
        show tekrok normal at center
        "Tekrok cast Sabia a stern glance, but his eyes then flickered toward where Groknak had gone."
        show tekrok angry2 at center
        t "Stop wasting time, human. Tekrok will do your work for you, yet again."
        scene bg mainhall
        call sabiabase
        with dissolve
        "Scowling back, Sabia stormed away, but she headed toward the room where Warchief Groknak had gone. Behind her, she could still hear Tekrok roaring at the shaman. Despite herself, that made her a smile a little."
        show groknak normal at right with dissolve
        "But she didn't smile long, since now she found herself facing the Warchief. Obviously he had heard what went on, so he now faced her with a grim expression on his face."
        s "Captain Tekrok will be speaking for me... does that take care of the complaint?"
    elif orcalliance == "rokgrid":
        "Just when Sabia was starting to think she had a serious problem, there was a hand on her shoulder."
        show rokgrid happy2 at center with moveinleft
        show orcshaman angry2 at right
        show sabiaemo normal at left
        "She turned in surprise and found Rokgrid behind her, with a deceptively peaceful smile. His hand had gripped her hard, though - at minimum, he wanted her to stop talking."
        show rokgrid happy3 at center
        r "Shaman Ornshakar, old friend... I had hoped this warrior would assist me. Can we not come to an agreement?"
        ornshakar "Don't try, Rokgrid. We all know the woman is your tool."
        show rokgrid angry1 at center
        r "That is a rather disrespectful way to refer to a Captain, Shaman Ornshakar. Must Captain Rokgrid bring his complaint formally?"
        show orcshaman surprised at right
        "That made Ornshakar widen his eyes. He backed up a little, almost as if there had been a threat. While he paused, Rokgrid turned back to her and spoke in a low voice."
        show rokgrid happy2 at center
        r "I can tie up his complaint, but this isn't your real problem. Go talk to the Warchief."
        scene bg mainhall
        call sabiabase
        with dissolve
        "Sabia had more questions for him, but now was obviously not the time. She nodded and turned away - behind her, she could hear Ornshakar objecting, but Rokgrid intercepted him with more honeyed words. Despite the situation, that made her smile a little."
        show groknak normal at right with dissolve
        "But she didn't smile long, since once she entered the back room, she found herself facing the Warchief. He looked up in surprise, his eyes narrow."
        s "Captain Rokgrid has some complaints of his own. I think we need to talk."
    else:
        "Just when Sabia was starting to think she had a serious problem, she heard the sound of a staff tapping on the floor of the hall."
        show ylva normal at center
        show ylva2 arm2 at center
        with moveinleft
        show orcshaman angry2 at right
        show sabiaemo normal at left
        "Turning, Sabia saw Ylva stride forward, gaze serious."
        show ylva opennormal at center
        ylva "Shaman Ornshakar, Ylva has several questions for you. Are you interfering with this matter for the sake of the tribe's spiritual health?"
        show orcshaman angry3 at right
        ornshakar "Why get involved with this? Do not meddle in Ornshakar's affairs!"
        show ylva openclosed2 at center
        ylva "Ylva disagrees that they are yours alone. You have taken on a great many affairs, Ornshakar... and you have done very little to guide this tribe. The council would not approve."
        ornshakar "Are you threatening Ornshakar?"
        show ylva closedsad at center
        ylva "Ylva is appealing to your better instincts. Withdraw this complaint and focus on your true work."
        hide orcshaman angry3 with moveoutright
        "The two shamans argued in low, terse voices for some time, but in the end, Ornshakar withdrew from the hall. Ylva remained behind, tapping her staff on the floor thoughtfully."
        show ylva normal at center
        ylva "He was on shaky ground making such a complaint, anyway. Shamans are not supposed to meddle in affairs of war."
        if A_ylva >= 5:
            show sabiaemo happy1 at left
            s "Thank you, Ylva! Glad I can count on you."
            if orcalliance == "dajrab":
                show ylva happy1 at center
                ylva "And I would be glad to help you... but actually, I was sent by Dajrab. It seems he knew of Ornshakar's meddling."
                show sabiaemo happy3 at left
                s "I should have known. He likes to work indirectly, doesn't he?"
                show ylva normal at center
                ylva "I will not comment on local matters. Likewise, I will leave you to argue your case with the Warchief."
                show sabiaemo normal at left
                s "Hopefully it won't be a problem, now that you took care of this problem."
                show ylva openclosed1 at center
                ylva "Perhaps... but perhaps not. Speak carefully, Sabia. And good luck."
                hide ylva openclosed1
                hide ylva2 arm2
                with moveoutleft
                "With that, Ylva left the chamber, no longer tapping her staff to make an entrance. Sabia watched her for a moment, wishing she had a better grasp of the situation, but then turned back to find the Warchief."
                show groknak normal at right with dissolve
                "She found him in the back room, seated and staring at a map. He looked up in surprise, his eyes narrow."
            else:
                show ylva happy1 at center
                ylva "I am glad to help you, but you are extremely lucky that I could. Had I not been informed by others about Ornshakar's meddling, I would not have been able to assist you."
                "Sabia had assumed everything would go smoothly, but she realized that itself was a weakness - a lack of information. Without a Captain as an ally, she did need assistance from someone. She nodded thankfully to Ylva."
                show sabiaemo happy3 at left
                s "I'll keep that in mind in the future, thanks."
                show ylva normal at center
                ylva "But now, I must leave you to argue your case with the Warchief."
                show sabiaemo normal at left
                s "Hopefully it won't be a problem, now that you took care of this problem."
                show ylva openclosed1 at center
                ylva "Perhaps... but perhaps not. Speak carefully, Sabia. And good luck."
                hide ylva openclosed1
                hide ylva2 arm2
                with moveoutleft
                "With that, Ylva left the chamber, no longer tapping her staff to make an entrance. Sabia watched her for a moment, wishing she had a better grasp of the situation, but then turned back to find the Warchief."
                show groknak normal at right with dissolve
                "She found him in the back room, seated and staring at a map. He looked up in surprise, his eyes narrow."
        else:
            show sabiaemo irritated2 at left
            s "Thank you, but... why did you help me?"
            if orcalliance == "dajrab":
                show ylva openclosed2 at center
                ylva "It wasn't my choice - I was sent by Dajrab. It seems he knew of Ornshakar's meddling."
                show sabiaemo closed2 at left
                s "So that's the only reason. I suppose I should thank him."
                show ylva normalnarrow at center
                ylva "I would not have done it, but Ornshakar's meddling truly is shameful. But I will leave you to deal with the Warchief yourself."
                s "I see."
                show ylva normal at center
                ylva "But... Captain Dajrab spoke highly of you. Perhaps it would be better if we were on good terms in the future?"
                menu:
                    "Agree":
                        $ A_ylva += 2
                        s "We haven't gotten off on a good foot, but we don't have to like each other to work together. Yes, perhaps we can."
                        show ylva happy1 at center
                        "To Sabia's surprise, Ylva gave her a slight smile at that."
                        ylva "Good. But for now, I think you should speak to Warchief Groknak."
                        show sabiaemo normal at left
                        s "Hopefully it won't be a problem, now that you took care of Ornshakar."
                        show ylva openclosed1 at center
                        ylva "Perhaps... but perhaps not. Speak carefully, Sabia."
                        hide ylva openclosed1
                        hide ylva2 arm2
                        with moveoutleft
                        "With that, Ylva left the chamber, no longer tapping her staff to make an entrance. Sabia watched her for a moment, wishing she had a better grasp of the situation, but then turned back to find the Warchief."
                        show groknak normal at right with dissolve
                        "She found him in the back room, seated and staring at a map. He looked up in surprise, his eyes narrow."
                    "Disagree":
                        $ dom += 1
                        s "If you don't want to give any help, I don't need it."
                        hide ylva openclosed1
                        hide ylva2 arm2
                        with moveoutleft
                        "Ylva frowned at that, then turned and left the chamber, no longer tapping her staff to make an entrance. Sabia watched her for a moment, wishing she had a better grasp of the situation, but then turned back to find the Warchief."
                        show groknak normal at right with dissolve
                        "She found him in the back room, seated and staring at a map. He looked up in surprise, his eyes narrow."
            else:
                $ A_ylva -= 1
                show ylva openclosed2 at center
                ylva "I only came because Ornshakar's meddling truly was shameful. Even that might not have been enough, but some of your allies begged me to intervene."
                show sabiaemo closed2 at left
                ylva "This is the last time, Sabia."
                hide ylva openclosed2
                hide ylva2 arm2
                with moveoutleft
                show sabiaemo irritated1 at left
                "With that, Ylva walked out of the chamber. Sabia frowned after her for a while, then shook her head. It was more important to find the Warchief and gain permission."
                show groknak normal at right with dissolve
                "She found him in the back room, seated and staring at a map. He looked up in surprise, his eyes narrow."
    show sabiaemo normal at left
    "Groknak stared at her with a heavy gaze, and Sabia realized that she had missed something. There wasn't hatred there, and he hadn't been stopping her just to oppose her. Groknak stared at her for a long time."
    show groknak normalopen at right
    g "Human... by law you are one of us, but not in spirit. You will bring destruction upon us all."
    show groknak normal at right
    "Sobered by the change in tone, Sabia said nothing and moved to stand opposite him. She examined his face more carefully and saw the tension there. He was older than she had thought at first, too, and worn by a long and difficult life."
    show sabiaemo closed2 at left
    s "I'm Lundar's enemy now too. Do you really think I'm going to go charging and antagonizing them?"
    g "Groknak has seen enough warriors leave with the best of intentions and return with death on their heels."
    show sabiaemo irritated1 at left
    s "What exactly are you afraid of?"
    "He was silent for a long moment, briefly touching his helmet in a strangely sentimental movement before suddenly pulling his hand back. When his eyes fixed on her again, they did not look afraid - his gaze gave no ground at all."
    show groknak normalopen at right
    g "Do you remember the tribe of Az og Dar?"
    "After searching her memory for only a moment, it came to her."
    show sabiaemo normal at left
    s "They lived in the province of Azal before the southeastern edge was fully integrated into Lundar. They tried to launch an assault on the Grand Temple of Relona."
    show groknak normal at right
    g "That is the story. Groknak knew the Warchief of that tribe. He was no fool, and he would not have tried such a foolish assault."
    show sabiaemo closed2 at left
    s "Maybe. But if I recall, the chief was killed during the battle."
    show groknak normalopen at right
    g "Of course he would have done his duty, once he had been drawn into the war. But Groknak does not believe he caused it."
    g "He was Groknak's friend, a comrade from a time before we had any great rank. He was... smarter than Groknak. More cautious. He agreed that war against Lundar was not the way forward, and tried to move Az og Dar away from the border."
    show sabiaemo irritated1 at left
    s "What, are you saying Lundar started the fight?"
    show groknak normalopen at right
    show sabiaemo closed2 at left
    g "Meaningless. Lundar is at the start of this entire war."
    g "But this fight... no, Groknak can imagine the truth. Young warriors raided into human lands. Perhaps filled with visions of treasure or war, or more likely pursuing their own private vendettas. But they went too far. They brought Lundar down upon their heads and ended their entire tribe. Despite the work of a wise Warchief."
    show groknak normal at right
    show sabiaemo sad1 at left
    "After his heavy words ended, Groknak sat in silence for a long time. Sabia examined him, realizing that she had been gauging him wrong this entire time."
    "Groknak was not a coward or a fool. He understood what he faced and sought to find a path to survival for his people. Compared to the aggressive Warchiefs of the past, he might seem weak - but those Warchiefs would have gotten their tribes killed long ago. Warchief Groknak was perhaps the perfect leader for this era of waning orc influence."
    "What she would do with that, Sabia wasn't sure. But she stayed focused on her true goal and spoke quietly."
    show sabiaemo closed4 at left
    s "Warchief... do you truly believe that I will happily stay here in camp and do nothing?"
    g "No."
    show sabiaemo closed2 at left
    s "Then you need to ask yourself a question. If you want to protect your tribe, is it better to deny me what I'm going to do anyway? Or to permit this and maintain some control over my actions?"
    "He didn't answer and no longer looked at her. Sabia paused for a moment, unsure, then decided to take a risk. She reached forward and touched his shoulder - just the armor plate, not his skin, but it still made him shift in surprise."
    show sabiaemo sad1 at left
    s "I will not pretend to be your friend, Warchief. But you can decide whether or not I am your enemy."
    if A_groknak >= 5:
        $ groknakbonus = True
        show groknak normal at right
        "To her surprise, Groknak didn't knock her hand away immediately. Instead, he looked her in the eye for a time, then stood up, forcing her back. The quiet moment was gone, but she saw no anger in his eyes."
    else:
        $ groknakbonus = False
        show groknak angry3 at right
        "Groknak paused a moment, then grunted and knocked her hand away. When he rose to his feet, all hint of the quiet from before was gone."
    show groknak suspicious1 at right
    g "Warchief Groknak will permit your raiding... on one condition."
    show sabiaemo normal at left
    s "Which is?"
    show groknak suspicious2 at right
    g "Before you are free to attack anywhere, you must first deal with a problem. There is a small group of rogue orcs, unconnected to any tribe, who are working as bandits in human lands. You understand how they will become a problem for us all."
    s "Then why haven't you sent someone to take care of it?"
    show groknak suspicious1 at right
    g "Because they live near human lands, and most warriors who attempted to destroy them would only cause more trouble. But perhaps you..."
    show sabiaemo closed1 at left
    s "I understand, then. I have your permission if I take care of these orcs first?"
    show groknak suspicious2 at right
    g "Only if you do so without causing a larger raid and manage to pacify the local humans. The Warchief's warriors will be watching you, Sabia."
    show sabiaemo normal at left
    s "Understood. I'll prove myself."
    show groknak normal at right
    "He didn't answer that, instead looking down again. But his eyes were not looking over the map as if for strategy, but instead gazing at one specific spot. Sabia couldn't be sure, but she thought he was staring at the province of Azal."
    "Deciding the time for words had passed, Sabia nodded silently and left."
    scene bg mainhall
    call sabiabase
    with dissolve
    $ recruitmentopened = True
    $ Mainarmy.add_troop(Sabiasquad)
    $ ef_forest2_unlocked = True
    $ ef_grove_unlocked = True
    $ ef_rogue_orc_camp_unlocked = True
    "On her way out, she considered her resources. She had her own unit of volunteers, but they were nothing like a real fighting force. With some work, though, maybe they could be more."
    if orcalliance == "tekrok":
        "Though he might make trouble, Tekrok would probably give her some forces as well. It was time for him to start giving some real support in their alliance."
    elif orcalliance == "rokgrid":
        "She could count on getting some decent troops from Rokgrid, though she'd probably need to negotiate with him. But she thought he'd meet the terms of their alliance."
    elif orcalliance == "dajrab":
        "Hopefully she could get some support from Dajrab. Their alliance had been a tenuous one so far, but she hoped that she had done enough to receive some direct support."
    else:
        "Without a Captain as an ally, her path might be a little more difficult, but Sabia was determined not to depend on anyone. And she did have other options..."
    if catgirlstatus == "enslaved":
        $ Mainarmy.add_troop(Catgirlslaves)
        "Fortunately, with the catgirls enslaved, Sabia could easily form a unit from some of them. She'd have to be careful not to let them turn on her, but she thought that many would prefer to fight for her than to service the orcs in the tents."
    elif catgirlstatus == "free":
        $ Mainarmy.add_troop(Catgirlallies)
        "Fortunately, she'd gotten some catgirl volunteers as well, grateful for her freeing them. Not as many as she could have had if she'd enslaved them, but enough to form their own unit."
    elif catgirlstatus == "recruited":
        $ Mainarmy.add_troop(Catgirlrecruits)
        "Since the catgirls had already joined them, Sabia was certain she could get a group of them as well. Most would prefer to fight for her than for orcs."
    else:
        $ Mainarmy.add_troop(Catgirlrecruits)
        "It would be easy to get catgirls to work for her, Sabia thought. They were already working off their debts, surely many would prefer to fight for her than to service the orcs in the tents."
    "To start, that was all she had. Not a real army, but a large enough force to raid. If she could scout far enough, she could reach human lands, get more information about her family, and start building toward her true goals."
    "She had a lot of work to do to get ready for that, but now she had permission. All she needed to do was take care of this problem, then she would finally have the freedom to attack as she saw fit..."
    jump lowerorccamp

label kiaprogressionscenes:
    scene bg countryside
    $ renpy.block_rollback()
    if kiacooldown == True:
        "Sabia headed out to try to find Kia, but there was no sign of her."
        return
    if kiaprogression == 2:
        call KLkiaintro2
    elif kiaprogression == 3:
        call KLkiaintro3
    elif kiaprogression == 5:
        call KLkiaintro4
    elif kiaprogression == 6:
        call KLbonequest
    elif kiaprogression == 7:
        call KLlutvrogmeeting1
    elif kiaprogression == 8:
        call KLlutvrogmeeting2
    elif kiaprogression == 9:
        call KLbacktrackingscene
    elif kiaprogression == 10:
        call KLsabiascene
    elif kiaprogression == 11:
        call KLylvalesson
    elif kiaprogression == 12:
        if kiabones >= 5:
            call KLbonequestcomplete
        else:
            "Sabia headed out to try to find Kia, but she seemed to be hunting for bones. Sabia decided to do the same."
    elif kiaprogression >= 13:
        "Kia spotted Sabia on her way and approached to lick her face, but then ran off to chase something. It seemed she was too restless to talk for now."
    jump eastern_frontier_map

label KLkiaintro1:
    $ kiacooldown = True
    scene bg countryside
    call sabiabase
    with dissolve
    if A_ylva >= 10:
        $ kiaprogression = 2
        "While moving outside camp, Sabia spotted Ylva heading out with a purposeful stride. That wasn't so unusual, as she needed to gather ingredients from outside camp for her rituals, but there was something that made Sabia curious."
        show ylva normal at right
        show ylva2 arm2 at right
        with dissolve
        "Once they were fully away from camp, Sabia hurried to catch up with her."
        show sabiaemo happy1 at left
        s "How's everything going, Ylva?"
        "Ylva gave her a considering glance, then nodded."
        ylva "It should be fine... follow me and I'll show you."
        "Though a little surprised, Sabia felt she could trust Ylva enough for that. They took a circuitous route away from camp to shake tails, though Sabia didn't think there were any, and eventually reached a hilly area."
        "They went up a ridge, and to Sabia's surprise, on the other side there was a small valley filled with trees. It seemed like a good place to hide something... or someone."
        show ylva closednormal at right
        ylva "This is where I usually meet her. I don't know if she'll be here, but she often is."
        show sabiaemo surprised1 at left
        s "Her? Do you mean...?"
        show ylva normalnarrow at right
        ylva "Don't make any sudden moves, and don't be alarmed. She can be... aggressive."
    elif A_ylva >= 5:
        $ kiaprogression = 2
        "While moving outside camp, Sabia spotted Ylva heading out with a purposeful stride. That wasn't so unusual, as she needed to gather ingredients from outside camp for her rituals, but there was something that made Sabia suspicious."
        "She considered showing herself, but decided to watch and wait. She pursued Ylva quietly as they moved further away from camp."
        "Then, without warning, Ylva turned back to look at her."
        show ylva angry1 at right
        show ylva2 arm2 at right
        with dissolve
        ylva "What is it, Sabia?"
        s "I was just wondering where you were going."
        "Ylva gave her a considering glance, then nodded."
        show ylva normal at right
        ylva "It's a bit of a secret, but I guess you deserve to know about this one. Follow me."
        "Though a little surprised, Sabia felt she could trust Ylva enough for that. They took a circuitous route away from camp to shake tails, though Sabia didn't think there were any, and eventually reached a hilly area."
        "They went up a ridge, and to Sabia's surprise, on the other side there was a small valley filled with trees. It seemed like a good place to hide something... or someone."
        "Ylva gave no indication it was anything special, just headed down into the valley, so Sabia followed her."
    else:
        $ kiaprogression = 1
        "While moving outside camp, Sabia spotted Ylva heading out with a purposeful stride. That wasn't so unusual, as she needed to gather ingredients from outside camp for her rituals, but there was something that made Sabia suspicious."
        show ylva normal at right
        show ylva2 arm2 at right
        with dissolve
        "Just what could Ylva be up to? Sabia prowled after her, and the orc seemed oblivious to being followed."
        "Right up until the point where Sabia moved around a tree and Ylva was gone. Sabia looked around in frustration, tried to check for signs of her passing, but there was nothing. She'd slipped away."
        "Scowling, Sabia just headed back to camp."
        return
    show sabiaemo irritated1 at left
    "Sabia thought she spotted a shadow shifting, turned with her hand on her weapon - and found herself slammed flat on her back, staring at the boughs overhead."
    show sabiaemo surprised1 at left
    "Claws savagely bit down into the earth beside her and Sabia found herself facing an inhuman face... a familiar one."
    show kia normal2 at center with dissolve
    "Though she hadn't gotten a good look before, there was no doubt in her mind that the woman-shaped creature on top of her was the Makhor. The coloring and head spines were too similar for it to be a coincidence."
    "For a moment, the Makhor stared down at her, eyes bright. Sabia was uncomfortably reminded that it was very much a predator."
    if A_kia >= 3:
        show kia happy1 at center
        "Then the Makhor leaned forward, snuffled at her face, and made a pleased growling sound. She pulled back enough to allow Sabia to get back up."
    else:
        show kia irritated1 at center
        "The Makhor snuffled at her suspiciously, gave a low growl... but pulled back. Still eyeing Sabia, she shifted away enough to allow Sabia to get back up."
    if A_ylva >= 5:
        show sabiaemo irritated2 at left
        "Sabia got up, rubbing the back of her head."
        s "You weren't kidding about her being aggressive."
        show ylva happy1 at right
        ylva "She's accepted you here, though, so I think the dangerous moment has passed."
    else:
        show sabiaemo angry1 at left
        "Sabia got up, rubbing the sore spot where she'd slammed into the ground. She scowled at Ylva."
        s "Why didn't you warn me?"
        show ylva happy2 at right
        ylva "You were the one stalking me earlier. I wanted to see how she'd react."
    show kia tilt1b at center with dissolve
    "Before Sabia could say more, the Makhor lunged at her, large paws coming down on her shoulders and putting them face to face. She sniffed at Sabia some more, tugged at her clothes experimentally, batting at her hair tie. Her head tilted to the side as if thinking."
    show kia normal1 at right with moveinright
    "Then, apparently satisfied, the Makhor retreated and sat down some distance away, apparently ignoring them completely. She frowned down at her paw, then licked at the fur as if grooming. After another frown, she concentrated... and the fur seemed to shift slightly. Some sort of magical grooming related to her transformation abilities?"
    show ylva normal at center
    show ylva2 arm2 at center
    with moveinright
    "In any case, it seemed like she was no longer interested. Ylva sighed and came to stand beside her."
    ylva "She acts very intelligently, but she doesn't seem to care about certain things. I don't know if this will work."
    show sabiaemo irritated2 at left
    s "What, exactly? What are you trying to accomplish, Ylva?"
    ylva "I don't want her attacking the camp, or even coming in. You can imagine how much it would disrupt everything."
    show sabiaemo normal at left
    s "I think she'll be cautious. She's a wild animal - she has good instincts. After being captured once, she'll be more wary in the future."
    show ylva closednormal at center
    ylva "She's wild, Sabia, but I'm not sure she's really an animal. Why take an orc-like form like that?"
    show sabiaemo irritated2 at left
    s "Orc-like form? She looks more human to me."
    show ylva opennormal at center
    ylva "I only meant the general shape... but I suppose it doesn't matter. She's something different from either."
    show sabiaemo closed2 at left
    s "I don't know, Ylva, I think all thi-"
    show kia happy2E at right
    makhor "Ylva?"
    show ylva surprised at center
    show sabiaemo surprised1 at left
    "The clearly spoken word surprised both of them. Sabia actually took a step back and shifted a hand to her weapon... but it was only the Makhor, now examining them both with bright eyes. They stared back at her."
    "After a moment, the Makhor leapt forward, both paws landing on Ylva's shoulders so they were face to face."
    show kia happy2 at right
    makhor "Ylva?"
    show ylva happy1 at center
    ylva "Ah... yes, my name is Ylva."
    "Without warning, the Makhor spun around, inside Sabia's range before she could react. Sabia found herself staring into those mismatched eyes, so close to hers. She swallowed and tried not to flinch, but she could feel the strength in the Makhor's paws."
    makhor "Ylva?"
    show sabiaemo closed2 at left
    show ylva normal at center
    s "Not Ylva. Sabia."
    show kia pawtiltcurious at right with dissolve
    makhor "Sabia?"
    show sabiaemo happy3 at left
    s "Yes, that's right."
    show kia pawtilteager1 at right
    makhor "Ylva! Sabia!"
    "Sabia had no idea how much the Makhor understood, but tried to put some meaning into her tone. Maybe that was the wrong approach, though. If their words were just sounds to her, she would have kept ignoring them instead of latching onto their names."
    show sabiaemo closed3 at left
    s "You think she's been listening?"
    show sabiaemo normal at left
    "But Ylva barely seemed to hear, instead focused fully on the Makhor. She put a hand on her own chest."
    show kia pawuncertain1 at right with dissolve
    show ylva happy2 at center
    ylva "Who?"
    "Ylva tapped herself a few times and repeated the word to make it clear."
    ylva "Ylva. I am Ylva."
    "Her hand swung to point at Sabia."
    ylva "Who? Sabia."
    show ylva happy2 at center
    "Then she pointed toward the Makhor."
    ylva "Who?"
    show kia tilt1 at right with dissolve
    "The Makhor cocked her head and peered at them. It was impossible to tell if she was confused, or thinking, or something else. After a long pause, she finally responded."
    show kia happy2 at right with dissolve
    makhor "Kiandhakhani!"
    "The name was growled, but it definitely sounded like a name. It was also going to be murder to pronounce, but Ylva made an effort."
    show ylva closedhappy at center
    ylva "So you're... Kianda-Kiandhakani?"
    makhor "Kiandhakhani!"
    show ylva normal at center
    show sabiaemo happy1 at left
    s "That's a hard name. Is it okay if we call you \"Kia\"?"
    show kia tilt2b at right with dissolve
    "The Makhor gave her a long look, again cocking her head. She released a low, curious whine... which gradually shifted into a pleased rumble."
    show kia pawuncertain1 at right with dissolve
    makhor "Kia?"
    show kia tilt1 at right with dissolve
    makhor "Kiaaaa..."
    show kia pawtiltcurious at right with dissolve
    makhor "Kiiiia..."
    show kia pawtilteager2 at right
    kia "Kia!"
    $ a_list.append("Kia")
    show sabiaemo surprised1 at left
    "Apparently quite pleased, the Makhor - Kia - pounced forward and abruptly licked Sabia's face. She was surprised, but Kia moved too quickly for her to do much about it."
    show sabiaemo happy1 at left
    show ylva happy1 at center
    ylva "You understand, then? Maybe not all the words, but you understand the concept of names, and you have one for yourself..."
    show kia happy2 at right with dissolve
    "Kia shifted around to look at Ylva for a moment, then smiled."
    kia "Kiandhakhani Kia! Not Ylva. Not Sabia. Kia!"
    ylva "She does understand."
    s "It seems so. Dogs and some animals can learn names, but she also understood the word \"not\" - that shows a lot more intelligence."
    show ylva normal at center
    ylva "The Makhor probably have their own language. We can't be sure without having two of them together, but that would be my guess."
    s "Then we can communicate with her. Perhaps y-"
    show kia happy3x at right
    "Without warning, Kia's ears perked up and her eyes glowed. They swiveled to the side, then her head swung in the same direction. A second later she was off like a shot, chasing after something small. Sabia could just see movement in the grass - a rabbit?"
    show sabiaemo eyebrow1 at left
    s "...I think the hard part might be getting her to pay attention."
    show ylva happy1 at center
    ylva "Still, this is a good sign. She's smart enough to make good decisions."
    show sabiaemo normal at left
    s "Not necessarily human decisions, though. Or, uh... orc decisions."
    "In the distance, Kia snatched up something, which was indeed a rabbit. Sabia expected it to be torn apart... but instead Kia flipped the rabbit over a few times with her tail, pushed it a short distance away, then sat back on her haunches."
    show kia happy3 at right
    "After a moment, the grass rustled as the rabbit recovered and began to run again. As Kia watched it, eyes alight, Sabia realized that Kia was just playing."
    "The Makhor hunted bigger prey than rabbits."
    show ylva closedhappy at center
    ylva "Regardless, I will try to see if I can't make some headway with her. I assume you won't tell anyone about this?"
    s "Obviously not. We both have to go out of camp for many reasons, so it should remain a secret."
    show ylva normalnarrow at center
    ylva "Still, let's be as cautious as possible."
    "Sabia nodded in agreement. But she had already been gone for quite some time and needed to get back to camp. As she left, she glanced back at the humanoid Makhor running through the grass."
    "Kia, apparently. Sabia had never expected to encounter such a creature, much less meet and exchange names with one. Her life really had changed in strange ways."
    "Shaking her head, Sabia hurried back to camp."
    $ A_kia += 1
    return

label KLkiaintro2:
    $ A_kia += 1
    $ kiaprogression = 3
    $ kiacooldown = True
    scene bg countryside
    call sabiabase
    with dissolve
    "When Sabia approached Kia's grove, there was no sign of either her or Ylva. But the shaman had left a while back and not returned, so Sabia thought there was a good chance sh-"
    show kia happy2 at right
    "Abruptly Kia popped up in front of her, grabbing Sabia before she could object."
    kia "Sabia! Eat!"
    "The Makhor nearly picked her up and pulled her deeper into the forest, roughly but not ungently. Sabia was soon escorted into a deeper clearing, where to her surprise a low fire burned. Atop it was a huge piece of meat, what looked like the remains of a deer."
    show ylva happy1 at center
    show ylva2 arm2 at center
    "Ylva was beside it, carefully finishing the cooking process without letting the fire produce too much smoke. It smelled delicious - Sabia couldn't help but draw closer, and Ylva smiled when she saw her."
    ylva "Seems like Kia smelled you a ways out."
    show kia pawtilteager2 at right with dissolve
    kia "Sabia! Eat!"
    "Kia pointed to her mouth as if to make her meaning clear."
    show sabiaemo happy1 at left
    s "Haha, I'm glad I'm not the one being eaten..."
    show kia happy2 at right with dissolve
    ylva "She showed up with this. I think it's a gift."
    s "It actually smells great. It's almost ready, I hope?"
    show ylva closedhappy at center
    ylva "Yeah, you can try some. Then maybe you can help me with Kia."
    show sabiaemo normal at left
    show ylva normal at center
    "When Ylva handed Sabia a knife, she eagerly used it to carve off a piece of sizzling meat. It was almost too hot to eat, but Sabia still wolfed it down. The meat itself was good, it was cooked perfectly, and Ylva hadn't gone overboard salting it like most orcs."
    "Ylva took a piece herself and chewed it thoughtfully. Before she could say anything, Kia popped up beside them."
    show kia happy4 at right
    kia "Ylva, Sabia, Kia. Sit!"
    show sabiaemo happy3 at left
    s "She... wants us to sit down?"
    show ylva closednormal at center
    ylva "I don't think so, actually... she's picked up some verbs quickly, but I'm not sure what she thinks \"sit\" means."
    show kia happy2 at right
    show ylva normal at center
    "If the Makhor wanted them to sit, Sabia was ready to sit. But instead of pushing the matter, Kia just watched them, rumbling happily."
    show sabiaemo normal at left
    "After eating for a while, Sabia cut another piece and extended it with the knife toward Kia."
    s "Eat?"
    show kia tilt1 at right with dissolve
    "Kia cocked her head for a long time, then moved forward and grabbed the meat off the knife with her teeth, unconcerned about the edge. She consumed it in several bites, face still filled with a puzzled expression."
    show kia pawtiltcurious at right with dissolve
    kia "..."
    show kia tilt1b at right with dissolve
    kia "Sabia eat. Kia not eat."
    show ylva happy1 at center
    ylva "She ate a lot of the deer raw. Either that's what she needs or it's just what she's used to."
    s "Ah. I hope it's not a problem that I-"
    show kia happy2 at right with dissolve
    kia "Sit!"
    "Kia settled back with a happy expression. Sabia again wondered if it was a command, but no... it seemed like Kia had intentionally spoken to cut her off. Whatever she meant by \"sit\" it seemed to be a positive word."
    "Sabia settled down to eat some more, and only while doing so noticed that the clearing wasn't the same as before. There was a roughly-bound book and a few sheets of paper, and also an area of cleared dirt that was covered in scratches."
    s "What's all this?"
    show ylva closedsad at center
    ylva "I'm trying to teach Kia more words via drawings, but it's not going well. Verbs that I can demonstrate, she gets right away, but abstract things like categories..."
    show ylva normal at center
    "Ylva used a stick to draw a simple figure in the dirt, drew the word \"orc\" beside it and spoke it aloud. Kia watched her curiously. Ylva followed the orc with a human, labeled and spoken in the same way, and kept going."
    show kia pawtiltconfused at right with dissolve
    "The drawings were actually not bad - even before the labels, Sabia could instantly tell which one was the catgirl, the elf, and the minotaur. Kia looked at the two of them, stared at the drawings a moment, then looked back to them and cocked her head to the side for a bit."
    show kia pawtilteager1 at right
    "After a moment, she reached down and began to scribble wildly in the dirt with one claw, ruining the drawings. Sabia looked for an image of some kind for a while before deciding that it was probably purely random."
    kia "Sit?"
    show ylva sad at center
    "Ylva sighed and set her stick aside."
    show kia pawtiltcurious at right
    ylva "No, that's not sitting. It's okay, Kia."
    show ylva normal at center
    "She took another piece of meat and chewed thoughtfully for a while, finishing a bit before swallowing and speaking again."
    show ylva opennormal at center
    ylva "That's about what's happened before. She doesn't seem to see the drawings, she just thinks it's some kind of game. That, or she doesn't care."
    show sabiaemo closed1 at left
    s "What if we got some paper and showed her proper drawings? Some mostly realistic ones."
    show ylva sad at center
    ylva "I tried that first. When I wasn't looking, she ate the paper."
    "Ylva sighed and stared upward into the clear sky. Meanwhile, Sabia kept watching Kia. She was still curiously scratching at the dirt with a puzzled look, growling to herself."
    show sabiaemo normal at left
    s "Maybe she can't see representations at all. You or I have grown up seeing pictures and reading words on paper, but to Kia they might just be random shapes."
    show ylva normal at center
    ylva "That's possible, but if so, how do we communicate any further than this?"
    show sabiaemo happy1 at left
    s "Well... maybe we could try showing her things in person?"
    "Ylva blinked at Sabia, then smiled slowly."
    show ylva happy1 at center
    ylva "That's not a bad idea. Definitely worth trying."
    show sabiaemo closed2 at left
    s "Isn't there a risk of her running out and causing trouble, though?"
    show ylva normal at center
    ylva "Yes, I think it would be best if we worked with her a little more, first. Give me some time, then let me know when you want to try."
    show sabiaemo normal at left
    "Sabia nodded and ate a little more. But her thoughts were drifting to what might be done. Both to help communicate with Kia, and what could be done if the Makhor was willing to work with her."
    menu:
        "Use the Makhor as a tool":
            $ slavery += 1
            "Kia might be smart, but she was ultimately a wild beast. She could be extremely dangerous if the orcs got ahold of her... Sabia needed to gain control first."
        "Turn Kia into an ally":
            $ freedom += 1
            "Meeting a Makhor had brought many surprises, but Sabia thought that Kia was a potential ally. Provided that they could actually communicate clearly with her."
    "How that would work, remained to be seen. For now, Sabia just enjoyed the food and considered the future."
    return

label KLkiaintro3:
    $ kiaprogression = 5
    $ kiacooldown = True
    scene bg road2
    call sabiabase
    with dissolve
    "The next time Sabia tried to go meet Kia, she found the clearing completely empty. Ylva had left camp, but there was no sign of her, either."
    "After exploring the grove for a bit, Sabia decided that it really was a coincidence. There was other work for Ylva to be doing, and Kia was apparently out. Counting the trip as a loss, Sabia headed back."
    "Sabia headed back at a brisk walk, resolving to at least enjoy the journey. But while she was scanning the horizon, she noticed something burning."
    "More than just a small fire... her immediate thought was that it might be bandits, and Sabia wished that she hadn't gone alone. She moved closer cautiously, resolving to at least scout a little for later usage."
    "As she got closer, it became obvious that there was some kind of wagon on fire. It was a small one, probably only carrying a person or two, and the rough wood looked orcish to her. The contents hadn't been stolen, they were smashed and currently on fire."
    "What that meant, Sabia wasn't sure. She saw something out of the corner of her eye and whirled, ready to fight... but there was no attack."
    show kia normal1 at right
    show sabiaemo irritated1 at left
    "Instead, she spotted Kia sitting in some tall grass not too far away. Her back was to the wagon as if she didn't even see the fire. Sabia frowned and moved closer."
    "Kia's tail was swishing back and forth playfully, and she seemed to be toying with a rabbit or some other small animal. Had she destroyed the wagon and then gotten distracted hunting something?"
    show kia happy2 at right
    "Sabia got closer and Kia smiled up at her. There was blood on her teeth."
    show sabiaemo surprised1 at left
    "Sabia looked down at what Kia was playing with and discovered that she was batting around a decapitated orc head. The face was still frozen in shock, though one eye had been burst open. There was a string of viscera and part of a spine hanging from the neck."
    show sabiaemo surprised3 at left
    "Though Sabia had seen decapitations before, she hadn't seen them played with like this and couldn't help but recoil a little. While she struggled to contain her reaction, Kia looked at her curiously."
    show kia happy4 at right
    "After a time, Kia lifted the gorey head in one hand and raised it toward Sabia."
    kia "Eat?"
    show sabiaemo closed2 at left
    s "Uh... no. No thank you, Kia."
    show kia uncertain2 at right
    kia "No eat?"
    show kia tilt1 at right with dissolve
    show sabiaemo normal at left
    "Kia dropped the head, settled back on her haunches, and observed Sabia as if her behavior was strange and inexplicable."
    show kia pawtilteager2 at right with dissolve
    "Without warning Kia smiled, grabbed the head, and sprinted to the wagon. Sabia followed, bracing herself and not entirely sure why."
    "Still smiling with bared teeth, Kia effortlessly spitted the skull on the spike of her tail and then stuck it into the flames. She began turning it back and forth like Ylva had done with the deer, though her movements were random imitations. While roasting the skull, Kia smiled brightly at her again."
    show kia happy2 at right with dissolve
    kia "Sabia eat?"
    show sabiaemo sad2 at left
    s "Uh... no, sorry. No, thank you."
    show kia pawtiltconfused at right with dissolve
    "Kia settled back in confusion, staring at her strangely. After a moment, she pulled the skull from the flames and examined it as if for defects. She frowned at Sabia's strange behavior, then flung the skull off her tail carelessly."
    show kia happy1 at right with dissolve
    kia "Sabia sit?"
    show sabiaemo normal at left
    s "Maybe. Where's Ylva?"
    show kia happy1E at right
    kia "No Ylva."
    s "So not here? I wish I could ask you why you killed these orcs, but I'm guessing you don't understand that?"
    show kia tilt2 at right with dissolve
    "Kia tilted her head to the side and blinked at her."
    show sabiaemo closed2 at left
    s "I thought not. Well, I don't know if trying to talk will do any good..."
    menu:
        "Stay":
            $ A_kia += 1
            "Since she'd already come out this far, Sabia resolved to see what she could do. She did try to convince Kia to move away from the wagon, which might draw others."
        "Go back":
            "Unlikely to make progress on her own and nervous that the fire might draw others, Sabia said goodbye to Kia and headed back to camp."
            "Kia stayed behind, and Sabia tried not to think about her playing with corpses as she walked back."
            return
    show sabiaemo normal at left
    "When they were some distance away, Kia abruptly sat down and faced Sabia. One of her paws swung up, pointing to herself."
    show kia pawtilteager1 at right with dissolve
    kia "Who?"
    show sabiaemo eyebrow1 at left
    s "...Kia?"
    "Kia nodded seriously. Sabia was puzzled until a moment later her paw swung toward the burning wagon."
    show kia happy1 at right with dissolve
    kia "Who?"
    show sabiaemo normal at left
    s "I don't know. Sorry. Did you kill people you didn't know?"
    kia "Who."
    "That... hadn't sounded like a question. Kia stared back at her, quite seriously. Abruptly Sabia was struck by a strong intuition that she was looking at another person from across a vast gulf. Kia might act like a beast, but she was an intelligent person trying to communicate from the opposite side."
    show kia happy2 at right
    "After giving an irritated whine, Kia's expression became more playful. Her paw swung up to point at Sabia."
    kia "Who?"
    show sabiaemo closed2 at left
    "It was a dumb question at face value. Had she been giving Kia too much credit? Was there a deeper meaning to it? Sabia wasn't sure how to answer."
    menu:
        "Don't answer":
            $ A_kia += 0
            show kia tilt1 at right with dissolve
            show sabiaemo irritated2 at left
            "Shaking her head, Sabia just threw up her hands. Kia put her paw down and cocked her head again, as if equally confused."
            "They stared at each other for a time, then Kia seemed to lose interest and wandered off. She didn't come back, leaving Sabia on her own."
            "Sabia headed back to camp, trying not to think about Kia playing with corpses."
            return
        "Sabia":
            $ A_kia += 0
            show sabiaemo normal at left
            "Kia nodded seriously as if this was a good answer. The earnestness of it made her smile, which just made Kia cock her head in confusion."
        "Ylva":
            $ A_kia += 1
            show kia pawtiltcurious at right with dissolve
            show sabiaemo happy1 at left
            "Sabia pointed to herself and declared that she was Ylva. Kia's eyes went wide and she stared in confusion for a long moment."
            show kia happy2 at right with dissolve
            kia "Not Ylva!"
            show kia pawtilteager2 at right
            "Kia released a curt growl that Sabia realized might be a laugh. She let out a sigh of relief, glad that she hadn't made a foolish mistake. After a moment, Kia pointed to the burning wagon."
            kia "Sabia!"
            show kia happy2 at right with dissolve
            "Normally that might have been creepy, but Kia didn't seem to be making a threat. No, judging from Kia's amused expression, she was just joking. Playing around with the new linguistic tools she'd been given."
            show sabiaemo happy2 at left
            s "Try that on Ylva next time. See what she does."
            "Kia didn't seem to understand, but gave another amused growl. Then her eyes lit up and she leapt to put her paws on Sabia's shoulders."
        "Kia":
            $ A_kia -= 1
            show kia irritated1 at right with dissolve
            show sabiaemo happy1 at left
            "Sabia pointed to herself and declared that she was Kia... and to her surprise, Kia released a low growl."
            "The Makhor lunged up, abruptly pinning Sabia back against a tree. Her claws pressed against Sabia's side, an uncomfortable reminder that Kia could tear her apart."
            show kia irritated2 at right
            kia "Sabia not Kiandhakhani."
            show sabiaemo surprised2 at left
            "Staring into those eyes burning with power, Sabia realized that she had misjudged Kia. The Makhor was a proud creature, and justifiably so."
            s "N-not Kia. It was just a joke. Sabia joking."
            show kia irritated1 at right
            "She was babbling broken sentences that Kia probably didn't understand. The Makhor continued examining her seriously."
            show kia normal1 at right
            show sabiaemo surprised1 at left
            "Then abruptly Kia leaned forward and licked her face. When she pulled back, there was no more of the dangerous ferocity."
    show kia happy2 at right with dissolve
    kia "Sabia sit!"
    show sabiaemo normal at left
    "Not one to contradict a Makhor, Sabia let Kia push her to the ground. They stayed together for a while, talking but not really talking. It was a strange sort of interaction, and Sabia was worried that more orcs would come, but the time passed without any further surprises."
    "The Makhor was surprisingly physically affectionate, often rubbing against Sabia. She didn't seem to care about her nakedness or consider it particularly sexual, but Sabia found herself discomforted. Usually she could ignore Kia's nudity, but when it was being rubbed against her like this..."
    show kia happy1 at right
    hide kia happy1 with moveoutright
    "Eventually Kia gave a lazy yawn and got off, stalking into the grasses. Apparently that was the end of their time together. Sabia got up more slowly, watching the Makhor as she vanished into the distance."
    "She headed back to camp slowly, thinking all the while."
    return

label KLkiaintro4:
    $ kiaprogression = 6
    $ kiacooldown = True
    scene bg countryside
    call sabiabase
    show kia happy1 at center
    show ylva normal at right
    show ylva2 arm2 at right
    with dissolve
    "Before Sabia could get out to the forest grove, she was met by Kia and Ylva coming in her direction. Kia greeted her, but seemed more interested in other things. Ylva, meanwhile, drew her aside and spoke in a low voice."
    show ylva openclosed3 at right
    ylva "Kia seems excited about this... I want to try to teach her as much as possible, but I'm afraid she'll lose interest if it's just boring lessons."
    show sabiaemo irritated2 at left
    s "What, you want me to make things exciting?"
    show ylva normal at right
    ylva "Just try to balance things, okay? Keep an eye on her mood and keep her engaged as long as possible."
    show sabiaemo normal at left
    s "Alright. I'll do what I can."
    "Was this really what she needed to do? Then again, Sabia reminded herself that this could be the difference between a murderous beast and a powerful ally. It couldn't be much worse than handling bored nobles..."
    "Ylva moved in front of Kia, raised a finger to her lips, and spoke softly."
    show ylva happy1 at right
    ylva "Kia? Hunt."
    show kia pawsorry at center with dissolve
    kia "Hunt!"
    show kia happy3 at center with dissolve
    "Kia dropped down into a seated position, much like a Makhor would naturally. Her eyes widened and her ears twitched in multiple directions."
    "When they started to move, Kia padded after them, shockingly silent. Sabia glanced back at her nervously, then toward Kia."
    show sabiaemo closed2 at left
    s "You sure she won't kill whatever we encounter?"
    show ylva normalnarrow at right
    ylva "...mostly sure. I used \"hunt\" to mean being silent before and she seemed to understand."
    show ylva normal at right
    show sabiaemo normal at left
    "They got closer to the camp, though not too close. Sabia led them to an open plain that was frequently traveled by those leaving camp. More importantly, it was at the bottom of a gradual slope, which had a cluster of trees perfect for watching below."
    show kia irritated1x at center
    "Before they were even fully settled, a group of orc raiders left the camp. They were laughing and shouting to one another, paying very little attention this close to home. Kia's eyes tracked them carefully and she bent lower, making Sabia fear that she might charge out at them."
    ylva "Kia, do you remember \"what?\" I tried to teach you. What are they?"
    show kia pawtiltcurious at center with dissolve
    "Kia looked up at her blankly. Not confused, but with a sort of uncertain amusement, as if this was a children's game and she was trying to decide whether or not to play."
    show ylva opennormal at right
    ylva "Those are orcs. Orcs."
    show ylva normal at right
    "Ylva repeated the word, then pointed to herself and repeated it again. At this, Kia shook her head, her mane of hair shimmering."
    show kia normal2 at center with dissolve
    kia "Not. Ylva {i}fsskit{/i}."
    "At first the last part sounded like a growl, but Sabia realized that it might be a word. Just not one she knew. Ylva frowned patiently and tried again."
    show ylva closedsad at right
    ylva "We explained this earlier, I thought you understood. What am I? I'm an orc. Same as them."
    show kia tilt1b at center with dissolve
    "Kia shook her head again. Ylva frowned, but Sabia had a glimmer of an idea. She caught Kia's attention, then pointed to Ylva."
    s "What? Fsskit."
    show kia happy1 at center with dissolve
    "Kia nodded agreement, so Sabia pointed at the band of orcs moving away."
    s "What?"
    show kia happy2 at center
    show ylva surprised at right
    show sabiaemo surprised1 at left
    kia "Food!"
    "The word was plain as day. Ylva's eyes widened and she took a quick breath, but she remained calm."
    kia "Food eat. Ylva, not eat."
    show ylva closedhappy at right
    show sabiaemo normal at left
    ylva "So I'm... not food."
    show kia happy1 at center
    kia "Not food."
    show ylva normal at right
    ylva "I'm... you said \"fsskit\"? What's that?"
    show kia uncertain1 at center
    "Kia stared back at her, puzzled, then gave a small growl of irritation. But a moment after that, she jumped up, put her paws on Ylva's shoulders, and began rubbing their faces together while releasing a rumbling growl."
    show kia happy2 at center
    kia "{i}Fsskit{/i}."
    "Ylva didn't pull back, instead touching Kia's hair gently. But over the Makhor's shoulder, she shot Sabia a confused glance."
    show sabiaemo happy1 at left
    s "I think I understand. Kia doesn't classify things the same way we do. It's... by function, not category."
    ylva "That seems like a very confusing way to view things."
    s "Not to her. I saw this a bit on the western front, actually - minotaurs don't think categorizing things into theoretical boxes is logical."
    show kia happy2 at center
    "Apparently ignoring them, Kia was still happily rumbling and rubbing against Ylva. Now that she had vocalized her theory, Sabia decided to give it another try."
    show sabiaemo normal at left
    s "So, Kia... orcs food. Ylva not food. But Ylva orc."
    show kia tilt1 at center with dissolve
    "Kia stared at her curiously. With enough pointing and repeating, however, Kia did seem to grasp the concept. Hopefully that meant they'd have less trouble in the future and could actually teach her something."
    "But though Kia seemed to understand the idea of abstract categories, it didn't seem to interest her. Sabia considered carefully how they could teach her while keeping her interested."
    $ KLkiainterest = 2
    if A_kia >= 3:
        $ KLkiainterest += 1
    call KLkiateaching
    return

label KLkiateaching:
    show ylva normal at right
    show sabiaemo normal at left
    if KLkiainterest > 3:
        $ KLkiainterest = 3
    if KLkiainterest == 3:
        show kia happy2 at center
    elif KLkiainterest == 2:
        show kia happy1 at center
    elif KLkiainterest == 1:
        show kia normal1 at center
    elif KLkiainterest == 0:
        show kia neutralE at center
        "Kia seemed restless, looking elsewhere as if she was starting to consider this uninteresting and beneath her."
    else:
        $ A_kia -= 1
        $ A_ylva -= 1
        show kia happy1 at center
        "Kia abruptly planted her paws on Ylva's shoulders and licked her face. She did the same to Sabia - and then she was off like a shot, vanishing into the distance."
        hide kia happy1 with moveoutright
        s "Guess we should teach her \"hello\"and \"goodbye\", huh?"
        show ylva sad at right
        ylva "I was hoping we wouldn't run her off, but..."
        call KLteachingdone
        return
    menu:
        "Teach Kia about catgirls" if KLcatgirls == False:
            $ KLcatgirls = True
            $ KLkiainterest -= 1
            $ KLlessons += 1
            if catgirlstatus == "enslaved":
                "At that moment, a small group of catgirls passed nearby. What the hell were they doing wandering free like that? Sabia knew that some had been given other tasks, but she disliked that she wasn't in charge of the whole process. Then again, wrangling them might have been more of a pain than she wanted to deal with."
            elif catgirlstatus == "free":
                "At that moment, a small group of catgirls passed nearby, chatting happily with one another. It surprised Sabia, but the catgirls seemed to have taken to life here."
            elif catgirlstatus == "recruited":
                "At that moment, a small group of catgirls passed nearby. It surprised Sabia, but the catgirls seemed to have taken to life here."
            else:
                "At that moment, a small group of catgirls passed nearby. As they left the orc camp, their ears perked up a little more, but it didn't look like they were going to run away."
            "In any case, this gave her a good opportunity to teach Kia another word. Ylva beat her to it."
            ylva "Catgirls."
            show kia happy1 at center
            kia "Catgirls."
            show ylva happy1 at right
            ylva "Good! What are catgirls?"
            show kia pawtiltcurious at center with dissolve
            kia "Catgirls {i}yrrkit{/i}."
            show ylva normal at right
            ylva "I'm sorry, we don't understand your words. Are catgirls {i}fsskit{/i}?"
            show kia pawtilteager2 at center
            kia "Not {i}fsskit{/i}. Catgirls sit. Not eat."
            s "I think we're going to have to accept that she wants to use some of her own words."
            show ylva happy1 at right
            ylva "I think it's real progress. We're much closer to communication."
            show kia happy2 at center with dissolve
            "At the moment, though, Kia seemed to have very little attention for them. She kneaded her paws in the ground with a low rumble that sounded somewhat happy."
        "Teach Kia about humans" if KLhumans == False:
            $ KLhumans = True
            $ KLkiainterest -= 1
            $ KLlessons += 1
            "Given how Kia approached categories, Sabia wasn't sure about teaching her the concept of \"human\". She pointed to herself."
            s "Human."
            show kia pawuncertain1 at center with dissolve
            kia "Orc?"
            s "Uh, the word is like orc. Humans are food?"
            show kia pawtilteager2 at center with dissolve
            kia "Eat!"
            ylva "Sabia is human. You don't eat Sabia."
            show kia happy2 at center with dissolve
            kia "Humans eat! Sabia sit!"
            ylva "Is Sabia... {i}fsskit{/i}?"
            show kia tilt1 at center with dissolve
            "That made Kia pause, cocking her head as if considering the question. After a moment, she made a chuffing sound and shook her head strangely. Not exactly a denial."
            show kia happy4 at center with dissolve
            kia "Sit. Not eat."
            show sabiaemo happy1 at left
            s "Haha, well, at least I'm not food."
            show kia happy1 at center
            kia "Humans food. Sabia human. Sabia not food. Food eat. Sabia sit."
            show ylva happy1 at right
            ylva "She really does understand quite a lot, now that she's starting to comprehend our way of thinking."
            "Though she seemed slightly proud of herself, Kia also no longer seemed interested in the subject."
        "Teach Kia about elves" if KLelves == False:
            $ KLelves = True
            $ KLkiainterest -= 1
            $ KLlessons += 1
            "Sabia wanted to include elves in their lessons, but they didn't have many options. Fortunately, eventually she spotted Alioch walking swiftly in the distance - Vehlis must have sent him on some errand."
            "She thought that he might be too far away, but when Sabia pointed in his direction, Kia just looked without squinting. Perhaps her eyes were much better than a human's."
            s "Elf."
            show kia happy2 at center with dissolve
            kia "Elf!"
            ylva "And what do you do with elves?"
            show kia normal2 at center
            "This made Kia pause, but she didn't seem confused. More like this question required some thought."
            kia "SitEat. Elf eat. Elf sit."
            show ylva closednormal at right
            ylva "She decides on a case by case basis, then?"
            s "Maybe. But she said orcs were food, and yet you're an exception there."
            show kia happy2 at center
            kia "Ylva {i}fsskit{/i}."
            show ylva normalnarrow at right
            ylva "I can't say I know any stories about Makhor and elves in particular. How odd."
            s "Maybe there's something else there, or I suppose it might be particular to Kia."
            "In any case, it was obvious they weren't going to resolve that question anytime soon, and Alioch was already out of sight."
        "View strange band of orcs" if KLlessons >= 3 and KLshamans == False:
            $ KLshamans = True
            $ KLlessons += 1
            $ KLkiainterest -= 2
            "Another band of orcs left the camp and Sabia ignored them, since it would just be more of the same lesson. Ylva's gaze flickered to them, but she seemed to think the same. Still, she seemed to want to take this as a lesson."
            ylva "Orcs - eat?"
            show kia angry3 at center
            kia "KILL."
            show ylva surprised at right
            show sabiaemo surprised1 at left
            "The word was spoken with such savagery that Sabia recoiled immediately, her body reacting on instinct to the threat. Ylva felt the same and moved back as well, but her eyes were especially wide."
            ylva "I... I didn't teach her that word..."
            show sabiaemo closed2 at left
            s "It wasn't me, but shouldn't we be more worried that she might charge them now?"
            show kia irritated1x at center
            "Fortunately, though Kia continued to stare pure hatred toward the orcs, she showed no signs of charging. Instead, she settled lower into the grass, eyes still burning."
            kia "Kill."
            show ylva closedsad at right
            ylva "Well... I think if she wanted to kill them now, she'd just do it. So we're safe for now."
            show sabiaemo irritated2 at left
            s "But why those orcs? What's different about them?"
            show ylva normal at right
            ylva "They're not from Groknak's tribe - they were visitors who came for the Red God's Arena. I'm not sure why they'd make Kia so angry."
            "Frowning, Sabia did her best to commit the specific orcs to memory. They didn't seem to be going far, instead searching for something near camp. Not so suspicious, but she resolved to look into the matter later."
            show kia normal1 at center
            "Kia slowly calmed down and the light faded from her eyes. Ylva sat nearby and spoke soothingly to her, which seemed to help. Eventually Kia's ears perked up more happily and she cocked her head again, looking at them curiously."
        "Take a break to eat" if KLfoodbreak == False:
            $ KLfoodbreak = True
            $ KLkiainterest += 1
            "Seeing that Kia's interest was waning, Sabia signaled that they should take a break to eat the food they'd prepared."
            show kia happy3 at center
            "It was too risky to make a fire this close to camp, but that was why she'd cooked the meat beforehand. Ylva had also brought a bloody slab of meat that Kia happily tore into, adding a new shade of crimson all over her face."
            "When they were done, Kia happily licked off the blood on her paws. She then brushed one paw against her face... but it was more than that. There was a shift of subtle magic that seemed to wipe away the blood."
            s "What kind of magic is that? Is it magic at all?"
            show ylva openclosed1 at right
            ylva "It's part of her nature, at the deepest level. I don't think she considers magic as any different than one of her other senses."
            show sabiaemo happy1 at left
            s "Sounds like you've been giving that some thought."
            show ylva happy1 at right
            ylva "I was curious too, so I've been observing her carefully."
            show kia happy2 at center
            "They might have said more, but Kia had hopped up and was looking at them expectantly. She seemed pleased after the meal, so perhaps she was ready for some more conversation."
        "Take a break to sit" if KLsitbreak == False:
            $ KLkiainterest += 1
            $ KLsitbreak = True
            "Seeing that Kia's interest was waning, Sabia signaled that they should relax for a while and not try to learn any more words."
            if A_kia >= 4:
                $ KLkiainterest += 1
                $ A_ylva += 1
                show kia happy2 at center
                "Sabia found herself surprisingly comfortable with Ylva. Working together to help Kia bonded them in more ways than one."
                "On top of that, Kia didn't seem to mind them talking. She just watched them with a look that swung between curiosity and lazy satisfaction, and occasionally rubbed up against them."
            else:
                $ A_ylva += 1
                show kia tilt1 at center with dissolve
                "It didn't go quite as smoothly as she'd hoped, with Kia staring at them when they tried to talk and occasionally rubbing against Ylva."
                "She found herself surprisingly comfortable with the orc woman, though. Working together to help Kia bonded them in more ways than one."
        "Let Ylva teach":
            $ KLkiainterest -= 1
            $ KLlessons += 1
            show kia pawtiltcurious at center with dissolve
            if KLfirstlesson == False:
                $ KLfirstlesson = True
                "Ylva took a while to go over words that she had been trying to teach Kia. Simple, useful words - Sabia approved. It might be insulting to compare Kia to a dog, but it reminded her of obedience training: it didn't make sense to start with abstract concepts."
                "Though Kia was obviously much smarter than that, her mind was also focused on things important to survival, like food. Making those clear was essential to communicating effectively with her."
            else:
                if KLlessons >= 3:
                    "Since Kia seemed to understand most of the simple words, Ylva started using them in more combinations. Kia proved surprisingly good at this. She might not have human grammar, but she seemed to understand the concept of words as more than just names."
                else:
                    "Ylva took some time to go over the words they had been learning."
            "Though it was obvious that Ylva had more she wanted to cover, Kia started to grow uninterested after a while and so Ylva eased off."
        "Finish":
            $ A_kia += 1
            "When Sabia glanced at the sky, she was surprised how much time had passed. Kia stretched her body and let out a long yawn, then looked at them. She didn't seem annoyed, but Sabia wondered if she was nearing her limit. Ylva traded a glance with her and nodded."
            ylva "Okay, Kia. I think that's enough for today. We're done."
            show kia neutralE at center
            kia "Goodbye?"
            show ylva happy1 at right
            ylva "So you {i}did{/i} learn that one... yes, Kia. Goodbye for now."
            show kia normal1 at center
            show ylva normal at right
            "Kia's head swung to look at Sabia, slightly stern, as if expecting Sabia to say something. It clicked for her the next second."
            show sabiaemo happy1 at left
            s "Goodbye."
            show kia happy2 at center
            kia "Goodbye!"
            hide kia happy2 with moveoutright
            "That said, Kia was off like a shot, disappearing into the distance. Sabia took the moment to stretch herself, sore after spending so long in one place."
            call KLteachingdone
            return
    jump KLkiateaching
    return

label KLteachingdone:
    if KLlessons >= 5:
        $ A_ylva += 2
        show ylva happy1 at right
        ylva "That was very well done, Sabia. I'm glad you held her interest so long."
        s "I didn't do much. She likes you better, anyway."
        ylva "Maybe, but it's good to have someone else's perspective. You helped us take major steps forward today."
        s "Hopefully once she understands more, she'll be more interested."
        show ylva normal at right
        "Ylva murmured assent, but seemed to be lost in thought. Since she seemed inclined to stay, Sabia nodded to her and then headed back to camp. Though she'd spent most of the time just sitting, it had been a good day of work."
    elif KLlessons >= 2:
        $ A_ylva += 1
        show ylva closedsad at right
        ylva "I suppose we made more progress than before. Thank you, Sabia."
        s "Just keep doing what you can with Kia, alright?"
        "Sabia headed back to camp, wondering just where all this was going to take her."
    else:
        $ A_ylva -= 1
        show ylva angry1 at right
        ylva "I had really hoped to teach her more. This was poorly handled."
        "She wasn't addressing Sabia directly with that, but it still sounded like a reproach. Sabia scowled, but decided not to take the bait."
        s "We'll try again next time."
        "Sabia headed back to camp, wishing that she could have managed things better, but also vaguely irritated at the Makhor."
    return

label KLmaplyconvo:
    scene bg countryside
    call sabiabase
    show maply 1 at right
    show maplyemo normal at right
    with dissolve
    s "Maply... do you know anything about the Makhor?"
    show maplyemo eyebrows at right
    maply "Wow, you're always straight into serious stuff... I don't know very much. I mean, you just saw one in the arena, right? You probably know more than me."
    s "No, I'm interested in if catgirls have any stories or legends about them. Or rumors - anything like that."
    show maplyemo normalopen at right
    maply "Well, uh, there are some. You've heard about how catgirls were the first people to walk on this continent, right?"
    show sabiaemo closed2 at left
    "Absurd propaganda, Sabia had always assumed, but she held her tongue about that. They weren't recent arrivals and they might know something."
    s "I've heard the stories. They have to do with the Makhor?"
    show maplyemo normal at right
    maply "They say that the Makhor were here even before we were. There were even a few groups that worshipped them, though most treated them as just dangerous neighbors."
    show sabiaemo normal at left
    s "Neighbors? There were more of them?"
    show maplyemo happy at right
    maply "No, they were always rare. But in the legends, if a Makhor lived near a catgirl tribe, they would leave out offerings. And in return, it wouldn't harm the tribe."
    show maplyblush at right
    maply "And, umm... there are stories about Makhor taking away catgirls or even males to umm... play with. It was apparently an honor. But those are... I don't know if those stories are true..."
    s "Hmm. Do you know of any catgirl tribes that still have a connection like that with a Makhor?"
    show maplyemo normal at right
    hide maplyblush
    maply "I don't think so. Our caravans move around so much these days, there wouldn't be a chance. I've only heard stories."
    s "That's good to know. Thank you, Maply."
    "Sabia turned those new facts over in her mind thoughtfully. Nothing she could use immediately, but possibly useful for the future."
    return

label KLbonequest:
    $ kiaprogression = 7
    $ kiacooldown = True
    scene bg countryside
    call sabiabase
    with dissolve
    $ kiabonequest = True
    "Sabia made another attempt to meet with Kia, but found no one in the usual clearing. Just as she was starting to head back, irritated at the time wasted, she caught a glimpse of a fleeting shadow."
    show kia normal1 at right
    "That was her only warning before Kia showed up behind her. She seemed quieter than usual, sniffing at Sabia thoughtfully. After a moment, her tail slid back into a more relaxed position."
    kia "Sabia come."
    s "Come? Where are we going?"
    show kia tilt1 at right with dissolve
    kia "Sit."
    hide kia tilt1 with moveoutright
    "With that pronouncement, Kia moved away. She quickly opened a lot of distance between them, then looked back as if not sure why Sabia was so slow in following. Deciding she had to see where this went, Sabia jogged after her."
    "They hiked out of the depression, the Makhor setting a blistering pace that didn't seem to be taxing her at all. They took a curving route away, Sabia doing her best to keep up the pace."
    show sabiaemo closed2 at left
    "Eventually, though, she tripped and had to stagger to a halt to avoid falling. She took a moment to catch her breath and ease her aching legs. Though she was in good combat shape, it had been a long time since she'd marched like this."
    show kia pawtiltcurious at center with moveinright
    "Kia moved beside her and watched silently. There was something odd in her gaze, a sense of superiority that rubbed Sabia the wrong way. But abruptly, Kia grinned."
    show kia pawtilteager1 at center
    kia "Sabia small. Kia help."
    show sabiaemo sad1 at left
    s "What is... that supposed to mean?"
    show kia pawtilteager2 at center
    "Kia cheerfully put a paw on Sabia's head, roughly smoothing back strands of hair."
    kia "Sabia small."
    show kia happy1 at center with dissolve
    show sabiaemo normal at left
    "It was strange and maybe a little condescending, but Kia seemed to be speaking warmly. And Sabia decided that, compared to the Makhor's real body, she was indeed pretty small. It made her wonder exactly what Kia thought of them and what her words meant."
    "Once Sabia had recovered, she followed Kia again. This time Kia didn't go quite as fast, but Sabia forced herself to increase the pace and not trip. Maybe it was just a pride thing... but she also didn't want to look weak in front of a predator."
    "Eventually they reached a hilly area and Kia seemed to get more excited. She darted forward, disappearing for a while, then returned and gave a barking growl. Maybe they were almost there, then."
    "When Sabia followed, she discovered that there was a small cave hidden in the hills. She noted that their curved route had actually taken them a little closer to the orc camp, but further from any human settlements and major roads."
    scene bg cave
    call sabiabase
    show kia happy1 at center
    show ylva normal at right
    show ylva2 arm2 at right
    with dissolve
    "The inside had the same wild smell as Kia. Most notably, Ylva was there, but Sabia scanned the rest of the room. There was a pile of bones that had been cracked open by strong jaws - mostly animal, but some humanoid skulls as well. There was a pile of what might have been grass in one corner of the cave, and a deeper area in shadows that Sabia couldn't see."
    show ylva happy1 at right
    ylva "Oh, Sabia. I'm glad Kia brought you here too."
    s "Did you know about this place?"
    show ylva normal at right
    ylva "I think this was her real hideout. She might have been meeting us in the other location as a... precaution."
    "That was sensible, so it didn't bother Sabia much. Plus, the fact that the Makhor trusted her enough to show her this place was a sign that she was making progress."
    show sabiaemo happy1 at left
    s "So this is your home, Kia? It seems nice."
    show kia happy2 at center
    kia "Kia sit."
    show kia normal1 at center
    show sabiaemo normal at left
    "There was something serious in her eyes, though. She walked further into the cave, looking back at her expectantly. Ylva closed her eyes and nodded for her to go, so Sabia followed quietly."
    "In a shadowy room of the cave, Sabia found more bones... much bigger bones. She was puzzled for only a moment before she recognized some of them as bones that had been in the arena. Makhor bones."
    show sabiaemo surprised1 at left
    s "Kia... these are the bones of the other Makhor? You're... gathering them?"
    show kia pawsad1 at center with dissolve
    show sabiaemo normal at left
    kia "Kia... {i}fsskit{/i}."
    show kia neutralE at center with dissolve
    show sabiaemo closed2 at left
    "Crouching down, Kia picked up one of the bones and pressed her face against it, giving a low whine. Sabia heard a few sounds that might have been words, but they dissolved into a low croon of raw animal pain. Kia bent lower over the bones, stroking them gently."
    ylva "I talked to her earlier and tried to get a clear story out of her. I'm not sure if these bones belonged to a friend or a mate or something else, but it was someone Kia knew."
    show sabiaemo sad1 at left
    s "Which was why she wanted to protect them?"
    ylva "Yes. I'm not sure what she wants - not to bury them, I tried - but I'm pretty sure she wants to do something to memorialize her friend."
    show kia irritated1 at center
    kia "Not {i}fsskit{/i}. Orcs. Food danger! Kia small. Hurt."
    show kia irritated1x at center
    kia "Orcs kill."
    "The words tumbled out, not quite making sense, but there was so much fury in the final words that Sabia didn't dare question her. Ylva spoke softly beside her."
    ylva "They tricked her into believing the bones were her friend, something to do with the scents, and that was when she was poisoned."
    show kia pawsad1 at center with dissolve
    "Kia settled into the pile, her fury turning to sadness. She looked up at Sabia and released a low growl that might have included words, but it was too difficult to make them out."
    ylva "I think she wants our help to gather them."
    show sabiaemo closed2 at left
    s "I think I understand that, but what can we do?"
    if RGAwonbone:
        $ A_kia += 1
        $ kiabones += 1
        $ Inventory.add_item(Makhorbones,1)
        show kia happy2 at center with dissolve
        show sabiaemo normal at left
        "Abruptly Kia sat up alertly, eyes flickering around the pile. She grabbed up a bone, leapt forward, and thrust it in Sabia's face."
        kia "Sabia help!"
        "For a moment Sabia was confused, but then Sabia recognized the bone as the one she had earned in the Red God's Arena... and given back to Kia. The Makhor was smiling at her now, and Sabia couldn't help but smile back."
    else:
        show kia normal1 at center with dissolve
        show sabiaemo sad1 at left
        "Abruptly Kia shifted forward, focusing on them again. She pointed to the bones insistently."
        kia "Help. Give."
    show sabiaemo normal at left
    s "Okay... I'll keep my eyes open, Kia."
    show kia normal1 at center with dissolve
    "Kia nodded seriously, then pushed them back into the main room of the cave. Once there, her sorrow was replaced with some of her usual energy."
    show kia happy4 at center
    kia "Sabia good. Ylva good. Small help."
    s "What do you think she means by th-"
    show kia happy2 at center
    kia "Sit!"
    hide kia happy2 with moveoutright
    "Kia pushed them down near the pile of grass, then rushed out of the cave."
    show ylva closednormal at right
    ylva "I'm not sure. I... think that she wants to take care of us because we're small and can't hunt."
    show sabiaemo irritated2 at left
    s "Like we're baby Makhor or something? Maybe, but it could also be pride. She doesn't want to be in our debt."
    show ylva normal at right
    ylva "Yes, that's also possible."
    show sabiaemo normal at left
    show kia happy2 at center with moveinright
    "In any case, Kia was now dragging what appeared to be most of the corpse of a cow into the cave with a cheerful look on her face."
    "They roasted and ate it together, the atmosphere staying light. But Sabia occasionally found her gaze wandering to the other room of the cave and thinking about the bones within."
    "If she wanted the Makhor on her side, she'd need to collect those bones."
    return

label KLelmyscene1:
    scene bg silvertusk
    call sabiabase
    show elmy normal at right
    with dissolve
    s "Elmy... do you know anything about a poison that could be used against a Makhor?"
    show elmy happy2 at right
    elmy "I... that's an odd question."
    s "Well? Do you?"
    show elmy normal at right
    elmy "They didn't trust me to be involved with the Makhor in any way. But... I have noticed some strange patterns with ingredients bought from the bar."
    elmy "If you want to use a normal poison on a truly large beast, there are certain ingredients that can be used to increase the intensity and make sure it spreads over a large body."
    s "Hmm. Could a technique like that be used to make an antidote to that kind of poison?"
    show elmy angry1 at right
    elmy "What... what exactly are you planning?"
    s "If the orcs try to control a creature to use in combat, I want to have some kind of counter."
    show elmy normal at right
    elmy "I see... it's not impossible, but it won't be easy to find all the ingredients."
    s "I have bigger concerns than running errands - can I pay you to put it together?"
    elmy "With one condition, I would do it for 110 Lundils. But I need you to come along with me to gather one particular ingredient."
    s "What, is it somewhere dangerous?"
    show elmy angry1 at right
    elmy "It shouldn't be, but there are rumors in the bar that some orcs have disappeared in that area. I'm not willing to risk my life for this."
    s "Alright, fine. I'll go along with you and pay the money if you can handle this for me."
    return

label KLelmyscene2:
    $ kiacooldown = True
    $ KLelmypotion = True
    scene bg countryside
    call sabiabase
    show elmy normal at right
    with dissolve
    "After Sabia gave Elmy the payment, which was deposited with Jadk, they headed out of camp. Usually Sabia explored north or northwest, since her goal was to approach Lundar, but this time they traveled east."
    "Elmy set a brisk pace and seemed determined to get things over with as soon as possible, resisting any attempts to talk. Sabia decided that she could accept that and followed quietly."
    "Though she didn't have the full story, she knew that the orcs had used some kind of poison on Kia to weaken and confuse her. That was how they had been able to capture her, and try to use her for their own purposes. Sabia wanted to prevent that from ever happening again."
    "And if it also helped Kia - well, Sabia wasn't going to pretend she wasn't fond of the Makhor."
    "They arrived at their destination, a broad plain that didn't look too different to Sabia. Lots of fields of wildflowers mixed with tall grasses."
    elmy "The ingredient looks like those white clovers, but has seven leaves. Keep guard, but help me look if you can."
    show sabiaemo closed2 at left
    "Sabia bristled at being commanded, but held her tongue. She needed Elmy to do this, after all, and there was no question who was really in charge."
    show sabiaemo normal at left
    "Letting the catgirl search through the flowers, Sabia turned away and scanned the fields lazily. She doubted she could identify the right flower anyway, so best to just keep watch for any potential threats."
    "Had Elmy bought her story about the reason she needed the antidote? Sabia thought she had, but wasn't quite sure. That could potentially be a liability - Elmy might be no friend to orcs, but she could still betray Sabia accidentally or under torture."
    "She'd need to change the plan based on circumstances, but Sabia tried to decide which course was best."
    menu:
        "Trust Elmy with the secret":
            $ sub += 1
            $ freedom += 1
            show sabiaemo closed1 at left
            "It would be foolish to tell Elmy everything, but Sabia decided that it wouldn't be so bad to give Elmy more information if necessary. She might be a good ally in this."
        "Stick with the plan":
            show sabiaemo closed2 at left
            "Sabia shook her head and resolved to just stick with the lie for now."
        "Eliminate Elmy when possible":
            $ dom += 1
            $ slavery += 1
            show sabiaemo closed2 at left
            "Narrowing her eyes, Sabia considered her options for removing Elmy. She might have her uses now, but once Sabia had enough resources, it might be better to make sure she could never say anything."
    show sabiaemo surprised1 at left
    "Sabia's thoughts were interrupted by a cry of fear from Elmy. Her hand flew to her weapon and she shifted into a combat stance as she turned toward the sound..."
    show elmy sad1 at right
    show kia happy3 at center
    with dissolve
    "And discovered Kia crouched over a fallen Elmy."
    show sabiaemo normal at left
    "Elmy's eyes were wide with shock and she seemed frozen, prey in the sight of a predator. Kia, meanwhile, was baring her teeth in a fearsome smile, but one that Sabia didn't think was dangerous..."
    show kia happy2 at center
    kia "Who?"
    show kia pawtilteager2 at center with dissolve
    "Elmy just stared back, unable to answer. Kia cocked her head, waiting for an answer, her tail swishing back and forth playfully."
    "Getting no answer, Kia easily picked Elmy up by the shoulders and held her up in Sabia's direction."
    kia "Sabia! Who?"
    s "Uh... Elmy. That's Elmy. Can you put her down and stop scaring her? She's here to help."
    show kia tilt1 at center with dissolve
    show elmy normal at right
    "This shot all her plans to hell, but Sabia decided she would just have to improvise. Kia considered her words impassively, while Elmy seemed to calm down a little, her mind engaging with the situation."
    elmy "You... is this really the...?"
    show kia happy1 at center with dissolve
    kia "Elmy. Catgirl. {i}Yrrkit{/i}. Not food."
    "While she declared things, Kia set Elmy down and began sniffing over her. She seemed especially curious, pulling at Elmy's frilly clothes. She nearly tugged off the catgirl's top, leading Elmy to yelp and pull it back into place. That seemed to pierce through her shock."
    show elmy sad2 at right
    elmy "Then you must be... I don't know what to thi-"
    show kia happy2 at center
    kia "Elmy! Sit!"
    show elmy sad1 at right
    "Kia dropped to the ground and tugged Elmy into her lap. She began to slide her paws through Elmy's hair, smoothing out the tangles. Sabia blinked as she watched them. It reminded her of animals grooming each other... or someone petting a favored animal."
    show kia happy4 at center
    kia "Not eat Elmy. Sit good."
    show elmy normal at right
    "Though Elmy still looked uncomfortable to have the huge paws on her, she had regained most of her usual composure."
    elmy "This is the Makhor, Sabia? I... won't ask how all this came about."
    show sabiaemo eyebrow1 at left
    s "Good, because I won't answer. I trust you'll keep this a secret?"
    show elmy sad2 at right
    elmy "Doesn't look like I have much of a choice."
    show sabiaemo happy1 at left
    s "Actually, it seems she likes you."
    show kia happy2 at center
    show elmy happy2 at right
    show sabiaemo normal at left
    "Kia ignored them, continuing to pet Elmy while growling happily. Even after the catgirl no longer looked frazzled from the fright, Kia kept touching her hair and occasionally catching her tail to stroke it."
    show elmy happy1 at right
    elmy "So you wanted the antidote in case someone tries to control her again?"
    s "That's right. I didn't anticipate this would happen, but... she has a mind of her own."
    show elmy happy3 at right
    elmy "Well, if you keep her from eating me or carrying me off, I'll help you. I didn't like seeing them hurt her either."
    show kia pawtiltcurious at center with dissolve
    kia "..."
    show kia pawtilteager2 at center
    kia "Elmy good!"
    show elmy happy1 at right
    s "Can you let her go? Elmy needs to gather ingredients to help you, and she needs to go back home."
    show kia tilt2 at center with dissolve
    "Kia stared at Sabia for a while, then reluctantly let Elmy go. The catgirl sprang up a bit too quickly, but once a short distance away, stopped and gave a polite curtsy."
    show elmy happy3 at right
    elmy "Nice to meet you, Lady Makhor."
    show kia happy2 at center with dissolve
    kia "Kia!"
    show elmy happy2 at right
    elmy "Kia... will you let me do my work now?"
    show kia tilt1 at center with dissolve
    show elmy happy1 at right
    "Kia cocked her head and just watched, but didn't pounce as Elmy slowly tried to get back to her task. Sabia drew closer just in case something might happen, but things proceeded quietly. Elmy nervously gathered ingredients while Kia watched her with bright eyes."
    "Had the Makhor kept catgirls as pets or something? Or did they have some other manner of animal kinship? Sabia wasn't sure what to make of it."
    "In any case, her plans were out the window, but her goal had been accomplished. In the future, she'd have a defense against anyone trying to control Kia."
    show kia happy2 at center with dissolve
    show elmy normal at right
    "Elmy tried to finish her work and get away smoothly, but Kia pounced on her before she could leave, stroking her hair some more before finally letting her go. After a while, the two of them finally headed back, Kia following part of the way as a rustle in the grass."
    hide kia happy2 with moveoutright
    s "Just what do you make of that?"
    show elmy sad1 at right
    elmy "I am... not sure. There are stories of Makhor, but I had always dismissed them as just stories..."
    s "Well, if you betray either of us, you'll live to regret it."
    show elmy normal at right
    elmy "I won't."
    "Elmy looked over her shoulder, searching for Kia, but the Makhor had fallen back when they got closer to the orc camp. But something in her expression made Sabia believe her."
    "For now, she left Elmy to brew the potion, since it would apparently take some time. Sabia decided to be glad things hadn't turned into a disaster and focus on her other work."
    return

label KLlutvrogmeeting1:
    $ kiaprogression = 8
    $ kiacooldown = True
    scene bg countryside
    call sabiabase
    with dissolve
    "When Sabia left the camp and headed out to meet Kia, she had a strange feeling. Was she being followed? She circled to shake them, but didn't spot anyone. That was when she realized that someone was moving ahead of her."
    "It wasn't that someone was following her, it was that they were moving in the same direction. A coincidence, most likely, but Sabia still didn't like it. She began to pursue them, though from as much of a distance as she could manage."
    "Whoever it was, they moved very carefully and she never caught sight of them. Strangely, though, they seemed to be zeroing in on Kia's territory. Sabia found herself playing with the hilt of her weapon as she pursued."
    "As they got closer, the person ahead of her started moving slower and Sabia became concerned they were actually hunting Kia. She wanted to close the distance and see who it was, but was afraid they'd notice her."
    "Then she heard a loud growl and realized that it was too late. Sabia scrambled forward, bursting out of a cluster of trees and stumbling straight into the scene."
    scene bg countryside
    show lutvrogbase at right
    show lutvrogaxe at right
    show lutvrogwraps at right
    show lutvrogwrists at right
    show lutvrogemo suspicious at right
    show kia angry5 at center
    with dissolve
    "Kia and Lutvrog faced off a short distance away. Kia's claws were out and her eyes blazed, while her tail lashed dangerously. By contrast, Lutvrog was completely still. He was always serious, but now she saw deadly focus in his eyes."
    "How the hell had Lutvrog found her? Especially since he hadn't been following her... Sabia realized that it didn't matter. She had only a split second to act before they attac-"
    "Kia lunged forward, nearly a blur. As soon as she got into range, Lutvrog's axe came down in a brutal chop."
    "Kia swiped it aside, then her other paw came up, slashing across Lutvrog's chest and drawing a little blood. Sabia was shocked that he didn't try to dodge or block - then realized why a second later."
    "Lutvrog shifted his axe and parried Kia's tail, which stabbed out toward his neck. A moment later he reversed his grip, slamming down and striking Kia on the side of the head."
    show kia angry3 at center
    "She dropped back onto all fours with a snarl, eyes burning. Lutvrog shifted his grip slightly. There was a brief pause while they eyed one another, and Sabia realized this was her chance to act."
    menu:
        "Stand back and watch":
            $ sub += 1
            "Though she wanted to intervene, Sabia had no idea what would actually accomplish what she wanted. That made her hesitate, and the hesitation lasted long enough that she missed her chance."
            "Lutvrog and Kia exchanged another brutal set of blows that left both of them bleeding. Just when they were about to assault one another again, Kia's ears twitched."
            show kia irritated1x at center with dissolve
            kia "Sabia! Danger!"
            call sabiabase
            with moveinleft
            show sabiaemo surprised2 at left
            s "Wait, no! You don't need to fight him!"
        "Try to stop Kia":
            call sabiabase
            with moveinleft
            "Sabia ran closer, making both fighters hesitate. She quickly focused on Kia, raising her hands desperately."
            show sabiaemo surprised2 at left
            s "Kia, wait! He's not an enemy!"
            if A_kia >= 5:
                $ A_lutvrog += 1
                show kia tilt1 at center with dissolve
                "Kia looked at her with an odd expression, but shifted back. Unfortunately, Lutvrog stepped forward into the gap. Sabia opened her mouth to shout him down too..."
            else:
                show kia angry3 at center with dissolve
                "Kia's gaze flickered to her, but her eyes stayed hard. Sabia tried to think of something else to say to get through to her..."
        "Try to stop Lutvrog":
            call sabiabase
            with moveinleft
            "Sabia ran closer, making both fighters hesitate. She quickly focused on Lutvrog, trying to show her conviction in her eyes."
            show sabiaemo surprised2 at left
            show lutvrogemo normal at right
            s "Lutvrog, wait! She's not an enemy!"
            if A_lutvrog >= 5:
                $ A_kia += 1
                show lutvrogemo sad at right
                "Lutvrog looked at her thoughtfully and his axe lowered just slightly. Sensing weakness, Kia shifted forward. Sabia opened her mouth to try to stop her..."
            else:
                show lutvrogemo suspicious at right
                "Lutvrog looked at her, but she saw suspicion in his eyes. He didn't shift his stance at all, and Kia tried to think of a way to convince him before Kia attacked..."
    show kia angry3 at center with dissolve
    show sabiaemo surprised3 at left
    "But it was too late. The two fighters threw themselves at each other and Sabia despaired... except this clash was different."
    "They attacked fast, but some of the lethal edge had gone. Lutvrog was playing defensively now, and Kia had a chance to claw at his eyes that she didn't take."
    "This time they didn't back down, striking at one another in a furious exchange of blows until finally both retreated. Lutvrog still looked suspicious, but Kia sat down and gave a strange nod."
    show sabiaemo normal at left
    show kia happy1 at center
    kia "Not food."
    show lutvrogemo normal at right
    "At this, Lutvrog sighed slightly and shifted to rest his axe on his shoulder. He was bleeding slightly from the scratches on his chest, but didn't seem to notice. Instead, his focus was on Sabia, eyes demanding an explanation."
    s "Okay... good... can you two not attack each other again?"
    show kia happy2 at center
    kia "Orc who?"
    show lutvrogemo normalopen at right
    lut "Lutvrog needs a good explanation for this, Sabia."
    show sabiaemo closed2 at left
    s "I assume you've already figured out what she is. If you're here to kill her or bring her back... I don't know how this is going to end."
    show lutvrogemo normal at right
    show sabiaemo normal at left
    lut "It was noticed that some orcs were disappearing. Most were from other tribes, but they disappeared near our camp, so Lutvrog was sent to track down the problem."
    show kia happy3x at center
    kia "Orc who!"
    "Kia brought a paw down on the ground with a surprisingly large sound, drawing Sabia's attention. She turned to the Makhor, giving a conciliatory smile."
    show sabiaemo happy1 at left
    s "Kia, this is Lutvrog. He's not an enemy, not bad. I hope. So please don't attack."
    show kia pawtilteager2 at center with dissolve
    show sabiaemo normal at left
    kia "Lutvrog. Not food."
    "Since Kia seemed to be thinking about this, Sabia turned back to the orc quickly. But based on how his eyes had lost their hardness, she felt less worried about the conflict turning deadly."
    s "So, are we okay? You won't feel duty-bound to kill her?"
    show lutvrogemo normalopen at right
    lut "This matter is not complete. Lutvrog does not believe Kia to be malicious, but she has killed and is likely to kill again."
    if lutvrogsex:
        show sabiaemo sad1 at left
        s "Lutvrog, please don't do this to me... Kia doesn't deserve anything else..."
    else:
        show sabiaemo irritated1 at left
        s "Oh, come on, don't give me this! She's just taking her just revenge!"
    show lutvrogemo normal at right
    lut "Lutvrog did not say that he would pursue or report her. After all, it may be that someone else is responsible for the deaths."
    show sabiaemo irritated1 at left
    s "But after that?"
    show lutvrogemo happy at right
    lut "Lutvrog respects all warriors. The event of the Red God's Arena was... in poor taste."
    show sabiaemo happy1 at left
    s "Okay, good. What if we can convince Kia to stop killing orcs nearby? Can you go back and say it was bandits or something?"
    show lutvrogemo normal at right
    lut "Lutvrog will not lie. Lutvrog must investigate more and then consider this."
    show sabiaemo closed2 at left
    s "I guess being honorable is a double-edged sword. Fine. Just don't do anything major without talking to me first, okay?"
    lut "...very well."
    "Sabia looked to Kia, wondering if she and Ylva could communicate all of this clearly enough. Or if Kia would listen even if she understood. But this was better than nothing."
    show kia pawtiltconfused at center
    "Also, Kia had come closer and was sniffing at both of them. She tilted her head and gazed at Sabia curiously."
    if lutvrogsex:
        kia "Lutvrog mate?"
        show sabiaemo surprised1 at left
        s "Wait, what?"
        show kia pawtilteager2 at center
        kia "Lutvrog and Sabia mate?"
        show sabiaemo closed2 at left
        s "I... wait... it's not like that."
        show lutvrogemo happy at right
        "Lutvrog regarded her with what looked like quiet amusement, which was not at all helpful. Sabia shot him a quick glare then focused back on Kia."
        show lutvrogemo normal at right
        s "We {i}did{/i} mate, but we're not mates. Damn, does that difference even make sense to you?"
        show kia tilt2 at center with dissolve
        "Kia stared at her, her head tilting from side to side."
        show kia pawtiltconfused at center with dissolve
        kia "Kia should mate?"
        show sabiaemo surprised2 at left
        s "What? No! What... how did you get that out of what I said?"
        show kia tilt2 at center with dissolve
        kia "..."
        show sabiaemo closed2 at left
        s "Sometimes I think I know what you're thinking, but other times..."
        show lutvrogemo happy at right
        show sabiaemo closed2 at left
        "Lutvrog chuckled while Sabia sighed in exasperation. Kia considered them for a while, then reared up and put her paws on Lutvrog's shoulders. His body flexed in preparation, but he didn't pull back or retaliate."
        show kia happy2 at center with dissolve
        kia "Not food."
    else:
        kia "Lutvrog and Sabia {i}fsskit{/i}?"
        show sabiaemo closed2 at left
        s "Maybe? I'm still not sure what all that means."
        show sabiaemo normal at left
        "Kia considered that for a moment, then reared up and put her paws on Lutvrog's shoulders. His body flexed in preparation, but he didn't pull back or retaliate."
        show kia happy2 at center with dissolve
        kia "Not food."
    show kia happy2 at center
    hide kia happy2 with moveoutleft
    show sabiaemo normal at left
    "With that, Kia sped away from them, apparently little the worse for the wear after the fight. They watched her go and Sabia let out a long breath that she hadn't realized she had been holding in."
    show sabiaemo happy1 at left
    s "Well... congratulations. You're not food."
    show lutvrogemo happy at right
    lut "Lutvrog thinks that is a significant compliment, from a predator."
    show lutvrogemo normal at right
    show sabiaemo normal at left
    "Yes, it probably was. Kia seemed to divide the world into dangerous things and small things she could either eat or... sit. Sabia still wasn't sure she understood that completely."
    if A_lutvrog >= 5:
        $ A_lutvrog += 1
        $ kiabones += 1
        $ Inventory.add_item(Makhorbones,1)
        "She felt surprisingly tired, but Lutvrog seemed thoughtful. He reached down to his discarded pack and removed something she hadn't noticed."
        lut "In the arena, Lutvrog noticed that she sought to defend the bones. A fallen comrade?"
        show sabiaemo closed2 at left
        s "Something like that."
        lut "After the arena, a warrior bet his trophy against Lutvrog. It is no longer his."
        "Lutvrog revealed that what he was holding was another Makhor bone. Not a large one, but it had the familiar dark heavy look of the others. To her surprise, Lutvrog handed it to her."
        show sabiaemo surprised1 at left
        s "You're giving it to me?"
        lut "Lutvrog gives it to the Makhor and trusts you can give it to her."
        show sabiaemo happy1 at left
        s "I will, thank you."
        "Sabia gratefully took the bone and put it away. That left her in a positive mood, but Lutvrog was still watching her thoughtfully."
    else:
        $ A_lutvrog += 1
        "She felt surprisingly tired, and fortunately it looked like Lutvrog wasn't going to keep her long."
        lut "Lutvrog will keep this secret. If she does not continue to kill orcs, then Lutvrog has done his duty."
        show sabiaemo happy1 at left
        s "Thank you, Lutvrog."
    lut "Lutvrog wonders if you have plans for the Makhor."
    show sabiaemo normal at left
    "All Sabia could do was shrug. There was no good way to answer that, and her plans were too vague at this stage. After a time, Lutvrog nodded, apparently understanding. He moved away from her, continuing his patrol outside of Kia's territory."
    "Sabia remained there for a while before finally heading back to camp. That was one disaster averted."
    return

label KLlutvrogmeeting2:
    $ kiaprogression = 9
    $ kiacooldown = True
    scene bg countryside
    call sabiabase
    with dissolve
    "Sabia ventured out on the path that had become familiar by now. So familiar that she wondered if she shouldn't change things just for the sake of security. While thinking about that, Sabia was surprised to hear what sounded like the clash of combat, though not exactly steel on steel."
    "Ready to act, Sabia hurried toward it... and started to panic as she realized what was happening."
    scene bg countryside
    show lutvrogbase at right
    show lutvrogaxe at right
    show lutvrogwraps at right
    show lutvrogwrists at right
    show lutvrogemo happy at right
    show kia powerhappy at center
    with dissolve
    "Kia and Lutvrog faced off in the tall grass. Both were bleeding, though the injuries looked light. But Lutvrog gripped his axe entirely seriously, and Kia was glowing with power..."
    call sabiabase
    show sabiaemo surprised1 at left
    with moveinleft
    s "Wait, wait!"
    "Sabia burst toward them, intending to throw herself between them... and realized that she had misjudged the situation. The two of them looked intense, but they weren't murderous. Kia's tail was twisting more playfully than angrily, now even faster as she saw Sabia."
    show kia happy2 at center with dissolve
    kia "Sabia!"
    show sabiaemo closed2 at left
    s "You two... were sparring?"
    show lutvrogemo normalopen at right
    lut "A bit roughly, but yes. Lutvrog apologizes for troubling you."
    show kia happy1 at center with dissolve
    kia "Lutvrog play!"
    show sabiaemo normal at left
    s "Well, I guess it's good that the two of you are getting along. Does that mean you've come to a decision about her?"
    show kia tilt1 at center with dissolve
    show lutvrogemo normal at right
    lut "Lutvrog has reflected on this matter. Though she has a beast's instincts, Kia is a true warrior. She does not kill out of senseless malice and she does not take advantage when given an opening."
    show kia pawtilteager2 at center with dissolve
    kia "Play good!"
    show lutvrogemo suspicious at right
    lut "As such, Lutvrog cannot forgive how dishonorably she was treated in the Red God's Arena."
    show sabiaemo happy1 at left
    s "I'm relieved to hear that... so I take it you've found some way to reconcile this with your duty?"
    show lutvrogemo normal at right
    lut "Lutvrog was sent to stop the killings, not to administer vengeance. Kia's hatred is primarily toward the orcs who captured her... Lutvrog has persuaded her to leave Grok og Dar in peace and kill outsiders only further from camp."
    show sabiaemo irritated2 at left
    s "Really? That's... well, even if that's so, are you sure she won't still kill orcs for food?"
    show kia happy2 at center with dissolve
    kia "Orcs food!"
    "Sabia glanced toward this exclamation, then swung her gaze back to Lutvrog skeptically."
    s "Are you sure? Ylva and I can try to communicate all of this to her, but I don't know..."
    show lutvrogemo happy at right
    lut "No. Lutvrog and Kia have come to an understanding."
    show lutvrogemo normal at right
    show kia pawtilteager1 at center with dissolve
    kia "Orcs Lutvrog tribe. Food orcs, Kia not eat. Bad orcs, only long hunt."
    show sabiaemo surprised1 at left
    s "Okay... I don't know how you did it, but sorry for doubting you."
    show kia pawtilteager2 at center with dissolve
    kia "Sabia! Lutvrog give!"
    "Kia grabbed hold of Sabia and pulled her a short distance away, where she soon saw a heap of corpses in the grass."
    show sabiaemo surprised1 at left
    "It took Sabia a second to recognize it for what it was: a pile of meat taken from various wild animals. The fact that Kia seemed to have eaten much of it quite messily had thrown her off at first."
    show sabiaemo normal at left
    s "You brought a peace offering, huh?"
    kia "Lutvrog give!"
    show lutvrogemo happy at right
    lut "It was difficult for Lutvrog to explain, as Kia seems to think of animals, orcs, and humans as equally food. But she is intelligent enough to gather meaning in time."
    s "So Kia... you won't take revenge on any of the orcs from this tribe anymore?"
    show kia pawtiltcurious at center with dissolve
    kia "..."
    show kia pawtilteager2 at center with dissolve
    kia "Here not bad. Lutvrog good!"
    "Her tail cheerfully thumped against Lutvrog's chest, a movement that might have knocked Sabia off her feet and was rather alarming considering the spike. But Lutvrog did not even flinch, apparently able to detect that there was no killing intent."
    show lutvrogemo normalopen at right
    lut "Truthfully, Lutvrog thinks that Kia has already killed most of her targets. But still, Lutvrog's work is done. The threat is neutralized."
    show sabiaemo happy1 at left
    s "Great to hear! Then I trust that you'll definitely keep this secret?"
    show lutvrogemo normal at right
    lut "Yes. Lutvrog believes this to be the just path... and Lutvrog has enjoyed sparring with such a different partner."
    show kia happy3x at center with dissolve
    kia "Kia play?"
    show sabiaemo happy3 at left
    s "Haha... I don't think I could take it..."
    "Kia hopped up and gave her face a happy lick. Sabia stayed with them a little while longer, making sure everything was fine, but the atmosphere was surprisingly relaxed. It was nice to see a conflict end well for once."
    "But since they wanted to spar more and Sabia didn't like the idea of getting knocked around that much, she headed back to camp."
    return

label KLbacktrackingscene:
    $ kiaprogression = 10
    $ kiacooldown = True
    scene bg cave
    call sabiabase
    with dissolve
    $ kiabones += 3
    $ Inventory.add_item(Makhorbones,3)
    "This time, Sabia headed to the cave because she had been invited. Ylva had apparently been doing work of her own, but wanted Sabia's help with something. Sabia wished she could have learned the details in camp, but they were already taking enough risks."
    show ylva normal at right
    show ylva2 arm2 at right
    "When she arrived, she spotted Ylva waiting for her outside the mouth of the cave. Sabia was about to greet her when Kia popped up out of nowhere."
    show kia happy2 at center
    kia "Hello!"
    hide kia happy2 with moveoutright
    "With that, she raced off again. Sabia approached Ylva and raised an eyebrow."
    show sabiaemo happy1 at left
    s "So she's learned greetings now?"
    show ylva happy1 at right
    ylva "Yes, it's remarkable how much she's learning. But more importantly, she was able to tell me the story of how she was captured."
    show sabiaemo normal at left
    s "Really? So that's why you called me here?"
    show ylva normal at right
    ylva "Not just that. Kia thinks that there is something important left in the trap and wants our help in retrieving it."
    show sabiaemo closed2 at left
    s "Ah. How far is it? I'm interested in seeing this trap, but I do need to stay focused."
    ylva "Under two days traveling there, I think."
    show sabiaemo normal at left
    s "Hmm. I should be able to manage that."
    show ylva happy1 at right
    ylva "Good. It seems like they set the trap in an isolated area, so it wasn't difficult to plan our route..."
    scene bg countryside
    with dissolve
    "As Ylva explained, Sabia realized that this trip wouldn't be so difficult. Ylva seemed to be skilled with this kind of organization, so the process should go smoothly. Assuming that Kia cooperated, anyway."
    "They headed east from Kia's hideout and Sabia tried to calculate their journey. They'd get into lands of other orc tribes, but probably not into the eastern elven lands. They'd need to be cautious in case anything went wrong."
    "But after a while, Sabia stopped thinking about any of that and found herself enjoying the trip. Ylva was decent conversation, while Kia raced ahead and to the sides while occasionally coming back to pad alongside them."
    "They ate food that Ylva had prepared for their first break, and Kia caught them a deer for their evening meal. When Sabia settled down to sleep, she found herself surprisingly content. Almost like being on the campaign trail again..."
    scene bg black with dissolve
    pause 3
    scene bg countryside
    call sabiabase
    with dissolve
    "Sabia woke up early, her back twinging. Her tent in the orc camp wasn't much, but it was better than sleeping on the ground. She tried to stretch out the stiffness, then noticed that the other two weren't awake yet."
    show kia happy4 at center
    show ylva normal at right
    show ylva2 arm1 at right
    with dissolve
    show sabiaemo surprised1 at left
    "More relevantly, Kia had entangled herself with Ylva during the night. It was almost like... no, Ylva was still fully clothed. Kia was rumbling softly in her sleep and rubbing herself against Ylva's body."
    show ylva opensad
    show ylva3 blush at right
    "Sabia didn't intend to wake them, but her shifting caused some noise. Ylva blinked awake, then blushed slightly to find the Makhor entwined with her."
    ylva "Kia, wha..."
    show kia happy4 at center
    show kia2 blush1 at center
    kia "Ylva."
    "The Makhor released an even louder rumbling sound and shifted happily on top of the orc, pinning her down a little longer. Kia settled her head against Ylva's chest and closed her eyes contentedly, her hair spread across both of them."
    show sabiaemo normal at left
    "Leaving Ylva to her fate, Sabia cleaned up their camp and got ready for the day's travels. By the time she was done, Ylva had managed to extricate herself and help. Kia remained where she was, occasionally yawning broadly and showing off her teeth."
    show kia happy2 at center
    show ylva2 arm2 at right
    show ylva normal at right
    hide ylva3 blush at right
    hide kia2 blush1 at center
    with dissolve
    "They didn't talk about it as they started walking, but Sabia found herself contemplating the Makhor as she ran ahead. She didn't know any stories of Makhor treating other races as anything other than animals, but the stories had obviously left out a lot. Exactly how did Kia view them?"
    "There was a vibrant beauty to her, especially her flawless skin. The color had thrown Sabia off at first, but now she considered it a healthy red. Ahead of them, Kia walked forward, her hips rocking from side to side. It could have been a sexy walk... if not for the huge detail of her tail lashing from side to side with her movements."
    show ylva normalnarrow at right
    "After they had traveled for some time, Ylva began frowning to the side, eyes squinting as if looking for something. Sabia looked nervously, but Kia didn't seem alarmed and surely her senses were better."
    s "Is everything okay?"
    show ylva normal at right
    ylva "Oh, it's fine. It just looks like... let's take a little detour to see."
    "They shifted their path slightly and Sabia soon saw what Ylva had noticed: what she'd written off as an odd hill was actually an intentionally created mound. The earth had grass growing over it, but it was obviously artificial: the central mound was too smooth, and four pillars curved up the sides."
    show ylva happy1 at right
    ylva "I haven't seen many of these Relonan shrines... Sabia, I don't think you're very religious, but do you want to do anything to pay your respects?"
    show sabiaemo angry1 at left
    s "I have no respect for that {i}thing{/i}."
    "Stomping up to it, Sabia kicked at one of the pillars, but it resisted her. The roots of the grass had grown through, so it was tougher than she expected. Not that it made a huge difference - and the others were staring at her now."
    show ylva sad at right
    ylva "I don't understand... aren't these sacred sites of Relona?"
    show sabiaemo closed1 at left
    s "They're perversions of the goddess's teachings."
    "Finally getting one of the pillars somewhat knocked down, Sabia backed off and frowned at Ylva."
    show sabiaemo irritated2 at left
    s "Don't you know this? I thought you'd studied the Order."
    show ylva angry1 at right
    ylva "Just a little, in preparation for traveling human lands to learn more. How am I supposed to know minor theological details?"
    show sabiaemo irritated1 at left
    s "Minor details? This is the difference between the religion of Lundar and hated heretics!"
    ylva "That doesn't-"
    show kia pawtiltcurious at center
    kia "What doing?"
    "Kia popped up between them, her gaze swinging from the mound to them in great confusion. Her interruption deflated the tension and left the two of them exchanging a glance."
    show sabiaemo closed2 at left
    s "Sorry, Kia, not sure how to answer that."
    show ylva normal at right
    ylva "This is a talk for Sabia and me, Kia. Sorry."
    show kia tilt1 at center
    kia "..."
    show kia happy2 at center
    kia "Sabia Ylva sit."
    hide kia happy2 with moveoutright
    "With that, Kia flicked her tail and then sprinted off in the direction they were going. Sabia and Ylva paused for a moment before following her at a slower pace, leaving the mound behind them."
    ylva "I have seen some Relonan rituals in the east... are they not the same as in Lundar?"
    show sabiaemo normal at left
    s "Not at all. The differences might seem small, but it's more than just theology. Pagan religions like that are to be exterminated by the Order of Relona."
    show ylva closednormal at right
    ylva "I didn't realize it was so serious. Was the problem the mound itself, or something specific about it?"
    show sabiaemo closed2 at left
    s "Mounds like that are usually for heretical rituals. I'm not sure how much is just rumors because people like scandals, but they have a bad reputation. But it was also wrong because it had four pillars - there are supposed to be only three spheres or pillars around the central sphere."
    show ylva normal at right
    ylva "Hmm, I think I've noticed before. But I thought the difference between three and four was just a difference in the design."
    show sabiaemo normal at left
    s "No, it's theological. People get killed over it."
    ylva "You don't strike me as a very theological person. Do you actually believe it makes that big a difference?"
    show sabiaemo closed4 at left
    s "I believe the Order of Relona does have some real power. And I grew up a good Lundari citizen, which means being a good Relonan. Some of what gets taught is obviously bullshit."
    show ylva closedhappy at right
    ylva "I see... this is all a little strange to me. Orc religion is much more free-flowing, focusing on the spirit of the act instead of the act itself."
    show sabiaemo normal at left
    s "Well, it's not the same. Heretics are declared outside the Order, almost less than human in a way."
    show sabiaemo irritated1 at left
    s "This far out, maybe the details don't matter. But if the Order sends a Lustrator to judge the situation... that makes things a lot messier."
    show ylva normal at right
    ylva "These Lustrators enforce Relonan theology, I take it?"
    s "And whatever else is in the Order's best interest. They're no joke."
    show sabiaemo closed2 at left
    s "On the western front, the Lustrator was a man called Bedhver... I don't want to know what he would have done if he had been given full authority."
    show ylva normalnarrow at right
    ylva "He was that fanatical?"
    s "Everybody wanted to beat the minotaurs, but Bedhver of the Scouring Light wanted to take control of the whole region and transform it into a \"crucible of Relona\" - he was the kind of man who talked about burning away sin, and you had to wonder if he meant literal fires."
    ylva "He wasn't able to, I take it?"
    s "No. The Order of Relona commanded that he work with us, so he limited his actions."
    show sabiaemo irritated1 at left
    s "But if there was a Lustrator out here, they wouldn't be under anyone's orders. If they're sent out to judge a situation, they don't answer to anyone but Relona herself."
    ylva "...I can see why that would be a concern."
    show sabiaemo normal at left
    "They kept walking together, talking idly of less serious religious matters. Sabia found herself a little torn, since she didn't think much of orc shamanism but didn't want to offend Ylva. It made the conversation difficult."
    show kia normal1 at center with moveinright
    "Just as she was trying to think of another topic of conversation, Kia came racing toward them at a dead sprint. Sabia braced herself for an attack from the direction she'd come, but Kia skidded to a halt in front of them, expression serious."
    kia "Come."
    "They glanced at each other, then followed Kia. She didn't sprint but quickly led them at a pace that required them to run to keep up. When they got close, Sabia realized they had arrived at their destination."
    scene bg countrypit
    call sabiabase
    show ylva normal at right
    show ylva2 arm2 at right
    show kia normal1 at center
    with dissolve
    "What had once been an ordinary plain had been destroyed by the remnants of a battle. The heart of it was a large pit, but Sabia let her gaze first examine the rest. Huge claw marks torn in the ground that could only have been Kia. There were also fragments of weapons and nets scattered around the hole."
    "But the center of it was the pit, a large hole that seemed to have been lined with sharpened stakes. They were now largely broken and covered with rubble, which let her put together an order of events..."
    show ylva sad at right
    ylva "Kia... this was where they captured you?"
    show kia angry1 at center
    show sabiaemo sad1 at left
    kia "Kia smell {i}fsskit{/i}. But {i}fsskit{/i} not. Fall. Hurt. Attack."
    "Kia was prowling around the edges of the battlefield, growling low in her throat. Sabia recognized the raw animal wariness. Though Kia might be fully intelligent, her instincts warned her about this place."
    show ylva closedsad at right
    ylva "They probably had the bones on a pit trap, then. But I don't sense any magic..."
    s "There wouldn't have been. Even if the orcs could manage illusions, that would have alerted Kia."
    ylva "Right. Based on the positions... they had the pit lined with poisoned stakes. They had people ready, but they were counting on the poison to incapacitate her."
    show sabiaemo happy2 at left
    s "But it wasn't enough. Looks like she destroyed the hole on her way out and took a lot of them down with her."
    show kia irritated1x at center
    kia "Throw. Hurt. Kia kill."
    show ylva sad at right
    ylva "Yes, that makes sense... the initial trap might have handicapped her, but they'd have followed up with projectile weapons. Kia might have killed them, but with the injury from the trap and all the others, the poison took its toll."
    show sabiaemo normal at left
    s "No bodies, though."
    ylva "They would have cleaned them up. It seems like they even tried to remove most of the trap, but couldn't entirely remove all the rubble."
    s "You seem pretty confident. Exactly which orcs did this?"
    show kia pawsad1 at center with dissolve
    show ylva normal at right
    "Instead of answering, Ylva hopped down over the edge of the pit, sliding a short distance down the ragged slope before jabbing her staff into the dirt to hold her position. Kia gave a worried hiss and edged closer to the pit."
    "Ylva picked up one of the sharpened stakes that was mostly intact and examined it carefully. Soon after, her expression darkened. It meant something to her, but she wasn't saying anything."
    show sabiaemo irritated2 at left
    s "You know something about who did this, don't you?"
    show ylva closedsad at right
    ylva "It can't..."
    show ylva sad at right
    ylva "I'm not sure. The local shaman of a small tribe couldn't make a poison like this. It likely came from Kelshatan."
    "It seemed obvious that the council of shamans was involved, almost not worth saying. Sabia watched Ylva, wondering what else she knew that she wasn't telling. It wasn't worth bringing up now, but she filed it away."
    show sabiaemo normal at left
    s "Alright, Kia... why are we here?"
    show kia pawuncertain1 at center
    kia "Kia help. Smell."
    show kia angry1 at center with dissolve
    "She shifted closer to the edge of the pit, her fur all on end and her tail rigid behind her. As close as she would get, Kia pointed toward one side of the pit that had collapsed."
    show ylva normal at right
    ylva "Maybe some of the bones were trapped in the rubble?"
    show sabiaemo happy1 at left
    s "That would make sense. I'll help you dig."
    show ylva angry1 at right
    show sabiaemo normal at left
    ylva "I can get them. The rubble is less stable than it looks."
    "Ylva began moving across to the pile of rubble and Kia prowled around the edge, watching her nervously. Sabia waited for a moment, then decided that she should go down and help anyway."
    "She moved down the side of the pit as slowly and carefully as possible, avoiding jabbing herself on any of the remaining stakes. Many had been broken or crushed under rocks, but in a way that was more dangerous, because there were sharp fragments of stakes within the rubble."
    "By the time she reached the other side, Ylva was using her staff as a lever to push away some of the larger rocks. She worked at a feverish pace, and though Sabia helped move aside some of the smaller pieces that were dislodged, she frowned at the orc woman."
    show sabiaemo sad1 at left
    s "Are you okay, Ylva?"
    show ylva closedangry at right
    ylva "Let's get the bones and go back. I don't like lingering here."
    show sabiaemo closed2 at left
    s "I see. Kia, do you want to help?"
    show kia irritated1x at center
    "Kia kept pacing by the edge, still growling. They could have finished this almost immediately if Kia had transformed, but Sabia supposed she couldn't blame the Makhor for not wanting to get near the trap again."
    show ylva angry1 at right
    "Ylva, though... what was wrong with her? Sabia watched as she stabbed the end of her staff in between two boulders and heaved... and realized that the second stone was under much more of the slope of rubble than it looked like from Ylva's angle."
    show sabiaemo surprised1 at left
    s "Ylva, wai-"
    show kia uncertain1 at center
    show ylva surprised at right
    ylva "Aah!"
    "Too late. A large piece higher on the slope of rubble broke apart and struck below, dislodging more pieces. In seconds there would be a small landslide of rocks and fragments of stakes tumbling down toward Ylva, who was only now looking up at the noise."
    "Sabia had no time to think, she just acted. Throwing herself forward, she grabbed Ylva around the waist and jerked her backward, toward the center of the pit. They fell just as the landslide crashed down where Ylva had stood."
    "Ylva was shaken but fine, getting off Sabia where they had fallen. Her eyes were wide and she looked back toward Sabia."
    show ylva sad at right
    ylva "Sabia..."
    show sabiaemo surprised3 at left
    s "Fuck, that hurts..."
    "As the panic subsided, Sabia could feel a burning line of pain along her arm. She had succeeded in pulling Ylva away from the landslide, but in throwing them away, she had scraped along one of the stakes still in the ground. She hadn't even felt it at first, but now the burning was turning into a numbness that spread from her arm..."
    show sabiaemo closed2 at left
    s "Do... do you think the poison would still be working?"
    show ylva closedsad at right
    ylva "After this long exposed, it must be weakened, but if it was made for a Makhor..."
    show ylva sad at right
    "Ylva bent down to examine the wound and the concern was obvious in her eyes. Sabia found her vision growing a bit blurry, but she could still see a red blur move beside Ylva's green."
    show kia pawsad1 at center with dissolve
    kia "Sabia hurt."
    "Kia had overcome her fear of the pit and now crouched beside Ylva."
    ylva "Yes. If I had time to create a potion, maybe..."
    if KLelmypotion:
        "But there wasn't time, that was obvious. Sabia wished she had brought the potion that Elmy made, but then again, it had been made for a Makhor. A human trying to use the same might make the antidote just as lethal as the poison."
        "With no easy options and her vision growing blurrier, Sabia winced and squeezed her arm as if she could force the poison out by willpower alone."
    else:
        "But there wasn't time, that was obvious. Sabia winced and squeezed her arm as if she could force the poison out by willpower alone."
    show kia happy1 at center with dissolve
    kia "Kia help."
    show sabiaemo surprised1 at left
    "Sabia was suddenly bundled up in soft-furred arms and they were flying through the air. She felt a moment of panic, but Kia landed smoothly, her legs absorbing all the shock."
    show sabiaemo normal at left
    "She lay Sabia down on the soft grass and bent closer, licking at the wound. Sabia's arm was numb enough that she barely even felt it. Could Kia do something about the poison? But if she could, why hadn't she done something before?"
    show kia powerhappy at center with dissolve
    "When Sabia saw Kia's tail shift down toward her spike-first she should have worried, but she was too tired. The sharp end touched her arm... and Sabia felt a surge of something warm."
    show sabiaemo surprised1 at left
    "Magic pulsed through her, but it was like no magic Sabia had felt at home. It was raw and hot, sweeping away the numbness and the pain, leaving her gasping for breath."
    show sabiaemo2 blush at left
    "Yet it also called to something animal within her. A groan escaped her lips that was closer to a moan and her back was arching involuntarily. Her nipples had grown rock hard within her clothes and even as the magic subsided, the heat still burned within her."
    show ylva surprised at right
    ylva "Kia... did you purify the poison?"
    show sabiaemo closed2 at left
    "It seemed that Ylva had managed to climb out of the pit and caught up with them, now moving into Sabia's vision and staring down at her in concern."
    show kia happy2 at center with dissolve
    kia "Kia help."
    show ylva happy1 at right
    ylva "That's good, but... what kind of magic is this? How can you purify poison?"
    show kia happy4 at center
    kia "Sabia small. Easy help."
    "Kia put an affectionate paw on her stomach, but it prompted a low moan in Sabia's throat. She cut off a second later, flushing in embarrassment, but it was too late."
    show ylva normal at right
    ylva "Is she actually alright?"
    show kia happy2 at center
    kia "Sabia want mate."
    ylva "Oh! Sabia, uh, are you okay?"
    show sabiaemo irritated2 at left
    s "The numbness is gone, but... what kind of magic is this, Kia?"
    show kia happy3 at center
    "Kia cocked her head at them for a moment, then gave a slow smile. She patted Sabia's stomach again, which felt unfairly good, then shifted back and began to gather magic."
    kia "Magic for Kia mating."
    show sabiaemo surprised1 at left
    show ylva normalnarrow at right
    show kia futachange1 with dissolve
    "Power glowed around Kia, similar to when she had transformed from her monstrous body, but this time it pooled between her legs."
    show kia futachange2 with dissolve
    "As they watched, eyes widening, Kia's body distorted and a new member grew from where her pussy had been a moment ago."
    show ylva normal at right
    show ylva3 blush at right
    show kia futachange3 with dissolve
    "When the magic finished, Kia had a throbbing cock between her legs, still glowing faintly with magic. Ylva had drawn back in shock, while Sabia was warring with herself and the magic still glowing warmly within her. She really didn't want to see that thing in Kia's full size form, though..."
    show sabiaemo surprised1 at left
    s "Kia... are you saying you want to mate with me?"
    show kia pawtiltcurious at center
    show kia3 cock at center with dissolve
    hide ylva3 blush at right
    "Kia tilted her head again, as if considering, and Sabia wasn't sure what she wanted to happen."
    if A_kia >= 5:
        $ kiaprogression = 10
        $ primekiasabiascene = True
        show kia happy2 at center
        show kia2 blush1 at center
        show sabiaemo happy1 at left
        with dissolve
        "Eventually Kia reached down, one finger of a paw sliding between Sabia's legs. She moaned immediately as the soft fur bunched against her."
        kia "Kia like Sabia. Kia help mating?"
        "Sabia flushed and shivered, not sure what to say, but at that moment Ylva coughed loudly."
        ylva "This place isn't exactly safe."
        "Kia abruptly shifted to put her paws on Ylva's shoulders, eyes bright. The orc woman did an admirable job of remaining calm."
        kia "Ylva want mate?"
        show ylva openclosed2 at right
        show ylva3 blush at right
        ylva "Kia... maybe we should focus on getting the bones and returning to somewhere safe?"
        hide kia3 cock with dissolve
        show kia happy1 at center
        "That seemed to confuse Kia for a moment, but after a second she transformed back and pulled away. Apparently not put off by the whole thing, which was good - Sabia did not want to see what havoc a horny Makhor could wreak."
        "While Sabia bandaged the wound on her arm, Kia and Ylva worked with the rest of the rubble more carefully. By the time Sabia was done, they had retrieved several pieces of bone."
    else:
        $ kiaprogression = 11
        show kia happy1 at center
        hide sabiaemo2 blush
        "Eventually Kia patted her on the head. The motion was friendly, but not erotic like the previous touch. In fact, the warmth within her seemed to be ebbing now."
        kia "Sabia not {i}fsskit{/i}. Kia just help."
        show sabiaemo closed1 at left
        s "I see... thank you, Kia."
        show kia happy2 at center
        "Kia abruptly shifted to put her paws on Ylva's shoulders, eyes bright. The orc woman did an admirable job of remaining calm."
        kia "Ylva want mate?"
        show ylva openclosed2 at right
        show ylva3 blush at right
        ylva "Kia... maybe we should focus on getting the bones and returning to somewhere safe?"
        hide kia3 cock with dissolve
        show kia happy1 at center
        "That seemed to confuse Kia for a moment, but after a second she transformed back and pulled away. Apparently not put off by the whole thing, which was good - Sabia did not want to see what havoc a horny Makhor could wreak."
        "While Sabia bandaged the wound on her arm, Kia and Ylva worked with the rest of the rubble more carefully. By the time Sabia was done, they had retrieved several pieces of bone."
    show kia happy4 at center
    show ylva closednormal at right
    "As soon as Kia finished brushing the bones off, she pulled them close and rubbed them against her face. She seemed to have entirely forgotten about what had just happened. Sabia glanced toward Ylva, swallowed, and decided that maybe it was best for them to do the same."
    "Despite the strangeness of it all, their trip had been a success. They had acquired multiple bones from Kia's friend, plus significantly more information about how the orcs had captured her. All of that might be useful in the future."
    "But the trip back was awkward. Sabia was left with very mixed feelings about how Kia curled up with Ylva each night. The orc woman seemed to have adapted to the new information and just stroked Kia's hair gently, but Sabia still wasn't sure what to think."
    "In any case, they got back without another... incident."
    return

label KLsabiascene:
    $ kiaprogression = 11
    $ kiacooldown = True
    scene bg cave
    call sabiabase
    with dissolve
    "It was a little strange to return to Kia's cave after their trip together, and the strange magic she had seen and felt. But Sabia thought it would probably be fine, since Ylva was likely to be there."
    show kia happy2 at center with moveinright
    "But she wasn't. The cave seemed empty until abruptly Kia flashed in from the side, pinning Sabia to a wall. She put her paws on Sabia's shoulders, but unlike before, Kia also rubbed up against her while giving a pleased rumble."
    kia "Sabia!"
    s "Umm... hello, Kia."
    kia "Here not danger!"
    "Sabia laughed nervously, wondering what Kia meant by that but suspecting that she already knew. Was she wanting to pick up where they left off?"
    show kia pawtilteager2 at center
    kia "Sabia want mate?"
    s "Umm..."
    menu:
        "Accept":
            "Maybe there was still some magic swimming around inside her, but Sabia found herself warm and relaxed. It was just the two of them, after all. No one else would know and she'd get some quick relief..."
            show kia happy4 at center
            "In answer, Sabia reached up and brushed the soft fur on Kia's thigh. Kia immediately released a pleased rumble and bent lower, licking Sabia's face."
            kia "Kia make cock."
            "The magic started to swell and Sabia found herself hesitating..."
            menu:
                "Let it happen":
                    show kia futachange1 with dissolve
                    pause 1
                    show kia futachange2 with dissolve
                    pause 1
                    show kia futachange3 with dissolve
                    "Deciding she was willing to experiment, Sabia just held onto Kia as the Makhor grew a new organ..."
                    if makhorfightpeace:
                        call kiasabiaFg
                    else:
                        call kiasabiaFr
                "Persuade Kia to try something else":
                    s "Kia... do we need that to mate?"
                    show kia tilt1 at center with dissolve
                    "Kia paused and stared at her, apparently confused."
                    kia "Not mate?"
                    s "Yes mate, but... not cock?"
                    show kia normal1 at center with dissolve
                    "Kia blinked rapidly in surprise, cocked her head back and forth a few times, then bent down to sniff at Sabia's crotch. Sabia yelped and pulled back a little bit, then found Kia looking up at her."
                    show kia pawtiltcurious at center with dissolve
                    kia "Sabia have cock?"
                    s "Ah, no... but can we mate without that?"
                    show kia happy2 at center with dissolve
                    kia "Not mate. Sit."
                    "Sabia sighed in disappointment, regretting that she'd ended up turning down Kia. That is, until Kia pounced on her..."
                    if makhorfightpeace:
                        call kiasabiaYg
                    else:
                        call kiasabiaYr
            "When it was over, Sabia lay happy and sated, glad the mossy stone was so comfortable. After fucking her so thoroughly, Kia wrapped herself around Sabia and began rumbling happily."
            "Deciding to just accept it, Sabia let herself drift into a peaceful sleep..."
        "Refuse":
            show sabiaemo closed2 at left
            "Sabia shook her head rapidly. Befriending the Makhor was one thing, but this..."
            show kia happy2 at center
            "Fortunately, Kia didn't seem to take it personally. She shifted backward, ears twitching."
            kia "Not mate?"
            s "No, but we can still be... umm, sit?"
            kia "Sabia sit!"
            "Apparently equally pleased with that, Kia roughly pulled Sabia down to the floor and began rubbing against her while rumbling happily. They talked a little, but mostly just enjoyed the company."
            "Eventually Sabia managed to relax, but her throat still felt a little dry when she thought about what might have happened..."
    return

label KLylvalesson:
    $ kiaprogression = 12
    $ kiacooldown = True
    $ kiabones += 1
    $ Inventory.add_item(Makhorbones,1)
    scene bg cave
    call sabiabase
    show kia happy2 at center
    show ylva happy1 at right
    show ylva2 arm1 at right
    with dissolve
    "When Sabia entered Kia's cave, she immediately heard voices. She found Ylva and Kia sitting opposite one another in the nest of grass. Ylva was speaking, while Kia watched her with rapt attention, her tail curled around one of Ylva's legs."
    show sabiaemo happy1 at left
    "Sabia paused a moment, smiling at the scene, but then focused on what was actually being said."
    show sabiaemo normal at left
    show kia pawtiltcurious at center with dissolve
    kia "Humans eat orcs?"
    ylva "Not literally. But Lundar is very big, very dangerous. Lots of them together, and organized."
    show kia pawtiltconfused at center
    kia "Human... packs?"
    show ylva happy2 at right
    ylva "Something like that. You should know about this."
    show kia pawuncertain1 at center with dissolve
    kia "Know catgirl packs. Humans different."
    show ylva normal at right
    ylva "Maybe not packs in the same way, but they're working together. Orcs, too. The council of shamans may not have full executive power, but orcs are working more in unison."
    show kia normal1 at center with dissolve
    "Kia considered this skeptically for a moment, as if the whole thought was strange. After a pause, she turned and smiled at Sabia."
    show kia happy2 at center
    kia "Sabia! Kia and Ylva talk!"
    show sabiaemo happy1 at left
    s "Evidently. You can speak much more clearly now."
    show kia happy1 at center
    kia "Kia learn clothes!"
    show sabiaemo normal at left
    show ylva happy1 at right
    ylva "Learn {i}more{/i} about clothes. She actually understood the basics even before."
    show kia happy2 at center
    "Nodding agreement, Kia stroked the fur fringes of Ylva's outfit. The orc woman squirmed a little, but didn't pull away since her touch seemed purely innocent."
    kia "Food small. Can't change. Hurt easy. Needs..."
    show kia pawtiltcurious at center with dissolve
    "Pausing, Kia hugged her shoulders and pretended to shiver."
    kia "What this?"
    ylva "Warmth. We wear clothes to stay warm."
    show kia pawtilteager1 at center
    kia "Need warm. Kia knows this."
    show kia pawtilteager2 at center
    kia "But! Kia learn clothes meaning. Learn many things."
    show kia happy2 at center with dissolve
    "Kia hopped up, still keeping the end of her tail against Ylva's leg, and came to examine Sabia."
    show kia tilt1 at center with dissolve
    if Sabia.armor == Rags:
        kia "Old clothes. What mean?"
        s "I didn't have anything else to wear, so I had to use these."
    if Sabia.armor == Leatherarmor:
        kia "Strong clothes. For fight? What mean?"
        s "That's right. It would be easy to get hurt without these."
        show sabiaemo closed2 at left
        s "Well, it's not exactly the armor I'd want, but it's better than nothing."
    if Sabia.armor == Heavyleatherarmor:
        kia "Strong clothes. For fight? What mean?"
        s "That's right. It would be easy to get hurt without these."
        show sabiaemo closed2 at left
        s "Well, it's not exactly the armor I'd want, but it's better than nothing."
    if Sabia.armor == Orcslavearmor:
        kia "Shiny. But not warm. What mean?"
        s "That's, uh... these are orc clothes. They were a gift."
    if Sabia.armor == Barmaidclothes:
        kia "Weird clothes. What mean?"
        s "I... wear this for work. It's hard to explain."
    show sabiaemo normal at left
    show kia pawuncertain1 at center with dissolve
    "Kia considered that for a moment, then shook out her hair a little. Her comprehension had obviously increased, but humans and orcs must still seem quite strange to her."
    show sabiaemo happy1 at left
    s "Anyway, I was just checking on you. How are we doing on finding Makhor bones?"
    show kia happy2 at center with dissolve
    kia "Ylva help!"
    ylva "I persuaded someone in camp to sell me the bone they won, saying I needed it for my research. Which is true, in a way."
    show sabiaemo normal at left
    s "Ah, that's clever. But how many more do you think are still held in camp?"
    show ylva normal at right
    ylva "I don't think Kia wants to get every single one. Just enough for... something."
    show kia happy1 at center
    kia "Important."
    "After that declaration, Kia made no more effort to explain herself. Ylva gave a sort of half shrug and Sabia just nodded. If it was important to the Makhor, then it was automatically important to some degree."
    "She sat down with them and just let the conversation go where it would. Kia was understanding a lot now, and she didn't want Ylva to present a biased view of politics. Not that Kia had a strong grasp of politics, seeming to view everything through the lens of individuals."
    "But despite that motive, Sabia found herself relaxing. This... wasn't bad. When Kia eventually became sleepy and they decided to go, Sabia was almost disappointed."
    return

label KLshamanscamp:
    $ kiacooldown = True
    $ KLshamanscampraided = True
    $ kiabones += 1
    $ Inventory.add_item(Makhorbones,1)
    scene bg countryside
    call sabiabase
    with dissolve
    "The next time Sabia spotted the strange group of orcs leaving camp, Sabia trailed them from the distance. She had brought hunting equipment as an excuse if they noticed her, but they didn't seem to be paying too much attention."
    "She got absolutely no indication of what they were looking for, and in fact wasn't sure they were searching for something specifically. But she did hear them mention Shaman Ornshakar, which made her doubly certain that this was worth her time."
    "Following them long enough, she discovered that the orcs had a small camp not too far from the main one. It seemed to be some kind of outpost... perhaps one for meetings that couldn't be done in camp?"
    "While the orcs chatted with one another, Sabia kept her distance. But once they headed out, Sabia crept into camp and examined what they'd left behind."
    "Mostly normal supplies, though she found an unusual number of shamanic talismans. Nothing incriminating, unfortunately."
    show sabiaemo closed2 at left
    "She did discover that one of the orcs had left his Makhor bone trophy behind. After a moment of consideration, Sabia decided that she should take it for Kia. The question was just how far she should go."
    "Keeping her knowledge of the camp to herself could be useful later, or might never matter. If she destroyed it now, it would definitely cause Ornshakar some trouble, but not very much..."
    menu:
        "Steal things and burn it down":
            $ ORNcampburned = True
            $ money += 27
            show sabiaemo normal at left
            "Since she would be burning most of the evidence, Sabia looted everything thoroughly. She ended up with the Makhor bone and 27 Lundils, which wasn't bad."
            "That done, she lit a fire in their firepit and made sure that it spread. Most likely they wouldn't believe it had happened accidentally, but at least the doubt would be there. Ornshakar would have to worry about whether or not he had an enemy working against him."
            "Once she was satisfied that the flames would consume the entire camp, Sabia fled from the smoke back to camp. Another blow struck against that fool shaman."
        "Take the Makhor bone and leave it alone":
            $ ORNcampburned = False
            $ money += 14
            show sabiaemo normal at left
            "Sabia resolved to keep the fact of the camp for future reference. For now, all she really needed was the Makhor bone - but to make it seem like it might be theft, she also took 14 Lundils and some food that was unguarded."
            "Taking her spoils, Sabia headed away from the camp and marked it for future reference."
    return

label KLbonequestcomplete:
    $ kiaprogression = 13
    $ A_kia += 2
    scene bg cave
    call sabiabase
    with dissolve
    "When Sabia checked in on Kia's cave, at first she thought no one was there. But when she stepped further in, she heard a strange sound. Sabia frowned and pursued cautiously."
    show kia happy4 at center
    show kia2 tears at center
    "Kia sat in the back room, her arms filled with Makhor bones. When she saw Kia, she opened her eyes slowly. They were glistening with tears, but she smiled."
    kia "Enough."
    show sabiaemo closed2 at left
    s "Enough? As in you don't want to look for any more?"
    kia "No. Enough bones for {i}gartnn{/i}."
    show sabiaemo normal at left
    "The last word didn't mean anything to Sabia, but Kia said it carefully, as if it meant something important. Could it be a name? Or maybe a ritual? Or maybe some condition had been satisfied that Sabia couldn't understand?"
    show kia happy2E at center
    "If there was any doubt that Kia's tears were happy ones, a moment later she launched herself forward, pinning Sabia to the wall and rubbing herself against her with a loud rumble."
    kia "Sabia help! Kia is happy!"
    show sabiaemo happy1 at left
    s "I'm glad we were able to help."
    hide kia2 tears at center
    show kia happy2 at center
    "Kia wiped away her tears and pushed closer to Sabia."
    kia "Sabia is {i}fsskit{/i} now!"
    show sabiaemo happy3 at left
    "Though the meaning of that word still wasn't clear, Sabia found herself smiling. It obviously meant something important to Kia. Meanwhile, the Makhor pulled back, eyes alight, tail swishing eagerly."
    show kia happy1 at center
    kia "Kia help Sabia! How?"
    show sabiaemo closed2 at left
    "That was exactly the offer that Sabia had been wanting all this time, but now that she received it, she found herself in an odd position. It wasn't as if she had a single thing she wanted to use Kia for - even asking her to come in and kill Groknak or a Captain would just add complications."
    "Instead, she needed Kia as an asset in the future. And that meant actually having a solid connection with her, which included Kia having a better understanding of Sabia's situation. That might be difficult."
    show sabiaemo normal at left
    s "That's hard to explain. You see, my family... wait, has Ylva taught you that?"
    show kia pawuncertain1 at center with dissolve
    kia "Human-kin. Sabia-kin."
    show sabiaemo closed4 at left
    s "Well... someone in my family tried to have me killed. I think it was my sister."
    show kia angry1 at center with dissolve
    kia "Bad."
    show sabiaemo normal at left
    s "That's right, it's ba-"
    show kia pawtiltcurious at center with dissolve
    kia "Why?"
    "Sabia paused for a second, not having expected that question. Kia peered at her curiously, asking the question at more than surface level. But how could she explain knotty human politics when she wasn't even sure of the exact reasons herself?"
    show sabiaemo closed2 at left
    s "Uh, well... my family doesn't get along. We have different views on a lot of things."
    show kia normal1 at center with dissolve
    kia "Family important. Sit, not fight."
    show sabiaemo normal at left
    s "It's not that easy. We want different things. My family doesn't want to let me have important things."
    show kia pawuncertain1 at center with dissolve
    kia "Family not let Sabia hunt?"
    show sabiaemo irritated1 at left
    s "No, not lik-"
    show kia pawtiltcurious at center with dissolve
    kia "Not let Sabia mate?"
    show sabiaemo closed2 at left
    "Sabia sighed and rubbed her eyes, while Kia seemed increasingly puzzled."
    show sabiaemo closed4 at left
    s "No, it's a human thing. They won't... let me be free. And because we fought, my sister tried to kill me."
    show kia neutralE at center with dissolve
    "Kia sat back and pondered this for a long moment, turning over what must be entirely alien concepts to her. After a long time, she gave a brief nod."
    show kia happy1 at center
    kia "Kia help Sabia."
    show sabiaemo happy1 at left
    s "Thank you, Kia."
    "Not wanting to continue the awkward conversation, Sabia stepped forward and gestured to all the bones."
    show sabiaemo normal at left
    s "What do we do with these now?"
    show kia happy2 at center
    kia "{i}Gartnn{/i}."
    s "Which is...?"
    show kia happy4 at center
    kia "{i}Gartnn{/i} is... fire. Ashes. Memory. {i}Gartnn{/i} is last goodbye."
    "A funeral or memorial ceremony, then. But Kia wasn't done - though she was more somber now, her tail remained animated."
    show kia happy1 at center
    kia "Here bad for {i}gartnn{/i}. Kia must find good place. Maybe long time."
    show sabiaemo happy1 at left
    s "Okay. If we can help with that, let us know."
    show kia happy2 at center
    kia "Sabia is {i}fsskit{/i}."
    "And that seemed to be that. Sabia stayed in the cave for a while, staring at the bones, before she finally headed back. She felt as though she had ended one task, but began another."
    return

label tekrokraidintro:
    $ Mainarmy.add_troop(Tekrokorcs)
    $ tekrokraidintroduced = True
    scene bg tekroktent
    call sabiabase
    show tekrok normal at right
    with dissolve
    "When Sabia entered, she found the tent empty except for Tekrok, who was pacing back and forth. He saw her and glowered."
    show tekrok angry2 at right
    t "It's time for you to pull your weight, human. Tekrok hears you have been preparing a raiding party?"
    show sabiaemo closed2 at left
    s "It's not where I want it to be yet, but yes."
    show tekrok normal at right
    t "Get it ready. Tekrok needs you to attack this settlement."
    show sabiaemo normal at left
    "Tekrok savagely stabbed a finger against a map hung on the wall. It was less rough than she'd expected, so Sabia quickly recognized the target. It was a human settlement."
    s "This is a test of my loyalty, then?"
    t "Well? Will you?"
    show sabiaemo closed4 at left
    s "I don't care about a bunch of peasants who aren't even Lundari. But that's a stupid target - you want to bring Lundar's armies down on your head?"
    show tekrok angry2 at right
    t "Tekrok does not believe it will come to that. Will Lundar march through Governor Andian's territory this close to an agreement? Tekrok thinks not."
    show sabiaemo closed2 at left
    "That made Sabia blink - Tekrok was less foolish than he looked. There was confidence in his voice that made her believe he was right about an agreement being worked on - Lundar had wanted to expand its borders into that territory in any case."
    show sabiaemo normal at left
    s "Maybe not. But what happens once Lundar expands into that territory and finds a village it now owns still burning?"
    show tekrok normal at right
    t "This would be no action of the tribe. That is why Tekrok sends you. Lundar would first send an expeditionary force."
    show sabiaemo closed2 at left
    s "You're deluding yourself if you think you can handle even that force. You might be able to crush a few farmers with brute force, but what happens when you face Trausan cavalry?"
    show tekrok angry1 at right
    show sabiaemo irritated1 at left
    "Tekrok lunged toward her with a growl, but Sabia didn't back down and he stopped short. She saw hatred burning in his eyes... but also something else, a glimmer of something smarter. He gave a derisive snort and didn't back down either."
    t "We will not face them head on. Tekrok has been training pike units from weaker allies - they will perish, but they will take your precious lizards with them. And Traus does not have enough cavalry to send huge units."
    "That... was actually a good strategy. Dangerous as Trausan cavalry was, they weren't invincible if a trained force would stand against them instead of breaking. Tekrok wasn't speaking of just winning a war with numbers, he had a real strategy. Sabia narrowed her eyes before speaking more quietly."
    show sabiaemo irritated2 at left
    s "And what happens when Lundar starts sending mages?"
    show tekrok normal at right
    t "Tekrok will not tell you all his plans, human."
    show sabiaemo eyebrow1 at left
    s "Because you don't have any?"
    show tekrok angry2 at right
    t "Hah. You humans can destroy a great deal, but you lack other magic. Especially when it comes to finding small units that refuse to stand and fight."
    "Also true - it was a point that Sabia had brought up plenty of times against mages who tried to say the infantry was useless. Human magic was unparalleled in destruction, but less useful against opponents that fought from the shadows."
    show sabiaemo normal at left
    s "Say that all of that actually works - you can't move the camp. What happens when Lundar comes to burn down Grok og Dar?"
    t "The Warchief will have no choice but to go to war - but by then, we will be ready."
    show tekrok normal at right
    t "Tekrok is done with your questions, human."
    "Though she could have asked more, Sabia was fairly sure it would do no good. He had made his point: he actually had something of a plan. Ranting about dominating humans probably sounded good to the orcs who followed him, but Tekrok wasn't as stupid as they were. Sabia found herself considering that and frowned, forcing herself to focus again."
    show sabiaemo closed1 at left
    s "I know you don't trust me, so I won't push you on specifics. But I'm useless to you if I don't know any of your plans. What else are you arranging?"
    show tekrok angry2 at right
    "Tekrok scowled at her and didn't answer, but seemed to be considering the question."
    t "Tekrok will not answer these questions now."
    show sabiaemo normal at left
    s "At least tell me this: do you have support from the council of shamans? Because just hiding isn't going to work if you don't have magical support. But based on what you said to Ornshakar..."
    show tekrok angry1 at right
    t "Tekrok hates that little worm. But not all on the council are so blind. Tekrok will say no more."
    "So he did have at least some ideas there. Sabia doubted Tekrok was too good a negotiator, but among orcs maybe he was better than he looked. But before she could come up with another question, Tekrok contradicted himself and spoke again."
    show tekrok angry2 at right
    t "Ylva is not so stupid. She has foolish views, but she is young. And her uncle... perhaps a new alliance can be forged there."
    if A_ylva >= 10:
        show tekrok happy1 at right
        t "Tekrok has noticed that she has taken a liking to you. So be it. Perhaps you can do more to form an alliance with her than Tekrok."
        show sabiaemo closed1 at left
        s "Ylva is too smart to get involved in this kind of plan."
    else:
        t "You should do more to form an alliance with her. Perhaps you could do more than Tekrok."
        show sabiaemo closed2 at left
        s "I'm not sure she likes me enough for that... and I don't think she'd listen to what you have to say."
    show tekrok normal at right
    t "Tekrok is willing to wait. All orcs will see the truth in time."
    show tekrok happy1 at right
    t "And Tekrok is not limited to merely orcs. There are others who could stand against Lundar... have you heard of the Accursed Queen of Silver?"
    show sabiaemo surprised1 at left
    s "The Vegardan pirate lord? You have contact with her?"
    t "Not with her directly, but Tekrok has Vegardan alliances. They have long been pursued by Lundar, and they have no love for humans."
    show sabiaemo happy1 at left
    s "That's impressive... but how did you manage to contact her? I didn't think the sea lords exactly kept offices..."
    show tekrok normal at right
    t "No more questions."
    show sabiaemo normal at left
    s "Fine... so for now, you want me to attack that settlement?"
    t "Yes, but you must do it of your own will. Otherwise, Warchief Groknak's prohibition against Tekrok will apply."
    show sabiaemo closed1 at left
    s "Then you actually have to trust me to do this right."
    show tekrok angry2 at right
    t "Tekrok is your only chance here, human. But Tekrok does not trust you. That is why Tekrok will only give you a small number of troops and supplies to support the attack."
    show sabiaemo irritated2 at left
    s "You really expect me to raid a settlement of that size with troops I can scrape together myself and a bit of backup? I know you have a lot more troops just sitting around."
    show tekrok angry1 at right
    t "You can have them when you earn them, human whore."
    show tekrok normal at right
    "With that, Tekrok turned away, though she thought his gaze lingered on her. Sabia recognized the dismissal and left the tent, but found herself thinking about many things."
    show sabiaemo normal at left
    "Tekrok was not quite the brute he pretended to be. She still thought his dream of another war between all races was insanity. Even if all his plans worked out well, the most he could do was cause significant attrition to the Lundari forces sent to take care of him."
    "But if those forces were her human enemies, would that be such a bad thing? Sabia had already resolved to use whatever allies she could find, after all, and Tekrok might be more useful than she had expected."
    "Especially if she could get him to give her more access to his military resources. As she left, Sabia found her strategic considerations interrupted by thoughts about that final glance, and what might be done to convince him..."
    return

label tekrokraidsex:
    $ kiacooldown = False
    scene bg tekroktent
    with dissolve
    if Sabia.armor == Orcslavearmor:
        pass
    else:
        "Sabia had intended to manipulate Tekrok for more support, but as she started to enter, she reflected on the corpses and skulls ornamenting his headquarters."
        "She wasn't going to have much effect on him dressed like this. Better to wear the clothing he'd given her."
        return
    call sabiabase
    show tekrok normal at right
    with dissolve
    if tekroktargetraided:
        "When Sabia entered she found Tekrok alone, but he immediately scowled at her."
        t "What is it, human whore?"
    else:
        "When Sabia entered she found Tekrok alone, but he immediately scowled at her."
        show tekrok angry2 at right
        t "Tekrok doesn't want to see you unless you've done your job, human whore."
    menu:
        "Provoke Tekrok sexually" if dom >= 5:
            $ tekrokraidsexdone = True
            $ sub += 1
            show sabiaemo happy2 at left
            s "You keep calling me a whore, but all you ever do is send me to your men. Afraid of something?"
            show tekrok angry1 at right
            t "Tekrok has better things to do than fuck human sluts."
            show sabiaemo eyebrow1 at left
            s "In a camp full of men? Hmm, I didn't think you the type..."
            show tekrok angry2 at right
            "Tekrok roared and lunged forward, grabbing her throat and slamming her against the wall. Not as hard as he would have if he meant to kill her, though, so Sabia just smirked at the threat."
            t "What game is this, human? Tekrok knows you mean to manipulate him."
            show sabiaemo happy2 at left
            s "You said you wouldn't give me more support because you didn't trust me. Well, I need that support to accomplish anything. I thought maybe I could do something to prove my loyalty."
            show tekrok normal at right
            t "Hmph, and be paid for your body in support? In Tekrok's world, humans will be paid nothing."
            show sabiaemo eyebrow1 at left
            s "Do we live in that world?"
            "Tekrok glowered, but let go of her neck. He still loomed over her, a solid mass of muscle at close range. Sabia gave him a coy smile."
            s "Do you actually mean anything you say, or do you just talk big?"
            show tekrok angry2 at right
            t "Bah! Your words mean nothing - but Tekrok will prove he is more than just talk."
            call TekrokSabiaDom
        "Sub: Submit obediently to Tekrok" if sub >= 5:
            $ tekrokraidsexdone = True
            $ dom -= 1
            $ sub += 3
            show sabiaemo happy3 at left
            s "I need your help, Tekrok. You're withholding help that I need to work for you."
            show tekrok normal at right
            t "Bah. You have earned nothing."
            show sabiaemo closed3 at left
            s "Earning support is something between equals. I thought you considered me just a tool..."
            "Tekrok paused, eyeing her suspiciously. He shifted forward, an ominous mass of muscle looming over her."
            show tekrok angry2 at right
            t "You have given Tekrok no reason to believe you know your proper place."
            show sabiaemo normal at left
            s "I won't submit so easily... but I know you're my only chance. I'll play the role I need to under you."
            show tekrok happy1 at right
            show sabiaemo happy3 at left
            t "Oh? Will you really play every part of that role?"
            s "Yes... you've already used me for your men, why not use me for yourself? I would rather be yours than a bunch of lowly warriors'..."
            show tekrok angry2 at right
            t "Hah. Humans will have no right to such pride when Tekrok's world has come."
            show tekrok happy1 at right
            t "But for now, you are a good tool. If you mean what you say, then prove it!"
            call TekrokSabiaSub
        "Nothing":
            return
    scene bg tekroktent
    call sabiabase
    show tekrok normal at right
    with dissolve
    "Afterward, Sabia lay back and tried to decide if that had been a mistake. In a way it was nothing new, but there was a difference between fucking Tekrok's underlings and fucking the Captain himself."
    "To her surprise, Tekrok shifted. He scowled at her, but his glowering was almost affectionate."
    show tekrok angry2 at right
    t "If you betray Tekrok, the next time Tekrok will make sure you do not enjoy it."
    show sabiaemo happy3 at left
    s "Oh yeah? Maybe I want to see what you got, then."
    show tekrok happy1 at right
    t "Hmph. Say that when you can walk normally."
    show sabiaemo normal at left
    s "...seriously, Tekrok. I went this far, I'm not going to betray you over something stupid like a little village."
    t "Tekrok knows this. You will have your support."
    show sabiaemo closed1 at left
    s "Good. I'll make better use of it than your underlings could."
    show tekrok normal at right
    t "That is probably true. Tekrok's men are strong, but they would throw themselves into the jaws of Lundar for no purpose."
    show sabiaemo irritated2 at left
    s "What, and you're not?"
    show tekrok angry2 at right
    t "Tekrok is no fool, human. Lundar is not as unified as it seems, especially now that you humans believe yourselves the victors. How well can you fight if Nusai turns against Mendahar?"
    s "They've never been the best of allies, but they're no fools. All such conflict would disappear if they thought there was a greater threat from you."
    show tekrok normal at right
    t "Maybe. Unless some provinces of Lundar believed there was a greater threat from the north and others did not."
    show sabiaemo surprised1 at left
    s "The Kingdom of Erxia? Do you seriously have an Erxian contact?"
    "Tekrok eyed her for a long time before answering."
    t "No."
    show sabiaemo normal at left
    show tekrok happy1 at right
    t "No, Tekrok's reach is still limited. But as strong as Lundar is, it is surrounded by enemies. They should not have left so many alive. Now, there is a path for a victory that will leave humans forever serving their rightful masters."
    show sabiaemo closed1 at left
    s "You actually think you can pull off a scheme like that?"
    show tekrok angry2 at right
    t "Tekrok is done talking and done fucking, human. You have no more purpose here. Get out."
    show sabiaemo normal at left
    "She saw real anger in his eyes again, so Sabia hastened to leave. The fact that he had talked to her for that long meant something, though. Maybe he was just more relaxed after sex, like most men, but Sabia wondered if she wasn't gaining some leverage against him."
    "And that plan of using Lundar's enemies to break apart ancient fault lines in the nation... she couldn't let Tekrok do it, but a similar plan might be useful in her hands..."
    $ Tekrokorcs.combat += 2
    $ Tekrokorcs.raid += 2
    $ Tekrokorcs.siege += 1
    return

label tekrokraidevent:
    "The settlement Tekrok had ordered her to attack was so small it didn't even have a name, but in lands this dangerous, it did have a few guards. The peasants themselves could probably use bows, if they had time, so Sabia needed to raid hard and fast."
    menu:
        "Nothing for now":
            return
        "Raid":
            $ tekroktargetraided = True
            $ kiacooldown = False
    "The trickiest part was that Sabia didn't want to trigger reports of an army, so she needed a smaller group that could strike fast..."
    $ reset_armies()
    $ deployarmies(["Raiders",2])
    call deployment
    $ raidreward = 50
    if Raiders.get_deployed() == 0:
        $ raidreward = 25
    if Raiders.get_raid() >= 8:
        $ raidreward += 20
        "The settlement's few guards were no match for Sabia's raiders, who effortlessly smashed their defenses and looted everything they could take. Many of those who saw either hid or didn't fight, so Sabia left them alive."
    elif Raiders.get_raid() >= 4:
        "The settlement's few guards tried to put up a resistance against Sabia's raiders, but were soundly defeated. They were able to loot the settlement while fighting off the guards, then exit cleanly."
    else:
        $ raidreward -= 20
        "It should have been an effortless battle, yet Sabia's soldiers struggled a surprising amount. They managed to loot the settlement, but they took many injuries and even a few casualties from the local guards."
        $ Raiders.injury_random(1,2)
    if Raiders.has_tag("Catgirls"):
        $ raidreward += 10
        "The catgirls proved surprisingly helpful, fast where the orcs were slow and able to easily pin down defenders. The orcs were surprised, but didn't give the catgirls any trouble on the way back."
    "Their success left them with a new problem: how to distribute everything they had looted. Though they had a basic agreement, the orcs seemed to want more, so Sabia had a choice to make..."
    menu:
        "Be generous":
            $ raidreward = int(raidreward / 2)
            $ money += raidreward
            $ L_orcs += 1
            "Sabia gave the raiders more than their usual share, which was a very popular decision. Earned [raidreward] Lundils."
        "Balanced split":
            $ money += raidreward
            "Sabia made an even compromise. Earned [raidreward] Lundils."
        "Be greedy":
            $ raidreward = int(raidreward * 1.5)
            $ money += raidreward
            $ L_orcs -= 1
            "Sabia took most of the money for herself, prompting much grumbling. Earned [raidreward] Lundils."
    "Raid successful, their group returned back to camp. There, that was Tekrok's task out of the way."
    return

label tekrokraidaftermath:
    $ tekrokraidaftermathscene = True
    scene bg tekroktent
    call sabiabase
    show tekrok normal at right
    with dissolve
    "Sabia returned to Tekrok's tent with a smug look on her face. When she saw that he wasn't alone, however, she had to wipe it off and look more subservient."
    s "Captain Tekrok... by pure coincidence, a settlement has been burned to the ground."
    show tekrok happy1 at right
    t "You see, boys? The human whore is good for something after all!"
    show sabiaemo sad2 at left
    show sabiaemo2 blush at left
    "Sabia bowed and flushed... but didn't leave. Tekrok waved a dismissive hand, but she didn't budge. After a moment, he rolled his eyes."
    show tekrok normal at right
    t "Tekrok will have greater tasks for you in the future, human. Tekrok will send along a few more next time."
    "At that, Sabia bowed politely and backed out. He might say it dismissively, but she was sure that he understood the situation. She was more use to him if he actually supported her with proper troops and supplies."
    "On her way out, for a moment Tekrok caught her eye. There was something there that she hadn't expected, a gleam of possessiveness that made her legs feel funny. Sabia hurried out of the tent."
    return

label rokgridraidintro:
    $ Mainarmy.add_troop(Rokgridorcs)
    scene bg rokgridtent
    call sabiabase
    show rokgrid normal at right
    with dissolve
    $ rokgridattackfake = 0
    $ rokgridfakeraidquest = True
    "When Sabia entered Rokgrid's tent, he was speaking with two well-dressed orcs - by which Sabia meant dressed in much of anything. Rokgrid said a few low words to them and they moved out, but Sabia got a decent look at them as they passed. Not local orcs, or at least she didn't think so."
    show rokgrid happy2 at right
    r "Sabia! I know you are quite busy, but we have much to discuss - I hope you can spare at least a little time for it?"
    s "That's why I'm here. I'm starting to move outside the camp and I don't want us to get in each other's way."
    show rokgrid happy3 at right
    r "Oh, I hope we can do quite the opposite! I believe now is an excellent time for us to work together."
    show sabiaemo happy1 at left
    s "What do you have in mind?"
    show rokgrid happy2 at right
    r "For a start, I will assign you a small group of orcs loyal to me. You may use them however you wish!"
    show sabiaemo closed1 at left
    s "That's very generous... a little too generous. What do you want in return?"
    show rokgrid normal at right
    r "I would like you to finish a little task for me. I say \"little\", but it is a tricky matter of no small importance."
    show rokgrid happy2 at right
    r "But first, I must speak of my goals. With the Red God's Arena complete and the new year begun, this is an excellent time to gain control of the warcamp. It cannot be done immediately, but Tekrok's influence must be strangled once and for all."
    show sabiaemo normal at left
    s "So, how do I help with that?"
    show rokgrid normalclosed at right
    "Rokgrid moved closer to her, clasped her arm, and spoke in a conspiratorial whisper."
    r "Tekrok has a group of raiders not officially aligned with him, ones he uses for all manner of secret assignments. Personally, I suspect they were responsible for arranging the group that originally attacked you. I want them eliminated."
    show sabiaemo closed2 at left
    s "I get why you want that, but surely you don't think I can just go kill them."
    show rokgrid normal at right
    r "No, this must be done secretly. Fortunately, we have a unique opportunity. An unusual number of orcs have been disappearing when ranging far from camp lately, and are found killed by animals."
    show sabiaemo irritated2 at left
    s "And you want me to fake one of those attacks? That's difficult, since we couldn't let even one escape. Do you know more about the attacks?"
    r "Since the bodies are usually torn by other animals, there is some room for error. But I would like you to investigate this matter and do your best to make the deaths be beyond suspicion."
    show sabiaemo normal at left
    s "Got it. Other than that, I can use whatever methods I want?"
    show rokgrid happy2 at right
    r "Yes, I trust your judgment. And if that works out, perhaps it can lead to even greater cooperation, hmm?"
    "It gave her a new task to complete, and some serious research and preparation to do, but Sabia thought it reasonable. But though Rokgrid seemed to have other business, she was more curious about bigger issues than this one assignment. Besides, she couldn't let him think of her as a mere flunky."
    show sabiaemo closed1 at left
    s "Is killing off some of Tekrok's agents the full extent of your ambition?"
    show rokgrid happy3 at right
    r "Of course not... but perhaps now is also a good time for me to explain more of my plans."
    show rokgrid normal at right
    r "As you may know, Lundar is continuing to negotiate with unaffiliated regions surrounding it in order to extend its borders. In particular, the lands of Governor Andian."
    show sabiaemo closed2 at left
    s "That's been in the works and uncertain for a long time, though."
    r "Oh, indeed. Another province joining Lundar is a time of both risk and opportunity. But most importantly, it is a time when we cannot have a human-hating brute like Tekrok smashing through any attempts at diplomacy."
    show sabiaemo normal at left
    s "So you're trying to undermine him without throwing the camp into chaos. Fair enough. But do you really think that you'll be able to negotiate with Lundar?"
    show rokgrid happy2 at right
    r "Well, as I have said, I would hope for that. But if not... I do have another plan."
    show rokgrid happy3 at right
    r "Some of the provinces Lundar has recently absorbed have retained a certain degree of autonomy. The governors of the northeast have seemed particularly reasonable, for example."
    show sabiaemo irritated2 at left
    "Sabia raised her eyebrows, but said nothing. Rokgrid was pretty well-informed, if he knew about that. How much control to exert over new provinces was a topic of fierce debate within Lundar, so not easy to meddle with, but it offered him more opportunities than trying to negotiate with the capital."
    show rokgrid happy2 at right
    r "If we can eliminate Tekrok, I think we may be able to strike a deal with a human province for peace. If that province was then accepted into Lundar, and continued its policies of non-aggression... it would offer new paths to peace."
    show sabiaemo normal at left
    s "Wouldn't be easy, but at least that plan isn't completely impossible. But you need Tekrok gone for that to happen."
    show rokgrid normal at right
    r "More than that, it must be done without open conflict. At least, conflict that is not respected in our culture. Though Dajrab may have no designs on the Warchief's throne, he would stand in the way of anyone he believed was trying to tear the tribe in half."
    show sabiaemo happy1 at left
    s "Which is why you need people like me to work secretly. You're not bad, Rokgrid."
    show rokgrid happy2 at right
    "She considered telling him it was almost human, but decided that it might sound condescending. Rokgrid beamed at her compliment, though."
    r "Thank you! I hope we can continue working together for a long time to come... but let's take care of this little matter of Tekrok's men, shall we?"
    "Sabia nodded and left, though she thought Rokgrid was making far too light of his request. She needed to kill a group of trained warriors and make it seem like a believable animal attack. That would be no mean feat."
    "On the other hand, the fact that he was giving her a difficult task of real importance meant that he trusted her. That was a sign she was getting closer to her goals."
    return

label rokgridraidkia:
    $ rokgridraidkia = True
    $ kiacooldown = True
    scene bg road2
    call sabiabase
    with dissolve
    $ rokgridattackfake += 1
    "It took a while to set up properly, but Sabia managed to reach Kia at a time when she was going out to hunt orcs. She seemed very insistent that Sabia stay back, so far back that Sabia only heard the screams and roars as the orcs were killed."
    "But when Sabia caught up, she got what she wanted: a good look at the damage Kia caused. Some of the bodies had been torn apart, but many were killed by claws through the throat or a tail stab in a vital organ. Not like human weapons, but perhaps not so hard to fake, especially given the mess Kia left."
    "Sabia bent down to the corpses, examining the wounds carefully. Yes, they might be able to get close enough that the orcs wouldn't look too closely. Especially since the bodies would be found much later, after some decomposition had taken place."
    show kia tilt1 at right with dissolve
    "While she was bent down, measuring, Sabia realized that Kia was watching her."
    kia "What doing?"
    s "Measuring. I... need claws of my own."
    show kia pawtiltcurious at right with dissolve
    kia "Sabia need claw?"
    s "That's right."
    show kia happy1 at right
    "Kia pointed to her weapon and then looked at Sabia insistently."
    kia "Sabia have claw."
    show sabiaemo closed2 at left
    s "Ah, it's more complicated than that. Sorry, I don't know how to help explain. Claws like yours, not human claws."
    show kia pawtiltcurious at right with dissolve
    kia "Like Kia claws?"
    show sabiaemo normal at left
    s "That's right. Actually... could I take a look at yours?"
    if A_kia >= 5:
        $ A_kia += 1
        $ rokgridattackfake += 2
        show kia tilt1 at right with dissolve
        kia "See claw?"
        show kia happy1 at right with dissolve
        "Kia extended one large paw and Sabia examined the claws carefully. She tried to be careful not to rub Kia's fur the wrong way and to her surprise Kia gave a pleased rumble."
        "After that, Sabia examined her tail, noting the unusual patterns on the spike. Those would be difficult to fake, but not impossible."
        show kia happy2 at right
        "Abruptly, Kia grabbed Sabia's hand. Sabia started to pull back, afraid she'd offended the Makhor... but to her surprise, Kia began to stroke her hands in a similar way that Sabia had to her, rumbling happily."
        kia "Sabia sit!"
        "Not willing to contradict the eager Makhor, Sabia spent a while with her, stroking each others hands. As dangerous as they were, Kia's touch was gentle, and her fur was quite soft."
        "It wasn't so bad... but more importantly, Sabia had plenty of information to fake an attack."
    else:
        "Kia seemed to consider the matter for a long time, long enough that Sabia wasn't sure if she understood, then abruptly she shook her head in a flurry of hair."
        show kia irritated1 at right with dissolve
        kia "Not touch claws."
        menu:
            "Try anyway":
                $ A_kia -= 1
                $ rokgridattackfake += 1
                s "Oh, come on, I just want to s-"
                show kia angry5 at right with dissolve
                show sabiaemo surprised1 at left
                "A moment later, Sabia found herself slammed on her back with the wind knocked out of her lungs. Kia's hand was flattened on her stomach, claws digging into her skin barely gently enough not to draw blood."
                kia "Not!"
                hide kia angry5 at right with moveoutright
                "With an ominous growl, Kia let go and then ran off, disappearing into the grasses. Sabia took a long time to catch her breath before getting up."
                show sabiaemo closed2 at left
                "Still, she'd gotten some information about what the corpses looked like. That would prove useful."
            "Let it go":
                $ A_kia += 1
                show sabiaemo closed1 at left
                s "Okay... if you say so, I won't."
                show kia normal1 at right
                "Kia nodded seriously. Sabia sighed and decided to try something else."
                show sabiaemo normal at left
                s "Do you want to see my claw?"
                show kia pawtiltconfused at right with dissolve
                kia "Human claw?"
                "Sabia extended her weapon and Kia took it between two fingers, as if it was a curious object. She peered at it for a while and bit it a few times, but then seemed to grow bored."
                show kia happy2 at right with dissolve
                "Dropping the weapon in front of Sabia, Kia hopped up to put her paws on her shoulders and licked her face. After that, she was off like a shot, disappearing into the grasses."
                hide kia happy2 at right with moveoutright
                "Her gambit to get more information on Kia's claws might have failed, but Sabia had gotten a good look at the corpses she left behind. That would prove useful."
    return

label rokgridraidevent:
    "It wasn't too difficult to find the group of Tekrok's orcs that Rokgrid wanted her to kill, but before she did anything Sabia wanted to be damn sure she was prepared..."
    menu:
        "Nothing for now":
            return
        "Eliminate them":
            $ rokgridraiddone = True
            $ kiacooldown = False
    "The group of Tekrok's agents wasn't very large or well-armed by orc raiding standards, but the point wasn't just to beat them. They needed to be killed quickly without any survivors, then effectively faked to be because of monster attacks."
    "Sabia decided to send two forces to attack from opposite sides, while holding the rest back to make sure that there would be no survivors."
    $ reset_armies()
    $ deployarmies(["Attackers",2],["Sweepers",3])
    call deployment
    if Attackers.get_deployed() == 0:
        $ rokgridattackfake -= 1
    if Sweepers.get_deployed() == 0:
        $ rokgridattackfake -= 1
    if Sweepers.get_raid() >= 1:
        $ rokgridtargetkilled = True
    else:
        $ rokgridattackfake -= 1
        "Without sufficient forces to kill off any stragglers, Sabia considered the whole project a non-starter. And she wasn't doing herself any favors by shuffling her troops around in a nearby area. She'd have to try again later."
        return
    if Attackers.get_combat() >= 5:
        $ rokgridattackfake += 1
        "The fight was short and brutal. Fortunately, her forces were more than up to the task and quickly killed the majority of Tekrok's agents."
    else:
        "The fight was short and brutal. Unfortunately, some of her own forces were injured in the battle and one warrior was killed. He'd need to be removed later to avoid any suspicions."
        $ Attackers.injury_random(1,2)
    if Sweepers.get_raid() >= 4:
        $ rokgridattackfake += 1
        "Most importantly, the few who escaped the main fight were killed before they could get far by her backup forces."
    else:
        "Most importantly, there were no survivors. Those who escaped the main fight got further than she would have liked, but her forces managed to run them down in the end."
    if rokgridattackfake >= 5:
        $ A_rokgrid += 2
        $ L_orcs += 1
        "Sabia then began to tamper with the evidence on the battlefield, using everything she'd learned from Kia to make sure it was faked well. Her men had used blunt weapons, which she hoped wouldn't be too unusual given how Kia fought, and the slashes and stab wounds would be perfect."
        "All in all, she thought the operation couldn't have gone much better. Her men seemed to agree."
    elif rokgridattackfake >= 3:
        $ A_rokgrid += 1
        "Sabia then began to tamper with the evidence on the battlefield, using what she'd learned from Kia to make sure it was faked well. Her men had used blunt weapons, which she hoped wouldn't be too unusual given how Kia fought, and the slashes and stab wounds would be perfect."
        "It wasn't a perfect job, but it would probably pass inspection by the time any other orcs went looking for them."
    elif rokgridattackfake >= 2:
        "Sabia then began to tamper with the evidence to make it look like an attack of monsters or wild animals. She thought it would probably pass inspection by the time any other orcs went looking for them."
    elif rokgridattackfake >= 1:
        $ A_rokgrid -= 1
        $ L_orcs -= 2
        "Sabia then began to tamper with the evidence to make it look like an attack of monsters or wild animals, but given how poorly things had gone, it was a rough job. She would have to hope they weren't discovered until the bodies had decomposed more."
    else:
        $ A_rokgrid -= 2
        $ L_orcs -= 4
        "Sabia then began to tamper with the evidence to make it look like an attack of monsters or wild animals, but given how poorly things had gone, it was a nearly impossible job. She would have to pray they weren't discovered until the bodies had decomposed most of the way."
    "In the end, as she returned to camp, what mattered to her was that she'd done Rokgrid's task and gained more freedom to move as she wanted."
    return

label rokgridraidaftermath:
    scene bg rokgridtent
    with dissolve
    if Sabia.armor == Barmaidclothes:
        $ rokgridraidaftermathdone = True
    else:
        "As Sabia approached Rokgrid's tent, she caught a glimpse of him inside. He had set things up differently, some kind of formal dinner at a table."
        "While she watched, Sabia saw Rokgrid fussing with the positioning of the silverware, as if to ensure that everything was perfectly in place. It was obvious that he was taking this very seriously as a formal event."
        "Though Sabia had hated her mother's lessons in decorum, they'd serve her well here. A dress would make a real impact on Rokgrid... but she didn't have a dress. Wearing something inappropriate would be missing a chance to earn a lot of loyalty from him."
        "Her options were limited, but Sabia decided she should come back wearing something distinctly human..."
        return
    $ Rokgridorcs.combat += 1
    $ Rokgridorcs.defense += 1
    $ Rokgridorcs.diplomacy += 2
    $ Rokgridorcs.siege += 1
    $ kiacooldown = False
    call sabiabase
    show rokgrid happy2 at right
    with dissolve
    if rokgridattackfake >= 2:
        pass
    else:
        $ Rokgridorcs.diplomacy -= 1
        "Rokgrid smiled at her when she entered, but his smile was somewhat brittle."
        r "So, it is done."
        s "I did what you asked."
        r "I am glad Tekrok's men are dead, but it sounded poorly done. We will have to pray that our work is not discovered."
        s "But I did the job, right?"
        r "Yes. In exchange, I will further supply the warriors I sent to you. But now please leave me be - I have a great deal of work to do in order to make sure this cannot come back to bite us."
        "Sabia shrugged and left his tent. She'd gotten what she wanted."
        return
    "Rokgrid's tent was usually well lit by lanterns, so Sabia was surprised to find it much more softly lit by candles. Not only that, the usual furnishings had been replaced by a table she hadn't seen before - actually not a bad one, lacquered in a recent style that had been popular in Rhaetia."
    show rokgrid happy4 at right
    r "Sabia. I would invite you to a celebratory dinner... for no particular reason whatsoever, of course."
    show sabiaemo happy2 at left
    s "Ah, I see. It's a wonderful coincidence that I just happened to return from my walk in time for it."
    show rokgrid happy2 at right
    r "Yes, we have been quite fortunate lately. Please, join me."
    show sabiaemo happy1 at left
    "Smiling despite herself, Sabia took the seat he offered. It was ridiculously unsubtle, but that was clearly not the point. Rokgrid seemed quite pleased by her success, hurrying to sit opposite her."
    r "There are severe limitations in the fare I can offer, but I have done my best..."
    "Rokgrid was being modest - Sabia was trying to avoid salivating over what looked like the first good meal she'd had since she'd left Lundar. Her sister might have turned her nose up at the roughness of the stuffed pheasant and eggs, but they looked to be well-prepared."
    "And if the steak was rather orcish, Sabia had grown to tolerate orc meat, and this looked to be of far higher quality than the usual."
    show sabiaemo happy3 at left
    s "This is impressive, Rokgrid. I don't think I can hold back."
    "She didn't, either, tucking into the food with all the hunger of her raiding and more besides. It might have been unladylike, but par for the course when it came to soldiers, who ate what they could get because they might not get another chance. Rokgrid took a more moderate approach, dining almost like a human."
    show rokgrid normal at right
    r "My warriors reported no difficulties - I hope there was nothing they missed?"
    show sabiaemo normal at left
    s "No, it went quite smoothly."
    show rokgrid happy2 at right
    r "Good. In that case, there is no more need to talk of such simple business! Let me offer a toast to a job well done!"
    "He had poured two glasses of wine for them, so Sabia took one and returned the toast. She took a sip, expecting some orc take on wine, but was surprised to find it tasted completely human."
    show sabiaemo happy1 at left
    s "So, if we aren't talking of simple business... what's next?"
    show rokgrid happy3 at right
    r "Just back from the campaign trail and already eager for more? You're quite ambitious."
    show sabiaemo closed1 at left
    s "You have to be, in Lundar."
    show rokgrid happy2 at right
    r "Yes, I'd thought that. My people often think of human cultures as weak, but I've often thought that human nobles seemed more cutthroat than orcs. What do you think?"
    "Sabia chewed on that question for a little while, simultaneously chewing on her steak. It really was quite good... she knew she'd be overeating before the night was over."
    show sabiaemo normal at left
    s "It depends on your position in society, I think. The more power your family has, the less room there is for mercy."
    show rokgrid normal at right
    r "Hmm, fascinating. And your family has a great deal of power, does it not?"
    show sabiaemo closed1 at left
    s "We're not in line for the throne, but yes. My mother is a very influential Archmage, my sister is of course her clone, and my father is a general."
    r "Took more after him, did you?"
    show sabiaemo closed2 at left
    s "I suppose so."
    "Though Rokgrid seemed to be honestly interested instead of delving for information, the potential for it made Sabia wary. He was smarter than he looked and might be able to play the simple orc. Besides, she preferred not to discuss her family."
    show sabiaemo happy1 at left
    s "What about you? There aren't any hereditary orc positions, are there?"
    show rokgrid normalclosed at right
    r "It would certainly go against our values. Truthfully, there are some families that are considered more spiritual than others, so the council of shamans is less diverse than you might hope."
    show sabiaemo normal at left
    s "How did you end up as a Captain, then? Can't have been easy, acting... as you do."
    show rokgrid normal at right
    "She worried that she might have offended Rokgrid with that, but he simply looked thoughtful."
    r "It was easier than you might think. Many orcs are proud, but some are realists. They know that Lundar is the dominant force in our world, and that we must adapt in order to survive."
    show rokgrid happy2 at right
    r "But to answer your question... it was something that I wanted from a young age. One of the Captains of a previous generation was quite a brute, ruling by virtue of strength of arms alone. He wanted my sister, and though she did not care for him, no one dared oppose him."
    show sabiaemo sad1 at left
    s "Oh... did he...?"
    show rokgrid happy3 at right
    r "Heh, no. My sister tore out one of his tusks and spat it down his throat."
    show sabiaemo happy1 at left
    s "She sounds impressive. Is she with the council of shamans now?"
    show rokgrid sad1 at right
    r "I fear not. It has been many years since she died of an illness."
    show sabiaemo sad1 at left
    s "Oh. I'm sorry to hear that."
    show rokgrid normalclosed at right
    r "Thank you... but I did not mean to speak of this. Truthfully, my reasons are far more ideological, I just... drifted into memories instead..."
    "He was silent for a moment, less composed than Sabia had ever seen him. Eventually his eyes lit up again, though he remained serious."
    show rokgrid normal at right
    r "There was no great inciting incident. I merely saw that my people would continue to lose to humans unless we changed. So I grew strong, took the strengths of Lundar that I could, and obtained a position where I could be a better leader than those in my youth."
    show sabiaemo normal at left
    s "You've come a long way, then. Also, that's a very nice suit of armor."
    show rokgrid happy2 at right
    r "Thank you for saying so! There was an elven slave in a nearby town who would cooperate with me. He convinced his master to forge the armor to my specifications. Sadly, he was killed before he could convey my order for a matching sword."
    show sabiaemo closed2 at left
    s "Ah, that's a pity."
    "Meanwhile, Sabia tucked that piece of information away in her head. Rokgrid seemed eager to talk, only eating a little, so Sabia took another serving and kept eating. She was mostly satisfied now, but it was so good..."
    show rokgrid sad1 at right
    r "Sabia... I know you are still bound nearby because your raiders are orcs, but a woman of your ambition will not stay here long. When you get enough power to leave, will you?"
    show sabiaemo closed1 at left
    s "...no, at least not right away. Just going back to Lundar wouldn't solve my problem, even if my family isn't ready for me. I need to be much better prepared."
    r "I am... glad to hear that. And not only because I believe you will be a valuable ally in the coming conflicts."
    show rokgrid normalclosed at right
    "Rokgrid twisted his fork in a strange way... was he nervous? Sabia observed him more carefully while pretending to focus only on her food. Her social skills weren't excellent, and Rokgrid had decent control of his face, but she could see the tension in his body."
    show rokgrid normal at right
    r "There is one thing I wish to get out of the way quickly. I have a great many irons in the fire, so my resources are stretched thin. But thanks to your success, I can now assign more of them to work under you. They are yours regardless of anything else."
    show sabiaemo irritated1 at left
    s "Rokgrid, just what is this really about?"
    r "I am not naive, Sabia. I know that in my lifetime, the most I can hope for between orcs and humans is tolerance. But still..."
    show rokgrid sad1 at right
    "His free hand moved across the table and touched hers, making Sabia freeze for a moment before she suppressed her surprise."
    r "I know there is no real future for us together, perhaps not even as allies. But for now... is it too much to hope we could be more than that?"
    show sabiaemo normal at left
    "Sabia bought time by giving him a neutral smile. It was obvious what he was suggesting, and just as obvious that she only had a few choices. Refusing him would be downright stupid - even if he took rejection well, she would be turning down a chance for significantly more influence."
    "And truthfully, part of her thought it didn't sound so bad. Or maybe it was just the fact that she was high from her victory, full of wine, and feeling deeply satisfied from all the food."
    show sabiaemo closed2 at left
    "Still..."
    menu:
        "Refuse":
            $ A_rokgrid -= 1
            show sabiaemo closed4 at left
            s "Rokgrid, I'm sorry. I can't say what you want to hear."
            show rokgrid normalclosed at right
            r "I see."
            "He withdrew his hands from hers and his eyes grew cooler, but at least he didn't lash out in rage."
            show rokgrid normal at right
            r "That is, of course, your decision. I hope that we can continue to work together effectively."
            show sabiaemo closed2 at left
            s "Of course."
            r "Then please, eat as long as you like. You deserve it."
            hide rokgrid normal with moveoutright
            "With that, he rose from the table and left swiftly. Sabia frowned after him, still eating but now rather distracted. She didn't fear a severe reaction from him, but she'd no doubt upset him considerably."
            show sabiaemo normal at left
            "Worth it, she decided. Sabia ate alone until she was full."
            return
        "Accept solely for political advantage":
            $ A_rokgrid += 1
            "Rokgrid's naked emotion irritated her, but Sabia decided that she needed to take advantage of it. She let her smile grow warmer and tried to pretend well enough to fool him."
        "Make the best of it":
            $ A_rokgrid += 3
            "He might be an orc, but Rokgrid had just treated her better than a lot of men she'd known. Sabia found herself smiling despite herself."
    $ rokgridsecondraidmeal = True
    show sabiaemo happy1 at left
    s "You're right, it can't last. But that doesn't mean we can't have something now."
    show rokgrid happy2 at right
    "She saw his eyes light up when she spoke and his hand gripped hers more tightly. He seemed to be restraining himself to stay in his seat."
    r "I do not want to interrupt a warrior's hunger, but..."
    show sabiaemo lick1 at left
    s "Oh, I've been going without more than food..."
    call RokgridSabiaA
    scene bg black with dissolve
    "After he had sated himself, Rokgrid lay back drowsily. But one of his hands reached out, sliding along her thigh."
    r "Must this be... only one time?"
    s "Why hold back?"
    "There was only one real option after coming this far - and besides, she could always just not take him up on it in the future. Apparently satisfied with that, Rokgrid quickly fell into a deep sleep."
    "Though she had gotten caught up in the pleasure of it, Sabia was fully back in reality, regardless of how she'd played affectionate with him. She pulled out of his arm and sat up in bed, staring down at him and reflecting on what had just happened."
    "She had her reasons, of course, but also a tangle of emotions. In the end, Sabia felt..."
    menu:
        "Affection":
            $ freedom += 1
            $ A_rokgrid += 1
            "Strange though it was, Sabia found herself with a warm affection for Rokgrid. It would never work between them, of course, but she didn't regret it."
            "Most likely, this time had earned her enough loyalty from Rokgrid. But maybe in the future it wouldn't be so bad to use him from time to time."
        "Nothing":
            "As hot as she had been not long ago, now Sabia felt only a cool consideration. She'd made the logical choice. That was all. Perhaps she could use it as leverage against him in the future."
            "Most likely, this time had earned her enough loyalty from Rokgrid. If she needed more, she could always use her body again."
        "Disgust":
            $ slavery += 1
            "The sex might have been satisfying, but Sabia found herself repulsed by the orc and his immitation of humanity. This changed nothing. At most, perhaps it would persuade her that some orcs could be kept as personal servants."
            "Most likely, this time had earned her enough loyalty from Rokgrid. She hoped she wouldn't need to fake any more encounters with him, but would do what was necessary to keep him as a useful tool."
    "For now, though, all she wanted to do was sleep off all that delicious food..."
    return

label rokgridraidsex:
    menu:
        "Initiate sex":
            call RokgridSabiaC
        "Let Rokgrid lead":
            call RokgridSabiaB
    return

label dajrabraidintro:
    $ Mainarmy.add_troop(Dajraborcs)
    scene bg dajrabtent
    call sabiabase
    with dissolve
    $ dajrabraidintroduced = True
    "When Sabia entered Dajrab's tent... he wasn't there. She blinked for a moment, staring over the dimly lit space."
    "Part of her was tempted to take the opportunity to look through his things, but Sabia decided against it. There was too much chance that his tent was defended in some way or that she was being watched. So instead, she turned around to go."
    show dajrab normalclosed at right with dissolve
    "And discovered that she was indeed being watched, by Dajrab himself. He was entering not long after her, not acknowledging that anything was different than normal."
    show dajrab normalopen at right
    d "Do you need something, Sabia?"
    s "We need to discuss the terms of our alliance. I will be working further from camp, with both the risks and advantages that involves."
    show dajrab normalclosed at right
    d "Indeed. The primary thing I ask of you is not to disturb the stability of our tribe, but I do not know if I can ask that."
    show sabiaemo closed2 at left
    s "I'll try not to cause you any trouble."
    show dajrab normalopen at right
    d "In any case, I presume you are looking for more troops?"
    show sabiaemo normal at left
    s "I hoped so, yes."
    show dajrab normalclosed at right
    d "Then I propose a simple deal: I will give you a small contingent of soldiers to assist you as you see fit. In return, I would like you to bring your own raiders to assist me in a task. Once it is complete, I will grant you more resources."
    show sabiaemo closed1 at left
    s "Sounds fair. What's the task?"
    show dajrab normalopen at right
    d "A merchant caravan will be coming from Vegardan lands. They are taking a considerable risk venturing into ours, so it is essential that they are well-guarded."
    show sabiaemo normal at left
    s "So you need me to do that, huh? What are they bringing?"
    show dajrab normalclosed at right
    d "Normal goods. The purpose of this venture is more to forge a working relationship with them, than to acquire anything important."
    "Sabia wasn't sure she believed that, but she nodded anyway. As usual, she could trust Dajrab to offer her a straightforward deal and not waste her time."
    show sabiaemo closed3 at left
    s "I'll gladly accept the deal, then. You'll need to give me some time to prepare my troops, however - is there a deadline for meeting this caravan?"
    d "They will be working in Vegardan lands until we can meet them, so not really."
    "With that Dajrab nodded to her and turned away. Sabia nodded back and left, considering her options..."
    return

label dajrabraidevent:
    "Helping guard Dajrab's caravan would be quite a trip, and Sabia wanted to be prepared before she joined the guards..."
    menu:
        "Nothing for now":
            return
        "Raid":
            $ dajrabcaravanfinished = True
            $ kiacooldown = False
    scene bg road
    call sabiabase
    with dissolve
    "The first leg of the trip to Vegardan lands was bound to be mostly boring, since they were a well-armed group guarding nothing in particular. Sabia was surprised to find that Dajrab and some of his orcs came along as well, but otherwise it was uneventful."
    "She made sure her men were getting along well enough, but otherwise things progressed in an ordinary fashion. Almost boring, actually."
    show neve1 at right
    show neveemo normal at right
    with moveinright
    "Until, to her surprise, Neve showed up at the edge of camp one day."
    show sabiaemo surprised1 at left
    s "Neve? Why are you here? Is this more political than it seems?"
    show neveemo happy3 at right
    n "Heh, relax, Sabia. This is indeed just a simple guard assignment - Dajrab doesn't get involved in schemes like that."
    show sabiaemo normal at left
    s "Hmm, okay. Then why follow us?"
    show neveemo happy1 at right
    n "Just curious how far you're going to go into Vegardan lands. I don't want to ask Dajrab."
    s "We're just supposed to be meeting our contacts on the border. Why, do you know someone there?"
    show neveemo closed1 at right
    n "My betrothed, the prince of the Vegardan elves."
    show sabiaemo irritated2 at left
    s "Wait, really?"
    show neveemo eyeroll2 at right
    n "Haha, no. I'm just messing with you."
    show sabiaemo happy2 at left
    s "I figured."
    show neveemo normal at right
    n "In all seriousness, I have a lot of concerns there. I haven't been back in years, but I try to keep track of people."
    show neveemo closed1 at right
    n "For one, I'm wondering if the Vegardans are actually intending to develop trade across the Eskra. That would be a change, and it might mean something has shifted back there."
    show sabiaemo normal at left
    s "They don't trade with anyone in the Sorthyos region, really?"
    show neveemo normal at right
    n "Not usually. There's some basic trade with Arwans to the north, and more exotic goods with Carchedon and a few tribes in the Xhan. Going west could mean getting entangled with Lundar."
    show neveemo closed3 at right
    n "But more importantly, it would indicate a change in the balance. The strongest powers in Vegardan lands have always been the sea lords. The three strongest have made a truce between them that keeps the lesser sea lords in balance, with the land-based powers being secondary in nature."
    show sabiaemo eyebrow1 at left
    s "Wow, you didn't even try to stick to the story that the sea lords are pirates unaffiliated with Vegard, huh?"
    show neveemo eyeroll1 at right
    n "Oh, please, it's an open secret."
    show neveemo normal at right
    n "But there's a difference between raiding the seas and getting involved with anything further inland. Most groups have no real navy, while Erxia and Carchedon can only control nearby waters. But a land assault..."
    show sabiaemo normal at left
    s "Lundar has definitely thought about it, but there's a lot of territory and the Eskra in the way."
    show neveemo happy1 at right
    n "As it's been for a long time. So the sea lords are safe for now."
    "There was something about the way she said it that made Sabia curious."
    show sabiaemo closed2 at left
    s "You're concerned for their safety? That didn't sound like it was a sentiment of loyalty to your homeland."
    show neveemo happy3 at right
    n "Hah, no. But I once had a dear friend who... took a different path in life. I hope she's doing well, so I try to hear stories of her when I can."
    show sabiaemo surprised1 at left
    s "Wait, stories of her? Exactly who is she?"
    show neveemo closed2 at right
    n "By the way, if you're going to cross the river, keep an eye out for the The Butcher King of Bronze. He likes to make surprise raids up the river, sometimes."
    "Neve casually dropped the name of a feared pirate lord, one of the three sea lords of Vegard, as if he was a friend. There was a curve to her lips that suggested she was playing with Sabia a bit, but Sabia thought she also saw sincerity deep within her eyes. Whoever her friend was, they really had been close."
    show sabiaemo closed4 at left
    s "You're not going to tell me any more, are you?"
    show neveemo happy3 at right
    n "Nope. But can you tell me everything about your little trip?"
    show sabiaemo closed2 at left
    show neveemo normal at right
    s "Hmm..."
    menu:
        "Keep quiet about things":
            show sabiaemo normal at left
            s "Sorry, but Dajrab doesn't tell me much."
            n "That's usually how he works. Well, I figured I would ask."
        "Tell Neve about the trade plans":
            $ A_neve += 1
            show sabiaemo normal at left
            "Sabia explained everything Dajrab had told her, especially about possible increased trade in the future. Neve nodded thoughtfully."
            show neveemo closed1 at right
            n "I see. Perhaps not so destabilizing, but worth considering. I'll see what happens if you bring the caravan back safely."
            s "Well, that's all I know. I hope it helped."
            show neveemo happy1 at right
            n "Yes, it did. Thank you, Sabia."
    show sabiaemo normal at left
    s "So... are you planning to stick around? You're not coming all the way with us, are you?"
    show neveemo happy1 at right
    n "No, I just wanted to see you off. But I've come this far, I think I'll stick around if I'm not any trouble."
    show sabiaemo happy1 at left
    s "Feel free!"
    "So that night, Neve joined the campfire with Sabia's men. She was surprisingly popular with the warriors... or, on second thought, that wasn't very surprising."
    "What Sabia hadn't expected was that Neve actually seemed to get along with them. Some of the orcs ogled her, but she didn't seem to mind and teased them right back. Dajrab's forces were very respectful, speaking to her as another warrior. And Sabia discovered that Neve could drink truly enormous amounts of alcohol without getting drunk, which the orcs seemed to approve of greatly."
    "Eventually most were asleep and the fire was burning low. Sabia took the first watch and found Neve sitting beside her."
    show sabiaemo normal at left
    s "Seemed like you were having fun."
    show neveemo happy2 at right
    n "Yeah, they're a decent bunch."
    show sabiaemo closed3 at left
    s "You seem to get along well with so many orcs - what do you have against Tekrok, then?"
    show neveemo closed1 at right
    n "You've heard about his plans for creating an alliance of all other races to defeat Lundar, right?"
    show sabiaemo normal at left
    s "Yes, I had some idea. And he wants you involved?"
    show neveemo closed3 at right
    n "He wants me as his damn queen. A symbol of unity between races and all that. Far too ridiculous for my taste."
    show neveemo eyeroll1 at right
    n "I don't mind a little romance, I'll even let a man kiss me if he's a good enough fuck. But Tekrok's ideas of a king and queen leading a multi-racial army... that's too sweet for my taste."
    show sabiaemo eyebrow1 at left
    s "Huh, he doesn't seem the type."
    show neveemo eyeroll2 at right
    n "Don't be fooled by appearances, Sabia. Of course, you should really know that by now."
    s "Yes, I suppose so."
    show sabiaemo happy1 at left
    show neveemo happy2 at right
    "They chatted lightly until the end of Sabia's shift, when Neve smiled at her and slipped way into the darkness."
    "Sabia was tired, but didn't get to sleep immediately. Instead, she found herself wondering if Neve had any family in Vegardan lands, and what it might be like to meet them..."
    scene bg black
    pause 3
    scene bg countryside
    call sabiabase
    with dissolve
    "The next day, they began their march in earnest. There were no more surprise guests, which made things rather routine. She thought that her units bonded a little better, which would be good for morale, but the trip was uneventful."
    "Sabia had been looking forward to seeing more Vegardan elves, particularly if any of them had connections to Neve, but to her disappointment she didn't get a chance. Instead they met a group of human and orc merchants already across the river, only one male Vegardan elf briefly present to negotiate final details with Dajrab."
    "Since there was nothing she could earn from getting involved with that, Sabia instead went to examine the caravan itself. The wagons were sturdy and well-built, more orcish than elvish, but she was more interested in their contents."
    "As far as she could tell, it really was just ordinary goods. Some raw ore, some rare leather and furs, a few drinks that orcs valued. Reasonably valuable, no doubt a profit for all sides, but nothing remarkable."
    "Of course, it was possible that the valuable cargo was much smaller and impossible to find by a simple search. But that could always be true, and at least she wasn't helping guard anything illegal or otherwise troublesome."
    "They then turned around and headed back, just like that. It was almost boring, and Sabia found herself lulled into a sense of complacency."
    "Then, with almost no warning, their trip went from sedate to an attack. Sabia lurched into action."
    "The bandits hit the other side of the caravan and were blocked by other guards, but there was a group assembling on a nearby hill, ready to rain arrows down on the defenders' flank."
    "Sabia needed to send a group strong enough to endure their fire and take them down... but she couldn't afford to send all the troops she had. With only a moment to give orders, Sabia made her decision..."
    $ reset_armies()
    $ deployarmies(["Archer Assault",3])
    call deployment
    if ArcherAssault.get_deployed() == 0:
        $ dajrabraidperformance -= 1
    if ArcherAssault.get_defense() >= 5:
        $ dajrabraidperformance += 1
        "Her forces rushed the archers quickly, avoiding most of the arrows before the bandits could change their plans. Sabia watched with some satisfaction as the ambush group was butchered."
    else:
        "Her forces charged the archers, taking heavy injuries as they took the hill. Sabia winced at the losses, but the archers didn't have a strong enough position to avoid being overcome."
        $ ArcherAssault.injury_random(2,2)
    "But just as the archers went down, another group of bandits attacked straight for the heart of the caravan. Had both been feints to split them up? These bandits were far more prepared and organized than she would have expected."
    "Most importantly, there was no time for her forces or any of the other guards to return. She had to work with the guards she had and face the bandits in raw combat."
    $ deployarmies(["Caravan Defense",3])
    call deployment
    if CaravanDefense.get_deployed() == 0:
        $ dajrabraidperformance -= 1
    if CaravanDefense.get_combat() >= 5:
        $ dajrabraidperformance += 2
    elif CaravanDefense.get_combat() >= 3:
        $ dajrabraidperformance += 1
    elif CaravanDefense.get_combat() >= 1:
        pass
    else:
        $ dajrabraidperformance -= 1
    if CaravanDefense.get_defense() >= 5:
        $ dajrabraidperformance += 2
    elif CaravanDefense.get_defense() >= 3:
        $ dajrabraidperformance += 1
    elif CaravanDefense.get_defense() >= 1:
        pass
    else:
        $ dajrabraidperformance -= 1
    if dajrabraidperformance >= 1:
        "Sabia had expected a mere raid, but the bandits clashed with the defenders with surprising ferocity. It was an actual battle - for a moment both sides engaged in a melee without the ability to tell the victor."
    else:
        "As the bandits smashed through the feeble remaining defenses, Sabia realized how horribly she'd miscalculated. But it was too late."
        "The bandits reached her position first with a hail of arrows, then they closed with knives. She raised her weapon, but the knife took her in the back..."
        show gameover with dissolve
        pause 3
        $ renpy.full_restart()
        return
    if dajrabraidperformance >= 5:
        $ A_dajrab += 2
        "Eventually the outcome became clear: her forces had soundly defeated the enemy. Despite the viciousness of the battle, they had overwhelmed the bandits without taking any serious losses."
        "Unfortunately, no matter how well they fought, her forces could only hold part of the line. On the other end of the line, the primary bandit attack was overcoming the other hired guards..."
    elif dajrabraidperformance >= 3:
        $ A_dajrab += 1
        "Eventually the outcome became clear: her forces had rebuffed the bandits with only a few losses of their own. They'd take some time to recover, but they'd done much worse to the enemy."
        $ CaravanDefense.injury_random(1,2)
        "Unfortunately, her forces could only hold part of the line. Beside her position, the primary bandit attack was overcoming the other hired guards..."
    else:
        "Eventually the outcome became clear: her forces were victorious, but at a heavy cost. They took heavy injuries before they drove off the majority of the bandits, but they hadn't managed to defeat them all."
        $ CaravanDefense.injury_random(2,2)
    "A group of bandits broke through, rushing the wagons, and Sabia froze. Standing and fighting seemed foolish, but what would happen to the caravan if she retreated?"
    show dajrab normalclosed at right with moveinright
    "Before she could make a decision, Dajrab emerged from the lead wagon and marched out to meet them without the slightest hint of fear."
    d "Enough, bandits. If you go further, Dajrab will face you."
    "He met the first of the bandits, one moving fast and carrying a jagged sword. Dajrab's movements were slow and Sabia wondered how he was going to deal with it... except that he didn't. The bandit slashed him across the neck."
    show dajrab normal at right
    show sabiaemo surprised1 at left
    "And it did nothing."
    "The bandit froze in shock at the sight of his attack being useless, and in that time Dajrab cut him down with a brutal chop. It was a reasonably good attack, but nothing special - the real question was how in the hell he had just shrugged off that attack."
    "Other bandits hesitated at the sight, so Dajrab set about killing them. A few others attacked and got in blows, but they seemed to do nothing."
    show sabiaemo closed2 at left
    "How the hell was that possible? Orc magic was good at enhancing a warrior's strength, but she had only heard rumors of warriors who had bodies like iron. Was that what he had earned through all the scars covering his body?"
    show dajrab normalclosed at right
    "In any case, the battle ended very soon, the bandits drawing back. Dajrab didn't give chase, instead gesturing for the backup forces to follow and defeat them."
    show dajrab normalopen at right
    show sabiaemo normal at left
    d "Dajrab has struck the first blow. Dajrab trusts you can do the rest."
    show dajrab normalclosed at right
    "His forces charged out with a loud roar, partially a battlecry and partially cheering for their Captain."
    hide dajrab normalclosed with moveoutright
    "Dajrab disappeared into one of the wagons again, but Sabia was left thoughtful. Perhaps there would be more advantages to picking him as her Captain than she expected."
    "The attack stopped the caravan for a time even though they needed to press on to get out of the bandits' territory. There were injured to look after and wagons to check."
    "The orcs were also quite happy to loot from the bandit corpses. They might not have been carrying much money, but they did have good weapons and some armor that the orcs now considered theirs."
    if dajrabraidperformance >= 5:
        $ money += 100
        $ L_orcs += 2
        "To Sabia's surprise, the orcs brought her a share of the loot without being asked. The equipment struck her as too poor in quality for her to use, not to mention filthy, but she managed to sell it to traders with them for 100 Lundils."
    elif dajrabraidperformance >= 3:
        $ money += 50
        $ L_orcs += 1
        "To Sabia's surprise, the orcs brought her a share of the loot without being asked. The equipment struck her as too poor in quality for her to use, not to mention filthy, but she managed to sell it to traders with them for 50 Lundils."
    else:
        "Given how poorly the attack had gone, however, they needed to hurry on and had little time for looting."
    "For the rest of their journey home, Sabia was constantly tense and ready for another attack, but none came. It occurred to her that Dajrab had likely hired all the extra warriors not as a general precaution, but to prepare for this attack in particular."
    "She wondered just how much he knew about the local bandit situation, but doubted he would share too much information. Still, she'd done what he wanted - once they got back to camp, she needed to talk to Captain Dajrab."
    return

label dajrabraidaftermath:
    $ Dajraborcs.combat += 1
    $ Dajraborcs.defense += 1
    $ Dajraborcs.raid += 1
    $ Dajraborcs.diplomacy += 1
    $ Dajraborcs.magic += 2
    $ dajrabraidaftermathscene = True
    scene bg dajrabtent
    call sabiabase
    show dajrab normalclosed at right
    with dissolve
    "Once the caravan was fully settled, Sabia found Dajrab in his tent. He gave her a respectful nod."
    d "Sabia."
    show sabiaemo happy1 at left
    s "Our deal was that you'd reinforce my troops now, right?"
    show dajrab happy at right
    d "Indeed, you have more than earned it. I have already given the orders for more of my men to join yours. You will also find these to have some magical training."
    show sabiaemo happy3 at left
    s "Really? I assume not enough to cast spells, but..."
    show dajrab normalopen at right
    d "Their rituals will leave them inexhaustible, difficult to injure, and less vulnerable to enemy magic."
    show sabiaemo happy1 at left
    s "Thank you, Dajrab."
    show dajrab normalclosed at right
    d "There is no need. I trust that you will use them well."
    "That could have been the end of it, but Sabia found herself pausing and considering. It had been a straightforward assignment, just as he'd promised, but she found herself with other questions."
    show sabiaemo irritated2 at left
    s "Why go to Vegardan lands?"
    "Dajrab did not answer for a time, examining her with his open eye, then he nodded slowly."
    show dajrab normalopen at right
    d "It is a matter of avoiding the struggle between Captains. Whether Tekrok or Rokgrid becomes Warchief, they will make changes that could erase many efforts. I try to focus on ways to strengthen our tribe that will not conflict with either of them."
    show sabiaemo normal at left
    s "That's smart, I guess. And you're happy just doing that?"
    show dajrab normalclosed at right
    d "It is Dajrab's role."
    show sabiaemo closed2 at left
    s "I see."
    show dajrab normalopen at right
    d "What of you, Sabia? What greater purpose do your actions serve? And I do not mean something as simple as revenge."
    show sabiaemo normal at left
    "Sabia wondered exactly how much he knew, but doubted it would do any good to press him on the issue. Instead she considered his question carefully."
    menu:
        "To take back what's rightfully mine":
            $ dom += 2
            "Her answer earned her no response at all, at first. Eventually Dajrab closed his eyes thoughtfully."
        "I just want to serve people":
            $ sub += 2
            "Her answer earned her a raised eyebrow, at first. Eventually Dajrab closed his eyes thoughtfully."
        "I need an army to reshape the world":
            $ slavery += 2
            "Her answer earned her a bit of a wry smile, at first. Eventually Dajrab closed his eyes thoughtfully."
        "I need allies to reshape the world":
            $ freedom += 2
            "Her answer earned her a curious look, at first. Eventually Dajrab closed his eyes thoughtfully."
    show dajrab happy at right
    d "So you say. I hope you remember that you will need to use every tool at your disposal, no matter your goal."
    "After considering that a moment, Sabia nodded and left. She'd been right to pick Dajrab as her ally. Meanwhile, she was interested in seeing these new troops he had promised..."
    return

label nevemaplychat1:
    $ kiacooldown = False
    $ maplynevesex = True
    scene bg countryside
    show neve1 at left
    show neveemo happy1 at left
    show maply 3 at right
    show maplyemo eyebrows at right
    with dissolve
    $ A_neve += 1
    $ A_maply += 1
    maply "H-hello..."
    show neveemo happy2 at left
    n "Hello there, Maply. What brings you here?"
    show maplyblush at right
    maply "I was just w-wondering if you get lonely out here..."
    n "Nah, it's okay. Nice and quiet on the outskirts."
    hide maplyblush at right
    show maplyemo surprise2 at right
    maply "Oh!"
    show maplyemo normalopen at right
    maply "If it was me, I'd get lonely. That's why I stay in the orc camp, even though most of the orcs are stinky."
    show neveemo normal at left
    n "Yes, you catgirls do like to stick together."
    show maplyemo sad2 at right
    maply "It's not just that! Being cast out of a caravan is the worst possible thing you can do to someone! We'd probably die on our own!"
    show maplyemo sad1 at right
    show maplyblush at right
    maply "Well, I would, because I'm just a scout. I think you're probably fine. I just... wondered if you get lonely without any other Vegardan elves."
    show neveemo happy3 at left
    n "Heh, that's considerate of you. But personally, I find there are more similarities than differences, no matter someone's race."
    show maplyemo surprise2 at right
    hide maplyblush at right
    maply "Oh! I didn't mean to say that catgirls think outsiders are bad or anything! It's true that we more often connect with Arwan elves, but we like anyone who's willing to work with us!"
    show neveemo happy1 at left
    n "Relax, Maply. I'm not offended."
    show maplyemo normal at right
    maply "That's good. But, umm... do you not want to answer my questions? Did you get outcast from your home or something?"
    n "Nah, it's nothing like that. Stop fidgeting so nervously, Maply... come over here and sit down."
    show maply 3 at center
    show maplyemo happy at center
    with moveinleft
    maply "Okay!"
    show maplyblush at center
    maply "You seem really nice, Neve, but you kinda scare me, eheheh..."
    show neveemo happy2 at left
    n "I'm not so scary. To answer your question, I wasn't outcast or anything, I just... needed to go in a different direction. You know how most of the sea lords travel the oceans, right?"
    hide maplyblush at center
    maply "Yeah! I haven't seen the ocean, but I've heard about how big it is! I want to see it one day!"
    show maplyemo sad2 at center
    maply "I don't know if I'd like to go on a boat, though. I don't like getting all wet. Except, umm, for baths. Baths are different."
    show neveemo happy1 at left
    n "Not all Vegardans spend their time on the oceans, there are plenty who run the ports, grow food, and run other industries. It's just that the sea lords are the real powers."
    show maplyemo sad1 at center
    maply "Don't they have to be on the ocean for a really long time, though? I think that would be hard, unless you had really good friends on the same boat..."
    n "That part isn't so bad - not so different from a caravan, I think, though you don't have very much space."
    show maplyemo happy at center
    maply "So you've been on a boat before? Was it a big one?"
    show neveemo closed2 at left
    n "Oh, yes. Half of my childhood was on one, climbing all over the rigging with my friends..."
    show maplyblush at center
    maply "Wow... and you've also traveled all over the place, right? You've done so many things..."
    show neveemo happy2 at left
    n "Well, I've had a lot of years to explore. You're still young, I'm sure you'll see the ocean and a lot of other places eventually."
    show maplyemo normal at center
    maply "Mmm... but, umm... Neve..."
    show maplyemo normalopen at center
    maply "Maybe I haven't seen a lot of women, but I think you're really beautiful! I like you a lot more than any of the girls in my caravan!"
    show neveemo happy3 at left
    n "Well, well, so it comes out..."
    show maplyemo sad2 at center
    maply "Umm... I know you go with orcs sometimes... so maybe you don't like girls? Or maybe you do, but I'm..."
    show neveemo happy2 at left
    n "You're cute, Maply. I wouldn't be talking to you if I didn't like you."
    show maplyemo happy at center
    maply "Oh, really? That's amazing!"
    show maplyemo sad1 at center
    maply "The truth is... when I asked if you were lonely, I was kind of talking about myself... I have some friends here, but I haven't been close to anyone since we came to camp... everything is so strange here..."
    show maplyemo happy at center
    maply "But you seem so confident and cool, Neve! Being around you, I feel more like myself again!"
    show neveemo eyeroll2 at left
    n "So... are you looking to spend time chatting with me, or are you asking for something more?"
    show maplyemo eyebrows at center
    maply "M-more..."
    show maplyemo happy at center
    maply "Can I, umm, try to do something nice for you? I'm not very good, but..."
    show neveemo happy2 at left
    n "Heh, come this way..."
    call nevemaplyA
    play music orccamp fadeout 2.0 fadein 2.0
    show maplyemo normal at center
    maply "Wow! I... I can't believe I was able to..."
    n "That was pretty damn good, Maply. Maybe we can do this again sometime!"
    show maplyemo happy at center
    maply "Yeah! Definitely!"
    show maplyemo eyebrows at center
    maply "Umm... is it okay if I sleep here, though? It'd be so much more comfortable..."
    show neveemo happy3 at left
    n "Come over here, you..."
    return

label raidquest1:
    $ raidquest = 1
    call sabiabase
    "The orcs Sabia had recruited were utterly unacceptable as a raiding party. But where Sabia once might have considered that to be true simply because they were orcs, now she could see that they had more potential than she had given them credit for."
    "The problem wasn't the raw materials, but the lack of cohesion. They were essentially just a group of warriors who were on the same side, not a fighting unit. To become a force she could actually use, they needed discipline."
    "That meant they needed to train together. Though the training grounds were usually run casually, Sabia discovered that it did have some organization. She figured out a good time, wrangled all her raiders to be there, and prepared for a good training session."
    "Only to find the training ground overrun with other orcs and all the training weapons taken."
    "Chalking it up to orc incompetence, Sabia rescheduled. But when that time ended up not working either, she realized that someone was blocking her. While her men actually wanted to train, they weren't going to put up with this, and neither was Sabia. She set out to find the orc in charge of the training yard schedule."
    show orcbase at right
    show orcloincloth at right
    show orcnecklace at right
    show orcemo normal at right
    with dissolve
    if sub >= 10:
        show sabiaemo sad1 at left
        s "Excuse me... I'm sorry to bother you, but my troops have been signed up to train, and they've always been interrupted."
        show orcemo sad2 at right
        orc "Sorry, Sabia. Me not know why happening, must be accident."
    elif sub >= dom:
        show sabiaemo closed2 at left
        s "Are you intentionally sabotaging my troops' training by scheduling other people?"
        show orcemo sad2 at right
        orc "Me not sabotaging anyone. Just chance, wrong training at same time."
    else:
        show sabiaemo angry1 at left
        s "Just what the hell is this?"
        show orcemo normalopen at right
        orc "What do you mean?"
        show sabiaemo angry2 at left
        s "Don't give me that shit. Why the fuck are you sabotaging my troops in the training?"
        show orcemo angry at right
        orc "Me not sabotaging anyone. Just chance, wrong training at same time."
    show sabiaemo normal at left
    s "Twice in a row? That's unlikely."
    show orcemo normalopen at right
    orc "Me not the one doing it. But... maybe someone else."
    show sabiaemo irritated2 at left
    s "Who would it be?"
    show orcemo suspicious at right
    orc "Galbag in charge of special trainings. Some warriors trade favors... sometimes make mistakes."
    s "Hmm. Where can I find this Galbag?"
    show orcemo normal at right
    orc "Always in Silvertusk Bar. Trades many favors."
    if sub >= dom:
        show sabiaemo happy1 at left
        s "I'll go speak to him, then. Thank you for your help."
    else:
        show sabiaemo closed2 at left
        s "You'd better hope he has answers for me."
    return

label raidquest2:
    $ kiacooldown = False
    $ raidquest = 2
    call sabiabase
    "As many times as Sabia had entered the Silvertusk Bar, she thought that she'd fully grasped everything about it. Orcs got drunk there, how hard could it be?"
    "But now, thinking about what she'd been told on the training grounds, she found herself looking in a different way. Lots of orcs were there to get drunk, yes, but not all. Some were there to meet friends, some to kill time, and some seemed like they had clear business in mind."
    "Even looking carefully, she might not have found this \"Galbag\" without the more specific instructions. He wasn't in a dark corner, as she expected, but instead in a well-lit section by one wall. He used his mug more like a prop than a drink, though, and she saw him occasionally talk to another orc and exchange money."
    "Definitely her target, and the one getting in the way of having her orcs be properly trained. Sabia put on a neutral smile and went to sit beside him."
    show orcbase2 at right
    show orcloincloth2 at right
    show orcemo2 normal at right
    with dissolve
    s "So... I hear you're the one to ask for favors."
    show orcemo2 smile1 at right
    orc "Maybe me am, maybe not. What do you need?"
    if sub >= dom:
        show sabiaemo sad1 at left
        s "Well... I want to help my men train, but things just haven't been going well in the training grounds..."
        show orcemo2 normal at right
        "He gave her a curious look, obviously understanding what she intended but surprised by the soft approach."
    else:
        show sabiaemo irritated1 at left
        s "Say I wanted to sabotage my training sessions."
        show orcemo2 suspicious at right
        "He immediately gave her a suspicious look and Sabia stared at him unblinkingly. He obviously understood what she intended."
    show orcemo2 normalopen at right
    orc "Galbag just trades favors. Helps make the camp work, ya know?"
    show sabiaemo normal at left
    s "Yes... and I'm interested in making sure that things work for me."
    show orcemo2 smile1 at right
    "The orc chuckled and took a long drink, watching her. Eventually he set his mug down and sat back with a satisfied sigh."
    orc "Pretty woman like you, Galbag wants to help... but people keep asking for favors, ya know? Me gotta help out."
    if dom >= 15:
        "So he was definitely the one responsible... or at least a step closer to the one responsible. Sabia kept her face neutral and considered her options."
        menu:
            "Get more information":
                "Deciding that she needed to find the person at the root of the problem, Sabia chose to let things go further. She put on a relaxed look and settled back into her seat."
            "Dom: Make an example of him":
                $ dom += 2
                $ raidquest = 5
                show sabiaemo happy1 at left
                show orcemo2 sad1 at right
                "Sabia smiled sweetly, her hand sliding around the orc's shoulder. He leaned in to touch her..."
                "And she used his own momentum against him, smashing his head through the table. The cheap wood broke, leaving him sprawling in the broken pieces, which drew enough attention."
                show sabiaemo angry1 at left
                s "Listen here, you piece of shit. Stop interfering with my training and I'll do you the favor of not beating you to death."
                "She'd planned to step on his throat and apply more threats, but it looked like that wasn't necessary. The orc pulled back, shaking his head frantically, and the others in the bar were laughing approvingly. It was obvious what would happen if they kept trying to mess with her."
                "After glowering at him a while longer, Sabia stalked out. She was certain the next time she tried to schedule training, she wouldn't have any problems."
                return
    else:
        "So she'd found the one arranging the interruptions... but not the one actually responsible. Realizing that she would need to get more information, Sabia made herself smile a little more."
    show sabiaemo normal at left
    s "I understand, you have to do your job. So... just who is this, asking for favors to interfere with me?"
    show orcemo2 smile3 at right
    orc "Now, now, me can't reveal such things..."
    show sabiaemo happy3 at left
    s "Come on... it would be a favor to me, after all..."
    show orcemo2 smile2 at right
    orc "Not professional. Course... Galbag's professionalism can get sloppy when he's drunk and happy, ya know?"
    show sabiaemo normal at left
    "Resisting the urge to roll her eyes, Sabia ordered a drink for him. He didn't seem actually interested in getting drunk, it was more an excuse to keep her there and chat, infuriatingly friendly with her."
    show sabiaemo2 blush at left
    "In fact, given the way he wrapped an arm around her shoulders and leaned closer as they drank, she wondered if that wasn't his real goal. Well, it meant that he was open to manipulation instead of firmly against her."
    "After she endured enough of it, the orc laid a grimy hand on her knee and leaned closer."
    show orcemo2 smile1 at right
    orc "Alright, Galbag will see if we can't exchange favors... you want to meet my contact, just listen..."
    "He leaned even closer, obviously leering at her breasts for a while, and then whispered a time and place in her ear. So to finish this, she needed to meet him in the main group of tents within the upper camp."
    "Sabia considered just stalking out, but decided to thank him. She left the bar considering her next move."
    return

label raidquest3:
    $ kiacooldown = False
    call sabiabase
    if dom >= 10:
        "It was the time she'd been given by Galbag, so Sabia considered her options. The location he'd given her was in the middle of the main orc tents in sight of plenty of orcs, so she wasn't worried about an ambush. That didn't mean she had to go alone, however..."
        menu:
            "Bring troops":
                "Sabia brought along a group of raiders... only to see Galbag disappear ahead of her with a scowl. Apparently the meeting was supposed to be between only the three of them."
                "Sighing, Sabia ordered her troops to fall back. She'd have to return without them later... or at least pretend to."
                return
            "Have troops follow at a distance":
                $ raidquesttroops = True
                "Sabia ordered her troops to mix with the others and keep their distance, but be ready for her signal, then she headed in."
            "Don't bring troops":
                "Deciding that she couldn't risk scaring off the contact, Sabia headed in on her own."
    else:
        "At the time she'd been given by Galbag, Sabia headed out of the camp. The location he'd given her was in the middle of the main orc tents in sight of plenty of orcs, so she wasn't worried about an ambush."
    "She reached a semi-secluded tent near nowhere in particular - a good place to meet for secret meetings that wouldn't look too suspicious."
    show orcbase2 at right
    show orcloincloth2 at right
    show orcemo2 suspicious at right
    show orcbase at center
    show orcloincloth at center
    show orcnecklace at center
    show orcemo suspicious at center
    with dissolve
    "She found Galbag there, along with a new orc who looked nervous. They were looking around, but hadn't seen her yet."
    if sub >= 10:
        "Sabia approached more noisily than she needed to, letting them know she was coming. When they noticed her, she put a bit of sway into her hips and smiled as she approached."
    elif sub >= dom:
        "Not wanting to scare them off, Sabia approached more noisily than she needed to, letting them know she was coming."
    else:
        "Sabia advanced swiftly and silently before intentionally breaking a branch and marching up to them. It must have seemed like she came out of nowhere, because both of them jumped slightly."
    show orcemo2 normalopen at right
    orc "This is contact you wanted."
    show orcemo2 normal at right
    s "So you're the one... if you have so much against me, why meet me here?"
    show orcemo sad1 at center
    "The new orc swallowed uncomfortably, not meeting her gaze for a while. His gaze wandered over her body instead, which wasn't great, but there was real discomfort there."
    orc "It's not me... someone else doesn't want you to go raiding. They hired me to make it happen, so me asked Galbag to organize training to interrupt yours."
    show sabiaemo irritated2 at left
    s "And they couldn't just hire Galbag?"
    show orcemo angry at center
    orc "These are sensitive matters. It's not that simple."
    "Though he looked rough, Sabia realized that this orc was the equivalent of a special agent. This was no petty vendetta... someone was using him to get at her directly."
    show sabiaemo closed2 at left
    s "Just how high does this go? Is this that damn Ornshakar again?"
    show orcemo2 smile1 at right
    show orcemo normal at center
    "The new orc gave her no indication, but Galbag made a little scoffing sound that suggested not. She did have some leverage here, so Sabia used it to keep pressing."
    s "After talking to Warchief Groknak, I don't think it's him... plus, he could just order me to stop if he wanted that..."
    show sabiaemo normal at left
    "Talking casually about the Warchief made them a little uncomfortable, but they didn't give any indication. Sabia thought she was getting close now, so smiled and kept going."
    s "So there aren't that many options, are there? It's not like your hierarchy is that complicated. Just tell me who asked you to interfere with me."
    orc "It's not that easy..."
    show sabiaemo happy2 at left
    s "Which Captain is it?"
    show orcemo2 normal at right
    "Her sharp question made the orc flinch. His eyes dropped to the ground, but Sabia refused to look away. She let the silence stretch uncomfortably."
    $ raidoppositionknown = True
    show orcemo normalopen at center
    if orcalliance == "tekrok":
        orc "Fine. It was Rokgrid."
        s "Trying to take out one of Tekrok's allies, then? I suppose I shouldn't be surprised."
    elif orcalliance == "dajrab":
        orc "Fine. It was Rokgrid."
        s "Really? I wonder if he's angry I didn't work with him, or if he has something against Dajrab..."
        "The orc shrugged uncertainly. Obviously he just followed orders and did the dirty work."
    elif orcalliance == "rokgrid":
        orc "Fine. It was Tekrok."
        s "So he either hates me or he hates Rokgrid. Or both. Not at all surprised."
    else:
        orc "Fine. It was Tekrok."
        s "Because I've gotten this far on my own? Not at all surprised."
    show orcemo sad1 at center
    orc "Me can't just ignore an order from a Captain..."
    show sabiaemo normal at left
    s "You don't need to ignore it. You just need to let me train successfully - say I outwitted you somehow."
    orc "But... me get problems..."
    show orcemo2 smile2 at right
    orc "Galbag agrees. This is our work. If we're going to help you, we need something in return..."
    s "Hmm..."
    if raidquesttroops == True:
        menu:
            "Sub: Use body to persuade them" if sub >= 20:
                $ raidquest = 3
                $ sub += 2
                $ L_orcs -= 5
                show sabiaemo happy1 at left
                "Giving them a coy smile, Sabia shifted her position, thrusting her chest forward a little more and putting a hand on her hip."
                s "I'm not hearing any reasons you {i}can't{/i} work with me on this, just reasons it would be inconvenient... anything I can do to make your life a little easier?"
                show orcemo smile1 at center
                "The contact swallowed and then gave a grin, but before he could speak, Galbag broke in."
                show orcemo2 smile2 at right
                orc "This is inconvenient for me, too. Lots of changing plans, bad for business."
                show orcemo smile3 at center
                orc "That's right. And disappointed Captains can cause real problems..."
                show sabiaemo closed3 at left
                s "Come on, boys. We know how this is going to go, we can come to an agreement."
                orc "And you need us both to keep quiet. This isn't something you can pay for with just one little blowjob or something..."
                show sabiaemo closed2 at left
                s "I can't afford to constantly keep paying - and it isn't worth that. One payment, then we have a deal."
                "The two orcs whispered fiercely to one another for a time, apparently united by the prospect of fucking her. Eventually they turned back and Galbag spoke."
                orc "One night with each of us, and we can do whatever we want."
                show sabiaemo irritated2 at left
                s "Hmm... one night with both of you at the same time."
                orc "Deal."
                show sabiaemo happy1 at left
                s "In that case... meet me in my tent when I give you the signal."
                "Sabia left, considering the deal that she'd made. Her position wasn't weak, so she thought the deal would hold, then she could finally get her troops properly trained. But first, she needed to get through that night..."
            "Make a compromise":
                $ raidquest = 5
                $ dom += 1
                $ sub += 1
                show sabiaemo eyebrow1 at left
                s "The Captain can't keep track of every warrior, can he? And it's not like he can stop them from training individually - that would be impossible."
                orc "What's your point?"
                show sabiaemo closed4 at left
                s "What he wants is to stop me, but all he can really track is whether my training sessions get blocked. That's your job, nothing more."
                show sabiaemo normal at left
                s "Galbag, you're hiring random warriors to fill up the training grounds, right?"
                orc "That's right. Or bums - they're cheaper."
                show sabiaemo happy1 at left
                s "What if you \"hired\" {i}my{/i} warriors to block my training sessions? I could pretend to get angry about it and we all get what we want."
                "The orcs blinked at that, not having expected that option. One opened his mouth to object, but Sabia cut him off."
                show sabiaemo normal at left
                s "It has to cost money to hire those bums, right? My warriors wouldn't cost you anything."
                "Galbag nodded reluctantly. The other orc seemed more hesitant, but it was obvious the tide was turning against him and he hadn't denied her logic yet."
                s "Things might be difficult for you if you went against a Captain... but I guarantee they'll be difficult if you go against me. Go on, take the easy option."
                "In the end, they both agreed. As Sabia headed back to camp, she was quite certain that her problems using the training grounds were over."
            "Use hidden troops to persuade them":
                $ raidquest = 5
                $ dom += 1
                show sabiaemo happy2 at left
                s "No... no, I don't think so."
                "Sabia gave a sharp whistle, the signal for her men to stop milling around quietly and approach, an ominous wall of strength."
                orc "Wait a minute... we're near camp, you can't..."
                show sabiaemo eyebrow1 at left
                s "Do what? My troops are just relaxing nearby... sorry, does that make it difficult for you to work? Well, they'll have a lot of free time on their hands, since they can't train..."
                orc "..."
                show sabiaemo closed3 at left
                s "And you, Galbag... I imagine you need some privacy to conduct business in the bar, right? It'd be a shame if there were a bunch of idle orcs around..."
                orc "Dammit, fine! We do what you say."
                show sabiaemo happy1 at left
                "Sabia made a gesture for her orcs to stand down, though they stayed close."
                s "You don't need to humiliate yourselves - you can even stop me sometimes, when we arrange it. But if you don't let me train, I will make your lives a living hell."
                "The two orcs had obviously intended to manipulate her here, but now found themselves surrounded by a much larger group. They hastily agreed, but Sabia didn't let them go for a while, making sure they were deeply uncomfortable and aware of how much she could make their lives difficult."
                "By the time they all returned to camp, Sabia was quite certain that her problems using the training grounds were over."
    else:
        menu:
            "Sub: Use body to persuade them" if sub >= 20:
                $ raidquest = 3
                $ sub += 2
                $ L_orcs -= 5
                show sabiaemo happy1 at left
                "Giving them a coy smile, Sabia shifted her position, thrusting her chest forward a little more and putting a hand on her hip."
                s "I'm not hearing any reasons you {i}can't{/i} work with me on this, just reasons it would be inconvenient... anything I can do to make your life a little easier?"
                show orcemo smile1 at center
                "The contact swallowed and then gave a grin, but before he could speak, Galbag broke in."
                show orcemo2 smile2 at right
                orc "This is inconvenient for me, too. Lots of changing plans, bad for business."
                show orcemo smile3 at center
                orc "That's right. And disappointed Captains can cause real problems..."
                show sabiaemo closed3 at left
                s "Come on, boys. We know how this is going to go, we can come to an agreement."
                orc "And you need us both to keep quiet. This isn't something you can pay for with just one little blowjob or something..."
                show sabiaemo closed2 at left
                s "I can't afford to constantly keep paying - and it isn't worth that. One payment, then we have a deal."
                "The two orcs whispered fiercely to one another for a time, apparently united by the prospect of fucking her. Eventually they turned back and Galbag spoke."
                orc "One night with each of us, and we can do whatever we want."
                show sabiaemo irritated2 at left
                s "Hmm... one night with both of you at the same time."
                orc "Deal."
                show sabiaemo happy1 at left
                s "In that case... meet me in my tent when I give you the signal."
                "Sabia left, considering the deal that she'd made. Her position wasn't weak, so she thought the deal would hold, then she could finally get her troops properly trained. But first, she needed to get through that night..."
            "Make a compromise":
                $ raidquest = 5
                $ dom += 1
                $ sub += 1
                show sabiaemo eyebrow1 at left
                s "The Captain can't keep track of every warrior, can he? And it's not like he can stop them from training individually - that would be impossible."
                orc "What's your point?"
                show sabiaemo closed4 at left
                s "What he wants is to stop me, but all he can really track is whether my training sessions get blocked. That's your job, nothing more."
                show sabiaemo normal at left
                s "Galbag, you're hiring random warriors to fill up the training grounds, right?"
                orc "That's right. Or bums - they're cheaper."
                show sabiaemo happy1 at left
                s "What if you \"hired\" {i}my{/i} warriors to block my training sessions? I could pretend to get angry about it and we all get what we want."
                "The orcs blinked at that, not having expected that option. One opened his mouth to object, but Sabia cut him off."
                show sabiaemo normal at left
                s "It has to cost money to hire those bums, right? My warriors wouldn't cost you anything."
                "Galbag nodded reluctantly. The other orc seemed more hesitant, but it was obvious the tide was turning against him and he hadn't denied her logic yet."
                s "Things might be difficult for you if you went against a Captain... but I guarantee they'll be difficult if you go against me. Go on, take the easy option."
                "In the end, they both agreed. As Sabia headed back to camp, she was quite certain that her problems using the training grounds were over."
    return

label raidquest4:
    $ kiacooldown = False
    $ raidquest = 5
    $ sub += 3
    $ L_orcs -= 5
    call sabiabase
    "Sabia sent coded messages to both orcs - not that it was much of a code, since they knew exactly what they'd be getting. She chose a late hour when there wouldn't be too many orcs about - both to avoid too many knowing that she was bringing orcs to her tent, and to cut down on how long their night lasted."
    "Galbag and his contact showed up, their erections obvious in their pants. Sabia rolled her eyes and decided to get it over with."
    call raidquestbribery
    "In the morning, Sabia wiped off some of the slime and fixed her gaze on Galbag."
    s "We have a deal, then?"
    orc "We have a deal, slut."
    "The two of them sauntered out of the tent, leaving Sabia to clean herself off. At least she could finally get back to work."
    return

label raidquest5:
    $ raidquest = 6
    $ Sabiasquad.combat += 1
    $ Sabiasquad.defense += 1
    $ Sabiasquad.raid += 1
    $ Sabiasquad.diplomacy += 1
    $ Sabiasquad.siege += 1
    call sabiabase
    "Her problem finally dealt with, Sabia was able to train her raiders as a unified group. She'd expected them to refuse drills and other discipline, but they took to it rather quickly."
    "Perhaps more importantly, it unified them as a group, and increased their loyalty to her. Sabia found herself surprised at how well they performed. Of course, she'd been selective in choosing some of the better orcs."
    "They might have a long way to go, but she felt that her forces had finally become a unit worthy of the name."
    return

label tutorialraid:
    scene bg countryside with dissolve
    $ renpy.block_rollback()
    $ kiacooldown = False
    $ tutorialraiddone = True
    $ tutorialraidscore = 0
    "Now that she was finally prepared, Sabia led her group of warriors out to take down the group of rogue orcs. She wanted the task done as quickly as possible so she could choose where to raid herself, but also needed to do it right."
    "The rogue orcs were fairly predictable, hiding out in a grove between orc and human lands. Fortunately, her own orcs had no qualms about killing them - they seemed to view the rogue orcs as worthless trash... not so different from how most humans viewed orcs. In any case, she wouldn't have any problems with their loyalty."
    "Her only problem would be how best to attack the group. They had built a primitive fort that would be a pain to take down with her current forces, so she needed some kind of edge. Then, once they had the enemy out from hiding, she needed a main force to crush them."
    "Given the resources available to her, Sabia considered her options..."
    $ reset_armies()
    menu:
        "Draw them out with a raiding party":
            $ deployarmies(["Raiders",1],["Main Force",3])
            call deployment
            "Though she wanted to fight, Sabia needed to hold back so that she would have plausible deniability if things went wrong. So all she could do was wait at a distance and watch, hoping her plan went successfully..."
            if Raiders.get_deployed() == 0:
                $ tutorialraidscore -= 2
                "Without a raiding group, the first stage went horribly. The rogue orcs didn't begin to emerge until they were fully prepared and heavily armed."
            else:
                if Raiders.get_raid() >= 4:
                    $ tutorialraidscore += 1
                    "The raiders hit hard and fast, taking down several scouts and setting fire to one of the rogue orcs' shacks before pulling back. Enraged, the group rushed out after them, directly into the path of her main force."
                else:
                    "The raiders hit the rogue orc camp, but they weren't fast enough. The sentries spotted them and mounted a counterattack."
                    "Sabia winced as she saw many of her troops fall or take injuries, but as disastrous as the raiding attempt was, it did draw out the enemy."
                    $ Raiders.injury_random(1,2)
            if MainForce.get_deployed() == 0:
                $ tutorialraidscore -= 2
                "Getting the orcs out in the open did little good without a strong force to hit them, however. Sabia had to order a much-delayed attack that went poorly."
            else:
                if MainForce.get_combat() >= 10:
                    $ tutorialraidscore += 2
                    "Once they were out of their fortifications, Sabia's forces fell on them. It was a brutally short battle, every single one of the rogue orcs was killed with few losses on her side."
                elif MainForce.get_combat() >= 6:
                    $ tutorialraidscore += 1
                    "Once they were out of their fortifications, Sabia's forces hit them on the flank. Though the rogue orcs tried to put up a fight, they were soon overwhelmed."
                elif MainForce.get_combat() >= 3:
                    "Once they were out of their fortifications, Sabia's forces hit them on the flank. The rogue orcs put up far more of a fight than Sabia expected, and she was nervous as she watched her orcs struggle, but in the end they prevailed."
                else:
                    $ tutorialraidscore -= 1
                    "Her forces tried to hit the rogue orcs when they left their fortifications, but despite having the element of surprise, they did poorly. They were victorious in the end, but their losses were embarrassingly high given the weakness of their foe."
                    $ MainForce.injury_random(1,2)
        "Destroy their walls":
            $ deployarmies(["Siegers",1],["Main Force",3])
            call deployment
            "Though she wanted to fight, Sabia needed to hold back so that she would have plausible deniability if things went wrong. So all she could do was wait at a distance and watch, hoping her plan went successfully..."
            if Siegers.get_deployed() == 0:
                $ tutorialraidscore -= 2
                "Without a force to carry out the siege, the first stage went horribly. The rogue orcs didn't begin to emerge until they were fully prepared and heavily armed."
            else:
                if Siegers.get_siege() >= 4:
                    $ tutorialraidscore += 1
                    "Though the orcs didn't have much in the way of siege equipment, they did a surprisingly good job of rigging together battering rams and ladders from what they had on hand. Their attack didn't demolish the fortification, but it did destroy the gate and throw the defenders into confusion."
                else:
                    "Without proper siege equipment and with little training, Sabia's attempt at a siege was pathetic. The only sense in which it succeeded was that the rogue orcs emerged from their fortifications to attack the siegers, and Sabia saw many fall while her main force advanced to assist them."
                    $ Siegers.injury_random(1,2)
            if MainForce.get_deployed() == 0:
                $ tutorialraidscore -= 2
                "Getting the orcs out in the open did little good without a strong force to hit them, however. Sabia had to order a much-delayed attack that went poorly."
            else:
                if MainForce.get_combat() >= 10:
                    $ tutorialraidscore += 2
                    "Once they were out of their fortifications, Sabia's forces fell on them. It was a brutally short battle, every single one of the rogue orcs was killed with few losses on her side."
                elif MainForce.get_combat() >= 6:
                    $ tutorialraidscore += 1
                    "Once they were out of their fortifications, Sabia's forces hit them on the flank. Though the rogue orcs tried to put up a fight, they were soon overwhelmed."
                elif MainForce.get_combat() >= 3:
                    "Once they were out of their fortifications, Sabia's forces hit them on the flank. The rogue orcs put up far more of a fight than Sabia expected, and she was nervous as she watched her orcs struggle, but in the end they prevailed."
                else:
                    $ tutorialraidscore -= 1
                    "Her forces tried to hit the rogue orcs when they left their fortifications, but despite having the element of surprise, they did poorly. They were victorious in the end, but their losses were embarrassingly high given the weakness of their foe."
                    $ MainForce.injury_random(1,2)
        "Send a group to pretend to trade":
            $ deployarmies(["Diplomats",1],["Main Force",3])
            call deployment
            "Though she wanted to fight, Sabia needed to hold back so that she would have plausible deniability if things went wrong. So all she could do was wait at a distance and watch, hoping her plan went successfully..."
            if Diplomats.get_deployed() == 0:
                $ tutorialraidscore -= 2
                "Without a force to attempt the diplomacy ruse, the first stage went horribly. The rogue orcs didn't begin to emerge until they were fully prepared and heavily armed."
            else:
                if Diplomats.get_diplomacy() >= 4:
                    $ tutorialraidscore += 1
                    "Though Sabia had been uncertain about diplomacy working, her group was able to make the rogue orcs drop their guard. Soon they were emerging from their fortifications to talk trade, giving her plenty of time to strike."
                else:
                    "The group Sabia sent to try to trick the rogue orcs almost got inside, but they did something to alert them. Sabia couldn't see what it was from a distance, but the rogue orcs attacked them, cutting down many while the main force advanced to assist them."
                    $ Diplomats.injury_random(1,2)
            if MainForce.get_deployed() == 0:
                $ tutorialraidscore -= 2
                "Getting the orcs out in the open did little good without a strong force to hit them, however. Sabia had to order a much-delayed attack that went poorly."
            else:
                if MainForce.get_combat() >= 10:
                    $ tutorialraidscore += 2
                    "Once they were out of their fortifications, Sabia's forces fell on them. It was a brutally short battle, every single one of the rogue orcs was killed with few losses on her side."
                elif MainForce.get_combat() >= 6:
                    $ tutorialraidscore += 1
                    "Once they were out of their fortifications, Sabia's forces hit them on the flank. Though the rogue orcs tried to put up a fight, they were soon overwhelmed."
                elif MainForce.get_combat() >= 3:
                    "Once they were out of their fortifications, Sabia's forces hit them on the flank. The rogue orcs put up far more of a fight than Sabia expected, and she was nervous as she watched her orcs struggle, but in the end they prevailed."
                else:
                    $ tutorialraidscore -= 1
                    "Her forces tried to hit the rogue orcs when they left their fortifications, but despite having the element of surprise, they did poorly. They were victorious in the end, but their losses were embarrassingly high given the weakness of their foe."
                    $ MainForce.injury_random(1,2)
    "The most important thing was killing every single rogue orc, and that at least was accomplished. Sabia went to join them in order to make sure it was done properly herself."
    if tutorialraidscore >= 3:
        $ L_orcs += 2
        "Her forces were in a surprisingly good mood, the entire attack having gone perfectly. They were happy to obey her when it came to taking what they could and getting out quick."
    elif tutorialraidscore >= 2:
        $ L_orcs += 1
        "Her forces were in a fairly good mood, apparently agreeing that she had led them well. She'd expected problems getting them to leave in a disciplined manner instead of staying to loot, but they did a good job of taking what they could and following her."
    elif tutorialraidscore >= 1:
        $ L_orcs -= 5
        "Her forces were in a sour mood, irritated that they had done poorly despite their overwhelming numbers. Sabia resolved to do better next time."
    else:
        $ L_orcs -= 10
        "She was surprised to find her own forces glowering at her. The attack had been an unmitigated disaster, and it seemed they blamed her. Though she wished they had fought better, she had to admit she had led them to this point."
    "Though she'd hoped to retreat without even a glimpse of humans, Sabia did spot what might have been farmers on the horizon. They didn't seem likely to attack, especially since her orcs behaved themselves, but it made her damn nervous."
    "Just in case they called guards, Sabia decided to set up a rearguard while they returned to camp, hoping she had enough forces for it..."
    $ deployarmies(["Return Guard",1])
    call deployment
    if ReturnGuard.get_defense() >= 2:
        $ tutorialraidscore += 1
        "They got back to camp without incident, but Sabia felt safer knowing that she'd been able to field a good force."
    else:
        "They got back to camp without incident, but Sabia was anxious the entire time. If they had been attacked, it would not have gone well for her forces."
    "When they returned, her forces were happy to disperse to enjoy their share of the loot. It wasn't much, so Sabia had taken nothing for herself. Except for permission to raid, which was the true prize."
    call sabiabase
    with dissolve
    show groknak normal at right
    with moveinright
    "She had planned to find Groknak and demand his permission, but to her surprise he found her as she returned to camp."
    g "So. The rogue orcs are dead?"
    s "To the last man."
    g "Then you have fulfilled the terms of our agreement. Warchief Groknak grants you permission to raid freely in the future."
    if tutorialraidscore >= 4:
        $ A_groknak += 2
        g "Indeed, it is granted freely. Warchief Groknak has heard of how well you executed the raid."
    elif tutorialraidscore >= 2:
        $ A_groknak += 1
        g "Though you could have done better, Warchief Groknak respects how you executed the raid. There should be no problems with human settlements."
    else:
        $ A_groknak -= 1
        g "But this is only because a Warchief keeps his word. Your performance was very disappointing."
        s "I did what I could with the troops I had."
        g "Hmph. Do better in the future."
        "Sabia shrugged off his comments. All that mattered was that she had the troops and the freedom to use them."
        return
    s "I don't want any trouble, just like I told you earlier. You can count on me to do well in the future, too."
    if groknakbonus:
        if orcalliance == "tekrok":
            $ Tekrokorcs.combat += 1
            g "Indeed... and Warchief Groknak will assist. No equipment can be disbursed to you, but... the warriors of Tekrok who were assigned to you will be given proper helms from the Warchief's horde."
            s "Oh, really? Thank you!"
            g "The only thanks necessary is to do as you have promised and cause no trouble."
        elif orcalliance == "rokgrid":
            $ Rokgridorcs.combat += 1
            g "Indeed... and Warchief Groknak will assist. No equipment can be disbursed to you, but... the warriors of Rokgrid who were assigned to you will be given proper helms from the Warchief's horde."
            s "Oh, really? Thank you!"
            g "The only thanks necessary is to do as you have promised and cause no trouble."
        elif orcalliance == "dajrab":
            $ Dajraborcs.combat += 1
            g "Indeed... and Warchief Groknak will assist. No equipment can be disbursed to you, but... the warriors of Dajrab who were assigned to you will be given proper helms from the Warchief's horde."
            s "Oh, really? Thank you!"
            g "The only thanks necessary is to do as you have promised and cause no trouble."
        else:
            if kulganalive == True:
                $ Kulganorcs.combat += 1
                g "Indeed... and Warchief Groknak will assist. No equipment can be disbursed to you, but... the group under the warrior named Kulgan will be given proper helms from the Warchief's horde."
                s "Oh, really? Thank you!"
                g "The only thanks necessary is to do as you have promised and cause no trouble."
            else:
                g "Warchief Groknak would like to assist you... but it would not do to directly assist a human's forces. See to it that you continue to cooperate with our tribe in the future."
                s "I understand."
    else:
        g "See that you do."
    "With that, Groknak nodded for her to go. Sabia turned away with a smile on her face - less because she had succeeded, and more because she finally had the troops and the freedom to use them."
    jump eastern_frontier_map

label banditintroraid:
    "Sabia was surprised how brazenly the bandits made camp in the hills. They made so many fires, if they had been within Lundar, they would have been stamped out within a few days. But out here, it seemed they were a force to be reckoned with."
    "Furthermore, their camp was fortified and heavily defended. Not something to assault lightly..."
    menu:
        "Nothing for now":
            return
        "Eliminate them":
            $ banditintroraiddone = True
    if orcalliance == "tekrok":
        "Sabia spent several days trying to bring it up with Tekrok, but he seemed uninterested. Finally he sent a group of troops with her, though not under her command. It was better than nothing."
    elif orcalliance == "rokgrid":
        "Sabia spent several days trying to get additional support from Rokgrid, but he seemed to believe targeting human bandits was risky. Finally he sent a group of troops with her, though not under her command, and promised more support once she learned more about the group."
    elif orcalliance == "dajrab":
        "When Sabia tried to bring it up with Dajrab, he seemed even more closed than usual. He sent a group of troops with her, though not under her command, and said they would speak more later if she succeeded."
    else:
        "Sabia would have liked to get support from one of the Captains, but given the choices she'd made... she had no choice but to go things alone."
    scene bg countryside
    call sabiabase
    show orcbase2 at right
    show orcloincloth2 at right
    show orchelmet2 at right
    show orcpiercing2 at right
    show orcshoulder2 at right
    show orcstrap2 at right
    show orcwrap2 at right
    show orcbeard21 at right
    show orcemo2 normal at right
    with dissolve
    "Sabia met with her commander at a safe distance."
    s "How does it look?"
    show orcemo2 normalopen at right
    orc "There are two approaches, both at a disadvantage. Either up the main hill from the south, or between hills to the east."
    s "They have archers?"
    orc "In both positions."
    s "But they'll be more of a threat to the south. Hmm..."
    "If the bandits were allowed to amass their forces, they'd be too much of a threat. She needed to distract them on one front, cripple them from the other, then take out their defenses when the two met. Pretty risky."
    s "We'll feint from the southern hill approach, get their archers to mass there. The real attack will be from the east."
    orc "The southern group will be tricky. It needs to be fast enough to look like a real threat, but they'll take serious losses if they can't defend against the arrows."
    s "In a perfect world, I'd get better equipment, but there's no time. This will have to be the plan."
    orc "And if the bandits have more troops outside the base?"
    s "I was thinking we need reserves anyway."
    if orcalliance == "sabia":
        orc "We'll be stretched thin. Me hope this not mistake, Sabia..."
        s "So two groups... and maybe a third if things go bad..."
    else:
        orc "If we hold out, will get support from the Captain... me think this can work, Sabia."
        s "So two groups..."
    scene bg countryside
    with dissolve
    $ reset_armies()
    $ deployarmies(["Southern Hill Assault",2],["Eastern Valley Assault",2])
    call deployment
    $ temp1 = 0
    "Sabia assigned her forces as best she was able and gave the command to start the attack..."
    if SouthernHillAssault.get_deployed() == 0:
        $ temp1 -= 1
        "But with no troops in the south, she was afraid the attack was doomed to failure... Sabia assigned a few stragglers reluctantly."
    if EasternValleyAssault.get_deployed() == 0:
        $ temp1 -= 1
        "But with no troops in the east, she was afraid the attack was doomed to failure... Sabia assigned a few stragglers reluctantly."
    pause 1
    if SouthernHillAssault.get_defense() >= 5:
        "Sabia winced as the troops from the south charged into a hail of arrows. The bandits shifted with surprising speed, concentrating their archers on the attack."
        "But to her surprise, her troops managed to weather the assault fairly well, which seemed to unnerve the bandits."
        if SouthernHillAssault.get_raid() >= 5:
            $ temp1 += 1
            "Once they reached the bandit camp itself, they hit hard and fast. The bandit camp was thrown into complete chaos trying to cope with the swift strike."
        else:
            "Once they reached the bandit camp itself, they struggled to deal damage, but Sabia hoped that they had served as an effective distraction."
    else:
        "Sabia winced as the troops from the south charged into a hail of arrows. The bandits shifted with surprising speed, concentrating their archers on the attack."
        "She saw plenty of troops falling, and even if they won and healed the injured, she was going to feel the consequences."
        $ SouthernHillAssault.injury_random(1,3)
        if SouthernHillAssault.get_raid() >= 5:
            $ temp1 += 1
            "But once the survivors reached the camp, they hit hard and fast. The bandit camp was thrown into complete chaos trying to cope with the swift strike."
        else:
            "Some survivors did make it through, but they struggled to deal damage. Sabia had to hope that they had served as an effective distraction."
    "Meanwhile, the forces she'd assigned to the east had been moving as subtly as possible through the valley that led to the camp."
    if temp1 >= 1:
        "The bandits noticed them coming, but too late to mount full defenses. Her forces reached the edge of their camp before facing resistance and falling into a pitched melee."
        if EasternValleyAssault.get_combat() >= 4:
            $ temp1 += 1
            "It frustrated her to watch from a distance and just hope her strategy worked... but she could tell that her forces were crushing the bandits."
        else:
            "It frustrated her to watch from a distance and just hope her strategy worked... but her forces won in the end, even if they took losses in the process."
            $ EasternValleyAssault.injury_random(1,2)
    else:
        "As she'd feared, the bandits noticed their movement in time to set up decent defenses. The two forces clashed viciously in the valley."
        if EasternValleyAssault.get_combat() >= 6:
            $ temp1 += 1
            "It frustrated her to watch from a distance and just hope her strategy worked... but she could tell that her forces were crushing the bandits."
        else:
            "It frustrated her to watch from a distance and just hope her strategy worked... but her forces won in the end, even if they took losses in the process."
            $ EasternValleyAssault.injury_random(1,2)
    $ temp2 = 0
    $ temp2 += SouthernHillAssault.get_combat()
    $ temp2 += EasternValleyAssault.get_combat()
    "With the main bandit defense broken, both her forces combined together. Their position was superior, but the bandits didn't break and run as she'd hoped, turning it into an intense melee."
    call sabiabase
    with dissolve
    if temp2 >= 12:
        $ temp1 += 2
        "Disoriented by the two-pronged attack, the bandits swiftly succumbed to her forces. Sabia smiled as she approached to check out the aftermath."
    elif temp2 >= 8:
        $ temp1 += 1
        "Disoriented by the two-pronged attack, the bandits succumbed to her forces. Sabia smiled as she approached to check out the aftermath."
    elif temp2 >= 4:
        "Her troops had a difficult time quelling the bandit camp, given their superior strategy. Sabia frowned as she approached to check out the aftermath."
    else:
        $ temp1 -= 1
        "Despite her strategy, her troops had a difficult time quelling the bandit camp. Sabia scowled as she approached to check out the aftermath."
    "Yet as Sabia got closer, she heard war cries... and saw a new group of bandits surging across the plains toward her troops, which were still off-balance and positioned wrong from the battle."
    "A group returning at the proper time? Or had the bandits been so organized that they had backup ready? Either way, Sabia suddenly had a huge problem on her hands and little time to give commands."
    if orcalliance == "sabia":
        "There was no one coming to save her, though, so Sabia desperately tried to command reserves..."
        $ deployarmies(["Reserves",2])
        call deployment
        if Reserves.get_combat() >= 6:
            $ temp1 += 2
            "Having held strong troops in reserve, Sabia managed to intercept the bandit attack easily. They hit the charging bandits hard, preventing them from joining the main battle."
        elif Reserves.get_combat() >= 3:
            $ temp1 += 1
            "Having held troops in reserve, Sabia managed to intercept the bandit attack. They hit the charging bandits hard, preventing them from joining the main battle."
        elif Reserves.get_combat() >= 1:
            "They weren't the troops she would have picked, but Sabia still had forces in reserve. They managed to intercept the bandit attack, nullify their backup."
        else:
            "There was no one left, leaving her horribly overextended. Sabia judged that her forces might still win the day... but not before the bandits crashed into her position."
            "Sabia lifted her weapon to fight. She didn't even see the arrow that took her in the eye."
            show gameover with dissolve
            pause 3
            $ renpy.full_restart()
    else:
        $ temp1 += 1
        if orcalliance == "tekrok":
            "Fortunately, at that moment the forces Tekrok had sent to observe rushed into battle, intercepting the bandits before they could attack. Sabia breathed a sigh of relief."
        elif orcalliance == "rokgrid":
            "Fortunately, at that moment the forces Rokgrid had sent to observe rushed into battle, intercepting the bandits before they could attack. Sabia breathed a sigh of relief."
        elif orcalliance == "dajrab":
            "Fortunately, at that moment the forces Dajrab had sent to observe rushed into battle, intercepting the bandits before they could attack. Sabia breathed a sigh of relief."
    "With their surprise attack blunted, the bandits started to succumb to Sabia's numbers. Signs of resistance quickly faded."
    "Sabia waited tensely to see if even more troops would appear, but it seemed the battle was truly over now. She headed into the camp to learn more."
    "Unfortunately, all the bandits were either dead or dying and it was hard to extract information from them. None seemed to know anything, though she would have liked to properly torture them. Getting her orcs to attack less brutally would be important in the future."
    "Her forces seemed happy with their loot, but Sabia was surprised just how little the bandits had to plunder. How could such an effective group be so unsuccessful?"
    if temp1 >= 5:
        $ kiabones += 2
        $ Inventory.add_item(Makhorbones,2)
        $ money += 150
        "There wasn't much to go around, but Sabia's troops brought her 150 Lundils as her share."
        "But the far larger prize was found in a pit where the bandits had dumped the bodies of orcs: two of those orcs had been carrying Makhor bones."
        "The orcs gave them to Sabia as a trophy of her victory, and she kept them for her own purposes."
    elif temp1 >= 4:
        $ kiabones += 2
        $ Inventory.add_item(Makhorbones,2)
        $ money += 100
        "There wasn't much to go around, but Sabia's troops brought her 100 Lundils as her share."
        "But the far larger prize was found in a pit where the bandits had dumped the bodies of orcs: two of those orcs had been carrying Makhor bones."
        "The orcs gave them to Sabia as a trophy of her victory, and she kept them for her own purposes."
    elif temp1 >= 3:
        $ kiabones += 1
        $ Inventory.add_item(Makhorbones,1)
        $ money += 75
        "There wasn't much to go around, but Sabia's troops brought her 75 Lundils as her share."
        "But the far larger prize was found in a pit where the bandits had dumped the bodies of orcs: one of those orcs had been carrying a Makhor bone."
        "The orcs gave it to Sabia as a trophy of her victory, and she kept it for her own purposes."
    elif temp1 >= 2:
        $ kiabones += 1
        $ Inventory.add_item(Makhorbones,1)
        $ money += 50
        "There wasn't much to go around, but Sabia's troops brought her 50 Lundils as her share."
        "But the far larger prize was found in a pit where the bandits had dumped the bodies of orcs: one of those orcs had been carrying a Makhor bone."
        "The orcs gave it to Sabia as a trophy of her victory, and she kept it for her own purposes."
    else:
        "There was little enough to go around that Sabia let her troops have it all, just pondering the larger concern."
    show orcbase2 at right
    show orcloincloth2 at right
    show orchelmet2 at right
    show orcpiercing2 at right
    show orcshoulder2 at right
    show orcstrap2 at right
    show orcwrap2 at right
    show orcbeard21 at right
    show orcemo2 normal at right
    with moveinright
    orc "Not bad, Sabia. These bandits were strong."
    s "Too strong, do you think? Do humans usually fight this hard? I expected them to just run for their lives."
    orc "Not sure. They were... very well-equipped. Especially given their good equipment."
    s "Maybe they'd spent their money on that equipment, but that doesn't sound like most bandits I know."
    orc "You think is something else?"
    s "They might be part of something bigger. A wannabe mercenary company, maybe. I think we should be on our toes."
    orc "Okay. But was still good victory."
    if orcalliance == "tekrok":
        hide orcbase2 at center
        hide orcloincloth2 at center
        hide orchelmet2 at center
        hide orcpiercing2 at center
        hide orcshoulder2 at center
        hide orcstrap2 at center
        hide orcwrap2 at center
        hide orcbeard21 at center
        hide orcemo2 angry at center
        with moveoutright
        "At that moment, her commander shifted away, and Sabia soon saw why. Tekrok was stomping toward her - so he had come after all?"
        show tekrok normal at right with moveinright
        t "You did well, Sabia. Tekrok respects this."
        s "Thanks for your help."
        t "Tekrok did not come to help you, but to secure victory."
        s "Whatever you say, then. Did these bandits seem unusually well-equipped to you? Do you know anything about this?"
        t "No... but Tekrok agrees that it is unusual. This is worth considering in the future."
        "Sabia talked with Tekrok for a while longer, making sure that they finished things cleanly, and then they finally headed back to camp to lick their wounds and count their spoils."
    elif orcalliance == "rokgrid":
        hide orcbase2 at center
        hide orcloincloth2 at center
        hide orchelmet2 at center
        hide orcpiercing2 at center
        hide orcshoulder2 at center
        hide orcstrap2 at center
        hide orcwrap2 at center
        hide orcbeard21 at center
        hide orcemo2 angry at center
        with moveoutright
        "At that moment, her commander shifted away, and Sabia soon saw why. Rokgrid was walking toward her - so he had come after all?"
        show rokgrid happy2 at right with moveinright
        r "Excellent work, Sabia! I'm glad I was here to assist you, but I think you would have managed even without me!"
        s "I appreciate the backup. But did these bandits seem unusually well-equipped to you? Do you know anything about this?"
        show rokgrid sad2 at right
        r "No, and this fact is troubling. I try to keep tabs on all military forces, especially human ones not aligned with Lundar."
        show rokgrid happy2 at right
        if rokgridsecondraidmeal:
            r "But this will be something to investigate later! For now, we should celebrate our victory!"
            scene bg rokgridtent
            call sabiabase
            show rokgrid happy2 at right
            with dissolve
            "Rokgrid ushered Sabia to a tent that had been set up, where she discovered that another dinner was waiting. Sabia wasn't going to refuse a decent meal, but she had to smile that he was trying to set up exactly the same events as last time."
            "Well, that didn't make him less subtle than a lot of humans she knew. Sabia didn't roll her eyes at him and just chatted - honestly, it wasn't hard to pretend to be happy at all, still flush from her victory."
            "And when he reached across the table to take her hand... well, there were worse ways to work off stress from the battle..."
            call rokgridraidsex
            $ rokgridfoodunlocked = True
            "Afterward, Sabia saw deep affection in Rokgrid's eyes. She didn't share it, but she did think this was an important alliance she needed to strengthen as much as possible."
            "So far, he'd always initiated their dinners, and seemed a little cautious. Perhaps she should take the initiative, if she wanted to pursue this further..."
        else:
            r "But this will be something to investigate later! For now, you should celebrate our victory!"
            "Sabia talked with Rokgrid for a while longer, making sure that they finished things cleanly, and then they finally headed back to camp to lick their wounds and count their spoils."
    elif orcalliance == "dajrab":
        "Sabia looked toward Dajrab's troops, wondering if the Captain had come to watch, but there was no sign of him."
        "Since it looked like he wasn't showing, Sabia talked with her commander for a while longer, making sure that they finished things cleanly, and then they finally headed back to camp to lick their wounds and count their spoils."
    else:
        "Sabia talked with her commander for a while longer, making sure that they finished things cleanly, and then they finally headed back to camp to lick their wounds and count their spoils."
    jump eastern_frontier_map


label SUtentacle1:
    $ SUgivententaclequest = True
    scene bg mainhall
    call sabiabase
    show vehlis normal at right
    show vehlis2 arm1 at right
    with dissolve
    "Sabia noticed that Vehlis wasn't conducting business in her usual room, but speaking to several warriors in the hall. The conversation seemed to end with neither side happy, leaving Sabia curious, so she approached."
    s "Something wrong?"
    show vehlis open at right
    vehlis "I assume you already heard about the unusual number of orcs dying in excursions outside of camp?"
    show sabiaemo closed2 at left
    s "I mean, I did, but didn't that stop? I thought they got the monsters responsible."
    "The actual \"monster\" responsible had been Kia, who Sabia thought had understood that she needed to stop killing orcs. If she had reneged on the deal... but Vehlis was shaking her head."
    show sabiaemo normal at left
    show vehlis closed1 at right
    vehlis "Too many people have been assuming that there was only a single explanation. But life is rarely that simple."
    show vehlis normal at right
    vehlis "Alioch treated an orc that died of what seemed to be hanging - but the injury on the neck had signs of acidic burn. I think we might have a tentacle monster on our hands."
    show sabiaemo surprised1 at left
    s "Seriously? But this is far outside their usual territory... and wouldn't they have left a bunch of slime and other signs?"
    show vehlis eyebrow2 at right
    vehlis "I said a singular monster for a reason, they behave differently - look, I don't have time to explain everything. The point is that if one is alone, it wouldn't leave the usual signs. I'm fairly sure I'm right, but the warriors aren't convinced it's worth it."
    show sabiaemo normal at left
    s "You wanted them to remove the threat?"
    show vehlis closed2 at right
    vehlis "No, a singular monster isn't such a serious threat. But tentacles can be harvested for many valuable ingredients: their slime is potent, their skin is tough, and of course limbs can be converted into... useful tools."
    s "I have some idea."
    show vehlis normal at right
    vehlis "All those things are doubly valuable in a location like this, where tentacles are rare and there's no local trade in them. But it seems nobody is interested in taking the risk."
    show sabiaemo closed1 at left
    s "And so you explained all this because you're hoping I will?"
    show vehlis happy at right
    vehlis "If you could capture the creature alive - or at least kill it - I would be able to sell it and I'd give you a significant cut of the profits."
    show vehlis normal at right
    vehlis "But I warn you, it might be difficult to find. Lone tentacles tend to hide, and even with our reports on the area of attacks, it would take a skilled tracker to find its lair."
    show sabiaemo normal at left
    s "Hmm... I'll consider it."
    "Vehlis nodded and returned to her room, leaving Sabia to consider the opportunity. It might be a pain to track down the tentacle herself, but she could see the benefits."
    if nevedildohint:
        "Sabia recalled that Neve had expressed interest in tentacle monsters - to make a dildo, but still, she might have more expertise. Since Sabia had no experience with tentacles except one aftermath on the western front, perhaps it would be good to reach out to the elf."
    else:
        "She didn't have any experience with them herself except one aftermath on the western front. If she did pursue it, she'd need to find someone more knowledgeable."
    return

label SUtentacle2:
    if SUnevejoined:
        $ SUtentacleprogression = 1
        scene bg countryside
        call sabiabase
        show neve1 at right
        show neveemo normal at right
        with dissolve
        "With Neve joining her, Sabia headed out to hunt for the tentacle with more confidence. Neve definitely set their direction, but they walked together as they headed out."
        "Though Sabia had assumed they'd talk along the way, she wasn't quite sure how to start a conversation. Plenty had passed between the two of them, so why were things strange and awkward now?"
        show sabiaemo closed2 at left
        s "So... what exactly are we going to do when we find the tentacle?"
        show neveemo eyeroll2 at right
        n "Finding it is the first step, which might not be so easy. But once we do, you'll want to dress properly."
        show sabiaemo irritated2 at left
        s "Dress properly? You mean get ready to fight it? I don't know if I have enough armor to defend against their slime..."
        show neveemo closed1 at right
        n "Armor isn't usually the way to go. Some of them can melt through metal, and in any case that's not the main problem."
        show neveemo normal at right
        n "No, the main threat when fighting tentacles is them getting a grip on you in the first place. You want to go in as light as possible."
        show sabiaemo normal at left
        s "That makes sense. I'll try to remember for next time."
        show neveemo happy1 at right
        n "You haven't fought any tentacles before, I take it?"
        show sabiaemo closed2 at left
        s "No, never had a chance. I hear there are some infesting the southern part of the Tellian Mountains, but there was only one time..."
        show sabiaemo sad2 at left
        s "Usually we were alert for minotaurs, so when a group disappeared, we assumed it was them. But when we found them... they'd been torn to pieces and there was tentacle slime everywhere."
        show neveemo closed2 at right
        n "And you were all really tense for a while but they never showed up again?"
        show sabiaemo normal at left
        s "Yes, exactly! Do you know something about why it might have been?"
        show neveemo normal at right
        n "Sorry, don't have any answers there. They probably had some reason to attack that group that makes sense only to them."
        show neveemo closed3 at right
        n "Tentacles aren't just animals, but they're definitely not like people. The difference between, say, humans and orcs is much smaller than the difference between either and tentacles."
        show sabiaemo closed1 at left
        s "How did you end up getting experience with tentacles?"
        show neveemo happy1 at right
        n "Oh, I headed straight into the Sorthyos Wilds to look for them. Had some interesting encounters, but I never found one of their nests so I can't say that I really understand them."
        show sabiaemo normal at left
        s "What do you mean?"
        show neveemo closed1 at right
        n "Tentacles behave differently depending on the size of the group, that much I'm pretty sure of. So I don't know what they'd be like in truly large groups like must be in their nests."
        show sabiaemo happy1 at left
        s "I'm kind of envious, to be honest... you went and explored the Sorthyos Wilds just because you were curious?"
        show neveemo smirk1 at right
        n "Well, I wouldn't have done it if I wasn't prepared. Most of the Wilds is safe enough, but it's not something I'd recommend just anyone try."
        show sabiaemo happy3 at left
        s "No, I more meant the freedom to be able to just explore like that. It sounds nice."
        show neveemo happy2 at right
        n "...in my experience, freedom isn't something that you can be given. It's something you have to take."
        show sabiaemo normal at left
        s "Hmm..."
        show neveemo happy1 at right
        n "But you're talking like you're some peasant who lived in one town her entire life. You got to travel a lot while in the war, right?"
        show sabiaemo closed4 at left
        s "Sure, and I did enjoy some of that. It's different when you're a soldier, though, because you're always taking your camp with you."
        show sabiaemo pout3 at left
        s "And once I was promoted, I ended up in more headquarters positions. So I didn't get much meaningful travel until... well, until now, basically."
        show neveemo happy3 at right
        n "Heh. You might not enjoy the circumstances, but I guess you do have your freedom, huh?"
        show sabiaemo closed2 at left
        s "I don't know... I actually feel more bound than before. There's so much I need to do..."
        show neveemo closed2 at right
        n "And yet you're jaunting off to go hunt a tentacle monster. Not something you did much before, I'm guessing."
        show sabiaemo normal at left
        s "That's... hmm, I guess I should think more about that..."
        show neveemo normal at right
        "Sabia lapsed into silence for a time, considering what Neve had said. She'd been so focused on her goals for so long, she hadn't considered things in that light."
        "Freedom might be nice, but in a way it was the opposite of responsibility. If she got what she wanted, struck back against her family, would that mean she traded one for the other? That was a good trade, or so she told herself, and yet..."
        "Sooner than she had expected, they arrived at a location that seemed notable to Neve. She bent down and examined dead leaves for a while, which looked no different to Sabia than the others, then eventually rose and showed her one."
        show neveemo closed1 at right
        n "You see the shine? That's not how these leaves should look... this is dried tentacle slime."
        show sabiaemo annoyed1 at left
        s "But you said it wouldn't be leaving slime?"
        show sabiaemo normal at left
        show neveemo normal at right
        n "In areas it fights, no. But it will still leave slime in areas where it makes a nest."
        "Neve tossed the leaf aside and got to her feet, brushing off her hands."
        show neveemo irritated2 at right
        n "This place is long dried. That means that the tentacle is making multiple nests, likely moving every few days."
        show neveemo normal at right
        "Neve turned around and headed in a new direction, forcing Sabia to hurry to follow her."
        show sabiaemo closed2 at left
        s "Is it just being cautious, do you think? Or is that natural behavior?"
        show neveemo closed1 at right
        n "I'm not sure, but it's possible that it's moving somewhere. We need to check for other old nests."
        "After searching around for some time, they found a second one. Based on the signs that Sabia could still barely see, Neve thought that she had a rough idea where the tentacle might be, which was unfortunately far from their current position."
        "They returned to camp wearily, but Sabia was hopeful that they'd be able to track the tentacle down next time."
    else:
        if Sabia.stamina >= 200:
            $ Sabia.stamina -= 200
            scene bg countryside
            call sabiabase
            with dissolve
            "Sabia headed out fresh, determined to search until she found the tentacle's lair. But though she searched the area where the orcs had gone missing thoroughly, she couldn't find any sign of the tentacle. Maybe this really was beyond her own abilities."
        else:
            $ Sabia.stamina = 0
            scene bg countryside
            call sabiabase
            with dissolve
            "Sabia attempted to find the tentacle, but wore herself out before she had gotten very far. She limped back to camp completely exhausted."
    return

label SUtentacle2neve:
    $ SUnevejoined = True
    scene bg countryside
    show backdrop
    call sabiabase
    show neve1 at right
    show neveemo normal at right
    with dissolve
    "As Sabia approached Neve, she wondered just how to bring this up. She couldn't just blurt it out, but she'd feel incredibly awkward trying to be too casual about it."
    "After a moment, Sabia shook her head and decided to just go through with it. This could benefit them both, after all, so there was no reason to hesitate."
    show sabiaemo happy1 at left
    s "Neve, are you busy? I was wondering if we could work together on something?"
    show neveemo closed1 at right
    n "Well, you know the types of things I don't like to get involved in..."
    show sabiaemo normal at left
    s "It's nothing political. But Vehlis thinks there's a tentacle that could be tracked down, and I think you have some experience with that..."
    if nevedildohint:
        show neveemo smirk1 at right
        n "Heh, you {i}know{/i} that I'm interested in them. Such useful creatures... especially useful appendages.."
        show sabiaemo closed2 at left
        show sabiaemo2 blush at left
    else:
        show neveemo happy2 at right
        n "Yes, I'm interested in them."
        show sabiaemo happy1 at left
    s "So... will you help me? You can have half of whatever I earn from Vehlis."
    show neveemo closed2 at right
    n "I'll help you in return for first choice of the tentacle's byproducts, which will probably be valued at less than half."
    show sabiaemo happy1 at left
    hide sabiaemo2 blush at left
    s "Deal!"
    show neveemo happy1 at right
    n "Then just let me know when you want to head out. I'll be right with you."
    return

label SUtentacle3:
    $ SUtentacleprogression = 3
    $ SUgreyisle_prompt = 1
    scene bg countryside
    call sabiabase
    show neve1 at right
    show neveemo normal at right
    with dissolve
    "Sabia headed out to meet up with Neve and try to track down the exact location of the tentacle. When she arrived, the dark elf glanced her over."
    if Sabia.armor == Rags:
        $ A_neve += 1
        show neveemo happy2 at right
        n "I see you remembered what I said about wearing light clothing. I appreciate that."
        show sabiaemo happy1 at left
        s "Of course. Can we go hunt this thing now?"
    else:
        $ Sabia.equip(Rags,inventory="yes")
        show neveemo closed1 at right
        n "You're going to want lighter clothing than that, Sabia."
        show sabiaemo closed2 at left
        s "Alright, give me a minute to get changed..."
        scene bg black with dissolve
        pause 1
        scene bg countryside
        show neve1 at right
        show neveemo normal at right
        with dissolve
        call sabiabase
        with moveinleft
        s "Will this do?"
        n "That will do just fine. Let's go."
    show sabiaemo normal at left
    show neveemo normal at right
    "They headed out at a quick pace, faster than before since Neve seemed to have a clear idea where their target might be. Sabia was glad to find that she could keep up without too much difficulty."
    show neveemo smirk1 at right
    n "You seem eager about this."
    show sabiaemo closed3 at left
    s "Not to seem greedy, but I'm really looking forward to the profit we can get from harvesting this tentacle. I don't want to spend years of my life working in an orc camp."
    show neveemo happy1 at right
    n "They can certainly be very profitable. I did a hunt once before and it got us a decent amount of coin even after losing a large percentage to resellers. Hopefully with Vehlis we'll get more of the value."
    show sabiaemo irritated2 at left
    s "You know... if tentacles are worth so much, why don't we see more widespread hunting of them?"
    show neveemo closed1 at right
    n "Because it's more dangerous the more tentacles you try to fight. I can think of a couple examples. I heard that the minotaurs tried to harvest an entire nest of tentacles, though that was more for religious ritual than money. The tentacles hit back until they came to a truce."
    show sabiaemo surprised1 at left
    s "They're capable of retaliating?"
    show neveemo normal at right
    n "Somewhat indiscriminately, but yes. They're not normal animals."
    show sabiaemo normal at left
    s "And what was the other example?"
    show neveemo closed4 at right
    n "A couple Carchedonese traders funded an expedition deep into the Grey Isle to try to bring back a huge harvest. None of them ever returned."
    show sabiaemo closed2 at left
    s "..."
    show neveemo happy1 at right
    n "That one isn't just a spooky story, either. Ask Vehlis, there are records of the whole thing. Anyway, in general since it's difficult to harvest tentacle ingredients, most are happy to keep them rare. They wouldn't want to flood the market and undercut their profits, anyway."
    show sabiaemo normal at left
    s "Hmm... well, it's a good thing that this one is alone, then."
    show neveemo normal at right
    n "Yes, in my experience they aren't so smart on their own. Stay cautious, but don't worry too much."
    "They chatted about lighter subjects as they got further from camp, then Neve drew silent as she began to focus, apparently following signs that Sabia couldn't notice."
    "They soon reached a hilly area that had something odd about it that Sabia couldn't quite put her finger on. Neve bent down to examine something, then abruptly stood up and shook her head."
    show neveemo irritated1 at right
    n "I really thought it was headed this way, but I guess I was wrong."
    s "How can you tell?"
    show neveemo closed1 at right
    n "We're actually on top of a nest, but it's an old one. Hasn't been used in years."
    show sabiaemo surprised3 at left
    "Sabia shifted uncomfortably, gaze shifting beneath her."
    s "The nest is under the ground? Right beneath us?"
    show neveemo normal at right
    n "Not directly beneath, no. I don't think anyone knows the full layout of a nest, but there are smaller tunnels near the surface away from the entrances. They might be to let air through, though I don't know if tentacles need to breathe."
    show sabiaemo normal at left
    "Neve walked some distance away and kicked at the earth, uncovering a small hole. It could have been just a rabbit burrow or something similar, but it made Sabia uncomfortable."
    show neveemo happy1 at right
    n "You see? Absolutely no residue, no scent... this would be a logical place for the tentacle to stay, but there's no sign of it."
    show sabiaemo irritated2 at left
    s "Huh, then I guess we need to retrace our steps. But are these really air tunnels?"
    "Sabia moved alongside Neve and poked at the tunnel with her foot. It did indeed feel old and undisturbed. Curious about the shape of it, Sabia set above shifting some more dirt with her foot."
    show neveemo irritated2 at right
    show sabiaemo surprised2 at left
    "And without warning, a {i}lot{/i} of dirt began to shift."
    "There was the loud sound of something collapsing underneath them and Neve leapt to her feet, but even her reaction time wasn't enough. By the time she had her footing again, the ground was giving way underneath them and they dropped down in a shower of rocks and dirt."
    call SUtentaclesex1
    scene bg countryside
    call sabiabase
    show neve1 at right
    show neveemo normal at right
    with dissolve
    "They dug their way out of the hole carefully, ready for an attack, but none came. Neve hopped out first, eyes cautious, then shook her head."
    n "I think it's really gone."
    "She extended a hand and helped pull Sabia out of the hole. Sabia brushed herself off and frowned at nothing in particular."
    show sabiaemo annoyed1 at left
    s "You said there were no signs of it."
    show neveemo closed1 at right
    n "I don't think I was wrong about that... it's just smarter than I gave it credit for. I think it knew we were following and was more careful."
    show sabiaemo closed2 at left
    s "But if it had wanted to hurt us, that was the perfect time."
    show neveemo normal at right
    n "If I had to guess... I think it's confused. Maybe it got separated from its nest somehow and it isn't sure what to make of things."
    "Sabia massaged her forehead as she considered the new information."
    show sabiaemo angry1 at left
    s "Okay, fine... We need to think one step ahead of it. Maybe we can lure it in?"
    show neveemo closed4 at right
    n "Not today, we can't. I'm sure it will flee to another location, so we'll have to track it down again."
    show sabiaemo irritated1 at left
    s "I agree. Plus, we should prepare... I don't know if there are any traps that work on tentacles, but at minimum we can get food to help lure it."
    show neveemo happy2 at right
    n "Heh. Unless you want to arrange another tunnel collapse, I think that's a good idea..."
    show neveemo normal at right
    show sabiaemo normal at left
    "They headed back to camp together, discussing the possibilities. Sabia was still determined to harvest the tentacle, but it was strange to think that it knew they were pursuing it and was trying to avoid them."
    "Of course, many animals acted that way around humans. She didn't know many that wouldn't have taken the chance to hurt them, but Sabia couldn't afford to think about that if she wanted to get this done."
    return

label SUtentacle4:
    $ SUtentacleprogression = 4
    scene bg countryside
    call sabiabase
    show neve1 at right
    show neveemo normal at right
    with dissolve
    "Sabia met Neve outside of camp with a sack filled with bloody meat. The grimy sack the orcs had given her made her stomach turn over, but she doubted that a tentacle would be so discerning."
    "This time Neve led the way faster than usual, eyes constantly darting from sign to sign. Sabia thought she could pick up on some of what Neve was seeing, though she couldn't pick things up herself. It seemed that Neve was looking first for quiet, dark locations that the tentacle might like, then scanning for other signs."
    "Soon enough, they reached a clearing that made Neve pause. It was closer to camp than the other ones had been - was the tentacle getting closer?"
    show sabiaemo irritated1 at left
    s "Is it here?"
    show neveemo closed3 at right
    n "Ssh. I think it might be, but it's hiding."
    show sabiaemo irritated2 at left
    s "Then... do we lure it out?"
    show neveemo closed1 at right
    "Neve closed her eyes for a long moment, concentrating on something, then abruptly shook her head."
    show neveemo normal at right
    n "No. I have the feeling it's confused, too frightened to talk to us... let's not try to meet it today."
    show sabiaemo normal at left
    "Instead they left the meat out somewhat near the clearing, then retreated. Sabia felt a little disappointed, but when they moved some distance away, Neve put a finger to her lips and nodded toward a large tree."
    "With a boost from Neve, Sabia was able to get into one of the lower branches. Neve leapt up beside her the next moment and they both crept to a position where they were partially blocked by leaves, but could still see the meat."
    "They waited a very long time, long enough that her tension was starting to turn to boredom and Sabia considered breaking her silence. Then, abruptly, she saw a dark flicker."
    scene bg countryside
    show SUtentacle 1
    call sabiabase
    show sabiaemo surprised1 at left
    show neve1 at right
    show neveemo irritated2 at right
    with dissolve
    "She held her breath as she saw the tentacles slide across the ground toward the meat. They circled around it, reared up... and then shifted in their direction."
    "Even from a distance, the low keening sound cut straight into her ears. Sabia hadn't known what she expected a tentacle to sound like... but it wasn't that."
    show SUtentacle 2
    "It then went silent, as if waiting for a response. Sabia and Neve glanced at each other, but stayed silent."
    hide SUtentacle 2 with dissolve
    "After enough time passed, the tentacles abruptly moved, wrapping around the meat and then surging away. In moments there was nothing left but the sack, no sign of the tentacle monster at all. Sabia let out her breath heavily."
    show sabiaemo normal at left
    s "So that's done. You think it knew we were here?"
    show neveemo closed1 at right
    n "I swear, others were dumber than this... maybe it's a different type? But yes, it knew we were here."
    show sabiaemo happy1 at left
    s "It accepted the food, though."
    show neveemo happy1 at right
    n "Yes, it's a good first step. I think we need to make it more comfortable before we get any closer."
    show sabiaemo normal at left
    s "So that's all for the day?"
    n "Probably so, yeah."
    "Sabia climbed down the tree, a little disappointed that they hadn't been able to do more. Still, it was progress."
    return

label SUkiameetsneve:
    $ SUtentacleprogression = 5
    scene bg countryside
    call sabiabase
    with dissolve
    "Sabia headed out to the point where she'd agreed to meet Neve, but found the elf had yet to arrive. Restless with thoughts of what they were planning, Sabia shifted the new sack of meat uncomfortably from hand to hand."
    "After a time, she realized that she was being watched. Her eyes narrowed suspiciously and she put a hand on her weapon, trying to find the source. She didn't think it was just her imagination, yet now she was uncertain. It didn't feel like a threat..."
    show kia happy2 at right with dissolve
    "Abruptly Kia popped up from behind a bush. Sabia imagined her watching through the leaves and breathed a sigh of relief."
    kia "Sabia! Hello!"
    show sabiaemo happy1 at left
    s "Hello, Kia. I'm glad it's just you."
    show kia happy1E at center with moveinright
    "Kia padded closer silently, peering at her. She bent down and sniffed at the bag cheerfully."
    kia "Give Kia? Kia eat?"
    show sabiaemo closed3 at left
    s "Sorry, Kia, but it's not for you. We need to... uh..."
    show sabiaemo closed2 at left
    "How the hell could she explain something like that. Kia blinked at her, expecting a sentence, then eventually cocked her head and tried on her own."
    show kia tilt1 at center with dissolve
    kia "Sabia hunt?"
    show sabiaemo normal at left
    s "No, not re... well, kind of. It's a little different."
    show kia tilt1b at center
    kia "..."
    s "I'm not here to hunt. I'm here to meet someone."
    show kia pawtilteager2 at center with dissolve
    kia "Ylva?"
    show sabiaemo closed1 at left
    s "Sorry, not Ylva. Someone else. Someone who doesn't know you, so they might be scared."
    show kia happy1 at center with dissolve
    "Kia nodded seriously and shifted into the shadow of a tree."
    kia "Kia hunt."
    show sabiaemo sad1 at left
    s "I... don't know if that's a good idea. It might be better if y-"
    show kia angry3 at center with dissolve
    "Without warning Kia lunged at her, grabbing Sabia's shoulder with one paw and easily pulling her back. Kia's eyes were bright and her gaze was fixed on the woods on the other side of the clearing. Sabia followed it..."
    show neve1 at right
    show neveemo normal at right
    with dissolve
    "And discovered Neve standing there, a slightly curious expression on her face. Kia pulled Sabia behind her."
    show kia angry5 at center
    kia "Sabia! Danger!"
    show sabiaemo surprised1 at left
    s "What? You mean N-"
    show kia power2 at center with dissolve
    kia "Danger!"
    "Hairs all over Kia's body were rising and her claws were shifting dangerously. Neve saw the threat as well and casually shifted her hands into a different position."
    show neveemo happy1 at right
    n "Did you get a new pet, Sabia?"
    show sabiaemo angry2 at left
    "Sabia realized that she had only a short time to say something and stop things from turning bad."
    menu:
        "Wait, stop!":
            show sabiaemo angry1 at left
            "Sabia desperately reached out to grasp Kia as she called out. Though she couldn't overpower the Makhor, her words did seem to reach her. Kia blinked at her, then eyed Neve suspiciously."
            show kia angry1 at center with dissolve
            kia "Not... enemy?"
            n "I'm not here to hurt you."
        "She's a friend!":
            $ A_neve += 1
            show sabiaemo angry1 at left
            "Sabia desperately reached out to grasp Kia as she called out. Though she couldn't overpower the Makhor, her words did seem to reach her. Kia blinked at her, then eyed Neve suspiciously."
            show kia tilt2 at center with dissolve
            kia "Is friend?"
            n "I'm not here to hurt you."
        "She's {i}fsskit!{/i}":
            $ A_kia += 1
            show sabiaemo angry1 at left
            "Sabia desperately reached out to grasp Kia as she called out. Though she couldn't overpower the Makhor, her words did seem to reach her. Kia blinked at her, then eyed Neve suspiciously."
            show kia pawtiltconfused at center with dissolve
            kia "Is {i}fsskit{/i}?"
            n "Not sure what that means, but I'm not here to fight."
    show sabiaemo irritated1 at left
    show kia angry1 at center with dissolve
    "Kia continued eyeing Neve suspiciously. After a pause, Neve took her hands off her blades and shifted back slightly. Sabia breathed a sigh of relief as the most dangerous moment passed, though the clearing was still thick with tension."
    show neveemo happy2 at right
    n "My name is Neve. I'm Sabia's friend."
    show kia angry2 at center
    kia "Danger."
    show neveemo closed2 at right
    n "Maybe. Seems to me that {i}you're{/i} pretty dangerous too. Do I need to protect Sabia from you?"
    show kia irritated3 at center
    kia "Not!"
    show neveemo normal at right
    "Neve shrugged and looked to Sabia, though she was careful not to move any closer."
    show sabiaemo closed2 at left
    s "This is... hard to explain. But I ran into her after the Arena..."
    show neveemo closed1 at right
    n "And it's not hard to guess what she is. I've only spotted a Makhor once from a distance... I didn't realize they could take a form like that."
    show kia tiltirritated at center with dissolve
    show neveemo normal at right
    "While they spoke, Kia looked between them, as if still skeptical, a low growl still vibrating from her. Sabia sighed and stepped in between them before turning to face Kia."
    show sabiaemo normal at left
    s "Kia, it's alright. She's safe. She's on our side."
    show kia pawuncertain1 at center with dissolve
    n "..."
    show kia pawtiltcurious at center with dissolve
    "Kia approached cautiously, moving herself between Sabia and Neve before stalking closer. Sabia saw Neve's stomach flex as she shifted into a slightly more prepared stance, but kept her posture passive."
    "She dropped down onto all fours, then sniffed at the metal on one of Neve's leggings suspiciously. After looking up at Neve for a while, she shifted up with her paws on Neve's waist, now sniffing at her belt. Neve bore this with a slight chuckle."
    show neveemo happy2 at right
    n "I guess you must be attuned to magic. Shouldn't be surprised."
    show kia pawtilteager1 at center with dissolve
    kia "Claws sharp."
    "After plucking at Neve's blades, Kia reared up onto her legs to sniff all around Neve's top. Kia did not seem to notice that this had her rubbing herself all over Neve's breasts, but Neve shot Sabia another glance."
    show neveemo closed1 at right
    n "Are you about done? I don't like having such dangerous claws so close to me."
    show kia normal1 at center with dissolve
    "Kia dropped back, thoughtfully staring at Neve. After a time, she released a barking growl."
    show kia happy1 at center with dissolve
    kia "Danger smell not bad."
    show neveemo happy3 at right
    n "Well, thank you!"
    show sabiaemo happy1 at left
    "Now that things seemed calmer, Sabia moved in between them and smiled."
    s "Neve... meet Kia. I guess it's good that it happened now instead of at some worse time."
    show neveemo happy2 at right
    n "She seems fun. I want to pet all that hair, but I'm guessing she wouldn't want me touching her."
    show kia normal2 at center with dissolve
    "Kia shifted beside Sabia, wrapping her arms around her protectively."
    kia "Not smell bad. Not {i}fsskit{/i}."
    show sabiaemo normal at left
    s "Give her some time to warm up to you."
    show neveemo happy1 at right
    n "I'd be happy to, but she can't come along. The scent of a predator like her is sure to scare off anything."
    show kia pawtilteager1 at center with dissolve
    kia "Hunt?"
    show sabiaemo closed2 at left
    s "Kind of... but not hunting in the same way."
    show kia happy2 at center with dissolve
    "Kia nodded, licked along the side of Sabia's face, then darted away. She stopped some distance from them and turned back with a smile, pausing a moment before darting away."
    kia "Later sit!"
    hide kia happy2 with moveoutleft
    "Then she was gone. Neve watched her disappearing form, smiling slightly, then turned back to Sabia with an eyebrow."
    show neveemo happy3 at right
    n "Not bad, Sabia."
    show sabiaemo happy3 at left
    s "Haha, maybe. Let's go and get this finished."
    show neveemo closed2 at right
    n "I think I'd like to ask some questions about our new friend on the way..."
    scene bg black with dissolve
    pause 1
    scene bg countryside
    call sabiabase
    show neve1 at right
    show neveemo normal at right
    with dissolve
    "The conversation about Kia was less awkward than Sabia had feared. Neve seemed to be positively inclined toward the Makhor, though Sabia wasn't sure how well things would work out."
    "But as they moved on, Neve started frowning. Eventually she stopped in a dark clearing like those they usually scanned for traces of the tentacle, folding her arms and tapping one foot thoughtfully."
    show sabiaemo irritated1 at left
    s "Something wrong?"
    show neveemo closed3 at right
    n "I guessed that it would come this way, but apparently I was wrong. Let's keep moving."
    show neveemo normal at right
    show sabiaemo normal at left
    "They took a wide arc to check other locations, but still came up with nothing. Eventually Neve frowned and set off swiftly in one direction."
    show sabiaemo irritated2 at left
    s "Did it get better at hiding its tracks again?"
    show neveemo closed1 at right
    n "Maybe, but maybe not."
    show neveemo normal at right
    "Eventually they reached their destination, which Sabia recognized as the location they'd explored the previous time even before she saw the caved in portion. Neve bent down, examined something, and shook her head."
    show neveemo happy1 at right
    n "Fresh slime. It didn't move like it did before."
    show sabiaemo normal at left
    s "What does that mean? Is it staying here?"
    show neveemo normal at right
    n "Considering how many of the upper tunnels collapsed, I can't imagine it would be a good nest. I'm not sure what to think."
    s "Well, it's possible that it expected us to come back. Let's leave the food in a non-threatening manner and go."
    show neveemo closed2 at right
    n "Perhaps that's best for now."
    "Sabia dumped out the sack of meat, glad not to have to carry it any more. There was no sign of the tentacle aside from traces of its previous presence, so they left to retreat to a safe distance."
    scene bg countryside
    show SUtentacle 1
    call sabiabase
    show sabiaemo surprised1 at left
    show neve1 at right
    show neveemo irritated2 at right
    with dissolve
    "And promptly discovered the tentacle slithering through the trees behind them."
    "Sabia froze for a second, then started to jump for her weapon, but Neve's hand shot out to catch her wrist. They stayed like that, motionless, and Sabia realized that though the tentacles were moving about restlessly, they weren't getting any closer."
    show sabiaemo surprised2 at left
    s "What?"
    show neveemo closed1 at right
    n "It can read our intentions a little and I don't want it turning aggressive."
    show sabiaemo irritated2 at left
    s "What are we going to do about it, though?"
    show SUtentacle 2
    "In response, the tentacle monster released a low keening noise again. Sabia didn't see anywhere on the tentacled mass where the sound might come from, it almost seemed to echo directly in her mind. It sounded... confused? Or maybe that was just her interpretation."
    show neveemo happy1 at right
    n "Hey there, tentacle. We're not here to hurt you."
    show sabiaemo sad1 at left
    s "But we..."
    show sabiaemo surprised1 at left
    show SUtentacle 3
    "When Sabia started to speak, the tentacle creature shrank back, its tentacles lashing a little faster. Sabia's eyes widened."
    s "Can it understand us?"
    show neveemo normal at right
    n "I really doubt that, but it must be able to sense something about us. Let's back off before we send it running again."
    "Considering how quickly the tentacles were slithering, Sabia was happy to do so. They retreated from the pile of meat, and once they were a sufficient distance away, the tentacles started crawling forward."
    show SUtentacle 2
    "They curled around the pile of meat but didn't drag it away, instead releasing another keening noise in their direction. Neve nodded for them to take another step back, but the tentacle didn't run off with the food yet."
    show sabiaemo sad1 at left
    s "Does it sound lonely to you?"
    show neveemo closed1 at right
    n "Maybe. I doubt it likes being alone like this, but I expected it to just be afraid of us."
    show sabiaemo closed2 at left
    s "Might it be... risky to attack it? You said earlier about tentacles retaliating..."
    show neveemo smirk1 at right
    n "Getting soft, Sabia?"
    show sabiaemo sad1 at left
    "Neve's eyes were dancing playfully, though. She watched Sabia for a moment, then directed her attention to the tentacle with a smile on her face."
    show neveemo happy2 at right
    n "I'll admit, I'm much more curious to learn about why this one is different than to get some money."
    show sabiaemo closed2 at left
    s "I do still need resources, but I feel like just killing it might be short-sighted..."
    show sabiaemo normal at left
    hide SUtentacle 2 with dissolve
    "Abruptly the tentacle made a loud keening, wrapped its limbs around the meat, and slithered off. Sabia sighed... until she noticed that it had left behind something."
    "She was cautious, but Neve moved forward swiftly, bending down next to where the tentacle had been. She chuckled and glanced back at Sabia."
    show neveemo closed2 at right
    n "Look at this. It shed."
    show sabiaemo surprised1 at left
    "Sabia blinked and looked closer, realizing that what she had taken as a tentacle was more like a sheath of skin. It glistened with fresh slime."
    s "They shed? Like... like snakes?"
    show neveemo normal at right
    n "I don't think it's like snakes at all, but I'm not sure. But anyway, this is valuable. Not as valuable as slaughtering the whole tentacle, but it's worth something."
    show sabiaemo irritated2 at left
    s "Thanking us for the meat?"
    show neveemo happy1 at right
    n "I've never once heard of tentacles engaging in any kind of trade, but possibly."
    show sabiaemo normal at left
    "No answers were forthcoming and there was no more sign of the tentacle, so they gathered the shed skin into the sack and headed back."
    show neveemo normal at right
    "On the way back, Neve seemed thoughtful until she finally turned to Sabia and spoke in a low voice."
    show neveemo closed1 at right
    n "I don't think I'm interested in killing it anymore. If that's still your plan, I think I'll leave you here."
    show sabiaemo sad1 at left
    s "No, I... I mean, can we repeat this deal? If we can, then the total would eventually add up to more than just harvesting it, right?"
    show neveemo normal at right
    n "Possibly, though it's a mistake to think we understand tentacles too much."
    show sabiaemo closed4 at left
    s "You have an idea, don't you?"
    show neveemo happy3 at right
    n "Oh, I definitely do. You remember how it touched us last time, don't you? I think we know at least one thing it wants..."
    show sabiaemo closed2 at left
    "Sabia averted her gaze, thinking about that possibility despite her best efforts. Would the tentacle monster thank them for that as well? Might it offer a lot more than for the meat? She tried to tell herself that was the only consideration."
    s "I see what you mean, but I don't know..."
    show neveemo happy1 at right
    n "Look. I'm going to try and experiment with it in a few days. If you want to come with me, feel free to come. If not, that's fine."
    show sabiaemo normal at left
    "Sabia nodded her agreement and they returned to camp in silence. When Sabia offered to share the profit from the tentacle sheath with Neve, she was just waved off."
    $ money += 100
    "Vehlis wasn't present, but Alioch took the sheath and paid her 100 Lundils up front. More than she had expected, for just a little."
    "Sabia headed back into camp with a lot on her mind."
    return

label SUtentacle5:
    $ SUtentacleprogression = 6
    scene bg countryside
    call sabiabase
    show neve1 at right
    show neveemo happy2 at right
    with dissolve
    "When Sabia headed out to meet Neve, she was still a little uncertain. The dark elf's smile made her waver, but she knew she had to make a choice soon."
    n "I'm about to head out to meet our tentacled friend... have you decided if you're coming along?"
    show sabiaemo closed2 at left
    s "I..."
    menu:
        "Refuse":
            show sabiaemo angry1 at left
            s "I won't have anything to do with this. You can do what you have to do, but..."
            show neveemo closed1 at right
            n "Fine, suit yourself."
            "Neve left shortly after that and Sabia watched her go. She felt better about that decision, but she did regret that she'd never be able to harvest the tentacle monster."
            return
        "Join Neve":
            pass
    show sabiaemo pout1 at left
    show sabiaemo2 blush at left
    s "Alright, I'm... I'm with you. You'd better fight if it tries to hurt us, though."
    show neveemo happy3 at right
    n "I don't think it will be a problem, but I'm not suggesting we just throw ourselves at it. The first step is to communicate... this should be interesting."
    show neveemo normal at right
    show sabiaemo normal at left
    hide sabiaemo2 blush at left
    "They made their way to the tentacle's nest quickly and mostly quietly. At the edge, Neve checked for the signs again, then smiled to herself."
    show neveemo happy2 at right
    n "It hasn't moved. That's a good sign."
    show sabiaemo closed2 at left
    s "You didn't ask me to bring meat or anything... you {i}do{/i} have a plan, right?"
    show neveemo happy1 at right
    n "Yeah, I have a theory about how exactly they work. Let's go further in."
    "They moved forward quietly, still not seeing any sign of the tentacle. Neve reached about the middle of the clearing, then settled down on the ground, gesturing for Sabia to do the same."
    n "Now, think happy thoughts."
    show sabiaemo irritated2 at left
    s "Are you serious? It's not like it can read minds."
    show neveemo closed2 at right
    n "Maybe not, but I'm pretty sure tentacles have a sense of smell far superior to ours. The way it hid, the way it reacts to things... I think it can smell slight changes in us. So seriously, adopt a non-threatening attitude."
    show sabiaemo normal at left
    show neveemo normal at right
    "Sabia did her best, wiping the scowl off her face. She tried to reflect on the fact that she trusted Neve, to rescue them from a bad situation if nothing else. And she really didn't plan to kill the tentacle for its parts any more."
    "As for letting it touch them again... well, maybe that wouldn't be so bad. The thought seemed absurd to her, but everything about her life now would have seemed absurd a year ago. She would never have even considered treating a tentacle monster like an intelligent creature, but it might be just that."
    scene bg countryside
    show SUtentacle 2
    call sabiabase
    show sabiaemo normal at left
    show neve1 at right
    show neveemo normal at right
    with dissolve
    "The sound of in-drawn breath from Neve made Sabia open her eyes again. The creature was approaching them now, sinuously moving through the shadows. As before, it stopped before it reached them, but not as far away this time."
    show neveemo happy1 at right
    n "That's right, we're not here to hurt you..."
    show sabiaemo sad1 at left
    "Another keening sound... and this time, the sound in Sabia's mind was joined by a strong impression. For a flickering moment, she felt a sense of isolation and disorientation."
    s "It really is lonely..."
    show neveemo sad at right
    n "You're used to living in a nest, aren't you?"
    "The tentacle monster shifted closer, and the keening went higher. Again Sabia was overwhelmed with a raw sensation: other tentacles around her, working together and unified. It wasn't a warm feeling like being with family, it was something deeper than that: a sense that all was right with the world, everything had purpose."
    "And then the sound shifted sharply and all the purpose was taken away, leaving the tentacle monster alone in dangerous territory. Still coming out of the intense sensations, Sabia felt for it on a deep level."
    show neveemo closed4 at right
    n "You're getting that too, right, Sabia?"
    show sabiaemo closed2 at left
    s "Yes, I am. I don't know how it's happening, but..."
    show neveemo happy1 at right
    n "Don't worry about that. Let's not lose it. We're really not here to hurt you."
    show sabiaemo surprised1 at left
    "That prompted a lower tone and a violent surge of feeling in her mind: Sabia was overwhelmed by the sense of a vast, mindless threat that attacked without reason... until her mind oriented itself and she realized that she was seeing humans and other races from the tentacle's perspective."
    show neveemo sad at right
    n "No, that's not what we want at all..."
    show sabiaemo closed2 at left
    "In response, a sense of... uncertainty. Not curiosity, since she wasn't sure how much the tentacle was even capable of that. The tentacles shifted uncertainly, circling them but not coming any closer."
    show sabiaemo2 blush at left
    "If it was so uncertain now, why had it approached them before and touched her? When Sabia thought back to the tentacle touching her, the memory was so strong it was almost as if she was feeling it again. This time instead of screaming, she flushed, her mind imagining what it would be like to feel those tentacles sliding all over her and Neve..."
    show sabiaemo surprised1 at left
    show SUtentacle 1
    "And abruptly Sabia realized that the tentacle was surging toward them. Her eyes flew wide in alarm and the tentacle immediately stopped."
    show neveemo irritated1 at right
    n "Sabia, what are you doing?"
    show sabiaemo closed2 at left
    s "I was just thinking about last time... I think it felt it..."
    show neveemo happy3 at right
    n "Oh, in that case..."
    show neveemo closed2 at right
    show neveemo2 blush at right
    "Neve closed her eyes and hummed to herself, making Sabia flush as she tried not to think about what Neve might be imagining. The tentacles lifted higher than she'd seen before, on alert. They moved forward, but then shifted back."
    show SUtentacle 2
    "It stayed there, not closing the distance. When it made another keening sound, Sabia got a strong sense of confusion and uncertainty."
    show neveemo smirk1 at right
    n "Are you thinking evil thoughts, Sabia?"
    show sabiaemo surprised1 at left
    show sabiaemo2 blush at left
    s "No! I mean, not particularly."
    show neveemo happy1 at right
    n "I don't think it understands specific words... maybe it picks up on the atmosphere. And I have to admit this is a bit tense..."
    show sabiaemo closed2 at left
    "Sabia took a deep breath, trying to decide if she would really go through with it... but that choice had been made, hadn't it? She wasn't going to come this far with Neve only to back out now."
    show sabiaemo normal at left
    s "If it was willing to approach us the first time, I think we should try to recreate that."
    show neveemo normal at right
    n "I doubt we'll be able to trigger another collapse."
    show sabiaemo closed2 at left
    s "Not that, just the form of it. It might get the idea."
    show neveemo happy2 at right
    n "Hmm... well, I'm willing to try it."
    "The tentacles shrank back when they got to their feet, but didn't flee. Sabia swallowed as she made her way with Neve to the hole where they had fallen... and abruptly the dark elf grabbed her and pulled her over the edge."
    call SUtentaclesex2
    scene bg countryside
    show basenaked at left
    show sabiaemo normal at left
    show nevenaked1 at right
    show neveemo happy2 at right
    with dissolve
    "When it was over, the tentacle shrank away with surprising speed. Sabia had actually been looking forward to relaxing against Neve with the tentacles around them, but apparently the tentacles weren't much for cuddling."
    "Still, it wasn't so bad just resting against Neve like this. Sabia gave Neve a fond smile, but the other woman seemed surprisingly serious."
    show sabiaemo surprised1 at left
    "Only then did Sabia realize that they were being watched. Her entire body tensed up, searching for anything to use as a weapon as she scanned for the threat and saw predatory eyes..."
    kia "What doing?"
    show kia pawtiltcurious at center with dissolve
    "Sabia looked up in shock to find Kia regarding them. She seemed simply curious, sniffing at the seed that covered them and then pulling back with the same expression."
    show sabiaemo2 blush at left
    s "Kia... this... I mean..."
    show neveemo happy3 at right
    n "Haha, I trust she knows what fucking is?"
    show sabiaemo closed2 at left
    s "She knows, it's just not always easy to communicate..."
    "Pushing aside her embarrassment, Sabia pointed toward where the tentacle monster had gone."
    show sabiaemo normal at left
    s "What? Tentacle. Tentacle monster."
    show kia normal2 at center with dissolve
    "Kia promptly shook her head."
    kia "Not. {i}Chufk{/i}."
    show neveemo normal at right
    n "Hmm, is that one of her words? A name for tentacles?"
    hide sabiaemo2 blush at left
    s "I don't know... she hasn't named other species. For example, for her humans are just food."
    "Kia nodded agreement seriously."
    show kia happy2 at center
    kia "Humans food."
    s "Are {i}Chufk{/i} food?"
    show kia tilt1 at center with dissolve
    kia "Not food. {i}Chufk{/i}."
    show sabiaemo irritated2 at left
    s "But this is a \"What?\", right? Not a \"Who?\""
    show kia tilt2 at center
    "Kia stared at her blankly."
    show sabiaemo closed2 at left
    s "I want to know if there's a connection between Makhor and tentacles... can {i}Chufk{/i} be {i}fsskit{/i}?"
    show kia pawtiltcurious at center
    kia "Not. Can be {i}Chufk{/i}."
    n "I'm pretty sure it's a name."
    show kia happy2 at center with dissolve
    "Kia hopped closer and brought her paws down next to Sabia impatiently."
    kia "What doing?"
    show sabiaemo normal at left
    s "That's hard to explain... we needed to get things from the... the {i}Chufk{/i}... so we had to lure it in. Kind of like hunting. But we lured it in via mating."
    show kia normal1 at center
    kia "Not mate."
    show sabiaemo happy1 at left
    s "I'm not saying we're mates, but we did just mate."
    show kia normal2 at center
    kia "Not."
    show sabiaemo closed2 at left
    s "Guess we're just not communicating here..."
    show neveemo happy1 at right
    show sabiaemo normal at left
    n "The thing we just did, I would call mating. You say it wasn't?"
    show kia tilt1 at center with dissolve
    "Kia cocked her head and peered at them for a long time, then settled back with an odd expression."
    show kia neutralE at center with dissolve
    kia "Maybe Sabia mate. {i}Chufk{/i} not mate."
    show neveemo happy2 at right
    n "Ah, that's interesting..."
    show sabiaemo closed1 at left
    s "She might be right. I don't know how tentacles breed, but have you ever heard of anyone getting impregnated from tentacles?"
    show neveemo normal at right
    n "I get the impression it isn't possible, but we have no idea what happens to those who disappear in tentacle nests."
    show sabiaemo closed1 at left
    s "So Kia... I just want to check, it's not a problem? Not dangerous? You're not angry or anything?"
    show kia normal1 at center with dissolve
    kia "{i}Chufk{/i}."
    show sabiaemo irritated2 at left
    s "That's... not very clear."
    show kia tilt1 at center with dissolve
    "Kia blinked at her a few times, then cocked her head again."
    kia "{i}Chufk{/i} are {i}Chufk{/i}."
    show neveemo happy3 at right
    n "She has a point there."
    show sabiaemo angry1 at left
    s "You're not helping!"
    show neveemo happy1 at right
    show kia happy1 at center with dissolve
    kia "Sabia not bad."
    show sabiaemo normal at left
    "Kia approached and gave her face a lick. She then hopped over to Neve with a happier expression than she'd shown before, sniffed her a bit, then licked her face carefully."
    show kia happy2 at center
    kia "Smell good. Who?"
    s "That's Neve."
    show kia pawtilteager2 at center with dissolve
    kia "Neve not bad."
    show kia happy2 at center with dissolve
    "Kia then hopped back, regarded them both with a cheerful expression for a moment, then shot away. Neve watched her go and then chuckled."
    hide kia happy2 with moveoutright
    show neveemo happy2 at right
    n "Like I thought, she's a fun one."
    show sabiaemo closed2 at left
    s "Do you think she'll go back to disliking you when you put the armor on again?"
    show neveemo happy1 at right
    n "Not sure, but I hope she won't be threatening in the future."
    show sabiaemo normal at left
    s "Anyway, let's collect all the slime and get back to camp."
    show sabiaemo closed2 at left
    show sabiaemo2 blush at left
    "Only then did Sabia realize how long she'd been carrying a conversation while naked - in fact, all of them had been completely naked. That was natural for Kia and Neve seemed confident, but Sabia was a little surprised with herself."
    "But given what she'd just done with the tentacle, there wasn't much room for embarrassment. She got cleaned up and dressed before they gathered what they needed and headed back to camp."
    scene bg black with dissolve
    $ money += 220
    "The slime sold for 220 Lundils. A small reward in the end, yet Sabia felt as though the knowledge she'd gained was more valuable..."
    return

label SUtentacle6:
    scene bg countryside
    "When Sabia attempted to find the tentacle again, it seemed to have moved on and she couldn't find traces of it. Neve didn't seem to mind, but Sabia was a little disappointed she hadn't been able to learn more."
    $ SUtentaclequestdone = True
    return

label SUylvalake1:
    $ SUlakequest = 1
    show ylva normal at center
    show ylva2 arm2 at center
    with moveinright
    "When Sabia approached, Ylva seemed preoccupied by something. When she saw Sabia, she smiled slightly and nodded to her."
    show ylva happy1 at center
    ylva "Sabia, do you have a moment? I'm afraid I might need to ask for a favor."
    show sabiaemo closed1 at left
    s "You can definitely ask. What is it?"
    show ylva normal at center
    ylva "It has to do with the lake outside camp... when you have time, please meet me there."
    show sabiaemo normal at left
    s "Got it."
    return

label SUylvalake2:
    $ SUlakequest = 2
    scene bg orclake
    call sabiabase
    show ylva normal at right
    show ylva2 arm1 at right
    with dissolve
    "Sabia hiked out to the lake and found Ylva sitting some distance away. By the time Sabia reached her, she noticed an unusual shifting in the grass, someone moving low and fast... almost definitely Kia."
    "In any case, Kia kept chasing something through the grass while Sabia approached Ylva and nodded to her."
    show sabiaemo happy1 at left
    s "So, what's so important that you didn't want to talk about it in camp?"
    show ylva closednormal at right
    ylva "It's not like that. More that it's personal, plus I wanted to show you the location itself."
    "Ylva turned toward the lake and made a sweeping gesture that encompassed the whole region."
    show ylva normal at right
    ylva "This lake should be a boon for the whole region. At the very least, they could fish there."
    show sabiaemo normal at left
    s "Do orcs... I mean, do warrior tribes fish? Doesn't seem like their type of hunting, really."
    show ylva sad at right
    ylva "Regardless of if they wanted to, right now they don't have much of a choice. The lake is mostly dead and barren, offering little. It may still be a place of beauty, but unless something is done, it will be a fading beauty."
    show sabiaemo sad1 at left
    s "Really? Why'd that happen?"
    show ylva closednormal at right
    ylva "The Lakelord has turned his eye from it. Even after being in camp for some time, I have only uncovered some of why that might be."
    show ylva closedsad at right
    show sabiaemo normal at left
    ylva "When Warchief Groknak was solidifying his control of the region, attempting to maintain neutrality with Lundar, some bands of orcs resisted. Many were brought under control with politics, negotiation, or formal challenges of combat."
    show sabiaemo irritated2 at left
    ylva "But one resisted. And though the warriors will not speak of it... I believe they were killed, their bodies dumped into the lake."
    show ylva sad at right
    ylva "Normally the shamans should have made amends for this act and placated the Lakelord. But either they didn't know or they chose to do nothing. And now the lake is dying."
    show sabiaemo closed2 at left
    s "I... see..."
    show ylva normal at right
    ylva "You don't want to assist me in this?"
    show sabiaemo normal at left
    s "No, it's just, the whole story... oh, never mind. What is it that you actually want to do?"
    show ylva angry1 at right
    ylva "Don't dismiss the issue like that. If you're going to act like that, you don't have to force yourself to help."
    show sabiaemo irritated1 at left
    s "Look, I'm willing to help you. But don't go talking to me about the Lakelord and all that."
    show ylva closedangry at right
    ylva "I'm not forcing you to believe in our traditions, I just-"
    show sabiaemo irritated2 at left
    s "You're going on about the lake dying because the Lakelord is unhappy instead of, oh, having a bunch of corpses dumped into it? Don't be stupid."
    show ylva angry1 at right
    ylva "Stupid? The gods are a natural way to talk about the real world... don't pretend it's more ridiculous than all the Order of Relona's abstract theology."
    show sabiaemo angry1 at left
    s "Are we really going to do this? Because I might not defend everything Relonan, but if you're going t-"
    show kia pawtiltconfused at center with dissolve
    kia "Why loud?"
    show sabiaemo normal at left
    show ylva normal at right
    "Both of them stopped, turning to find Kia watching them curiously. She shifted forward in between them, looking back and forth between Sabia and Ylva."
    show sabiaemo closed2 at left
    s "That's... uh..."
    show ylva normal at right
    ylva "Sabia and Ylva... do not believe the same things."
    show kia tilt1 at center with dissolve
    kia "Bee-leev?"
    show sabiaemo irritated2 at left
    s "How the hell do we explain that?"
    show ylva closednormal at right
    ylva "It's like we have... different packs. I follow the gods, like the Lakelord. Sabia follows Relona."
    show kia pawuncertain1 at center with dissolve
    kia "Lakelord who? Relona who?"
    show ylva normal at right
    show sabiaemo normal at left
    "The two of them glanced at each other and gave an awkward half-shrug. Sabia realized that her anger had dissipated and was frustrated with herself for rising to the bait. It wasn't worth arguing over something like that, not with Ylva."
    show ylva opennormal at right
    ylva "They're gods, Kia. It's hard to explain, but they're much bigger than us."
    show kia pawtilteager2 at center with dissolve
    kia "Big big food?"
    show ylva openclosed1 at right
    ylva "Not literally big. And they're not food. It's about ideas. They're not here, but they still influence ou-"
    show kia happy2 at center with dissolve
    show ylva surprised at right
    "Ylva was cut off when Kia licked her face. The Makhor put a paw on each of their shoulders and looked between them."
    show ylva normal at right
    kia "They not here. Ylva here. Sabia here. Sit! Sit happy!"
    show kia happy1 at center
    "Kia seemed extremely serious about this, and after a moment Sabia found herself smiling."
    show sabiaemo happy2 at left
    s "She does have a point."
    show ylva happy1 at right
    ylva "Heh, I suppose so... I'm sorry, Sabia. I was pushing you on if you'd take orc beliefs seriously and I let it get out of hand."
    show sabiaemo closed3 at left
    s "It's fine. We're not going to agree on everything, but we shouldn't be at each other's throats."
    show kia happy2 at center
    "Kia sat back on her haunches and looked between them, rumbling approvingly."
    show sabiaemo normal at left
    s "Alright, what did you want to ask my help for?"
    show ylva normal at right
    ylva "I want to do some rituals to purify the lake, but I'm not asking for your help with anything religious. The problem is that there are several groups occupying the lake that might stop me."
    "Ylva unrolled a small map she'd been carrying and pointed to three points around the lake."
    show ylva opennormal at right
    ylva "First, there's a group of Groknak's orcs on the southern side. They've just taken the lake as their camp, but they aren't religious enough to leave when I asked."
    show ylva normal at right
    ylva "Second, there's a group of humans to the northwest. Obviously I didn't approach them, but I think they're some kind of scouting party."
    show ylva openclosed2 at right
    ylva "And finally, in the northeast there's a small group of unaffiliated orc bandits. They just use the lake as a base when not attacking."
    show sabiaemo closed1 at left
    s "So you want me to make them go away, huh?"
    show ylva normal at right
    ylva "Essentially. I hope the local orcs would listen to you, and maybe you can negotiate with the humans. The bandits, I'm afraid we'll need to kill."
    show sabiaemo normal at left
    s "I understand. I may be able to take them out."
    show kia tilt1 at center with dissolve
    kia "Bad things?"
    "Kia shifted closer to them, pointing out to the lake."
    show kia pawtilteager2 at center with dissolve
    kia "Ylva not like? Want Kia eat bad things?"
    show ylva happy2 at right
    ylva "Uh... thank you, Kia, but maybe not. No eat, no kill."
    show kia tilt2 at center with dissolve
    "Kia sat back and considered this bit of insanity, then glanced toward Sabia."
    show kia pawtilteager1 at center with dissolve
    kia "Sabia help Ylva."
    show ylva normal at right
    ylva "I would appreciate your help, Sabia. But you're not obligated. If you don't want to do this, just tell me - better that than promising and not following up."
    "It did sound like a lot of trouble for a superstition, but Sabia also didn't want to antagonize her allies..."
    menu:
        "Offer to help":
            $ SUlakequest = 3
            show sabiaemo happy1 at left
            s "Of course I'll help! I can't resolve everything right away, but I'll see what I can do."
            show ylva happy1 at right
            ylva "Thank you. I'm not in a hurry, but I hope I can purify the lake before politics pull me away."
            show sabiaemo normal at left
            s "I suppose I should get star-"
            show kia happy2 at center with dissolve
            kia "Sit!"
            "The insistent Makhor made sure that Sabia did not get started any time soon. The time between them passed smoothly, but when Sabia finally returned to camp she found herself with yet more tasks to complete."
        "Decline to help":
            show sabiaemo closed2 at left
            s "I'm sorry, but I don't know if I'll be able to do it."
            show ylva closednormal at right
            ylva "...thank you for your honesty. I'll see what I can do on my own."
            "That soured the mood a little, but Ylva honestly didn't seem to hold it against her. Kia was confused by the change, so they only sat together for a short time before they headed their separate ways."
    return

label SUylvalake3:
    scene bg orclake
    call sabiabase
    with dissolve
    "Sabia headed out to find the group of local orcs, not sure exactly what she'd find. They were a part of Groknak's warband, so presumably it might be possible to get through to them, but they hadn't listened to Ylva."
    "There could be a lot of reasons for that. It might be because she was a woman, in which case Sabia would do no better. She hoped that it was antipathy toward shamans. Or they might just be stubborn bastards."
    "They didn't seem that way when she got close enough to see them. They were just lounging beside the lake, drinking and talking. Just the kind of laziness she would have expected from orcs, before she'd ended up here."
    show orcbase2 at right
    show orcloincloth2 at right
    show orcstomach2 at right
    show orcemo2 normal at right
    with dissolve
    "Sabia headed up to one of the orcs that was standing guard and didn't seem drunk."
    show sabiaemo irritated2 at left
    s "Why does the Warchief have you on assignment all the way out here?"
    if L_orcs >= 50:
        show orcemo2 normalopen at right
        "The orc seemed startled to see her and actually stood up a little straighter before answering. It wasn't respect like she'd expect in a human army, but it was a lot better than she'd expected."
        orc "Sorry, Sabia... we just wanted to get away for a bit..."
        show sabiaemo happy1 at left
        s "And I don't blame you, but I need this area clear for my exercises."
        show orcemo2 normal at right
        "The orcs grumbled a little, but good-naturedly, and they did start to pack up their things. Sabia hadn't expected things to go so well and wasn't sure if they would stick..."
        menu:
            "Just let them go":
                "Deciding not to push her luck, Sabia just let them go at their own rate. But to her surprise, one of the orcs approached her with a gleam in his eyes... and not the type she'd expected."
            "Threaten to use force" if dom >= 5:
                $ dom += 1
                $ L_orcs -= 1
                show sabiaemo angry1 at left
                s "Go on, get a move on!"
                "They grumbled a little more, but did hurry up. As they did, one of the orcs approached her with a gleam in his eyes... and not the type she'd expected."
            "Flirt with them" if sub >= 5:
                $ sub += 1
                $ L_orcs -= 1
                show sabiaemo happy2 at left
                s "Come on, boys, surely you big strong warriors can go faster than that?"
                "That earned her more than a few stares, and Sabia wasn't sure it actually made them go any faster. But one of the orcs with a gleam in his eye actually didn't seem to be ogling her."
        show orcemo2 smile1 at right
        orc "You doin' this for the Warchief? Or cuz you wanna get with Ylva?"
        show sabiaemo surprised1 at left
        s "Th-that's..."
        show orcemo2 smile3 at right
        orc "Just sayin'. Female that good, we'd fuck her too if she let us..."
        show sabiaemo angry1 at left
        s "That's none of your business!"
        "The orc laughed, but moved away to work with the others. After she fought down her blush, she considered that this was probably for the best. If the warriors were treating her more like them, that meant she was getting a little real respect."
    elif L_orcs >= 20:
        show orcemo2 sad1 at right
        "Seeing her, the grunted and gave a half-shrug. Not as polite as she would have liked, but it was better than she would have expected for a human."
        show orcemo2 normalopen at right
        orc "Not assignment, just here. You gotta problem?"
        menu:
            "Persuade them":
                show sabiaemo closed2 at left
                s "The Warchief needs you back at camp. With Lundar paying more attention, we can't afford to take risks."
                show orcemo2 normal at right
                orc "Hunh. Human talking about Lundar like that?"
                show sabiaemo irritated2 at left
                s "I'm the one leading a war party. I can't have you getting my warriors hurt because you're being careless."
                if L_orcs >= 30:
                    $ L_orcs += 1
                    "To her surprise, she actually seemed to get through to them. After some argument, the orcs began to pack up. They did so in a pretty lazy way, but considering she hadn't needed to use threats, she'd take what she could get."
                else:
                    $ L_orcs -= 2
                    "The orc scoffed, and the others argued, but in the end they agreed and started packing up. Sabia caught more than a few ugly glares cast her way, but the important thing was that they were obeying."
            "Threaten to use force" if dom >= 5:
                $ dom += 1
                $ L_orcs -= 3
                show sabiaemo eyebrow1 at left
                s "You know I'm in charge of a raiding party now, right? One of our jobs is to cut down rogue orcs. It would be a shame if we... make a mistake."
                show orcemo2 angry at right
                orc "You wouldn't dare!"
                show sabiaemo closed4 at left
                s "I don' think I'll need to. You boys will do the smart thing, right?"
                show orcemo2 normal at right
                "The orc seemed taken aback, but did move away to the others. After some argument, they resentfully started packing up."
                show sabiaemo angry1 at left
                s "Go on, get a move on!"
                "They grumbled a little more, but did hurry up. Sabia left them to their work."
            "Flirt with them" if sub >= 5:
                $ sub += 1
                $ L_orcs -= 3
                show sabiaemo happy3 at left
                s "I need to use this place for a little something... surely you can do me a favor?"
                show orcemo2 smile1 at right
                orc "And what do we get for this favor?"
                show sabiaemo closed1 at left
                s "I won't forget, I'll be grateful..."
                "Though she wasn't sure if she really convinced him, the orcs didn't seem to be particularly insistent about staying. After some lazy discussion, they started to pack up. Sabia left them to their work."
    else:
        $ L_orcs -= 3
        show orcemo2 suspicious at right
        "The orc scowled in response."
        orc "Shut up, human. We don't answer to you."
        show sabiaemo surprised1 at left
        "Sabia was surprised by the amount of disrespect in his voice. Well, she wasn't going to earn it back easily, and it didn't seem like he would be open to subtle methods."
        show sabiaemo closed2 at left
        "It wasn't going to win her any friends, but she thought she had no choice but to brute force this."
        show sabiaemo eyebrow1 at left
        s "You know I'm in charge of a raiding party now, right? One of our jobs is to cut down rogue orcs. It would be a shame if we... make a mistake."
        show orcemo2 angry at right
        orc "You wouldn't dare!"
        show sabiaemo normal at left
        "Sabia just met his gaze flatly. Truthfully, she probably couldn't get away with killing them, but her troops could still rough them up. She stared as if she had ever intention to murder him in his sleep."
        show orcemo2 normalopen at right
        orc "Dammit, fine. We just wanted to get away from the camp..."
        show sabiaemo angry1 at left
        s "The Warchief needs you fighting, warrior. Get moving."
        "The orcs grumbled significantly and Sabia caught many nasty glances shot her way, but it looked as though they were actually packing up. She nodded in satisfaction and left them to it."
    show sabiaemo normal at left
    "When Sabia checked a little later, it seemed that the orcs really had left their position. Hopefully the area would stay clear."
    return

label SUylvalake4:
    scene bg orclake
    call sabiabase
    with dissolve
    "Approaching the group of humans was going to be the trickiest issue overall, so Sabia scouted them first. It seemed to be a small group of armored soldiers, likely from a local province."
    "Attacking them in force would only bring a lot of attacks down on their heads, so she needed to do this alone. Sabia tried to consider if she was ready..."
    menu:
        "Come back later":
            return
        "Approach them":
            $ SUlakequest += 1
            $ SUlakehumans = True
    "Taking a deep breath, Sabia headed out to meet the human band. Strange that she should be so nervous to meet humans after so long with orcs, but given the potential politics involved, they could actually be more dangerous."
    show humansoldier normal at right with moveinright
    "The soldiers were not lazing around - they quickly spotted her and sent someone out to intercept. Sabia didn't exactly stand down, but raised her hands to show she intended no threat."
    show humansoldier angry at right
    soldier "Who the hell are you?"
    s "I-"
    $ temp1 = 0
    if Sabia.armor == Rags:
        $ temp1 -= 1
        soldier "And what the hell are you wearing? Did you survive some kind of attack?"
        show sabiaemo closed2 at left
        s "Something like that."
    if Sabia.armor == Leatherarmor:
        $ temp1 += 1
    if Sabia.armor == Heavyleatherarmor:
        $ temp1 += 2
    if Sabia.armor == Orcslavearmor:
        $ temp1 -= 2
        soldier "And what the hell are you wearing? Are you some kind of slave?"
        show sabiaemo irritated1 at left
        s "I wore what I had, alright?"
    if Sabia.armor == Barmaidclothes:
        $ temp1 += 1
    show humansoldier normal at right
    soldier "We're on an official mission from Whitecrest. Whatever local trouble you have, we're not interested."
    show sabiaemo normal at left
    "If they were from Whitecrest, that meant they were Governor Andian's men. Not someone she could get much information from, and definitely not someone she could trust. Best just to get them out of her way as quickly as possible."
    show sabiaemo happy1 at left
    s "I'm not here to interfere with your mission. But we need to talk."
    soldier "You'd better tell us exactly why you're here. Lone women don't travel this far into orc lands for no reason."
    show sabiaemo closed4 at left
    s "No kidding. After so long among brutes, this is the kind of reception I get from fellow humans?"
    show sabiaemo irritated1 at left
    "Immediately she found herself second-guessing the way she'd chosen to say that. Did \"fellow humans\" sound unnatural? Her sense for such things was a little skewed after so long in the orc camp, but it was too late to change it now."
    if L_humans >= 25:
        $ temp1 += 3
        show humansoldier sad at right
        "To her surprise, it seemed to work. The soldiers mostly looked sympathetic or respectful... but they were still very cautious."
    elif L_humans >= 15:
        $ temp1 += 1
        show humansoldier normal at right
        "Her words seemed to reach the soldiers, at least. She saw a few who looked uncertain, but others seemed more inclined to try to protect her and at least a few looked respectful."
    else:
        $ temp1 -= 1
        show humansoldier angry at right
        "The soldiers glanced at each other and she saw deep suspicion in their eyes. Damn, then she hadn't been able to win them over."
    soldier "Before you say any more, state your business."
    show sabiaemo closed2 at left
    s "(Whatever my story, it needs to be something that convinces them to leave...)"
    menu:
        "You're antagonizing the orcs":
            $ temp1 += 1
            show sabiaemo normal at left
            show humansoldier surprised at right
            soldier "What does that mean? You live in one of the nearby villages?"
            s "The orcs don't raid too often, normally. But heavily armed soldiers like you... we're going to be the ones suffering for it."
            show humansoldier normal at right
            soldier "We don't want to harm your communities, lady, but we do have a mission..."
        "The orcs are massing, you're not safe here":
            show sabiaemo normal at left
            show humansoldier surprised at right
            soldier "What, they're planning an attack?"
            show sabiaemo closed2 at left
            s "I don't know, but there are a lot more of them. A group as small as yours isn't safe."
            show humansoldier angry at right
            soldier "I think we know what we're doing, woman."
        "I'm an agent of Lundar":
            $ temp1 += 2
            show sabiaemo normal at left
            show humansoldier surprised at right
            soldier "What?"
            show sabiaemo closed2 at left
            s "You heard me. Lundar sent me into this region as a scout."
            show humansoldier normal at right
            soldier "Our governor hasn't bowed to Lundar yet... you don't have any authority over us."
            show sabiaemo closed4 at left
            s "I don't give a shit about that. But by fooling around here, you're getting in my way."
    show humansoldier normal at right
    show sabiaemo normal at left
    "The soldier glanced back to the other men, particularly one of them with a more ornate outfit. The commander of the group, most likely."
    if temp1 >= 7:
        $ L_humans += 3
        $ Sabia.xp += 5
        $ SUhumansconvince = True
        "To her surprise, the commander smiled and nodded at her. He also made a military signal with one hand, but it didn't seem to be an attacking signal. The soldiers all relaxed somewhat, and the one nearest to her nodded."
        show humansoldier happy at right
        soldier "Sorry about that, milady. We're all just on edge due to the mess with the provinces."
        "She didn't know what he meant by that, but couldn't seem ignorant, so nodded."
        show sabiaemo happy1 at left
        s "I understand. I just didn't want you to be in unnecessary danger."
        show humansoldier normal at right
        soldier "We appreciate that. But would you be willing to give us some more intelligence on the region?"
        show sabiaemo normal at left
        "He wasn't demanding, so she had options. It would seem suspicious to delay too long, so she had to make a decision quickly..."
        menu:
            "Say you don't know enough details":
                $ L_orcs += 1
                show sabiaemo closed2 at left
                s "I'm sorry, but I haven't gone far enough to know more than you do."
                "A few of them seemed a little suspicious about that, but after some conversation between the commander and the others, they seemed to believe her."
                "So as to avoid seeming suspicious, Sabia stayed with them a little longer, pretending to be glad to meet fellow humans. Hopefully that would be a good enough pretext."
            "Feed them lies":
                $ L_orcs += 3
                $ L_humans -= 1
                show sabiaemo normal at left
                "Sabia hesitated only a moment before she began weaving believable lies. She was concerned that it might be just a test, so didn't say anything too outlandish, but they seemed to actually want the information."
                "The positions she gave them would leave the governor unprepared to deal with the local orcs if he tried to act, which probably served her best interests. She also tried to tell them things that soldiers would want to hear."
            "Tell them the truth":
                $ L_orcs -= 1
                $ L_humans += 3
                show sabiaemo normal at left
                "Sabia hesitated only a moment before deciding to tell them the truth. They might be able to check her answer, plus she had no loyalty to the orcs."
        "Fortunately, it seemed to have the intended effect. After she spoke with the soldiers for a while, they seemed pleased with what she had told them. They also agreed to retreat from the lake and didn't push her too hard on other details."
        "Sabia watched them secretly, but they kept their word. After cleaning up their camp, they relocated further away from the lake... that was good enough for her."
    elif temp1 >= 5:
        $ L_humans += 2
        $ Sabia.xp += 2
        "The commander made a gesture that Sabia wasn't sure the meaning of, but the soldier nodded. Fortunately, he also took his hand off his blade."
        show humansoldier normal at right
        soldier "We're grateful to you for your warning. But we'd like some more information from you - how much do you know about the local orc positions?"
        menu:
            "Say you don't know enough details":
                show sabiaemo closed2 at left
                s "I'm sorry, but I haven't gone far enough to know more than you do."
                "A few of them seemed a little suspicious about that, but after some conversation between the commander and the others, they seemed to believe her."
                "So as to avoid seeming suspicious, Sabia stayed with them a little longer, pretending to be glad to meet fellow humans. Hopefully that would be a good enough pretext."
            "Feed them lies":
                $ L_orcs += 3
                $ L_humans -= 3
                show sabiaemo normal at left
                "Sabia hesitated only a moment before she began weaving believable lies. She was concerned that it might be just a test, so didn't say anything too outlandish, but they seemed to actually want the information."
                "The positions she gave them would leave the governor unprepared to deal with the local orcs if he tried to act, which probably served her best interests. She also tried to tell them things that soldiers would want to hear."
            "Tell them the truth":
                $ L_orcs -= 3
                $ L_humans += 3
                show sabiaemo normal at left
                "Sabia hesitated only a moment before deciding to tell them the truth. They might be able to check her answer, plus she had no loyalty to the orcs."
        "Fortunately, it seemed to have the intended effect. After she spoke with the soldiers for a while, they seemed pleased with what she had told them. They also agreed to retreat from the lake and didn't push her too hard on other details."
        "Sabia watched them secretly, but they kept their word. After cleaning up their camp, they relocated further away from the lake... that was good enough for her."
    elif temp1 >= 3:
        $ L_humans += 1
        "The commander made a gesture that Sabia wasn't sure the meaning of, but the soldier nodded. Fortunately, he also took his hand off his blade."
        show humansoldier normal at right
        show sabiaemo normal at left
        soldier "We're grateful to you for your warning. But we'd like some more information from you - how much do you know about the local orc positions?"
        menu:
            "Feed them lies":
                $ L_orcs += 3
                $ L_humans -= 3
                "Sabia hesitated only a moment before she began weaving believable lies. She was concerned that it might be just a test, so didn't say anything too outlandish, but they seemed to actually want the information."
                "The positions she gave them would leave the governor unprepared to deal with the local orcs if he tried to act, which probably served her best interests. She also tried to tell them things that soldiers would want to hear."
            "Tell them the truth":
                $ L_orcs -= 3
                $ L_humans += 3
                "Sabia hesitated only a moment before deciding to tell them the truth. They might be able to check her answer, plus she had no loyalty to the orcs."
        "Fortunately, it seemed to have the intended effect. After she spoke with the soldiers for a while, they seemed pleased with what she had told them. They also agreed to retreat from the lake and didn't push her too hard on other details."
        "Sabia watched them secretly, but they kept their word. After cleaning up their camp, they relocated further away from the lake... that was good enough for her."
    else:
        $ L_humans -= 1
        show humansoldier angry at right
        "The commander made a curt gesture... close enough to Lundar's hand signals that Sabia could guess what it meant. The soldier advanced on her and she struck before he could put a hand on his weapon."
        $ enemy_level = 6
        $ enemy_maxhp = 500
        $ enemy_hp = enemy_maxhp
        $ enemy_type = 1
        $ enemy_skills = [Enemyattack]
        $ enemy_attack = 70
        $ enemy_defense = 20
        $ enemy_magdefense = 0
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
        hide humansoldier angry at right with dissolve
        "The soldier dropped, bleeding but not dead. Sabia held her weapon ready but pointedly didn't finish him off. That would have been her only chance, as the other soldiers were advancing around her, but she didn't want to make this worse than it already was."
        show sabiaemo angry1 at left
        s "I came here to try to help you, and this is how I'm treated?"
        soldier "We need to ask you some more questions..."
        show sabiaemo irritated2 at left
        "Sabia acted like she was about to answer, then abruptly broke through their circle before it could completely close. She heard the soldiers coming after her, surprisingly fast in their heavy armor, and stayed moving slow enough for them to keep after her."
        scene bg countryside with dissolve
        "Only after she had led them far from their camp did she finally lose them in a cluster of trees that looked like it was isolated but actually connected to a larger forest area. She kept watch for some time after that."
        "The soldiers searched for her for a while, then sent a few back to camp. But those only secured their supplies, then went to join the others, still searching for her."
        "It was a bad solution, but it had worked. Whatever the soldiers had been concerned about at the lake, they were now pursuing her in the wrong direction."
    return

label SUylvalake5:
    scene bg orclake
    call sabiabase
    with dissolve
    "Sabia scouted the bandit group and discovered it to be of a frustrating size. It seemed to be a few outcast warriors, not terribly organized or successful as bandits. Nothing like the organized groups that she'd come to expect."
    "But that was a mystery for another time. For now, her problem was that a group this small couldn't be raided. With no plunder of any kind, her troops would demand payment that she didn't have. And it would be a waste of resources to bring so many to bear against a small group."
    "But conversely, there were more of them than she could just take on by herself. Just when Sabia was starting to think she didn't have an easy way through this, she heard a quiet voice."
    kia "Hunt."
    show kia happy3x at center
    show ylva normal at right
    show ylva2 arm2 at right
    with dissolve
    "Sabia turned and found Kia behind her... and Ylva as well, both silent and low to the ground. Despite the situation, Sabia smiled."
    show sabiaemo happy1 at left
    s "I thought you sent me to do this."
    show ylva happy1 at right
    ylva "I appreciate that you've been sincerely trying to help. Let's see if we can't do this cleanly."
    show sabiaemo closed1 at left
    s "Well, with your help, we have more options."
    show kia pawtilteager2x at center with dissolve
    kia "Kia eat?"
    show sabiaemo normal at left
    s "You shouldn't have to do everything, Kia... let me go first and serve as a distraction. Then you can hit them from behind."
    show kia tilt1 at center with dissolve
    "Kia cocked her head in confusion, and the plan took more explaining than Sabia had expected."
    scene bg orclake
    call sabiabase
    with dissolve
    "But in the end, she strode toward the camp on her own, fairly confident that the Makhor understood. It wasn't a hard plan, and if all went well then she shouldn't have any problems."
    "When she got close, two orcs laughed and moved toward her. They didn't even try to talk to her, just reached out with grasping hands."
    "Sabia severed the first's arm at the wrist and he fell back, roaring in pain. The second immediately became more alert, drew his axe, and the battle was on."

    show orcbase at right
    show orcloincloth at right
    show orcaxe at right
    show orcstomach at right
    show orcemo angry at right
    with moveinright
    $ enemy_level = 6
    $ enemy_maxhp = 400
    $ enemy_hp = enemy_maxhp
    $ enemy_type = 1
    $ enemy_skills = [Enemyattack,Enemyquickattack,Enemyquickattack]
    $ enemy_attack = 65
    $ enemy_defense = 0
    $ enemy_magdefense = 0
    $ GenericOrc1.face = "angry"
    $ GenericOrc1.extras = ["Loincloth", "Stomach", "Axe"]
    $ player = Sabia
    $ enemy = GenericOrc1
    call duel
    if _return == "Victory":
        "Sabia shoved aside the corpse, but there was already another orc charging at her..."
    else:
        show gameover with dissolve
        pause 3
        $ renpy.full_restart()
    scene bg orclake
    call sabiabase
    with dissolve
    show orcbase at right
    show orcloincloth at right
    show orcaxe at right
    show orcnecklace at right
    show orcemo angry at right
    with moveinright
    $ enemy_level = 6
    $ enemy_maxhp = 400
    $ enemy_hp = enemy_maxhp
    $ enemy_type = 1
    $ enemy_skills = [Enemyattack,Enemyquickattack,Enemyquickattack]
    $ enemy_attack = 70
    $ enemy_defense = 0
    $ enemy_magdefense = 0
    $ GenericOrc1.face = "angry"
    $ GenericOrc1.extras = ["Loincloth", "Necklace", "Axe"]
    $ player = Sabia
    $ enemy = GenericOrc1
    call duel
    if _return == "Victory":
        pass
    else:
        show gameover with dissolve
        pause 3
        $ renpy.full_restart()

    scene bg orclake
    call sabiabase
    with dissolve
    "Though Sabia had been constantly on alert for more bandits attacking her from the sides, no one interfered with her fights. When she dropped her last opponent and looked up, she discovered why."
    "Her gaze was first drawn to the orc running screaming away, Kia in hot pursuit. She seemed to be running slower than her full speed, intentionally running the orc ragged while gleefully snapping at his heels."
    show ylva angry1 at right
    show ylva2 arm2 at right
    "Looking away, Sabia instead focused on Ylva... and found that the young shaman didn't need her help. She had said she had a warrior's rank, but Sabia hadn't reflected on what that meant."
    "The blows Ylva dealt with her staff looked painful, but didn't take down the orcs right away. But none of their blows had a chance of touching her. Her staff caught every blow except the ones she let pass - those she easily deflected with the buckler strapped to her other arm, freeing her staff to land another blow."
    "By the time Sabia got close, Ylva had beaten down the remaining orc bandits. She stood back, taking deep breaths but far from exhausted."
    show sabiaemo happy1 at left
    s "Not bad, Ylva!"
    show ylva closedhappy at right
    ylva "I try to keep up my combat skills as well."
    show sabiaemo normal at left
    s "Do we need to be worried about any escaping?"
    show sabiaemo surprised1 at left
    show ylva surprised at right
    "Both of them heard a scream that ended in a loud crunch. Sabia just shook her head."
    show sabiaemo happy2 at left
    show ylva happy1 at right
    s "Never mind, I shouldn't have asked. Should we clean up these bodies now?"
    show ylva normal at right
    ylva "A quick grave should be fine, if it's not too close to the lake."
    "They worked together to dispose of the bandits, even Kia helping once she understood that they were intending to dig. It was done surprisingly quickly, so Sabia headed back to camp nursing her minor bruises and cuts."
    "Still, she felt good about the encounter. She wasn't wasting her time on errands, she was investing more in an alliance that could be very useful to her. She needed to make time to finish Ylva's task, regardless of the value of purifying the lake."
    return

label SUylvalake6:
    $ A_ylva += 5
    $ SUlakequest = 7
    scene bg orclake
    call sabiabase
    with dissolve
    "When Sabia went to tell Ylva that all the problems around the lake had been resolved, she didn't find the female shaman anywhere. Puzzled, Sabia headed out of camp instead, wondering if one of the groups had come back."
    "Well, that was obviously not true of the bandits, but she could see it happening with either of the others."
    show ylva closednormal at right
    show ylva2 arm2 at right
    "But as she started to circle the lake, she spotted Ylva and realized that wasn't the case. The other woman knelt in the shallow water, either meditating or praying. It was certainly no brutish ritual."
    "Deciding to keep her thoughts to herself, Sabia simply moved a reasonable distance away and waited patiently. Eventually Ylva finished her ritual and rose to face her, already smiling."
    show ylva happy1 at right
    ylva "I suppose I should have thanked you for all your work first, Sabia. But with the lake clear, I wanted to begin right away."
    show sabiaemo closed1 at left
    s "Are you finished? Is, uh, the Lakelord happy now?"
    show ylva closedhappy at right
    ylva "It isn't that simple a process. I will be returning here many times over the coming days, both praying to the gods and monitoring the lake."
    show ylva happy2 at right
    ylva "But thanks to your work, I do not predict any problems. Thank you, Sabia."
    show sabiaemo normal at left
    s "You're welcome. It wasn't too hard, in the end."
    show ylva happy1 at right
    ylva "If you ever need a place to rest away from camp, feel free to stop by."
    show sabiaemo happy1 at left
    s "Thank you, I'll keep that in mind."
    "Sabia stayed for a while after that, though with Ylva returning to her rituals it felt a little uncomfortable. But the lake {i}was{/i} both peaceful and beautiful. She could see herself relaxing here, if she didn't need to be working all the time."
    "Eventually she turned to go, but she thought about the lakeside as she left. It wasn't possible to work constantly, maybe she could spend a little time there in the future..."
    return

label SUylvalake7:
    $ SUlakequest = 8
    scene bg orclake
    call sabiabase
    with dissolve
    "Sabia headed out to the lake, thinking that maybe she could chat with Ylva after her rituals. But for once, the shaman wasn't at her usual place."
    "Wondering if she wouldn't be by soon, Sabia found a comfortable place and lay back on the grass, where she could look over the lake. It really was a nice view."
    "And the grass was {i}much{/i} softer than it had looked. Or maybe that was just her tiredness talking. Sabia found herself settling back more and more, letting her eyes droop closed..."
    scene bg black with dissolve
    pause 1
    scene bg orclake
    "Sabia came awake slowly to the sound of voices. For a panicked instant she cursed herself for not snapping to alertness earlier, but then realized why she hadn't panicked."
    show ylva normal at left
    show ylva2 arm2 at left
    show kia happy1 at right
    with dissolve
    "The voices she heard were Ylva and Kia. Though Sabia considered going straight out to meet them, she still felt very loose and relaxed in her position on the grass. She yawned and sat up slowly."
    "By then, she had started to hear their voices more clearly. Sabia looked more cautiously and found them in a grassy area below, a short distance away from the shore. Kia was sitting, impatiently waiting for Ylva to finish her ritual."
    show ylva2 arm1 at left
    with dissolve
    show kia happy2 at right
    "When Ylva finally rose and set her staff aside, Kia's ears perked up eagerly."
    kia "Ylva sit?"
    show ylva happy1 at left
    "Ylva smiled and nodded, but it seemed this time Kia meant actually sitting. Kia grabbed her with both paws and pulled her down onto the soft grass, which Ylva took gracefully enough. Soon Kia was rumbling happily and rubbing against Ylva."
    show kia happy2E at right
    kia "Kia likes Ylva."
    show ylva happy2 at left
    ylva "Ylva likes you too, Kia."
    "That prompted a much louder rumble and Kia began nuzzling against Ylva's neck. That made the spines on her head shift quite close to Ylva's face, but the orc seemed concerned for only a moment before she put a hand in Kia's mane of hair."
    show kia happy1E at right
    kia "Ylva want mate?"
    show ylva openclosed1 at left
    ylva "Kia... do Makhor have mates? Or do they just have sex?"
    show kia pawtiltcurious at right with dissolve
    "Kia pulled back, cocking her head and considering this question."
    kia "Mates? {i}Fsskit{/i} mate?"
    show ylva openclosed3 at left
    ylva "I'm not sure, honestly. I'm sorry, that may have been a difficult concept."
    show kia tilt1 at right with dissolve
    kia "..."
    show kia normal1 at right with dissolve
    kia "Makhor are... not many. Even... back. Many many days."
    show ylva normal at left
    ylva "In the past? Yes, Ylva has heard that Makhor were never common."
    show kia happy1 at right
    kia "Is good. Walk far, hunt freely. Food has packs, Makhor not have packs."
    show kia happy2 at right
    kia "But {i}fsskit{/i} good! After many days, see {i}fsskit{/i}. Sit, talk, hunt. Maybe mate."
    show kia happy2E at right
    kia "Walk is good, but {i}fsskit{/i} is happiness."
    show ylva closedhappy at left
    ylva "Ylva thinks she understands a little."
    show kia happy2 at right
    kia "Sometimes special {i}fsskit{/i}. Walk together sometimes. Make nests. Make small Makhor."
    show ylva happy1 at left
    ylva "So you do have mates. At least that's how it sounds."
    "Kia rumbled agreement, but then shifted back with a concerned expression."
    show kia pawuncertain1 at right with dissolve
    kia "Orcs not like this. Ylva have pack."
    show ylva normal at left
    ylva "That's true. Are you saying that's a problem?"
    show kia pawtiltcurious at right with dissolve
    kia "Not. Kia want understand. This not Ylva pack... why leave pack?"
    show ylva openclosed3 at left
    ylva "Oh. That's... difficult to explain. Ylva is still young, still small. It's necessary to complete a journey, to see the world."
    show kia happy1 at right with dissolve
    kia "Walk good. Small Makhor walk with {i}fsskit{/i} until big."
    show ylva normal at left
    ylva "It's something like that, yes. Ylva has gained considerable rank, but... I need more to get what I want."
    show ylva surprised at left
    "Ylva paused as if surprised by her words, then shook her head slightly. Meanwhile, Kia considered her thoughtfully."
    show ylva normal at left
    show kia pawtiltsorry at right with dissolve
    kia "Ylva like tribe?"
    show ylva surprised at left
    ylva "What? Of course Ylva does."
    show kia pawtiltconfused at right
    "Kia did not answer, just rumbled as if uncertain. After a pause, Ylva frowned and closed her eyes."
    show ylva closedangry at left
    ylva "Not everything is perfect. Ylva tried to tell you about Lundar."
    show kia tiltirritated at right with dissolve
    kia "Bad!"
    show ylva sad at left
    ylva "That's not what... well, it is true in a sense. It makes everything more difficult."
    show ylva closedsad at left
    ylva "It was difficult for Ylva to get everything she wanted. It sounds like all Makhor are equal, but for us..."
    show kia pawtiltcurious at right with dissolve
    kia "Eee-kwal?"
    show ylva normal at left
    ylva "That's hard to explain. Everyone walks together? Anyone can be {i}fsskit{/i}? Big Makhor and small Makhor are all Makhor."
    show kia pawtiltconfused at right
    kia "..."
    show ylva sad at left
    ylva "Maybe that didn't get through to you. Well, it's not the same for orcs. There are too many complications, both from inside and from outside."
    show kia neutralE at right with dissolve
    kia "Not let Ylva hunt?"
    show kia irritated2 at right
    "Kia paused and gave a low growl of frustration."
    show kia irritated1 at right
    kia "Not hunt. Kia mean... do Ylva things. Not let Ylva do Ylva hunting?"
    show ylva happy1 at left
    ylva "That... may be right. Perhaps you do understand."
    show kia happy1 at right
    kia "But Kia good. Kia should walk freely, should hunt, should mate."
    "Kia pulled Ylva closer and began stroking her possessively, as if she could protect her that way. Ylva gave an odd smile and relaxed against the Makhor."
    show ylva happy2 at left
    ylva "Thank you, Kia."
    show kia normal1 at right
    kia "Kia think tribe bad. Ylva say good, but not."
    show ylva closedsad at left
    ylva "That's not true. There was a man, a great shaman... he took me in when Ylva had nothing. He's like a father to me."
    show ylva sad at left
    ylva "But for politics... they always get in the way. Everyone wants to do what's right, even if it's hard. But when you disagree about what's right..."
    show kia pawtiltconfused at right with dissolve
    kia "..."
    show kia pawtilteager2 at right
    kia "Ylva should be free. Walk with Kia. Be happy."
    show ylva happy1 at left
    ylva "That's... that sounds nice, Kia. It really does."
    show ylva closedhappy at left
    ylva "Ylva is afraid it's more difficult than that. My pack is my pack, even if it isn't perfect."
    show ylva happy1 at left
    ylva "But... Ylva would like to be happy with you, Kia."
    show kia happy1E at right
    show kia2 blush1 at right
    with dissolve
    "Kia rumbled much louder and began rubbing herself against Ylva more aggressively. Ylva didn't pull away this time, and eventually bit back a moan from the rubbing."
    kia "Ylva wants Kia change?"
    menu:
        "Kia points to her crotch."
        "Ask Kia to change":
            call SUkiaylvasexF
        "Ask her to stay like she is":
            call SUkiaylvasexY
    scene bg orclake
    call sabiabase
    show sabiaemo closed2 at left
    show sabiaemo2 blush at left
    with dissolve
    "Sabia had looked much longer than she had intended and now found herself blushing and trapped in place. She could try to creep away, but the chance that they would notice her was too high, and then she'd have a very awkward conversation."
    "Instead, Sabia stayed where she was and tried not to hear the soft noises from the two of them. She wasn't able to get back to sleep."
    "When they finally left, Sabia got up, aching from so long lying on the ground. She headed back to camp, trying not to think too much about what she'd seen."
    return

label orcsquadtraining:
    scene bg countryside
    call sabiabase
    with dissolve
    "Though Sabia had to admit that the orcs did more training than she would have thought, it was nothing like the drilling that a proper army needed. They might be able to do well enough in a brawl, but if they needed to follow commands... well, all her plans would shatter as soon as they met the enemy."
    "It was hard enough to maintain strategy just due to the chaos of battle, so Sabia began scheduling more training sessions. The orcs were willing to come... but the drills never went to her satisfaction."
    "A few of the better warriors at least seemed to care, but she couldn't fill an army with just those. Plenty of others were more what she would have expected from orcs. Lazy, constantly leering at her, not interested in power beyond individual strength. It was a mess."
    "The leering was something she'd mostly gotten used to, but there was a lot of it... enough that it really started to irritate her. Eventually Sabia called a break in training early and pulled aside one of the group leaders to talk about things."
    call sabiabase
    show orcbase at right
    show orcloincloth at right
    show orcnecklace at right
    show orcemo normal at right
    with dissolve
    if dom > sub:
        s "What's wrong with everyone? I refuse to believe this is the best I can get out of warriors from a big tribe like this."
    else:
        s "No one can focus... what am I doing wrong?"
    orc "It's hard to take orders from a human female. Especially with you dressed like that."
    show sabiaemo irritated2 at left
    s "You're saying I should dress differently? Would that really solve the problem?"
    orc "Probably not. Too much sexual tension, not enough release. Maybe it would be okay if there were females in camp."
    show sabiaemo closed2 at left
    s "Hmm. Then I need to resolve this..."
    if dom > sub:
        "What the orcs wanted was to fuck her, but that wasn't an option since it would just exacerbate the problem. No, she needed an alternative."
    else:
        "The idea of offering herself briefly occurred to her, but Sabia set it aside. That would probably lead to them focusing more on her body, which would make things worse. Fortunately, she did have a few options."
    menu:
        "Continue as normal and try to be more strict":
            $ SUorctraining = True
            $ L_orcs -= 2
            s "(Shit... I can't think of anything good.)"
            scene bg countryside
            call sabiabase
            with dissolve
            "Unable to come up with anything she felt was a truly good idea, Sabia just did her best to keep the orcs on task. They got a little better, but she felt as though she hadn't fixed the underlying problem."
        "Strategically punish orcs who misbehave" if dom >= 10:
            $ SUorctraining = True
            $ SUorcstrained = True
            show sabiaemo eyebrow1
            s "Alright, I know what I'm going to do."
            scene bg countryside
            call sabiabase
            with dissolve
            "When they began training again, Sabia proceeded as normal, but stayed closer to the orc lines and kept an eye out for an opportunity. She ignored the orcs just ogling her, waiting for someone who was really neglecting his work to leer at her."
            "Without warning, Sabia spun on him and jabbed him in the eyes with two knuckles. The orc dropped back with a roar of anger - and Sabia poked him in the stomach with her weapon hard enough to draw blood."
            show sabiaemo angry1
            s "You think I'm going to send you out to fight a bunch of weaklings? You lose focus, you die!"
            "The orcs shrank back in surprise. Sabia had been prepared to fight the orc she'd jabbed, but to her surprise he actually fell back looking a little contrite."
            show sabiaemo closed2
            s "If you can't pay attention to the battles we're fighting, then you're not warrior enough to be in this force. Do I make myself clear?"
            show sabiaemo normal
            "Though not all the orcs agreed, she saw most were nodding grudgingly and a few even looked ashamed. Sabia clapped the orc she'd hit on the shoulder."
            s "Now, let's begin again. And do it right this time!"
            "Though the ogling didn't stop, her force became substantially more focused as they continued training. Given what she had to work with, Sabia was satisfied with that."
        "Appeal to future tribal victories" if L_orcs >= 40:
            $ SUorctraining = True
            $ SUorcstrained = True
            show sabiaemo happy1
            s "Thanks for letting me know. I think I have an idea that might refocus them."
            scene bg countryside
            call sabiabase
            with dissolve
            "When they next drilled together, Sabia gave a brief speech. She wasn't much for speeches, but she knew the orcs weren't either and thought she understood them well enough to appeal directly to them."
            s "Orc leaders think too small. Living in camps with just men, capturing a few women occasionally... is that all you want? Is that what orcs deserve?"
            show sabiaemo happy1
            s "Only if you're the scum that humans think you are! Be better than that!"
            "She painted a picture for them of fighting back Lundar, being able to recover the tribe's women, capturing plenty of slaves along the way. Though she didn't emphasize the sexual aspect, she made the implication obvious and it seemed to get through even the thickest of skulls."
            "By the time she was done and they tried drilling again, the orcs were more focused. They still stared at her sometimes, but their minds were also on what proper training could give them in the future."
            "Given what she had to work with, Sabia was satisfied with that."
        "Use enslaved catgirls to motivate them" if catgirlstatus == "enslaved" and SUorcstrained == False:
            $ SUelmyprompt = True
            $ SUelmyquest = 1
            $ Aliochshop.inventory.append([Cheapfood,100,1])
            $ Aliochshop.inventory.append([HGNBeer,50,1])
            show sabiaemo eyebrow1
            s "Alright, I know what I'm going to do."
            scene bg countryside
            call sabiabase
            show sabiaemo happy2
            with dissolve
            s "You boys seem frustrated... how about we have a little contest?"
            "Her announcement immediately drew the attention of most, but she planned to sweeten the pot even more. What was the point of having slaves if she wasn't going to exploit them?"
            s "If you manage to focus today, I'll give you some of our spoils of war. Not enough catgirls to go around in the tents, right? Well, if you do good enough, I'll arrange for some exclusive use."
            "That fired up her troops immediately, though it was only a shallow motivation. Still, it was something to work on, so Sabia ran them through the paces of training."
            s "There aren't enough cats to go around, boys... you're not getting anything if you fuck up!"
            show sabiaemo eyebrow1
            s "Besides, why should soldiers who just want to fuck around be rewarded? You'd better do a damn good job if you want to earn any relief!"
            "By the time the training session was over, Sabia had hammered home the point that rewards were tied to good performance. She'd done a decent job of it... but that was just half the battle. Unless the reward for the warriors she identified as the best was actually good, her strategy wouldn't work."
            "But it wouldn't be so easy to set it up. She doubted she could do something like this in the middle of the tavern, or random orcs would get in the way. And she'd need food and alcohol to keep the orcs happy."
            "And of course, she needed to find a catgirl who would be a good target..."
    return

label SUelmypokerscene:
    $ SUorcstrained = True
    $ SUelmyquest += 1
    scene bg silvertusknight
    call sabiabase
    with dissolve
    "Once everything was set up, Sabia got half the bar reserved for her troops and set things up. To her surprise, they actually had a lot of ideas of their own of how they wanted to use Elmy."
    "They brought out some dice carved from bone and started up what seemed like a simple gambling game. Long, though, with the pot building up over multiple rounds. They didn't use Lundils, just stones... which made it fairly obvious what the prize was going to be."
    scene bg black with dissolve
    pause 3
    call SUelmypokersex
    "The night was obviously a huge success as far as her warriors were concerned, but the real question was if it would make a difference. Sabia scheduled another drilling session as soon as possible."
    scene bg countryside
    call sabiabase
    show sabiaemo happy2
    with dissolve
    "The next time, her soldiers did better. She'd been skeptical, but they actually did seem less sexually frustrated and less inclined to ogle her... though some still did."
    "This was an adequate solution, Sabia decided. Even in Lundar, there were only a few soldiers motivated by pure ideology. Most were motivated by baser desires, even just pay. But if their incentives were in the right places, they'd fight for the men at their side when it came down to it."
    "It seemed some things were true about soldiers, human or orc. Watching her soldiers drilling, Sabia began to consider future plans again. If they had to be built on the back of catgirl slaves, that didn't bother her so much."
    return

label SUhuntingorc:
    if huntingopen == True:
        pass
    else:

        if SUhuntingquest == 0:
            $ SUhuntingquest = 1
            scene bg forest
            call sabiabase
            show orcbase at right
            show orcloincloth at right
            show orcnecklace at right
            show orcbeard1 at right
            show orcwrap at right
            show orcwrists at right
            show orcaxe at right
            show orcemo normalopen at right
            with dissolve
            s "Okay, what do I need to do in order to hunt in the tribe's forest?"
            orc "Need special permission."
            if dom >= sub:
                s "Seriously? I'm not some lowly warrior, I think I can fucking hunt!"
            else:
                s "Can't you give me permission?"
            orc "Need to prove you can hunt without trouble."
            s "Okay, that's progress. What can I do to prove it to you?"
            orc "Come back later, help hunt boar."
            s "Alright, you got it."
        elif SUhuntingquest == 1:
            scene bg forest
            call sabiabase
            with dissolve
            "When Sabia arrived to help hunt the boar, it was clear that the orc intended to let her do it alone. A fearsome task, but she had a lot better equipment and training than she'd had in the past."
            "Sabia headed out cautiously, searching for signs of the boar. They quickly became obvious, as it crashed through the forest recklessly."
            if Sabia.hp >= 10:
                if Sabia.stamina >= 200:
                    $ SUhuntingquest = 2
                    $ Sabia.hp -= 5
                    $ Sabia.stamina = 0
                    "Everything about her plan was perfect - she charted the boar's crashing path, lay in wait, leapt out and dealt it a fearsome blow... and it wasn't enough."
                    "Ignoring the huge wound, the boar rammed into her. Sabia only barely managed to avoid being gored on the tusks and was still sent tumbling over the ground. It was a miracle she kept a grip on her weapon."
                    "By the time she got up, it was charging straight at her. Sabia swallowed and stood her ground."
                    "One of the tusks grazed her leg, but Sabia managed to dodge aside and slam her weapon into the beast's head. It still didn't fall, but as it stumbled away, she saw that its wounds were beginning to take their toll."
                    "She followed it, weary but satisfied. As soon as the beast dropped her hunt was over."
                    scene bg forest
                    call sabiabase
                    show orcbase at right
                    show orcloincloth at right
                    show orcnecklace at right
                    show orcbeard1 at right
                    show orcwrap at right
                    show orcwrists at right
                    show orcaxe at right
                    show orcemo normalopen at right
                    with dissolve
                    "Sabia limped back to the hunting camp, dragging the boar behind her. The orc seemed surprised, but just grunted."
                    orc "Can hunt a little."
                    s "A little? What else do I need to do to prove myself?"
                    orc "Need to be able to help other hunters. Can tend wounds? Make potions?"
                    s "...fine. I'll prove I can do that too."
                else:
                    "Sabia tried to track the boar, but her attention started to wane. When she heard it crashing through the underbrush, it was too late."
                    "All at once she was face to face with the beast, which was charging straight at her. And though Sabia had fought in battles, there was something different about a wild beast that large."
                    $ Sabia.hp -= 5
                    $ Sabia.stamina = 0
                    "She abandoned all effort to attack it and just leapt aside, then fled. She scraped herself up in the process, but managed to escape the boar. One hunt unsuccessful, but she would do better next time."
            else:
                "Sabia tried to track the boar, but her attention started to wane. When she heard it crashing through the underbrush, it was too late."
                "All at once she was face to face with the beast, which was charging straight at her. Sabia raised her weapon too late to do anything and the boar's tusks skewed through her stomach..."
                show gameover with dissolve
                pause 3
                $ renpy.full_restart()
        elif SUhuntingquest == 2:
            scene bg forest
            call sabiabase
            show orcbase at right
            show orcloincloth at right
            show orcnecklace at right
            show orcbeard1 at right
            show orcwrap at right
            show orcwrists at right
            show orcaxe at right
            show orcemo normalopen at right
            with dissolve
            if Inventory.has_item(Orchealthpotion):
                $ SUhuntingquest = 3
                s "Here you go, a health potion for orcs. Do I have permission to hunt now?"
                orc "Give potion."
                s "..."
                menu:
                    "Give him the potion":
                        $ huntingopen = True
                        $ Inventory.rem_item(Orchealthpotion)
                        s "Fine, here it is."
                        orc "Good. Alright, you can hunt now."
                        s "Finally!"
                    "Refuse" if dom >= 10:
                        $ huntingopen = True
                        s "The point was to see if I had access to potions, not to hand you one for free."
                        orc "Must test if works."
                        s "Bullshit. I've done enough for you - do I need to get Captains involved?"
                        orc "...fine, can hunt now."
                        s "Finally!"
                    "Persuade him otherwise" if sub >= 10:
                        $ huntingopen = True

                        s "Aww, but I've worked so hard... are you sure you wouldn't let me?"
                        orc "..."
                        s "I might need this potion to help you, after all..."
                        orc "...fine, can hunt now."
                        s "Finally!"
            else:
                orc "Must prove can make potions."
                s "(Guess I don't have a choice. I need a health potion specifically for orcs.)"
    return

label SUarmorquest:
    $ SUarmorsuppliesquest = True
    scene bg countryside
    call sabiabase
    with dissolve
    "While walking, Sabia was taken off guard when her foot was caught in a snare. It jerked her into the air, but on instinct she cut through the rope with her weapon."
    "As she hit the ground, Sabia shook off her surprise and got to her feet. That snare had been built for someone of human size, not an animal. Who the hell was trying to capture her?"
    show orcbase2 at right
    show orcloincloth2 at right
    show orcstrap2 at right
    show orcshoulder2 at right
    show orcaxe2 at right
    show orcemo2 normal at right
    with moveinright
    "An orc moved out of hiding, weapon at the ready."
    orc "Looks like me caught a good one!"
    s "You didn't catch anything!"
    orc "You fetch a good price!"
    $ enemy_level = 6
    $ enemy_maxhp = 400
    $ enemy_hp = enemy_maxhp
    $ enemy_type = 1
    $ enemy_skills = [Enemyattack,Enemyquickattack,Enemyquickattack]
    $ enemy_attack = 70
    $ enemy_defense = 0
    $ enemy_magdefense = 0
    $ GenericOrc2.face = "normal"
    $ GenericOrc2.extras = ["Loincloth", "Strap", "Shoulder", "Axe"]
    $ player = Sabia
    $ enemy = GenericOrc2
    call duel
    if _return == "Victory":
        scene bg countryside
        call sabiabase
        with dissolve
        $ SUarmorsupplies = True
        "Though Sabia had intended to leave him alive, she'd ended up needing to kill the orc. But still, she might be able to learn more about what he had been up to."
        "She headed into the bushes where he had been hiding and found supplies. Mostly just filthy orc food and a few hunting supplies, but there were two things of note."
        "One was a scribbled piece of paper with orc script on it, suggesting that the shamans would pay for sexually desirable human females. Well, she was reading between the lines, but the meaning seemed obvious enough."
        "Stranger was a bundle that included some finely wrought metal, a little silk, all of it making... not much of anything. It seemed like raw materials, but Sabia had no idea what purpose it was meant to serve."
        "Sabia resolved to take it back to camp, see if anyone knew what it was, or would at least be willing to pay for it."
    else:
        show gameover with dissolve
        pause 3
        $ renpy.full_restart()
    return

label SUorcsmith:
    scene bg tradinglodge
    call sabiabase
    with dissolve
    show orcbase at right
    show orcloincloth at right
    show orcaxe at right
    show orcnecklace at right
    show orcemo normal at right
    with moveinright

    orc "You need somethin'?"
    menu:





















        "Do you know what this junk is?" if SUarmorsupplies:
            "The orc looked over the mess of metal and silk, then grunted."
            orc "Raw materials for traditional orc slave outfit."
            s "I see. He was probably planning to make whoever he captured wear it to increase their value."
            orc "Not my problem. Want sell?"
            if Inventory.has_item(Orcslavearmor):
                $ SUarmorsupplies = False
                $ money += 115
                s "Would it be much different than the armor that Tekrok gave me?"
                orc "Little weaker, maybe."
                s "Then I don't need it. What is it worth to you?"
                "After a little haggling, Sabia sold the materials for 115 Lundils."
            else:
                $ SUarmorsupplies = False
                s "Would it actually be usable armor?"
                orc "Would be not bad armor overall. Also, orcs would like very much."
                s "Alright, then I guess it's an asset I should have. You already have the materials, so I trust you can finish the armor?"
                orc "25 Lundils."
                s "...fine. You'd better make it functional."
                $ money -= 25
                $ Inventory.add_item(Orcslavearmor)
                "After paying the fee, Sabia watched the smith like a hawk to see if he'd run off with both money and materials. But he actually worked to finish the armor and didn't seem to do a bad job."
                "The armor pieces had given her the vague sense of orc magic as well, which might be crude but could be effective. If it had come from the shamans, it might have value to her."
                "Sabia wasn't sure about how she felt about actually wearing armor meant to mark slaves, but she felt she'd earned a useful piece of equipment."
        "Nothing":
            pass
    return


label kentarkquestintro:
    $ kentarktraining = 10
    "When Sabia approached Lutvrog, he seemed more serious than normal... which was downright troubling on the somber orc."
    s "Everything okay, Lutvrog?"
    if orcalliance == "sabia":
        lut "Lutvrog was merely thinking that you face a very difficult path, defying the Captains and walking alone."
    else:
        lut "Lutvrog was merely thinking that you will face greater and greater challenges in the future."
    show sabiaemo closed2 at left
    s "That's true, but I'll just have to keep doing the best I can."
    lut "Lutvrog thought... perhaps you would like to attempt the Kentark training."
    show sabiaemo surprised1 at left
    s "Kentark? The same rank as you and Ylva?"
    lut "The same. Now, Lutvrog cannot give that rank - only the council of shamans may do so. But you could still benefit from undergoing the training."
    show sabiaemo happy1 at left
    s "I can try! There are some things I can't sacrifice, but if it just involves hard work, I'll do my best!"
    show lutvrogemo happy at right
    lut "Good. But the training involves many disciplines and is partially self-directed. Lutvrog can only teach the basics."
    "Lutvrog began to explain all the different skills a Kentark was expected to have, from combat and strategy to woodlore and spiritcraft. Sabia began to doubt that she really wanted to do everything necessary... but some of the skills seemed potentially useful."
    "In the end, she felt that she knew enough to pursue further training on her own. The real prize would be to return to Lutvrog when she had enough of a basis in the training to learn more."
    return


label kentarkquestscene:
    $ kentarkscenedone = True
    $ Sabia.add_con(1)
    $ Sabia.xp += 10
    $ Sabia.maxhp += 10
    $ A_lutvrog += 2
    s "Alright, Lutvrog. I think I might be ready for the first stage of Kentark training."
    lut "Indeed. Lutvrog has seen how hard you have worked."
    s "Does it involve a ritual, or...?"
    lut "While there are many religious elements, Lutrog thinks you are interested first in power."
    s "I won't deny it."
    lut "Then let us begin by moving outside of camp so we have enough space."
    scene bg countryside
    call sabiabase
    show lutvrogbase at right
    show lutvrogstick at right
    show lutvrogwraps at right
    show lutvrogwrists at right
    show lutvrogemo normal at right
    with dissolve
    "Once they were a significant difference from the camp, Lutvrog gave Sabia a potion to drink. From anyone else, Sabia would have been suspicious, but she drank it."
    "Though it tasted foul, she could feel orc magic stirring within it. And while orc shamans were inferior to mages from Lundar overall, they were pretty good when it came to bodily enhancement. Sabia swallowed to get the taste out of her mouth and focused on Lutvrog."
    lut "Now, you may only defend yourself."
    s "Wait, do you mean?"
    "Lutvrog answered by attacking, striking out with his stick. Sabia wasn't able to get her weapon up in time and the blow hit her shoulder."
    "Strangely, the feeling that spread from the blow was more pain than numbness. Sabia was taken off guard, but Lutvrog was already attacking again. She hastily moved to defend."
    "What followed was a long and desperate defense as Lutvrog rained down attacks. If they had been fighting for real, her only hope would have been to take him down before his stamina and strength could overwhelm her."
    "Like this, she took a pummeling that left her entire body numb. Yet she could feel something working within her through the pain, so she kept doing her best to defend."
    "When she struggled to block any blows, Lutvrog began to teach her specific stances and defenses in a style similar to his. Sabia nodded and did her best to learn despite the numbness."
    "Eventually the numbness wore off and the aching made her collapse. Strangely, her body didn't feel as though it would bruise, but it definitely hurt and she was exhausted."
    s "Did I mess that up?"
    lut "No, you did well. When you recover, you will find yourself slightly more durable."
    s "Thanks, Lutvrog! Just... give me some time before we have to walk anywhere."
    lut "Heh, of course."
    "She lay on her back, staring at the sky and thinking about the path that had taken her here, learning special orc techniques."
    if orcalliance == "sabia":
        $ Sabia.xp += 10
        $ Sabia.add_str(1)
        $ Sabia.maxhp += 5
        $ Sabia.maxstamina += 10
        "Before her mind could wander too far, Lutvrog urged her to her feet."
        lut "Up. If you truly plan to fight alone without a Captain to assist you, you face a very difficult path."
        "Sabia groaned but managed to get to her feet. This time he tutored her on offensive techniques, and though she never managed to break his guard once, she felt as though she at least learned a few tricks."
        "When they were done, she found Lutvrog looking at her curiously."
        lut "Lutvrog wonders... if Sabia could choose any path, what path would she want?"
        s "..."
        menu:
            "To dominate my enemies":
                $ dom += 3
                $ sub -= 1
                $ freedom -= 1
                $ slavery += 3
                lut "Hmm. A harsh path."
            "To rule over a group of allies":
                $ dom += 3
                $ sub -= 1
                $ freedom += 3
                $ slavery -= 1
                $ A_lutvrog += 1
                lut "Hmm. Strength of will attached to a noble purpose."
            "To manipulate my enemies":
                $ dom -= 1
                $ sub += 3
                $ freedom -= 1
                $ slavery += 3
                lut "Hmm. That is not Lutvrog's path, but it can be a dangerous one."
            "To serve with strong allies":
                $ dom -= 1
                $ sub += 3
                $ freedom += 3
                $ slavery -= 1
                lut "Hmm. That is not Lutvrog's path, but your goal is noble."
        "That left the conversation awkward, but before the silence could extend for long, Sabia heard something rustling in the grass nearby."
    else:
        "Before her mind could wander too far, Sabia heard something rustling in the grass nearby."
    show kia pawtilteager2 at center
    with moveinleft
    kia "Sabia Lutvrog play!"
    show sabiaemo happy1 at left
    s "Hello, Kia. Yes, we were training."
    show kia happy2 at center with dissolve
    show sabiaemo normal at left
    "The Makhor hopped up to her, sniffing all over her body. Sabia was embarrassed to have the Makhor smelling her while she was this sweaty, but Kia bared her teeth happily."
    kia "Sabia less small!"
    show sabiaemo closed1 at left
    s "Well, I'm pretty sure that's a good thing. Lutvrog was helping me."
    if lutvrogsex:
        $ A_lutvrog += 1
        kia "Lutvrog good. Lutvrog mate who?"
        lut "Lutvrog does not have a mate."
        show kia pawtiltconfused at center with dissolve
        kia "No mate?"
        show sabiaemo closed4 at left
        s "Why are you asking about this all of a sudden?"
        show kia happy1 at center with dissolve
        kia "Because Lutvrog's thing hard. Want mate."
        show sabiaemo surprised1 at left
        show sabiaemo2 blush at left
        "Sabia blushed as she realized what the Makhor meant. Not receiving a response, Kia crouched down next to Lutvrog and pointed directly at his crotch."
        kia "Want mate."
        "Sabia had been thinking entirely about their training, only occasionally admiring Lutvrog's body while they took breaks. Yet now Kia's insistence reminded her of how his cock had felt the last time. She couldn't help but imagine him hard under his loincloth the entire time..."
        "Kia began lifting his loincloth."
        kia "Lutvrog thi-"
        show sabiaemo angry1 at left
        s "I get it already!"
        show kia pawuncertain1 at center with dissolve
        "Kia looked at her, understanding that she was angry but unsure why. She started to reach toward Lutvrog's loincloth again, but he gently moved her hand aside."
        show sabiaemo closed2 at left
        lut "Sabia does not want to mate."
        show kia pawtiltcurious at center with dissolve
        kia "Why not mate? Lutvrog good. Sabia good."
        show sabiaemo normal at left
        s "It's not that simple."
        show kia normal2 at center with dissolve
        "Kia stared at her for a long time, not impressed by Sabia's logic."
        kia "Mating good."
        hide kia normal2 with moveoutright
        "With that pronouncement, she ran off into the grass again, leaving Sabia hot and bothered... and apparently Lutvrog was ready as well."
        "He started to walk back and as Sabia watched him go, she felt a stab of longing. She didn't want to let this go. She hurried up to him and put a smile on her face."
        show sabiaemo eyebrow1 at left
        s "So you were that hard up, huh? Pun intended."
        lut "Such things are natural. Lutvrog focuses his energy on training."
        show sabiaemo closed1 at left
        s "You know... if you wanted to let off some stress... you could have asked me..."
        lut "Thank you. Lutvrog will ask you the next time he wants to spar."
        show sabiaemo pout2 at left
        s "Hey! You're not that dense, are you mocking me?"
        show lutvrogemo happy at right
        show sabiaemo pout3 at left
        "She saw Lutvrog's smile and shook her head."
        s "Oh, you're going to pay for that. I'll make you wish you'd been asking me all along..."
        "As they returned to camp, Sabia prodded Lutvrog toward the room where they had had sex for the first time and he went more than willingly. The walk had done her tired muscles good, and Kia's teasing had left her with a lot of stress to work off as well..."
        call LutvrogTitfuck
        jump eastern_frontier_map
    else:
        kia "Lutvrog good."
        "Kia remained nearby and chatted with them cheerfully for some time, but little came of it. At least by the time Kia grew bored, Sabia felt much better."
        "She and Lutvrog returned to camp, Sabia immensely satisfied by her progress."
    jump traininggrounds2


label maply_hellhound_quest1:
    scene bg sabiatent
    show maply 1 at right
    show maplyemo sad1 at right
    with dissolve
    maply "...Saby?"
    maply "Saby? Are... are you awake Saby?"
    call sabiabase
    show sabiaemo irritated1 at left
    with dissolve
    s "What... what time is it?"
    "Sabia grumbled. Her eyes didn't want to open. She glanced out the half-open flaps of the tent that Maply hadn't closed, and saw the camp bathed in the silver light of the moon."
    show sabiaemo pout3 at left
    s "Maply. It's still the middle of the night, I'm still half asleep, and-"
    show maplyemo surprise2 at right
    maply "But Sabia!!"
    show maplyemo sad2 at right
    maply "They're hurting him!"
    show maplyemo sad1 at right
    show sabiaemo closed2 at left
    s "Who? What? Who is hurting who? What are you talking about Maply?"
    show sabiaemo sad1 at left
    "Sabia did her best to curb the irritability she felt at being woken in the middle of sleep."
    "Maply was clearly distraught, and the poor girl's state was only making it harder for the catgirl to get her point across."
    show maplyemo sad1 at right
    maply "Well, I wasn't sleeping because... well, I wasn't sleeping."
    show sabiaemo eyebrow1 at left
    s "And was Neve sleeping?"
    show maplyemo surprise1 at right
    maply "Neve? What do you mean Neve was-"
    show maplyblush at right
    maply "That- well, I don't... that's not important!"
    show sabiaemo sad2 at left
    "Sabia usually enjoyed her playful jabs at Maply, but the catgirl was clearly very distraught."
    show sabiaemo happy3 at left
    s "I'm sorry Maply. Take a deep breath, and tell me what the problem is. Then I can see if I can help fix it. Okay?"
    hide maplyblush
    show maplyemo eyebrows at right
    show sabiaemo sad1 at left
    maply "In the kennels, Saby! In the kennels, one of the hounds. I could hear him from outside the camp!"
    show maplyemo angry1 at right
    maply "One of the guards there - I don't know his name - but one of them was hurting one of the hounds."
    maply "I could hear his poor squeals and yelps from all the way outside!"
    show maplyemo angry2 at right
    maply "The other day, I saw him beating the poor hound."
    maply "It's not his fault! He's cooped up in a cage all day, every day! It's not right that they should hurt him for acting out."
    show maplyemo sad1 at right
    maply "Some of the Orcs aren't too bad... but they're not very good at taking proper care of animals, Saby."
    maply "You'll help me, right? We need to go make sure that the poor hound is ok!"
    show sabiaemo closed2 at left
    "Sabia was a bit annoyed at being woken up for something that Maply could have come to her about in the morning. But she could see how frantic and worried Maply was."
    show sabiaemo pout1 at left
    s "Alright, Maply. There isn't much we could do right now. It's the middle of the night still."
    s "But, tomorrow, I will see what I can do, alright?"
    show maplyemo eyebrows at right
    maply "T- tomorrow?"
    show sabiaemo closed1 at left
    s "We won't be able to do much tonight. Wait until tomorrow, and I will help. I promise, Maply."
    show maplyemo happy at right
    maply "You promise?"
    show sabiaemo normalopen at left
    s "I promise."
    show sabiaemo normal at left
    maply "Thank you Saby!"
    "The small catgirl flew at the half-asleep Sabia, and wrapped her arms around her, giving Sabia a tight squeeze."
    "Sabia managed to stifle a yawn as she reciprocated, enveloping the small girl within her embrace."
    maply "Tomorrow?"
    show maplyemo normal at right
    s "Tomorrow, Maply."
    "Sabia made a mental note to check up on the issue tomorrow as Maply closed the tent flaps, before heading back to sleep."
    scene bg black with dissolve
    pause (0.1)
    scene bg sabiatent with dissolve
    call sabiabase
    "Sabia awoke the next day well rested, if slightly later than usual."
    "She should have to look further into the issues at the kennels today, unless she wanted to upset Maply."
    "If the pleasure tents were anything to go by, she reasoned that the kennels would probably be poorly managed as well."
    jump lowerorccamp


label maply_hellhound_quest1_unf:
    scene bg sabiatent
    show maply 1 at right
    show maplyemo sad1 at right
    with dissolve
    maply "...Sabia?"
    maply "Sabia? Are... are you awake Sabia?"
    call sabiabase
    show sabiaemo irritated1
    with dissolve
    s "What... what time is it?"
    "Sabia grumbled. Her eyes didn't want to open. She glanced out the half-open flaps of the tent that Maply hadn't closed, and saw the camp bathed in the silver light of the moon."
    show sabiaemo pout3 at left
    s "Maply. I can't say I'm not surprised to see you here... in the middle of the night, no less."
    show maplyemo surprise2 at right
    maply "You weren't my first choice... but..."
    show maplyemo sad3 at right
    maply "They're hurting him!"
    show maplyemo sad1 at right
    show sabiaemo closed2 at left
    s "Who? What? Who is hurting who? What are you talking about?"
    show sabiaemo sad1 at left
    "Sabia did her best to curb the irritability she felt at being woken in the middle of sleep."
    "Maply was clearly distraught, and the poor girl's state was only making it harder for the catgirl to get her point across."
    show maplyemo sad1 at right
    maply "Well, I wasn't sleeping because... well, I wasn't sleeping."
    show sabiaemo sad2 at left
    "While Sabia took no pleasure in her previous dealings with Maply, the catgirl in tears now tugged at her more than when she had to get answers out of the catgirl."
    show sabiaemo happy3 at left
    s "I'm sorry Maply. Take a deep breath, and tell me what the problem is. And why you came to me?"
    show sabiaemo sad1 at left
    show maplyemo eyebrows at right
    maply "In the kennels, Sabia! In the kennels, one of the hounds. I could hear him from outside the camp!"
    show maplyemo angry1 at right
    maply "One of the guards there - I don't know his name - but one of them was hurting one of the hounds."
    maply "I could hear his poor squeals and yelps from all the way outside!"
    show maplyemo angry2 at right
    maply "The other day, I saw him beating the poor hound."
    maply "It's not his fault! He's cooped up in a cage all day, every day! It's not right that they should hurt him for acting out."
    show maplyemo sad1 at right
    maply "Some of the Orcs aren't too bad... but they're not very good at taking proper care of animals."
    maply "...I didn't want to ask you for help. But none of the orcs would understand... and you're in the tribe."
    maply "You'll help me, right? We need to go make sure that the poor hound is ok!"
    show sabiaemo closed2 at left
    "Sabia was a bit annoyed at being woken up for something that Maply could have come to her about in the morning. But she could see how frantic and worried Maply was."
    "And she had to admit that she did feel some sense of obligation to help Maply."
    show sabiaemo pout1 at left
    s "Alright, Maply. There isn't much we could do right now. It's the middle of the night still."
    s "But, tomorrow, I will see what I can do, alright?"
    show maplyemo eyebrows at right
    maply "T- tomorrow?"
    show sabiaemo closed1 at left
    s "We won't be able to do much tonight. Wait until tomorrow, and I will help. I promise, Maply."
    show maplyemo happy at right
    maply "You promise?"
    show sabiaemo normal at left
    s "I promise."
    maply "...thank you, Sabia."
    "The small catgirl stepped forward toward the half-asleep Sabia, her arms moving to give a hug."
    "But she stopped short, and pulled away from Sabia."
    maply "...tomorrow?"
    show maplyemo normal at right
    s "Tomorrow, Maply."
    "Sabia made a mental note to check up on the issue tomorrow as Maply closed the tent flaps, before heading back to sleep."
    "She hadn't made an ally of Maply before, but perhaps this could go some way to mending fences."
    scene bg black with dissolve
    pause (0.1)
    scene bg sabiatent with dissolve
    call sabiabase
    "Sabia awoke the next day well rested, if slightly later than usual."
    "She should have to look further into the issues at the kennels today, unless she wanted to further upset Maply."
    "If the pleasure tents were anything to go by, she reasoned that the kennels would probably be poorly managed as well."
    jump lowerorccamp


label maply_hellhound_quest2:
    call sabiabase
    with dissolve
    "How long Maply had been waiting at the kennels, Sabia didn't know - but it was clear that the catgirl had been there for a while."
    "Sabia could see Maply's cheeks were red, and it was clear to her that Maply had, if not been crying, at least sniffling."
    "Maply perked up, jumping off the wall she had been leaning on as Sabia approached."
    show maply 3 at right
    show maplyemo happy at right
    with dissolve
    maply "You came!"
    show sabiaemo closed1 at left
    s "Of course I did. I promised, didn't I?"
    show maplyemo sad1 at right
    maply "Well... yes. But still, I don't think most people would be too worried about a hellhound."
    show sabiaemo sad1
    s "Well, even if I am not worried about the hellhound, I'm worried about you, Maply."
    show sabiaemo normalopen at left
    s "So, come on then. Let's go check it out."
    show sabiaemo normal at left
    show maplyemo normal at right
    "Maply nodded, sniffling just a little bit more. She rubbed her nose with the back of her hand."
    maply "Ok then, Saby!"
    scene bg kennels with dissolve
    "The kennels were lined with cages along either side, each home to a hellhound."
    "Maply's pace quickened, and the catgirl was off in front of Sabia, eyes darting from cage to cage."
    "It seemed like Maply had a sixth sense, tracking down the hound she had heard and seen in mere moments."
    show maply 3 at right
    show maplyemo happy at right
    call sabiabase
    with dissolve
    maply "This is him!"
    s "How do you know?"
    maply "I just know."
    show maplyemo normal at right
    "Sabia saw an Orc lumbering over to them, clearly half-asleep."
    $ GenericOrc1.extras = ["Loincloth", "Shoulder", "Wrap", "Strap"]
    $ GenericOrc1.face = "normalopen"
    show GenericOrc1 at right
    show maply 3 at center
    show maplyemo normal at center
    with moveinright
    gorbek "Huh. What you want with this one? Been driving Gorbek crazy since Red God's Arena."
    "To emphasize his words, he jabbed his cane toward the hound, who promptly snapped at it, howling and barking its protest."
    show maplyemo sad3 at center
    "But still, the hound then shrunk to the back corner of his cage, letting a piteous whine rumble in its throat."
    if hellhoundchoice == "sub":
        show sabiaemo surprised1 at left
        "Sabia stared at the hound, trying not to let her eyes go too wide."
        "Was... was that the same hound as before?"
        "No wonder it was playing up."
        show sabiaemo closed2 at left
        "After she had given it some... intimate attention, Sabia had no doubt going back to a cage would be unwelcome."
        "She might even have sent the poor thing into a rut..."
        show sabiaemo pout3 at left
        "Its deep eyes glared at Sabia with hurt in them."
        "Best not let anyone know about it."
        show sabiaemo normal at left
        show maplyemo angry2 at center
        "Sabia blinked, coming back to the kennels with a start from her reminisce. Maply was not pleased."
    maply "You can't just hurt him for that!"
    maply "He's a hound! He's meant to be out and about, free, hunting and playing with his own kind. Not cooped up here!"
    maply "No wonder why he's acting out. I bet you wouldn't like being in a cage!"
    show maplyemo angry1 at center
    "Maply's voice was getting shrilled, higher; her nostrils flared as she breathed in heavily."
    show sabiaemo irritated2 at left
    "It was plain to Sabia that there was something more to this than just a mistreated hellhound, but that might be something she'd have to look into later."
    $ GenericOrc1.face = "normalopen"
    gorbek "Ugh. Gorbek not get paid enough to put up with whining catgirls. Meant to look after hellhounds."
    gorbek "Not loud, bossy catgirls."
    show sabiaemo closed4
    s "And is beating hellhounds what you constitute as looking after them?"
    show sabiaemo normal at left
    "The Kennelmaster sighed. He looked as if he were at the last, ragged and fraying ends of his patience."
    $ GenericOrc1.face = "sad1"
    gorbek "Look. This one used to be good, but then he changed after the Arena. What do you expect Gorbek to do?"
    $ GenericOrc1.face = "normalopen"
    gorbek "Groknak never going to let us sell hellhounds to any not in tribe. Gorbek don't want to, but maybe have to put him down."
    $ GenericOrc1.face = "normal"
    show maplyemo angry3
    "Maply almost exploded in anger. Sabia had to put a hand on the catgirl's shoulder to stop her from lunging forward."
    show maplyemo angry1 at center
    show sabiaemo normalopen at left
    s "Can you sell him to me, then?"
    $ GenericOrc1.face = "normalopen"
    gorbek "Can't sell him."
    $ GenericOrc1.face = "normal"
    show sabiaemo annoyed2 at left
    show maplyemo surprise2
    maply "But you just said that you could sell him to someone in the tribe!"
    show sabiaemo normal at left
    $ GenericOrc1.face = "normalopen"
    gorbek "Yes, but can't be sold untrained. Not good. Groknak not approve of that."
    $ GenericOrc1.face = "normal"
    show sabiaemo irritated2
    s "Then what {i}can{/i} we do?"
    "The orc sighed again, looking over at the hellhound, then back to the distraught Maply."
    $ GenericOrc1.face = "normalopen"
    gorbek "Maybe Gorbek can let you try to train him. Gorbek don't think you're going to be very successful, but if stop nosy humans and whining catgirls from annoying Gorbek, go for it."
    "Sabia's reassuring hand squeezed Maply's shoulder a bit tighter."
    show sabiaemo normal
    s "Thank you."
    gorbek "Maybe use the Arena. No one uses it now, Gorbek would go there. Nice and quiet and big space to train."
    "The Orc dumped some keys into Sabia's hands, and then started grumbling under his breath as he stalked off."
    hide GenericOrc1
    show maply 3 at right
    show maplyemo surprise2 at right
    with moveoutright
    gorbek "...aggressive hellhounds, human tribe-members and angry catgirls. Ugh. Gorbek don't know what's going on anymore."
    "Maply crouched down in front of the cage, and beckoned the hound over."
    show maplyemo normalopen
    maply "Come here boy!"
    maply "I'm not going to hurt you like that big mean orc does. Come on, it's ok!"
    show maplyemo normal at right
    "The hound barked, gnashing its wicked, glinting teeth. Its saliva splattered the walls from the force of the jaws snapping."
    show maplyemo sad1
    "Maply shrunk back into Sabia."
    show sabiaemo closed3
    s "Hmm. I remember back when I was young. Our kennelmaster made sure that our hounds had toys and treats to play with."
    s "It always seemed to keep them occupied when they were in their cages."
    show sabiaemo normal
    show maplyemo sad2
    maply "I don't think that orcs will have many toys or playthings for a hound, Saby."
    show maplyemo sad1
    "Maply pointedly looked around the interior of the kennels, and both she and Sabia noticed the lack of anything remotely resembling a toy."
    show sabiaemo normalopen
    s "Maybe Vehlis?"
    s "She is a trader after all. Maybe she has something? Traveling into orc territory, she might have brought something."
    show sabiaemo normal
    show maplyemo happy
    maply "Great idea, Saby! I'll go ask her right now!"
    show maplyemo normal
    s "Hang on Maply. I've already had some dealings with her, perhaps it would be best if I go. You haven't met her yet, have you?"
    show maplyemo eyebrows
    "Maply grimaced, looking back at the hound that had holed itself up in the corner, clearly worried that another strike might come at any moment."
    maply "Ok Saby... but don't take too long, please. I don't like seeing innocent animals locked up and hurt."
    maply "I just can't stand it at all!"
    show sabiaemo closed2
    s "(Maply seems far more upset about this than I'd expect most people to be... I wonder why?)"
    show sabiaemo normalopen
    s "I won't take too long. Vehlis is a busy woman, though. But I'll do my best to see her as soon as I can, Maply."
    show sabiaemo normal
    show maplyemo sad1
    maply "Thank you Saby. Please hurry, though."
    maply "I think I'll stay here for a little bit today."
    show sabiaemo normalopen
    s "Be careful. Hellhounds aren't known for their safe play, Maply."
    jump lowerorccamp


label maply_hellhound_quest2_unf:
    call sabiabase
    with dissolve
    "How long Maply had been waiting at the kennels, Sabia didn't know - but it was clear that the catgirl had been there for a while."
    "Sabia could see Maply's cheeks were red, and it was clear to her that Maply had, if not been crying, at least sniffling."
    "Maply perked up, jumping off the wall she had been leaning on as Sabia approached."
    show maply 3 at right
    show maplyemo happy at right
    with dissolve
    maply "You came!"
    show sabiaemo closed1 at left
    s "Of course I did. I gave my word."
    show maplyemo sad1 at right
    maply "Well... yes. But still, I don't think most people would be too worried about a hellhound."
    maply "And I wasn't sure you'd want to help me after..."
    show sabiaemo happy1 at left
    s "I've made mistakes, as everyone has. But people can try to fix them."
    "Maply nodded, sniffling just a little bit more. She rubbed her nose with the back of her hand."
    show maplyemo normal at right
    maply "Ok then, Sabia!"
    scene bg kennels with dissolve
    "The kennels were lined with cages along either side, each home to a hellhound."
    "Maplys's pace quickened, and the catgirl was off in front of Sabia, eyes darting from cage to cage."
    "It seemed like Maply had a sixth sense, tracking down the hound she had heard and seen in mere moments."
    show maply 2 at right
    show maplyemo normal at right
    call sabiabase
    with dissolve
    maply "This is him!"
    s "How do you know?"
    show maplyemo happy at right
    maply "I just know."
    "Sabia saw an Orc lumbering over to them, clearly half-asleep."
    $ GenericOrc1.extras = ["Loincloth", "Shoulder", "Wrap", "Strap"]
    $ GenericOrc1.face = "normalopen"
    show GenericOrc1 at right
    show maply 3 at center
    show maplyemo normal at center
    with moveinright
    gorbek "Huh. What you want with this one? Been driving Gorbek crazy since Red God's Arena."
    "To emphasize his words, he jabbed his cane toward the hound, who promptly snapped at it, howling and barking its protest."
    "But still, the hound then shrunk to the back corner of his cage, letting a piteous whine rumble in its throat."
    if hellhoundchoice == "sub":
        show sabiaemo surprised1 at left
        "Sabia stared at the hound, trying not to let her eyes go too wide."
        "Was... was that the same hound as before?"
        "No wonder it was playing up."
        show sabiaemo closed2 at left
        "After she had given it some... intimate attention, Sabia had no doubt going back to a cage would be unwelcome."
        "She might even have sent the poor thing into a rut..."
        show sabiaemo pout3 at left
        "It's deep eyes glared at Sabia with hurt in them."
        "Best not let anyone know about it."
        show sabiaemo normal at left
        "Sabia blinked, coming back to the kennels with a start from her reminisce. Maply was not pleased."
    maply "You can't just hurt him for that!"
    maply "He's a hound! He's meant to be out and about, free, hunting and playing with his own kind. Not cooped up here!"
    maply "No wonder why he's acting out. I bet you wouldn't like being in a cage!"
    show maplyemo angry1 at center
    "Maply's voice was getting shrilled, higher; her nostrils flared as she breathed in heavily."
    "It was plain to Sabia that there was something more to this than just a mistreated hellhound, but that might be something she'd have to look into later."
    gorbek "Ugh. Gorbek not get paid enough to put up with whining catgirls. Meant to look after hellhounds."
    gorbek "Not loud, bossy catgirls."
    show sabiaemo closed4
    s "And is beating hellhounds what you constitute as looking after them?"
    "The Kennelmaster sighed. He looked as if he were at the last, ragged and fraying ends of his patience."
    $ GenericOrc1.face = "sad1"
    gorbek "Look. This one used to be good, but then he changed after the Arena. What do you expect Gorbek to do?"
    gorbek "Groknak never going to let us sell hellhounds to any not in tribe. Gorbek don't want to, but maybe have to put him down."
    show maplyemo angry3
    "Maply almost exploded in anger. Sabia had to put a hand on the catgirl's shoulder to stop her from lunging forward."
    show sabiaemo irritated1
    s "Can you sell him to me, then?"
    gorbek "Can't sell him."
    show maplyemo surprise2
    maply "But you just said that you could sell him to someone in the tribe!"
    gorbek "Yes, but can't be sold untrained. Not good. Groknak not approve of that."
    show sabiaemo irritated2
    s "Then what {i}can{/i} we do?"
    "The orc sighed again, looking over at the hellhound, then back to the distraught Maply."
    $ GenericOrc1.face = "normalopen"
    gorbek "Maybe Gorbek can give you one week. If you can't train him by then, Gorbek going to have to look into other solutions."
    "Sabia's reassuring hand squeezed Maply's shoulder a bit tighter."
    show sabiaemo normal
    s "Thank you. One week."
    gorbek "Maybe use the Arena. No one uses it now, Gorbek would go there. Nice and quiet and big space to train."
    "The Orc dumped some keys into Sabia's hands, and then started grumbling under his breath as he stalked off"
    hide GenericOrc1
    show maply 3 at right
    show maplyemo surprise2 at right
    with moveoutright
    gorbek "...aggressive hellhounds, human tribe-members and angry catgirls. Ugh. Gorbek don't know what's going on anymore."
    "Maply crouched down in front of the cage, and beckoned the hound over."
    show maplyemo normalopen
    maply "Come here boy!"
    maply "I'm not going to hurt you like that big mean orc does. Come on, it's ok!"
    "The hound barked, gnashing its wicked, glinting teeth in the far back of its cage. It's saliva splattered the walls from the force of the jaws snapping."
    show maplyemo sad1
    "Maply shrunk bank into Sabia."
    show sabiaemo closed3
    s "Hmm. I remember back when I was young. Our kennelmaster made sure that our hounds had toys and treats to play with."
    s "It always seemed to keep them occupied when they were in their cages."
    show sabiaemo normal
    show maplyemo sad2
    maply "I don't think that orcs will have many toys or playthings for a hound, Sabia."
    "Maply pointedly looked around the interior of the kennels, and both she and Sabia noticed the lack of anything remotely resembling a toy."
    show sabiaemo normal
    s "Maybe Vehlis?"
    s "She is a trader after all. Maybe she has something? Traveling into orc territory, she might have brought something."
    show maplyemo happy
    maply "Great idea, Sabia! I'll go ask her right now!"
    show sabiaemo normalopen
    s "Hang on Maply. I've already had some dealings with her, perhaps it would be best if I go. You haven't met her yet, have you?"
    show maplyemo eyebrows
    "Maply grimaced, looking back at the hound that had holed itself up in the corner, clearly worried that another strike might come at any moment."
    maply "Ok Sabia... but don't take too long, please. I don't like seeing innocent animals locked up and hurt."
    maply "I just can't stand it at all!"
    show sabiaemo closed2
    s "(Maply seems far more upset about this than I'd expect most people to be... I wonder why?)"
    s "I won't take too long. Vehlis is a busy woman, though. But I'll do my best to see her as soon as I can, Maply."
    show maplyemo sad1
    maply "Thank you Saby. Please hurry, though."
    maply "I think I'll stay here for a little bit today."
    show sabiaemo normalopen at left
    s "Be careful. Hellhounds aren't known for their safe play, Maply."
    jump lowerorccamp


label maply_hellhound_quest3:
    call sabiabase
    show sabiaemo sad1 at left
    with dissolve
    "Sabia's muscles tensed as she swung the door open."
    show sabiaemo normal at left
    s "Oh."
    show vehlis normalL at right
    show vehlis2 arm1 at right
    with dissolve
    vehlis "Expecting something else?"
    show sabiaemo happy2
    s "Well... yes. The last few times were, uh..."
    show sabiaemo normal
    show vehlis happyL
    vehlis "When you make it a habit to barge in unannounced, you'll find yourself seeing things you shouldn't."
    show vehlis open
    vehlis "It seems you've managed to miss my fun for the day, though it does seem you are making a habit of interrupting me during things that I find to be of import."
    vehlis "How can I help you today, Sabia?"
    show vehlis normal
    show sabiaemo normalopen
    s "One of the hellhounds in the kennels has been playing up. Acting out, aggressive."
    s "Maply's made it her mission to make sure that the hound doesn't need to be put down."
    show sabiaemo normal
    show vehlis eyebrow2
    vehlis "I'm afraid I'm not in the market for any hellhounds at the moment... as fun as they might be, I'm sure."
    if hellhoundchoice == "sub":
        show sabiaemo surprised1
        show sabiaemo2 blush at left
        s "What do you mean?"
        show vehlis closed3
        vehlis "Oh, it's just I've heard sometimes, they take a little too strongly to their companions."
        show vehlis happy
        vehlis "If you know what I mean...?"
        show vehlis normal
        "Sabia disliked the knowing smirk that seemed etched on the banker's face."
        show sabiaemo closed4
        s "I- uh, I don't know what you're talking about."
        show vehlis open
        vehlis "Of course not."
        show vehlis normalL
        "Ever the consummate businesswoman, Vehlis let the remark slide."
    show sabiaemo normalopen
    hide sabiaemo2
    s "Actually, that's not what I was after. The kennelmaster wouldn't sell an untrained hound, anyway."
    s "I was wondering if you might have something to help a beast relieve energy? Some toys maybe?"
    show sabiaemo normal
    show vehlis concern
    vehlis "A toy? For a hellhound? That's a tall order. They're no mere hunting dog that a Lundarian, aristocratic family might have."
    show vehlis open
    vehlis "But. I might have something. Not on me, of course. Go see Alioch. His stocktake of my inventory is much more accurate, and complete than my own."
    "Vehlis spread her arms wide in a coy show of modesty."
    show vehlis happy
    vehlis "It is his job, after all."
    show vehlis normalL
    show sabiaemo happy1
    s "Thank you, Vehlis. I don't think I've seen Maply this distraught. Even when she was first captured, she seemed more calm than she is now."
    show sabiaemo normalopen
    s "How much is this going to cost?"
    show sabiaemo normal
    show vehlis normal
    vehlis "On the house."
    show sabiaemo irritated1
    s "Why?"
    show vehlis happy
    vehlis "Investing in a good cause."
    vehlis "Have a good day. And do try to not barge in on anything you don't want to see in the future."
    jump mainhall2


label maply_hellhound_quest4:
    show alioch happy at right
    call sabiabase
    with dissolve
    alioch "Sabia! It's good to see you."
    show sabiaemo happy1
    s "It's good to see you as well, Alioch."
    show sabiaemo normalopen
    s "But my visit is unfortunately not just for a chat."
    s "Vehlis said you might have something I'm looking for."
    show sabiaemo normal
    alioch "I might. More specifically, Vehlis might. But I'll need a few more details than that. What are you looking for?"
    show sabiaemo normalopen
    s "Something a hellhound might find entertaining. A toy?"
    show sabiaemo normal
    show alioch eyebrow1
    alioch "A toy for a hellhound! What would you need that for? No matter, it's not my place to ask."
    alioch "I might have something. Give me a moment."
    hide alioch with moveoutright
    "Disappearing, Alioch heads out the back. Sabia can hear him rummaging about."
    show alioch happy at right with moveinright
    "After a few minutes, he reappears, a grin etched on his face and holding something much brighter, and gaudier than Sabia expected."
    alioch "Here. It's a toy fit for a hellhound."
    show sabiaemo irritated2
    s "What is it?"
    show alioch normal
    alioch "A small, wooden bird. There's an enchantment on it. It will fly along, just above the ground, and swoop away whenever something gets near."
    alioch "It was used to lure out bigger, more dangerous game in the forests so that they could be brought down by arrows."
    show sabiaemo happy1
    s "That sounds perfect!"
    s "How do I get it to start, and how do I retrieve it, though?"
    show sabiaemo annoyed2
    "The Elf shrugged."
    show sabiaemo normal
    show alioch normal
    alioch "That one you'll have to figure out yourself."
    alioch "I hope this will help."
    if hellhoundchoice == "sub":
        show alioch happy
        alioch "Though if it doesn't, I'm sure you can always settle it down some other way?"
        show sabiaemo closed2
        show sabiaemo2 blush at left
        s "(How did Vehlis find out? Ugh.)"
        alioch "Have a good day!"
        hide sabiaemo2
        show sabiaemo normal at left
        s "(Well... anyway. I'd like to go now, but I doubt Gorbek would allow us to take the hound out this late in the day.)"
    else:
        alioch "I do need to get back to work now, though."
        show sabiaemo normalopen
        s "Thank you Alioch."
        alioch "Of course."
        show sabiaemo normal
        s "(I'd like to be able to go now, but I doubt Gorbek would allow us to take the hound out this late in the day.)"
    jump tradinglodge2


label maply_hellhound_quest5:
    call sabiabase
    show maply 1 at right
    show maplyemo happy at right
    maply "SABY!"
    maply "Did you get something from Vehlis? I could barely sleep last night! Can we go back and help him?"
    show maplyemo normal at right
    if maplybefriended == False:
        show sabiaemo happy2 at left
        s "...Saby?"
        "It almost sounded like something a friend would call her, trying to be cute."
        "Sabia was taken back a little bit, it coming from Maply."
        show maplyemo normalopen
        maply "It felt really formal to keep calling you Sabia! You need a personal name, so... Saby!"
        s "Hmm... does that mean you have another name?"
        show maplyemo happy
        maply "Yup, my mother named me Maple! But I don't really like how it sounds - so Maply!"
        show sabiaemo normalopen
        s "And... you're fine with calling me Saby?"
        maply "Yep! You made a mistake and I was really mad - but then you're being very nice now helping out."
        maply "So that's ok. I forgive you, Saby!"
        show maplyemo normal
        show sabiaemo normalopen
        s "...just like that?"
        show sabiaemo normal
        show maplyemo happy
        maply "Sure!"
        show maplyemo sad1
        maply "Do... do you not want me to call you Saby?"
        show sabiaemo happy3
        s "No. It's fine. I like it."
        show maplyemo normal
        s "So... which one is your real name, then? Maply, or Maple?"
        show maplyemo happy
        maply "They're both my names, Sabim!"
        s "Wait, what does that one mean?"
        maply "Not telling, hehehe!"
        s "...do you have any other names?"
        show maplyemo normal
        maply "Oh, a bunch. If I got famous enough, people might even call me Maplana!"
        s "So... 'Sabiana' would be a good thing?"
        maply "Yup! That's for pretty serious things, though."
        "As the two walked to the kennels, Sabia felt a tension she hadn't realized existed disappear, thanks to Maply's words."
        "On the way, Sabia explained to Maply what the item she received from Alioch was."
    else:
        show sabiaemo normalopen
        s "I did. We can."
        "As the two walked to the kennels, Sabia explained to Maply what the item she received from Alioch was."
    if hellhoundchoice == "sub":
        show sabiaemo sad1
        "Sabia was unsure how the hound was going to react to seeing her again."
        "It hadn't been so long ago that... well. No need to dwell on it."
        show sabiaemo normal
        "But it seemed that her worrying had been misplaced."
        "As soon as Maply unlocked the cage, the hound barreled out of it, and knocked the small catgirl to the ground."
        show sabiaemo surprised3
        "Sabia felt her gut wrench as she watched it happen, her body sluggish to react."
        show maplyemo happy
        "But Maply's cries weren't of pain or terror, but a happy giggling as the hound licked the catgirl's face happily."
        show sabiaemo normal
        "After a few moments, it gave a pensive look at Sabia, sniffed, and turned its attention back to Maply."
        "The two spent a few minutes tumbling on the floor before they left for the Arena."
    if hellhoundchoice == "drug":
        "Maply once again shot ahead of Sabia, and had the keys ready."
        "The small catgirl unlocked the cage, and the hound surged forward like a bolt of grizzled lightning."
        show sabiaemo surprised1
        "It darted past Maply, and pounced in front of Sabia, forepaws spread wide as it growled."
        "Maply rushed up and wrapped her arms around the hound without fear."
        "Whether it enjoyed Maply's attentions enough to dissuade it from its anger or it simply no longer cared, Sabia didn't know."
        show sabiaemo normal
        "But the hound relented, and turned its own attention towards the fawning Maply."
        show maplyemo happy
        maply "There's a good boy! C'mon!"
    scene bg black
    with dissolve
    pause (0.25)
    scene bg arenahound
    with dissolve
    pause (0.1)
    call sabiabase
    show sabiaemo pout3 at left
    show maply 1 at right
    show maplyemo normal at right
    with dissolve
    "As they arrived at the empty Arena, Sabia thought that the hellhound didn't seem nearly as bad as the kennelmaster suggested."
    show sabiaemo normal
    "Or perhaps Maply was just that good with animals?"
    show maplyemo normalopen
    maply "Quick Saby! He wants to play. Look, he's a good boy, isn't he?"
    maply "That mean orc just doesn't know how to look after good hounds!"
    show maplyemo normal
    "The hound was nothing more than a blur of red fur and white teeth as it darted around Maply, lunging in and stepping back."
    "Every now and then it would bite playfully at the catgirl."
    show sabiaemo normal
    "Sabia watched the two play for a few minutes, before pulling out the enchanted toy. Shrugging, she threw it in the air."
    "The light of the sun caught on the bright green and blue hues, glimmering and gleaming, and it took to the air immediately."
    "Though the hound had been enjoying playing with Maply, its ears perked up, and its eyes locked on to the bird as it started to glide about the empty arena."
    show maplyemo happy
    maply "I think he likes it Saby."
    "The hound seemed eager to prove the truth of Maply's words, bounding off after the colorful toy."
    "It took only a few seconds, and the hound closed on the toy, leaping into the air..."
    "And landed with a thud, dust billowing up tiny clouds about its paws. The false bird gained a bout of speed, pulling away from the hound's reach with ease."
    maply "So close! Try again! Try again! You'll get it this time! Ehehehe soooo close!"
    show maplyemo normal
    "Sabia leaned against one of the pillars on the edges of the Arena, content to watch Maply and the hound play."
    "The hound chased the bird, and Maply chased the hound, a giddy smile on her face."
    "It might be the happiest Sabia had seen the young catgirl."
    show maplyemo eyebrows
    maply "Oh, bad luck, boy!"
    show maplyemo normalopen
    maply "Quick, you have to run faster! Faster, faster! You'll get him!"
    show maplyemo normal
    "Sabia watched the hound respond to Maply."
    "With every urging cry from the catgirl, the hound's powerful legs moved a little bit faster, and the lead the bird had grew smaller and smaller."
    "And with every failed attempt it let out a disappointed whine, before dropping back to rub against Maply as the catgirl caught up."
    "Catgirls were an athletic and nimble bunch, but even Maply was no match for the ease the hound found at chasing and running, and she soon had a sheen of sweat on her forehead."
    show maplyemo normalopen
    maply "Oof. I think I need to have a short break. You're too fast for me!"
    "Maply sat on the ground unceremoniously, with a little thud."
    "The bird wheeled about, but the hound ignored it and trotted over to Maply."
    show maplyemo happy
    maply "Aww... you're a little sweetie aren't you? Yes you are!"
    maply "Yes you are! Who's a good hellhound?"
    show maplyemo normal
    show sabiaemo closed2
    s "(Was the beast just bored...?)"
    show sabiaemo normal
    "It plopped down next to Maply, and rested its head on the catgirl's lap, nose twitching and sniffing."
    "Sabia could hear a deep rumbling from the hound's belly as Maply pet it, pulling it in closer to her."
    "Vehlis's favor whizzed about the Arena once more, unchased, before it flitted back down with an easy grace to Sabia, landing neatly on the ground in front of her."
    show sabiaemo eyebrow1
    s "Well I suppose that answers at least one question today."
    "Sabia pocketed it, and looked skyward. The sun had moved across the cloudy blue, and as much as she didn't want to break up Maply and the hound, they had to head back for the day."
    show sabiaemo normal
    show maplyemo sad3
    maply "Nooo! I don't want to take him back. The kennelmaster is going to be mean to him again!"
    show maplyemo angry1
    "Maply wrapped her arms about the hound's neck tight, and buried her face in red fur. The hound licked happily at Maply's chest."
    show sabiaemo happy3
    s "I think he might have just needed a bit of play. With all the excitement from the Red God's celebrations, maybe he just got worked up."
    s "How about we leave the toy with him in his cage? We can check on him tomorrow and see how he's going."
    show maplyemo sad2
    "Maply sniffed, rubbing her reddening eyes with two tiny fists."
    maply "Ok, Saby. I don't want to... but maybe you're right."
    "The three of them left the Arena, on the walk back to Grok og Dar Maply seemed a little happier, and the hound kept a little closer to the catgirl."
    scene bg black
    with dissolve
    pause (0.25)
    scene bg kennels
    with dissolve
    "They returned back to Grok og Dar as the sun was starting its descent, and Maply sniffled as they led the hound back to its cage."
    call sabiabase
    show maply 1 at right
    show maplyemo sad2 at right
    with dissolve
    maply "We'll be back tomorrow, ok, boy? Be good for me? You can keep this toy for now! Maybe it will help keep you entertained, even if it can't fly too far in here."
    show maplyemo sad1 at right
    show sabiaemo normalopen
    s "I'm sure he'll be fine for one night, Maply. And besides, he was very obedient and friendly today. I'm sure that he was just bored."
    show sabiaemo normal
    "The kennelmaster scoffed at the two girls from a distance, grumbling something incoherent and yet identifiably dismissive from the tone."
    show maplyemo eyebrows
    maply "I promise I'll be back tomorrow!"
    jump lowerorccamp


label maply_hellhound_quest6:
    show maplyemo sad2
    maply "Saby, he broke the toy!"
    "Maply was frantic, dashing over to Sabia."
    show maplyemo sad3
    maply "He was doing so good too... but then he broke it and was growling and snarling at Gorbek!"
    maply "Gorbek said that we won't be able to train him, that he's too aggressive! But Saby that's not right, he was so sweet yesterday!"
    show sabiaemo normalopen
    s "Slow down Maply! What happened?"
    show maplyemo sad1
    maply "I went to check on him earlier, before you came. The toy bird was in pieces about the cage, and he was snapping at the kennelmaster and growling..."
    show sabiaemo happy1
    s "Calm down Maply. I had an idea last night. Maybe play isn't enough - he needs to go on a proper hunt."
    maply "A hunt?"
    show sabiaemo closed3
    s "He was enjoying the enchanted bird so much yesterday - and that was intended as a hunting aide, as a sort of lure."
    show maplyemo sad2
    maply "Oh... so he wanted to hunt? But he only got to play with fake prey?"
    s "Exactly! So-"
    show maplyemo happy
    maply "If we take him out to hunt, maybe he'll settle down?"
    show sabiaemo normalopen
    s "It's worth a try."
    scene bg black
    with dissolve
    pause (0.25)
    scene bg kennels
    with dissolve
    "The two went to pick up the hound from the kennels."
    "As was usual by now, Maply ran off ahead, and unlocked the cage before Sabia had gotten halfway there."
    "The hound pounced on Maply, driving the catgirl to the ground, before leaping off and jumping around, twirling about and snapping playfully at Maply's feet."
    call sabiabase
    show sabiaemo happy1
    with dissolve
    s "Come on, let's take him out for a real hunt then."
    show maply 1 at right
    show maplyemo happy at right
    with dissolve
    maply "Yes! He's going to love that! Aren't you? A nice hunt in a big open area! Let's go!"
    hide maply
    hide maplyemo
    with dissolve
    show sabiaemo normal
    "Maply bounded off, running out the gates of the camp without looking behind. Sabia had to ease into a jog to keep up with the two."
    "The hound kept close to Maply as they ran over to the forest, as if it didn't want to stray too far from Maply."
    scene bg black
    with dissolve
    pause (0.25)
    scene bg forest
    call sabiabase
    show maply 1 at right
    show maplyemo normal at right
    with dissolve
    maply "He seems so happy, Saby."
    show maplyemo normalopen
    maply "I think you might have been right!"
    show maplyemo normal
    "The hound seemed at home in the forest, dashing this way and that, excitement palpable from the wagging tail far ahead of them."
    "Before long, it spotted a small hare, and dashed off in a flurry of red fur and gnashing teeth."
    "It disappeared behind some trees as it chased its prey, the powerful thudding of the paws on the ground fading."
    show sabiaemo normalopen
    s "So, Maply. Why was this so important to you?"
    s "All of this over just a few heard yelps?"
    s "Even those that are fond of animals would think twice about looking into something so innocuous."
    show sabiaemo irritated1
    show maplyemo sad1
    "Maply didn't reply to start with. She just stood there, head upturned just a little as she watched the forest canopy swaying and rustling in the wind."
    "The hound popped back into sight, dashing back to Maply's feet and depositing a hare. It rested on its haunches, looking up expectantly at Maply."
    show maplyemo happy
    maply "Good boy! You're such a good boy, aren't you? That mean orc doesn't know anything!"
    show maplyemo normal
    "Satisfied, it gave Maply a lick on the face, its large tongue almost as big as Maply's head, before bounding off, after some other prey it had seen."
    "Sabia thought Maply wasn't going to answer, and though curiosity burned in her, she was ready to let the question drift away."
    show maplyemo normalopen
    maply "My mom died when I was pretty young."
    show maplyemo normal
    show sabiaemo sad2
    s "I'm sorry, Maply. I didn't know."
    maply "It's not your fault, Saby. You don't need to be sorry."
    show maplyemo happy
    maply "A caravan is like a giant big family anyway, so I didn't have too much trouble growing up!"
    maply "Though the caravan is always supportive - it was like having a big family of helpful sisters, y'know? I still ended up spending more time with the animals than anyone else did in my free time!"
    maply "I just connected with them easily, and I always made friends with them."
    maply "It's probably the bit of my dad in me more than anything else, though!"
    show maplyemo normal
    show sabiaemo normalopen
    s "I didn't know fathers stuck around for their catgirl daughters?"
    show maplyemo happy
    maply "Oh. They don't. Dad was an Arwa though."
    show maplyemo normal
    show sabiaemo happy3
    s "An Arwan Elf? I suppose an affinity for nature and animals would make sense!"
    show maplyemo normalopen
    maply "No Saby, he was an Arwa."
    show sabiaemo surprised1
    s "An... I'm sorry. What?"
    s "Your dad was a four-legged animal, with a horn from his forehead?!"
    maply "Yep!"
    maply "Ehehehe! Everyone always gets confused when I say that cause the elves are named after the animal. They've got a pretty deep connection, I think. And it goes back so long too!"
    show sabiaemo eyebrow1
    s "Huh. I knew catgirls could mate with animals - but I thought it was uncommon, and they preferred Elves."
    show maplyemo smirk
    maply "They do! But I guess mom just couldn't help herself."
    show maplyemo normal
    show sabiaemo normal
    "Before Sabia had the chance to say anything else, the hound's bark boomed through the forest, bouncing off the trees."
    "Half excitement, and half calling, Maply responded instinctively to it, running after it."
    "Sabia followed."
    "The hound wasn't too far ahead, and they came upon it quickly, a large elk a few hundred yards in the distance."
    "It must have been a little spooked from the hound's call, as it was scanning the forest floor, but unable to spot anything it judged out of the ordinary."
    show maplyemo normalopen
    maply "I don't mind this, if you were wondering, Saby."
    maply "Animals being mistreated or hurt is bad! But hunting is natural."
    show maplyemo normal
    show sabiaemo happy1
    "Sabia nodded, about to speak. Once more, she was cut off as the hound exploded from its hidden vantage. The elk jumped, startled at the sight, and bounded off as fast as it could in the opposite direction."
    hide maply
    hide maplyemo
    with moveoutright
    "Maply darted after the hound, and Sabia almost sighed, sliding into a run to follow at the end."
    scene bg forest
    with dissolve
    "The hound moved easily through the forests, seeming to pivot and dart off in another direction without stopping."
    "No less at home was the elk - or even Maply."
    "Sabia definitely felt the odd one out, trailing behind all three of them."
    "She could hear Maply urging the hound on, and the elk itself crashing into leaves and low hanging branches."
    "Maply, ahead, had stopped running, and Sabia caught up with her."
    $ GenericOrc1.extras = ["Loincloth", "Axe", "Piercing", "Helmet"]
    $ GenericOrc1.face = "smile2"
    $ GenericOrc2.extras = ["Loincloth", "Axe", "Hair", "Stomach"]
    $ GenericOrc2.face = "smile2"
    show GenericOrc2:
        xzoom -1 anchor (1.0,1.0) pos (0.8,1.0)
    show GenericOrc1:
        anchor (1.0,1.0) pos (1.1,1.0)
    show maply 1:
        anchor (1.0,1.0) pos (0.85,1.0)
    show maplyemo surprise1:
        anchor (1.0,1.0) pos (0.85,1.0)
    with dissolve
    call sabiabase
    show sabiaemo surprised2
    with moveinleft
    maply "...Saby?"
    bandit1 "Heh. What do we have here, then?"
    bandit2 "A cute little catgirl."
    bandit1 "And you wanted to go to work today!"
    bandit2 "Of course I fucking did. The boss has been breathing down our backs so fucking hard lately to keep the pressure up---"
    $ GenericOrc1.face = "angry"
    bandit1 "Shut up you stupid idiot!"
    show maplyemo sad2
    maply "Lemme go!"
    show sabiaemo irritated1
    s "Yes. Let her go."
    "Sabia's fingers wrapped about the hilt of her sword, angling herself so that it was noticeable."
    $ GenericOrc1.face = "smile1"
    bandit1 "Nah. Don't think so. Whoa! Hey, now, don't even think about drawing that sword..."
    bandit1 "If you do, something might happen to this pretty little slut."
    show maplyemo sad3
    maply "Saby! Help!"
    menu:
        s "(...should I try to find out more?)"
        "Try to glean information.":
            $ A_maply -= 1
            show sabiaemo normalopen
            s "Wait, bandits have bosses?"
            show maplyemo sad1
            bandit1 "Fuck. Everyone has a boss somewhere, don't they?"
            bandit2 "...yeah but we're skiving off today..."
            $ GenericOrc1.face = "angry"
            bandit1 "SHUT. UP. YOU. DOLT."
            "One of the bandits held a blade against Maply, the threat of it sliding in palpable."
        "Focus on saving Maply.":
            $ A_maply += 1
            show sabiaemo angry1
            s "Of course, Maply!"
            show maplyemo eyebrows
            bandit1 "Whoa there!"
            "A glint of steel in the light that broke through the canopy caught Sabia's attention, and she saw the pointed blade of the dagger threatening to slide into Maply's side."
    show maplyemo sad3
    "Maply screamed. The sound broke through the forest, and the canopy rustled as birds took flight, fleeing from the screech."
    show sabiaemo surprised2
    "One of the bandits smirked confidently, but Sabia's look of surprise wasn't for the bandits."
    "If she had thought she had seen the fury of a hellhound before, she realized in that instant she was very much incorrect."
    "Hackles were raised, and it hit Sabia that the hound hadn't been hunting the elk. It had been toying with it, playing."
    "It was like a streak of fire, shooting through the forest. Mouth wide, and teeth like razor-sharp daggers lining its jaws."
    "The full weight of it smashed into the bandit holding the axe, and the orc tumbled several yards away, rolling over himself again and again."
    call shake ("h")
    $ renpy.show("GenericOrc1mask", at_list=[screen_farright], what=AlphaBlend(Transform("GenericOrc1", alpha=0.9), "GenericOrc1", bloodhit_effect, alpha=True))
    pause(0.1)
    hide GenericOrc1
    hide GenericOrc1mask
    with dissolve
    "Sabia watched, frozen by the sheer ferocity the hound was displaying."
    "The second bandit barely had time to blink before he found his leg pinned by teeth."
    show maplyemo surprise1
    show maply at screen_farleft:
        xzoom -1
    show maplyemo at screen_farleft:
        xzoom -1
    with move
    "Maply darted over to Sabia and wrapped her arms around her as they both watched the man clawing at the forest floor, trying to free himself from that iron grip."
    "The hound must have judged that there was enough space between Maply and the threat, and released the bandit, barreling down past Sabia and Maply to the other attacker."
    "Wind whistled as it passed them. It stood its ground, between Maply and the bandit, growling. The threat was clear, and the hound's eyes were like burning flames."
    hide GenericOrc2 with moveoutright
    "Scrambling to his feet as best he could, the unprepared bandit glanced at his comrade, glanced at the hound, back at his friend. Then he turned and fled, stumbling as he did so."
    "Behind Sabia, the hound plonked itself down next to Maply, and it was clear it wasn't going to budge."
    show sabiaemo closed1
    "Sabia couldn't help but feel a sense of smugness, even if most of the work had been done by the hound."
    show maplyemo sad3
    maply "Saby! Behind you!"
    show sabiaemo surprised2
    $ GenericOrc1.extras = ["Loincloth", "Axe", "Necklace", "Beard2", "Wrists"]
    $ GenericOrc1.face = "suspicious"
    show GenericOrc1 behind maply at center with moveinright
    "Whirling on the spot, Sabia was a bit too slow, and the first strike from the previously hidden enemy drove the breath from her."
    $ Sabia.hp = int(Sabia.hp / 2)
    $ enemy_level = 7
    $ enemy_maxhp = 500
    $ enemy_hp = enemy_maxhp
    $ enemy_type = 1
    $ enemy_skills = [Enemyattack,Enemyattack,Enemyquickattack]
    $ enemy_attack = 65
    $ enemy_defense = 0
    $ enemy_magdefense = 0
    $ GenericOrc1.face = "normal"
    $ GenericOrc1.extras = ["Loincloth", "Axe", "Necklace", "Beard2", "Wrists"]
    $ GenericOrc1.actives = []
    $ player = Sabia
    $ enemy = GenericOrc1
    call duel
    if _return != "Victory":
        show gameover with dissolve
        pause 3
        $ renpy.full_restart()
    else:
        play music orccamp fadeout 2.0 fadein 2.0
        $ Sabia.face = "normal"
        show Sabia at left
        "The third bandit defeated and fleeing, Sabia turned to Maply."
        $ Sabia.face = "happy3"
        pause(0.01)
        show maply 1 at right
        show maplyemo normal at right
        with moveinright
        s "Well! I guess you're much safer with him than I thought you were."
        show maplyemo happy
        maply "I told you he was a good boy!"
        $ Sabia.face = "normal"
        "The hound was sniffing at the ground, several meters away from Sabia and Maply, prowling the perimeter."
        $ Sabia.face = "pout1"
        s "These bandits are beginning to become a bigger problem. And it sounds like they're going to be pushing harder in the future... we should head back now."
        show maplyemo normalopen
        maply "That's a good idea Saby. We've gone so far though! I think we're past the Arena..."
        $ Sabia.face = "normalopen"
        s "That's alright. I don't think we'll need to worry about any more ambushes, not with your friend around."
        show maplyemo happy
        maply "Ehehe you're probably right, Saby."
        show maplyemo normal
        $ Sabia.face = "normalopen"
        s "Hopefully, the hunt plus all the unexpected excitement is enough to temper his attitude a little bit. But only time will tell."
        show maplyemo normal
        maply "I hope so too..."
        hide Sabia
        hide maply
        hide maplyemo
        with dissolve
        "The journey back through the forest to Grok og Dar was uneventful. The hound stayed close to Maply, and Sabia followed a few steps behind."
        "Maply, although still a little shaken from the bandit attack seemed in higher spirits, sure that the hound would behave now, and wouldn't receive any more punishments or poor treatments."
        "Sabia knew she'd have to check in with Maply later."
        jump lowerorccamp


label maply_hellhound_quest7:
    scene bg countryside
    call sabiabase
    with dissolve
    "As Sabia passed the gates to the camp outskirts, she saw a red streak dashing this way and that. Maply standing with a forlorn look etched on her face, watching the hound play."
    show maply 1 at right
    show maplyemo sad1 at right
    with dissolve
    maply "Hello Saby..."
    show sabiaemo normalopen at left
    s "What's wrong, Maply?"
    show sabiaemo normal at left
    "Maply drew some squiggles in the dirt on the ground with a stick she held, before answering."
    show maplyemo sad2
    maply "Gorbek said that he wasn't good again last night, Saby. I thought the hunt would have worked - even without the bandits!"
    maply "And Gorbek didn't even tell him he was good for fighting off bandits!"
    maply "He just grunted."
    show maplyemo sad1
    show sabiaemo sad1
    s "I'm sorry Maply... I'm not sure what else we could try. I'm not an expert in hounds, let alone orcish hellhounds..."
    show maplyemo sad2
    maply "That's ok Saby."
    show maplyemo happy
    maply "You've tried so much and been really helpful, and most other people wouldn't have bothered to help me with something they think is so small!"
    show maplyemo sad2
    maply "But I think we'll just go to the Arena and play a little bit."
    maply "He was so good yesterday! He deserves at least some fun and reward, right?"
    show maplyemo normal
    show sabiaemo normalopen
    s "Of course he does! Let's go, then."
    show maplyemo normalopen
    maply "That's ok Saby. I wanted to go just the two of us today. You've helped so much and I know you're busy with other stuff!"
    show sabiaemo irritated1
    s "Are you sure that's a good idea with bandits around?"
    show maplyemo happy
    maply "Don't be so silly Saby! I think I'll be safe with him after yesterday!"
    show maplyemo normal
    show sabiaemo pout1
    s "I... yeah. That's a good point. Alright then, well, have fun. But do be careful just in case."
    show sabiaemo normal
    show maplyemo normalopen
    maply "Sure Saby. Thanks again for all your help. Come on, let's go!"
    "The hound's ears twitched, and it swiveled on the spot, bounding towards Maply."
    "It was at her side almost in an instant, and the two started their walk to the still-empty Arena."
    hide maply
    hide maplyemo
    with dissolve
    if hellhoundchoice == "sub":
        show sabiaemo eyebrow1
        s "(I have a feeling I know what the 'play' might be...)"
        show sabiaemo closed2
        s "(But I do still hope she's careful, even with the hound there.)"
    else:
        show sabiaemo closed2
        s "(I hope she's still careful, even if she does have the hound with her...)"
    scene bg black
    with dissolve
    pause (0.25)
    scene bg arenahound
    with dissolve
    pause (0.1)
    show maply 1 at right
    show maplyemo normal at right
    with dissolve
    "Like yesterday, as they traveled the hound made sure to stay near to Maply, and before long they found themselves in the Arena."
    show maplyemo sad2
    maply "You were so brave yesterday, getting rid of {i}both{/i} of those bandits! All by yourself!"
    maply "And big mean Gorbek didn't even tell you you did a good job."
    show maplyemo sad1
    "She spent a few minutes watching as the hound enjoyed the freedom to run around, circling about the Arena a few times."
    "Every now and then, he stopped, and sniffed at something only he could smell, before running back to Maply, to check she was still ok."
    show maplyemo normalopen
    maply "Aww... you're so sweet. Always making sure I'm ok!"
    show maplyemo normal
    "Maply fell to the sandy floor on her knees, and wrapped her arms around the hound."
    show maplyemo sad2
    maply "I just wish you would be good at the kennels! Then you wouldn't-"
    show maplyemo happy
    maply "Eehehe, that tickles!"
    "The hound had started to lick at Maply. Not just a friendly, happy lick."
    "There was a little more to it, and there was a low rumbling in his belly as he inched closer, licking and sniffing at Maply."
    show maplyemo surprise1
    "His tongue moved a bit lower, lapping between Maply's legs, running along the catgirl's svelte thighs."
    show maplyblush at right
    maply "O... oh. I... I see! You like me more than just friends?"
    "The hound barked loudly, looking up at Maply's eyes with its own."
    show maplyemo eyebrows
    maply "Uhhm... well. You {i}were{/i} really brave and saved me yesterday... and you definitely deserve a reward."
    show maplyemo normal
    maply "Is this why you've been acting out...? Because you want... want a mate?"
    "Again, the hound barked loudly, before pushing his snout up into Maply's arms, lapping at her face."
    show maplyemo normal
    "Maply stood up, and giggled, smiling down at the hound. She wasn't exactly sure about this, but..."
    maply "Ok then...! Why not? You deserve a reward, and you're nice and sweet and so brave!"
    show maply 1n with dissolve
    "Her head turned about, following the hound as it circled her while she undressed, watching, and waiting almost patiently."
    call MaplyHellhound
    play music orccamp fadeout 2.0 fadein 2.0
    $ GenericOrc1.extras = ["Loincloth", "Shoulder", "Wrap", "Strap"]
    $ GenericOrc1.face = "smile1"
    scene bg black with dissolve
    pause (0.1)
    scene bg kennels
    call sabiabase
    show GenericOrc1 at right
    with dissolve
    gorbek "Little catgirl brought hound back earlier in day, Sabia!"
    gorbek "Gorbek not sure what she did - but he has been acting like his old self!"
    gorbek "Took food nicely, not trying to bite Gorbek, even let me clean cage and not try to snap at Gorbek!"
    $ GenericOrc1.face = "normal"
    show sabiaemo happy1
    s "Great! So I can buy him now, then?"
    show sabiaemo annoyed2
    $ GenericOrc1.face = "smile1"
    gorbek "Hahahaha! Oh, Sabia serious?"
    show sabiaemo normal
    gorbek "Can't sell with just one day of good behavior. Gorbek keep him for now, but if he stays good and doesn't act out again, then maybe Gorbek and Sabia can discuss deal."
    $ GenericOrc1.face = "normal"
    gorbek "But maybe catgirl should keep coming around, make sure hound doesn't slide back."
    $ GenericOrc1.face = "smile1"
    gorbek "If he stays good, maybe Gorbek get catgirl to train all the hounds, hahahahah!"
    $ GenericOrc1.face = "normal"
    show sabiaemo annoyed1
    s "...right. Well, as long as you're not going to do anything-"
    show sabiaemo normal
    gorbek "Don't worry about that. Gorbek won't do anything if hound keeps being good - no problem now!"
    gorbek "But Gorbek have work to do for now!"
    hide GenericOrc1 with moveoutright
    s "(Well, that's another issue out of the way now, thankfully. I should go check with Maply at some point, though.)"
    jump lowerorccamp


label maply_hellhound_quest_end:
    call sabiabase
    show maply 1 at right
    show maplyemo happy at right
    maply "Hey Saby! Did you hear?!"
    show sabiaemo happy1
    s "I did. Gorbek said the hound was behaving fantastically!"
    s "How'd you get him to stop being aggressive?"
    maply "...eheheh, I'm not sure! He just started being good I guess!"
    show maplyemo normal
    if hellhoundchoice == "sub":
        show sabiaemo happy2
        s "He just 'started being good' did he? Isn't that interesting... I wonder why he did that?"
        show sabiaemo eyebrow1
        s "There wasn't anything else that went on?"
        show maplyblush at right
        show maplyemo normalopen
        maply "I dunno! I guess he just needed a little more play!"
        show maplyemo normal
        s "Hmmm..."
        hide maplyblush
    if maplybefriended == False:
        $ maplybefriended = True
        show sabiaemo normalopen
        s "...I suppose I was wrong about you as well."
        show sabiaemo normal
        show maplyemo normalopen
        maply "What do you mean Saby?"
        show sabiaemo normalopen
        "When we... captured you. I thought you were heartless and-"
        show maplyemo happy
        maply "That's ok Saby. That's in the past, we're friends now!"
        show sabiaemo closed2
        s "..."
        show sabiaemo happy1
        s "We are. Thanks, Maply."
        maply "Of course Saby!"
    show sabiaemo normalopen
    show maplyemo normal
    s "We'll look at trying to buy him from Gorbek in the future."
    s "We can't buy him yet, apparently - not until Gorbek judges that the hound's back to its old self for good."
    show maplyemo sad2
    maply "I know. He told me the same thing."
    show maplyemo happy
    maply "I'll be visiting him a lot though, and taking him out to play. Make sure he has a lot of fun and doesn't get bored cooped up there!"
    if hellhoundchoice == "sub":
        show sabiaemo normalopen
        s "Just play?"
        show maplyblush at right
        maply "Yes! What else do you think we'd do?"
        show sabiaemo normalopen
        s "Hunting?"
        show sabiaemo normal
        hide maplyblush
        show maplyemo happy
        maply "Oh yeah, hunting too... eheheh!"
    show sabiaemo happy1
    s "Well, I'm glad that so far it's turned out well."
    s "But I've no lack of other tasks to see to, Maply."
    maply "Thanks so much Saby. Again."
    "Before Sabia could leave, Maply practically pounced on her, and gave her a tight hug, ears twitching and tail whipping about happily."
    "After a minute, Maply relinquished her grip and Sabia was able to leave."
    jump orcoutskirts2
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
