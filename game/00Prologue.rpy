


label prologue:
    show expression "opening/opening0.jpg" with dissolve
    pause 1
    show expression "opening/opening1.jpg" with dissolve
    $ renpy.pause ()
    show expression "opening/opening2.jpg" with dissolve
    $ renpy.pause ()
    show expression "opening/opening3.jpg" with dissolve
    $ renpy.pause ()
    play music forest fadeout 2.0 fadein 2.0
    scene bg forest2
    with dissolve
    call sabiabase
    with dissolve
    show sabiaemo angry1 at left
    s "That's far enough! Report, men!"
    show humansoldier normal at right
    with moveinright
    show sabiaemo normal at left
    soldier "We're getting close to the ruins, Commander Dufuor. We can make it there tonight if we double march."
    s "What do our scouts say about the region?"
    soldier "The path is surprisingly bad for ancient human lands, but we shouldn't have a problem following it."
    s "And the surrounding forests?"
    show humansoldier sad at right
    soldier "..."
    show sabiaemo annoyed1 at left
    s "I'm asking you for a full report, soldier. You {i}did{/i} send out thorough scouting parties like I ordered, right?"
    soldier "..."
    show sabiaemo annoyed2 at left
    s "Unbelievable. When we get back I'll have you all written up for demerits."
    show humansoldier sad at right
    soldier "C-commander! Please, there's no need for such extensive scouting. This part of Lundar is almost empty after the war - even if one of the lesser races could organize a raiding party, they'd never come here."
    show sabiaemo angry1 at left
    s "Do you really think Archmage Lynn Dufuor would ask her own sister to secure a ruin if it wasn't critically important? This isn't the time to get sloppy!"
    show humansoldier angry at right
    soldier "But Commander... it's a struggle to motivate the men when they don't even know why we're out here. We won the war, we need to stabilize our control, not... wander off like this."
    show sabiaemo angry2 at left
    s "That's not for you to know, soldier. If you can't obey orders, I'll replace you with someone who can."
    show humansoldier normal at right
    soldier "...yes, Commander."
    show sabiaemo normal at left
    s "Send the scouting parties I ordered immediately. I don't like this terrain, and I think I've seen signs of recent activity."
    soldier "Surely just some orc mongrels fleeing our armies."
    show sabiaemo annoyed2 at left
    s "(I can't believe I'm left with these people. I had to prioritize loyalty over competence due to the nature of this mission, but still...)"
    s "(I wish I hadn't sent so many of my men to the Obsidian Ridge and the Icemark. With my veterans I wouldn't have to deal with this shit. We'd probably be back already.)"
    show sabiaemo normal at left
    s "Maybe, but something about this feels wrong to me. Let's take two days to reach the ruins and do this right."
    soldier "As you command, then. I'll go order th-"
    show sabiaemo irritated1 at left
    "At that moment screams echoed in the forest. Sabia snapped to attention, searching for the source, while the soldier hastily dropped into a defensive position."
    show humansoldier surprised at right
    soldier "Wait... what's that?"
    soldier "Gyaaah!"
    hide humansoldier
    with dissolve
    scene bg forest3
    call sabiabase from _call_sabiabase_12
    show sabiaemo surprised2 at left
    with dissolve
    s "(An orc! No, there's more than one!)"
    show orcbase at right
    show orcloincloth at right
    show orcaxe at right
    show orcnecklace at right
    show orcemo normal at right
    with moveinright
    show sabiaemo angry2 at left
    s "(Shit, I should have immediately assumed these idiots couldn't follow orders. Now I'm surrounded...)"
    show sabiaemo angry1 at left
    s "That's far enough, scum!"
    show orcemo smile1 at right
    orc "Huhu... puny human... we gonna kill ya."
    show sabiaemo angry2 at left
    s "Exactly what I would expect from your kind. But do you really think you can face me?"
    show orcemo normal at right
    orc "We watched you. You yell a lot, but you don't fight."
    s "That's where you're wrong, orc. I'm more than a match for all of you!"
    show sabiaemo irritated1 at left
    s "(Bluffing will only get me so far. I'm certain I could kill any one of them in combat, but they'll just gang up on me like the cowards they are.)"
    s "(My only hope is if some of my soldiers survived. I need to buy time, but I have to play this carefully...)"
    menu startneg1:
        "Attack an orc":
            $ startnegtime += 1
            show sabiaemo normal at left
            jump startnegfight
        "Reason with them":
            $ startnegtime += 1
            show sabiaemo normal at left
            s "What do you think you can accomplish? You're already dangerously close to human territory, your fates are sealed."
            show orcemo smile1 at right
            orc "Don't think so. Humans don't care about this place. We kill you, go back - easy!"
            s "I know it's hard for you, but think for a second! No one cares that you're here now, but if you so much as touch a hair on my head, the entire Lundar army will hunt you down!"
            show orcemo normal at right
            "One of the orcs laughed and started to say something, but another orc cuffed him on the side of the head. The biggest of them stared at Sabia for a moment, then shook his head."
            show orcemo angry at right
            orc "Liar. We know your kind - if we let you go now, you bring more humans to kill us, no matter what."
            "Sabia thought about contradicting him, but she saw the hatred in his eyes. Besides, it was true. If she managed to escape, she'd have each of these orcs captured and flayed alive in front of her."
            "The orcs were beginning to crowd closer. Sweat trickled down the back of Sabia's neck as she felt them preparing to attack. She'd bought a little time, but she was running out of it."
            jump startneg2
        "Stay in defensive position":
            show sabiaemo angry2 at left
            "Sabia kept her sword ready and glared, hoping that she could intimidate the orcs into hesitating. To her surprise, they began advancing on her almost immediately, eyes burning with rage."
            show sabiaemo surprised3 at left
            s "W-wait! I'll kill the first one that gets near!"
            orc "Maybe you'll get one. And then we'll get you."
            show sabiaemo angry2 at left
            s "Tch!"
            "The orcs were beginning to crowd closer. Sweat trickled down the back of Sabia's neck as she felt them preparing to attack. She'd bought a little time, but she was running out of it."
            jump startneg2
        "Run away" if startnegrun == False:
            $ startnegrun = True
            $ startnegtime += 1
            show sabiaemo normal at left
            "Sabia did her best to flee, but didn't get far into the trees before more orcs showed up to block her path. Chuckling, they herded her back to the clearing."
            jump startneg1
    menu startneg2:
        "Break through their circle":
            show sabiaemo normal at left
            "Sabia feinted at one orc, then tried to leap between him and another."
            "To her horror, the orcs lunged after her, catching her arm. She tumbled to the ground and in an instant the orcs were upon her, raising bloody weapons."
            jump startnegbang
        "Attack an orc":
            $ startnegtime += 1
            show sabiaemo normal at left
            jump startnegfight
        "Bluff them" if startnegbluff == False:
            $ startnegbluff = True
            if startnegplead == True:
                "Though Sabia had an idea for a bluff, she realized that it would be useless. After seeing her plead, the orcs were losing any fear of her."
                jump startneg2
            $ startnegtime += 1
            "Sabia slipped one hand into her cloak and pretended to grip something."
            show sabiaemo angry1 at left
            s "I didn't want to use this, but you leave me no choice: get any closer and I'll kill us all."
            show orcemo suspicious at right
            "Some orcs cringed and some sneered, but they all hesitated a moment. Sabia gave them her best smirk."
            show sabiaemo happy2 at left
            s "Maybe your pathetic shamans can't manage it, but human mages can create potions that wreak terrible destruction. All I have to do is drop this..."
            "Abruptly one of the orcs gave a loud growl and took a step closer."
            show orcemo angry at right
            orc "Liar. If you had such a weapon, we would have been told."
            show sabiaemo irritated2 at left
            "Sabia's eyes narrowed, not understanding what he could mean. But it seemed like the statement broke her bluff, leaving her surrounded by the orcs with even fewer options."
            jump startneg2
        "Plead with them" if startnegplead == False:
            $ startnegplead = True
            $ startnegtime += 1
            $ L_orcs -= 1
            $ sub += 1
            "Though she couldn't bring herself to beg, Sabia realized that her only hope of survival might be enduring the orcs, not escaping them. She shifted to a less aggressive stance."
            show sabiaemo sad1 at left
            s "Why do you have to kill me? What good does that do?"
            orc "What good does keeping you alive do?"
            show sabiaemo angry1 at left
            s "Don't be stupid. I'm a noble, I have a lot of information you need."
            "Another orc gave a loud growl and shook his head. After a brief, guttural discussion, they turned back to her with dark looks. No luck, then, but at least she had gained a little time."
            jump startneg2
        "Surrender to the orcs" if startnegsubmit == False:
            $ startnegsubmit = True
            $ sub += 1
            show sabiaemo sad1 at left
            s "(Perhaps fighting is useless...)"
            jump startneg2


label startnegfight:
    $ L_orcs += 1
    show sabiaemo angry2 at left
    "Sabia struck out at the first orc to move incautiously. Her sword, edge honed by magic, easily swiped through the orc's neck."
    call shake ("h")
    "But even as that orc fell, two others were striking at her. Sabia managed to dodge one club, but the second sent her sprawling to the ground."
    call shake ("v")
    show sabiaemo sad1 at left
    "The blow left her stunned, but worst of all it sent her sword falling out of arm's reach. Sabia struggled to get up, but it was too late: the orcs descended on her."
    jump startnegbang


label startnegbang:
    "Sabia realized that there was nowhere to retreat and fighting would soon become impossible."
    menu:
        "One last hit":
            $ dom += 1
            $ sub -= 1
            show sabiaemo angry2 at left
            "As her sword was knocked away, Sabia fought on with her fists, but she couldn't overpower the stronger orcs."
        "Surrender":
            $ sub += 1
            $ dom -= 1
            show sabiaemo sad1 at left
            "Not going for her sword, Sabia didn't fight back and instead hoped they would spare her life."
    if startnegtime >= 2:
        pass
    else:
        $ startcondition = "gangbang"
    scene bg forest3
    with dissolve
    if startcondition == "gangbang":
        "Just when Sabia gave up and accepted that she'd be killed, there was a roar and new forces struck them from behind."
    else:
        "Just when Sabia thought the orcs would slay her, there was a roar and new forces struck them from behind. She had delayed long enough."
    call sabiabase
    "She jerked to her feet, eyes darting to take in the situation."
    "All around the clearing, the orcs were being killed or captured... by other orcs. The new band looked every bit as disgusting to her, but they quickly gained the advantage."
    scene bg forest3
    call sabiabase
    show lutvrogbase at right
    show lutvrogaxe at right
    show lutvrogwraps at right
    show lutvrogwrists at right
    show lutvrogemo normal at right
    show orcbase2 at center
    show orcloincloth2 at center
    show orchelmet2 at center
    show orcpiercing2 at center
    show orcshoulder2 at center
    show orcstrap2 at center
    show orcwrap2 at center
    show orcbeard21 at center
    show orcemo2 angry at center
    with dissolve
    "Two of the orcs approached her. The first looked angry, while the second hung back with a watchful look."
    orc "What are you doing here, human?"
    s "..."
    menu:
        "Give a short answer":
            s "We were traveling to find some important records from before the war."
            show orcemo2 suspicious at center
            orc "Records from these barren lands?"
            show sabiaemo irritated2 at left
            s "Humans had settled most of these lands before your kind came, orc."
            show orcemo2 normal at center
            "After staring at her a moment, the leader simply shook his head."
        "Tell a lie":
            $ startnegmood -= 1
            s "We were patrolling Lundar when we came under attack for no reason."
            show orcemo2 normal at center
            "The orcs watched her with neutral expressions. Sabia found herself uncomfortable, unable to read what was in their dark eyes. After a moment, the lead orc shook his head."
        "Insult them":
            $ startnegmood -= 1
            $ L_orcs -= 1
            show sabiaemo angry2 at left
            s "Why should I answer filthy orc scum?"
            "This seemed to make the orcs slightly annoyed and the leader shook his head."
        "Say nothing":
            show sabiaemo irritated1 at left
            "Sabia gave them both an icy stare and refused to answer. They waited for a moment, then the leader shook his head."
    orc "The Warchief commanded us to stay out of human lands. The orcs who attacked you are traitors for willfully disobeying his order."
    show lutvrogemo suspicious at right
    quietorc "But for what reason?"
    show orcemo2 normal at center
    orc "Doesn't matter, Lutvrog. Our job is to bring them back. That is all."
    "Their attention turned back to her and Sabia watched them nervously. She doubted their words meant anything - orcs were orcs - but maybe she could use this in some way."
    orc "The problem is you. We have no orders about human women. This is a problem."
    if startcondition == "gangbang":
        "Sabia wanted to argue with them, but as her adrenaline wore off, she found her knees weakening. The previous conflict had exhausted her... Sabia crumpled to the ground in darkness."
        jump introNeve
    else:
        "Sabia froze as she realized that she had a chance. This orc was thinking of killing her, but unlike the others, he hadn't promised it. Perhaps she had a chance to keep herself alive..."
    menu startneg3:
        "Listen to them talk" if startnegtalk == False:
            $ startnegtalk = True
            $ startnegmood += 1
            if startnegbluff:
                orc "Do you think she actually has magic that can burn everything?"
                show lutvrogemo suspicious at right
                quietorc "Lutvrog is certain it was a bluff."
                show orcemo2 angry at center
                orc "Hmph."
            quietorc "She might be able to tell us something about what happened."
            show orcemo2 normal at center
            orc "Maybe. But it's not worth taking her back. She'll just try to escape."
            show lutvrogemo normal at right
            quietorc "..."
            show orcemo2 angry at center
            orc "Hmph. Didn't want to make any decisions today..."
            jump startneg3
        "Ask about them" if startnegask == False:
            $ startnegask = True
            $ startnegmood += 1
            s "What exactly are you doing? Orcs don't stay out of human lands, you raid all the time."
            show orcemo2 normal at center
            orc "Maybe others do. But those who follow Warchief Groknak are commanded not to waste their strength against Lundar."
            show sabiaemo irritated2 at left
            s "How many does this Warchief command? Are you trying to form another horde?"
            orc "...you are still our enemy, human. We tell you nothing."
            jump startneg3
        "Ask about rogue orcs" if startnegrogue == False:
            $ startnegrogue = True
            $ startnegmood += 1
            show sabiaemo irritated2 at left
            s "Why kill the orcs who attacked me?"
            show orcemo2 normal at center
            orc "They proved themselves traitors by disobeying the Warchief. And cowards, so many fighting against a single human woman."
            show sabiaemo normal at left
            s "..."
            orc "You humans might not care about honorable combat. But to those who keep the old ways, honor still means something."
            jump startneg3
        "Jump for your sword":
            $ startcondition = "unconscious"
            show sabiaemo angry2 at left
            "Sabia lunged away from them, grabbing for her sword."
            "To her shock, the quiet orc moved almost as fast as she could. From his superior position, he managed to pick up the sword before she could... and then handed it to her."
            hide orcbase2 at center
            hide orcloincloth2 at center
            hide orchelmet2 at center
            hide orcpiercing2 at center
            hide orcshoulder2 at center
            hide orcstrap2 at center
            hide orcwrap2 at center
            hide orcbeard21 at center
            hide orcemo2 angry at center
            with dissolve
            show lutvrogbase at center
            show lutvrogaxe at center
            show lutvrogwraps at center
            show lutvrogwrists at center
            show lutvrogemo normal at center
            with moveinright
            quietorc "So you have chosen violence."
            lut "Very well. The name of the one who will defeat you is Lutvrog."
            show sabiaemo angry1 at left
            s "I can't care about your name, orc!"
            scene bg forestF
            $ enemy_level = 10
            $ enemy_maxhp = 800
            $ enemy_hp = 800
            $ enemy_attack = 120
            $ enemy_defense = 120
            $ enemy_magdefense = 50
            $ enemy_type = 1
            $ enemy_skills = [Enemyattack]
            $ player = Sabia
            $ enemy = Lutvrog
            call duel
            $ Sabia.xp +=1
            play music forest fadeout 2.0 fadein 2.0
            scene bg forest3
            call sabiabase
            show lutvrogbase at right
            show lutvrogaxe at right
            show lutvrogwraps at right
            show lutvrogwrists at right
            show lutvrogemo normal at right
            with dissolve
            "Another heavy blow struck Sabia in the head. Her sword dropped from her fingers and her body followed it to the ground as the darkness overwhelmed her..."
            jump introNeve
        "Suggest a duel" if startnegmood >= 2:
            s "You keep going on and on about honor. Then why is it all of you against me?"
            show orcemo2 angry at center
            orc "Humans have no honor. You always slaughter us with superior numbers."
            show sabiaemo annoyed2 at left
            s "(That's called strategy, you dumb brute.)"
            show sabiaemo angry2 at left
            s "But I'm not doing anything like that now. We were traveling peacefully and traitors from your group attacked us!"
            if startnegplead == True:
                show orcemo2 normal at center
                orc "Hmph. You're just begging for your life. We heard you pleading with them earlier."
                orc "You'll say anything to survive. It isn't even worthwhile to speak of your honor."
                "Sabia started to protest, but without warning a heavy blow caught her from behind. She fell to the ground as the darkness overwhelmed her..."
                jump introNeve
            else:
                $ L_orcs += 1
                $ A_lutvrog += 2
                show orcemo2 normal at center
                orc "Hmph. You're just saying what you think will help you survive. You can have no honor when you risk nothing."
                s "Risk nothing? With all of you threatening to kill me?"
                orc "The war may be over, but this is still war to us."
                show sabiaemo normal at left
                s "..."
                s "(If I can use their ridiculous 'honor' against them, maybe I still have a way out of this. One on one, none of them stand a chance.)"
                s "You want me to risk something? Fine. Here's my deal:"
                s "If you have any honor, fight me. One on one, no tricks or numbers. If I win, you have to let me go without harming me."
                s "If I lose, you brutes can have all my equipment. It's enchanted and quite valuable."
                orc "...hunh."
                show orcemo2 smile1 at center
                orc "Well, that would solve both our problems. But how do we know you'll keep your word once you lose?"
                show sabiaemo angry1 at left
                s "Insolent little...!"
                show sabiaemo annoyed1 at left
                s "You're pretty confident you'll win. Well, so am I. If your honor is worth anything, take the challenge! Or are you going to just overwhelm me with numbers like you mocked us for?"
                orc "Hmph. It's in your hands, Lutvrog."
                hide orcbase2 at center
                hide orcloincloth2 at center
                hide orchelmet2 at center
                hide orcpiercing2 at center
                hide orcshoulder2 at center
                hide orcstrap2 at center
                hide orcwrap2 at center
                hide orcbeard21 at center
                hide orcemo2 angry at center
                with dissolve
                lut "My name is Lutvrog. Lutvrog hopes you provide him with an honorable duel."
                s "I can't care about your name, orc!"
                lut "Very well, then. Let us simply do battle. I will give you time to retrieve your equipment."
                scene bg forestF
                $ enemy_level = 10
                $ enemy_maxhp = 800
                $ enemy_hp = 800
                $ enemy_attack = 120
                $ enemy_defense = 120
                $ enemy_magdefense = 52
                $ enemy_type = 1
                $ enemy_skills = [Enemyattack]
                $ player = Sabia
                $ enemy = Lutvrog
                call duel
                $ Sabia.xp +=2
                play music forest fadeout 2.0 fadein 2.0
                scene bg forest3
                call sabiabase
                show lutvrogbase at right
                show lutvrogaxe at right
                show lutvrogwraps at right
                show lutvrogwrists at right
                show lutvrogemo normal at right
                with dissolve
                "Sabia staggered backward, her stinging hands clutching nothing as her sword was flung away."
                show sabiaemo sad1 at left
                "She hadn't just lost, she had been utterly overwhelmed. Instead of hacking wildly, the orc used a surprisingly subtle style to drain her stamina and leave her exhausted."
                show lutvrogemo happy at right
                lut "An interesting battle. Lutvrog has not encountered such a style among humans before."
                show sabiaemo irritated2 at left
                s "Huh? You beat me, then praise my fighting?"
                show lutvrogemo normal at right
                lut "Talk, but the others are not so patient. If you have any honor at all, you will keep your word."
                show sabiaemo surprised2 at left
                s "Wait, aren't you the one who won my armor?"
                hide lutvrogbase at right
                hide lutvrogaxe at right
                hide lutvrogwraps at right
                hide lutvrogwrists at right
                hide lutvrogemo normal at right
                with moveoutright
                "Instead of answering, Lutvrog turned and walked away. Sabia gaped after him, not sure that she could believe it. And almost insulted, in a way."
                show orcbase2 at center
                show orcloincloth2 at center
                show orchelmet2 at center
                show orcpiercing2 at center
                show orcshoulder2 at center
                show orcstrap2 at center
                show orcwrap2 at center
                show orcbeard21 at center
                show orcemo2 smile1 at center
                with dissolve
                "While she still gaped, the other orc came up behind her and struck her on the back of the head, sending her tumbling into darkness..."
                $ startcondition = "sex"
                jump introNeve


label introNeve:
    $ Sabia.unequip(Originalarmor)
    $ Sabia.unequip(Originalsword)
    $ Sabia.equip(Rags)
    $ Sabia.recoverhp()
    $ Sabia.stamina = 100
    $ a_list.append("Lutvrog")
    $ a_list.append("Neve")
    stop music fadeout 10.0
    scene bg black
    "..."
    scene bg tent
    play music orccamp fadeout 2.0 fadein 2.0 
    "Everything faded in around her slowly. First her own heartbeat, then a painful ache on the back of her head, then the sight of a tent around her."
    "Someone had taken her armor and weapons. Though she was just on a cot with a thin blanket, it was actually fairly comfortable."
    call sabiabase from _call_sabiabase_9
    show sabiaemo angry2 at left
    s "(Ugh... someone cleaned me up, but my head is aching. I barely remember getting carried back to their camp.)"
    show neve1 at right
    show neveemo normal at right
    with dissolve
    n "Oh, hey, you're up. You're tougher than you look."
    show sabiaemo surprised2 at left
    s "An elf? What's going on?"
    show neveemo happy1 at right
    n "That's what I'm here to explain! Well, and they also asked me to clean you up, didn't want you attacking them when you woke."
    show neveemo normal at right
    n "This is the clan of Warchief Groknak. The orcs that attacked you were a few traitors who broke his laws."
    show sabiaemo angry1 at left
    s "A likely story. Does this 'Warchief' really think the Kingdom of Lundar will buy that?"
    show sabiaemo irritated2 at left
    show neveemo happy3 at right
    n "Heh, you think he's trying to get away with raiding by blaming traitors? He's no fool, he knows Lundar would crush him for that."
    show neveemo normal at right
    n "No, his strategy has been to stay far away and avoid attention. That's why he forbade any of his warriors from getting near Lundar."
    show sabiaemo normal at left
    s "Well... I guess since I'm not enslaved right now, I should hear you out."
    n "Groknak says the tribe is dishonored by the traitors, so in exchange he will allow you to return to human lands unharmed."
    show neveemo happy3 at right
    n "Though I should point out that he's just upset about the tactics they used and the way they ganged up on you."
    show sabiaemo annoyed2 at left
    s "I guess I shouldn't expect orcs to be any more logical than that. So I can just leave?"
    show neveemo happy1 at right
    n "That's right, they also hired me to take you safely wherever you want to go."
    n "My advice would be to get out quick, but you might want to stay to see some of the traitors tried and executed."
    show sabiaemo surprised2 at left
    s "Tried? Orcs have trials?"
    show neveemo happy3 at right
    n "What, you think they resolve all conflicts just by fighting each other?"
    show neveemo happy1 at right
    n "Now, the traitors are obviously going to be found guilty and executed. But there are some others who were involved in the whole business who might die too - they made contact, accepted payment, that kind of thing."
    show sabiaemo irritated1 at left
    s "Wait... accepted payment?"
    n "Even orcs aren't going to risk their lives on an attack like this without reason. No, the trials so far have proved that someone hired them."
    s "To attack humans? Or me specifically?"
    n "I've gotten the sense it was you specifically, but we don't know a lot. The only other detail the traitors agreed on was that the one hiring them was a mage with purple hair."
    show sabiaemo surprised2 at left
    s "What?"
    show neveemo happy3 at right
    n "Oh ho! Someone you know?"
    show sabiaemo irritated1 at left
    s "..."
    show neveemo normal at right
    s "(It has to be Lynn... so you finally made your move, did you, sister? I never imagined that it would be through orcs... that's probably exactly why you used such an unorthodox tactic.)"
    s "(There are two main questions now. Who all was involved? And why now? Was I going to find something Lynn wanted to keep secret in those ruins? Or was it just a convenient way to isolate me?)"
    s "(You'll pay for this, Lynn! As soon as I get back to Lundar... if Mother doesn't flay you alive, I will!)"
    n "You seem lost in thought."
    show sabiaemo normal at left
    s "This... complicates things."
    n "Well, that's none of my business - I try not to get involved in anyone's politics. You want to watch the trials, or should I escort you somewhere?"
    show sabiaemo irritated1 at left
    s "I don't give a shit what happens to a bunch of orcs. I need to get back to Lundar as soon as possible."
    show neveemo happy1 at right
    n "Fine with me. Where to?"
    show sabiaemo normal at left
    s "Let me see... where are we now?"
    n "I left you a large map, but it's lacking in local detail. To actually see this area in meaningful detail..."
    show expression "maps/region1.jpg" as map
    "Neve unrolled a map on a low table. It actually looked pretty accurate, so it couldn't be from the orcs."
    show expression "maps/region1b.jpg" as map
    n "This covers the whole region... the orc camp is down here."
    show expression "maps/region1c.jpg" as map
    s "Hmm. To the northwest there's an incorporated territory that wants to join Lundar. I know the governor there, he should be on my side."
    hide map
    n "Off we go, then!"
    scene bg black
    "..."
    scene bg road2
    call sabiabase from _call_sabiabase_10
    show neve1 at right
    show neveemo happy1 at right
    with dissolve
    n "Alright, here we are. Looks like a rough day, but I assume you can make it from here?"
    show sabiaemo surprised3 at left
    s "A rough d- I can literally see wagons burning in the distance!"
    n "Bandits. They're a big problem in this area."
    show sabiaemo angry1 at left
    s "Impossible! I inspected the territory personally when it applied for entry to Lundar, it was..."
    show sabiaemo sad1 at left
    s "..."
    show sabiaemo normal at left
    s "Maybe this goes deeper than I thought. Tell me, what race are most of the bandits?"
    show neveemo smirk1 at right
    n "Oh, almost all human. Your mercenary armies turned to banditry pretty much immediately after the war."
    s "I know that, but Governor Andian assured me it was under control."
    show sabiaemo irritated1 at left
    s "No doubt everything I was shown was just a ruse to make me think the territory was stable."
    s "But I asked Lynn to magically confirm, and she said it was fine... so she was planning to undermine me starting at least three months ago."
    show neveemo normal at right
    n "...well, I'll stay out of your business. What now?"
    show sabiaemo normal at left
    s "I doubt I could survive on roads like these without my equipment."
    n "Taken by the orcs, sorry."
    s "It doesn't matter. Even if I reached Governor Andian, he's probably working for my enemies. He'd just betray me again."
    show sabiaemo angry2 at left
    s "Shit... I don't see any way through this..."
    n "..."
    show neveemo happy2 at right
    n "It sounds to me like you've been betrayed by some people close to you. Out of options, huh?"
    show sabiaemo annoyed1 at left
    s "Don't mock me, elf."
    n "I'm not mocking, just trying to understand. Do you have any other allies you can contact?"
    show sabiaemo irritated1 at left
    s "...not anywhere near here. I've always relied on my family's connections, but since I was backstabbed by someone in my own family, it's difficult."
    n "And you want to get revenge on this person, yes?"
    s "Yes."
    show neveemo happy3 at right
    n "I think you have a short window of opportunity to find new allies among Groknak's tribe."
    show sabiaemo surprised2 at left
    s "Are you serious? A bunch of orcs?"
    n "Do you have other options?"
    show sabiaemo pout1 at left
    s "..."
    show neveemo normal at right
    n "The issue is this: the traitorous orcs weren't working alone. Someone in a position of authority had to be involved for them to make a connection with a human mage and strike that far away."
    n "Though they got caught, if the Warchief hadn't sent special scouts for this very purpose, they might have gotten away with it. The entire tribe is very tense about this."
    s "What does any of that have to do with me?"
    show neveemo happy1 at right
    n "Right now, you're a potential witness in the most important trial in recent memory. You have a bit of leverage you might be able to use to your advantage."
    show sabiaemo normal at left
    s "Hmmm... I wish I had other options, but there aren't many. What all will the trial involve?"
    n "Unfortunately, as a human you don't have any standing in the tribe. You can't be a witness."
    s "But you think I can get enough standing?"
    show sabiaemo annoyed2 at left
    s "This had better not end with me eating a human's heart or something."
    show neveemo happy3 at right
    n "Haha, never fear. If you go back and announce your intentions, the leaders involved will realize that they can use you in their conflicts. They'd be willing to help you in exchange for favors now."
    show sabiaemo normal at left
    s "Has this trial really thrown the tribe that off balance?"
    show neveemo happy1 at right
    n "Oh yes. You see, there are three Captains beneath the Warchief. They've always been at odds over the succession."
    show sabiaemo annoyed2 at left
    s "Well, that part sounds familiar."
    n "There are strong suspicions against one of the Captains. If the charges stick, he could be executed as a traitor as well."
    n "Obviously, he wants to prove the charges false and his enemies want him dead. They need any edge they can get - so even those who hate humans might be willing to work with you."
    show sabiaemo annoyed1 at left
    s "Ugh. I hate to get involved with this mess, but I'm not sure I have a choice."
    show neveemo normal at right
    n "So, back to camp?"
    show sabiaemo irritated1 at left
    s "Wait. What exactly is your role in all this?"
    n "Oh, I'm a neutral observer."
    s "Then why are you doing this? You didn't have to tell me any of that."
    show neveemo happy2 at right
    n "Let's just say I was a little impressed by what I heard about you. I'm not involved in your conflict either, but I wish you all the best."
    show neveemo normal at right
    n "But once we get back to camp, my duty is done. I'm happy to talk to you if you want, but don't expect any more favors."
    show sabiaemo happy3 at left
    s "That's fair. Thank you... what's your name, again?"
    show neveemo smirk1 at right
    n "Well, a human asking my name? Maybe I had you wrong..."
    show neveemo happy2 at right
    n "I'm Neve."
    show sabiaemo happy1 at left
    s "Comm... Sabia Dufuor. Just Sabia, at least for now."
    n "Then let's head back to camp, Sabia. You have a rough path ahead of you."
    scene bg black
    n "I'll leave you here, Sabia. Good luck."
    s "(I'd better work like my life depends on it. Because it does.)"
    jump lowerorccamp
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
