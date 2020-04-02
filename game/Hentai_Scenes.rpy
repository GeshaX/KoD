


init -1:
    $ beta_testing = False
    default h_scene = ""


init -1 python:
    def hentai_scene(scene_number, scene_name="None", effect="None"):
        if beta_testing == True:
            renpy.show("hentai_scene", what=Solid("#000000"))
            return
        global h_scene
        if scene_name != "None":
            h_scene = scene_name
        if effect != "None":
            renpy.transition(effect)
        if renpy.loadable("scenes/{} ({}).jpg".format(h_scene, scene_number)):
            renpy.show("hentai_scene", what=Image("scenes/{} ({}).jpg".format(h_scene, scene_number)))
        else:
            renpy.show("hentai_scene", what=Image("scenes/{} ({}).png".format(h_scene, scene_number)))


label sabiafirstbj:
    scene bg relieftents
    call sabiabase
    show orcbase at right
    show orcloincloth at right
    show orcemo normal at right
    with dissolve
    "When the hideous orc entered, Sabia found herself wincing. Was she really going to do this?"
    "She told herself she would do anything, but the idea of an orc having its way with her like that... no. She would let them use her, but not fuck her."
    "Awkwardly getting into position, Sabia tried to focus on the reward instead of what she was about to do."
    $ hentai_scene(1,"sabiafirstbj",dissolve)
    pause 1
    s "I'll use my hand, but nothing else, okay?"
    "The orc didn't seem happy, but didn't argue. All it really wanted was to unload the heavy cum from its balls, as quickly as it could."
    menu:
        "Get it over with quickly":
            $ dom += 1
            "If she was going to subject herself to this, Sabia decided that she might as well stay in charge."
            $ hentai_scene(3)
            "When the orc dropped its loincloth, its hideous green cock popped out at her. Sabia didn't like the look of the disgusting thing, but she could handle it if that was what she had to do."
        "Just let him have his way":
            $ sub += 1
            "Sabia decided that the easiest way to get through the ordeal was to stay uninvolved and just let the orc do whatever it wanted."
            $ hentai_scene(2)
            "When the orc dropped its loincloth, its hideous green cock popped out at her. The repulsive thing was intimidating, thick and throbbing straight in her face. Sabia thought she could put up with it for long enough if she had to."
    $ hentai_scene(4)
    "When the orc put a hand on her head, though, trying to push her face into its cock, Sabia wondered if she really could."
    orc "Well? Come on, do something!"
    s "Alright, alright!"
    $ hentai_scene(5)
    pause 1
    "Wishing she was anywhere else, doing anything else, Sabia hesitantly reached out and wrapped her fingers around the orc's cock. It felt even thicker than it looked, she couldn't really get her fingers around it."
    $ hentai_scene(6)
    "Avoiding eye contact, Sabia began to stroke her hand up and down the thick shaft. It felt so hard against her hand, and she could feel the large veins pressing against her."
    "Sabia gave a little shudder of revulsion as precum from the top of the orc's cock began to slide down its shaft. Her hand felt dirty, but it was easier to slide her hand along the shaft with her fingers so slick."
    $ hentai_scene(7)
    "Just when she was beginning to think she could finish off the orc with a quick handjob, it reached down and grasped her head with his second hand."
    orc "Too slow!"
    s "H-hey! Calm down before I-"
    $ hentai_scene(8)
    call shake ("h")
    "Whatever Sabia intended to threaten was cut off by the orc ramming its cock into her open mouth. As Sabia tried not to choke, it was the most she could do to brace herself and try to push away from the thick cock invading her mouth."
    $ hentai_scene(9)
    "Facing resistance, the orc stopped thrusting. It kept its cock inside her mouth, though, stretching her thick lips around its girth. That left her with no way to complain, but she gave the orc a vicious glare as she struggled against its grip."
    $ hentai_scene(10)
    "Without warning, the orc tugged on her head and swung its hips forward, ramming its cock into her throat. All Sabia could do was choke and groan as it fucked her face."
    "Now that it could make real use of her throat, the orc didn't hold back. It kept slamming its length into the tight hole, grunting in pleasure as her throat convulsed around its shaft."
    "All she could do was brace herself and try to catch an occasional gasp of breath. Blushing in humiliation, Sabia vowed to endure it."
    $ hentai_scene(11)
    "And then, on one thrust, the orc didn't pull out. Sabia looked down in surprise, not quite able to believe that such a thick shaft could fit in her mouth, much less her throat."
    $ hentai_scene(12)
    "But the orc just wasn't pulling out. Running out of air, Sabia desperately grabbed at the beast's hips, trying to pull herself away. Yet in her kneeling position, she had absolutely no chance against the orc's overwhelming strength."
    $ hentai_scene(13)
    "Her struggles slowed down as she started to get light-headed. The cock in her throat was cutting off all air, so deep she couldn't even bite down properly. Her vision was beginning to swim."
    $ hentai_scene(14)
    "Sabia's world retracted to the sensation of the thick shaft in her throat. She could feel every throb in the orc's veins, every detail of its cock as it shifted inside her."
    $ hentai_scene(15)
    "Finally, the orc pulled out with a satisfied grunt. Sabia was left gasping for breath, the heady rush of air almost making her fall again. The orc didn't leave her mouth free for long, though, pushing its cockhead back in."
    "Not wanting to endure another ordeal like the previous one, Sabia did her best to suck and lick the head in her mouth. It made the orc grunt and thrust a little slower for a while, giving her enough time to catch her breath."
    $ hentai_scene(16)
    "But soon, it began to thrust ruthlessly again. As her eyes rolled back in her head, Sabia did her best to endure it. She could feel the creature's pace getting erratic, surely it couldn't last long..."
    $ hentai_scene(17)
    call shake ("h")

    "The orc came deep in Sabia's throat, pumping its load of thick cum directly into her. It was a small comfort that she didn't have to taste it... at least at first."
    $ hentai_scene(18)
    "Soon the cum had filled her throat and reached her mouth, the musky scent going straight to her head. Lightheaded as she was, it was all Sabia could do to swallow as fast as she could, but the orc was pumping more cum into her even faster."
    "By the time it was done, the cum had overflowed her lips, making an utter mess of her face."
    $ hentai_scene(19)
    orc "Hmph. Good throat, bad slut."
    "The orc dropped a number of coins onto the floor of the tent and stalked out. Sabia did her best not to collapse, just gasping for breath to recover from the forceful experience."
    "The cum had made a mess of her face and more of it had overflowed, dropping over her breasts and sliding further as they heaved with each breath."
    $ money += 9
    "When she had recovered, Sabia grabbed the 9 Lundils that had been left behind and did her best to set the experience behind her."
    if gallery_workaround == True:
        jump gallery
    return


label sabiatent1:
    $ hentai_scene(1,"sabiatent1",dissolve)
    "As Sabia waited for the orc to enter the tent, she tried to steel herself. She'd keep control of the situation this time."
    $ hentai_scene(2)
    "She still had to avert her gaze when the orc entered and dropped his loincloth. Did they {i}all{/i} have cocks like that? Sabia was beginning to regret returning to the tents, but she was committed now."
    $ hentai_scene(3)
    s "I'm going to use my hand and that's it."
    "The orc gave an irritated grunt, but she didn't leave any hint of a question in her voice. She wasn't swallowing any more of that awful orc spunk."
    $ hentai_scene(4)
    "To prevent the orc from taking matters into its own hands, Sabia reached out and grasped his shaft. Despite herself, she hesitated a little at the feeling of the thick shaft, veins throbbing along its length."
    $ hentai_scene(5)
    "Getting over it, Sabia began jacking her hand up and down the orc's shaft. Even though it was a little dry, she went hard and fast. Precum began to slide from the tip of the cock, which felt disgusting on her hand but made the handjob go more smoothly."
    $ hentai_scene(6)
    "Despite the speed with which Sabia was sliding her hand up and down the orc's cock, it still hadn't come yet. She swallowed her irritation and kept at it, even as her arm started to get tired."
    "But she refused to let up, knowing that the orc would use that as an excuse to ram into her mouth. It did seem to be grunting in pleasure as she stroked its cock, so she was getting somewhere."
    $ hentai_scene(7)
    s "Seriously, not yet? Tell me when you're about t-"
    $ hentai_scene(8)
    call shake ("h")

    "At that moment the orc's shaft throbbed. Sabia had only a split second of warning before the first jet of cum erupted from the orc's cock."
    $ hentai_scene(9)
    "She should have moved her head or turned its cock aside, but she was too stunned by how explosively it came. The first burst of cum hit just above her eyebrow and splattered over her face."
    "Suddenly covered in orc cum, Sabia was too stunned to react. Her hand stayed where it was, gripping the throbbing cock, as jet after jet of cum covered her hair and face."
    $ hentai_scene(10)
    "As the orc finally finished coming, Sabia collected herself. Her face felt disgusting and her hair would be a nasty mess, but at least it was over."
    $ money += 4
    "Grumbling a little, the orc dropped 4 Lundils on the ground and stalked out, leaving her to collect them and clean herself quickly."
    if gallery_workaround == True:
        jump gallery
    return


label sabiatent2:
    $ hentai_scene(2,"sabiatent2",dissolve)
    "Once again, Sabia found herself facing a horrible orc cock, trying not to pay too much attention to it or what she was going to do."
    $ hentai_scene(4)
    s "Okay, just stay there and I'll take care of you."
    "Sliding her fingers around an orc's cock no longer felt unnatural, though it still repulsed her. Sabia averted her eyes as she began to stroke the throbbing length."
    $ hentai_scene(5)
    "This orc was certainly eager, quickly coating her hand with precum. At least that made it easier to slide her hand over the cock, she was starting to dislike the feeling of rough orc skin."
    $ hentai_scene(6)
    "Now that she was over her disgust, the worst part of giving handjobs was how long they took. It left her with a long period of time to do nothing but think, and her thoughts tended to wander in strange directions."
    "Orc cocks wouldn't be so bad if they weren't such a terrible green color. When Sabia closed her eyes, she found herself thinking that she wouldn't mind a human with a cock like this. Quite thick, satisfyingly hard..."
    $ hentai_scene(7)
    "Sabia jerked her thoughts away from that idea."
    s "Are you {i}still{/i} not done? I don't have all day here!"
    orc "Me want it to keep going."
    s "Surely you can speed this up."
    $ hentai_scene(8)
    "In response, the orc slid a hand around her head. Sabia glared... but he didn't ram into her throat. The orc could overpower her, she knew that all too well, but it gave her a chance."
    "Oh, fuck it. Sabia gave a slight nod and opened her mouth. This one wasn't so bad, she could let him use her mouth to get it over with faster."
    $ hentai_scene(9)
    "The orc shifted its cock, now pointing toward her open mouth. Sabia winced, expecting a thrust, but none came. Instead it shifted its cock against her tongue and lips."
    $ hentai_scene(10)
    "Sabia averted her gaze and tried not to grimace. Orcs had a certain musk to them... it wasn't exactly pleasant, but she was getting used to the heavy, masculine scent."
    "Meanwhile, the orc's cock was slathered in her saliva. Sabia was getting impatient, but at least it would be easier when the orc fin-"
    $ hentai_scene(11)
    "The orc thrust its hips forward, cock sliding between her lips. Even just the head and a few inches nearly made her gag, but Sabia managed to choke back her reaction."
    $ hentai_scene(12)
    "Sabia glared up at the orc, but it was no longer paying attention to her as anything but a wet hole. It kept shifting its hips back and forth, pleasuring the end of its cock instead of just ramming into her throat."
    $ hentai_scene(13)
    "Eventually Sabia decided she could just let it use her mouth. This one wasn't choking off her air, at least, and since its shaft was covered in saliva it didn't feel as rough. Her jaw was stretched wide, but the experience wasn't so awful."
    $ hentai_scene(14)
    call shake ("h")

    "She was actually starting to get used to the rhythm when the orc grasped her head with both hands and began thrusting harder into her mouth. After a few times, jets of cum started bursting from its tip, overwhelming her."
    $ hentai_scene(15)
    "Though she glowered, Sabia drank the orc's cum as it pumped into her throat. Better than leaving it in her mouth, after all, and it would help the orc finish faster."
    if beta_testing == False:
        show expression "scenes/sabiatent0.jpg" as hentai_scene
    "When the orc dropped its money and left, Sabia took a few moments just to catch her breath. It was more than the usual amount. Thinking over it a while, Sabia decided that it was worth it."
    if gallery_workaround == True:
        jump gallery
    return


label sabiatent3:
    $ hentai_scene(1,"sabiatent3",dissolve)
    "This time when the orc entered, Sabia managed to keep a smile on her face. She remembered the advice Neve had given her and tried to focus on the fact that this would make it be over sooner."
    $ hentai_scene(2)
    "As usual, the orc just dropped its loincloth without ceremony, making its cock swing upward toward her face. Sabia forced herself to give a sultry look."
    s "Ooh, that's quite a big cock you have for me..."
    $ hentai_scene(4)
    "She began sliding her hand up and down the orc's cock and it immediately grunted. Giving the head a little more attention, she quickly had her hand covered in precum and moving smoothly."
    $ hentai_scene(5)
    "Sabia kept smiling at the orc throughout the entire handjob. She began to move faster, hand pumping over the orc's thick cock, the motion making her breasts sway back and forth."
    "This wasn't so bad, really. The orc twisted and grunted, clearly under her control. Eager to take things up a notch, Sabia gave another smile... and shifted its cock down."
    $ hentai_scene(7)
    "She kept eye contact with the orc as she brought its cock to her mouth and began lavishing attention on it with her tongue. Its eyes bulged, clearly wanting to claim her mouth but unable to resist her rhythm."
    $ hentai_scene(8)
    "Sabia shifted all her attention to the beast's cock, getting it nice and wet. If this thick thing was going to be fucking her mouth, she wanted it to do so comfortably."
    $ hentai_scene(10)
    "When she finally bobbed her head forward, taking the orc's cock into her mouth, she was surprised how easy it was. She kept her hand around the shaft, stroking it gently as she began to bob her head over the tip."
    "Soon she found herself taking a little more of the cock with each bounce. It hadn't been part of the plan, but it was clearly taking the orc to the edge. Sabia let out a moan of her own as she pulled back, then sucked even more of its length into her mouth."
    $ hentai_scene(11)
    "As the orc began to thrust faster, Sabia's eyes rolled back in her head. She still kept bobbing and stroking the cock mindlessly, driving the orc crazy as it fucked her face."
    $ hentai_scene(12)
    call shake ("h")

    "Faced with such an assault, the orc couldn't last long. Sabia felt each and every jet of cum as it pulsed past her hand and filled her mouth."
    $ hentai_scene(13)
    "She kept her lips sealed around the shaft, even though she couldn't keep the copious cum from leaking out over her face. Sabia just kept her eyes on the orc's and gently milked the last of its cum with her hand."
    $ hentai_scene(14)
    "The orc pulled out with a satisfied sigh and didn't immediately stomp away. Sabia stared up at him adoringly, eyes sliding over the still thick shaft, as the orc dropped her money on the ground and left."
    $ hentai_scene(15)
    "Immediately her gaze shifted. So it really was that easy to control the beasts. Disgusting creatures... but as Sabia glanced down at the money that had been left, she decided that it was worth it."
    if gallery_workaround == True:
        jump gallery
    return


label sabiatent4:
    $ hentai_scene(1,"sabiatent4",dissolve)
    s "Come on in, big boy. Show me what you've got."
    "Most orcs who came into her tent now could barely wait to get their loincloths off. Sabia gave this one a sultry smile as she ran her eyes over its impressive length."
    $ hentai_scene(2)
    s "Mmm, I'm going to have some fun with this..."
    "She began to stroke the shaft, a comfortably familiar motion by now. The orc was so eager that its shaft was already slick with precum, which suited her just fine. Sabia gave him another smile for being cooperative."
    $ hentai_scene(3)
    "Soon she slid its cock down, still stroking slightly, and began giving it attention from her mouth as well. The orc grunted loudly and tried to thrust forward, but she kept it well in hand."
    "It was actually easy to get them off with just this, but as satisfied as they were, the orcs never paid as well unless they took her throat. So Sabia focused on getting its cock good and slick."
    $ hentai_scene(4)
    "When she was ready, she slid her eyes up to the orc. Though she kept stroking gently and licking over its head, she eased off her attentions, practically begging it to take over."
    $ hentai_scene(5)
    "Soon enough, it pushed forward, thick cock filling her mouth. Sabia felt a small surge of satisfaction - orcs were so easy."
    $ hentai_scene(6)
    "She stopped stroking the orc's cock, letting it use her mouth as it wanted. When she kept them satisfied like this, most didn't fuck her face brutally, instead working their way deeper a bit at a time."
    $ hentai_scene(7)
    "Each thrust went a little deeper until Sabia had the orc's entire cock down her throat. Her nose was pressed against the creature's powerful body and though she couldn't breathe, Sabia didn't struggle or try to pull away."
    $ hentai_scene(8)
    "As the shaft stayed in her mouth, cutting off her air, Sabia made a show of looking down with a little fear in her eyes. The orc grunted and then finally pulled back."
    $ hentai_scene(9)
    "She didn't need to fake the desperate breaths once her airway was free again - deepthroating orcs really was rough. Even as she caught her breath, though, Sabia kept sucking gently on the head of the orc's cock."
    $ hentai_scene(10)
    "It only gave her a moment before it thrust inside again. Sabia groaned and just took the thick shaft as it began to thoroughly fuck her throat."
    $ hentai_scene(11)
    "Though the orc got faster and rougher, Sabia didn't find herself choking. She was into it now, bobbing her head to meet the orc's thrusts, sucking intensely, letting her eyes roll back in her head."
    "At first she had told herself it was all an act, but Sabia was no fool. Repulsive as the whole thing was, when she got worked up enough, she actually enjoyed it. Sabia eagerly helped the orc fuck her face until it let out a low roar."
    $ hentai_scene(12)
    call shake ("h")

    "As many orc loads as her mouth had taken, Sabia was still a little startled at the rush of hot cum. She moaned softly as the orc roared its pleasure."
    $ hentai_scene(13)
    "With the orc's cock still down her throat, all Sabia could do was drink down everything it unloaded into her mouth. She was getting lightheaded, but it would be over soon."
    $ hentai_scene(14)
    "The orc finally pulled out, though it left the head of its cock in her mouth. Sabia sucked up the last of its cum and began to clean the head and shaft. This one hadn't been too rough, it deserved a little extra care."
    $ hentai_scene(15)
    "Finally the orc pulled out, slapped her ass, and departed the tent. Sabia took a moment to catch her breath, still flushed from the blowjob."
    "The orcs might be simple brutes, but part of her enjoyed mastering them. It was certainly better than scrabbling for a pathetic few Lundils in the dirt. Sabia smiled as she began to clean herself off."
    if gallery_workaround == True:
        jump gallery
    return


label neveorctravelers:
    play music sex1 fadeout 2.0 fadein 2.0
    $ hentai_scene(1,"neveorctravelers",dissolve)
    "Neve was pinned between two burly orcs - no, not pinned. Sabia flushed as she realized that the elven woman was actively rocking between the two, biting her lip, egging them on. One hand teased at the orc behind her."
    "They had larger than average cocks for orcs, pumping into both of Neve's holes. She took them both easily despite their thickness, her body obviously clenching tightly around the thick lengths."
    $ hentai_scene(2)
    "Getting a better grip on her own leg, Neve shifted her hips into position and pushed back against the orc behind her. He grunts loudly as if her huge ass had squeezed down on his cock."
    $ hentai_scene(3)
    n "Come on, give it to me harder than that!"
    $ hentai_scene(4)
    "In response, the orc in front of Neve grabbed her leg, shifting her position. Neve eagerly squirmed on the two cocks, but let them manhandle her body between them. From her new position, the orc behind her was able to get a better grip on her thigh and ass."
    $ hentai_scene(5)
    call shake ("h")
    "Using his leverage, he pulled Neve down at the same time he thrust up into her ass. Neve let out a scream as her back entrance was split open even further."
    $ hentai_scene(6)
    "Not letting up for a second, the orc continued to violate her asshole at a brutal, pounding pace. The muscles in Neve's ass and thighs rippled with the force of his fucking, but as she moaned she pushed back against him, urging him to go even deeper."
    "As she watched, Sabia found herself squirming and she wasn't sure why. The idea of something that thick in her ass... god, it would kill her. And yet Neve's screams were clearly pleasure and she was impaling herself onto the orcs' cocks over and over..."
    $ hentai_scene(7)
    "When at last the orc behind her began to slow down, Neve let out a satisfied sigh and flicked his ear."
    n "Ahh... that was just what I needed! Now, keep that up while I-"
    $ hentai_scene(8)
    call shake ("h")
    "Without needing to be commanded, the orc in front of Neve plunged into her pussy. His relatively gentle thrusts had clearly gotten him riled up, because now he began slamming into her brutally."
    $ hentai_scene(9)
    "The lean muscles in Neve's body flexed as she came, then relaxed. She slid back against the orc behind her a little, letting him spread her legs in position so that the other orc could pound her pussy."
    "They kept pumping into her with surprising stamina, but Sabia was even more surprised by Neve. Her body was covered in a sheen of sweat, her breasts bounced almost violently, yet after enjoying it for a bit, she started rocking between the two again."
    $ hentai_scene(10)
    n "Mmm, that's good. What do you say we finish this up, boys?"
    $ hentai_scene(11)
    "In response, the orcs both pulled back, their shafts glistening with her pussy juices. Neve grinned in anticipation and pulled her leg further back, lining herself up over the two of them."
    n "Alright, give me everything you've got!"
    $ hentai_scene(12)
    call shake ("h")
    "Both orcs thrust in to the hilt, Neve's lean body somehow accepting both thick cocks. Neve bit her lip and her eyes rolled back in her head as a convulsion went through her body."
    $ hentai_scene(13)
    "As they pounded her, Neve shuddered between them, the force rolling up her body. Her thighs jiggled, her taut stomach undulated, her breasts bounced, and her silver hair shook as she tossed her head."
    "Sabia found herself pressing her thighs together as she watched, holding her breath unconsciously. It was insane, but it looked like Neve wasn't going to let up, she wanted to get fucked like that forever."
    $ hentai_scene(14)
    "But even the two had their limits, their thrusts into her pussy and asshole starting to become erratic as they grunted. Neve chuckled and began rolling her hips, taking over their movements."
    n "Almost done, huh? I haven't gotten fucked like this in ages... fill me up, boys!"
    $ hentai_scene(15)
    "Growling, the orcs redoubled their speed, slamming into Neve from both sides as all three fell into the same rhythm. Neve's moans of pleasure turned to screams and her entire body seemed to freeze up, all her muscles tensing as she came hard."
    $ hentai_scene(16)

    call shake ("h")
    "Cum exploded inside Neve's body as the orcs came with a pair of roars. Their hips shook as they released what seemed like rivers of cum inside her. After having held back for so long, the orcs' balls were boiling with cum, and they unloaded it all into Neve's tight holes."
    $ hentai_scene(17)
    "Panting in satisfaction, Neve kept rolling her hips gently, milking out the last of the orcs' cum. She watched it pour out of her packed pussy with a pleased look, her breasts rising and falling as she caught her breath."
    "Sabia could only stare, still not quite sure she could believe what she had seen. Though she told herself she should go and pretend she saw nothing, Sabia found her eyes sliding over the orcs' brute masculinity, Neve's taut body, the thick cocks spreading her holes open..."
    "And that was the moment Neve glanced toward Sabia."
    play music orccamp fadeout 2.0 fadein 2.0
    if gallery_workaround == True:
        jump gallery
    return


label tekrokcrew1:
    play music sex2 fadeout 2.0 fadein 2.0
    $ hentai_scene(1,"tekrokmenbarmaid",dissolve)
    "Though Sabia was usually naked in the relief tents, she actually found herself more self-conscious wearing her outfit from the bar. Even on her hands and knees, the blouse squeezed her breasts together, and the frilly skirt just ornamented her ass."
    "It was obvious that the orcs crowding into the tent appreciated it. Plenty of them had eyed her while she worked in the bar, but now they could do whatever they wanted to her. Sabia promised herself that Tekrok's support would be worth it."
    $ hentai_scene(2)
    "After some shoving and arguing, the first of the orcs approached her and dropped its cock onto her face."
    orc "This is what's on tap today!"
    s "I'm thirsty, so I hope you have a lot for me!"
    $ hentai_scene(3)
    "She almost regretted encouraging them, when the orc grunted and moved its cock into position rather eagerly. But hopefully if she played along this wouldn't destroy her jaw."
    $ hentai_scene(4)
    "Almost immediately the orc shoved its cock into her mouth. Sabia tried not to choke and lavished attention over the swollen head, alternatively licking and sucking."
    $ hentai_scene(5)
    "Though the orc tugged on her head, jerking her back and forth a little, it was satisfied to enjoy her mouth instead of invading her throat. Sabia did her best to suck him off quickly."
    "The motion of rocking forward and back sent her breasts swaying, straining against the fabric of her outfit even more than usual. The sensation of the cloth on her nipples made Sabia moan into the orc's cock."
    $ hentai_scene(6)
    "Without warning, another orc dropped behind her and grabbed her ass. In the bar, she would have swatted its hand away, but now it was just getting started. Sabia braced herself for what she knew was coming."
    $ hentai_scene(7)
    "The orc's cock slapped against her thighs a little, then slid into her pussy. Sabia groaned around the cock in her mouth. At least this orc was moving slow enough to let her get a little wet."
    $ hentai_scene(8)
    "Grunting in satisfaction, the orc reached forward and tugged down her blouse. Her breasts sprang free, adding a wild bounce to the swaying movements as she was pushed back and forth by the orcs fucking her from both ends."
    $ hentai_scene(9)
    "Soon the orc thrusting into her from behind reached forward, grasping one of her breasts and fondling it. Rough as the orc's touch was, Sabia found herself shivering with each touch to her hard nipples."
    "Though the orcs didn't give much of a shit about her pleasure, Sabia was beginning to gasp and moan. The cock in her mouth wasn't so bad, her pussy was gripping the orc behind her tightly, and her chest felt hotter with each grope."
    $ hentai_scene(10)
    call shake ("h")
    "Just as Sabia was starting to get used to it, the orc in front of her jerked her head forward, finally impaling her face on its cock."
    $ hentai_scene(11)
    "Sabia choked and spluttered, but she was helpless to do anything about it. With powerful hands on her hips and head, not to mention the cocks deep inside her, she was completely trapped in place."
    $ hentai_scene(12)
    "Instead of fighting, Sabia just gave in to the overwhelming sensations. Her throat was getting fucked raw, but she could take the thick length."
    "Meanwhile, Sabia began actively pushing her hips back against the orc fucking her from behind. Not only was its thick cock pounding her so good, her skirt was flapping wildly, slapping against her newly sensitive skin and adding to the experience."
    "Surrendering to the pleasure, Sabia writhed between the two orcs. She thrashed wildly as they filled her from both ends, squirming each time her breasts were fondled, sucking as hard as she could, thrusting her hips back to meet the cock hammering into her."
    $ hentai_scene(13)
    call shake ("h")

    "When the orcs finally came, the rush of heat sent Sabia over the edge. She was barely even conscious of them pumping cum into her pussy and down her throat, all she could focus on was the intense heat."
    $ hentai_scene(14)
    "The ecstasy faded away slowly. Sabia found herself still spitroasted on the two orc cocks. They jerked a few more times, sending more cum sliding down her chin and thighs."
    "If they had pulled out then, Sabia probably would have collapsed, but they kept enjoying her wet holes. That gave her a second to recover."
    "But Sabia didn't even try to refocus, not with the other orcs crowding around her. All she could do was keep on her hands and knees, because she was going to be there for a while..."
    play music orccamp fadeout 2.0 fadein 2.0
    if gallery_workaround == True:
        jump gallery
    return


label tekrokcrew2:
    play music sex2 fadeout 2.0 fadein 2.0
    $ hentai_scene(1,"tekrokmenslave",dissolve)
    "Sabia's cheeks burned as she stayed in position, waiting for Tekrok's orcs. Wearing the slave armor was even more embarrassing than just being naked, the metal and fabric showing off her body as their property."
    $ hentai_scene(2)
    "The first orc shoved up behind her without any warning, cock sliding between her thighs and against her stomach. Sabia squirmed but kept her expression cheerful."
    s "Easy there, boy! We've got lots of time!"
    $ hentai_scene(3)
    orc "Less talking, more fucking!"
    s "Hey now, n-"
    $ hentai_scene(4)
    s "Aaaaah!"
    "The orc's massive hand came down hard on her hips, a slap that sent her ass jiggling. The stinging sensation made her jerk forward awkwardly, but the orc dug its fingers into her reddened skin and kept her close."
    $ hentai_scene(5)
    s "There's no need to be rough!"
    orc "You're our slave, slut! We'll use you however we want!"
    $ hentai_scene(6)
    "Realizing that he was right, Sabia directed her glower away from him. She knew she needed to convince this group of orcs to support her, but having this creature rub between her thighs while slapping her ass was humiliating."
    $ hentai_scene(7)
    "The orc reached forward to fondle her breasts, and her outfit offered no protection whatsoever. Sabia shuddered as the orc mauled her breast while still pushing against her."
    "But she was going to get fucked hard soon, so Sabia did her best not to focus on the worst of it. Though the orc's cock rubbing against her stomach was repulsive, it was at least giving her clit some stimulation. And as rough as the hand on her breasts was, it was better than nothing."
    "Just as Sabia was starting to get into it, she felt the thin string of her outfit's lower half strain against her skin, pressing into her curves."
    $ hentai_scene(8)
    "It snapped a second later, and the orc tossed aside the flimsy garment. Sabia looked backward, realizing with horror and desire that there was now nothing between her pussy and the thick cock that was pushing up against her stomach even more insistently now."
    orc "That's better, slut. Time to use you hard."
    $ hentai_scene(9)
    call shake ("h")
    "Before she could protest, the orc pulled back and then rammed its cock straight into her pussy. Sabia screamed as it hilted inside her, the orc's hard body ramming against her ass."
    "Immediately the orc began thrusting back and forth, the force of its movements sending her breasts swaying. The strips of cloth over her breasts swung even more, whipping up enough that the cold metal grazed her flesh."
    $ hentai_scene(11)
    "After fucking her hard for a while, the orc leaned forward enough to grasp her breast again. Teased by the flicking metal, Sabia's breasts were sensitive, her nipple digging hard into the orc's palm as it fondled the heavy sphere."
    "It shifted its hand on her ass, instead gripping more of her thigh. That made the ring of metal dig into her skin, and Sabia gave a little gasp. The metal wasn't painful, but every time it pushed into her skin it reminded her that she was nothing but a slut for these orcs to fuck."
    $ hentai_scene(12)
    "As the orc began to speed up, Sabia's eyes rolled back in her head. The cock was ramming deep inside her, as if to remind her that the orcs owned her pussy now. She clenched tightly, and at that moment the orc came with a roar."
    call shake ("h")

    "Sabia's body was still shuddering in orgasm as the orc unloaded inside her, heavy balls unleashing a flood of cum that filled her completely. The creature grunted and snorted as it emptied itself inside her."
    $ hentai_scene(13)
    orc "That's how you should look, slut: full of orc seed!"
    s "Yeah, you're really virile. Get on with it."
    $ hentai_scene(14)
    "The orc pulled out, and despite herself, Sabia missed the length just a little. Without the intense sensation, she was more aware of all the little sensations: the heavy shoulder plate, the strips against her breasts, the fishnet under her knee."
    "Those all reminded her of the outfit, and Sabia preferred to keep that out of mind. Instead she looked toward the gathered orcs."
    s "Alright, who's next?"
    $ hentai_scene(15)
    "The next orc didn't waste any time, getting into position behind her and thrusting between her thighs. Fuck, this one's cock felt really thick. As it thrust against her, it reached forward to grasp one of her breasts."
    $ hentai_scene(16)
    orc "This is better. Better for human women to be orc sluts. You like more than human men."
    "Sabia wanted to contradict him, but realized that would be stupid. This orc was at least being a little gentle, she didn't want to discourage that. She'd need some gentleness, with how thick that cock felt..."
    s "Why don't you show me, big guy?"
    $ hentai_scene(17)
    call shake ("h")
    "He did just that, huge cock pushing inside her. Though he didn't go fast, his girth stretched her pussy so wide that Sabia found herself moaning and bucking as she was impaled on the huge cock."
    $ hentai_scene(18)
    "When he finally buried his entire length inside her, Sabia was panting for breath and swimming in the pleasure. And this was just the second orc... she let go of any more thoughts of resistance."
    "Instead she just let the orc control her body. His grip on her hips made it easy for that thick cock to push inside her, and he kept fondling her breasts as well. She felt like nothing but a toy for the orcs..."
    "Flushing, Sabia found herself coming again. It would be the first of many times..."
    play music orccamp fadeout 2.0 fadein 2.0
    if gallery_workaround == True:
        jump gallery
    return


label lutvrogscene:
    play music sex1 fadeout 2.0 fadein 2.0
    $ hentai_scene(1,"lutvrogscene1",dissolve)
    "Sabia mounted Lutvrog confidently and let herself slide down his powerful muscles until her ass came to rest against his hard shaft. His control slipped, just a little, and he bucked underneath her. The sign of desire rippling through his corded body made Sabia shiver."
    $ hentai_scene(2)
    "His cock strained against the globes of her ass, the shaft pressing itself between them. She could feel it throbbing with his heartbeat and couldn't help but look back at the fearsome member."
    s "Looks like you had a hidden weapon during our match? I'm lucky you didn't use that thing, because I bet you really know how..."
    "Lutvrog grunted and shifted slightly. She could feel his muscles flex against her soaked slit, which she ground against him a little."
    s "Come on, Lutvrog, don't tell me you're giving up? I'm giving you a chance for a rematch here..."
    $ hentai_scene(3)
    "He responded to her provocation by reaching down and grabbing her ass. The power in his grip made Sabia give a little gasp. All orcs had big hands, usually they just looked brutish to her, but with Lutvrog she could feel the raw masculine power in his arm."
    "As he massaged her ass, his shaft pushing against her more insistently, Sabia found herself looking over his face. Lutvrog was still in control, but she could see the burning desire there and wanted to see it unleashed. Smiling, she lifted her hips slowly, sliding them up his shaft until she was poised over the head of his cock..."
    $ hentai_scene(4)
    call shake ("h")
    "Lutvrog's hand gripped her hip tighter and pulled her down, impaling her on his cock... just like she wanted. Sabia couldn't help but cry out as the force of it rippled upward through her body. Fuck, it felt even thicker than it looked."
    $ hentai_scene(5)
    "When he had finally buried most of his length inside her, Sabia was left gasping for breath. Her hands that had been caressing his chest now gripped it to keep herself from falling, but her arms felt so weak. Occasionally she dipped forward, her breasts brushing the muscles of his chest, and it wasn't just teasing, she was struggling not to collapse."
    "Sabia glanced backward again - she couldn't see his shaft very well over the curve of her ass, but the sensation of his hand and cock dominating her hips was plenty. Sabia bounced up and down his shaft just a little."
    s "Alright, that was a good opening move, but if that's all you've got, I-"
    $ hentai_scene(6)
    call shake ("h")
    "With a roar, Lutvrog grabbed her ass with his other hand and began fucking her. Sabia wailed and thrashed, but the intense thrusting was exactly what she needed. His cock filled her so completely, strained every part of her core to the limit."
    "Despite her victory, she really was helpless now - Lutvrog had an overwhelming advantage in strength, and he used it to pump her hips up and down his shaft even as he rammed up inside her."
    "Normally Sabia tried to remain in control with her partners, but now she reveled in giving up all pretension. She bounced her hips and screamed like a whore, fingernails scratching his chest as he kept plowing inside her pussy."
    $ hentai_scene(7)
    "Before too long she was covered in even more sweat than she had been after the match. Her first orgasm crept up on her out of nowhere, sending a rush of pleasure through her body. When she gasped and collapsed against his chest, Lutvrog slowed down. Instead of thrusting so violently, he sank fully inside her and stirred her pussy with his cock while his hands massaged her ass."
    $ hentai_scene(8)
    "Even so, it took her a moment to recover enough to push herself upright. She stared down at his face, focused on enjoying her tight pussy, and with a whimper tried to move her hips faster again."
    "He returned to thrusting, the movement of her hips again controlled by his overwhelming strength. Sabia settled for adding a grinding motion against his body every time she came down against it."
    "Most orcs humped wildly until they came, but Lutvrog kept up the steady pace, driving her through another toe-curling orgasm. When Sabia came down from the heights of pleasure, she saw that he was nearing his limit as well."
    lut "Lutvrog... is close. If you want Lutvrog t-"
    s "Don't pull out! Give me everything!"
    "Her words seemed to push him over the edge, and Lutvrog began a furious assault of thrusts inside her. Sabia screamed and thrashed around his shaft as it devastated her pussy."
    $ hentai_scene(9)
    call shake ("h")

    "When he came she felt his entire body tense up, as if all his strength was gathered and emptied inside of her. Cum exploded inside her pussy, jet after jet of heat filling her utterly and taking her over the edge one more time."
    $ hentai_scene(10)
    "For a moment her mind was overwhelmed by pleasure, then Sabia came to, lying against Lutvrog's chest. His hands still gripped her ass possessively. Though he had emptied most of his load inside her, his cock still twitched, depositing smaller loads that were still more than most men could come."
    "Part of Sabia felt like she should be ashamed, but she brushed it aside. It felt too damn good for her to care, so she just smiled down at Lutvrog before reluctantly pulling herself off his cock."
    if gallery_workaround == True:
        jump gallery
    return


label badendorctent:
    play music sex2 fadeout 2.0 fadein 2.0
    scene bg black with dissolve
    "Months later..."
    $ hentai_scene(1,"badendorctent",dissolve)
    "Sabia shifted on her hands and knees in the center of the tent, waiting for the next orc who would use her. Her veins throbbed with the drug that kept her mind hazy and happy."
    "When the high faded occasionally, she always found herself looking for more. Not because she was addicted, but because when her mind was operating at full, she would always realize that she had no way of moving forward from here."
    "As much as she still wanted revenge, there w-"
    $ hentai_scene(2)
    "Sabia's thoughts were cut off as another orc cock appeared in front of her, gloriously thick and throbbing. She immediately let out a sigh as her body started to heat up automatically."
    $ hentai_scene(3)
    "By now it was an instinct, Sabia didn't even think before reaching up to touch the orc's shaft. It pulsed in her hand, promising so much."
    $ hentai_scene(4)
    "She began to pump her hand along the orc's length. Her hands were almost always slick now, since the orcs were using her so frequently. She would keep stroking until the orc got bored and took her another way."
    $ hentai_scene(5)
    "Today, though, another orc entered and got into position behind her. Sabia moaned seductively and wiggled her hips back against him, delighting in the thick length along her stomach. Soon it would be inside her, and then all other thoughts would be gone."
    $ hentai_scene(6)
    "As the orc behind her began to fondle her breasts, teasing the chain between her nipples, the other orc became more aggressive. Sabia eagerly shifted his cock so she could lavish attention on it with her tongue."
    $ hentai_scene(7)
    "Finally, {i}finally{/i}, the orc behind her thrust his enormous cock inside her. Sabia let out a cry of pleasure, the pumping in her veins lighting on fire and overwhelming her."
    $ hentai_scene(8)
    "She didn't choke even slightly when the other orc pushed into her mouth. Instead, Sabia just kept stroking the back half of his cock as he fucked her face with the rest."
    "Meanwhile, the other orc was pounding her pussy and her mind until she was almost delirious. There were no more thoughts, just pleasure, but her body had been so well-trained that she kept stroking, sucking, and squeezing."
    $ hentai_scene(9)
    call shake ("h")

    "Soon both warriors unloaded, emptying huge loads inside the camp cumdumpster. Sabia took them, eagerly and easily, drinking down the cum in her mouth even as she came at the feeling of more jetting inside her pussy."
    $ hentai_scene(10)
    "Both orcs took a while to finish, her body instinctively milking every drop of cum from them. They stayed inside her, enjoying the feeling of her body shuddering as their cum brought her to orgasm yet again."
    $ hentai_scene(11)
    "The cock in her mouth began to pull out, and Sabia whimpered, sucking on the tip gently to try to keep the orc there. She heard the warrior chuckle, and realized yet again that it was hopeless. She was nothing but the camp whore now, there was no action that she could take to get what she wanted."
    "Instead Sabia leaned forward, sucking his cock back into her mouth. Better to stay in the hazy pleasure, where all she wanted was the next time the warriors would enter and use her again..."
    show gameover as hentai_scene with dissolve
    pause 3
    if gallery_workaround == True:
        jump gallery
    return


label badendorctrial:
    play music sex2 fadeout 2.0 fadein 2.0
    $ hentai_scene(1,"badendorctrial",dissolve)
    "Sabia seethed on the floor of the tent. She had already done everything she could to try to escape the chains that bound all four of her limbs, but they were firmly tied to something heavy sunk beneath the tent."
    "They had given her some kind of drug, something to weaken her will. Sabia could feel it working through her, but denied it any power over her. These savages couldn't possibly threaten her with their primitive potions."
    $ hentai_scene(2)
    "Finally they came for her, and Sabia didn't give them the pleasure of the slightest shame. Even as an orc moved up behind her, she just glowered at it."
    s "So brute force is all you savages understand, huh? You'll regret this when human legions desce-"
    $ hentai_scene(3)
    s "Gah! Unhand me, you brute!"
    "The orc didn't answer, just kept squeezing her breast. Sabia squirmed to move away, but she was bound too firmly in place. The movement only made her more conscious of the huge cock pressing up against her stomach."
    s "I'll never submit to you scum. All y-"
    $ hentai_scene(4)
    "The orc brought a hand down hard on her ass, drawing a shocked yelp from Sabia's lips. She didn't want to give them the pleasure, bit her lip to stay quiet, but the orc kept slapping at her luscious cheeks, enjoying her squirming above its cock."
    "Despite herself, the spanking was making her body heat up. The foul potion they'd made her drink, no doubt. Sabia did her best to ignore the growing sensations until the assault ended."
    $ hentai_scene(5)
    s "Is... is that all? You think you can just slap anyone around to get them to obey you?"
    $ hentai_scene(6)
    "The orc didn't even answer, just kept rubbing against her stomach while another orc approached her face. Sabia glowered up at the filthy beast, vowing to bite its cock off when it got close enough."
    $ hentai_scene(7)
    call shake ("h")
    "Abruptly the orc behind her rammed into her cunt, drawing a cry that was immediately muffled by another thick green cock hitting the back of her mouth. In a flash, Sabia had gone from glowering to impaled on orc cocks."
    $ hentai_scene(9)
    "Sabia tried to bite down, but it was too late. The cock in her mouth stretched her lips too wide for her to bite effectively, and the orc's skin was tough. She was helpless to do more than squeeze her lips into an even thinner line around the thick shaft."
    "As she struggled, the two orcs began to fuck Sabia. She glowered down at the cock pushing into her throat, even as the orc behind her was starting to feel good. Just a primitive sensation brought on by their drug, nothing she couldn't handle. All she had to do was endure a little longer."
    $ hentai_scene(10)
    call shake ("h")
    "Before she could get used to the pace, the orc in her mouth finally managed to shove down her throat. Sabia let out an angry scream, completely muffled by the cock that blocked off her throat. She tried to twist away, but moving her head only pleasured the orc's cock more."
    $ hentai_scene(11)
    "Instead of pulling out, the orc began to jerk her head back and forth, trying to cram the final inch of its cock down her throat. Sabia could do nothing but take it, her head completely controlled by its powerful hands."
    "Meanwhile, the orc behind her just kept pounding away. Though it gripped her hips to keep them in place, each powerful thrust still pushed her forward a little, driving a bit more of the other orc's cock down her throat."
    $ hentai_scene(12)
    "Sabia began to get lightheaded. She tried to catch a breath, but her throat was constantly filled with thick orc cock. There was no air to be had, just the pleasure coursing through her body more and more with each thrust."
    "Her eyes began to roll back in her head. Her hips were jerking automatically, dominated by the pumping sensation of each thrust. Even the cock in her throat felt good now..."
    $ hentai_scene(13)
    call shake ("h")

    "She had no idea how long it was, there was nothing but an endless ordeal of fucking until at last both orcs came inside her. Sabia moaned as their hot cum filled her, coming again. She had completely lost track by now."
    $ hentai_scene(15)
    "Even after it was done, the orc didn't pull out, staying inside her convulsing throat. And in that moment, Sabia didn't care. These disgusting orc cocks hadn't beaten her, but... she could feel them just a little longer. As long as it felt so good..."
    $ hentai_scene(16)
    "Months later..."
    $ hentai_scene(17)
    "After months of resistance, Sabia had finally been completely broken. No more curses against orcs came from her lips - she did nothing but moan and occasionally beg to be stuffed full of cock again."
    "She stayed in the tent, still bound only because the orcs liked fucking her that way. But she had no chance of escape: any orc could shove a cock inside her and she would immediately begin coming violently."
    "Sabia spent every day being used over and over as the orcs' cumdumpster. A few warriors had gotten revenge on her at first, but now she was just another fucktoy for them to use to get off."
    "And that was all Sabia wanted anymore."
    show gameover as hentai_scene with dissolve
    pause 3
    if gallery_workaround == True:
        jump gallery
    return


label lynnintroscene:
    play music sex1 fadeout 2.0 fadein 2.0
    $ hentai_scene(2,"lynnintroscene",dissolve)
    l "Well, someone's eager."
    soldier "Of course! I can't believe Archmage Lynn is going to... to..."
    $ hentai_scene(4)
    l "You know how to flatter a girl, at least."
    $ hentai_scene(1)
    l "But first, we need to discuss the exact details of what your scouts found."
    soldier "N-now? I'm this hard and you want to talk?"
    l "Enjoy the view, but if I don't like your answers, that's all you're getting."
    soldier "Fine..."
    $ hentai_scene(2)
    l "Now... why exactly did you decide to send scouts?"
    soldier "Reports of orcs at the border. The mages sai-"
    l "No, I don't like that answer at all. Surely you can... remember differently?"
    soldier "Fuck, I'm so... okay! It was reports from an unaffiliated province! I know a man out there, he can confirm!"
    $ hentai_scene(1)
    l "That's better."
    soldier "Then..."
    $ hentai_scene(5)
    l "Alright, then, let's see what I can do about your little friend here..."
    soldier "Oh, thank Relona!"
    l "No. Thank {i}me{/i}."
    $ hentai_scene(7)
    "Lynn finally leaned forward and slid her perky breasts around the soldier's shaft. They couldn't extend all the way, but they were silky soft and he groaned in pleasure. Lynn raised her eyebrows at the desperate need throbbing through his shaft."
    $ hentai_scene(6)
    l "You really wanted this, didn't you? Do all you soldiers stare at me, wishing you had Archmage Lynn's tits wrapped around your cock?"
    soldier "Oh, fuck!"
    "Her words made his hips buck involuntarily, which was a good enough answer. Smirking, Lynn set to work. The man was still useful, so she needed to ensure his loyalty any way she could."
    $ hentai_scene(9)
    "Hiding her smirk, Lynn instead began sliding down, rubbing her breasts against the sides of his shaft. The man squirmed, really nothing but a beast. Still, he was hot and hard between her breasts, she might be able to get a little enjoyment out of it."
    "At the base of his cock, Lynn halted, squeezing tighter, letting her breasts push against his thighs as well. She gave an appreciative murmur, then began sliding back up."
    $ hentai_scene(10)
    "As the soldier groaned in pleasure, Lynn pumped her breasts up and down his shaft. He really was so simple... but the sensation was starting to get to her as well. Lynn squeezed her small, hard nipples and began to increase the pace."
    $ hentai_scene(13)
    soldier "Please... more..."
    "Damn impertinent of him to demand anything more now... but he had a pretty good cock, so Lynn decided not to punish him. Instead, she gave him a smile... and went lower."
    $ hentai_scene(14)
    l "This is what you want, isn't it? My noble lips on your cock?"
    soldier "Oh fuck yes!"
    $ hentai_scene(15)
    "Lynn opened her mouth, breathed on the throbbing head, then extended her tongue to lick it just a little. The taste was heavy and masculine, normally she would have hated it, but Lynn found herself lapping over the head of his shaft, wanting more."
    $ hentai_scene(16)
    "Soft moans left her mouth as she lavished attention over the man's cock. She kept squeezing her breasts around the base of his shaft even as her tongue explored the top. He felt so hard, so alive..."
    $ hentai_scene(18)
    "Shivering deliciously, Lynn dragged herself back up his cock, a line of saliva stretching between her lips and the head of his cock. He groaned and bucked his hips, trying to fuck her tits, but she easily rode out the motion."
    $ hentai_scene(19)
    l "You liked that, did you? Well, just remember where your loyalties lie, and there might be some more..."
    soldier "Wait, please! You've gotta finish me off!"
    "Lynn chuckled, squeezing the head of his cock a little more... then let her breasts fall away."
    $ hentai_scene(20)
    l "No, this has been fun, but I got what I wa-"
    $ hentai_scene(21)
    call shake ("h")

    "Her dominant words sent the man over the edge. His cock pulsed, releasing a huge jet of cum toward her face..."
    $ hentai_scene(22)
    call shake ("v")
    pause 1
    $ hentai_scene(23)
    call shake ("v")
    pause 1
    $ hentai_scene(24)
    call shake ("v")
    pause 1
    l "You bastard! Did you seriously plan to come all over my face?"
    soldier "Ahh! Archmage Lynn, please! You were... you were just too good!"
    $ hentai_scene(25)
    "Lynn narrowed her eyes and glared down at him, letting him squirm. But aside from the end, it hadn't been intolerable, and he'd given her everything she needed. Besides, she might need his cooperation again."
    l "Just don't forget who's in charge here and you might have another chance."
    soldier "Yes, of course!"
    l "Then get out. I have a meeting to prepare for."
    if gallery_workaround == True:
        jump gallery
    return


label nevemaply1:
    play music sex1 fadeout 2.0 fadein 2.0
    $ hentai_scene(2,"maplyneve1",dissolve)
    maply "H-hey! Just... just what are you doing?"
    "The catgirl clawed at the bonds on her wrists, unintentionally wiggling her tight little butt in the process. She cast a plaintive glance over her shoulder... and her eyes widened in surprise."
    $ hentai_scene(3)
    "Neve slid over Maply, pressing her breasts against the catgirl's slender back. Maply's eyes went even wider, which made Neve chuckle softly."
    n "Don't tell me you're surprised? You have entire caravans of women... surely you must play around with each other..."
    $ hentai_scene(4)
    maply "S-sometimes... but I... why are you...?"
    n "Because you're cute. Now, let's see how you react..."
    $ hentai_scene(5)
    call shake ("h")
    pause 3
    "Maply cried out in surprise as Neve reached underneath her and tweaked one of her nipples. The catgirl tried to pull away, but Neve's fingers were agile and kept massaging the nipple until it was hard as stone."
    n "Good reaction..."
    $ hentai_scene(6)
    "Even though it had barely begun, Maply's breathing was becoming heavy. Face blushing brighter, she stared back at Neve, eyes fixed on the other woman as she kept teasing her nipples."
    "Maply squirmed to escape the sensation, but Neve easily had her pinned down. The movements only made the other woman's breasts rub against her back... and Maply realized, even through the cloth, that Neve's nipples were hard as well."
    $ hentai_scene(7)
    n "Now, let's see how you're doing back here..."
    "Neve slid a hand over the catgirl's tight ass, confidently sliding to her pussy before spreading it. Maply squirmed and gave a low whine, but her hips seemed to be moving toward Neve's fingers now."
    n "Oh, that's a nice color. But you're not as wet as I expected... maybe catgirls aren't as easy as they say?"
    $ hentai_scene(8)
    "Still spreading the catgirl's pussy, Neve returned to teasing her nipples as well. Maply couldn't hold in a moan, her body jerking at the sensations from both ends. Neve smiled to herself as she slowly learned the other woman's body, learning how to tease her just far enough."
    $ hentai_scene(9)
    "Once she was ready, Neve slipped two fingers inside. Her pussy didn't resist at all and neither did Maply, gritting her teeth but not struggling as Neve explored deeper inside her."
    n "Here we go... relax and enjoy it..."
    $ hentai_scene(10)
    "Maply did just that, her eyes rolling back a little as Neve began to push her slender fingers deeper inside her. She kept her mouth closed, though, only little whines of pleasure managing to escape from time to time."
    "Neve chuckled and began hooking her fingers a little more, seeking out the spots that would send the catgirl over the edge. It didn't take very long before Maply's whimpers could barely be contained."
    $ hentai_scene(11)
    "At that moment Neve plunged her fingers even deeper inside and Maply let out a cry. That sound seemed to break her self control and all attempt to keep silent vanished. Maply bucked and moaned and pushed her hips back against Neve's hands, desperate for more. Neve smiled broader and began playing her body like a fiddle."
    $ hentai_scene(12)
    call shake ("v")
    maply "Ahhhhh!"
    "The catgirl's slim body bucked wildly as she came, all her muscles spasming as she went over the edge. Her hips convulsed as her juices squirted out, drenching Neve's hand and splattering over the tent."
    $ hentai_scene(13)
    "Neve let her ride it out, then slipped her fingers from the other woman's burning pussy to give her a chance to recover a little. Maply was panting for breath now, eyes foggy, having completely surrendered to the pleasure."
    n "Mmm, that's a good look for you. Had enough?"
    $ hentai_scene(14)
    "When Neve acted like she might pull her fingers further away, Maply gave a low whine."
    maply "Wait... I... I..."
    n "Don't worry, we're not done. In fact, I have something for you..."
    $ hentai_scene(15)
    n "Do you have anything like this in your caravan?"
    maply "What... what is that?"
    n "Don't worry, it will make you feel good..."
    $ hentai_scene(16)
    "Neve slid the tip of the dildo against the catgirl's pussy, prompting Maply to moan. The dildo was warm and slightly soft, not like any toy she had felt before. As it teased at her outer folds, Maply began to push her hips back again, instinct taking over and demanding something inside her."
    $ hentai_scene(17)
    call shake ("v")
    "Obliging her gladly, Neve slid the tip of the dildo inside. Maply's eyes went wide and she let out a low groan, her hips bucking for more penetration, but Neve kept control of their movements."
    $ hentai_scene(18)
    "Soon Maply collapsed, only able to pant and moan, surrendering to Neve's rhythm. Neve rewarded her for it by returning attention to her nipples and finally sliding the dildo a little deeper inside her."
    $ hentai_scene(19)
    "She carefully teased at all the sensitive places she had found earlier, now adding the sensation of the other woman's pussy stretching wider and the dildo's bumps rubbing her sensitive walls."
    "Soon it was easy to play her body like an instrument, drawing from the catgirl's cries of passion, desperate mewlings, and shudders of ecstasy. Neve pushed her through more and more pleasure, always easing away just as she came close to her limit..."
    $ hentai_scene(20)
    call shake ("v")
    "...until she plunged the dildo inside just when Maply was at the limits of her pleasure, sending her tumbling over the edge. Maply screamed and her body spasmed as she came again, her juices shooting out even more intensely from around the dildo."
    $ hentai_scene(21)
    "When it ended, Neve mercifully eased off on her stimulation. The catgirl beneath her was a wreck of pleasure, eyes unfocused, entire body still trembling. Neve smiled and sent one hand caressing along her side..."
    n "Now, if you tell me just a few things, I'll hold you a while..."
    if gallery_workaround == True:
        jump gallery
    return


label orcmaply1:
    play music sex2 fadeout 2.0 fadein 2.0
    $ hentai_scene(1,"maplyorcA",dissolve)
    maply "Why... why do I gotta do this?"
    "Sabia chuckled and looked down at the squirming catgirl. She had a tight little body that didn't look like it could hold up, but maybe that would just make this easier."
    s "I hoped you'd give me information... but since you've refused, I'm afraid I couldn't stop someone from finding out..."
    $ hentai_scene(2)
    maply "F-finding out? What do you mean?"
    $ hentai_scene(3)
    "Maply got her answer when Sabia gestured and the orc pushed inside the tent. He snorted, ripped off his loincloth, and grabbed the catgirl's small but incredibly rounded ass."
    maply "Aaah!"
    $ hentai_scene(4)
    maply "You... are you really going to let him...?"
    s "Sorry Maply, nothing I can do to stop him."
    $ hentai_scene(6)
    maply "N-no! Not there!"
    s "Oops, looks like he's interested in the back door!"
    maply "Please, n-not that! I'll d-die!"
    s "Well... you there... sure you don't want to fuck that tight little pussy instead?"
    $ hentai_scene(5)
    orc "Guh. Maybe. All holes good."
    maply "That's... that's not as bad, but..."
    s "Alright, pull back for a bit."
    $ hentai_scene(7)
    "The orc obeyed, but kept his hands firmly gripping Maply's hips, not letting her forget that at any moment, the huge shaft could split open one of her holes. Maply whimpered and squirmed, but she was also blushing fiercely."
    s "While he decides which hole to use, why don't you and I discuss some secrets, hmm?"
    maply "But... but..."
    $ hentai_scene(6)
    maply "Eeek! Okay, okay, I'll talk!"
    scene bg black with dissolve
    pause 1
    s "(Hmm, I think she's telling the truth, but she might know more. Should that be enough to let her off the hook?)"
    menu:
        "Be merciful":
            s "Thank you for answering, Maply... I'll tell him to be gentle..."
            maply "Wait..."
            $ hentai_scene(1,"maplyorcB")
            call shake ("v")
            "The orc eagerly thrust his cock straight into Maply's defenseless pussy. Though it seemed far too small to take his girth, somehow it managed to take the entire thing as it plunged deep inside."
            $ hentai_scene(2)
            "The orc massaged her ass as he sank even deeper inside her, enjoying her body spasm as it struggled to cope with the huge invader."
            maply "It's... it's too big... I... I can't..."
            orc "Hnnh! Catgirl pussy is the best!"
            $ hentai_scene(3)
            maply "Please... not too rough..."
            orc "Me gonna fu-"
            s "She told us enough. At least take it slow..."
            $ hentai_scene(4)
            "Begrudgingly obeying Sabia, the orc began to thrust into Maply less brutally than he would have normally. He still had plenty to enjoy, feeling the catgirl's small pussy wrapped around his cock."
            "She began to moan almost immediately, her body adapting to the pace the orc set. Maply panted for breath and began to push her hips back against the thrusts, even though her chest heaved and her arms trembled from the overwhelming sensation."
            $ hentai_scene(5)
            "Finding her hole wetter and increasingly welcoming, the orc began to fuck along with her instead of just hammering her pussy. With his fingers easily gripping her hips, it was easy for him to move her into the perfect position so that he could thrust deeper and deeper."
            "The harder he fucked her, the better Maply responded, her pussy clenching around his shaft. She seemed to be a creature of pure instinct now, a female submitting to the mating and loving it. With a catgirl in heat wrapped around his cock, the orc couldn't last long."
            $ hentai_scene(7)
            call shake ("h")

            "He unloaded inside of her, his cum seeming to jet out forever. Maply released a scream of pleasure, her entire body shuddering as she was filled up and the hot cum sent her over the edge."
            $ hentai_scene(8)
            "Her body gave out as soon as her orgasm did, slumping to the floor of the tent. The orc kept his cock inside her, letting her pussy milk the last of his cum. Though her eyes had rolled back in her head, she looked... satisfied."
            "Sabia could only shake her head. If that was how catgirls were, maybe working with them wouldn't be so bad..."
        "Be cruel":
            s "That's not good enough. Guess there's nothing I can do to stop him..."
            maply "W-wait!"
            $ hentai_scene(1,"maplyorcC")
            call shake ("v")
            "Maply's protest was useless, as the orc eagerly rammed his cock against her asshole. The small bud resisted for a moment, it seemed like his shaft couldn't possibly fit, yet eventually it yielded."
            $ hentai_scene(2)
            "The head got inside on the first thrust, and after that, the orc could only sink in slowly, a bit at a time. Maply screamed in pain as her asshole was stretched wide... and yet she endured. It seemed impossible, but eventually she took the entire thing."
            $ hentai_scene(3)
            orc "Hu! Catgirl holes are the best..."
            "Looking back at the orc, Maply gave a desperate whimper."
            maply "Please... be gentle..."
            $ hentai_scene(4)
            "Ignoring her entirely, the orc began railing her with all his strength. His thick legs and heavy belly slapped against her ass as he rammed inside it, brutalizing her back entrance."
            $ hentai_scene(5)
            "Sabia watched in shock as the catgirl's cries turned from pain to pleasure. Soon her mouth was hanging open, her eyes were unfocused, and she was just taking the brutal assfuck. Like a bitch in heat, which was really close to the truth."
            $ hentai_scene(6)
            "Grunting in satisfaction, the orc got a better grip on her ass, his hands wrapping entirely around the smaller curves. Maply gave a cry and tried to squirm away, but it was too late: with his new leverage, the orc began to pound her ass even more brutally."
            "It was obvious that he was just using her hole for his pleasure, yet it didn't seem to matter. The catgirl's thrashing became unclear, almost looking like she was pushing back against the cock violating her entrance."
            $ hentai_scene(7)
            call shake ("h")

            "Before too long, the orc blew his load inside the catgirl's asshole. Her tiny body, already packed with his cock, couldn't hope to hold all the cum he pumped inside her. It began gushing out of her stretched ass, running down over her glistening pussy."
            $ hentai_scene(8)
            "When the orc finally finished he stopped for a moment, enjoying the catgirl's asshole spasming around his cock as he let out the last few jets. Maply only shuddered and panted for breath, still coming down from her orgasm."
            "Sabia shook her head. Maybe the little whore would be more cooperative now..."
    if gallery_workaround == True:
        jump gallery
    return


label sabiabargrope1:
    show orcbase at right
    show orcloincloth at right
    show orcemo smile2 at right
    show basesimple at screen_farleft
    show baroutfit2 at screen_farleft
    show sabiaemo normal at screen_farleft
    with dissolve
    "Sabia had a fairly good idea what would happen, but she steeled herself to go through with it. Maybe if she played her cards right, it would pay off in the end. But she tried not to think about that, instead putting a smile on her face and serving the orcs."
    show orcbase at center
    show orcloincloth at center
    show orcemo smile2 at center
    with moveinright
    show orcbase at left
    show orcloincloth at left
    show orcemo smile2 at left
    with moveinright
    $ hentai_scene(1,"sabiabargropeA",dissolve)
    "For the first round of drinks, they just leered at her and made a few lewd jokes. Sabia was self-conscious about her skirt swishing around her thighs, nearly displaying her ass, but otherwise started to get comfortable working."
    $ hentai_scene(2)
    call shake ("v")
    "So she was completely unprepared when it happened: an orc reached out and grabbed her ass."
    show sabiaemo surprised2 at screen_farleft
    show sabiaemo2 blush at screen_farleft
    $ hentai_scene(3)
    "Even though she'd expected it, Sabia still found herself freezing up, her cheeks blushing scarlet. The orc gripped a little harder, fingers sinking into her ass, but hesitated."
    $ hentai_scene(4)
    "He pulled his hand away, but not far. All the orcs were watching her to see how she would react, and Sabia realized that she had to decide - fast - if she was going through with this."
    menu:
        "Let it happen":
            $ bargroping += 1
            show sabiaemo closed2 at screen_farleft
            "Sabia gritted her teeth and tried to ignore it, just going about her work. But it wasn't long before the rowdy group of orcs ordered another round and watched her as she approached, eyes filled with lust."
            $ hentai_scene(5)
            show sabiaemo surprised3 at screen_farleft
            "The same orc reached out to grab her. This time it wasn't a quick grope, he squeezed her ass hard. Sabia had to bite her lip to stop from making a sound, which the orc seemed to take as a challenge."
            $ hentai_scene(6)
            show sabiaemo surprised1 at screen_farleft
            "Since she wasn't fighting back, he began to massage the entire globe of her ass, getting a feel for the soft but perky sphere. The other orcs laughed and hooted in approval, enjoying watching her squirm."
            "With the orc groping her ass so intensely, Sabia had to struggle to get the mugs down on the table, which meant that she had to endure it even longer. Which the orc didn't mind at all, really getting a feel for her ass."
            $ hentai_scene(7)
            show sabiaemo closed2 at screen_farleft
            "When she was finished and finally walked away, she could still feel his hand, hot on her ass. Her skirt was so short, she knew the other orcs could probably see it, but Sabia just vowed to endure it."
            if gallery_workaround == True:
                jump gallery
            return
        "Stop him":
            show sabiaemo angry1 at screen_farleft
            s "None of that!"
            "Sabia rapped his wrist hard with a mug as she set it down on the table. The orc scowled, but drew his hand back."
            if gallery_workaround == True:
                jump gallery
            return
        "Beat the shit out of him" if (dom >= 2 and orcbarbeatdown == False):
            $ dom += 2
            $ L_orcs += 3
            $ Sabia.xp += 2
            $ orcbarbeatdown = True
            show sabiaemo closed2 at screen_farleft
            hide sabiaemo2 blush
            "Sabia grabbed the orc's mug, lifted it, and then brought it down on his head as hard as she could. He dropped to the table, stunned, and she delivered a savage kick to his crotch. When he collapsed to the ground, she stomped his neck hard before going about her work."
            "None of the orcs tried to grope her after that."
            if gallery_workaround == True:
                jump gallery
            return


label sabiabargrope2:
    show orcbaseL at center
    show orcloinclothL at center
    show orcemo smile2L at center
    with dissolve
    with dissolve
    "When Sabia saw the group of orcs again, she steeled herself and headed to serve them their drinks. This time, she doubted they'd hesitate."
    show basesimple at right
    show baroutfit2 at right
    show sabiaemo closed2 at right
    with moveinright
    show sabiaemo2 blush at right
    with dissolve
    $ hentai_scene(1,"sabiabargropeB",dissolve)
    "As she got closer, she could feel their eyes all over her. She had never been so conscious of how her work outfit pushed her breasts up, creating soft mounds of flesh for them to ogle."
    $ hentai_scene(3)
    orc "There's our drinks!"
    "One of the orcs stood up as she came, as if to greet her - but he moved around behind her, between her and the rest of the room, his bulk blocking her from the view of everyone else."
    $ hentai_scene(4)
    show sabiaemo happy1 at right
    "Sabia put on her best smile and tried not to show any anxiety."
    s "That's right, boys! Sit down and I-"
    $ hentai_scene(5)
    call shake ("v")
    show sabiaemo surprised2 at right
    "The orc interrupted her by reaching up and grasping one of her breasts. Sabia couldn't help but let out a soft cry as his fingers gripped it tightly."
    $ hentai_scene(6)
    show sabiaemo sad2 at right
    "When the shock passed, the orc didn't pull away. She could tell he was close to doing it, but kept his hand on her breast to see what she'd do. Sabia swallowed, wishing she had a better idea..."
    menu:
        "Don't make a big deal of it":
            $ bargroping += 1
            pass
        "Stop him":
            $ hentai_scene(7)
            show sabiaemo angry2 at right
            s "Get your fucking hand off me!"
            $ hentai_scene(9)
            "The orc pulled back hastily, hearing the steel in her voice. Sabia slammed their drinks down on the table, glowered at them, and stalked off."
            if gallery_workaround == True:
                jump gallery
            return
    $ hentai_scene(8)
    show sabiaemo happy3 at right
    s "Y-you're getting pretty handsy there, big guy. No need to be rough."
    orc "So it's fine if me not rough?"
    $ hentai_scene(10)
    show sabiaemo surprised2 at right
    "Before Sabia could respond, the orc grabbed her other breast and began to massage it, only barely more gently than before. Sabia let out a gasp, not having expected him to switch hands so quickly, but she endured."
    $ hentai_scene(11)
    show sabiaemo happy2 at right
    s "Easy there. You don't want me to break, do you?"
    orc "Heh. Maybe."
    $ hentai_scene(12)
    show sabiaemo surprised3 at right
    "She started to say something, but before she could respond, the orc reached his other hand up again. Sabia gritted her teeth as he began to palm both breasts, pulling her back against his chest and playing with them roughly."
    "Despite everything she was thinking, her body was responding against her will. Her nipples were getting hard, and she was sure the orc could feel them digging into his palms even through the fabric of her blouse. His chuckling supported that idea."
    $ hentai_scene(13)
    show sabiaemo happy1 at right
    s "You... you had enough yet?"
    orc "Huhh. Maybe for now..."
    show sabiaemo closed2 at right
    "The orc left her alone, finally letting her deliver their drinks. But judging from the expression of all the rest, this was far from over."
    if gallery_workaround == True:
        jump gallery
    return


label sabiabargrope3:
    $ bargroping += 1
    show basesimple at center
    show baroutfit2 at center
    show sabiaemo closed2 at center
    show sabiaemo2 blush at center
    with dissolve
    show orcbaseL at left
    show orcloinclothL at left
    show orcemo smile2L at left
    with moveinleft
    show orcbase2 at right
    show orcloincloth2 at right
    show orcemo2 smile2 at right
    with moveinright
    "The third time Sabia approached the rowdy group of orcs, she knew exactly what she was getting into. They basically ignored her drinks, quickly surrounding her."
    $ hentai_scene(2,"sabiabargropeC",dissolve)
    "In a matter of seconds, Sabia found herself trapped against the table and completely surrounded by rough orc bodies. The scent of their unwashed bodies overwhelmed her, foul and yet somehow intoxicating."
    $ hentai_scene(3)
    "They didn't play around this time: one of the orcs immediately reached up and began fondling her breast. Sabia could have jabbed his stomach with her elbow, or kicked backward and got him in the crotch, but she didn't resist."
    $ hentai_scene(4)
    "Instead she just stood there, letting the orc molest her as the others crowded closer. Her body trembled in reaction to his rough touch, the plate of mugs still held aloft as a pathetic justification for all this."
    "But this... this wasn't enough. They could grope her all day and it wouldn't go as far as it needed to go. So Sabia swallowed and gave her best smile."
    $ hentai_scene(5)
    s "Come on, boys, drinks are here. What are you waiting for?"
    $ hentai_scene(6)
    "One of the others reached out and grabbed her ass, gripping it so hard that she would have fallen forward if not for the orc behind her still groping her tits."
    $ hentai_scene(8)
    "As he explored her taut ass, Sabia found herself beginning to pant for breath. Her nipples were already hard, and the groping of her ass was only pushing her tits forward into the orc's hands even more."
    $ hentai_scene(9)
    call shake ("v")
    "Then the orc pulled his hands down... and peeled off her top."
    $ hentai_scene(10)
    "Even though she had known it would happen, Sabia still found herself shocked for a moment. Her tits were out in the middle of the bar in broad daylight, on display for the brutish orcs surrounding her. Even the orc fondling her ass stopped for a moment, impressed... then he gave a little squeeze and let go."
    $ hentai_scene(11)
    "That was the signal for the rest of the orcs to descend on her. A different orc shoved in behind her and took his turn mauling her tits, while more hands grabbed at her ass. The fabric of her blouse hadn't been thick, but it had provided some protection... now there was nothing between her sensitive breasts and the rough orc fingers laying claim to them."
    $ hentai_scene(12)
    "The orcs were fully into it now, groping her from every angle. Sabia moaned and twisted involuntarily as her breasts were squeezed and pressed while rough hands gripped her ass. She couldn't even keep track of the orcs now, they were just a brute mass taking liberties with her body."
    $ hentai_scene(14)
    "As more and more orcs began to fondle her, Sabia found herself releasing soft, gasping moans. Everything about the scene was filthy, yet somehow that made it even hotter. Her body was their plaything, eagerly awaiting each new touch."
    $ hentai_scene(16)
    "Then, without warning, the orcs pulled back. They still surrounded her with a wall of muscle, but they didn't lay a hand on her body. Instead they just stared at her, luscious flesh red from their groping, trying to catch her breath. They saw a slut who was about to surrender to them completely."
    $ hentai_scene(17)
    "This time, though, they retreated. Sabia had only a moment to hastily pull her top back up to keep anyone else from seeing her."
    "Not this time, but soon..."
    if gallery_workaround == True:
        jump gallery
    return


label sabiabargrope4:
    $ bargroping += 1
    show basesimple at center
    show baroutfit2 at center
    show sabiaemo closed2 at center
    show sabiaemo2 blush at center
    with dissolve
    show orcbaseL at left
    show orcloinclothL at left
    show orcemo smile2L at left
    with moveinleft
    show orcbase2 at right
    show orcloincloth2 at right
    show orcemo2 smile2 at right
    with moveinright
    "Determined to see it through this time, Sabia sauntered over to the group of orcs with an extra swing of her hips and bounce of her chest. Not that they needed much encouragement... this group was more than ready to take advantage of her."
    $ hentai_scene(1,"sabiabargropeD",dissolve)
    "This time when they surrounded her, they took the mugs away from her. Instead, one of the orcs grasped her wrist, holding her in place as all the others surrounded her. They didn't even need to say anything, they knew why they were here."
    $ hentai_scene(4)
    "All at once they descended on her, hands groping over every part of her body. Sabia couldn't help but let out a little squeal as her tits and ass were groped roughly, yet her body was responding immediately. Her body was still a little sensitive from the last time, so when they lay hands on her she couldn't help but cry out."
    $ hentai_scene(6)
    "But that cry quickly became sweeter as the orcs relentlessly assaulted her body. Moaning, Sabia pressed her hips backward and her chest forward, eager for more of their touch. There wasn't enough of her to go around, so the orcs eagerly grabbed whatever they could."
    $ hentai_scene(8)
    s "What... what do you say we take this to the next level, boys?"
    "The first moment she got a chance, Sabia delivered the sultry offer that she'd planned. The orcs laughed, not at all surprised, knowing that it would end up here eventually."
    $ hentai_scene(9)
    call shake ("v")
    "Despite her words, Sabia still gasped when they tore down her blouse and skirt. Her skin was so hot and flushed that the air of the tavern felt shockingly cool."
    $ hentai_scene(10)
    "The orcs took a moment to admire her body, making lewd comments about the fact that she had worn underwear just for them. Sabia only panted for breath, knowing that it made her chest heave and not caring. They wouldn't be able to hold themselves back now, not for long..."
    $ hentai_scene(12)
    "A hand gripped her ass, squeezing so tightly it actually lifted her into the air a little. But Sabia had barely finished gasping when the orc behind her reached around to grasp one of her breasts, massaging it eagerly."
    $ hentai_scene(13)
    "He was even more forceful than before, drawing a gasp from Sabia's lips. She tried to squirm away on instinct, but any way she turned, their hands were still able to paw at her body."
    $ hentai_scene(14)
    "Another orc reached for her ass as well, both globes now palmed by an enormous orc hand. Just feeling up her ass, they were able to completely control her hips, pushing her forward, pressing toward the orc in front of her."
    $ hentai_scene(15)
    "As the orcs took turns playing with her body, Sabia moaned wantonly. She knew exactly what they were thinking: all they had to do now was reach out and grab her and she was helpless to do anything but become their toy."
    $ hentai_scene(16)
    "Hands descending on her from every side and soon Sabia was reduced to whimpered gasps. The raw heat of their bodies flooded her, sweat beginning to cover her skin and make it even easier for their hands to slide over her flesh."
    $ hentai_scene(17)
    "Orc after orc took liberties with her body, but this wouldn't be enough for them. Not this time. Sabia could tell that they were all rock hard under their loinclothes, wanting nothing more than to thrust their cocks straight into her body."
    s "Boys... what do you say we take this somewhere private?"
    $ hentai_scene(18)
    orc "Yes! Let's get to the tents!"
    "The orcs pulled back for the final time, leaving her gasping for breath. The marks of their hands were clearly visible on her body, obviously ready for them in every way. Sabia shook her head coyly."
    s "Tents? You think I'd charge you boys? No, let's head somewhere more private..."
    "Laughing raucously, the orcs practically lifted Sabia off her feet as they rushed out into the night air, dragging her out to a narrow crevice behind the bar. They left behind their drinks and a lot of their weapons in the bar in their eagerness to fuck her until she couldn't beg for any more."
    scene bg black
    "She had just finished stripping out of her uniform when the orcs cut them down."
    if gallery_workaround == True:
        jump gallery
    return


label catgirls1punishment:
    play music sex1 fadeout 2.0 fadein 2.0
    $ hentai_scene(1,"catgirlsexample",dissolve)
    "The catgirl leader had been chained to the floor, with only a short leash for movement. Not that it mattered, with an orc looming behind her. He kept her pushed forward on her hands and knees while keeping her back arched by tugging on one of her arms."
    $ hentai_scene(2)
    catgirl "It doesn't matter how many of you there are, I'll take you!"
    "The orc didn't seem to notice, except for his chuckle. He was obviously not the first orc to fuck her and it was clear he wouldn't be the last. Instead he merely pushed her forward harder, pressing her small breasts against the rug beneath her, before finally shoving all the way inside."
    $ hentai_scene(3)
    "Immediately the catgirl gave a loud moan as his cock filled her up. It seemed like he would have to be splitting her apart, yet her body managed to take it. In fact, there was no pain at all in her cries, just a hint of anger."
    $ hentai_scene(4)
    "Even that faded away as the orc set about really fucking her. The catgirl's body was so much smaller it seemed like a toy in his hands, easily shifted into the position he wanted to be a perfect sleeve for his cock."
    "As the fucking continued, the catgirl's eyes rolled back and she began releasing moans of pleasure. It seemed like her hips were moving back against the orc's now, trying to get his shaft even further inside her."
    $ hentai_scene(5)
    "Sabia had no intention of watching it for too long, but she found herself wandering back to the tents. It had been going on for hours, the catgirl leader crying out in pleasure until going silent, only to resume not long after."
    $ hentai_scene(6)
    "When Sabia peeked inside again, the catgirl was still in the same position, but she bore all the marks of the brutal fucking she had endured. In addition to the cum covering every part of her body, it seemed like a few of the orcs had been having fun with whips while she'd been gone."
    "The newest orc behind her pulled her into position even as he shifted his hips to line up his cock. The catgirl didn't object this time, just panted for breath and waited for him to finally thrust inside her."
    $ hentai_scene(7)
    "At last he did, slamming against her ass, and her panting gave way to gasping moans once again..."
    if gallery_workaround == True:
        jump gallery
    return


label catgirls1working:
    play music sex1 fadeout 2.0 fadein 2.0
    $ hentai_scene(1,"catgirlsworking",dissolve)
    "Sabia looked in on the building where the catgirls worked, hoping things weren't too rough. She seemed to be entering at the start of the day, as currently there were only a few catgirls being used."
    "Her eyes naturally fell on one catgirl with striking red hair. She was bent over at the waist, shifting uncomfortably but not resisting."
    $ hentai_scene(2)
    catgirl "Are... are you sure it will fit? I t-think it's too big..."
    "The orc grunted and began working his way into her, not ungently, and the catgirl gave a little squeak as her pussy was spread wide."
    $ hentai_scene(3)
    "Soon the orc was pumping into the catgirl's body, making her wail in pleasure. Giving in to instinct, the catgirl began to press her hips back against the orc as he thrust inside her."
    $ hentai_scene(4)
    "Her eyes eventually rolled back in her head and she gave herself over to the pleasure entirely, moaning and drooling as the orc pounded her over and over."
    if catgirlscaptured >= 5:
        $ hentai_scene(5)
        "Another catgirl was pulled in nearby, drawing Sabia's attention. This one was dropped on her back before the orc thrust in straight from above, filling her pussy with thick cock."
        $ hentai_scene(6)
        "The orc only gave her a moment to get used to being stretched out like that before he began to drive his hips up and down like a machine, pistoning his cock straight down into the catgirl. Though she was completely pinned in place, her moan sounded like she was encouraging him on."
        $ hentai_scene(7)
        "Caring only for his own pleasure, the orc hammered into her until he finally came inside her, his powerful thrusts sending spurts of it out onto her ass."
        $ hentai_scene(8)
        "The orc paused for a moment, enjoying the sensations of her quivering pussy packed full of his cum. But as he waited there, the catgirl's tail slid out, wrapping around his leg as if to hold him there."
        $ hentai_scene(9)
        "Grunting appreciatively, the orc plunged back down into the catgirl, this time setting a pace like he meant to go all night."
    if catgirlscaptured >= 10:
        $ hentai_scene(10)
        "Not far away, a third catgirl was drawn in, her hips bucking wildly against the orc fucking her. Getting a better grip on her hips, the orc let her arch backwards to rest her shoulders against the ground, her breasts heaving as he pumped inside her."
        $ hentai_scene(11)
        "They only took a little while to adjust to their new position and then they were fucking intensely again. The catgirl threw her head back and moaned as the orc kept pounding her raised legs, sending her thrashing with pleasure."
        "At that moment, Sabia heard a strange whine, partially pleasure and partially a complaint. She turned just in time to see another catgirl brought close."
        $ hentai_scene(12)
        pause 1
        "This one was pushed forward onto the floor nearby, where she immediately reached out to clasp the other catgirl's hand. The orc didn't seem to mind fulfilling her request, considering that he had a good grip on her fantastic ass."
        $ hentai_scene(13)
        "When he pushed inside, the catgirl didn't object, just moaned and squeezed her friend's hand harder. Her friend squeezed back and her eyes began to cross with pleasure."
        "Now that she had what she wanted, the catgirl seemed to descend into mindless ecstasy almost immediately, mouth lolling open and her hips pumping back against the orc's as he began fucking her hard and fast."
        $ hentai_scene(14)
        "The two kept holding hands even as the orcs fucked them from orgasm to orgasm. Soon both were quivering wrecks, but they didn't let go... or stop moving their hips. Soon they managed to draw grunts from the orcs fucking them, and huge spurts of cum followed."
        $ hentai_scene(15)
        "The catgirl on the right looked even more out of it as cum rolled down her ass and back. She had enough presence of mind to watch her friend, however, who had cum splattered all over her gorgeous body and face."
    if catgirlscaptured >= 15:
        $ hentai_scene(16)
        call shake ("v")
        pause 1
        "Without warning, two more pairs of catgirls and orcs crowded in on either side of Sabia. The room was getting crowded now, but they didn't seem to care. And it was obvious why: the catgirls dropped to their knees and began sucking on the orc cocks presented to them."
        $ hentai_scene(17)
        "One of the catgirls was struggling a little, but kept dutifully bobbing her head. The orc played with her hair and ears, encouraging her to take even more but content to enjoy her mouth for now."
        $ hentai_scene(18)
        "Both orcs came at the same time, one filling the catgirl's mouth to bursting and sending cum spilling out over her lips. The other had been more successful, taking the cock all the way to the base so she could swallow the jets of cum straight down her throat."
        $ hentai_scene(19)
        "As their orcs finished, the catgirls pulled back a little, gently caressing the spent cocks even as they drank down the rest of the copious cum. Soon, the cocks were far from spent. All across the room, orcs and catgirls began to fuck one another even more intensely, their cries growing louder and louder..."
    "Having seen enough, Sabia left the tents."
    if gallery_workaround == True:
        jump gallery
    return


label catgirls1enslaved:
    play music sex2 fadeout 2.0 fadein 2.0
    $ hentai_scene(1,"catgirlsenslaved",dissolve)
    "Sabia looked in on the building where the catgirls were held prisoner. She seemed to be entering at the start of the day, as currently there were only a few catgirls being used."
    "Her eyes naturally fell on one catgirl with striking red hair. She was bent over at the waist, glowering fiercely."
    $ hentai_scene(2)
    catgirl "Dammit, let me go! Don't stick that thing in me!"
    "The orc ignored her, instead beginning to work his cock inside the catgirl. She wriggled and squirmed, but his massive hands kept her from too much as he impaled her on his cock."
    $ hentai_scene(3)
    "Soon the orc was slamming to the hilt with every thrust, hammering the catgirl's helpless body. For a while she bucked and twisted, but eventually she gave in and stayed still, letting his hips slap against her ass."
    $ hentai_scene(4)
    "Her mind slowly surrendered and soon the catgirl's eyes were rolled back in her head, drool falling from her lips. She groaned and thrust back, nothing but a bitch in heat now."
    if catgirlscaptured >= 5:
        $ hentai_scene(5)
        "Another catgirl was dragged in and chained up beside the first, drawing Sabia's attention. This one was pinned on her back before the orc slammed in from above, driving his cock deep inside her."
        $ hentai_scene(6)
        "Without hesitating, the orc began to pound the catgirl beneath him, his hips hammering down against her thighs as he penetrated her over and over. It seemed like he was determined to impale her to the floor with his cock."
        $ hentai_scene(7)
        "Not caring about the catgirl's pleasure, the orc soon dropped a load inside her, filling her pussy to bursting and drawing a wail from the catgirl's lips."
        $ hentai_scene(8)
        "The orc hesitated for a moment, getting a better grip on her body as he got ready to go again. The catgirl lay limply, cum streaming out of her filled pussy and sliding down over her ass."
        $ hentai_scene(9)
        "As soon as he'd caught his second wind, the orc began hammering down into her again."
    if catgirlscaptured >= 10:
        $ hentai_scene(10)
        "Not far way, another orc dropped a catgirl onto her back. He let go of her hips only long enough to chain her with the others, then he thrust straight inside. Letting out a moan, the catgirl arched her back incredibly far. The orc got a better grip on her hips and then began fucking her like that, arched against the floor."
        $ hentai_scene(11)
        "Without anything to grab onto, the catgirl just lay back with her arms limp at her sides, letting the orc use her hips however he wanted. Her body shook with the force of his thrusting, making her large breasts bounce up and down, nearly striking her own face."
        $ hentai_scene(12)
        "As they got started, another catgirl was pushed down nearby, her large chest pressed against the floor. She seemed to ignore the orc gripping her ass, instead plaintively reaching out toward the nearest catgirl. Her hand scrabbled on the floor a bit before she managed to reach her, and they gripped each other tightly."
        pause 1
        $ hentai_scene(13)
        "The orc obviously didn't care, since he was focused on reaming the catgirl in front of him. She whimpered for a moment before she seemed to give in entirely and the orc began hammering away at her ass."
        $ hentai_scene(14)
        "Meanwhile, the orc fucking her friend was getting closer. He pounded her hips in the air until he pulled out just as he came, sending jets of cum all over his prize. The catgirl saw it coming, but was helpless to do anything but be marked as an orc fuckslave by the hot, sticky cum."
        $ hentai_scene(15)
        "Her friend had also taken a thick load and now drooled mindlessly with her eyes crossed. They kept a loose grip on each other's hands as the orcs began to fuck them again."
    if catgirlscaptured >= 15:
        $ hentai_scene(16)
        call shake ("v")
        pause 1
        "Sabia was nearly knocked off her feet as several more orcs crowded in with catgirls in tow. They pushed the catgirls down to their knees and jammed their faces straight into their cocks."
        $ hentai_scene(17)
        "Having long since given up, the catgirls began bobbing their heads back and forth, trying to avoid a brutal facefucking. The room was starting to get a little crowded, but as Sabia backed away, she kept watching them."
        $ hentai_scene(18)
        "Soon the newest orcs came as well, pumping loads of cum down the throats of the new catgirls. They weren't even chained in place, but as they struggled just to keep up with swallowing, it was obvious that no chains were necessary."
        $ hentai_scene(19)
        "One of the catgirls looked up, hoping for a break, but none was coming. The orc began to pump down her throat again as all around the room, the orcs fucked their prizes."
    "Having seen enough, Sabia left the tents."
    if gallery_workaround == True:
        jump gallery
    return


label barrinintscenedom:
    play music sex2 fadeout 2.0 fadein 2.0
    "Sabia roughly stripped away Barrin's armor and tossed it into one corner of the room."
    $ hentai_scene(2,"barrinintscenedom",dissolve)
    s "Alright, kid. You have two options... enjoy yourself and tell me everything I want to know, or hold back and suffer for it."
    $ hentai_scene(3)
    barrin "What is this? You think you can make me talk by... acting like a whore?"
    s "That's pretty confident talk..."
    $ hentai_scene(4)
    s "For someone who's so very exposed right now."
    barrin "W-wait! Don't-"
    $ hentai_scene(5)
    call shake ("v")
    "Sabia snapped the tight ring around Barrin's cock, where it constricted the base tightly. She grabbed the shaft with her hand and felt it buck, but he was bound firmly enough that it was useless."
    $ hentai_scene(6)
    barrin "F-fuck, that's tight..."
    $ hentai_scene(7)
    s "I'm not going to do any permanent damage... you need that thing to make future little Governors, right? But if you don't cooperate, this is going to get very uncomfortable..."
    barrin "I... what do you think I'm withholding from you! I told you everything!"
    s "Is that so...?"
    $ hentai_scene(9)
    s "You're a bad liar. You need to be punished for that..."
    barrin "W-wait, please!"
    $ hentai_scene(10)
    "But it was too late. Sabia gripped his cock firmly and began to pump her hand up and down. It was a little rough, but she didn't really care if he enjoyed it or not. Barrin groaned and bucked his hips as if he was already at his limit."
    barrin "Please... please let me come..."
    $ hentai_scene(11)
    "Smirking, Sabia made eye contact and continued stroking his cock. Barrin groaned and tried to twist away from her."
    s "That was quick... let me guess: you've only fucked a few of your father's maids? Let them tell you how good you were after you came in two seconds?"
    "Controlling him was remarkably easy, his hips bucking up into her hand entirely predictably. Sabia found herself enjoying dominating him, but kept herself in control. She needed information, after all."
    $ hentai_scene(12)
    s "Alright... are you feeling more cooperative now?"
    barrin "I... I..."
    $ hentai_scene(13)
    barrin "I can tell you more about my father's troops movements... and where we were scouting before we got off course..."
    "He spilled out a huge amount of information about the movements of both Governors... more than he'd intended to, given how utterly thrown off he was by the growing ache in his balls."
    s "Oh? You finally want to play along? That's so sweet of you..."
    $ hentai_scene(14)
    s "But I think you're still hiding something."
    "It was just a guess, but Sabia was happy to torture him a little more. His cock seemed ready to burst, the veins digging into her hand. It had finally gotten a little lubricated, so she could easily pump her hand up and down in a movement that was comfortable for her and torture for him."
    "Sabia slid her body up against him further, both to give herself some stimulation and increase his torment. He moaned as she pressed her breasts further against his chest and began grinding her hips against his. He didn't have a bad body, and hearing his tormented gasps and moans was almost fun."
    $ hentai_scene(15)
    barrin "Th-there was a letter!"
    s "Oh?"
    "Sabia stopped pumping her hand, but she kept it around his shaft, squeezing just a little."
    $ hentai_scene(16)
    s "Alright, tell me. If I believe you, maybe I'll be merciful. If not... well, you'll get to see what I can really do."
    barrin "It was a... a dead drop. We have a mole in Governor Andian's estate, you see..."
    $ hentai_scene(17)
    s "I'm listening..."
    "He soon spilled everything, revealing that their scouting mission had a second objective. Their mole had left a package of critical troop information at a specific location, but Barrin's group had misjudged and gone too near the orc camp."
    "The correct location was close as well, though. Getting it now would be a real risk for someone like Barrin... but not for her."
    "Eventually he was done, and this time Sabia believed that he'd told her everything. He lay beneath her, groaning for release, all his defenses stripped away. She could be merciful... if she wanted."
    menu:
        "Let him come":
            $ L_humans += 1
            s "You know what, Barrin? You've been a good boy, I'll let you finish this time."
            pass
        "Leave him that way":
            $ L_humans -= 1
            s "Thanks for the info! The orcs will drop you off soon!"
            barrin "W-wait! Aren't you going to let... let me..."
            s "Ask one of the orcs!"
            if gallery_workaround == True:
                jump gallery
            return
    $ hentai_scene(19)
    "She removed the cock ring and Barrin gave a low groan, his cock twitching almost as if it would come right that second. She waited a few moments before wrapping her fingers around his shaft again, gently this time."
    $ hentai_scene(19)
    "Sabia found a comfortable rhythm pumping his shaft, pushing herself against him even harder as she let his pleasure spike like never before. Earlier, she had changed up her pace, never giving him satisfaction, but now she stroked him firmly and consistently."
    $ hentai_scene(20)
    call shake ("h")

    "It wasn't long before his entire body convulsed and cum exploded from his cock."
    $ hentai_scene(21)
    "More cum than she'd expected shot into the air, arcing high and splattering over her thigh and ass. Sabia hadn't wanted to get dirty... but it didn't really matter, with Barrin gasping for breath like that underneath her. He gave a deep groan when she squeezed his sensitive cock a little, but she let her fingers slip away."
    $ hentai_scene(22)
    s "Very good, Barrin. You're going to live through this after all."
    barrin "I... I will?"
    s "That's right... just listen to me and follow instructions..."
    if gallery_workaround == True:
        jump gallery
    return


label barrinintscenesub:
    play music sex1 fadeout 2.0 fadein 2.0
    "Sabia slid off the pieces of Barrin's armor gently, planting light kisses on the exposed skin."
    $ hentai_scene(1,"barrinintscenesub",dissolve)
    s "Mmm... you have such a nice body... so strong..."
    barrin "You think so? Then free my arms."
    $ hentai_scene(2)
    s "But... but I'd get in trouble."
    barrin "I won't try to escape, wench. I just want to touch you."
    s "If... if you say so..."
    $ hentai_scene(3)
    "The instant Sabia freed his arms, Barrin reached down to grab her ass. Sabia gave an exaggerated yelp, but she didn't need to exaggerate much. He was as handsy as an orc, and his erection left no doubt as to his intentions."
    barrin "Now, slide on top..."
    $ hentai_scene(4)
    "Sabia glanced back at his cock, for a brief moment unable to hide the annoyance on her face. His wasn't bad, but he was kind of an idiot and she didn't want to fuck him."
    barrin "Come on... get on it!"
    $ hentai_scene(5)
    s "If... if I do that the orcs will punish me..."
    $ hentai_scene(6)
    "In response, Barrin reached his other hand up to grope one of her breasts, even as he kept massaging her ass. He rolled her flesh in his fingers as he responded."
    barrin "That's a shame, you have a great body."
    $ hentai_scene(7)
    s "Can I... help you some other way? I'm not going to leave you without relief..."
    $ hentai_scene(8)
    "She started to slide away, but Barrin gripped her harder, pulling her body against his even as he mauled her breast and ass. The stimulation was starting to get to her, her nipples slowly hardening. She shivered and looked away from his face."
    barrin "Alright, then, wench. Let me feel that hand on my cock!"
    $ hentai_scene(9)
    "Sabia meekly reached down to slide her fingers around his shaft, which pulsed in her hand. Barrin smirked and kept squeezing her as she hesitated before beginning, no doubt just enjoying a slender female hand on his cock."
    $ hentai_scene(10)
    "She wanted to get it over with, though, so Sabia began sliding her hand up and down. Barrin groaned and bucked his hips into her hand almost immediately."
    $ hentai_scene(11)
    s "You're so hard... it's so powerful... I can't wait to feel you..."
    "Sabia whispered the words in her best seductive voice, hoping to send him over the edge sooner. But he clearly didn't need any help just focusing on his pleasure, as Barrin seemed to have already forgotten about her except as a body to grope and a hand to milk his balls."
    $ hentai_scene(12)
    "As Sabia kept sliding her hand up and down his shaft, she let her expression shift to a slightly more natural smile. His tough controlling act was only skin deep. She might be serving his lusts, but his lusts were serving her."
    barrin "That's right... keep it up just like that..."
    s "I can't believe you're captured by orcs and you still have everything under control like this..."
    barrin "It, uh, comes from experience..."
    s "But I don't understand... just why would you need to risk any harm to yourself?"
    "It was easy to get Barrin talking, clearly enjoying his boasting while she stroked his cock. She asked apparently innocent questions and he outlined quite a bit about the movements of both Governors... more than he'd intended to, but he was distracted."
    $ hentai_scene(13)
    "She wanted to prolong it and get more information from him, but the kid didn't have the stamina for it. Recognizing the erratic bucking of his hips meant he was about to come, Sabia stopped talking and instead focused on milking his cock. Barrin groaned and slumped backward, hands finally letting go of her as he focused entirely on his shaft."
    $ hentai_scene(14)
    call shake ("h")

    "It wasn't long before it exploded, cum jetting up into the air."
    $ hentai_scene(15)
    "Sabia could have dodged it, but thought he'd probably want to see his cum splattered all over her thigh and ass. She couldn't help but frown a little, but Barrin was still catching his breath after the intense orgasm and was too far gone to notice."
    $ hentai_scene(16)
    barrin "That was fantastic... I wish I could take you back with me..."
    "Though his cock was growing soft in her hand, it seemed clear that Barrin still wanted her. His hand gripped her ass even more possessively than before."
    $ hentai_scene(17)
    barrin "Ahh... that was fantastic. I'm almost glad I lost the letter, to have experienced that..."
    s "Hmm? What's this?"
    barrin "It wasn't the main mission, but... we were going to pick up a drop from a messenger. We have a mole in Governor Andian's estate, you see..."
    "Sabia hid her interest and asked him soft questions. Still relaxing in the afterglow, Barrin talked easily about things he probably shouldn't have. Her mother had always told her men got stupid and emotional after they came, but she'd never seen it so clearly before."
    "Soon she had the exact location of the drop that he had missed: a forested region north of the orc camp. Getting it now would be a real risk for someone like Barrin... but not for her."
    $ hentai_scene(18)
    "She had everything she needed, but Sabia had to let him grope her for a while longer before it became obvious that his cock wasn't going to get hard enough again."
    barrin "Remember the plan, alright wench? If I can get in touch with my father, I can arrange everything..."
    s "Alright..."
    if gallery_workaround == True:
        jump gallery
    return


label vehlisaliochA:
    play music sex1 fadeout 2.0 fadein 2.0
    $ hentai_scene(1,"vehlisaliochA",dissolve)
    $ renpy.pause ()
    "A curvy blond woman who could only be Vehlis sat completely naked above the plush couch. Not on it, because she was actually sitting on the lap of an elven pleasure slave."
    $ hentai_scene(2)
    "Focused on the thick cock poking up between her thighs, Vehlis didn't see Sabia at all. She was rocking herself along the slave's shaft, the outer folds of her pussy sliding around it. Apparently she had been teasing him for a while, because his cock was slick with her juices."
    "Leaning back into a slightly more comfortable position, Vehlis murmured a command that Sabia couldn't quite hear."
    $ hentai_scene(3)
    "Immediately obeying his mistress, the slave reached forward to grasp her hips. He massaged her soft curves, shifting her hips to press against his cock even harder, drawing a pleased gasp from Vehlis."
    $ hentai_scene(4)
    "The woman bit her lip and stared down at his cock eagerly. She obviously had this slave well-trained to match her exact preferences, because she didn't need to give him many commands."
    $ hentai_scene(5)
    "Rising up, Vehlis positioned herself above the slave's cock. It throbbed, the impressively thick girth massaged by her soft thighs. Vehlis merely wiggled in position, torturing her slave by prolonging things a little longer."
    $ hentai_scene(6)
    vehlis "Well? What are you waiting for?"
    "Her casual phrase was apparently the command, because the elf slave immediately gripped her hips tighter and pulled her down."
    $ hentai_scene(7)
    call shake ("v")
    $ renpy.pause ()
    "Vehlis plunged down onto his cock, burying the thick head inside her. She gave a low moan and her eyes fluttered slightly."
    $ hentai_scene(8)
    "Her slave didn't stop, though, beginning to piston up into her. He did all of the work while Vehlis just shivered in position, her ass bouncing against his hips."
    "She began to rock her hips as well, getting more of his shaft inside her on each thrust. Her body twisted with the movements, her large breasts beginning to sway and jiggle as she got into it."
    $ hentai_scene(9)
    vehlis "Alright, what do you say w-"
    $ hentai_scene(10)
    "As her eyes shifted back to her slave, they passed over the door. And though it was open only a crack, she didn't miss Sabia watching them. Though her face remained flushed, it instantly regained a look of cool composure."
    vehlis "Can I help you?"
    s "Wh-what? I need to speak with you about business, but you..."
    vehlis "I'm enjoying my property in my own room, and you're intruding."
    s "Yes... but..."
    $ hentai_scene(11)
    "The slave let go of her hips and passively lay back, as if he was nothing more than her seat. Sabia had a feeling that Vehlis had used him this way in the past - she seemed less embarrassed by it than Sabia was."
    vehlis "If you've tracked me here, you're clearly driven. I'll make you a deal - I'll give you an audience, but you get out and let me finish."
    s "I..."
    vehlis "Shoo!"
    $ hentai_scene(12)
    "Though Sabia retreated into the shadows outside the room, she didn't go all the way. It infuriated her that she obeyed, but the woman had the same commanding tone that her mother did. Plus, she couldn't afford to offend the representative of the Bank of Talos."
    "But out of a sense of stubbornness, Sabia refused to stop watching. With her gone, Vehlis seemed to switch right back into the mood, wiggling her hips a little."
    vehlis "Good work, slave, you didn't soften at all."
    $ hentai_scene(13)
    vehlis "Now, let's see what we can do with this..."
    "Vehlis pushed herself up to her feet, letting the slave's cock slide out of her again until only the tip was nestled against her pussy. Once again she teased him a little, a smirk playing at the corner of her lips."
    $ hentai_scene(14)
    call shake ("v")
    $ renpy.pause ()
    "Then she dropped her hips, impaling herself on the cock again. The slave groaned and bucked his hips, but she pushed him back to the couch with a hard thrust of her ass."
    $ hentai_scene(15)
    "While he lay motionless beneath her, Vehlis picked up where they left off, bouncing herself on his lap. She opened her mouth and began to moan freely. Her entire body was undulating now, her breasts heaving in a beautiful display that she denied her slave. At most, he could have seen the sides of her heavy breasts as they bounced."
    "Yet he held on, not coming as Vehlis worked her way closer and closer to orgasm. Sweat covered her body now and her moans became sweeter."
    vehlis "Almost... there..."
    $ hentai_scene(16)
    vehlis "Now!"
    call shake ("h")

    $ renpy.pause ()
    "The slave came on command, his hips jerking as he began unloading into her. Vehlis cried out as she came, her entire body shuddering."
    $ hentai_scene(17)
    "Sabia was surprised that she let the slave come inside her, but judging from her expression, that was what she'd wanted. Vehlis looked down, watching the cum ooze out of her pussy where they were still joined, a pleased expression on her face as she came down from her orgasm and relaxed back against her slave."
    scene bg black with dissolve
    vehlis "Alright, you can come in now."
    $ hentai_scene(18,effect=dissolve)
    s "Alright, I - aah! You said I could come in!"
    $ hentai_scene(19)
    vehlis "You seemed like you were in a hurry. What is it you wanted to talk about?"
    "Vehlis arched an eyebrow primly, as if she wasn't seated on a cock with cum still oozing out of her. And despite the fact that Vehlis was completely naked, Sabia felt as if she was the one who was improper somehow."
    s "Please... this is a serious matter..."
    $ hentai_scene(20)
    vehlis "Is this making you uncomfortable? Alright, give me a moment to dress... you had better make this worth my while."
    if gallery_workaround == True:
        jump gallery
    return


label nevealiochsabia:
    play music sex1 fadeout 2.0 fadein 2.0
    $ hentai_scene(1,"nevesabiaalioch",dissolve)
    "Though Sabia wasn't inexperienced, she hadn't done anything like this. If it had been anyone but Neve, she would have recoiled, but... the elf embraced her eagerly, pulling her in before she could have second thoughts. Sabia felt her own curves sliding against the other woman's and found herself caressing the side of Neve's impressive bosom."
    $ hentai_scene(2)
    n "Mmm, that's nice."
    s "You're so beautiful, Neve..."
    n "Oh, I know it..."
    $ hentai_scene(3)
    n "And this guy knows it too, judging from his cock."
    alioch "I'm just admiring the human. Are you sure you're really a warrior, with this fat ass?"
    n "You want to play that game? Try it out for yourself."
    $ hentai_scene(4)
    "While Sabia watched, Neve slid backward, the globes of her ass sliding around the elf slave's cock. She bounced her ass against him, letting the jiggling caress the sides of his cock. It looked good, even to Sabia, but the whole thing was still strange to her..."
    $ hentai_scene(5)
    n "Why so uncomfortable?"
    s "I'm just, uh... not sure what to do..."
    n "I'd like to feel your touch a little more... I saw your eyes looking, why not give it a feel?"
    $ hentai_scene(6)
    "Though a little nervous, Sabia reached around Neve's waist to grasp one of the cheeks of her ass. It was as soft as she had imagined, her fingers sinking into her silk skin. Neve gave an appreciative murmur, but then shot a glance backward."
    n "How do you like that? You ready to blow your load?"
    alioch "Please. You'll have to do better than that."
    n "Alright, Sabia, let's give him a show!"
    $ hentai_scene(7)
    "Neve began to bounce her hips, letting the curves of her ass tease his cock. She was fully in control of her movements, so Sabia just took the time to grope the other woman's body. She really did have an incredible one; Sabia wondered what it would be like to have the two of them together, without anyone else to distract them."
    $ hentai_scene(8)
    "But Alioch was there, and he was getting quite a show. Sabia couldn't help staring at her fingers, looking very pale as they sank into Neve's darker ass. It was an alluring image even to her - she was surprised the elf slave could keep his cool."
    "He managed, though, just thrusting his hips up in time with their movements and grinding against Neve's ass. Despite the strangeness of it all, Sabia found herself getting warmer and could feel her nipples hardening."
    $ hentai_scene(9)
    n "Is that all, Sabia? Don't you want more of me than that?"
    s "I do, just..."
    n "Go on, then! Show this spineless man how a real woman takes what she wants!"
    $ hentai_scene(10)
    "Trying to give Alioch a confident smile, Sabia reached down and grasped Neve's ass with both hands. As she kept bouncing, Sabia kneaded it, enjoying the softness of her curves."
    $ hentai_scene(11)
    "As Neve moved, Sabia enjoyed the feeling of her hips shifting in her hands. It felt good to feel her muscles sliding like this, not to mention the silky texture of her skin... Sabia understood why men couldn't keep their hands to themselves during sex."
    "But it seemed that Neve was doing more than just sliding against his cock now, she wanted to move to the next step. Sabia helped lift her hips upward, sliding her into position over Alioch's cock..."
    $ hentai_scene(12)
    "Inch by inch, Neve slid down the elf's shaft, giving a slight moan as it filled her. The flush of pleasure on her face made her look even more attractive and Sabia found herself pushing against the other woman harder, desperate for more stimulation."
    $ hentai_scene(13)
    "She couldn't help herself, she pulled one hand back to massage Neve's breast. Her nipples had been getting harder and harder against Sabia's body as she moved, and now they were incredibly hard in Sabia's fingers. Neve gave an appreciative moan."
    n "Sabia is taking some initiative... can't you?"
    alioch "Oh, are you finally starting? If you want initiative..."
    $ hentai_scene(14)
    call shake ("v")
    "Alioch thrust up into Neve's pussy, his hips arching off the bed as he slammed his cock inside her to the base."
    $ hentai_scene(15)
    n "Hmm, is that all?"
    "Despite her confident tone, though, Sabia could feel that Neve was moving her hips on her own, making her ass bounce as they thrust against one another. She kept a cocky smile on her face, but her body trembled slightly in pleasure against Sabia's."
    $ hentai_scene(16)
    "They began fucking each other and Sabia kept caressing Neve, but her attention wandered... until Neve captured her eyes with a smoldering gaze."
    n "Now, why aren't you having more fun?"
    s "Fun? We have to... the supplies..."
    $ hentai_scene(17)
    call shake ("v")
    n "Nonsense!"
    "Neve slid her free hand down and plunged two fingers into Sabia's pussy. Though Sabia let out a cry, she couldn't deny that she was already dripping wet and Neve's fingers felt incredible inside her."
    $ hentai_scene(18)
    "The other woman began gently thrusting her fingers inside Sabia, brushing near her clit but not being too rough yet. Sabia gave a low moan and found her hips bucking into Neve's hand."
    n "There, isn't that better?"
    s "But... the contest... between you two..."
    n "Relax, this is going to make it a lot harder for him to hold back."
    $ hentai_scene(19)
    n "Isn't it, you Arwan pervert? You like seeing her twist on my fingers, don't you?"
    "Alioch didn't answer, instead gritting his teeth. He kept pushing up, slamming against Neve's plush ass, but Sabia could see that it took effort. Did they really look that good together?"
    $ hentai_scene(20)
    "As Neve began bouncing her hips more violently, Sabia realized that they truly did. Their bodies were a perfect mix of curves and muscle, sliding against one another as Neve rode his cock. Sabia began to moan and didn't hold back, telling herself it was to win the competition but really just desperate for more of Neve's plunging fingers."
    $ hentai_scene(21)
    "Unable to help herself, Sabia grabbed Neve's ass again, massaging it roughly. Neve rewarded her with a moan and began moving her fingers faster."
    n "Ah, that's so good... take over, Sabia! Let's fuck him good!"
    $ hentai_scene(22)
    call shake ("v")
    "Sabia jerked Neve's hips down, impaling her fully on his cock. The movement sent a shudder of pleasure all the way up Neve's body, pressing it harder against Sabia's."
    $ hentai_scene(23)
    "All three of them were rocking and moaning now. Alioch pumped upward, Neve bounced her ass against him with each thrust, Sabia twisted and moaned. Neve's fingers were getting so deep, her legs felt weak, but she couldn't stop, she needed more..."
    "Though she was controlling the movements of Neve's hips, Sabia didn't feel in control. She was entirely swept up in the passion of it, losing herself and becoming nothing but ecstatic instinct."
    $ hentai_scene(24)
    "Not thinking about it, Sabia leaned forward and kissed Neve on the lips. For once, she actually surprised the other woman, leading to an awkward moment as their lips pressed together."
    $ hentai_scene(25)
    "But a moment later, Neve gave a low chuckle and kissed back. Sabia opened her eyes, staring directly into the other woman's eyes. They were both moaning and bouncing, yet they managed to connect, staring at one another in a moment of intimacy."
    $ hentai_scene(26)
    "For a time, Sabia lost herself in it completely. Her tongue tangled with Neve's, both of them pressing closer together as they explored each other's bodies. Neve's fingers were sliding deeper now and caressing her clit with each movement, and Sabia wanted it even harder."
    "She could feel Alioch's thrusts rippling through Neve's body, and it only made her hotter. Neve's hips leapt in her hands, her breasts heaved against Sabia's, her fingers jerked inside her... it was as if all three of them were connected."
    "She was burning up now, she couldn't hold out... Neve was moaning as well, giving herself over to the pleasure... Alioch's thrusts were becoming faster and more erratic..."
    $ hentai_scene(27)
    call shake ("h")

    "For a glorious moment, the only thing Sabia knew was the orgasm coursing through her body."
    "Yet as she came down, she could feel that they had gone over the edge as well, their pleasure buoying hers up. Neve's body was still shuddering and Alioch's cum had exploded inside her pussy."
    $ hentai_scene(28)
    "All three of them came down slowly, gasping for breath. Sabia pulled back from Neve and a string of saliva extended between their lips. She didn't even care, she just smiled at the other woman as she basked in the afterglow."
    $ hentai_scene(30)
    n "Hmph. I guess I have no choice but to call that a tie."
    alioch "She was trying so hard, I decided to have pity on you."
    n "Now don't star-"
    $ hentai_scene(31)
    s "Don't fight..."
    "Sabia's voice was soft, but she massaged one of Neve's breasts roughly and pushed her hips down harder against Alioch's exhausted cock. Both of them gave a low groan."
    $ hentai_scene(32)
    "And amazingly, they stopped arguing. Neve held Sabia a little closer and Sabia gladly fell into her embrace, closing her eyes for a moment and just enjoying the aftershocks of pleasure still traveling through her body..."
    if gallery_workaround == True:
        jump gallery
    return


label HGNtekrokscene:
    play music sex2 fadeout 2.0 fadein 2.0
    $ hentai_scene(1,"HGNtekrok",dissolve)
    "Sabia overcame her nervousness and began dancing in front of the orcs, though she was under no illusions that it would end there. Being bare naked in front of so many brutes, wearing nothing but a mask... it sent a thrill through her that was more than just nervousness."
    $ hentai_scene(2)
    "It wasn't long before an orc marched up toward her from behind. His eyes blazed as he stared at her, and Sabia struggled to keep swaying her hips as if he wasn't closing in on her."
    s "W-wait, what are y-"
    $ hentai_scene(3)
    "Instead of answering, the orc reached out and grabbed her ass, stopping her swaying movements cold. Sabia's eyes shot open and she release a small whimpering sound, but she didn't fight back."
    $ hentai_scene(4)
    "She glared back at the offending hand, wishing she could cut it off... but no, that wasn't why she was here. She had known what she was getting into."
    $ hentai_scene(5)
    "Rolling her eyes, Sabia looked away as he began groping her ass, eagerly feeling up the taut globe. There were more orcs coming, too, and she eyed the one pushing to the front of the group."
    $ hentai_scene(6)
    "Sure enough, as soon as she pulled away from the orc molesting her ass, the warrior approaching her was grasping one of her breasts. He squeezed it roughly, his huge fingers pinching around her nipple. She barely held back her yelp."
    $ hentai_scene(7)
    call shake ("v")
    "Metal closed around her wrists and Sabia realized that she had been distracted from their real plans: another orc had clapped manacles around her wrists and tied them to a board overhead."
    $ hentai_scene(8)
    "Now all Sabia could do was hang there, not quite able to stand comfortably, her body on display to all the orcs in the hall."
    s "Look, I didn't s-"
    $ hentai_scene(9)
    orc "You'll do whatever we say, slut."
    "With nowhere for her to retreat, Sabia had no choice but to let the orc push up against her. One of her breasts, nipple still stinging, flattened against his muscular chest. The orc had already discarded his loincloth, his erect cock rubbing up against her stomach as she squirmed."
    $ hentai_scene(10)
    s "Alright, fine. If we have t-"
    $ hentai_scene(11)
    "Without warning, Sabia's mask was torn from her face and tossed aside."
    $ hentai_scene(12)
    "It was a small thing, but suddenly she found herself with nothing standing in between her and the lustful gaze staring down at her. The mask had let her separate herself from the act, just a little, but now she was laid bare before everyone's eyes. Sabia flushed and tried to turn away, but the orc's grip on her head was too strong."
    $ hentai_scene(13)
    orc "Spread your legs, slut!"
    "Just when Sabia thought her position was too embarrassing, the orc made it even worse, hooking his arm under her leg and jerking it into the air. Not only did that let him reach around and squeeze her ass, it made her pussy visible to all the orcs in that direction. She squirmed, but she was also getting wet."
    $ hentai_scene(14)
    s "O-okay, big guy... take it easy with that thing, I w-"
    $ hentai_scene(15)
    call shake ("v")
    "Ignoring her entirely, the orc rammed his cock into her vulnerable pussy. Sabia let out a cry and her body bucked forward, but there was nowhere to go except against the orc's chest."
    $ hentai_scene(16)
    "Not giving her any time to adjust, the orc began thrusting into her repeatedly. Sabia gritted her teeth and tried to bear with it, not fighting the fact that her body was starting to respond."
    $ hentai_scene(17)
    "She lowered her eyes from the orc fucking her, trying to just focus on the sensation. He didn't care, not when he could plunder her pussy while molesting her ass. The other orcs hooted and hollered for him to fuck her faster and her cheeks burned."
    $ hentai_scene(18)
    call shake ("h")

    "He came without warning, simply grunting as his cock pulsed and he began unloading cum inside her. Sabia cried out at the sudden hot rush, but there was nothing she could do."
    $ hentai_scene(19)
    "The orc stayed there for a while, enjoying her tight pussy as he squeezed out the last of his cum. Though she had been reduced to a passive fucktoy, Sabia had still been jerked around enough that she was sweating and her body felt weak."
    $ hentai_scene(20)
    "When the orc left, she sagged in her restraints. She knew that made her breasts swing back and forth, and her ass was jutting out at an angle, but she needed to take a moment to recover before the next orc came for her pussy."
    $ hentai_scene(21)
    "Or her ass."
    "Instead of approaching slowly, the second orc had lunged at her, and Sabia was not prepared. Out of nowhere she had an orc squeezing her tits while his thick cock rubbed between the cheeks of her ass."
    $ hentai_scene(22)
    s "Uh... hey there... are you sure you wouldn't rather fuck my pussy?"
    $ hentai_scene(23)
    orc "Hell no! Me wanna open this tight ass!"
    "The orc loomed closer to her, his rank breath in her face. He didn't stop squeezing her breast or humping against her ass, his cock throbbing with need. There was no way she was getting out of this."
    $ hentai_scene(24)
    "Still, at least the orc didn't violate her asshole instantly. Trying to make the best of it, Sabia tried not to shudder as he licked her face and just focused on the other sensations. He was grabbing her breast as if he owned it, and the feeling of his shaft against her added a little excitement, though she was worried about how it would fit."
    $ hentai_scene(25)
    call shake ("v")
    "It fit. The orc had to ram against her tight anal ring several times, but he eventually managed to plunge inside her, cock sinking deep into her ass. Sabia let out a wail and bucked away from him."
    $ hentai_scene(26)
    "There was nothing she could do as he punched inch after inch of his cock deeper into her ass. Sabia groaned and twisted, but between her bound wrists and the orc's hand on her breasts, she couldn't get any relief."
    $ hentai_scene(27)
    "Eventually she just gave in to it, moaning as the orc's shaft violated her ass over and over. He was moving more easily now, his cock hard and hot as it scraped inside her and set her hips on fire."
    "Sabia began thrusting back, her ass striking against his hips each time he plunged inside her. She arched her back and moaned louder as her ass surrendered to the thick shaft inside it."
    $ hentai_scene(28)
    call shake ("h")

    "By the time he finally came inside her, Sabia was bucking and moaning helplessly. Jet after jet of cum flooded her asshole and she just took it before sagging in her restraints."
    $ hentai_scene(29)
    "The orc stayed inside her, grunting as he delivered seemingly endless pumps of cum inside her. His hands squeezed instinctively and his hips still gave small pumps as he finished. Each one crammed his cock even further inside her sensitive asshole, leaving Sabia panting."
    $ hentai_scene(30)
    "Chuckling, the orc gave her face another long, disgusting lick. After one last squeeze of her breasts, he finally pulled out, his cock dripping cum all over her stretched ass."
    $ hentai_scene(31)
    "That was two, and Sabia already felt like she was on fire. Some of the other orcs were masturbating furiously and she just stared at them through hazy eyes. Who was going to be the third orc?"
    $ hentai_scene(32)
    "Both the third and fourth came at the same time, abruptly trapping her between their muscular bodies. Sabia felt their cocks press against her and could imagine how they would feel pounding inside her."
    $ hentai_scene(33)
    "Resistance was pointless. Sabia gave them a nervous grin and looked at the orc behind her."
    s "Just... just don't be too rough."
    orc "Heh, you're a good slut."
    $ hentai_scene(34)
    "The orc in front of her spoke with a low laugh, running his hand through her hair roughly."
    orc "We'll treat you right. Spread your legs and take it."
    $ hentai_scene(35)
    call shake ("v")
    "Sabia obeyed and they plunged inside her. The two thick shafts rammed deep inside her body, filling her utterly and making Sabia scream out in pleasure."
    "They didn't need to fuck her violently, just filling her up was enough to turn Sabia into a moaning wreck that shuddered in between them, her soft curves sliding against their bodies as they thrust into both her holes."
    $ hentai_scene(36)
    "When the orc behind her leaned down to lick her face, Sabia didn't fight it, turning back to try to suck his tongue into her mouth. Her hips were on fire and the heat was rising through her entire body, turning her into their toy."
    $ hentai_scene(37)
    "The celebration went on more raucously than before, orcs drinking and shouting as she was fucked in their midst. Sabia let her eyes roll back in her head and surrendered to the pleasure as she became their fucktoy for the night..."
    if gallery_workaround == True:
        jump gallery
    return


label HGNdajrabscene:
    play music sex2 fadeout 2.0 fadein 2.0
    $ hentai_scene(1,"HGNdajrab")
    "Though Sabia didn't consider herself a very good dancer, she had an idea of what the orcs wanted. Raising her arms over her head, she began to twist and shake her body. The vines and leaves barely clung to her, leaving her nearly exposed, but she made herself forget about that and keep dancing."
    $ hentai_scene(2)
    "Strangely, the mask helped. She let her nervousness slip away and began to enjoy herself, her body undulating smoothly. It was definitely getting the orcs' attention, but most of them stayed back and just enjoyed the show."
    $ hentai_scene(3)
    "Until abruptly, one of them reached out and grasped her twisting ass. Sabia froze in place. All the other orcs were looking at her and she realized that she needed to decide exactly what she would do now or it would get out of hand."
    s "What... what are you doing?"
    orc "It's a ritual. Gotta touch the Horned God. For luck."
    "That sounded like bullshit to her, but then again... maybe it really was part of the stupid orc ritual. Sabia took a deep breath and made her decision."
    menu:
        "Stop him":
            $ dom += 1
            $ hentai_scene(1,"HGNdajrabA")
            "Sabia stopped dancing and glowered back at the orc, who froze as well. She couldn't let this go on, not if she wanted to be respected."
            $ hentai_scene(2)
            s "Get your hands off me!"
            $ hentai_scene(3)
            "The orc complied immediately, flinching back and retreating. Sabia rolled her eyes and just kept dancing. The orcs drank in the sight of her body, but none of them attempted to touch her as she completed her dance."
        "Keep dancing":
            $ sub += 1
            $ hentai_scene(1,"HGNdajrabB")
            "Rolling her eyes, Sabia decided that this was what she needed to suffer through, in order to keep orcs like these at the feast. The orc chuckled and kept massaging her ass as she returned to her dance. It was nowhere near as smooth with his hands on her, but that obviously didn't matter."
            $ hentai_scene(2)
            "Though she'd known it was coming, Sabia was still startled when another orc reached out and grabbed one of her breasts. She bit back a yelp as he pinched her nipple and pulled her breast upward by it."
            $ hentai_scene(3)
            "Just as she was starting to get used to it, the orcs grabbed at Sabia's outfit, tearing away the vines."
            $ hentai_scene(4)
            "She gasped to be suddenly exposed. The leaves hadn't offered much protection, but they had given things a thin veneer of respectability."
            s "Hey! What do y-"
            $ hentai_scene(5)
            "Even as she was speaking, another one of the orcs tore away her mask."
            $ hentai_scene(6)
            "That left Sabia completely nude in the hall. Flushing, she reached after the mask, but it was too late. She was no longer playing the Horned God, she was just exposed in front of all these orcs."
            $ hentai_scene(7)
            call shake ("v")
            "An orc reached out and slapped her ass, making her yelp and twist forward. It was a perverse mockery of a dance that set her breasts bouncing."
            $ hentai_scene(8)
            "The orc brought his hand down again, this time gripping her ass tightly. Sabia gave a shiver... but kept trying to dance. This was the decision she made, she needed to take it all the way."
            $ hentai_scene(9)
            "It seemed like the orc was satisfied with a good feel, because he let go, leaving his hand print bright on her ass. But Sabia barely had a second to dance alone before another orc reached out and grasped her breast roughly."
            $ hentai_scene(10)
            "Before she had time to adapt to that, another orc slid a hand along her thigh and pulled up, jerking her leg into the air. Abruptly Sabia was tottering on one leg, but the orc gripped her ass, keeping her from losing her balance."
            $ hentai_scene(11)
            "That left her barely balanced, unable to dance, completely at the mercy of the orcs that gripped her. Sabia flushed and stared at them, but they didn't take advantage of her helplessness except to keep groping her."
            "Maybe the first orc really hadn't been lying. The orcs crowding around to touch her definitely wanted more than luck, but at least they kept their cocks in their loincloths."
            $ hentai_scene(12)
            "The lucky orc who got to her first from behind reached out and grasped her free breast, squeezing it tightly. Sabia could barely hold back a low moan and then she was trapped between them, just twisting and shuddering as the orcs had their way with her."
            $ hentai_scene(13)
            "Sabia had no choice but to put up with it. Orc after orc pushed his way in and got a good feel, leaving her body hot and sticky from their sweat. Sabia endured until they'd finally had their fill, then hastily retreated from the hall."
        "Domination: Push him away and invite better orcs" if dom >= 5:
            $ dom += 1
            $ hentai_scene(1,"HGNdajrabC")
            s "Get your hands off me!"
            $ hentai_scene(2)
            "The orc pulled back and the others seemed a little disappointed. Sabia kept rocking her hips and scanned the watching crowd carefully, looking for warriors she recognized. If they really wanted to cop a feel in the name of this ritual, she might as well take advantage of it."
            s "You, and... you. Get up here. Oafs don't deserve any luck in the coming year, but you do."
            "Though the orcs were ones she respected at least a little, they were still orcs. They weren't going to refuse a chance like that and rushed toward her dancing body."
            $ hentai_scene(3)
            "They seized her firmly, but not violently. Sabia kept twisting in her dance as they touched her, keeping a smile on her face. One of them was actually giving her nipple some nice attention, she was beginning to heat up."
            $ hentai_scene(4)
            s "You boys want a little more? Let's get these things out of the way..."
            $ hentai_scene(5)
            "With a flourish, Sabia threw off her mask and the vines, leaving her completely naked in their hands. Maybe not part of the ritual, but judging from how loudly the orcs cheered, a popular move. As she twisted, her two chosen orcs kept touching her."
            $ hentai_scene(6)
            "But before too long had passed, the orcs surged closer, one of them lifting her into the air while the other grasped her breast that was bouncing freely. For a moment Sabia was trapped in their hands, one of her legs pulled off the ground, her position precarious."
            "Part of her hated the idea of them taking advantage of her right then, but another part of her wanted to fuck..."
            $ hentai_scene(7)
            "Fortunately, her chosen orcs only took what she offered, though they took it eagerly and a little roughly. Sabia favored them with a smile and kept twisting in their hands."
            "By the time her dance was done, Sabia's body was burning up. She felt like sexuality incarnate, and every eye in the hall was on her. She hoped that they couldn't see how wet she was getting."
            "When Sabia was done and she slowed down, the orcs let go of her. Sabia gave them another smile, then swept up her mask and darted out of the hall to raucous cheers."
    "Dajrab was nowhere to be seen and Sabia felt vaguely irritated that he'd just left while she was doing all that, but presumably he was doing something important."
    if gallery_workaround == True:
        jump gallery
    return


label badendmurdertrial:
    play music sex2 fadeout 2.0 fadein 2.0
    $ hentai_scene(1,"badendmurdertrial", dissolve)
    "Sabia's head swam, phantoms blurring over reality as she slowly returned to herself. She remembered a long journey, being jostled many times, but it was overwhelmed by a drugged haze and the sweet scent of whatever they had used to keep her down for so long."
    $ hentai_scene(2,"badendmurdertrial", dissolve)
    "Slowly, she managed to concentrate, the world coming into focus around her. She felt her limbs first, tightly bound in strange contraptions that she couldn't budge in the slightest. There was something squirming by her breasts, but Sabia was much more focused on escape. Unfortunately, the sight of an orc watching her removed all hope that she had regained consciousness when they didn't want her to."
    $ hentai_scene(3)
    s "Let me go, you bastard!"
    "The orc watched her with calm, emotionless eyes. He was as old as any orc she had seen, but still tall and strong. There was a magnificent bear fur around his shoulders, marking him as having a high rank, but she wasn't sure exactly what."
    vek "Have more respect, human. You are speaking to Behar Vek."
    s "As if I'd respect you. Let me out of this... thing. Just what are these filthy tentacles?"
    $ hentai_scene(4)
    "She glanced toward the strange tentacles, which were beginning to squirm more purposefully. She could feel a strange sucking sensation on her nipples, and no amount of squirming could relieve it."
    vek "Those \"filthy\" tentacles cost the lives of many warriors to acquire. But now, they should help us collect your milk."
    $ hentai_scene(5)
    s "What the fuck? You vermin are going to {i}milk{/i} me for your sick rituals?"
    vek "You do not need to understand. Your only purpose now is for breeding."
    $ hentai_scene(6)
    s "So this is some kind of fertility magic? You can't imagine it will work... at best you'll get twisted halfbreeds!"
    vek "It will not be orcs breeding you."
    $ hentai_scene(7)
    s "Wh-what?"
    vek "No, we think you will be useful for something much greater. You are a strong warrior, of sturdy Traus stock... perhaps you will survive where the others broke."
    $ hentai_scene(8)
    s "You bastard! You really think you can just use Lundari nobility for experiments like this? They'll crush your little tribe of traitors an-"
    vek "Enough. Behar Vek wanted you to understand your place here. But it is not necessary - begin the process."
    $ hentai_scene(9)
    call shake ("v")
    "Before Sabia could protest, there was a pulse of magic and the tentacles around her breasts squeezed tightly. They wriggled more intensely now, and the sucking sensation increased. A strange warmth blossomed through her chest..."
    $ hentai_scene(10)
    "To Sabia's horror, she felt a thin stream of milk leave her nipples. The tentacles kept sucking, as if they could coax more milk from her, and it seemed that they would be able to. She began struggling harder, but with her limbs locked into place there was little she could do."
    $ hentai_scene(11)
    s "What degenerate filth is this?"
    vek "Save your strength for the breeding. Our pet is not gentle."
    s "What p-"
    $ hentai_scene(12)
    "..."
    call shake ("v")
    "The room shuddered as something came down behind her. Sabia's eyes went wide, hoping that it was just something fallen, but knowing that it had been a monstrous footstep. The high shaman was looking up over her with a strange look in his eyes."
    call shake ("v")
    vek "To prevent the creature from tearing you apart, we have placed it permanently in heat. But that may make it... vigorous."
    $ hentai_scene(13)
    call shake ("v")
    "Sabia desperately tried to look behind her to catch a glimpse, but she was too restricted to be able to see. The stomps were getting closer now and she could hear the heavy breathing of a monster."
    call shake ("v")
    vek "Live and breed, human."
    "The shaman left her cell and locked it as another stomp came down just behind her. Sabia wanted to scream for him to come back, but her jaw was locked in place. The beast had to be just behind her now, and she had no idea what kind of monstrosity was currently behind her helpless body."
    $ hentai_scene(14)
    call shake ("v")
    "The monster pushed up behind her, dropping an obscenely large cock down upon her back. Sabia couldn't help but scream and try to squirm away, but it was useless. All her twisting only earned her a brief glimpse of the horrible beast."
    $ hentai_scene(15)
    "Giving up on escape, Sabia could only shudder in place. The monster's cock felt incredibly heavy, bumps and ridges rubbing against her back as it shifted back and forth. Judging from its snorting and heavy breathing, it wanted to mate, but it seemed to be puzzled by the strange creature they had set before it."
    $ hentai_scene(16)
    "Sabia looked up toward the shaman, who watched from the other side of the bars. She had no pride left, she forced herself to open her mouth and beg."
    s "Please! Anything but this! I'll give y-"
    $ hentai_scene(17)
    "The creature gave a rumbling growl and liquid splattered down over her back. Sabia's eyes widened as she realized that it was the monster's precum. If it could produce that much..."
    $ hentai_scene(18)
    s "Dammit... that thing is going to tear me apart, you're insane!"
    $ hentai_scene(19)
    "The shaman gave no answer, but his eyes shifted from her to the creature. It did seem to be moving, and Sabia glared back angrily as if she could stop it by sheer force of will. It was just a brute creature operating on instinct, maybe she cou-"
    $ hentai_scene(20)
    call shake ("v")
    "An enormous claw slammed down on her back and gripped her tightly."
    $ hentai_scene(21)
    "The sheer power Sabia felt in the creature's claw left her breathless. It could have eviscerated her easily, but instead it was grasping her... in order to mate. Sabia gave up hope of escaping it, her mind desperately searching for options."
    $ hentai_scene(22)
    s "Please... please don't..."
    $ hentai_scene(23)
    "Rearing back, the creature began pushing its cock against her thighs. Though it wasn't very accurate, the shaft was so enormous that it still ended up rubbing hard against every part of her backside. She felt the bumps rub against her pussy several times before it finally got lined up, the enormous head pushing against the opening."
    s "...wait..."
    $ hentai_scene(24)
    call shake ("v")
    "Ignoring Sabia, the monster slammed inside her, and she screamed."
    $ hentai_scene(25)
    "Sabia's entire torso was burning as she squirmed uselessly, impaled on the enormous shaft. The monster felt impossibly large, it should have been tearing her body apart, yet somehow she still lived. It hurt like hell, but the shamans must have done something to her. When she dared to look down, she could see a bulge emerging from her stomach."
    $ hentai_scene(26)
    "But if just having the tip of its cock resting inside her felt like this, Sabia couldn't imagine what it would be like to have it actually fuck her. She glared forward while she still could, eyes spitting hatred toward the shaman as he watched."
    vek "Your mind still remains? Good. Now survive the breeding."
    $ hentai_scene(27)
    "Realizing she couldn't afford to spare any attention, Sabia looked back toward the monstrosity mounting her. It was giving a low growl, apparently uncertain about how much resistance it was getting from her tight pussy."
    $ hentai_scene(28)
    "But after a moment, it pulled its hips back. The ridges of its cock pulled on her strained pussy and Sabia couldn't hold back a whimper. The heat of pain was turning into something else, her body responding against her will. The tentacles sucking on her nipples were still drawing a thin stream of milk and she shuddered, trying to think of any way to escape and giving up."
    $ hentai_scene(29)
    s "Please... gently..."
    "But even if the monster could hear her, she knew it didn't care. It kept shifting its hips, cock stirring inside her. She had a split second of warning as its claws gripped her more tightly, but that wasn't nearly enough."
    $ hentai_scene(30)
    call shake ("v")
    "The cock driving into her again felt like she'd been punched in the chest and Sabia cried out again, her mind overwhelmed by sensation so intense it was neither pleasure nor pain."
    $ hentai_scene(31)
    "Even though it stopped thrusting after that, Sabia was frozen, eyes wide and jaw slack. It was simply too big, forcing her entire body to wrap around the monster's cock."
    "Something was changing inside her, a transformation she was powerless to stop. The tentacles were draining more and more milk from her breasts and she felt as though her pussy was reshaping itself. She bitterly resisted the haze creeping into her mind, but it was only a matter of time."
    $ hentai_scene(33)
    "She hoped that the creature would give up, but as she felt it move, Sabia realized that there was no chance of that. She might be too small for the beast's monstrous girth, but it was beginning to recognize her as something it could fuck. It gave a loud grunt, pulled back, and Sabia whimpered."
    $ hentai_scene(34)
    call shake ("v")
    "Her whimper broke into a scream as the beast finally plunged all of its cock inside her. Sabia felt as though everything inside her had been replaced by the enormous shaft and she was nothing but a thin sleeve in the monster's claw."
    $ hentai_scene(35)
    "Yet somehow, she lived. The tension drained out of her body and Sabia began moaning as the beast thrust against her hips. It had its mate mounted and now it was going to breed her, no matter what."
    "She couldn't bring herself to look down, but she could {i}feel{/i} her body stretching around it. Her normally flat stomach was distorted each time the beast thrust inside her, its cock visible as it pushed into her."
    $ hentai_scene(36)
    "As she surrendered to the inevitable, Sabia felt the heat begin to change. The shaft plunging into her pussy stoked the heat higher until she melted, becoming nothing but a hole for the monster to breed. It disgusted her, but at least it didn't hurt, there was only burning pleasure."
    $ hentai_scene(37)
    "Her breasts throbbed with a new pleasure and Sabia looked down, realizing that she was beginning to fill the tentacles as they sucked more intensely. She had a momentary thought as to what the shamans were collecting it for, but that thought was pushed out by the cock thrusting inside her."
    $ hentai_scene(38)
    "Sabia moaned and bucked as best she could, but it didn't matter, the creature was going to fuck her hard regardless of whether she cooperated. Her juices and its precum had mixed together, making the ridges and bumps of its shaft slick enough to move smoothly inside her. It was grunting louder now as it plowed into her, finally finding a suitable hole to breed."
    "As it began to speed up, Sabia only moaned louder. Her body was already hollowed out by the beast... if it came inside her... the flood would fill her up entirely and there would be nothing left. Feeling the monster speed up, Sabia gave a moan that even she didn't understand and thrust back against it."
    $ hentai_scene(39)
    call shake ("h")

    "The monster gave a triumphant roar as it slammed inside her and erupted. Sabia gritted her teeth and screamed as she felt it pumping her full of more cum than she had ever imagined possible."
    $ hentai_scene(40)
    "It stayed inside her, cock pulsing over and over again as it kept pumping yet more cum into her packed pussy. Sabia was conscious of nothing but the liquid, filling her up and then bubbling out over her ass and rolling down her thighs."
    $ hentai_scene(41)
    "She was nothing but a broodmare for this monster now, and it had bred her. Sabia finally unlocked her jaw and released a low moan. The creature gave a satisfied grunt and pulled back."
    $ hentai_scene(42)
    "She shuddered and came again as it pulled out, her body suddenly feeling empty, even with all the cum inside her. Sabia nearly collapsed then and just basked in the heat of it, but she held on to some fraction of herself."
    vek "Not bad for a first breeding. Let's see how well you do with a second."
    $ hentai_scene(43)
    "Returning to herself just a little, Sabia looked up at him in horror. The shaman didn't even look smug - she wasn't an enemy now, just a female for the monster to breed. Closing her eyes, Sabia surrendered to the sensations still trembling through her hips."
    scene bg black with dissolve
    pause 1
    $ hentai_scene(44,effect=dissolve)
    "There were voices speaking, but Sabia barely even understood that. For too long, there had been nothing for her but the monster's roars and her own moans."
    $ hentai_scene(45)
    "She drifted back to consciousness, but her world was still black. At some point they had covered her eyes, not that it mattered since she was just here to be bred over and over again. Her belly hung heavily beneath her now, swelling with new life, and her breasts constantly released streams of milk as the tentacles sucked at her."
    "Sabia didn't know how long she had been there. They had forced a tube into her mouth that delivered a slow stream of the monster's cum, and it seemed to sustain her. At least, enough for her to remain conscious as she went through an endless cycle of breeding."
    orcshaman "The last monster was the same as the previous spawn. No difference at all."
    vek "Yes. Most disappointing."
    orcshaman "There is nothing wrong with the ritual. Perhaps the minotaur records were legends after al-"
    vek "No, such ancient drawings were not done lightly, they must reflect truth. Minotaurs do not simply invent enemies, they must have faced such winged creatures in the past. We see the results of the ancient rituals in their people today."
    orcshaman "Perhaps another female would be better? Have we captured the Vegardan?"
    vek "...no. The orcs we sent have all disappeared."
    orcshaman "Pity. Then what options do we have? Are there any more rituals that can be done with this one?"
    $ hentai_scene(46)
    "The high shaman didn't answer right away, instead bending closer and removing Sabia's blindfold. It didn't matter, since her eyes rolled in an unfocused manner. She heard their words, but they meant nothing to her anymore."
    vek "No... she has been used up. We might as well just use her to breed more of them."
    orcshaman "Very well. We will release the beast again."
    vek "Pity... we thought this one might be different..."
    $ hentai_scene(47)
    call shake ("v")
    "They left, but Sabia didn't care. All that mattered to her was that she could hear the monster approaching her again. Sabia could barely wiggle her hips, but it didn't matter, she knew it would breed her no matter what."
    $ hentai_scene(48)
    "The enormous claw on her back felt right now. She was more than just a hole to fuck for the monster, she was its broodmare. It grunted as it thrust its cock against her a few times before lining up behind her pussy in a motion that had become familiar."
    $ hentai_scene(49)
    call shake ("v")
    "It plunged inside her and Sabia's eyes rolled back in her head as the pleasure washed over her. At last, she was filled again. It felt good to have new life growing inside her, to be filled with cum, but nothing compared to that enormous cock thrusting inside her."
    $ hentai_scene(50)
    "She stayed there coming over and over again as the beast bred her yet again. Her body had been entirely reshaped to it now: she was everything she was meant to be when she was wrapped like a sleeve around that glorious shaft."
    $ hentai_scene(51)
    "Her breasts swung back and forth from the force, but they couldn't escape the sucking tentacles. As her body prepared to be bred again, more and more milk streamed out of her breasts. Sabia moaned as she felt the moment coming closer and closer."
    $ hentai_scene(52)
    call shake ("h")

    "Finally, the monster's seed began flooding inside her and Sabia's mind went blissfully blank."
    $ hentai_scene(53)
    "She slowly came to as the monster finished emptying its balls inside her. Sabia's reshaped pussy instinctively clenched as best it could, milking the last of it inside her even though she was already thoroughly bred."
    $ hentai_scene(54)
    "When the beast pulled away, Sabia whimpered softly into the muzzle. She felt empty again, but at least she had the cum covering her body and the life squirming within her."
    "That would be enough... until the next time."
    show gameover with dissolve
    pause 3
    if gallery_workaround == True:
        jump gallery
    return


label HGNelmysceneA:
    play music sex2 fadeout 2.0 fadein 2.0
    $ hentai_scene(1,"HGNelmysceneA",dissolve)
    "Elmy stripped off her top and dropped to her knees with a glare. Seeing her act so readily made Sabia smirk a little."
    s "Well, you're eager. Do you not know how blowjobs work, or did you just want to show off your tits?"
    $ hentai_scene(2)
    elmy "I just want this to be over quickly."
    s "Heh, if you say so."
    orc "Stop talking! Pay attention to me!"
    $ hentai_scene(3)
    elmy "Of course. If you'll remove your loincl-"
    $ hentai_scene(4)
    call shake ("v")
    "The orc threw it aside and pushed forward, his cock slapping against the startled catgirl's face. She gave a gasp and pulled away, but the heavy length was too close and kept pressing against her face."
    $ hentai_scene(5)
    "Elmy knelt there, frozen in shock at the green cock still pressing against her face. It was thick enough to cover a significant part of it, and she was obviously thinking about what it would feel like forcing her lips open."
    $ hentai_scene(8)
    orc "Start sucking!"
    s "You heard him, catgirl slut. Suck."
    $ hentai_scene(9)
    "Instead of obeying, Elmy opened her mouth and began to lick the orc's shaft. It was a small act of defiance, utterly futile, and the orc chuckled as he stared down at her, lapping away at his shaft."
    $ hentai_scene(10)
    "Though her face was burning, Elmy focused downward as if trying to forget about everything else and devoted herself to her task. Her body began bobbing slightly as she licked up and down the shaft, lavishing it with attention and covering it in a thin layer of saliva. She did her best, but it wasn't going to be enough."
    $ hentai_scene(11)
    orc "Me said suck!"
    "The orc pulled backward, leveling his length at Elmy's lips. She stared down it, the huge shaft aimed at her face like a battering ram. She shivered a little, her naked breasts jiggling, but knew that it was inevitable."
    $ hentai_scene(12)
    "Leaning forward, Elmy began licking the head of the orc's cock, massaging the sensitive tip with her tongue. She stared up at the orc, hoping her attentions would satisfy him, but saw hunger burning in his eyes."
    $ hentai_scene(13)
    orc "Suck!"
    "Thrusting his hips, the orc hammered his cock forward. Elmy had no choice but to open her mouth, since his cock would have struck her face and knocked her over otherwise. The force of it still made her reel backward a little, gagging on the thick head that now filled her mouth."
    $ hentai_scene(14)
    "Once he had the head inside, the orc paused, groaning as he enjoyed the catgirl's wet warmth. Her lips were stretched thin around his girth and it seemed like she couldn't possibly swallow any more of it, but they all knew that she would."
    $ hentai_scene(15)
    "Resigning herself to it, Elmy focused on the cock in her mouth and began bobbing over his head, giving him more attention with her tongue. The orc's cock tasted filthy and was already leaking precum, but on her knees at such an angle she had little room to retreat and so had to keep sucking."
    $ hentai_scene(16)
    call shake ("v")
    "Taking advantage of her position, the orc thrust again, pushing his cock into the back of her throat. Elmy choked and her throat convulsed, which just increased his pleasure."
    $ hentai_scene(17)
    "But with only a little more of his cock inside her, the orc didn't seem satisfied. Though Elmy went back to sucking as best she could, he scowled down at her."
    orc "Stupid catgirl... me need entire cock sucked, not just the tip..."
    $ hentai_scene(18)
    s "Need some help?"
    "Sabia sauntered closer and took the catgirl's head in her hands. Elmy made a panicked gagging noise, audible even around the cock stretching her mouth so wide. The orc grunted and nodded at Sabia encouragingly."
    $ hentai_scene(19)
    "Though Elmy didn't struggle, she did try to look back at Sabia, hoping for a little mercy. But Sabia was enjoying herself a little too much now and she wasn't about to stop."
    $ hentai_scene(20)
    call shake ("v")
    "Sabia gripped the catgirl's skull and pushed her forward, forcing her to take the orc's cock straight down her throat. It was a tight fit and Elmy gave a muffled groan, but Sabia kept pushing and it managed to fit."
    $ hentai_scene(21)
    "All of them froze, not quite believing that it had fit. The catgirl's throat bulged at the thick length filling it, yet somehow the orc had nearly his entire length inside her. The orc grunted in satisfaction, Elmy stared in shock, and Sabia just pressed her head a little more firmly."
    $ hentai_scene(22)
    "Elmy tried to pull back, but Sabia stopped her, keeping the cock deep inside her throat. She choked there for a while, growing more desperate as she lost air, but Sabia didn't let up."
    $ hentai_scene(23)
    "Soon her eyes were watering and her choking noises got softer. Elmy stared backward, desperate for release, and Sabia decided that she'd had enough. Instead of just letting her free, she gripped the catgirl's head and pulled it back enough for her to finally take a breath."
    $ hentai_scene(24)
    "For some time Elmy took deep breaths, though the orc's cock didn't leave her mouth. Her lips were still stretched wide, so it was difficult for her, but she gasped for air because she knew she wouldn't have long."
    s "You almost got it. Let's try again."
    elmy "Nnnnf!"
    $ hentai_scene(25)
    call shake ("v")
    "Sabia pushed down and the orc swung his hips forward, ramming even deeper into Elmy's throat. Her tail thrashed wildly, but otherwise she was helpless between them."
    $ hentai_scene(26)
    "It seemed impossible, but the orc was finally balls deep inside her mouth. Sabia pushed on the catgirl's head a little harder, but there was nowhere else for her to go. She shuddered as the thick shaft filled her throat, unable to do anything but let it use her as nothing but a wet hole."
    $ hentai_scene(27)
    "The fit was so tight that the orc could barely thrust a little, each movement pushing Elmy's head back against Sabia's hands. Elmy no longer fought back, passively sucking on the cock as it violated her throat."
    $ hentai_scene(28)
    "Finally she seemed to adjust, which only meant that the orc could pull back a little more and thrust better. He grunted as he sawed a few inches into her mouth. To Sabia's surprise, the catgirl slut was beginning to bob her head a little, sucking him off actively despite being so overwhelmed."
    $ hentai_scene(29)
    "After so much time in her tight throat, the orc couldn't last long. He thrust forward eagerly, his balls slapping against the catgirl's chin in an uneven beat as he began grunting louder and louder."
    $ hentai_scene(30)
    call shake ("h")

    "He finally came explosively, flooding the catgirl's throat with his thick seed. She yelped and tried to pull back, but Sabia held her in place, giving her no choice but to swallow it or drown."
    $ hentai_scene(31)
    "By the time the orc had emptied his balls inside her, Elmy was barely responsive. Cum covered most of her face and her eyes had rolled back in her head as she automatically sucked the cock still filling her."
    $ hentai_scene(32)
    "Now that it was finally over, Sabia pulled back, but it didn't matter. Elmy didn't respond until the orc finally pulled out. When he did, the catgirl gasped for breath, hopped up, and rushed away to clean herself. Sabia watched her flee and smirked."
    if gallery_workaround == True:
        jump gallery
    return


label HGNelmysceneB:
    play music sex1 fadeout 2.0 fadein 2.0
    "Seeing nothing immediately demanding her attention, Sabia began making a wider circuit around the feast. Rokgrid had set up a variety of things she didn't know about, including a set of smaller buildings."
    $ hentai_scene(1,"HGNelmysceneB",dissolve)
    "When Sabia peered into one of the buildings, she was surprised to notice a catgirl on her knees before several orcs. She realized that she probably shouldn't be surprised, given what Rokgrid had shown her, but this seemed to be a slightly different arrangement."
    $ hentai_scene(2)
    "Elmy glanced over at her briefly, then looked away, conspicuously ignoring her. Well, that was fair enough, but Sabia found herself lingering."
    $ hentai_scene(3)
    "Looking back to the orcs before her, Elmy gave them a slight smile. She braced her hands better against the floor and arched her back, showing off her surprisingly large breasts. Whatever arrangement they had, it seemed more voluntary than most."
    $ hentai_scene(4)
    "Even so, Elmy gave a slight gasp when the first orc brought out his cock. He set it against her face and began rubbing it, his shaft throbbing as it got even harder."
    $ hentai_scene(5)
    "Gathering herself, Elmy rubbed her cheek against the shaft as if testing its hardness. It looked ridiculously huge next to her face, but it was obvious what she intended to do."
    $ hentai_scene(6)
    "She began by extending her tongue and cautiously licking the shaft. After growing used to it, she began to lap more quickly, her tongue slowly covering the entire length and massaging it skillfully."
    $ hentai_scene(7)
    "After teasing the tip only a little, Elmy headed down, licking lower and lower while maintaining eye contact with the orc. He grunted and shifted as if he had to control himself to make sure he would last. Elmy gave a slight smile but only licked more eagerly."
    $ hentai_scene(8)
    "When she got low enough, she lavished attention all over his balls. She briefly tried to suck one into her mouth, but it was difficult and so she just sucked a little before licking over to the other."
    $ hentai_scene(9)
    "As she grew accustomed to them, Elmy looked back up again, staring into the orc's eyes. It was obvious to all of them that the contents of the balls she was lavishing so much attention on were soon going to be all over her, and that fact made the orc's cock jerk stiffly, bouncing against her head."
    $ hentai_scene(10)
    "Just when it looked like he was getting too close, Elmy pulled back so his cock was just resting against her face. Her eyes flickered to the orcs standing nearby - their cocks were rock hard and they were jerking them as they stared at her display."
    elmy "Alright... let me get started and then you two can come closer..."
    $ hentai_scene(11)
    "The orc pulled back, his cock straining in front of her face. Elmy took a deep breath as she stared down at the thick shaft in front of her, but it didn't look like she was going to back down. Her tail lashed playfully behind her, her self-control unable to hold back her raw instincts."
    $ hentai_scene(12)
    "Locking eyes with the orc again, Elmy began lavishing his cock with attention again. This time she alternated sucking with licking and didn't shy away from the sensitive head. The orc grunted and his hips jerked, but he didn't try to push between her lips, not yet."
    $ hentai_scene(13)
    "Unable to contain himself any longer, another of the orcs pushed forward, his cock bouncing at the side of Elmy's face. Without slowing down her efforts, she looked toward it and then up at him with a playful spark in her eyes."
    $ hentai_scene(14)
    "One of her hands rose and began to stroke the shaft. It looked far too small, not even able to fully wrap around it, but she eagerly began to pump her fingers along the shaft and the orc didn't seem to have any complaints with the catgirl's skillful hand."
    $ hentai_scene(15)
    "As he grunted and began to thrust, Elmy obliged him by pumping her hand along his shaft faster. They soon found a smooth rhythm, even as she kept up her attention on the cock of the orc before her."
    $ hentai_scene(16)
    "The third orc dropped his cock next to her face, where it bounced a few times before straining upwards to point toward her. Elmy's tongue finally faltered a little, though she kept pumping the cock in her hand."
    elmy "All three of you is a little much..."
    $ hentai_scene(17)
    elmy "I'll see what I can do..."
    "Grasping the second cock with her other hand, Elmy shifted into a more comfortable position, now with three massive cocks in her face. She looked a little embarrassed, but after coming this far there was no way any of them were going to stop."
    $ hentai_scene(18)
    "Smiling, Elmy began working all three cocks. Both her hands pumped back and forth, milking the thick members thrusting into them, while she opened her mouth and resumed bathing the head of the central orc's cock."
    $ hentai_scene(19)
    "Though she had all three of them under control, it looked like the act was starting to affect Elmy as well. Her motions became more vigorous, which sent her breasts bouncing. All three orcs were treated to the sight of an eager catgirl on her knees between them, breasts jiggling as she serviced their cocks."
    $ hentai_scene(20)
    "Unable to contain himself, the central orc pushed forward, his cock plunging between Elmy's lips. It spread them so wide they thinned out, but somehow he managed to fit the head of his cock into her gloriously wet mouth. Elmy choked once in surprise, then began sucking."
    $ hentai_scene(21)
    "Adapting to the new rhythm, Elmy looked back up. Her brilliant eyes met each of the orcs' in turn, staring straight back at them as she pleasured them. The orcs were obviously getting closer, hips bucking for more stimulation."
    $ hentai_scene(22)
    "When the central orc pushed even further in, Elmy managed to swallow more of his shaft without skipping a beat. Even as her arms pumped faster and faster, her head bobbed up and down into the orc's thrusts, sucking his cock as if her life depended on it."
    $ hentai_scene(23)
    "Elmy was moaning now, the sound muffled by the cock in her mouth. Sweat shone on her body from the exertion of working all three cocks so vigorously, but she didn't slow slightly as the orcs became more and more erratic, grunting and thrusting wildly."
    $ hentai_scene(24)
    call shake ("h")

    "The first of them came with a roar and that set off the others, all three cocks unloading thick streams of cum. Though surprised, Elmy did her best to drink down the cum in her mouth and accepted the cum that soon plastered her face."
    $ hentai_scene(26)
    "By the time it was done, her face and hair were covered in the orcs' seed. Elmy's eyes were hazy, as if she was overwhelmed by the thick, masculine scent that must be surrounding her. As the orcs at her sides started to pull back, Sabia shook herself, realizing how wrapped up in the scene she had become."
    $ hentai_scene(27)
    "She pulled back as the other orcs did, determined to focus on the feast again. But as she left, she noticed that the central orc's cock stayed in Elmy's mouth, and the catgirl was slowly cleaning it with her tongue..."
    "Shivering, Sabia closed her eyes and forced herself to refocus."
    if gallery_workaround == True:
        jump gallery
    return


label hellhoundsabiaA:
    play music sex1 fadeout 2.0 fadein 2.0
    scene bg black with dissolve
    "Whining eagerly, the hellhound began to tug at Sabia's clothes, claws threatening to cut her. Muttering at the beast, Sabia pulled them off and ducked lower, away from its claws..."
    $ hentai_scene(1,"hellhoundsabiaA",dissolve)
    "Which put her on her knees, face to face with the hellhound's cock."
    "Sabia found herself staring at it, surprised at how red it was. The pointed tip was leaking clear liquid, which threatened to fall on her breasts. Fuck, was she really going through with this?"
    $ hentai_scene(2)
    "The hellhound whined and pushed forward. Its cock would have pushed against her face if Sabia hadn't shifted back slightly. She turned to glare at it, but from this angle she could only see a mass of fur."
    $ hentai_scene(3)
    "That led her to realize that it couldn't see her either. The hellhound was leaving her free around its cock, when it could have tried to pin her down in a helpless position. It really did just want some relief - if it had wanted to hurt her, it could have done so as soon as she entered the cage."
    $ hentai_scene(4)
    "Sabia shifted back to look at the cock bobbing in front of her. The idea made her stomach flip strangely, but after everything that had happened to her... and this hellhound wasn't so bad. She'd probably blown orcs dumber than it."
    $ hentai_scene(5)
    "So she really was doing it. Sabia found herself blushing as she stared at the cock. This time, when it pushed forward toward her face, she didn't flinch away."
    $ hentai_scene(6)
    "Instead, Sabia reached up and hesitantly wrapped her fingers around the shaft and the hellhound gave a whimper of relief. It was much hotter than she'd expected and she could feel the beast's pulse in her fingers."
    $ hentai_scene(8)
    "The hellhound began to whine and scratch at the ground, but it didn't overpower her. Sabia glanced back again, feeling sorry for the poor beast. No doubt most orcs never treated their hellhounds well."
    $ hentai_scene(9)
    "So despite her misgivings, Sabia began to stroke her hand up and down the beast's shaft. The liquid from the tip quickly coated her hand, making it easy to slide up and down the hellhound's cock. It gave an approving growl and pushed forward into her grip."
    $ hentai_scene(10)
    "Building up a smooth rhythm, Sabia pumped her hand on the cock while she looked back toward the hellhound. It was panting now, a sound that struck her as happy. She wasn't sure how she felt about that, but her hand didn't stop moving."
    $ hentai_scene(11)
    "Abruptly the hellhound thrust forward, nearly jabbing her in the face with its cock. Sabia scowled and tried to hold it back, but her hand was so slippery that the hellhound was able to thrust between her fingers. It kept going, demanding more stimulation."
    $ hentai_scene(12)
    "Her irritation faded away as she felt the beast's desperation. It really did seem to need relief, so perhaps she... plus, at this rate, it might get even more aggressive if she didn't do something."
    $ hentai_scene(13)
    "With a shuddering breath, Sabia leaned forward and sucked the tip of the hellhound's cock into her mouth. She could only get part way down the shaft before it stretched her jaw wide and the pointed tip nearly choked her."
    $ hentai_scene(14)
    "Sabia gently stroked the base of the shaft while she kept sucking. She was even more vulnerable in this position, if the hellhound tried to thrust down her throat... but it was back to panting again, just enjoying her mouth."
    $ hentai_scene(15)
    "Deciding she could trust it for now, Sabia devoted her full attention to the hellhound's cock. She sucked as intensely as she could, her tongue playing all over the strangely-shaped tip. Meanwhile, her hand never let up massaging the rest of the shaft and the throbbing spheres at the base."
    "The hellhound began bucking slightly, forcing Sabia to shift her head back and forth to keep sucking. It made her breasts bounce, and she realized with a rush of shame that her nipples were rock hard."
    $ hentai_scene(16)
    call shake ("h")

    "At that moment, the hellhound came explosively, cum shooting down her throat. Sabia gagged in shock, barely able to keep up with the flood."
    $ hentai_scene(17)
    "Some time later, Sabia still sucked on the beast's cock in shock as it twitched out a few more streams. The hellhound's cum tasted strange, a sharper taste than she had expected. Huge amounts had overflowed her stretched lips, covering her chest and dripping from her breasts."
    $ hentai_scene(18)
    "As she slowly pulled back, Sabia stared down at the cock between her lips. It was a beast's, but the experience overall hadn't been too different. She'd... really done it."
    $ hentai_scene(19)
    "At last she pulled back, withdrawing the cock from her mouth. It was still firm, but no longer painfully hard as it had been before. She stroked it lightly and the hellhound gave a pleased bark."
    $ hentai_scene(21)
    "Well, at least it was happy. It would have been a waste to do all this for nothing... though Sabia found herself a little glad that she had given the poor creature a bit of relief."
    $ hentai_scene(20)
    "It pushed against her, possibly affectionately and possibly wanting more, so Sabia prepared to scramble out. She'd have to hope that this had been enough."
    if gallery_workaround == True:
        jump gallery
    return


label RGAvehlissex:
    play music sex1 fadeout 2.0 fadein 2.0
    $ hentai_scene(8,"RGAvehlissex",dissolve)
    "Sabia got into position, rubbing the fake cock between the globes of Vehlis' ass. She still looked good, but the metal was a little cold and the dildo just felt awkward."
    vehlis "See what I mean? It's not as comfortable as you'd hope."
    s "This feels magic, we must be missing something..."
    "The fact that it didn't work really irritated Sabia, since she {i}really{/i} wanted to fuck Vehlis. The other woman still lay in her comfortable position, at a perfect angle to enjoy. Sabia felt another surge of lust..."
    $ hentai_scene(10)
    "And the gemstones on the straps began to glow with power."
    vehlis "Well! That feels different, did you do something?"
    $ hentai_scene(11)
    "Instead of answering, Sabia gave a low moan and nearly fell forward onto the bed, steadying herself on Vehlis' ass. The metal no longer felt cold, it was filled with a warmth that seeped into her. The cock itself felt different... though she didn't feel anything through it, she felt a surge of pleasure when she pushed against Vehlis."
    s "I think... it's activated by desire..."
    vehlis "No wonder I couldn't figure it out by testing, then."
    "But though Vehlis spoke in a calm voice, Sabia could see that her face was more flushed than before. Her hips squirmed a little beneath Sabia, indicating that she was getting some pleasure from the device as well."
    $ hentai_scene(12)
    "Sabia reached down and grasped Vehlis' plush ass firmly, rubbing herself against it harder."
    s "You feel that? It feels just as good for me. I need you to promise no defensive magic is going to zap me, because I don't think I can hold back on fucking you much longer..."
    vehlis "If it keeps feeling this good, you have nothing to worry about."
    $ hentai_scene(13)
    call shake ("v")
    "Good enough. Sabia pulled back and rammed the strap-on into Vehlis. Both women immediately gave out low moans, Vehlis shuddering in pleasure while Sabia nearly fell forward from the flood of pleasure rushing through her hips."
    $ hentai_scene(14)
    "She had wanted to start thrusting immediately, but Sabia had to pause. She just held the strap-on inside Vehlis for a while, getting used to the little thrills of pleasure as her pussy clenched around it. If this was how it felt to have a cock... no, maybe this was what men meant by good pussy."
    $ hentai_scene(15)
    vehlis "Enjoying yourself? You might as well start moving, since it's not like you can come prematurely..."
    s "Give me a bit..."
    "Sabia got a better grip on Vehlis' ass, enjoying the combination of tautness and softness. All the lust that had brought her here welled up again as Sabia looked down at her. She couldn't let this chance go past her."
    $ hentai_scene(16)
    "Thrusting steadily, Sabia began to pound into Vehlis' pussy, drawing more moans from both of them. Each thrust sent so much more heat through her, Sabia couldn't stop. Almost even better, she saw the effect it was having on Vehlis and enjoyed watching the woman's ass jiggle as she fucked her."
    $ hentai_scene(17)
    "Reveling in the fantastic sensations, Sabia fucked Vehlis until they were both dripping with sweat. The sight of her luscious body glistening like that... Sabia bit her lip hard to avoid coming. She had a feeling it would be intense and she'd be too sensitive for more."
    "Yet she couldn't stop pumping her hips into Vehlis. Sabia opened her mouth and spoke through the moan."
    s "I'm... almost..."
    $ hentai_scene(18)
    vehlis "Then go harder! This is good... bury it! Take me over the edge!"
    "Sabia obeyed, slamming her hips even harder. Vehlis' soft ass was the perfect thing to pound against, the metal between them so hot it was like there was nothing at all. They were joined, their pleasure rising, higher and higher..."
    $ hentai_scene(19)
    call shake ("v")
    "Sabia screamed as she came, unable to hold back her voice even slightly. Her hips shook back and forth wildly as the pleasure took her and consumed her entire body. It was so intense she was barely aware of Vehlis as the other woman trembled and came along with her."
    $ hentai_scene(20)
    "When it was over, Sabia could only stand there, strap-on still deep inside Vehlis, her chest heaving as she panted for breath. But it was fine, the other woman obviously needed a moment to recover as well."
    $ hentai_scene(21)
    "Finally Sabia pulled out, dropping the strap-on onto Vehlis and leaning forward on her a little. Its length was completely soaked with juices from Vehlis, which dripped all over her back. Though the stones were fading and the sensations with them, Sabia still felt a little thrill when Vehlis wiggled her hips back against the toy."
    vehlis "I take it that was good for you?"
    s "Fantastic. I can barely stand."
    $ hentai_scene(22)
    vehlis "Let me just make an annotation..."
    s "Really? After that? What could possibly be so important?"
    $ hentai_scene(23)
    vehlis "Making a note that I should raise the price. That was a... ringing endorsement of the product."
    s "Heh. But is that all this was?"
    $ hentai_scene(21)
    vehlis "I hope you're not expecting me to get all mushy on you. But... you weren't bad, Sabia. I don't let very many people take charge, but you didn't waste the opportunity."
    s "Another time, then?"
    $ hentai_scene(23)
    vehlis "Heh, we'll see."
    if gallery_workaround == True:
        jump gallery
    return


label RGAdisqualification1:
    play music sex1 fadeout 2.0 fadein 2.0
    orc "Strip and bend over the table, slut."
    scene bg RGAint with dissolve
    $ hentai_scene(1,"RGAdisqualificationA",dissolve)
    "Sabia did so, trying not to scowl too much. She hated the idea of what she knew was coming, but since she didn't have another way of staying in the arena and the orc was technically doing her a favor... Sabia bent over the low table and shifted her hips into position."
    $ hentai_scene(2)
    orc "Hey, hey. Don't just stand there like a table or somethin'."
    $ hentai_scene(3)
    s "Isn't this what you want? Get it over with, bastard!"
    $ hentai_scene(4)
    orc "Nah. Me wanna hear you beg."
    s "Wh-what?"
    orc "Beg me to fuck ya. Or you don't get to go on."
    $ hentai_scene(5)
    "Sabia growled, but she didn't have many options. She shifted her hips, suddenly uncomfortable in her nakedness. Just letting him use her body was one thing, but making her beg?"
    "Trying to fight down the flush on her cheeks, Sabia swallowed her anger and tried to speak."
    $ hentai_scene(6)
    s "Alright... please come over and fuck me..."
    $ hentai_scene(7)
    "His hand slapped down on her ass, making Sabia yelp. Fuck, his hand felt big..."
    orc "Do better. What you want me to do?"
    $ hentai_scene(8)
    s "Guh... get your orc... get your filthy orc cock over here and fuck my pussy!"
    $ hentai_scene(9)
    orc "Better!"
    "The orc pushed up behind her, thrusting his cock in between her thighs. Sabia gave an undignified yelp and tried to squirm away on instinct, but that only made her twist around his cock, which was even worse. And worst of all, she could feel her pussy getting wet..."
    $ hentai_scene(10)
    "Sabia looked back toward the orc as he slowly pushed back and forth in between her thighs, the length pressing up against her stomach. She could feel his length throbbing against so much of her skin... he was a big one. The idea of him sticking that thing inside her."
    $ hentai_scene(11)
    "Abruptly the orc reached down again and began massaging her ass. But he didn't pull back to fuck her yet... was he still not done?"
    orc "Better... your slutty human cunt is made for orc cock. Don't forget it."
    $ hentai_scene(12)
    "Sabia looked away from him, trying to ignore his words and pretend that she wasn't getting wet. Couldn't he just fuck her already?"
    orc "Looks like you're out of practice... need to loosen you up a bit..."
    $ hentai_scene(13)
    call shake ("v")
    "His other hand came down on her ass... and his finger plunged into her asshole. Sabia gave a shuddering gasp and jerked forward, but she had nowhere to go."
    $ hentai_scene(14)
    "After the initial shock faded, Sabia was still left stunned. She'd just wanted to trade her body quickly, yet here he was teasing her pussy while he shoved his thumb into her ass. It wormed around so strangely, toying with the tight ring of muscle. It hurt, but not as much as..."
    orc "Huhuhu... that made you get wetter... your cunt is almost ready again..."
    $ hentai_scene(15)
    s "Just... just get it over with."
    orc "First, admit you're a human whore."
    s "B-bastard..."
    $ hentai_scene(16)
    orc "What was that?"
    "His finger shoved deeper inside her, making her squirm around his cock. Her juices were dripping down her leg now, yet the orc didn't stop taunting her."
    $ hentai_scene(17)
    s "Dammit..."
    orc "Me was gonna fuck your pussy... maybe you like it up the ass?"
    $ hentai_scene(18)
    s "No. I... I'm a human whore..."
    orc "Who lusts for orc cock."
    s "...who lusts for orc cock..."
    $ hentai_scene(19)
    orc "Good!"
    "His thumb finally left her ass, leaving it smarting. Instead he grabbed her hips, more seriously this time. Sabia was almost ready for some new humiliation, but his cock seemed even harder than usual against her stomach..."
    $ hentai_scene(20)
    call shake ("v")
    "Finally he thrust inside her pussy, and Sabia immediately let out a wail of pleasure. She couldn't help it, all the taunting had left her flushed and desperate. As his cock plunged so deep inside her, all she could do was spasm around it."
    $ hentai_scene(22)
    "Fuck, he felt even bigger than she imagined. Sabia stared backward at the orc as he groped her ass a little more, just enjoying her tight pussy. She needed him to go harder, he was taking too much time..."
    s "Please... please fuck me..."
    $ hentai_scene(23)
    "Grunting in satisfaction, the orc began truly hammering into her pussy, savagely pounding against her ass. All Sabia could do was grip the table and try to hold herself in place, moaning all the while."
    "Soon her entire body was covered in sweat. Her breasts swung back and forth wildly, tossing drops of sweat to the floor. Yet all she could focus on was the way her body clenched around his cock..."
    orc "Hu... not bad, but me try..."
    $ hentai_scene(24)
    "Just as Sabia was starting to fall into a rhythm, the orc shoved his thumb back into her ass. Sabia grunted and pitched forward, but she was trapped on his cock and could only suffer his thumb pushing into her."
    orc "That's good... you tightened up real good..."
    $ hentai_scene(25)
    s "Just... just get it over with..."
    orc "That's right. Me gonna wreck this pussy."
    "He began plunging into her with greater intensity, plumbing the depths of her pussy even as he toyed with her ass. And to Sabia's shock, the pain slowly gave way. She found herself twisting and clenching around his cock every time he shoved his thumb deeper."
    $ hentai_scene(26)
    "By the time his thumb was fully inside her, Sabia could only shake and moan with her eyes rolled back in her head. The orc stared down at her and grunted happily."
    orc "That's a good fucktoy. You deserve a reward..."
    $ hentai_scene(27)
    call shake ("h")

    "When he finally came, Sabia couldn't resist the flood of cum. The heat of his seed, his cock stretching her, his thumb exploring her ass... it overwhelmed Sabia and she screamed out her pleasure."
    $ hentai_scene(29)
    orc "Whew..."
    "The orc finally took his hands off her, just standing back and enjoying his cock inside her pussy as his cum oozed out. Sabia wanted to crawl away, but since she'd come this far, she had to see it through to the end."
    orc "Alright, slut. You going to thank me? Do it properly."
    $ hentai_scene(30)
    s "Thank... thank you for filling my slutty human cunt with your cock."
    orc "Huhu... you do learn fast..."
    "Sabia finally pulled away from him, cum rolling down her thighs as she struggled to walk properly and ignore the stinging in her ass. This had better be worth it..."
    if gallery_workaround == True:
        jump gallery
    return


label RGAdisqualification2:
    play music sex1 fadeout 2.0 fadein 2.0
    scene bg RGAint with dissolve
    $ hentai_scene(1,"RGAdisqualificationB",dissolve)
    "Once more, Sabia found herself bending over the table with her ass out. This time the administrator orc walked around in front of her, his cock already upright and throbbing."
    $ hentai_scene(2)
    "Okay... you want a blowjob this time? I can do you first, then him."
    orc "Do better, slut. What do you want me to do?"
    $ hentai_scene(3)
    "Sabia grimaced, pissed off that he was playing this game again. Better to just get it over with quickly, then."
    s "I want you to shove your orc cock into m-"
    $ hentai_scene(4)
    "Without warning, the guard pushed up behind her, his cock sliding past her slit and up her stomach. Sabia gasped in surprise, then struggled to hold back pleasure as he began to grind against her just a little."
    $ hentai_scene(5)
    s "H-hey! Wait your turn!"
    orc "Nah, me not want to wait. Me heard you a good slut."
    $ hentai_scene(6)
    orc "Me heard {i}all{/i} about last time."
    "Sabia winced at the feeling of his thumb pushing into her asshole, squirming at the slight tingling pain. But there was even less space to escape this time, as shifting forward only pushed her into the other orc's cock. He chuckled and pushed it against her face a few times."
    $ hentai_scene(7)
    orc "A human slut like you wants as much orc cock as possible, right?"
    s "W-wait..."
    $ hentai_scene(8)
    "Ignoring her rising flush and the way her pussy was getting wet all over the orc's cock, Sabia managed to glower up at the orc in front of her."
    s "Wait, dammit! We never agreed to anything like this!"
    $ hentai_scene(9)
    orc "Oh yeah? Seems to me that dirty cheating whores don't have room to negotiate..."
    $ hentai_scene(10)
    "He had her head firmly gripped with both hands, making it impossible for Sabia to escape even if she tried. His cock was still bobbing in her face, while the other orc humped between her thighs."
    orc "Now, what does a good human slut say?"
    $ hentai_scene(11)
    s "I'm not going to be-"
    $ hentai_scene(12)
    call shake ("v")
    "Her words cut off as the orc jerked her head forward and rammed his cock between her lips. Sabia thrashed wildly, unable to do anything but choke as he fed an enormous amount of orc cock down her throat."
    $ hentai_scene(13)
    "When he finally maxed out, she had most of his length down her throat, barely fitting. Sabia glowered, but she was glowering at his stomach. The huge cock had her pinned firmly in place. Not only that, the orc behind her had taken the opportunity to shove his thumb even deeper into her ass."
    $ hentai_scene(14)
    "Unable to fight back or argue, Sabia could only hang there in between them, trying not to choke and hoping they got on with it."
    $ hentai_scene(15)
    "Fortunately, the orc behind her didn't seem as patient. He had been humping eagerly between her thighs and against her stomach, but now pulled back, lining himself up with her dripping slit."
    $ hentai_scene(16)
    call shake ("v")
    "He didn't wait any longer, he just thrust inside. Sabia's scream was cut off by the thick girth in her mouth as she was fully impaled on long orc cocks."
    $ hentai_scene(17)
    "Both orcs wasted no more time, pounding into her from both sides. Her hands on the table were almost useless now, as her body was thrown back and forth like a doll. They had no technique, they just used her holes hard and fast."
    $ hentai_scene(18)
    "But both of them had stamina, and Sabia was running out of air as the thick orc cock kept invading her throat. She gasped and gurgled, only partially in pleasure, but that was the most she could do to make her desperation known."
    $ hentai_scene(19)
    "Just when she thought she couldn't hold on any longer, the orc finally pulled out. Sabia gasped desperately for air, not even caring that her face was filthy and saliva still connected his cock to her mouth."
    $ hentai_scene(20)
    "Behind her, the other orc didn't skip a beat. Despite nearly falling unconscious, Sabia was beginning to heat up, moving her hips back against him despite her best efforts at remaining in control. The orc was happy to take full advantage, still toying with her ass as he pounded into her pussy."
    $ hentai_scene(21)
    "Sabia turned her attention back to the cock in front of her, knowing what was to come. There was no point fighting it, so Sabia opened her mouth wider and waited for him."
    $ hentai_scene(22)
    "Sure enough, he took the opportunity to slam into her mouth again. Sabia shook back and forth, nothing but a piece of meat for the two orcs to holster their cocks inside. Both of them were speeding up now, grunting loudly."
    $ hentai_scene(23)
    call shake ("h")

    "They exploded at the same time, jet after jet of hot cum filling her. Already reduced to holes, all Sabia could do was take it as she was filled, then overfilled."
    $ hentai_scene(24)
    "When they were finally done, all she could do was hang between them, her arms limp and barely supporting her. Only the two hard cocks inside her kept her from slumping to the table."
    $ hentai_scene(25)
    orc "You see? What did me tell you?"
    "The head orc pulled out, letting her gasp for air again. The other one stayed inside her, tugging her hips closer to enjoy her cum-packed pussy. He chuckled and agreed with the other one."
    orc "Human cunt is great. Good luck in your next match..."
    "Still gasping for breath, Sabia couldn't muster a retort."
    if gallery_workaround == True:
        jump gallery
    return


label RGAdisqualification3:
    play music sex1 fadeout 2.0 fadein 2.0
    scene bg RGAint with dissolve
    $ hentai_scene(1,"RGAdisqualificationC",dissolve)
    $ hentai_scene(2)
    "Once again, Sabia found herself bent over the table for the orcs. It really made no sense that she had lost three times, but that was how it went. There would be three orcs this time, and she had no doubt they would come at her aggressively."
    $ hentai_scene(3)
    "The head orc swaggered in front of her, bouncing his cock on her face a few times, but Sabia just looked up at him."
    s "Alright, what do you want me to say this time?"
    orc "You don't need to say anything..."
    $ hentai_scene(4)
    orc "You just need to get fucked!"
    "The second orc lunged on top of her, completely blocking off all hope of retreat. His muscular body pressed into her hard, his cock insistently pushing against her thigh and covering it with precum. Sabia shivered at the abrupt assault... especially given how he was lined up behind her."
    $ hentai_scene(5)
    s "N-now wait a minute... surely you do-"
    orc "Gonna fuck this sweet ass! They've been training it for me!"
    $ hentai_scene(6)
    s "Stop it! I'll not be used lik-"
    $ hentai_scene(7)
    "Sabia cut off with a swallow as the orc grasped her waist, his enormous hand easily controlling her movements. He wasn't even trying to shut her up, just getting a good grip for what was going to come next."
    $ hentai_scene(8)
    s "Wait... are you really going to let him...?"
    $ hentai_scene(9)
    call shake ("v")
    "She got no answer except the orc's cock plunging into her ass. After having been teased so much, the ring of muscle gave way almost instantly, letting him hammer inside. Yet it was so much thicker than their thumbs that Sabia couldn't help but scream."
    $ hentai_scene(10)
    "Even after he'd penetrated deep into her bowels, Sabia was left gasping and struggling. It felt far too big, her ass was burning... and yet the pain was already becoming a heat that flowed through her, and her pussy was dripping wet."
    $ hentai_scene(11)
    s "Hey! Take it easy!"
    $ hentai_scene(12)
    orc "You're not very bright. Good holes, though."
    "The orc grasped her head, but just toyed with her hair instead of fucking her face. Sabia glowered at him, since it left her with nothing to focus on but the huge cock in her ass."
    $ hentai_scene(13)
    "She let out a grunting scream as the orc began to pump into her, turning her resisting ass into a hole for him to fuck. It hurt... but it hurt so good."
    $ hentai_scene(14)
    "Soon Sabia could only gasp and moan, shuddering underneath the orc as he rammed into her ass over and over. She was panting for breath, her mouth hanging open before the leader's cock, but he just kept waiting..."
    $ hentai_scene(15)
    "At that moment, the guard from before moved up, grasping her hips and thrusting his cock between her thighs again."
    $ hentai_scene(16)
    "Sabia gasped and looked backward toward him."
    s "Wait... there's not enough room for both of you back there..."
    orc "Don't care. Want human cunt again."
    $ hentai_scene(17)
    "The leader grabbed her head with his other hand, pulling her toward his cock more insistently. He gleefully leered down at her."
    orc "We're going to use all your holes today, slut. What do you say about that?"
    "Sabia didn't say anything. It was useless to resist, all she could do w-"
    $ hentai_scene(18)
    "At the same instant, the leader impaled her face on his cock and the orc behind her thrust straight into her pussy. Sabia let out a strangled yell as she was filled up in all three holes."
    $ hentai_scene(19)
    "She felt unbelievably full... Sabia was completely impaled on orc cocks and held up by their huge hands... she could hang loosely and it wouldn't matter - they controlled her body completely. She felt stretched too tight, there couldn't be room inside her for all of them, and yet..."
    $ hentai_scene(20)
    "And yet they didn't start fucking her right away, instead just enjoying the feel of her, shifting into position to get even deeper. Sabia hadn't gotten a good breath and was already straining for air, yet there was no relief in sight."
    $ hentai_scene(21)
    "When they began to thrust into her, Sabia had no strength left to resist. Her ass gave way, endlessly violated by one cock. Another fully claimed her pussy, forcing it to wrap around it as she spasmed in pleasure. And the leader was happy to make use of her mouth, staying deep inside her throat as he thrust his hips back and forth."
    $ hentai_scene(22)
    "He finally pulled back to give her some air and Sabia gasped... and then began to moan. The sensations were too intense, she couldn't resist any longer. Sweet moans kept emerging from her mouth despite her best efforts."
    $ hentai_scene(23)
    "Swallowing, Sabia finally submitted to the pleasure. She loved it, wanted to feel them fuck her even harder. She pushed her hips back into their thrusts and moaned louder."
    $ hentai_scene(24)
    "Right up until the moment that the leader thrust back into her mouth and she was gloriously full again. Sabia just hung there and let them fuck her, drifting in the sensations."
    "How long it went on, she couldn't have said. Her strength was gone, she had come several times, and yet they just kept pumping inside her."
    $ hentai_scene(25)
    call shake ("h")

    "When they finally came inside her, Sabia moaned so loudly that it could be heard even over the cock flooding her mouth with cum."
    $ hentai_scene(26)
    "She had already been filled to bursting with their cocks, so their cum quickly overflowed. Sabia felt it all over her, hot as it flowed down her body, and that made her orgasm again, her holes convulsing around their cocks and milking out the last they had."
    $ hentai_scene(28)
    "The orcs began to pull away, enjoying their last spurts inside her. Sabia was allowed to breathe again and gasped for breath, her chest heaving as she tried to recover from the experience. The orcs were laughing and joking about her, but she couldn't even hear their words..."
    if gallery_workaround == True:
        jump gallery
    return


label RGAnevelutvrogS:
    play music sex1 fadeout 2.0 fadein 2.0
    $ hentai_scene(1,"RGAthreesomeS",dissolve)
    "Before Sabia could do anything, Neve was diving on top of her, grabbing at her clothes. Soon Sabia was flat on her back, completely naked, with the elf on top of her. She flushed and squirmed a little, but she didn't struggle."
    $ hentai_scene(2)
    n "You're not complaining, are you? You look like you could use some stress relief."
    $ hentai_scene(3)
    s "I... no, but... what are we...?"
    $ hentai_scene(4)
    "Neve reached down and clasped her hand, folding their fingers together but also pinning Sabia's arm to the ground."
    n "You just lie back and relax, we'll take good care of you. Lutvrog, get that dick over here."
    s "But..."
    $ hentai_scene(5)
    "Her words were cut off when Neve slid a hand down between them, her fingers sliding into Sabia's pussy. They made a wet noise and slid deep easily, prompting Neve to chuckle and pull back to her outer lips, just teasing her."
    n "Heh, well, you're definitely ready."
    $ hentai_scene(6)
    "All Sabia could do was moan and squirm, unable to deny what she was feeling. Neve felt fantastic on top of her, both feminine curves and powerful muscle. Their breasts were pressed up against one another, her nipples hard against Neve's softness."
    $ hentai_scene(7)
    "Without warning Neve bent down, capturing Sabia's lips in a kiss. Sabia gasped, which only opened her mouth for Neve's tongue."
    $ hentai_scene(8)
    "A moment later, Sabia surrendered to it, falling into the kiss. Her hips were beginning to buck involuntarily now, seeking more of Neve's stroking fingers. It felt too good, she wanted to just let herself melt away in it..."
    $ hentai_scene(9)
    "When Neve finally pulled back, all Sabia could do was lie there and gasp for breath. Neve looked like a goddess propped up over her, staring down at her lustfully, saliva still connecting their lips for a brief moment."
    "Normally she might have said something, but she couldn't find enough breath to speak. Instead she just squirmed her hips, trying to rub her pussy against Neve's. Both of them were soaking wet, but she needed stimulation..."
    $ hentai_scene(10)
    n "Come on, Lutvrog... surely you want to join in after seeing all that?"
    $ hentai_scene(11)
    "Sabia swallowed audibly as he got on his knees behind them, his cock rock hard from their display. God, that thing was going inside her... inside both of them? Sabia didn't know how this was going to go and found her hips squirming more vigorously."
    $ hentai_scene(12)
    n "Shy? Don't worry, we'll take good care of you..."
    "Meanwhile, Lutvrog grasped Neve's ass firmly, enjoying squeezing it as he slid his cock along both of their slits, covering it in their juices. Neve's fingers had gotten her so worked up, Sabia couldn't bear it, the heat inside her growing ever more intense."
    $ hentai_scene(13)
    call shake ("v")
    "When he finally thrust inside her, Sabia let out a scream of pleasure. She squeezed Neve's hand tight and her entire body bucked upward into the other woman as the cock sank so deep inside her."
    $ hentai_scene(14)
    "Even when he fully hilted inside her and stopped moving, Sabia found that all she could do was gasp for breath. She had felt it before, but his cock still spread her so wide... she didn't know how she could take it, her pussy spasming around his shaft."
    "Neve chuckled, then bounced a little, urging Lutvrog on. Sabia opened her mouth to say something, but it was too late."
    $ hentai_scene(15)
    "As he began to thrust steadily inside her, Sabia moaned in pleasure. She wanted to squirm away from the intense sensations, but Neve on top of her kept her in place, pounded by the thick cock. The other woman's nipples were growing even harder as she watched Sabia's pleasure."
    "All her resistance melted away. Sabia bucked her hips harder and harder until she found herself coming, helplessly shuddering between the two warriors."
    $ hentai_scene(16)
    "Mercifully, Lutvrog stopped thrusting and let her enjoy the afterglow, his cock just resting inside her. Neve glanced over her shoulder at him."
    n "Looks like she's down for the count already. Want to continue sparring?"
    $ hentai_scene(17)
    lut "Of course."
    "His cock slid from Sabia's pussy, drawing a low moan from her. Instead he rubbed it against Neve's slit, while groping her taut ass."
    $ hentai_scene(18)
    "He didn't tease long, though, soon sliding his cock inside Neve's pussy. Though he went in slowly, Sabia watched as Neve's eyes widened and she took a shuddering breath of pleasure. Now it was her turn to squirm, her body twisting on top of Sabia's. It felt good, better than she imagined."
    $ hentai_scene(19)
    "When Lutvrog started thrusting, Sabia was the first one to moan. She could still feel his thrusts: Neve's body rubbing her slit, his balls slapping her ass, the force of the thrusts rippling through their bodies."
    "Though Neve was soon moaning in pleasure, Sabia was the one moaning most wantonly. Her desire was becoming a raging fire, stoked higher as she watched and felt Neve get fucked on top of her."
    $ hentai_scene(20)
    "When Neve bent down to kiss her again, Sabia was only surprised for a moment. More by the intense pleasure that flowed through her than the kiss itself."
    $ hentai_scene(21)
    "She gave herself to it, kissing back as she stared into the other woman's eyes. Neve chuckled into their kiss, then began moving more vigorously."
    "Bracing her hands and pushing her bust against Sabia's, Neve could pump her hips back even harder. That let her move harder into Lutvrog's thrusts... and also pushed her harder against Sabia's pussy."
    "Sabia heard Neve moan as she came..."
    $ hentai_scene(22)
    call shake ("v")
    "And an instant later Lutvrog hammered inside her, all the way to the hilt. Sabia screamed into Neve's mouth as she came helplessly."
    $ hentai_scene(23)
    "Worked up by everything, Sabia had no resistance to the pounding thrusts. All she could do was moan and shudder as her orgasm rolled on and on, Lutvrog's thrusts never ceasing."
    $ hentai_scene(24)
    "Neve's lips just kept capturing her mouth, her tongue exploring deeper. She was actively grinding against Sabia's body now, seeking more pleasure even though she had just come. Sabia let herself go and be used by the two of them as they saw fit."
    $ hentai_scene(25)
    call shake ("h")

    "Just when she thought she couldn't take it any more, she finally felt Lutvrog's cum pulsing down his shaft and flooding inside her. She gave a final scream of pleasure and her body bucked upward into Neve's."
    $ hentai_scene(26)
    "After that she went completely limp, all the pleasure wrung from her. All she could do was lie back and try to catch her breath between Neve's kisses. Lutvrog's cock stayed still inside her, enjoying her tight pussy as the last pumps of cum overflowed her pussy."
    $ hentai_scene(27)
    "Finally Neve pulled back, staring down at the exhausted Sabia beneath her. Though the other woman was flushed and breathing heavily, she seemed to be enjoying Sabia's expression more. She wiggled her hips a little and chuckled when Sabia whimpered."
    $ hentai_scene(28)
    n "Alright, I'll have mercy... for now. What do you think, Lutvrog?"
    "He grunted in response, still fully hilted in her pussy, and she felt him squeeze Neve's ass. Sabia just lay back and hoped she would have time to recover..."
    if gallery_workaround == True:
        jump gallery
    return


label RGAnevelutvrogD:
    play music sex1 fadeout 2.0 fadein 2.0
    $ hentai_scene(1,"RGAthreesomeD",dissolve)
    "When Neve made a move on her, Sabia was ready, wrestling with the other woman. Soon they tumbled to the ground, both of them stripped nude, with Neve falling on top of her. The other woman chuckled in pleasant surprise."
    n "Well, someone's eager!"
    s "With the two of you, how could I not be?"
    $ hentai_scene(3)
    "Sabia moved her hand up, sliding her fingers between Neve's. The other woman's hand felt so soft and slender, despite the callouses from her training. Giving it a squeeze, Sabia shifted her back so that their breasts were pressed together more comfortably, enjoying how hard Neve's nipples were against the softness of her breasts."
    "Staring up into the other woman's eyes was nice, but Sabia wanted more. Just when she felt Neve start to shift her weight, Sabia moved first."
    $ hentai_scene(4)
    "Her arm slid between their bodies, finding Neve's slit and beginning to explore around it. Neve gave a satisfying gasp of pleasure, then began rocking her hips against the movements of Sabia's fingers."
    s "You feel pretty eager too."
    n "Heh, how could I not be?"
    $ hentai_scene(5)
    "Enjoying the way the other woman's pussy sucked in her fingers, Sabia began fingering her more intensely. Neve didn't hold back, fully indulging in the pleasure."
    s "You feel almost wet enough for a cock. Don't worry, Lutvrog, we didn't forget about you..."
    $ hentai_scene(6)
    "Neve moved down and captured her lips, briefly surprising Sabia. The elf immediately slid her tongue between Sabia's lips, more insistent than Sabia had ever felt her."
    $ hentai_scene(7)
    "That suited her just fine. Sabia wrestled tongues with the other woman while her hand moved faster, her fingers now covered in Neve's juices. Lutvrog was moving into position behind them, more than ready."
    $ hentai_scene(8)
    "Before he arrived, Neve pulled back, staring down at Sabia and breathing heavily. Her chest heaved pleasantly against Sabia's and she was obviously ready for it. Sabia pulled her hand back to take Neve's again, leaving her pussy empty."
    $ hentai_scene(9)
    "Lutvrog's thick cock came down and slapped against Neve's ass. She grinned and looked backward eagerly, then wiggled her hips. It felt fantastic against Sabia, who was plenty warm herself but trying to hold it together."
    n "Is that for me, or for you?"
    $ hentai_scene(10)
    s "Give it to her."
    "At Sabia's command, Lutvrog reached down and grasped Neve's hips, lining himself up with her pussy. Neve gave a gasp of pleasure and squirmed a little in anticipation."
    $ hentai_scene(11)
    "Lutvrog slid into Neve slowly but surely, and Sabia got to witness every bit of it on the other woman's face. Neve's flush deepened, her eyes widened slightly, and she began a long, low moan that didn't stop until he was fully seated inside her."
    "Sabia felt every bit of it. The pleasure shuddering through Neve's body was obvious in the way her curves twisted on top of Sabia's. She could feel Lutvrog's thickness as it slid past her and spread Neve wide."
    $ hentai_scene(12)
    "When he finally began thrusting, Sabia found herself moaning as well. Neve was grinding into her too hard and the beautiful woman moaning on top of her was too erotic, Sabia was swept up in it."
    "And she decided that she didn't care, just indulged in the pleasure. All of them would get off and she wanted to feel Lutvrog's cock too, so she might as well embrace it wholeheartedly."
    $ hentai_scene(14)
    "Neve bent down to kiss Sabia and she returned it eagerly. The other woman stared into her eyes as she took the rough thrusts and Sabia felt Lutvrog's balls slapping against her ass with each one. Embracing Neve, the idea of the other two fucking, the force of the thrusts rippling through her... it was all too much, Sabia was close to the edge almost without any stimulation."
    $ hentai_scene(13)
    "When Neve came, Sabia was shocked at how aggressive the other woman became. Her hips shuddered wildly, her tongue delved deep into Sabia's mouth, and her entire body arched in pleasure."
    "It was so intense it took her almost to the edge... but not quite over."
    $ hentai_scene(15)
    call shake ("v")
    "A moment later Lutvrog's cock slammed inside her and Sabia screamed as she came. Neve captured it, kissing her even more intensely as Sabia was opened wide by the thick cock."
    $ hentai_scene(17)
    "Lutvrog kept fucking her through her orgasm and Sabia eagerly bucked her hips up against him as much as she could. Had they planned that from the beginning? Sabia didn't even care, it had felt too fantastic. Her pussy was on fire, demanding more even as Lutvrog fucked her through her orgasm."
    $ hentai_scene(18)
    "Soon Neve settled down on top of her, their kiss becoming slower and more affectionate. The other woman might have been warming her up, but as she relaxed down against Sabia, it was also obvious that she'd gotten off. Not a contest, just the three of them enjoying themselves."
    "Putting aside such thoughts, Sabia just enjoyed herself. Lutvrog's cock was plunging inside her steadily, taking her toward an even higher orgasm even though she'd barely finished her first. Neve was sliding on top of her slightly, which only got Sabia even more worked up. She needed release and she needed it soon."
    $ hentai_scene(19)
    call shake ("h")

    "When it finally came, Sabia's pussy squeezed hard around Lutvrog's cock and she felt him explode in response. Sabia bucked and moaned through a long, rolling orgasm that seemed to go on forever as more and more cum was pumped inside her."
    $ hentai_scene(20)
    "Even when it was over, Sabia didn't come down sharply, instead slowly drifting in the pleasure. She leaned up a little to kiss Neve, enjoying the other woman's body against hers even as she enjoyed Lutvrog's cock still resting inside her. God, she could stay like this forever..."
    $ hentai_scene(21)
    "When Neve finally pulled back, she was a glorious sight. The beautiful woman was propped up over her, staring down at her lovingly, her chest heaving, saliva still connecting their lips. Both of them just stared at each other for a while."
    $ hentai_scene(22)
    n "Well? Our little Sabia did pretty good sparring this way, didn't she?"
    lut "Not bad."
    $ hentai_scene(23)
    "Though she was still gasping for breath and trying to recover from the pleasure, Sabia managed a soft response."
    s "Just wait... I'll be stronger next time..."
    "Both of them chuckled and they relaxed there a moment longer, bodies still tangled together..."
    if gallery_workaround == True:
        jump gallery
    return


label RGAlastsceneintro:
    hide screen hudleft
    play music sex1 fadeout 2.0 fadein 2.0
    $ hentai_scene(1,"RGAlastscene",dissolve)
    "It had been a long time since Ellia dreamed of her childhood. She thought she had put her days scrabbling for food on the wrong side of the river Eskra behind her, yet she found her mind drifting through the memories."
    "She had never known her father, slain in wars against the humans. Her mother had tried to take care of her for several years, but eventually fell to illness. Then Ellia had been alone... which made her an ideal target for slavers."
    "The humans had swept through their disorganized camps one day, unstoppable. She and so many others had been swept up, chained, and thrown into carts. She had been terrified that they would eat her, as the other children had whispered over their feeble fires."
    "But instead, she was sold to an old couple and tasked with helping around their house. It was not a miserable life, and the fears of her childhood started to dwindle."
    "One day, when tasked with lighting the fire, her sparks had leapt from her hands instead of the flint. Ellia marveled at her first feeling of magic, and so had her owners. They seemed astonished by how quickly her power grew, and Ellia reveled in it."
    "Several days later, two mages came from the capital of Lundar."
    "They examined her dispassionately, then paid the couple and took her away without explanation. Ellia had fought them, but her power spluttered uselessly against them."
    "She had been certain that her brief reprieve was over, that her life would become a horror once again. Yet to her surprise, she was given as a slave to a young mage woman in Rhaetia. Her work, now focused on magic, was difficult, but she excelled."
    "Soon, she was more powerful than her master. Just when Ellia was beginning to ponder trying to escape, the mages appeared again."
    "Not to take her away, but with an offer."
    "She joined the mages the next day, studying with others, even humans. They scorned her at first, but they couldn't deny her growing power. Her dreams of her miserable childhood had faded away entirely, then... why had they returned? But the thought was snapped out of Ellia's mind and she kept pondering her past."
    "Soon even the humans couldn't deny her power. She was freed from slavery and became one of them in truth - she thought the first elf to ever receive that honor, though now Ellia realized that no one had ever confirmed that."
    "Ellia had been happy among the mages, and might have stayed there forever... had they not made a mistake, and sent her as a diplomat to the Elf Lords beyond the River Eskra."
    "She had been astonished to see that elves could still live like this - perhaps not the kingdoms of old, but far greater than the miserable camps on her side of the river. Her imagination had been spurred by the glories she saw there, and Lundar came to seem as far away as the camps of her childhood."
    "As a powerful mage, it should have been her birthright to lead her people against Lundar... but they did not trust her. She understood that, coming as she did as an ambassador of Lundar, and strove to prove their suspicions wrong."
    "At last, she had been given a chance to prove herself to them. She thought she might have been granted it by the son of one of the Elf Lords - a slender, handsome young man who Ellia believed might love her."
    "Yes, everything had seemed wonderful then, impossibly far from her childhood memories. All she had needed to do was lead a band of their warriors to eliminate a human Archmage, who was alone in a remote estate."
    "It was supposed to be easy. Her power was at least equal to an Archmage's, she was certain, and her band had poisoned weapons to assist. Then she would have proven herself, both as a loyal elf and a great mage. She could return to the Elf Lords, marry the prince, and take her rightful place..."
    "Until someone stepped into the corridor and her hope died."
    "Ellia hadn't even been able to see who it was, because her eyes were locked on the remnants of her companions splattered against the walls. In an instant, they had been torn apart in a splatter of blood and guts."
    "She had protected herself on instinct with a wall of magic, but it hadn't mattered. While she stared in horror at the gory spectacle all around her, something had broken through her shields and knocked her unconscious."
    "All at once, Ellia knew why she had dreamed of her childhood, why she was reliving her life. She let out a scream and reached for her power, destroying the spell that bound her."
    if gallery_workaround == True:
        jump gallery
    return


label RGAlastscene:
    play music sex1 fadeout 2.0 fadein 2.0
    $ hentai_scene(2,"RGAlastscene",dissolve)
    "As she woke, Ellia was shocked to discover that she was completely naked, bound in the air with all four of her limbs raised. As she struggled through the dream spells that had been wrapped around her, she figured out what had happened."
    $ hentai_scene(3)
    "Yes... she was bound by circles of magic that kept her in the air in this awkward, humiliating position. The human Archmage must have taken her by surprise and knocked her unconscious, then tried to pull all her secrets from her mind via the dreams."
    $ hentai_scene(4)
    "Well, the foolish human was going to regret not killing her when she had the chance. Ellia might have given up information about the Elf Lords from her memories, but it didn't matter if she killed the mage holding her captive."
    $ hentai_scene(5)
    "Summoning all her power, Ellia gathered it into a pure surge of magic. She would fling it against her bonds, then send it straight through the heart of the filthy human. Ellia shattered the bonds around her legs first."
    $ hentai_scene(6)
    "Except that they didn't break."
    "Ellia gasped, trying again, but the bonds didn't even quiver. Nothing had been done to inhibit her power, she had every bit of it she'd earned over her life, yet when she flung it desperately against the magic binding her... nothing. It was as if the restraints were sourced from a well of magic deeper than she could fathom."
    $ hentai_scene(7)
    "The magic tightened on her, gently but inexorably, and Ellia turned toward the monster that held her bound."
    "The human woman had to be the Archmage, calmly reading from a document. Barely even monitoring the spells that held Ellia bound so easily. Ellia felt a surge of pure terror and tugged at the magical prison with her physical strength, which was even more useless."
    ty "I know you broke the dream. Give me a moment and I'll be with you."
    $ hentai_scene(8)
    "After reading a little more, Tyra finally looked up at the captive elf. Ellia shuddered as the purple eyes fell on her. Not cruel, not passionate, just watching. And filled with the immense power that now held her bound."
    $ hentai_scene(9)
    ellia "You! You killed them all!"
    ty "As you intended to do to me and my servants. Little more than self-defense."
    $ hentai_scene(10)
    ellia "You... you bitch..."
    ty "I'm disappointed in your memories, Ellia. I wondered if perhaps you had been brutalized before we took you in, but you were treated rather well."
    ellia "As a slave! You only let me free because I was useful to you!"
    ty "Yes, that's how reality works."
    "Ellia growled and tugged at her bonds, but it was still completely useless. She tried to summon another wave of magic, but Tyra smothered it without so much as a gesture."
    ellia "How the hell are you so strong? I was stronger than any humans at the academy..."
    $ hentai_scene(11)
    ty "Oh dear. Did you really think there had never been another person as talented as you? There are always a few who are exceptional... and some of us have decades of experience over you."
    $ hentai_scene(12)
    ellia "You'll regret this, bitch! One day I'll be back, stronger than you, and I-"
    ty "Poor child. We gave you so much, and you threw it all away over your pride."
    ellia "I won't b-"
    $ hentai_scene(13)
    "Tyra raised a finger and the sound froze in Ellia's throat. She could barely manage a smothered whimper, staring at the overpowering mage."
    $ hentai_scene(14)
    ty "You're fortunate that I don't throw people away unless it's truly necessary. I'll permit you some freedom... if you tell me everything you know about the Elf Lord."
    ellia "I... you already saw everything, didn't you?"
    $ hentai_scene(15)
    ty "You really shouldn't lie to me. I'll give you another chance, but I really do need that information."
    ellia "W-wait! What's that spe-"
    $ hentai_scene(16)
    "Magic coursed through Ellia's body and she let out a scream... of pleasure. The magic tore straight through her defenses, bolts of pleasure tearing through her entire body."
    "There was nothing tender or affectionate about it, not like the prince's caresses. Just a raw torrent of pleasure, making her body shake violently as she was driven closer and closer to the edge..."
    $ hentai_scene(17)
    "Then, without warning, the magic stopped. Just as she was at the edge of her orgasm. Ellia was left dangling limply from the magical bonds, gasping for breath. She was torn between trying to recover from the mind-blowing pleasure and trying to thrust her hips, desperate for more stimulation."
    $ hentai_scene(18)
    ty "So you did manage to hide some information about the princeling from me. Not bad, but you need to realize these are old tricks."
    ellia "I... I..."
    ty "If you want to protect him, then you should cooperate. Tell me what you know and I could arrange for him not to be killed, when we move on his father."
    $ hentai_scene(19)
    ellia "No... I won't cooperate with you..."
    ty "You {i}will{/i} cooperate, little girl. The only question is how unpleasant it will be for you."
    $ hentai_scene(20)
    ellia "W-wait!"
    ty "No."
    $ hentai_scene(21)
    "Another surge of pleasure, more powerful than the last. Not having recovered from the first, Ellia had no chance. The pleasure consumed her, wracked her body with unwanted ecstasy, sent her breasts swinging as her torso and hips bucked wildly."
    "The lightning coiled in her pussy and she came, hard, her juices flooding her slit. Ellia gasped and sagged back as the magic faded."
    $ hentai_scene(22)
    "She had never felt anything that intense. Her moments with the prince were pale shadows compared to this, mere children playing together and discussing matters of state..."
    ty "There we go."
    $ hentai_scene(23)
    "Ellia realized with a flush of shame that she had surrendered some of the information. She was hanging here, completely naked, her own juices running down her body. All it had taken was a few pleasure spells, and this human had begun wringing the information from her."
    $ hentai_scene(24)
    ellia "Please... please..."
    ty "That wasn't so bad, was it? Cooperate, and we can do this pleasantly."
    ellia "I... no. I won't betray him, any of them. You... you killed them..."
    $ hentai_scene(25)
    ty "Pity. I had predicted that you would surrender after that, but I suppose I was wrong."
    "Tyra's eyes slid over the paper before her and she took a slow sip of wine. The look in her eyes sent a chill through Ellia's body."
    ty "I have contingency plans, of course. Time to kill two birds with one stone."
    $ hentai_scene(26)
    ty "Ellia... meet Brannam."
    "Her eyes grew wide as the door opened and another prisoner was floated inside by bonds of magic."
    ellia "No... noooo!"
    $ hentai_scene(27)
    "A huge minotaur floated into the room, guided by a gesture from Tyra. He was bound by the same magic that held Ellia, his muscles clenching against it, but his brute strength was even more futile than Ellia's magic."
    "But she didn't care about that, she was terrified by the enormous cock rising stiffly from his crotch... and the fact that Tyra was sliding them together so they would line up properly."
    $ hentai_scene(28)
    ellia "You! You're going to use this filth to rape me?"
    brannam "Not... filth..."
    "Tyra smiled at the two of them as if it was immensely funny, or perhaps just enjoying how they both strained in place. With a flick of her fingers she could bring them together, but instead she let them hover just a tiny distance from one another."
    ty "Actually, Brannam is being punished as well."
    $ hentai_scene(29)
    ellia "What?"
    $ hentai_scene("29b")
    ty "You were supposed to kill the clan leader, Brannam. Why didn't you? Don't you care about keeping your wife alive?"
    "The minotaur gritted his teeth and strained against his bonds harder, releasing a roar."
    brannam "If you hurt her, I-"
    ty "She's unharmed, Brannam. But if you don't explain yourself, I'll make sure she gets sent to a... less than reputable farm."
    brannam "No... I..."
    "Ellia watched in surprise as the enormous muscular body seemed to deflate. Though he still ground his teeth together, Brannam answered weakly."
    brannam "The clan leader was sick, it would not have been proper to fight him. What did I do wrong? I just waited for a day when the stars aligned... please don't send my wife away!"
    $ hentai_scene("29c")
    ty "She'll be fine... but I can't say the same for the outpost the clan leader torched. I didn't want you to fight him honorably, Brannam, I needed you to take his place before that happened."
    brannam "But... it would have been..."
    ty "Maybe I overestimated you. But you did answer, so we'll keep your wife safe. See how much easier it is to cooperate, Ellia?"
    ellia "I..."
    $ hentai_scene(30)
    ty "You'll learn."
    ellia "Wait, no! That thing will split me in half!"
    brannam "I don't want some filthy elf!"
    ty "Too bad."
    $ hentai_scene(31)
    call shake ("v")
    "The magic swirled around both of them and Ellia swung down, her ass against the minotaur's thick cock. The flat head struggled against her tight asshole, but the pressure was unstoppable and soon it punched inside her. Brannam groaned and Ellia screamed."
    $ hentai_scene(32)
    "Even after it came to a stop inside her, Ellia was left gaping. The head of the cock inside her was enormous, a thick rod of fire that had just begun to push inside her."
    $ hentai_scene(33)
    "If Tyra hadn't made her come earlier, it would have been agonizing. It was still far more than she wanted, so thick that the sensation was more than either pain or pleasure. Ellia stared down, still unable to believe that thing was disappearing inside her."
    "The minotaur was struggling too, his body responding to penetrating her tight hole, but his teeth were still clenched. Ellia had always hated minotaurs, but if he was thinking of his wife, she could at least understand him."
    "Not like the woman who sat watching them with a slight smile on her face."
    ty "You'll do better next time, Brannam, or I'll stop playing with pleasant tortures."
    brannam "...no... I..."
    $ hentai_scene(34)
    "Tyra sent another surge of magic and Ellia began shaking. The minotaur's hips were thrusting now, pushing up a little further into her each time. Bound as she was by the magic, there was nothing she could do to keep it from impaling her deeper and deeper. Ellia was reduced to gasping and panting, trying to seek pleasure so the immense pleasure did not become pain."
    $ hentai_scene(35)
    "When she gave a moan of pleasure, Ellia flushed, and the movement briefly stopped. She had never taken anything in her ass, and this cock was so much larger than the prince's... Ellia knew she should keep him out of her mind, but that thought fluttered away at the sensation of her ass being stretched by this pole of meat."
    $ hentai_scene(36)
    call shake ("v")
    "Without warning, she plunged down, her stretched asshole taking most of the cock inside her. It punched inside with terrible force, yet Ellia found herself moaning and her eyes rolling back in her head as her body shook helplessly."
    $ hentai_scene(37)
    "She might have blacked out for a moment, but came to with that enormous cock still in her ass. Tears were leaking from her eyes at the sheer size of the insertion, yet her body was betraying her. They could all see that her nipples were rock hard, and her hips were trembling with more than pain."
    ty "You two enjoy yourselves. After this, you'll get one more chance."
    $ hentai_scene(38)
    "The magical pleasure surged within her again, and Ellia broke. Her eyes rolled back, her mouth hung open, and she began to moan. Her hips jerked unwillingly on the enormous cock in her ass."
    $ hentai_scene(40)
    "When she was dragged back up the shaft, Ellia sobbed with relief. Stretching like this felt too good, gave her the relief that she needed. She threw her magic at the bonds around her - not to break free, but to try to pull herself back down to be filled again."
    $ hentai_scene(42)
    "Whether it was by her power or Tyra's act, Ellia didn't know, and she didn't care: what mattered was that she plunged back down onto the cock. She began to pump up and down, the thick length spearing inside her hotly and taking her to higher and higher peaks of pleasure."
    "She could distantly hear the minotaur growling and snarling, but that soon fell away. All that mattered was his cock and the pleasure it could bring her as she swung down, burying it inside her over and over again."
    $ hentai_scene(43)
    call shake ("h")

    "A flourish of magic rolled through them and they both came violently. Brannam roared and thrust his hips involuntarily as he began to pump hot cum inside Ellia's ass, and she wailed helplessly as the pleasure washed over her in a terrible, unending orgasm."
    $ hentai_scene(44)
    "Finally, it was over. Ellia floated, still impaled on the cock, and just tried to catch her breath. Her mind was no longer dominated by the need or the pleasure, but she had no more strength left to fight. Tyra was overwhelming, it was senseless to try to deny her anything."
    $ hentai_scene(45)
    "She groaned as she was pulled back and the cock slid out of her, trailing cum from her overstuffed ass. Terrified that Tyra might not be done, Ellia gasped enough breath to speak to her."
    ellia "I surrender! Please, I'll tell you whatever you want!"
    ty "Good girl. What about you, Brannam, feeling cooperative?"
    brannam "F-fuck you!"
    $ hentai_scene(46)
    ty "Hmm, pity. You weren't worth as much as I expected here, either, so perhaps I really did overestimate you. Perhaps you would be more useful elsewhere."
    "Her eyes returned to her paper and she took a sip of wine. That tone was the most chilling Ellia had yet heard, and all she could feel was gratitude that it wasn't directed toward her."
    "A tendril of pleasure slid inside her and Ellia welcomed it, collapsing into blissful unconsciousness."
    if gallery_workaround == True:
        jump gallery
    return


label nevemaplyA:
    play music sex1 fadeout 2.0 fadein 2.0
    $ hentai_scene(1,"nevemaplyA",dissolve)
    "Neve wiggled into position at the edge of the bed, getting comfortable. The thought of Maply between her legs already had her nipples rock hard, so she crooked a finger to beckon the catgirl over."
    n "Don't be shy now."
    $ hentai_scene(2)
    "It didn't take Maply very long to strip down, given her clothes, but she hesitated as she crawled into position, staring up at Neve nervously."
    n "Something wrong, Maply?"
    maply "Umm... I don't know if I'll be any good at this..."
    n "What, you don't have fun with each other in your caravans?"
    $ hentai_scene(3)
    maply "Most do, but I'm a young scout... I don't have a lot of experience."
    n "I'm not looking for expertise, Maply. Relax and enjoy yourself."
    $ hentai_scene(4)
    maply "Thank you, Neve... you're so nice..."
    n "You're the one licking me... now get to it!"
    $ hentai_scene(5)
    maply "I'll... I'll do my best!"
    "Her enthusiasm was adorable. Neve leaned back and shifted her position a little more, already a little wet and more than ready to feel the catgirl's mouth on her pussy."
    $ hentai_scene(6)
    "Maply hesitated a moment, intimidated by the sight of Neve's impressive body. Powerful legs, taut stomach, impressive breasts..."
    $ hentai_scene(7)
    "Did she really want little Maply to do this? Maply looked up uncertainly, so Neve gave her a warm smile. She edged a little closer."
    $ hentai_scene(8)
    maply "I'll try, anyway..."
    $ hentai_scene(10)
    n "Just enjoy yourself, Maply."
    "The catgirl blushed crimson when Neve caressed the side of her face, but she also smiled. Neve played with her hair affectionately for a while until the tension finally drained from the catgirl's body and she finally opened her mouth."
    $ hentai_scene(12)
    "Her tongue lapped out experimentally, finally touching Neve's pussy. She gave an appreciative murmur and pushed her hips forward, eager for more of the catgirl's agile tongue."
    "Maply hesitantly gripped Neve's thighs and drew herself closer, licking a bit deeper. But after a moment she started to go slower, her eyes sliding back up."
    maply "Am I d-"
    $ hentai_scene(13)
    "Neve cut her off by gripping the catgirl's head, pulling her closer, getting her tongue on her clit."
    n "That's great, Maply. Harder."
    $ hentai_scene(14)
    "With a happy sound, Maply devoted her full attention to caressing Neve's clit. She was still a little hesitant, but her tongue very eagerly began experimenting with twisting many different ways."
    "Neve had been planning to moan a little to encourage her, but to her surprise she found a real moan escaping her lips. That agile little tongue..."
    $ hentai_scene(15)
    maply "It... it really feels that good?"
    n "Oh, it does. But don't focus on the clit all the time. I want to feel you deeper, too."
    $ hentai_scene(16)
    "No longer hesitating, Maply bent lower and began exploring Neve's folds. Her tongue lapped between them, gently at first and then more strongly, delving deep inside her."
    $ hentai_scene(17)
    "As Maply devoted herself fully to eating Neve's pussy, her tongue began to explore more confidently. Long, careful licks that caressed her outer lips while also pushing deep. Neve found herself breathing heavily and grinding her hips up into the catgirl's face, which was soon covered with her juices."
    $ hentai_scene(18)
    "Maply's tail had been swishing back and forth happily, but to Neve's surprise it now arched up, brushing against her clit. She gave a cry of surprise at the sensations that radiated though her entire pussy."
    "Surprised by the cry, Maply started to pull back a little. Neve didn't let her."
    $ hentai_scene(19)
    n "Don't stop. Harder!"
    "Neve gripped the catgirl's head and drove it harder against her pussy. Maply stared up at her warmly, seeing how her mouth hung open and her breasts heaved as she panted."
    $ hentai_scene(21)
    "Immediately after, Maply went back to work. Her tongue again delved deep while her tail kept teasing, brushing over her abs before flicking around her clit. Combined with the catgirl's eager tongue, it was too much."
    "Neve gripped Maply's hair hard, bucking her hips into the other woman's face and moaning loudly. Maply gripped her thighs harder and leaned into it, licking harder and deeper, not letting up..."
    $ hentai_scene(22)
    "Neve let out a scream of pleasure as she went over the edge, her back arching, her abs flexing, and her pussy grinding against the other woman's face. Maply kept working through it, driving her orgasm to the very limit and prolonging it."
    $ hentai_scene(23)
    "By the time it was finally over, Maply's face was even more covered in Neve's juices. Neve's entire body had relaxed, muscles usually taut from training easing into a more comfortable position. She kept caressing the catgirl's head gently as Maply pulled her tail back and began lapping at her pussy more gently."
    $ hentai_scene(24)
    "The dark-skinned elf wanted to compliment her, but found she was too busy trying to catch her breath. All the while, Maply kept licking gently at her pussy, easing her slowly back to normal. She looked up, a bit of her old hesitance returning, and so Neve managed to find her voice again."
    n "That was fantastic, Maply."
    $ hentai_scene(25)
    maply "You... you enjoyed it? I liked it too... I can't believe someone like me could make someone like you come..."
    n "How could I not? You're too cute..."
    "It had been too long, Neve had forgotten just how thoroughly someone's mouth could pleasure her. As she ran her hands affectionately through the catgirl's hair, she was certain this would not be the last time..."
    if gallery_workaround == True:
        jump gallery
    return


label RokgridSabiaA:
    play music sex1 fadeout 2.0 fadein 2.0
    $ hentai_scene(1,"RokgridSabiaA",dissolve)
    "Since she wasn't wearing her armor and Rokgrid's came off easily, it was easy for them to disrobe, so Sabia soon positioned herself in Rokgrid's lap. His cock was rock hard between her thighs and she wondered how long it had been that hard."
    r "Then... we truly are...?"
    $ hentai_scene(2)
    s "You'd better believe we are! You really think I'd go this far just to tease?"
    $ hentai_scene(3)
    "Sabia reached down and lightly touched the head of his cock, which throbbed in her hand. It was hotter than she expected, and already leaking precum from the tip. Sabia began to rub gently, spreading it all over the head. They'd need the lubrication, if things went the way she expected."
    $ hentai_scene(4)
    s "This huge thing is going all the way inside me... and you'd better last..."
    r "Oh, I'll make a good showing of myself."
    s "You're confident now, but you haven't been with a woman as good as me."
    "Though she hadn't been sure about the banter at first, it seemed to be working on Rokgrid. His cock and her hand were plenty slick now, so she shifted her hips over the head, took a deep breath..."
    $ hentai_scene(5)
    call shake ("v")
    "And slammed down."
    "She'd had another line planned, but it was cut off by a scream as she slammed down on Rokgrid's cock to the hilt. It had been so slick, and her pussy was wetter than she'd wanted to admit, so he'd gone balls deep on the first thrust."
    $ hentai_scene(6)
    "Even after the shock passed, Sabia found herself panting as she accustomed herself to the cock so far up inside her. She would have expected an orc to start humping away immediately, but Rokgrid remained still, enjoying her pussy, and it made it even clearer just how full she was."
    r "Well? Not so bad, huh?"
    $ hentai_scene(7)
    s "Not bad... but you'd better have more than just a big cock..."
    $ hentai_scene(8)
    "In response, Rokgrid reached up and grasped one of her breasts, rolling her supple flesh in his hand. As his fingers flicked at her nipple, Sabia couldn't hold back a gasp of pleasure."
    r "Believe me, I intend to fully enjoy you. You really do have a gorgeous body, such a wondrous mix of strength and beauty..."
    s "You're good at talking, Rokgrid, but are we here to talk?"
    $ hentai_scene(9)
    "Her mocking had the desired effect: Rokgrid began to thrust up into her pussy. The short, controlled thrusts came faster than she had expected, quickly drawing small gasps and moans from her mouth."
    "Rokgrid shutting up and fucking her was preferable, if she was going to do this. Sabia tried not to think about him in particular, just enjoyed the muscles of his chest against her back, his hand exploring her breast, and his rapid thrusts inside her..."
    $ hentai_scene(10)
    "When Rokgrid raised his other hand to grasp her other breast, Sabia let out a loud moan. Her back arched and she found herself pushing down against his thrusts."
    r "You like this, huh?"
    s "Y-yes! Shut up and fuck me!"
    $ hentai_scene(12)
    "He kept doing exactly that, his thrusts coming harder and heavier. Rokgrid was squeezing her breasts roughly now, almost using them as handles, yet Sabia wanted more."
    "She began to bounce, not entirely under her own control, so that each thrust hammered up into her cunt. Her pleasure spiked higher and higher, pushed upward by the constant thrusts until she couldn't take any more..."
    $ hentai_scene(13)
    call shake ("h")
    "Sabia let out a scream as she came, crashing back against him as her legs gave out and impaling herself fully on his cock."
    $ hentai_scene(14)

    "As she came down from her orgasm, she felt surges of warmth deep within as Rokgrid filled her up with his cum. It seemed he had held out until she came, then took his time unloading inside her. Even now he was still pumping out more, while massaging her breasts more slowly."
    "She spent a while just resting there on his cock, catching her breath and recovering from the experience. It would take her a few seconds to be up for any more banter."
    $ hentai_scene(16)
    "When she pulled off of Rokgrid's cock, however, the orc pulled her back against his chest affectionately."
    r "You were fantastic, Sabia..."
    s "You weren't bad either... but you're kind of a mess down there."
    r "Well, given what w-"
    s "Maybe I should do something about that."
    $ hentai_scene(17)
    "Sabia slipped out of his lap and down onto her knees between his legs. She could actually hear him swallow at the sight of her before him, so she breathed out softly onto his cum-covered cock."
    "It wasn't the noblest road to power... but Sabia would do what it took. Looking at Rokgrid staring down at her almost in disbelief, Sabia was sure that he would never forget this."
    $ hentai_scene(19)
    s "It wouldn't be civilized to leave this huge thing so messy..."
    $ hentai_scene(20)
    r "No, it wou-"
    "His attempt at banter cut off in a choking sound as Sabia licked some of his cum off his cock. She started out gentle, since he'd just cum, but judging from his grunts, he didn't mind more."
    $ hentai_scene(21)
    "Sabia stared up at him as she cleaned his cock of the cum that had so recently been inside her. More was leaking from her pussy and staining the floor beneath her, but she ignored it and kept servicing him."
    $ hentai_scene(22)
    "After a quick smirk, Sabia shifted down and sucked the tip of his cock into her mouth. Rokgrid tried to say something else but again could only groan as she lavished attention all over his sensitive cock."
    $ hentai_scene(24)
    "When she judged he'd had enough, Sabia pulled off his cock and bent lower, letting it rest against her face as she cleaned lower on the shaft. She maintained eye contact the entire time, watching as Rokgrid stared at her with a combination of disbelief and desire. Her mouth was busy and his was free, but he couldn't manage a word."
    $ hentai_scene(26)
    "As Sabia finished her work and left his cock glistening, she didn't need to fake her smile. She'd accomplished something useful... and it had been more fun than she expected. Sabia gave his cock a final kiss, then hopped back to her feet."
    if gallery_workaround == True:
        jump gallery
    return


label RokgridSabiaB:
    play music sex1 fadeout 2.0 fadein 2.0
    $ hentai_scene(1,"RokgridSabiaB",dissolve)
    "Sabia shifted down onto her knees in front of Rokgrid and waited quietly for his command. He didn't strike her as the type to just throw her over a table and fuck her... but judging from the gleam in his eyes, he enjoyed being in charge."
    $ hentai_scene(2)
    r "I want to fully enjoy your mouth this time. Get to work."
    "She nodded and lowered her eyes to his cock, marveling at the thick shaft of green flesh. It was going to be rough on her jaw, because she had no doubt where this was going."
    $ hentai_scene(3)
    "Maintaining eye contact with Rokgrid, Sabia began licking all over his cock. Lightly at first, getting it good and slick, then more forcefully. He was so hard that his cock seemed to strain against her tongue."
    $ hentai_scene(5)
    "Once it was good and slick, Sabia slipped forward and began sucking as well. After a few light kisses, she drew the entire throbbing head into her mouth and sealed her lips around it, though it would have been difficult to do otherwise."
    $ hentai_scene(6)
    "Rokgrid's hand settled onto the back of her head, not forceful but surprisingly powerful. Sabia looked up at him and just kept sucking, bobbing her head a little as she got into it. She kept up her own pace... until she felt his fingers tighten in her hair."
    $ hentai_scene(7)
    call shake ("v")
    "His hand forced her down, slamming his cock down into her throat. Sabia gave a cry that was completely muffled as the thick cock filled her mouth and stretched her lips thin."
    $ hentai_scene(8)
    "The shock passed, but her throat was still full of orc cock and Rokgrid wasn't letting go. He kept her there, choking on his cock, and gave a relaxed groan."
    r "Ah, you have a fantastic throat... why don't you start using it?"
    $ hentai_scene(9)
    "Since he could easily use her throat by force, Sabia cooperated and began to suck as well as she could. Rokgrid's hand relaxed, letting her pull back just a little. He didn't let her go far, but she was able to rock back and forth as she sucked on his length."
    "She couldn't get much air with his girth filling her throat, though. Sabia kept sucking, but it was getting more and more difficult."
    $ hentai_scene(11)
    "Just when she grew desperate for breath, Rokgrid finally released her head, letting Sabia pull back. She gasped for breath with strands of saliva still connecting her lips and his cock, her breasts heaving. Rokgrid gave a satisfied chuckle."
    r "Not bad, Sabia. But I want more than your throat."
    $ hentai_scene(12,"RokgridSabiaB",dissolve)
    "Wiping any hint of a glare off her face, Sabia shifted up and into his lap, her ass pressing against his muscles and his cock against her pussy. It was even harder after her blowjob, and she doubted that it would just be rubbing against her for long."
    $ hentai_scene(13)
    s "Aren't you going to stick it in me, you brute?"
    r "I'm in charge, not doing the work. Let me feel your pussy, woman."
    s "Well, in that case..."
    "Sabia carefully shifted up, her pussy sliding against his shaft wetly. Rough as the blowjob had been, she was glad that it was now soaked in saliva, because what came next..."
    $ hentai_scene(14)
    call shake ("v")
    "Sabia let out a loud moan as she dropped down onto his cock, their bodies meshing together tightly as it filled her."
    $ hentai_scene(16)
    "It was easier than the first time, though it still felt huge. But now that her pussy was used to his cock from this position, Sabia found herself heating up. She wanted to start moving on her own, but Rokgrid was in charge..."
    r "Unf... I can't hold back anymore, I need to fuck you now!"
    $ hentai_scene(17)
    s "Finally!"
    "Sabia moaned as Rokgrid finally reached up and grasped one of her breasts commandingly. His hips began to shift underneath her, stirring his cock in her pussy. She let out a moan and had to steady herself by gripping his hip to avoid falling over."
    $ hentai_scene(18)
    "But soon it didn't matter what she did as Rokgrid began to fuck her in earnest. All Sabia could manage was moaning and shuddering as he thrust up into her and mauled her breasts with one hand. Rokgrid was even more forceful than before, as if he had just been exploring the pussy that he now owned."
    $ hentai_scene(20)
    "He let out a roar of pleasure and grasped her breasts with both hands, squeezing as he hammered into her at a faster rate. Sabia couldn't help but let out a cry of pleasure."
    $ hentai_scene(21)
    "As intense as it was, what drove Sabia crazy was that it just didn't stop. Though Rokgrid was just taking his pleasure from her, his thrusts were remarkably even, as if he could just keep pounding her pussy forever."
    "Her eyes rolled up in her head as she gradually dissolved into the pleasure, falling completely into his rhythm and becoming a toy in his hands."
    $ hentai_scene(22)
    call shake ("h")

    "Long after she had surrendered, Rokgrid finally took his pleasure with her, letting out a roar as he emptied his balls inside her."
    $ hentai_scene(23)
    "Sabia found herself collapsed back against his chest, still trying to recover as jets of cum kept pumping into her. Rokgrid didn't stop squeezing her tits, but he did seem to calm down and gave her a thoughtful look."
    r "Sabia? It wasn't too much?"
    $ hentai_scene(24)
    s "F-fuck no..."
    "It was a little hard, but Sabia managed to pull off his cock. Her legs trembled afterward and she fell back into his lap, his cum-covered cock sliding against her weary pussy."
    s "Just... just give me a bit..."
    $ hentai_scene(25)
    r "Oh, I'll give you more than that..."
    "Rokgrid chuckled and gave her breast an affectionate squeeze. Sabia sighed and leaned back against him to recover..."
    if gallery_workaround == True:
        jump gallery
    return


label RokgridSabiaC:
    play music sex1 fadeout 2.0 fadein 2.0
    $ hentai_scene(1,"RokgridSabiaC",dissolve)
    "Sabia gave Rokgrid a little smirk as she shifted down into his lap, grinding herself against his shaft a little."
    s "It's been a real long time since I took my time... why don't we see if you can put those hands of yours to use?"
    $ hentai_scene(4)
    "To her surprise, Rokgrid complied immediately. Sliding an arm around her hip, he pushed his hand between her legs. Though he didn't rush straight to fingering her, just teasing her outer folds made her moan in surprised pleasure."
    s "Good... ease into it..."
    $ hentai_scene(3)
    "Sabia found herself staring back at him as he began to thrust a finger inside her. He went slowly at first, but when she proved wet and ready, he began to pump it inside her with a regular rhythm that had her gasping and bucking her hips into his hand."
    "Not only that, his hand brushed against her clit as well, gentle compared to his thrusting finger but exactly the stimulation she needed. As he began to hook his finger inside her, Sabia realized that she'd forgotten just how good fingers could be."
    $ hentai_scene(5)
    "As Rokgrid fingered her roughly, Sabia came apart. Her body slumped back against him and she began moaning sweetly as her pleasure rose higher."
    $ hentai_scene(6)
    "She was feeling so good that she didn't even care when he reached up and began to fondle her. So long as he kept moving that finger inside her, he could grab whatever he wanted."
    "A surge of pleasure started in her stomach and fluttered lower, getting close... Sabia gripped his hip and pulled away from it."
    s "E-enough!"
    r "Something wrong?"
    $ hentai_scene(7)
    s "No... I just didn't want to come too early."
    $ hentai_scene(8)
    s "Your cock is looking pretty damn good right now... I expect you to do all the work using that thing on me."
    $ hentai_scene(9)
    call shake ("v")
    "Rokgrid obeyed, lowering her onto his cock. Her pussy was more than ready, she would have been fine if he'd just pounded inside, but the slower penetration drew a long moan from her lips."
    $ hentai_scene(10)
    "When he was finally fully inside her, Sabia found herself gasping for breath and more overcome than she'd expected. If it had been someone else, she might have just given in and let him take care of her. But with Rokgrid, she needed to play her role, so she managed to focus again."
    s "Come on... do your job..."
    $ hentai_scene(11)
    "Rokgrid chuckled and began to massage her breasts with both hands, while shifting his cock inside her only slowly."
    r "You want more, then?"
    s "You know I do. Get to it, you brute!"
    $ hentai_scene(12)
    "He obeyed, beginning to thrust beneath her. As usual, his pace kept absolutely steady, letting her get into the swing of the pleasure."
    "Sabia didn't try to resist any longer - she was going to come, and she was going to come hard. She shrieked and moaned as he massaged her breasts and kept pounding her like a machine."
    $ hentai_scene(13)
    "She couldn't resist, one of her hands flying down to finger her clit. Usually light brushing was enough, but she was far past that point, rubbing almost violently as she built up speed and headed straight for the edge."
    $ hentai_scene(15)
    s "So close... harder! Harder!"
    "Rokgrid obeyed, hammering into her and squeezing her breasts even more vigorously. Sabia threw aside all restraint, rubbing her clit in time with the thrusts and going over..."
    $ hentai_scene(16)
    call shake ("h")

    "The strongest orgasm Sabia had felt in years wracked her body, leaving her screaming at the top of her lungs and spasming violently. Only Rokgrid's hands on her chest and cock in her pussy kept her from collapsing entirely."
    $ hentai_scene(17)
    "She wasn't sure how much time passed before she came back to reality, but Sabia found herself in the same position. Her eyes were still rolled back and her mouth hung open. Rokgrid was holding her gently, hands now just kneading her breasts slightly."
    "She couldn't tell at first through the overflowing pleasure, but she realized that at some point he had come inside her. As she slowly became aware of the sensation of being filled with his hot cum, it only added to the sensations that were still flowing through her body."
    $ hentai_scene(19)
    r "So... you liked that a little?"
    s "Hah! We are {i}definitely{/i} going to have to do that again sometime..."
    if gallery_workaround == True:
        jump gallery
    return


label TekrokSabiaSub:
    play music sex1 fadeout 2.0 fadein 2.0
    $ hentai_scene(1,"TekrokSabiaSub",dissolve)
    "She'd known it would come to this, so Sabia stripped down. She expected Tekrok to take her immediately, but instead he pushed her to the ground. She lay there, looking over her shoulder at him, but he just stared at her."
    $ hentai_scene(3)
    s "Well? Surely you don't just want to look!"
    t "Heh. Tekrok is just admiring his prize."
    $ hentai_scene(5)
    "He did begin to remove his armor and clothing, though, so Sabia smiled at him. She didn't want to antagonize him, after all."
    $ hentai_scene(6)
    "When he dropped the loincloth, her eyebrows rose slightly. All orcs were packing quite a bit, but she was impressed by Tekrok. So long as he wasn't too forceful with it..."
    s "You're eager to claim your prize too, huh?"
    t "No more talking, human."
    $ hentai_scene(7)
    "He moved into position behind her swiftly, making Sabia catch her breath. His hands closed on her thighs confidently, as if he owned them, and his cock slid against her slit. Up close and personal like this, she was reminded just how massive he was... now that she'd come this far, her choice was made."
    $ hentai_scene(9)
    t "Hmf. Your body is already mostly prepared, human. Not bad."
    "It made her flush brighter to admit it to herself, but he was right. Sabia was already wet, and as Tekrok began thrusting between her thighs, she could see his shaft glistening. She didn't fight it, moaning softly and letting herself heat up, because she had a feeling she'd need it."
    $ hentai_scene(7)
    t "Spread your legs, human."
    s "Eh?"
    t "Tekrok wants to see your pussy as he claims it."
    $ hentai_scene(10)
    "Sabia obeyed meekly, trying to keep her embarrassment under control. Having him just ravage her was one thing, but making her participate like this..."
    t "Touch yourself, human."
    $ hentai_scene(11)
    s "O-okay."
    "Almost before she realized it, Sabia was rubbing her fingers gently against her slit, daring to brush higher. She was slick, but could she be ready for Tekrok fucking her? He chuckled as she obeyed and squeezed her thigh approvingly."
    $ hentai_scene(12)
    t "Keep going, or your worthless human cunt won't be worth Tekrok's time."
    "Sabia whimpered and began touching herself harder. Her lips couldn't help but hang open slightly as she panted for breath..."
    $ hentai_scene(13)
    "Abruptly Tekrok shoved a finger into her mouth, muffling her cry of surprise. Just his finger was surprisingly thick, invading her whole mouth. She realized only after she started sucking that biting down would have been an option, but that was far from her mind."
    $ hentai_scene(14)
    "Instead she just sucked on his finger as she slid her fingers deeper into her pussy. At least his finger muffled her whimpers of pleasure."
    t "Good... Tekrok is ready."
    $ hentai_scene(15)
    "His cock strained up against her, driven to unreal hardness by her display. It pushed against her lower lips and throbbed when she hesitantly touched it. Tekrok was already moving into position to take her, but she found herself helping line up his cock..."
    $ hentai_scene(16)
    call shake ("v")
    "When he thrust inside her pussy, Tekrok also pulled out his finger, so Sabia's scream rang free. She might have been worried about who might have heard her, but she couldn't think much about that with the enormous cock plunging into her."
    $ hentai_scene(17)
    "After she'd been made to do so much to prepare herself, her pussy took even the massive cock. Even his exploratory thrusts were overwhelming, but Tekrok didn't seem to be having any trouble moving inside her. He gave an appreciative grunt."
    $ hentai_scene(18)
    t "You belong to Tekrok now."
    s "I..."
    $ hentai_scene(19)
    t "Don't talk, human. Get fucked."
    "Tekrok began to hammer into her, smacking his hips against her ass as he plunged deep inside her pussy repeatedly. He pawed at her pussy with one hand while the other reached out to grasp her breast, easily molding it in his grip."
    "Sabia had expected him to make her repeat his claim, but now she realized that it was pointless. Why force her to say anything when he had her in his grasp and spitted on his cock? She gasped and moaned and shook as the brutal orc finally fucked her."
    $ hentai_scene(20)
    "After enjoying her cries for some time, Tekrok returned his finger to her mouth. Sabia began sucking on it instinctively, still shuddering as he kept ramming into her."
    $ hentai_scene(21)
    "She began to dissolve into the pleasure, becoming his plaything, but his thrusts were changing. Slower but more forceful, which still took her to the edge, but seemed to hint at something else..."
    t "Tekrok will have to use this hole many times. But there is another to claim..."
    $ hentai_scene(22)
    call shake ("v")
    "That was all the warning he gave her before he rammed into her ass. Sabia gasped as her anal ring gave way and he plunged deep into her guts, prompting a scream that he let ring out again."
    $ hentai_scene(23)
    "Sabia could only shiver in place, as if the cock in her ass was binding her entire body. It felt so huge, still burning inside her, but he had gotten deep inside her easily enough. Her pussy had covered him with plenty of her juices, after all."
    t "Too tight, but that can be fixed."
    $ hentai_scene(24)
    "Tekrok set about fucking her ass as roughly as he had fucked her pussy. Sabia was glad she was lying down, because it felt like her entire body would have given out otherwise. All she could do was lie there and take it as he hammered into her ass."
    $ hentai_scene(25)
    "She had managed to keep her leg up so far, but it finally dropped to the ground as the brutal fucking overcame her. Tekrok laughed but didn't seem to care about anything except making use of her ass."
    $ hentai_scene(26)
    "When he shoved a finger into her mouth again, Sabia eagerly sucked on it. She also didn't restrain her other hand, sneaking down to touch her neglected pussy. It was practically burning, eager for more as Tekrok violated her other hole, so she didn't hold back."
    $ hentai_scene(27)
    call shake ("h")

    "She came first, moaning and clenching. Tekrok gave a satisfied grunt and unloaded inside her, jet after jet of cum flooding into her bowels as Sabia screamed against his hand."
    $ hentai_scene(28)
    "He stayed inside her, seemingly endless cum pumping into her and overflowing from her ass. Sabia was still moaning around his finger, while Tekrok chuckled and gave a few more thrusts into her packed asshole."
    t "You know who you belong to, human. You cannot doubt it."
    $ hentai_scene(30)
    "Sabia averted her gaze and lay silent, still shivering from the pleasure. With his cum filling her ass and his hands still toying with her, there was nothing she could say."
    if gallery_workaround == True:
        jump gallery
    return


label TekrokSabiaDom:
    play music sex1 fadeout 2.0 fadein 2.0
    $ hentai_scene(4,"TekrokSabiaDom",dissolve)
    "Sabia stripped off the slave outfit before Tekrok could, but a moment later he forced her to the ground. Not as violently as he could have, but there was no doubt that he wanted to make a point."
    s "That all you got? Humans do worse to their slaves!"
    t "You think you can provoke Tekrok... do you want it that bad, human?"
    $ hentai_scene(6)
    s "Show me what you're made of, orc!"
    $ hentai_scene(8)
    "In response, Tekrok reached down and fastened a chain to the bracer on her wrist, then attached it to a table leg. Based on how his muscles bulged as he lifted it, she couldn't pull it off, not easily. She hadn't expected chains to come out this quickly."
    $ hentai_scene(9)
    s "Really? You need to chain down a human woman?"
    t "Tekrok knows who he's dealing with. You want Tekrok to use your cunt, you need to prove it's worthy. Or Tekrok will use you as furniture."
    $ hentai_scene(10)
    "Sabia glanced down over herself, spread out like this, naked but for the remnants of his slave outfit. Yes, she would certainly make a point like this. And while she thought that he actually wanted to fuck her, she wouldn't put it past him to actually just keep her on display for a while."
    t "Touch yourself, human."
    $ hentai_scene(9)
    s "What?"
    t "Orc cocks are too good for dry human cunts. Get it ready or Tekrok will leave you."
    $ hentai_scene(11)
    "Sabia flushed and looked away, but she found one of her hands creeping lower. If this was how he was going to play it, this was the game she'd need to play."
    $ hentai_scene(12)
    "Her fingers began sliding around her outer folds, but Sabia kept her jaw clenched and refused to give him any sounds. Honestly, though, her pussy was already slick and ready. His dominance had her hot, and she would have enjoyed it if they'd gotten started - maybe that was why Tekrok was drawing things out instead of just fucking her."
    $ hentai_scene(13)
    t "Spread your legs, human. Let Tekrok see."
    "Sabia glowered back at him, but obeyed."
    $ hentai_scene(15)
    "In fact, she decided to just ignore him. Sabia began stroking harder and deeper, brushing more against her clit with each stroke. Lying here, being chained... somehow that made it better, and she could probably get off without him even being involved. It would serve him right."
    $ hentai_scene(16)
    "Growling, Tekrok moved into position behind her, his cock slapping up against her slit and forcing her hand away. She hadn't been paying attention to him when he disrobed, so she was startled by the thick shaft that now pressed insistently against her. Startled... but ready. No more taunting."
    $ hentai_scene(17)
    s "Finally. I was beginning to think you just wanted to watch."
    t "Oh, no. Tekrok is going to fuck you good."
    s "Stop talking and do it, then."
    $ hentai_scene(18)
    "She talked a good game, but when Tekrok reached around to squeeze one of her breasts, Sabia couldn't hold back a moan of pleasure. Her pussy was soaking wet, too, beginning to cover his shaft. Tekrok chuckled and kept toying with her body."
    $ hentai_scene(19)
    s "Get on with it, bastard! Elves get to fucking faster than you! I sh-"
    $ hentai_scene(20)
    "One of his fingers pushed into her mouth mid-word, cutting her off. Her teeth came down on it, but didn't do much good given how thick it was. Maybe if she'd bitten down for real, but... she didn't want that, she wanted to finally get some relief after all the teasing."
    $ hentai_scene(21)
    t "You are Tekrok's toy, human. Tekrok will take as much time as he wants."
    "She gave a muffled answer and looked away, refusing to give him any more than that."
    t "But this isn't just a game, is it, Sabia? You want Tekrok to own you because you know he is strong enough to claim you."
    $ hentai_scene(22)
    "She had thought it was mere taunting, but his finger came out of her mouth and Sabia abruptly found herself able to answer and looking back at him. There was something different in his eyes... or maybe it was just how hot she was, or the whole situation..."
    s "If you think you're so strong... prove it..."
    $ hentai_scene(23)
    call shake ("v")
    "In response, Tekrok plunged inside - not into her pussy, but into her ass. Sabia let out a scream as his cock overcame her feeble resistance and punched up into her guts."
    $ hentai_scene(24)
    "The shock passed, but Sabia was still gasping for breath. His cock was like a molten bar shoved up inside her, slightly prepared by her juices but not nearly enough to let something that large easily fit inside her ass. Tekrok grunted and kept trying to thrust a little deeper."
    $ hentai_scene(25)
    "Despite the roughness of it... it felt good. Sabia could have argued back, but what she wanted more than that was pleasure to overcome the burning in her ass. She moaned softly and began thrusting her hips back against him as best she could, finding an angle that felt better for her."
    t "Not bad. Most humans can't do anything after Tekrok gets inside them."
    $ hentai_scene(26)
    "As if to prove it, Tekrok began to thrust inside her, his cock dragging its way out of her back channel before thrusting back in. He fucked her ass without any regard for her - and it didn't matter. The roughness of it left Sabia gasping and moaning and still jerking her hips back against him."
    $ hentai_scene(27)
    "Eager for more pleasure, Sabia reached down and began rubbing herself roughly. Tekrok didn't seem to care, just grunting and seizing her breast again."
    "He settled to fucking her ass in silence, groping all over her body as his cock fully enjoyed her tight hole. The teasing finally over, Sabia found herself driving into higher and higher heights of pleasure..."
    $ hentai_scene(28)
    s "H-harder! Fuck my ass!"
    "She spread her legs to give him a good look, pushing back against him again and trying to get him balls deep inside her. Tekrok grunted in surprise... and counterattacked."
    $ hentai_scene(30)
    "As if pleased by her defiance, Tekrok began to fuck her ass like never before. Sabia's body shuddered too much to keep pushing back against his powerful thrusts, but she fingered herself even harder and screamed until she was hoarse."
    "His finger claimed her mouth again and Sabia bit down on it, groaning as he kept pounding into her. The feel of his cock reshaping her ass, his hips slapping against her, his hands claiming her body... it was too much, Sabia found herself coming hard."
    $ hentai_scene(31)
    call shake ("h")

    "In the throes of pleasure, she felt his cock swell up, but it didn't matter. All she could do was plunge her fingers deep inside her, grind against her clit, and let the pleasure overwhelm her."
    $ hentai_scene(32)
    "When her scream finally stopped, Sabia knew she should probably tease him or thrust back while he was sensitive, but she couldn't. She lay there in his arms, her eyes rolling up, as her body still shuddered in the aftershocks of her orgasm. At least Tekrok didn't seem able to taunt her either, breathing heavily as he kept pumping jets of cum into her ass."
    $ hentai_scene(33)
    "She let her leg drop, but Tekrok didn't pull away. Instead he stayed fully seated inside her ass and returned his hand to groping her breast again."
    s "Not... not bad..."
    $ hentai_scene(34)
    t "This is what you wanted, isn't it, Sabia? A warrior to fuck you and show you your place?"
    s "Don't get... ahead of yourself..."
    "But her voice didn't sound very convincing, even to her. Not while she was still relaxing there with his cock in her ass."
    "Though Tekrok could have been brutal to her sensitive body, or mocked her, he didn't. Actually, his hand massaging her breast felt almost nice, and it wasn't so bad leaning back against his chest. Sabia decided that she could let herself rest, just this once..."
    if gallery_workaround == True:
        jump gallery
    return


label kiasabiaFg:
    play music sex1 fadeout 2.0 fadein 2.0
    $ hentai_scene(1,"kiaFsabiaA",dissolve)
    "Kia hit Sabia in a frenzy of movements, nearly tearing off her clothes and pushing her back against the rocks. Surprisingly quickly, Sabia found herself lying on the soft moss, the Makhor easily moving one of her legs upward and slapping her cock down against Sabia's stomach."
    kia "Sabia want mate?"
    "Sabia intended to look down at the ridged cock on her stomach, but her eyes ended up wandering over Kia's entire body. Her pert breasts, muscular stomach, soft fur, even her scales... she really was beautiful."
    $ hentai_scene(2)
    "And that thick cock sliding so near her pussy, covered in ridges and bumps that Sabia could just imagine inside her... she found herself flushing even more."
    s "Yes... I want it bad..."
    $ hentai_scene(3)
    kia "Kia mate good! Not bad!"
    "Sabia considered trying to correct her... but the Makhor was pulling back, shifting Sabia's leg to line her up properly..."
    $ hentai_scene(5)
    call shake ("v")
    "Even with time to prepare, Sabia wasn't ready. Kia's hips thrust forward powerfully, driving her cock deep inside Sabia on the first thrust and forcing a loud moan from her lips."
    $ hentai_scene(6)
    kia "Sabia small! Feels good!"
    "Sabia could barely listen, just gasping as she tried to get used to the shaft inside her. It was plenty big, but it was the strange ridges and bumps that felt best. And Kia kept shifting slightly, stirring it around inside her, never letting her get entirely used to the sensations."
    $ hentai_scene(7)
    kia "Sabia ready?"
    s "I want it... just be gentle..."
    $ hentai_scene(9)
    "In response, Kia eagerly pushed forward against her, thrusting deep inside Sabia's pussy. Sabia groaned as she felt the strange cock fill her, her body spasming against Kia's. The Makhor let out a happy growl and moved slowly, enjoying her body and letting her grow slicker and hotter."
    $ hentai_scene(8)
    "But soon her pace increased until her hips were slamming down against Sabia's over and over, driving that cock deep inside her. Sabia was moaning helplessly, overwhelmed by the sensations as they came harder and faster. She gasped for breath and managed to speak."
    s "Kia... slower..."
    $ hentai_scene(10)
    kia "Sabia like?"
    "The Makhor pulled out somewhat, but didn't stop moving, continuing with shallow thrusts. That gave her time to enjoy every ridge and bump of her cock, but Sabia managed to suppress a shiver of pleasure and answer."
    s "Yes... just remember how strong you are..."
    kia "Sabia small. Kia not hurt."
    $ hentai_scene(11)
    "The Makhor began to thrust again, still powerfully but now more gently. Now that the sensations weren't blasting into her, Sabia began to relax back into the pleasure... but Kia was leaning closer, her fur rubbing against Sabia's chest as she moved close to speak quietly."
    kia "In arena, Sabia not hurt Kia. So Kia not hurt Sabia. Only feel good."
    $ hentai_scene(12)
    "Sabia surrendered herself to Kia's gentle control, slowly coming apart underneath the Makhor as she thrust into her over and over again. It felt so strange feeling a woman's hips and thighs thrusting against her, but it felt good."
    "Growling happily while she fucked Sabia, Kia began playing with her body more. One paw squeezed her thigh, another toyed with a breast, scales occasionally brushing her nipples. Sabia felt like a toy in the Makhor's paws... and it felt fantastic."
    $ hentai_scene(13)
    call shake ("h")
    "When Kia finally began to thrust forcefully again, Sabia's body was ready and eager to take the pounding cock. It sent her over the edge, body shaking in pleasure, but Kia just kept thrusting into her, pushing her pleasure even higher."

    "While Sabia was still screaming out her pleasure, Kia joined her with a growl. Her cock throbbed powerfully and began to unload. Each shot of cum seemed unusually powerful, flooding into her with unusual force."
    $ hentai_scene(14)
    "When it was over, Sabia spent a while gasping for breath. Kia stayed inside her, still pumping out a little more cum. She growled happily while playing with Sabia's heaving breasts."
    $ hentai_scene(15)
    s "Fuck... that was... amazing..."
    $ hentai_scene(16)
    kia "Kia like mate!"
    "The Makhor's cock throbbed inside her, and Sabia wondered if her transformation magic meant that she could go forever. Fortunately for Sabia's weary pussy, Kia was content to lay down against her happily, gently caressing Sabia's body with her soft fur. Sabia wrapped an arm around her and relaxed into the Makhor's embrace..."
    if gallery_workaround == True:
        jump gallery
    return


label kiasabiaFr:
    $ hentai_scene(1,"kiaFsabiaA",dissolve)
    "Kia hit Sabia in a frenzy of movements, nearly tearing off her clothes and pushing her back against the rocks. Surprisingly quickly, Sabia found herself lying on the soft moss, the Makhor easily moving one of her legs upward and slapping her cock down against Sabia's stomach."
    kia "Sabia want mate?"
    "Sabia intended to look down at the ridged cock on her stomach, but her eyes ended up wandering over Kia's entire body. Her pert breasts, muscular stomach, soft fur, even her scales... she really was beautiful."
    $ hentai_scene(2)
    "And that thick cock sliding so near her pussy, covered in ridges and bumps that Sabia could just imagine inside her... she found herself flushing even more."
    s "Yes... I want it bad..."
    $ hentai_scene(3)
    kia "Kia mate good! Not bad!"
    "Sabia considered trying to correct her... but the Makhor was pulling back, shifting Sabia's leg to line her up properly..."
    $ hentai_scene(5)
    call shake ("v")
    "Even with time to prepare, Sabia wasn't ready. Kia's hips thrust forward powerfully, driving her cock deep inside Sabia on the first thrust and forcing a loud moan from her lips."
    $ hentai_scene(6)
    kia "Sabia small! Feels good!"
    "Sabia could barely listen, just gasping as she tried to get used to the shaft inside her. It was plenty big, but it was the strange ridges and bumps that felt best. And Kia kept shifting slightly, stirring it around inside her, never letting her get entirely used to the sensations."
    $ hentai_scene(8)
    "Before Sabia could say anything, Kia began to hammer into her, as if she could hammer Sabia into the rock. Sabia moaned and bucked beneath her, burning up in the relentless assault."
    s "Kia... slower..."
    "But Kia didn't seem to hear, still thrusting forcefully into Sabia's pussy. The heat of the Makhor's body seemed to spread through Sabia's, leaving her weak and limp with the cock thrusting inside her."
    $ hentai_scene(9)
    "Finally Kia relented, thrusting in to the hilt and leaving Sabia filled with cock. She tried to open her mouth to ask Kia to be gentler, but when she did, the Makhor ground their hips together harder, turning her words into a moan."
    kia "Sabia hurt Kia in arena."
    "Sabia gasped as she realized that the Makhor hadn't just been ignoring her. Kia didn't seem murderous, but there was a predatory gleam in her eyes."
    s "W-wait! I didn't kno-"
    $ hentai_scene(12)
    "Kia drew her hips back and slammed forward, silencing Sabia with another thrust. She squeezed Sabia's thigh roughly while using her pussy hard."
    kia "Sabia not bad. But Kia remember. So Kia use Sabia. Fair after."
    "After that, Kia proved that she had still been holding back, slamming her hips down on Sabia's even harder. Sabia moaned and twisted beneath the Makhor as she succumbed to the brutal fucking."
    $ hentai_scene(11)
    "Rough as it was, Sabia soon found herself moaning sweetly. Her body was completely under Kia's control, but she squeezed tight around the shaft each time their hips slammed together. She was being reshaped for the Makhor's cock and she just wanted it more."
    $ hentai_scene(13)
    call shake ("h")

    "Sabia had gone through several violent orgasms before Kia finally came inside her. The cum exploded inside her more forcefully than usual, each like a rush of fire. The heat drove Sabia over the edge, more powerfully than before, and she let out a scream."
    $ hentai_scene(14)
    "At last Kia stopped thrusting, enjoying Sabia's pussy as she unloaded the last of her cum. Sabia just lay there, gasping for breath... and more satisfied than she had been in ages."
    $ hentai_scene(16)
    kia "Sabia not bad."
    "Sabia stared up at the Makhor, glad that she had done her penance... Kia's throbbing cock made her wonder if her transformation magic meant that she could go forever. Fortunately for Sabia's brutalized pussy, Kia was content to lay down against her, , but gave her thigh one more squeeze before she did, reminding Sabia of her strength. Sabia certainly wouldn't be forgetting this..."
    if gallery_workaround == True:
        jump gallery
    return


label kiasabiaYr:
    play music sex1 fadeout 2.0 fadein 2.0
    $ hentai_scene(3,"kiaYsabiaA",dissolve)
    "Kia hit Sabia in a frenzy of movements, nearly tearing off her clothes and pushing her back against the rocks. Surprisingly quickly, Sabia found herself lying on the soft moss, the Makhor easily moving one of her legs upward and straddling her leg."
    kia "Sabia Kia sit?"
    $ hentai_scene(1)
    "She squeezed Sabia's thigh with a furry paw, but otherwise just stared at her expectantly. This might not be mating to Kia, but Sabia had a feeling this \"sitting\" would be more than a little sexual. This was her last chance to back out... but she didn't want to."
    $ hentai_scene(2)
    s "Go ahead, Kia... I want to feel you..."
    $ hentai_scene(4)
    kia "Sit!"
    "Kia pulled Sabia's leg closer to her, rubbing her hard nipples against her skin. The Makhor's body was surprisingly warm, but her pussy was even hotter, now grinding against Sabia's thigh. Sabia found herself moaning, surprised by how quickly the Makhor's heat bled over into her."
    $ hentai_scene(5)
    call shake ("v")
    "But that was nothing compared to when Kia pushed forward and pulled Sabia into position, grinding their pussies together. Sabia let out a louder moan as the stimulation increased and the Makhor's burning pussy pushed against hers."
    $ hentai_scene(6)
    kia "Sabia feel good!"
    "The rough stimulation over so much sensitive flesh made Sabia squirm in a completely different way than a cock. Kia was too rough, too hot... Sabia had to gasp for breath through her moans to manage to speak."
    s "Sl-slow down..."
    $ hentai_scene(8)
    "But Kia didn't stop, still grinding hard against Sabia's pussy. When Sabia tried to squirm away, she discovered that the Makhor had her completely trapped. Sabia groaned and twisted, her vision starting to unfocus as the rough pleasure overwhelmed her. Moving harder, Kia also leaned forward and spoke in a low voice."
    kia "Sabia hurt Kia in arena."
    "Sabia gasped as she realized that the Makhor hadn't just been ignoring her. Kia didn't seem murderous, but there was a predatory gleam in her eyes."
    s "W-wait! I didn't kno-"
    $ hentai_scene(9)
    call shake ("h")
    "Kia released a playful growl and ground even harder. The scream of pleasure overwhelmed her words and Sabia shook violently beneath the Makhor."
    $ hentai_scene(10)
    "Even as Sabia fell limply backward, unable to resist, Kia kept moving roughly, her hips slamming down into Sabia's."
    kia "Sabia not bad. But Kia remember."
    "Sabia could barely hear through the pleasure, her will to respond washing away in the sensations. Kia easily controlled her body with far superior strength, toying with her thighs and breasts even as she kept grinding their hips together."
    kia "So Kia use Sabia. Fair after."
    $ hentai_scene(9)
    call shake ("h")
    "Kia ground against Sabia with an animal ferocity that Sabia had never felt before. The pleasure spilled over, but Kia didn't slow in the slightest. The Makhor was coming but that didn't stop her at all, grinding over and over."
    call shake ("h")
    "Sabia was fucked through orgasm after orgasm until she was an exhausted wreck beneath the Makhor. Only then did Kia finally loosen her grip and stop grinding so hard."
    $ hentai_scene(12)
    "At last she pulled back, their juices extending between them. Sabia just lay there, gasping for breath... and more satisfied than she had been in ages."
    s "Fuck... that was... amazing..."
    kia "Sabia not bad."
    "Kia lay down against her happily, but gave her thigh one more squeeze before she did, reminding Sabia of her strength. Sabia certainly wouldn't be forgetting this..."
    if gallery_workaround == True:
        jump gallery
    return


label kiasabiaYg:
    play music sex1 fadeout 2.0 fadein 2.0
    $ hentai_scene(3,"kiaYsabiaA",dissolve)
    "Kia hit Sabia in a frenzy of movements, nearly tearing off her clothes and pushing her back against the rocks. Surprisingly quickly, Sabia found herself lying on the soft moss, the Makhor easily moving one of her legs upward and straddling her leg."
    kia "Sabia Kia sit?"
    $ hentai_scene(1)
    "She squeezed Sabia's thigh with a furry paw, but otherwise just stared at her expectantly. This might not be mating to Kia, but Sabia had a feeling this \"sitting\" would be more than a little sexual. This was her last chance to back out... but she didn't want to."
    $ hentai_scene(2)
    s "Go ahead, Kia... I want to feel you..."
    $ hentai_scene(4)
    kia "Sit!"
    "Kia pulled Sabia's leg closer to her, rubbing her hard nipples against her skin. The Makhor's body was surprisingly warm, but her pussy was even hotter, now grinding against Sabia's thigh. Sabia found herself moaning, surprised by how quickly the Makhor's heat bled over into her."
    $ hentai_scene(5)
    call shake ("v")
    "But that was nothing compared to when Kia pushed forward and pulled Sabia into position, grinding their pussies together. Sabia let out a louder moan as the stimulation increased and the Makhor's burning pussy pushed against hers."
    $ hentai_scene(6)
    kia "Sabia feel good!"
    "The rough stimulation over so much sensitive flesh made Sabia squirm in a completely different way than a cock. Kia was too rough, too hot... Sabia had to gasp for breath through her moans to manage to speak."
    s "Sl-slow down..."
    $ hentai_scene(7)
    "Kia immediately stopped moving so roughly, though she kept moving her hips against Sabia's. The other woman's hot pussy was still overwhelming, but now the stimulation was gradual enough that Sabia could enjoy it."
    s "Thank you..."
    kia "Sabia small. Kia not hurt."
    $ hentai_scene(8)
    "Though Kia began to move more forcefully, instead of slamming their hips together, she began to roll smoothly, rubbing them together with steady strokes. Sabia moaned and relaxed back against the moss, shuddering under the other woman's gentle ministrations."
    kia "In arena, Sabia not hurt Kia. So Kia not hurt Sabia. Only feel good."
    "The Makhor was rolling her hips forcefully now, but not violently. Sabia could feel her incredible strength, even the muscles flexing in Kia's stomach against her thigh, but Kia was still being gentle."
    "She coaxed Sabia's pleasure higher and higher until Sabia was moaning and twisting beneath her. Kia let out a pleased rumbling sound and moved faster, her entire body vibrating."
    $ hentai_scene(9)
    "They came at the same time, their bodies shaking against one another, making their pussies grind even more and increasing their pleasure. Sabia's eyes rolled back in her head and for a moment the Makhor's heat consumed her."
    $ hentai_scene(11)
    "In the aftermath, Kia stayed close, holding Sabia's leg close and rumbling happily. Sabia's chest was heaving with each breath, but she managed to gather enough to speak."
    s "That was... amazing..."
    $ hentai_scene(12)
    kia "Sabia sit!"
    "Kia finally pulled back, their juices extending between them. She rumbled happily again and caressed Sabia's body with her other hand."
    $ hentai_scene(13)
    s "We should... sit more often."
    "Kia lay down against her happily, gently caressing Sabia's body with her soft fur. Sabia wrapped an arm around her and relaxed into the Makhor's embrace..."
    if gallery_workaround == True:
        jump gallery
    return


label raidquestbribery:
    play music sex1 fadeout 2.0 fadein 2.0
    scene bg black with dissolve
    "The first orc to strip lay down on her bed and gestured for her to follow. Sabia was irritated by how he just took ownership of her tent, but said nothing. If this was going to go for the entire night, she couldn't afford to antagonize him."
    $ hentai_scene(2,"raidquestbribery",dissolve)
    "She straddled his hips, trying to ignore the thick green cock behind her. Before she could find a good position, he twisted an arm behind her back and pinned it there with overwhelming strength. Using that as leverage, he pulled her down against him, her pussy grinding against his hips and her breasts pushing against his chest."
    $ hentai_scene(3)
    s "Calm down! We have the whole night, there's no need to be impatient!"
    orc "You have two choices, human... you can give us a good night, or we can take it from you."
    $ hentai_scene(6)
    "He reached back to squeeze her ass, lustfully at first and then with crushing force. Sabia winced as she realized that he was right. Her deal depended on making this work. Her being able to walk the next morning depended on cooperating."
    $ hentai_scene(4)
    s "Fine... I assume you're not going one at a time, then?"
    "Sabia shifted against him to get into a more comfortable position. If they were fucking her from both ends, then she needed to be ready so it didn't wreck her entire body."
    $ hentai_scene(8)
    "But to her surprise, the second orc reached down to fondle her ass. He chuckled while Sabia yelped and the orc underneath her thrust against her slit a little."
    $ hentai_scene(9)
    orc "Now you're the one who's impatient... let us enjoy this ass a little... you show it off to everyone often enough."
    "Sabia endured his groping in silence as his hand wandered all over her ass. Meanwhile, her pussy was starting to get wet despite herself, and she knew she'd need it when they finally started fucking her."
    $ hentai_scene(10)
    "The orc finally let go of her ass, leaving her just straddling the first. He kept grinding against her slit, apparently in no hurry. Sabia wanted to say something sarcastic, but she was completely in their power and doubted it would do any good. All she could do was wait for them to finally start fucking her."
    $ hentai_scene(11)
    call shake ("v")
    "The hand slapping her ass took her completely by surprise, drawing a yelp and making Sabia lurch forward, her breasts hitting the orc's chest."
    $ hentai_scene(12)
    "He had hit her {i}hard{/i} and kept his hand there, enjoying how her ass jiggled. Not as hard as he could have, but the force of it left her ass stinging and her eyes watering."
    $ hentai_scene(13)
    s "How long are you going to draw this out?"
    orc "We want you squirming when we fuck ya... it's not fun if you go limp."
    s "I'm not going t-"
    $ hentai_scene(14)
    call shake ("v")
    "The other orc slapping her ass turned her sentence into another yelp. This time she managed to avoid falling forward, but there was absolutely nothing she could do to stop them tormenting her ass."
    $ hentai_scene(16)
    "Though she saw how this was going to go, Sabia couldn't help but glare back at the orc behind her. Judging from how he chuckled, he probably liked it better that way."
    $ hentai_scene(17)
    "When they took their hands off her, Sabia's ass was stinging. She had to crane her neck to see, but it looked like it was bright red, too. The orc behind her tugged off his loincloth and Sabia tried not to imagine how her sore ass would feel when he was ramming against it..."
    "But at that moment, the orc beneath her pulled on her arm. To avoid the tension she had no choice but to shift upward, and that was when she realized that he was moving his hips."
    $ hentai_scene(18)
    call shake ("v")
    "She plunged down onto his cock, moaning as the thick shaft filled her."
    $ hentai_scene(19)
    "Even when his thrust ended, Sabia was left atop him, gasping for breath. She was surprised just how easily he'd been able to thrust inside, her pussy readied by his shaft grinding against it... and the sting of their slaps, though she didn't want to admit it."
    $ hentai_scene(20)
    "Sabia looked back to where she mounted the orc and swallowed. Embarrassing as it was, she needed to work with her body's instincts to make it through the night. Just lying on top of him getting used to his length wasn't so bad, but..."
    $ hentai_scene(21)
    "She'd feared he'd start slapping her ass again, but Sabia still yelped at the blow. The orc laughed and kept slapping at her buttocks."
    orc "Come on, move!"
    $ hentai_scene(22)
    "Sabia obediently began to ride him, her hips rising and falling to impale herself on his cock over and over again. He stopped striking her ass so forcefully, instead just slapping it playfully to encourage her to ride him faster."
    "With an arm pinned, Sabia didn't have much leverage. She had no choice but to lean forward, flattening her breasts against his chest so that she could pump her hips more smoothly."
    $ hentai_scene(23)
    "When the other orc began striking her ass as well, Sabia didn't yelp, she moaned. Her ass burned from their blows and she found herself spasming wildly with each one. What had once been smooth movements became erratic humping on his cock."
    $ hentai_scene(24)
    orc "Not a bad start... let's go harder."
    "The orc beneath her began to thrust into her pussy harder, taking over the rhythm. His cock seemed to be reaching impossibly far up in her body, spreading the burning from her ass to the rest of her. Sabia moaned and followed his lead, bouncing on top of him into his thrusts."
    $ hentai_scene(25)
    call shake ("v")
    "Too late, she realized the other orc was moving into position. She felt the head of his cock pushing against her anus for only a second before he slammed through her resistance and plunged into her asshole."
    $ hentai_scene(26)
    "Her ass was nowhere near ready and his cock was dry, but the orc didn't seem to care. He just kept his grip on her ass to keep her in place and kept thrusting until he was balls deep inside her. Sabia groaned at the burning shaft inside her, but now that she was trapped between the two, she was even more helpless than before."
    $ hentai_scene(29)
    "Though she tried to move with their thrusts at first, it was completely useless. The two huge cocks pounding her from either side rendered her movements completely useless - she was just a piece of meat between them for their use."
    "Sabia's eyes rolled back slowly as she succumbed to the sensations. Her pussy was throbbing, her ass was burning, each thrust stung as it slapped against her buttocks, and her body just gave up at the assault of conflicting feelings."
    $ hentai_scene(30)
    call shake ("h")

    "While Sabia was still groaning half in pain, the orcs finally came inside her. Both unloaded at nearly the same time, so much cum pumping into both her holes that Sabia let out another moan."
    $ hentai_scene(31)
    "They just kept unloading inside her, giving Sabia a moment to gasp for breath. She should have been disgusted to be filled with so much orc spunk, but she found herself mostly grateful. All that cum in her ass would make the next round much easier... and she was sure there would be a next round."
    $ hentai_scene(32)
    "But as the orcs let go of her ass, Sabia realized just how rough it could be. That had been their warm up - the idea drew a low moan from her lips."
    "As the two orcs began to thrust into her again from both ends, Sabia let her body collapse and just let them fuck her. She'd need all her strength to make it through the night..."
    if gallery_workaround == True:
        jump gallery
    return


label SUtentaclesex1:
    $ hentai_scene(1,"SUtentacle1",dissolve)
    "Sabia had braced herself to protect her head, but the collapsing area was surprisingly narrow. Instead of tumbling downward, Sabia found herself wedged into a narrow crevice alongside Neve. They had some space to move side to side, but precious little between them, leaving their bodies pressed together."
    $ hentai_scene(2)
    s "I guess the tunnels collapsed... we're lucky we didn't get injured."
    $ hentai_scene(3)
    "Neve chuckled and made no effort to shift away from Sabia."
    n "I wouldn't be concerned. The bigger tunnels would be much deeper, so we just need to climb out."
    $ hentai_scene(4)
    call shake ("v")
    "Except at that moment, tentacles surged from the crevices all around them. Sabia let out a shriek and moved, but her body just flailed against Neve's curves due to their trapped position."
    $ hentai_scene(5)
    "In an instant, tentacles had wrapped all around them, so fast they'd startled even Neve. Sabia started to search for where her weapon had fallen in desperation, other hand going to the tentacle around her neck... but she realized that it wasn't tightening to crush her."
    $ hentai_scene(6)
    "Instead, the tentacles kept exploring her body. One wormed around her thigh, squeezing gently, while others picked at Neve's clothing, almost as if curious."
    n "It's not attacking..."
    $ hentai_scene(7)
    "The tentacles kept exploring, not at all shy about touching them. Sabia tried to squirm away from a tentacle that was beginning to rub against her breasts, but that just made her press against Neve again. This time, she could feel that the dark elf's nipples were hardening."
    n "Relax, Sabia. It obviously doesn't want to hurt us."
    $ hentai_scene(8)
    s "But... we don't know what it wants..."
    n "Seriously, relax. You're so tense all the time, you'd be happier if y-"
    $ hentai_scene(9)
    call shake ("v")
    "At that moment, one of the tentacles slithered underneath her loincloth, brushing against her barely defended privates. Sabia let out a surprised scream and thrashed between the stone and Neve."
    $ hentai_scene(10)
    "In a flash the tentacles retreated, pulling back into the stones. Sabia caught a brief glimpse of the creature's body, three eyes wide as if alarmed at the noise she had made. Then it was gone a second later, leaving her sweating for many reasons."
    n "Aww, seems like you scared it off."
    s "Yes... looks like it..."
    $ hentai_scene(11)
    n "So... are you going to take your hand off my hip any time soon?"
    "Sabia flushed and pulled back, trying to worm her way out of the hole. That only made her rub further against Neve, which made her blush even more. Fortunately, the other woman soon took pity on her and helped her leverage her way back up."
    if gallery_workaround == True:
        jump gallery
    return


label SUtentaclesex2:
    play music sex1 fadeout 2.0 fadein 2.0
    $ hentai_scene(1,"SUtentacle2",dissolve)
    "Sabia bit back a surprised yelp as she fell in after Neve. Doing it intentionally was much more embarrassing than falling in by accident, especially how Neve pulled her close. Determined not to fold too early, Sabia reached out to steady herself on the other woman's hip."
    n "I don't mind, Sabia, but that's going to make it hard to take our clothes off..."
    s "O-okay..."
    $ hentai_scene(2)
    "Sabia realized that it would have made more sense to strip before they got in. Instead they had to wriggle against one another as they slowly stripped down until their bodies were completely bare. Sabia flushed as she felt her bust pressing against Neve's, but didn't back down, instead reaching out to caress her waist again."
    $ hentai_scene(3)
    n "Mmm, this is comfortable. Even if the plan fails, it won't be all bad..."
    $ hentai_scene(4)
    s "I... I'm not saying I don't like it, but... the goal is just to draw out the tentacle monster again..."
    $ hentai_scene(5)
    call shake ("v")
    "Even though Sabia had been alert for the monster's arrival, she was still taken off guard when the tentacles slithered around them from all sides. She managed to avoid crying out this time, but still let out a gasp."
    $ hentai_scene(7)
    "The tentacles were exploring them like last time, less hesitantly now that there were no clothes in the way. Neve murmured in pleasure and watched the tentacles as they gathered around her body."
    $ hentai_scene(8)
    n "My, those nipples... you're not going to scream this time, are you?"
    $ hentai_scene(9)
    s "Not in a bad way..."
    n "This feels good... if our friend does run off, I think we're going to need to finish on our own."
    $ hentai_scene(10)
    "But this time, the tentacles showed no signs of retreating. Instead, more of them extended, fully exploring their exposed breasts. Sabia began panting as she felt the powerful muscles in the tentacles squeeze her breasts, while Neve bit back a little whimper of pleasure when one coiled around her nipple."
    $ hentai_scene(11)
    "Her panting lips were suddenly stretched by a thick tentacle exploring straight into her throat. Sabia choked, but managed not to bite down too much. Neve chuckled and spoke, though her voice was no longer so stable."
    n "That's a good sign... but I suggest you start sucking, or it won't stop."
    $ hentai_scene(12)
    "Sabia did her best to suck on the thick tentacle as it squirmed deeper into her throat. It seemed to thicken slightly, then withdrew, only to push forward again. It was definitely deep in her throat, but seemed content just to explore her mouth like that."
    $ hentai_scene(13)
    "Another tentacle dove into Neve's mouth, taking her off guard. Sabia could hear the muffled groan clearly and Neve's entire body twitched in surprise."
    $ hentai_scene(14)
    "Soon Neve began sucking... and the tentacle in Sabia's mouth pulled back. Her mouth was coated in a thin layer of the creature's slime, which left a pleasant numbing tingle. The tentacle shifted nearby, coiling against her chest along with the tentacles still gripping her breasts."
    $ hentai_scene(15)
    s "This what you were hoping for?"
    "Neve stared back at her, obviously unable to respond with the tentacle plunging into her throat. Her body answered for her, though, her hips bucking under Sabia's hands and her back arching a little, pressing their chests together even more."
    $ hentai_scene(17)
    "When it finally pulled away, Neve took a moment to catch her breath and then answered."
    n "I like a kiss as much as the next girl, but I was really hoping for-"
    $ hentai_scene(18)
    call shake ("v")
    "Responding to their urges, the tentacles assaulted their lower halves all at once. Sabia couldn't hold back a scream as her pussy and ass were invaded at the same time."
    $ hentai_scene(19)
    "But the tentacle showed no signs of retreating despite her cry, squirming deeper inside her as they stiffened. Sabia wriggled away on instinct, but was surprised how much Neve was shuddering. The powerful muscles on her torso were convulsing as if the tentacles were going deep. Their bodies pushed together harder, separated only by the tentacles still slithering around them."
    $ hentai_scene(20)
    n "It's going... so deep..."
    "Neve seemed to be having a hard time speaking. Sabia wanted to tease her, but only moans emerged from her lips as her own tentacles began to thrust more eagerly. They seemed to have explored her holes sufficiently and now just thrust with stiffened tentacles. Neve's hips began to rock against the thrusts, her entire body shaking back and forth with the movements."
    $ hentai_scene(21)
    "Tired of pushing against the uncomfortable rocks, Sabia tightened her grip on Neve's thigh and pulled the other woman closer. Neve gave a low moan and accepted it eagerly, meeting her gaze as their bodies slid together even more closely. The tentacles tightened around them, wrapping them closer together even as they kept thrusting into them."
    $ hentai_scene(23)
    "Sabia had only a few moments of warning as a tentacle slithered against her neck before it claimed her mouth again. She didn't even think of trying to resist, letting it claim her throat again and begin thrusting immediately. Neve let out a loud groan and shuddered violently against her, her rhythm falling apart for a time."
    $ hentai_scene(24)
    call shake ("v")
    "The two of them gripped each other even tighter as more tentacles wrapped around them, plunging into their holes that had already been stretched wide. Sabia's eyes rolled back in her head and she could no longer focus on Neve, but from the way the other woman squirmed, she was sure the dark elf was being filled with thrusting tentacles."
    $ hentai_scene(27)
    "Neve let out a muffled scream, the thrashing of her body falling into a rhythm of raw sexual pleasure. Sabia clung to her as she began to orgasm wildly, screaming around the tentacle stretching her lips even while the others continued to thrust so forcefully."
    $ hentai_scene(28)
    call shake ("h")

    "As Sabia succumbed to the pleasure over and over, she felt the tentacles begin to throb. As they pumped huge amounts of cum into the two of them, Sabia finally heard Neve give a scream as she came hard, her entire body vibrating against Sabia's."
    $ hentai_scene(29)
    "The tentacles stopped thrusting as they unloaded huge loads of cum inside them, but Sabia didn't stop coming. It was so hot and thick, filling her in a way she hadn't felt before. More and more pumped inside them, forcing out the older cum to slide down over her body."
    $ hentai_scene(30)
    "Gradually the spurts inside them began to dissipate, leaving Sabia able to recover. The tentacle in her mouth had pulled back just enough for her to catch her breath, but her lower holes were still utterly packed full of tentacles."
    "Sabia did have enough presence of mind to stare into the other woman's eyes as she came down from her pleasure. She had no idea what to say after sharing an experience like that... she was grateful for the tentacle between her lips, even as she whimpered as she felt it finally retreat..."
    if gallery_workaround == True:
        jump gallery
    return


label SUkiaylvasexF:
    play music sex1 fadeout 2.0 fadein 2.0
    $ hentai_scene(1,"YlvaKiaF",dissolve)
    "Ylva settled on her side in the grass, finding a comfortable position. Kia prowled around near her, looking uncertain."
    kia "Mate... like this?"
    $ hentai_scene(3)
    ylva "Come lie down behind me, Kia. You'll see."
    $ hentai_scene(5)
    "Ylva waited with some anxiety as Kia prowled nearer, as if still not sure about this. She wasn't truly afraid, though, and the sight of the Makhor approaching sent warmth pooling in her stomach."
    $ hentai_scene(7)
    kia "Ylva!"
    "Kia abruptly pounced, jumping down behind Ylva. The orc couldn't help but moan as she felt the Makhor's fur brush against her back. Kia's cock pushed between her spread thighs, rubbing against Ylva's slit and sending a shiver up her body."
    kia "Mate like this?"
    $ hentai_scene(8)
    ylva "That's right, but we don't have to start so quickly. We can enjoy each other first... why don't you touch my breasts?"
    kia "Nnhhh..."
    $ hentai_scene(9)
    "Abruptly Kia reached up and grasped one breast, molding it in her palm. Her claws tickled against Ylva's skin gently. As the fur of her palm brushed over Ylva's nipple, she couldn't help but moan."
    kia "Ylva likes?"
    ylva "Yes... that's... good..."
    "It was difficult to get words out already, her body much hotter than she had expected."
    $ hentai_scene(10)
    "Kia bent down and began kissing Ylva's neck, not quite like a human kiss. Closer to a bite, but she didn't sink her teeth in, just nuzzled her lips against Ylva's neck. Ylva gave a low moan, glad the Makhor was catching on so quickly."
    ylva "G-good!"
    $ hentai_scene(11)
    kia "Mate now?"
    "Kia looked to her as she spoke, lips whispering against her neck. In addition to squeezing Ylva's breasts, she was rubbing her cock harder against Ylva's slit. Her shaft was covered in Ylva's juices now."
    ylva "...yes..."
    $ hentai_scene(12)
    call shake ("v")
    "The instant she heard the word, Kia plunged her cock into Ylva's pussy. Ylva let out a cry as the ridges and bumps of the cock spread her wide open. Kia gave a happy cry as well, almost a roar."
    $ hentai_scene(13)
    "When it was fully inside her, Ylva needed a moment to gasp for breath. The other woman's body was pressed up against hers, Kia's hips against her ass to lodge as much cock inside her as possible. The Makhor growled in satisfaction, squeezing Ylva's breast harder."
    kia "Mate!"
    $ hentai_scene(14)
    "With that happy declaration, Kia began to thrust powerfully, slapping into Ylva's ass at a ferocious pace. Yet after the foreplay, Ylva was ready for it and found herself moaning almost immediately, her eyes rolling back as the cock explored her thoroughly."
    $ hentai_scene(15)
    "Still thrusting, Kia bent down to Ylva's neck again. This time she did bite, gently, just rough enough to leave a mark. She spoke quietly against her neck."
    kia "Kia's mate."
    "Was she claiming ownership? Ylva was briefly taken out of the experience, wondering, but as Kia kept kissing along her neck and stroking her breasts, she decided that she didn't care."
    $ hentai_scene(16)
    "Ylva began moaning her pleasure, letting herself enjoy it fully. She tensed her powerful core muscles and began pushing back against Kia's thrusts, getting that studded cock even deeper inside her. Ylva couldn't help but arch her back involuntarily as her pleasure mounted, though Kia's hand on her breast and mouth on her neck kept her from thrashing too much."
    $ hentai_scene(17)
    call shake ("h")

    "Just when Ylva thought she couldn't take it anymore, Kia thrust harder and growled into her neck. Her cock began gushing cum into Ylva's pussy and the flood of heat took Ylva over the edge as well."
    $ hentai_scene(18)
    "When the spurts of cum finally stopped, Ylva was left gasping, her breasts heaving beside her. Her legs trembled with the aftershocks, even with Kia stroking her thigh. The Makhor was looking at her curiously, almost shy."
    kia "Good, but... Ylva done mating?"
    $ hentai_scene(19)
    ylva "I want more! Just start out a little gentle, I'm sensitive."
    "To encourage the Makhor, she squeezed her pussy around the cock, which was still hard. Kia gave a playful little growl and then returned to her neck."
    $ hentai_scene(20)
    "The Makhor began gently biting and kissing along her neck and returned a hand to her breast, gently molding it and brushing the fur of her hands over her sensitive skin. Her cock shifted back and forth slowly, just teasing at her pussy. Ylva relaxed back against the Makhor's body and caught her breath for the next round..."
    if gallery_workaround == True:
        jump gallery
    return


label SUkiaylvasexY:
    play music sex1 fadeout 2.0 fadein 2.0
    $ hentai_scene(1,"YlvaKiaY",dissolve)
    "Ylva settled on her side in the grass, finding a comfortable position. Kia prowled around near her, looking uncertain."
    kia "Mate... like this?"
    $ hentai_scene(3)
    ylva "Come lie down behind me, Kia. You'll see."
    $ hentai_scene(5)
    "Ylva waited with some anxiety as Kia prowled nearer, as if still not sure about this. She wasn't truly afraid, though, and the sight of the Makhor approaching sent warmth pooling in her stomach."
    $ hentai_scene(7)
    kia "Ylva!"
    "Kia abruptly pounced, jumping down behind Ylva. The orc couldn't help but moan as she felt the Makhor's fur brush against her back. Though the Makhor massaged her thigh with a furry paw, she seemed uncertain."
    kia "Mate like this?"
    ylva "That's right, but we don't have to start so quickly. We can enjoy each other first... why don't you touch my breasts?"
    kia "Nnhhh..."
    $ hentai_scene(9)
    "Abruptly Kia reached up and grasped one breast, molding it in her palm. Her claws tickled against Ylva's skin gently. As the fur of her palm brushed over Ylva's nipple, she couldn't help but moan."
    kia "Ylva likes?"
    ylva "Yes... that's... good..."
    "It was difficult to get words out already, her body much hotter than she had expected."
    $ hentai_scene(10)
    "Kia bent down and began kissing Ylva's neck, not quite like a human kiss. Closer to a bite, but she didn't sink her teeth in, just nuzzled her lips against Ylva's neck. Ylva gave a low moan, glad the Makhor was catching on so quickly."
    ylva "G-good!"
    $ hentai_scene(11)
    "Under the Makhor's eager ministrations, Ylva soon found herself dripping wet. Kia looked back toward her hips and murmured against her neck as she spoke."
    kia "Ylva pussy want."
    "Kia wanted it, or Ylva wanted something? She wanted to ask for clarification, but it took a moment to catch her breath and Kia was moving already."
    $ hentai_scene(12)
    "When Kia plunged her hand between Ylva's legs, the orc couldn't help but cry out in pleasure. Not only did her fur brush against Ylva's clit, it rubbed against her sensitive thighs as well. Instead of plunging anything into her, Kia's fingers teased her pussy lips, stimulating the entire region in a way no cock could."
    kia "Ylva like?"
    $ hentai_scene(13)
    ylva "Y-yes! Just... keep going..."
    "Kia bent down and kissed at her neck again. This time she bit down a little, just enough to leave a mark without hurting."
    $ hentai_scene(14)
    "The direct stimulation quickly overwhelmed Ylva, but the Makhor didn't stop. Soon the orc was thrashing and moaning beside her, breasts shaking and her hips trembling to escape the questing fingers."
    $ hentai_scene(16)
    call shake ("h")
    "All too soon, Ylva went over the edge, her entire body shaking as Kia took her over the edge. The heat surged up from her pussy and flooded the rest of her body, for a time consuming all thought."
    $ hentai_scene(17)
    "Ylva was left gasping, her breasts heaving beside her. Her legs trembled with the aftershocks, even with Kia stroking her thigh. The Makhor was looking at her curiously, almost shy... then reached down again."
    $ hentai_scene(15)
    "All Ylva could do was gasp and moan as the Makhor began to work at her pussy again. This time she understood all of Ylva's weakest points even better, not letting her fully come down from orgasm before she drove her toward another one."
    $ hentai_scene(16)
    call shake ("h")
    "Surrendering to it, Ylva screamed out her pleasure as Kia took her over the edge time and time again. She felt the Makhor's teeth bite down harder and didn't care, actually welcomed the sharp teeth on her neck."
    $ hentai_scene(17)
    "When it finally ended, Ylva was an orgasmic wreck. If not for Kia taking hold of her thigh, she would have collapsed forward onto her face. Kia examined her carefully."
    kia "Ylva... like?"
    $ hentai_scene(18)
    ylva "Y-yes!"
    "That was all she could manage to gasp, but she wanted to encourage Kia. The Makhor's uncertain expression gradually diminished."
    $ hentai_scene(19)
    kia "Kia also like."
    "She reached forward and grasped Ylva's breast again, drawing a gasp. But this time she didn't squeeze, just gently caressed the sensitive orb. As the Makhor snuggled up behind her, Ylva felt herself drifting into exhausted rest..."
    if gallery_workaround == True:
        jump gallery
    return


label LutvrogTitfuck:
    play music sex1 fadeout 2.0 fadein 2.0
    $ hentai_scene(1,"LutvrogTitfuck",dissolve)
    "Sabia eased into place between Lutvrog's muscular legs, letting her breasts settle around his cock. Even many orcs would have been enveloped in her cleavage, yet his thick member kept them parted. It was strangely comfortable, feeling his length throb between her breasts, yet it also made her body rapidly heat up."
    $ hentai_scene(2)
    s "I saw how much you enjoyed these before... lie back and let me take care of this."
    lut "I leave myself in your hands."
    s "Or tits, as the case may be!"
    $ hentai_scene(3)
    s "Mmm, I'm going to have fun with this thing..."
    "He throbbed against her body, growing even harder, which she hadn't thought was possible. Sabia felt her nipples hardening even before she got started."
    $ hentai_scene(4)
    "Murmuring her pleasure, Sabia grasped her breasts and began to squeeze them around the base of his shaft. Her flesh yielded to his, every hard vein pressing into her skin, and Sabia moaned as she massaged his length with her breasts."
    $ hentai_scene(5)
    s "I don't have enough to take care of this big thing... guess I'll have to use my mouth..."
    $ hentai_scene(6)
    "She bent down, watching him as she lowered her mouth closer and closer to his cock. She could see his desire, almost wanted him to start thrusting and just fuck her tits, but he remained patient while she teased him."
    $ hentai_scene(7)
    "While she kept up a squeezing pattern around the base of his cock, Sabia began to devote her attention to his head. Her tongue lapped out, paying special attention to the slit at the end of his cock. She knew it would cover her in the end, but right now his self-discipline prevented even a drop of precum."
    "Sabia decided to see what she could do about that."
    $ hentai_scene(8)
    "Now that his cock was good and wet, she began to lavish attention all over his head, her tongue lapping over the huge organ. As she found her rhythm she looked up at him, maintaining eye contact as she wrapped her tits around the cock she was so eagerly sucking."
    $ hentai_scene(9)
    "That finally earned a grunt from him."
    lut "More. Use your tits."
    $ hentai_scene(12)
    s "More? You mean like this?"
    lut "Stroke my cock with your tits. Put some strength into it."
    "Hearing him order her sent a thrill through Sabia's body. She gathered her breasts around his cock more carefully, using their full weight to massage his length. Though she couldn't quite fit all of his length, she could wrap herself fully around his girth. It felt even hotter and harder between her breasts like that."
    $ hentai_scene(10)
    "Sabia fell into a rhythm, beginning to slide her breasts up and down his shaft. She'd coaxed a little precum from him now, making his length slick and allowing her to move more easily. Sabia found herself bouncing her entire body while she massaged her breasts in opposite directions, in order to better serve his cock."
    $ hentai_scene(11)
    "She moved so eagerly that she went too hard, had to fall back for a moment and catch her breath with her breasts just resting around his cock. Her heaving breaths made her breasts swell around him more, even while she was resting."
    "Well, more than resting. When Sabia began to move again, she realized just how wet she'd become. She needed this."
    $ hentai_scene(12)
    "Once again she began pumping her breasts, more quickly than the last time. His cock pushed between her breasts, veins and ridges rubbing against the sensitive skin of her cleavage. Her mouth hung open now, panting as she stared up at him."
    $ hentai_scene(13)
    "She began to focus all her attention on his cock, massaging around his shaft as she again bent down to lick at his head. When she could, she leaned down further to suck it, but she needed to feel his shaft even more."
    $ hentai_scene(15)
    "Sabia bent lower, squeezed her tits tighter. Her heavy breasts slammed against his muscular stomach as she pumped faster, trying to cover his entire shaft and lapping her tongue over what she couldn't."
    $ hentai_scene(16)
    lut "Gonna come."
    "Only his voice made her look up at him again. She could feel the throbbing in his cock and he was thrusting a little now, his body slapping against the bottom of her breasts, his cock thrusting between her breasts and pushing against her soft lips."
    $ hentai_scene(17)
    "Sabia pulled back and gave him a tight channel to thrust into as he began to move faster, but she couldn't stop. She kept bouncing her breasts in time with his thrusts, licking his cock whenever it pushed into her mouth."
    $ hentai_scene(18)
    call shake ("h")

    "When Lutvrog finally came, she felt it surge toward her. His balls tightened, his cock throbbed even more violently between her breasts, and then he began to unload, cum shooting explosively toward her."
    $ hentai_scene(19)
    "All Sabia could do now was tremble, her own pleasure peaking as she felt him throb against her chest. She kept his length wrapped in her tits as best she could as he unloaded everything he had all over her face."
    $ hentai_scene(20)
    "Finally Sabia let her hot breasts rest, again just sliding comfortably around his length. She opened her mouth to say something, but found she could only pant for breath."
    "But she didn't need to say anything. With his cock between her tits and his cum all over her face, Lutvrog got the picture."
    if gallery_workaround == True:
        jump gallery
    return


label SUelmypokersex:
    play music sex1 fadeout 2.0 fadein 2.0
    $ hentai_scene(1,"ElmyBar",dissolve)
    "Elmy blushed furiously under the table, humiliated to be treated like a prize. All she could see was the lower legs of the orcs as they played nearby. Judging from the sounds, the first winner would soon be decided."
    "Eventually one of them let out a roaring laugh and stomped over toward her. Elmy's eyes widened slightly as she saw the orcs approach, surrounding her table, but she tried to maintain control."
    orc "Open wide, cat whore!"
    $ hentai_scene(4)
    elmy "H-hey! I'm no-"
    orc "That's right - whores get paid! Now open up!"
    $ hentai_scene(5)
    "Elmy blushed deeper as she realized that he was right. She was nothing but a prize to be won, a pawn in Sabia's game. All she could do was shift nervously as the winning orc sat down in front of her."
    $ hentai_scene(6)
    "As soon as he got into position, he slapped his cock down against her face. Elmy shivered and tried to back away from the filthy member, but there were more orcs behind her. And it sounded like... were they really going to keep playing like this?"
    $ hentai_scene(7)
    elmy "Now, see here, I thought..."
    $ hentai_scene(8)
    "The orc in front of her slid a hand under the table and gripped her head with his powerful fingers."
    orc "Don't think, slut. Just suck."
    $ hentai_scene(10)
    "She resisted on instinct, but it didn't matter. With complete control of her head, the orc could easily hold her in place and line his cock up with her lips. They already had to stretch just to start to get around his head, how could she take the entire thing?"
    $ hentai_scene(11)
    "Desperate not to have her face fucked, Elmy began participating, her tongue lapping out all over the head of his cock. The orc growled in satisfaction and his hand tightened in her hair."
    $ hentai_scene(12)
    "Overhead, Elmy could hear the orcs talking and laughing as they began to play again. They all ignored her except the winner of the previous round, who was casually using her as a cock warmer."
    $ hentai_scene(13)
    "He began to thrust a little and Elmy gagged. She reached up to grab his cock, try to hold it back, but quickly discovered that was impossible - especially as it became slick with saliva and precum. Elmy settled for stroking along the shaft to try to hold him off. If he came on her face, that wouldn't be so bad."
    $ hentai_scene(14)
    "The orc in front of her settled down, enjoying her slender fingers struggling to wrap around his shaft. But at that moment, Elmy heard the sound of a chair scooting behind her. No, surely not..."
    $ hentai_scene(15)
    "Apparently the orcs had already finished another round and a second orc shifted his hips underneath the table. She struggled to look while still servicing the cock in front of her, but Elmy could feel his cock resting against her ass."
    $ hentai_scene(16)
    "As the orc reached down and began to paw her hips, Elmy found herself flushing in fury. She had assumed at worst she would service the orcs one at time, but they weren't going to wait and there was nothing she could do."
    $ hentai_scene(17)
    orc "Let go and open up, slut!"
    $ hentai_scene(18)
    "Elmy winced as she realized what was coming, but she was helpless between the two throbbing cocks. She dropped her hand to grip the floor instead so that at least she could control the movements of her body a little."
    $ hentai_scene(19)
    call shake ("v")
    "It didn't really matter. When the two orcs hammered into her throat and pussy, all she could do was shake and scream into the cock in her throat. It didn't matter if she could reach the floor, the thick cocks had her spitted between them."
    $ hentai_scene(20)
    "As the two orcs began to saw into her, Elmy could only try not to choke as her body shook wildly between them. They thrust wildly, giving no thought to anything but their pleasure and using her like a toy. It was humiliating that a woman who had so many hopes for her future was reduced to a piece of flesh, but that was all she was to them."
    $ hentai_scene(21)
    "Yet as the orcs kept pounding into her, Elmy realized that wouldn't be the worst humiliation. Her hips were beginning to respond, reacting to the thick invader by getting her wet. That let the orc thrust deeper into her and the pain began to be replaced by shameful pleasure."
    $ hentai_scene(22)
    "The orc in front of her began to grunt and Elmy looked toward him. His thrusts were more difficult to endure now, painfully stretching out her throat, but she hoped that he was getting close to coming."
    $ hentai_scene(23)
    call shake ("v")
    "Her hopes were shattered as the orc tugged her head down, forcing the majority of his cock down her throat. She gagged and spasmed wildly, struggling to pull back, but was helpless against his overpowering hand."
    $ hentai_scene(24)
    "Both orcs began to grunt and thrust more steadily. Her body had nowhere to go now, so all she could do was quiver and feel her breasts bouncing back and forth as they plunged into her."
    $ hentai_scene(25)
    "As the cock in her throat kept making short thrusts, Elmy realized that it might be a struggle just to breathe. She tried to gasp for breath when he pulled out a little but the orc behind her kept slamming into her hips and driving her forward. Her muffled moans began to fade out."
    $ hentai_scene(26)
    "Her eyes rolled back in her head as the world grew dim. Elmy surrendered to it, just let them use her body however they liked..."
    $ hentai_scene(27)
    call shake ("h")

    "When they finally exploded inside her, Elmy couldn't help but be filled with relief. The pleasure that she'd been struggling against overwhelmed her, surging from her hips as she was filled by the orc's thick cum."
    $ hentai_scene(28)
    "Yet even after they had emptied their loads inside her, they stayed in her pussy and mouth. More tears rolled down Elmy's cheeks as she struggled for breath, now a completely hopeless effort with cum bubbling out of her mouth."
    $ hentai_scene(29)
    "Finally the orc pulled out of her throat, letting her gasp for air. She was so glad to breathe again that she didn't even struggle when another orc moved in behind her and grabbed her hips."
    "She didn't know how long their game would last, but she hoped they would run out of money soon."
    $ hentai_scene(30)
    "Hours later, Elmy's body and hair were caked with cum. She felt utterly beaten down by the series of thick cocks, no longer resisting when the next winner moved in to take her mouth or pussy. Surely they must be almost done..."
    $ hentai_scene(31)
    "Yet just as she was hoping that, two more winners slid into place and she felt a new pair of cocks press up against her."
    $ hentai_scene(32)
    elmy "H-how are you not out of money yet?"
    orc "Huhu... we're not playing too hard, since the real prize is below the table..."
    elmy "No... t-that's..."
    orc "Now open up, slut!"
    $ hentai_scene(33)
    "Weeping, Elmy opened her mouth and accepted the next filthy cock into her lips. She didn't try to fight, just began to clean it with her tongue as best she could before the orc began using her throat and hoping the one behind her would be gentle."
    $ hentai_scene(35)
    "He wasn't. Elmy choked and moaned as she was again filled from both ends. She both flushed and reacted involuntarily as the orcs began to fuck her yet again. From the sound of the coins overhead, their game would be going on for a long time..."
    if gallery_workaround == True:
        jump gallery
    return


label MaplyHellhound:
    play music sex1 fadeout 2.0 fadein 2.0
    $ hentai_scene(1,"MaplyHellhound",dissolve)
    "Maply couldn't help it, she felt the rush of blood to her face, a red blush suffusing her cheeks as she fell to the Arena's floor. The hound's tongue lolled from its mouth as it panted. Even with him being behind her, Maply could see the thick shaft swelling up between the hound's legs."
    $ hentai_scene(2)
    maply "Oh... oh wow! You're... you're really big!"
    "In the back of her mind, a small doubt flitted about. Was something so big... was it going to even feel good? Or was it just going to hurt?"
    "She wasn't even sure it was right. What would Sabia think if she found out?"
    $ hentai_scene(3)
    "The hound watched Maply, listening to her words but still standing just a little bit off. He seemed to be just watching her, waiting. Maply nibbled at her lip, unsure. A big hellhound. Was she really going to? She felt her heart thudding in her chest, heavier and heavier."
    "With the desire bubbling up within her, she found herself tipping closer to giving in, and she gave her rear a quick wiggle. As she did so, her tail whipped around as well, and her pert boobs jiggled underneath, rubbing against the coarse sand."
    $ hentai_scene(4)
    "She gasped as the hound started to pad over to her. It hit Maply just {i}how{/i} big the beast was. And... how big its cock was. When it had been a few steps away, it had seemed smaller. She pursed her lips together, trepidation pulsing through her. Her body tingled, trembling like it does in the moment before leaping from a tall cliff into water. For a brief moment, she started to reconsider-"
    $ hentai_scene(5)
    "But that moment passed almost immediately, as the hound pressed up against Maply from behind. The thick shaft slapped down above the curves of Maply's ass, the tip resting just above the catgirl's lower back, pressing against the base of the blue tail."
    $ hentai_scene(6)
    "It felt good though. With the weight of the hound's paws on her back pushing her down, Maply found her nethers all afire, only inflamed further by the heat of the hellhound's shaft rubbing between her cheeks, the tip oozing precum that clung to her tail."
    $ hentai_scene(7)
    "If the cock was thick - and it was - then the knot that pushed up behind was even larger. Words were stolen from Maply, and instead a little moan rumbled in her throat. Panting above her, the hound's breathing came faster, and she knew that he was going to take her."
    "The hot breath felt reassuring like a comforting caress on her face, but... more than she had ever experienced before. There was something else with it."
    $ hentai_scene(8)
    "Maply didn't have time to ponder it. Faster than she had expected, the hound slipped the hot shaft down, and his powerful hind legs pushed forward. The cock thrust in, piercing Maply in one earth-shattering plunge. A low groan of pleasure slipped past her lips."
    $ hentai_scene(9)
    maply "Oh... o... slow... don't go too fast! I'm... you don't... mmm... don't want to hurt me!"
    "Maply's worry that the hound might lose control, and start wildly rutting into her, seemed misplaced. Or was it simply following her request?"
    $ hentai_scene(10)
    "Either way, it gave Maply a moment to relax. She was still surprised that it had managed to fit inside her, but she was glad that it had. Every thick, coursing vein rubbed against her sensitive walls as she wriggled her hips just enough to feel it moving inside her. The feel of that monstrous knot, pressing imperiously against her slit..."
    "It was like nothing she had felt before."
    $ hentai_scene(11)
    "The sound of the hound's body slapping against her toned ass and thighs bounced around the empty Arena. Her teasing movements and contractions had been too much for the hound. Maply's ass jiggled almost uncontrollably as the hellhound thrust in and out of Maply's almost-too-small tunnel."
    $ hentai_scene(12)
    "Her moans didn't stop him, and only seemed to make him go faster. The cock slipped out, before being thrust back in. Faster, harder. Pleasure and a sense of feeling absolutely full started to well up deep inside her. The only thought that Maply had was brief flashes of her time with that young Elf, a few years ago."
    "He had been eager, and it had felt... okay. But she knew why it hadn't felt as good as everyone had told her it would. She knew now."
    $ hentai_scene(13)
    "Pausing for just a moment, the hound wriggled, jostling his shaft around within Maply. Both of his front legs came down on Maply's own arms. The furred body felt nice and warm against her bare skin, and she felt safe in his embrace."
    "The soft fur sent shivers through her body, a tingle down her spine. It felt so good against her soft, smooth flesh, like each complemented the other in a way that she hadn't experienced before."
    $ hentai_scene(14)
    maply "Is... is that it? Are you already done?"
    "The words touched the sandy floor, her head pushed down several inches by the hound. Her question was little more than a rough gasp and the hound barked an answer at Maply's words. She somehow knew what it meant. He shifted his weight a little bit, and..."
    $ hentai_scene(15)
    "Started to hammer into Maply's pussy. The catgirl felt herself overwhelmed. There were too many sensations for her to process. The hound's weight atop her, the soft fur rubbing. Hot breath on her face. And most of all, the hound's legs driving himself deeper and deeper into Maply."
    $ hentai_scene(16)
    "Before long, the hound slipped into a rhythm. Maply's breath came fast, and her nipples were rock hard. Every now and then, they brushed against the sand, and it sent shocks of electricity shooting through her body that made her pussy clench tighter around the shaft. The hound licked Maply's face eagerly, like a lover's kiss."
    $ hentai_scene(17)
    "After a few moments, Maply was able to draw in a long, ragged breath, and almost focus. It was hard still, of course, with her slick, needy pussy filled with throbbing hellhound cock."
    maply "T-that's... that's good! Don't... mmm, don't stop!"
    "She knew she hadn't needed to say it. The animalistic lust, the rutting, it was so much easier than with a person."
    "They didn't have to try and please each other, didn't have to consider the other's pleasure. They just had to rut, and it felt good, the pleasure came for the both of them."
    "It was so different than with Neve, than with the few others she had been with, and it felt almost liberating to learn."
    $ hentai_scene(18)
    maply "WAIT! That's... that's not going to fit! You can't! I'm too... oooh... mngggg..."
    "Maply's words failed her. The hound tongue still lashed at her cheek, drool running down her chin as the thrusting intensified further."
    "The knot started to push in. Slowly, not with ease. Maply gritted her teeth, and found her thoughts put to the test."
    $ hentai_scene(19)
    "It felt like it was going to tear her apart, the knot was so big. But then the hound gave one more mighty push, and it forced its way in. Maply's pussy spread wide to accommodate it, and she felt every single inch of it. Breath caught in her throat, and for a moment she couldn't breathe."
    $ hentai_scene(20)
    "She had never felt as full as she did right now. Her tunnel squeezed upon every square inch of the hound's cock as the beast grunted and then groaned, a low rumbling from his belly that vibrated on Maply's back."
    "Her entrance was tight about the knot, and within moments she felt the warmth flowing into her as the hound came. With every rope of seed that painted Maply's insides, she felt the cock throb just before it delivered the next load."
    $ hentai_scene(21)
    "They stayed there, locked together, for several more minutes. Even if Maply had wanted to extricate herself, they were locked together until the knot deflated. The beast had cum so much inside her, that she would have sworn she could feel it almost sloshing around."
    $ hentai_scene(22)
    "Finally, though, the hound managed to wriggle out of Maply. The warmth, sticky wetness oozed out of her slit, running down her thighs until it formed a muddy puddle in the middle of the Arena. The hound panted triumphantly, taking possession of Maply once again with his paws on her back, and the still-dripping, oozing cock on the catgirl's lower back."
    $ hentai_scene(23)
    "With her lower back and ass coated in hellhound-jizz, it made a giant squelch as the hound leaned down upon Maply once more. Her blush deepened just a little as she felt the hot seed being smooshed further over her back. The hound lapped at her face happily."
    "Maply couldn't manage a word. Instead, she gave a little giggle as she pushed back against the hound's weight."
    if gallery_workaround == True:
        jump gallery
    return


label merchant_good_end:
    play music sex1 fadeout 2.0 fadein 2.0
    "Sabia and the two eager men quickly made their way into the inn’s room."
    "They quickly sat down onto the bed, and Sabia knew she’d have to keep up the naive act until they were worn out."
    $ hentai_scene(1,"sabia_merchants",dissolve)
    "Not letting them have any time to think, Sabia stripped, and hopped up onto the bed as well - but not before grabbing the vials and placing them on the mattress."
    $ hentai_scene(3)
    s "I think if you boys want to keep up with me, you might need to take a little sip of this virility potion! It’ll help you have the best sex of your life!"
    s "Helped by me of course!"
    s "(If they have just a little bit of stamina potion, it should perk them up for a short while… and then give them a massive crash. I doubt anyone will be able to wake them for hours.)"
    $ hentai_scene(2)
    "Tomas grabbed the bottle out of Sabia's hand quickly."
    m1 "Shounds great!"
    m2 "I don’t want none of that shtuff! I can fuck you fine right now! Where’s that tentacle shlime you said you had?!"
    $ hentai_scene(4)
    s "Whoa, hang on there! Just the tiniest bit or you won’t stop being hard for days!"
    "Tomas stopped mid motion, and then very delicately took a small sip of the stamina potion."
    "Not wanting to be left behind, Harald did the same despite his earlier protests."
    $ hentai_scene(5)
    s "Great! And I’ll grab the tentacle slime in a minute, once the potion kicks in, because-"
    $ hentai_scene(7)
    call shake ("h")
    s "Whoa! Ready to go are you?"
    "Tomas wasted no time, his cock throbbing and rock-hard. He inched forward on the mattress, and thrust his hips up against Sabia's bared chest."
    "It was bigger than Sabia had expected, and she could feel the heat from the thick member on her soft flesh."
    "Harald seemed content to watch for the moment, his eyes roaming Sabia's body and drinking in every curve."
    m1 "Yeah… c’mon, you gotta, like, push your boobsh together!"
    "Sabia hoped she didn’t let them have too much stamina potion, it was already clear it was working on them."
    $ hentai_scene(8)
    "With one hand she gripped her breast, fingers digging into the pliant flesh as she pushed it against Tomas’ cock."
    m1 "Oh…. mmnnnggg! That’s shoooo nice!"
    "The low groans of enjoyment filled the room. Tomas started to rock his hips slightly, thrusting his cock just a little bit between Sabia's tits."
    $ hentai_scene(9)
    "Pre-cum started to ooze from the tip of his shaft, and Sabia couldn’t help but find she enjoyed the heavy weight of the thick cock on her breasts."
    "If she was going to have to fuck them, she could at least enjoy it… and if the tentacle slime worked properly, she might enjoy it more than normal."
    s "I’ll get that slime now, I think? We don’t want to waste any of that potion right? And leave poor Harald over there!"
    m1 "I… uh, I guessh not…"
    $ hentai_scene(11)
    "Frowning, Tomas pulled back, and Sabia grabbed the vial full of tentacle slime."
    "Doing her best to give a wicked smile, Sabia arched her back a little bit more, sticking her tits out, hard nipples pointing upward."
    $ hentai_scene(12)
    "She licked her lips quickly, and then tipped the bottle down, letting the purply, viscous goop fall down onto her tits."
    "It flowed slowly, and clung to her flesh and curves."
    m2 "Gimme… gimme shome of that pussy!"
    $ hentai_scene(19)
    call shake ("h")
    "Grinning to himself, Harald moved over to Sabia, and yanked her on top of him, pushing her down until her pussy was pressing against his cock."
    s "Oh… fuck!"
    $ hentai_scene(16)
    "It worked almost straight away, Sabia could feel her tits and her stomach tingling, and a burning lust growing within her. She stopped the flow of the slime and put the bottle to the side."
    "Harald’s cock, with its heat and girth pressing against her pussy did nothing to help."
    "She could feel her arousal growing, her pussy started to throb in need and desire."
    $ hentai_scene(18)
    "Her chest rumbled, and her breath rushed out her nose in a shuddered exhale as hips started to rock back and forth, grinding her slit against the pulsing cock."
    s "I need this… fuck, I need this…"
    s "Fuck, it’s so big… and hot…"
    "Sabia moaned, running her dripping lips up and down Harald’s shaft, enjoying the pressure as she leaned forward a bit more."
    m2 "Fuuuuck! That’s…. hgnnnn!"
    "Harald gasped, and flopped back on the bed, thrusting against Sabia's movements, the tip of his cock leaking a constant and steady stream of pre-cum that slipped back down the length of his shaft."
    $ hentai_scene(20)
    s "Holy shit… was that too much slime? I can’t… I… fuck, I need more!"
    m1 "Wait for me- I want some of that stuff!"
    s "Hurry up, then!"
    "Tomas wasted no time, angling himself into position, and slapping his cock back down on Sabia's tits."
    $ hentai_scene(21)
    "Tentacle slime splattered over all three of them as he did so, and Sabia poured the rest of the slime."
    "It dripped down, coating her body with more of the stuff, along with Tomas’ cock and Harald’s shaft below."
    s "N- mmnngg!"
    "Sabia's eyelids fluttered wildly, and she felt a wave of pleasure rolling through her body and crashing."
    "Pleasure pulsed through her body, and the tentacle slime was only making everything feel better, and she knew she needed more."
    "Her pussy was sopping wet, and more of the slime still oozed down from the bottle."
    $ hentai_scene(22)
    "Once more, Sabia squeezed her breast against Tomas’ shaft, but this time it felt far better. Every square inch of her flesh that the slime had touched was hyper sensitive."
    "Tomas’ cock slipped and slid around, the heat from his pole sending shivers of pleasure jolting through Sabia's body, and making her whimper."
    $ hentai_scene(23)
    call shake ("h")
    s "OH FUCK!"
    $ hentai_scene(24)
    "Harald maneuvered himself so the tip of his pre-cum leaking cock was against Sabia's needy slit, and he thrust in."
    m2 "I can’t… I need more, fuck!"
    "Gritting his teeth, his cock started to piston in and out of Sabia with a vigor that made the bed creak from the strain."
    $ hentai_scene(25)
    "Sabia could barely think, her body was afire with pleasure and hunger, desire and lust."
    "Her hips rolled back and forth, grinding against Harald's cock as it filled her tunnel up."
    "Little whimpers rumbled in her throat, and her breath was uneven."
    m1 "This… this slime is really… nnnfg!"
    s "Mnnngggg!"
    "Sabia could barely speak. In fact, all three of them could barely speak. The tentacle slime really was a potent aphrodisiac, Sabia realized in the back of her mind."
    $ hentai_scene(29)
    "She threw the bottle away - there was more than enough slime over them all now."
    "Her nipples were like diamonds, and her tits kept bouncing and jiggling about, Tomas’ cock thrusting between them wildly."
    "She swore that Harald’s cock was swelling up inside her even more, growing a little thicker."
    "The pressure on her swollen pussy was growing, her lips straining to take the sheer girth of the frantically ramming pole."
    $ hentai_scene(30)
    call shake ("h")
    "Her whole body was bouncing up and down from Harald’s wild pounding, her ass slamming onto his thighs with loud claps, and the tip of Tomas’ pre-cum-and-slime-coated pole poking against her lips."
    "In her desperate need, her mind in a lust-fueled haze driven by the slime, she tried to wrap her lips around Tomas' cock, the need to suck growing, the desperate desire to sate her lust."
    "Both Tomas and Harald’s pace quickened even further, and Sabia's eyes rolled to the back of her head, her mouth gaping open with a low rumbling groan drowned out by the slapping, and wet squelches of the voracious fucking."
    "She felt Tomas’ thrusting pole pulse, balls slapping against the bottom of her tits, and he erupted."
    $ hentai_scene(31)
    call shake ("h")
    "Cum gushed out, a thick rope of the stuff that painted her chin white."
    "The burning heat from it, the smell of it hitting her nostrils. And the constant tingling, throbbing of the slime over almost all of her body. It was too much."
    "She found herself cumming - thighs shuddering, twitching. Her muscles contracting, squeezing down around Harald’s shaft deep inside her."
    "Harald came too, his hands balling up more of the bedsheets as he unleashed a torrent of cum inside Sabia."
    "Her breath caught in her throat, and she felt the warmth inside her, spreading through her while Tomas still continued to paint her face and hair and chest with more jizz, the wild frantic haphazard thrusting sending more spurts of cum flying out."
    s "There’s… you’re cumming so much… there’s so much cum!"
    "Sabia gasped in surprise, feeling her insides swelling up with even more jizz before it started to gush out about Harald’s cock, oozing out and down her thighs, mixing with the viscous slime."
    "The tip of her nose dripped with jizz, and it coated her normally pink lips, and at least half of her bangs were wet and sticky, saturated with cum."
    "And yet they both still went, a few more desperate thrusts and at least another one or two normal loads worth of jizz painting Sabia's face and insides, tits and thighs with more white."
    m1 "Fuck… that was… great!"
    $ hentai_scene(32)
    "Tomas blinked slowly, trying to keep his eyes open. Harald pulled out, and a river of cum gushed out of Sabia's abused hole, a pretty picture of white cum and red, swollen pussy lips."
    "Sabia's body still thrummed with lust, but she was coming down a little, and realized she had been riding the orgasm the whole time."
    m2 "I’m… that was… shit!"
    "Both of the merchants were heading quickly to a sleep. The mix of potent aphrodisiac, alcohol, orgasming and a little bit of stamina potion all caught up with them, making them crash. Hard. Just like Sabia had planned."
    $ hentai_scene(35)
    "They landed heavily on the bed, drifting to sleep almost immediately."
    $ hentai_scene(36)
    "Sabia licked her lips, unable to take her eyes from their still dripping cocks."
    $ hentai_scene(37)
    "She shook her head."
    s "Fuck, I need to get this slime off me before I get too distracted!"
    if gallery_workaround == True:
        jump gallery
    return


label merchant_bad_end:
    play music sex1 fadeout 2.0 fadein 2.0
    "Sabia and the two eager men quickly made their way into the inn’s room."
    "They quickly sat down onto the bed, and Sabia knew she’d have to keep up the naive act until they were worn out."
    $ hentai_scene(1,"sabia_merchants",dissolve)
    "Not letting them have any time to think, Sabia stripped, and hopped up onto the bed as well - but not before grabbing the vials and placing them on the mattress."
    $ hentai_scene(3)
    s "I think if you boys want to keep up with me, you might need to take a little sip of this virility potion! It’ll help you have the best sex of your life!"
    s "Helped by me of course!"
    s "(If they have just a little bit of stamina potion, it should perk them up for a short while… and then give them a massive crash. I doubt anyone will be able to wake them for hours.)"
    $ hentai_scene(2)
    "Tomas grabbed the bottle out of Sabia's hand hesitantly."
    m1 "What's this?"
    m2 "I don’t want none of that stuff! I can fuck you fine right now! Where’s that tentacle slime you said you had?!"
    $ hentai_scene(4)
    s "Just a little something to help you guys get extra hard, and extra excited!"
    "Tomas very delicately took a small sip of the stamina potion."
    "Not wanting to be left behind, Harald did the same despite his earlier protests."
    $ hentai_scene(5)
    s "Great! And I’ll grab the tentacle slime in a minute, once the potion kicks in, because-"
    $ hentai_scene(7)
    call shake ("h")
    s "Whoa! Ready to go are you?"
    "Despite their apprehension with the potion, Tomas wasted no time, his cock throbbing and rock-hard."
    "He inched forward on the mattress, and thrust his hips up against Sabia's bared chest."
    "It was bigger than Sabia had expected, and she could feel the heat from the thick member on her soft flesh."
    "Harald seemed content to watch for the moment, his eyes roaming of Sabia's body and drinking in every curve."
    m1 "Yeah… c’mon, push your tits together, fucking get them tight around me!"
    "Sabia hoped she didn’t let them have too much stamina potion, it was already clear it was working on them."
    $ hentai_scene(8)
    "With one hand she gripped her breast, fingers digging into the pliant flesh as she pushed it against Tomas’ cock."
    m1 "Oh…. mmnnnggg! Fuck that's good!"
    "The low groans of enjoyment filled the room. Tomas started to rock his hips slightly, thrusting his cock just a little bit between Sabia’s tits."
    $ hentai_scene(9)
    "Pre-cum started to ooze from the tip of his shaft, and Sabia couldn’t help but find she enjoyed the heavy weight of the thick cock on her breasts."
    "If she was going to have to fuck them, she could at least enjoy it… and if the tentacle slime worked properly, she might enjoy it more than normal."
    s "I’ll get that slime now, I think? We don’t want to waste any of that potion right? And leave poor Harald over there!"
    m1 "I… uh, I guess not…"
    $ hentai_scene(11)
    "Frowning, Tomas pulled back, and Sabia grabbed the vial full of tentacle slime."
    "Doing her best to give a wicked smile, Sabia arched her back a little bit more, sticking her tits out, hard nipples pointing upward."
    $ hentai_scene(12)
    "The small dose of potion seemed to be working, and any hesitation they had was quickly dropping away as Sabia continued to play the naive girl."
    "She licked her lips quickly, and then tipped the bottle down, letting the purply, viscous goop fall down onto her tits."
    "It flowed slowly, and clung to her flesh and curves."
    m2 "Gimme… gimme some of that pussy!"
    $ hentai_scene(19)
    call shake ("h")
    "Grinning to himself, Harald moved over to Sabia, and yanked her on top of him, pushing her down until her pussy was pressing against his cock."
    s "Oh… fuck!"
    $ hentai_scene(16)
    "It worked almost straight away, Sabia could feel her tits and her stomach tingling, and a burning lust growing within her. She stopped the flow of the slime and put the bottle to the side."
    "Harald’s cock, with its heat and girth pressing against her pussy did nothing to help."
    "She could feel her arousal growing, her pussy started to throb in need and desire."
    $ hentai_scene(18)
    "Her chest rumbled, and her breath rushed out her nose in a shuddered exhale as hips started to rock back and forth, grinding her slit against the pulsing cock."
    s "I need this… fuck, I need this…"
    s "Fuck, it’s so big… and hot…"
    "Sabia moaned, running her dripping lips up and down Harald’s shaft, enjoying the pressure as she leaned forward a bit more."
    m2 "Fuuuuck! That’s…. hgnnnn!"
    "Harald gasped, and flopped back on the bed, thrusting against Sabia’s movements, the tip of his cock leaking a constant and steady stream of pre-cum that slipped back down the length of his shaft."
    $ hentai_scene(20)
    s "Holy shit… was that too much slime? I can’t… I… fuck, I need more!"
    m1 "Wait for me- I want some of that stuff!"
    s "Hurry up, then!"
    "Tomas wasted no time, angling himself in to position, and slapping his cock back down on Sabia’s tits."
    $ hentai_scene(21)
    "Tentacle slime splattered over all three of them as he did so, and Sabia poured the rest of the slime."
    "It dripped down, coating her body with more of the stuff, along with Tomas’ cock and Harald’s shaft below."
    s "N- mmnngg!"
    "Sabia’s eyelids fluttered wildly, and she felt a wave of pleasure rolling through her body and crashing."
    "Pleasure pulsed through her body, and the tentacle slime was only making everything feel better, and she knew she needed more."
    "Her pussy was sopping wet, and more of the slime still oozed down from the bottle."
    $ hentai_scene(22)
    "Once more, Sabia squeezed her breast against Tomas’ shaft, but this it felt far better. Every square inch of her flesh that the slime had touched was hyper sensitive."
    "Tomas’ cock slipped and slid around, the heat from his pole sending shivers of pleasure jolting through Sabia’s body, and making her whimper."
    $ hentai_scene(23)
    call shake ("h")
    s "OH FUCK!"
    $ hentai_scene(24)
    "Harald maneuvered himself so the tip of his pre-cum leaking cock was against Sabia’s needy slit, and he thrust in."
    m2 "I can’t… I need more, fuck!"
    "Gritting his teeth, his cock started to piston in and out of Sabia with a vigor that made the bed creak from the strain."
    $ hentai_scene(25)
    "Sabia could barely think, her body was afire with pleasure and hunger, desire and lust."
    "Her hips rolled back and forth, grinding against Harald’s cock as it filled her tunnel up."
    "Little whimpers rumbled in her throat, and her breath was uneven."
    m1 "This… this slime is really… nnnfg!"
    s "Mnnngggg!"
    "Sabia could barely speak. In fact, all three of them could barely speak. The tentacle slime really was a potent aphrodisiac, Sabia realized in the back of her mind."
    $ hentai_scene(29)
    "She threw the bottle away - there was more than enough slime over them all now."
    "Her nipples were like diamonds, and her tits kept bouncing and jiggling about, Tomas’ cock thrusting between them wildly."
    "She swore that Harald’s cock was swelling up inside her even more, growing a little thicker."
    "The pressure on her swollen pussy was growing, her lips straining to take the sheer girth of the frantically ramming pole."
    $ hentai_scene(30)
    call shake ("h")
    "Her whole body was bouncing up and down from Harald’s wild pounding, her ass slamming onto his thighs with loud claps, and the tip of Tomas’ pre-cum-and-slime-coated pole poking against her lips."
    "In her desperate need, her mind in a lust-fuelled haze driven by the slime, she tried to wrap her lips around Tomas’ cock, the need to suck growing, the desperate desire to sate her lust."
    "Both Tomas and Harald’s pace quickened even further, and Sabia’s eyes rolled to the back of her head, her mouth gaping open with a low rumbling groan drowned out by the slapping, and wet squelches of the voracious fucking."
    "She felt Tomas’ thrusting pole pulse, balls slapping against the bottom of her tits, and he erupted."
    $ hentai_scene(31)
    call shake ("h")
    "Cum gushed out, a thick rope of the stuff that painted her chin white."
    "The burning heat from it, the smell of it hitting her nostrils. And the constant tingling, throbbing of the slime over almost all of her body. It was too much."
    "She found herself cumming - thighs shuddering, twitching. Her muscles contracting, squeezing down around Harald’s shaft deep inside her."
    "Harald’s came too, his hands balling up more of the bedsheets as he unleashed a torrent of cum inside Sabia."
    "Her breath caught in her throat, and she felt the warmth inside her, spreading through her while Tomas still continued to paint her face and hair and chest with more jizz, the wild frantic haphazard thrusting sending more spurts of cum flying out."
    s "There’s… you’re cumming so much… there’s so much cum!"
    "Sabia gasped in surprise, feeling her insides swelling up with even more jizz before it started to gush out about Harald’s cock, oozing out and down her thighs, mixing with the viscous slime."
    "The tip of her nose dripped with jizz, and it coated her normally pink lips, and at least half of her bangs were wet and sticky, saturated with cum."
    "And yet they both still went, a few more desperate thrusts and at least another one or two normal loads worth of jizz painting Sabia’s face and insides, tits and thighs with more white."
    m1 "Fuck… that was… great!"
    $ hentai_scene(32)
    "Tomas blinked slowly, trying to keep his eyes open. Harald pulled out, and a river of cum gushed out of Sabia’s abused hole, a pretty picture of white cum and red, swollen pussy lips."
    "Sabia’s body still thrummed with lust, but she was coming down a little, and realized she had been riding the orgasm the whole time."
    m2 "I’m… that was… shit!"
    "Both of the merchants took a seat back down on the edge of the bed."
    $ hentai_scene(35)
    "Sabia licked her lips, unable to take her eyes from the their still dripping cocks."
    $ hentai_scene(37)
    "She shook her head."
    s "Fuck, I need to get this slime off me!"
    "Sabia moved to get up off the bed, and find something to wipe herself clean."
    call shake ("h")
    scene black
    "While she was distracted, either Tomas or Harald hit her over the head. Hard."
    "She woke up some time later, bound and gagged on their caravan, heading toward one of the bandit camps."
    "They laughed, joking about it, wondering if they'd ever get to use her again."
    if gallery_workaround == True:
        jump gallery
    return


label neve_bandits_live:
    play music sex1 fadeout 2.0 fadein 2.0
    $ hentai_scene(1,"neve_human_bandits",dissolve)
    "Neve's face was a light red, and the stark white-grey hair clung to her forehead, a sheen of sweat there. Another few beads of sweat rolled down her smooth cheeks."
    "All three of them were gleaming with sweat, and their chests rose and fell, hearts pumping as they breathed a little haggardly."
    $ hentai_scene(2)
    n "You boys have... mmh! Pretty big cocks..."
    "The praise seemed to urge them to try a little bit harder, and their heavy thrusting became a little more insistent."
    "The bandit holding her in place made sure his thick shaft plunged further into Neve's tight ass."
    "A thick coat of pre-cum covered his cock and made it slide in easier, but even still Neve couldn't help but bite her lip each time it pushed in, making her tight anal ring stretch around the throbbing girth."
    $ hentai_scene(3)
    "Above her, the other excited bandit pumped with a steady rhythm into her wet slit - true to what Neve had said, his member was long and thick as well."
    "Each time he thrust in, his toned stomach slapping wetly up against Neve's raised thighs, her pussy lips kissed the shaft tightly, stretching just a little as well."
    guard1 "...fuck!"
    $ hentai_scene(4)
    guard1 "Elf pussy is so fucking... uggh! So fucking tight!"
    guard1 "Your 'lil cunt is just trying to milk our dicks, isn't it, elf slut?"
    $ hentai_scene(5)
    "Neve moaned loudly, eyes rolling back as he started to slam into her pussy faster. It caused her to jostle about, holes bouncing on the two thick shafts."
    "They weren't in sync with their pounding, but every now and then both of them pushed into Neve at the same time, and she felt herself fill up with girthy eager meat."
    "Each time it happened, she felt the cocks pushing against each other inside her, rubbing the thin wall that separated her ass from her pussy."
    "A little squeak of pleasure rumbled in her throat, the feeling of being so full at the same time, both lengths of hot, throbbing cock surging in, stretching her holes and rubbing against everything."
    $ hentai_scene(6)
    guard2 "Gawd, she's so fuckin' hot!"
    guard2 "I'unno how... how long - nngg! I'm gonna be able to fuck this tight elf ass before cumming!"
    n "Mmmh! That's... that's sweet of you boys to say!"
    $ hentai_scene(27)
    call shake ("h")
    n "Hnnng!"
    "Neve gasped in surprise."
    "The bandit that had been mostly supporting her had taken his hand away from her stomach, and grabbed one of her bouncing tits. His fingers squeezing, enjoying the feel of them sinking into the generous amounts of pillow flesh."
    "But doing so made Neve sink a few inches on his cock almost instantly, his balls slapping loudly against her dripping slit, the wetness making it squelch as their rapid fucking slowed down a little, focusing more on her tits."
    guard2 "Fuck these tits, they're really fucking good!"
    $ hentai_scene(9)
    "The first bandit sunk himself into Neve's pussy with a long, low groan of delight at his friend's words, and his hand whipped through the air, lightly slapping Neve's free breast."
    "His fingers grazed her nipple, and she yelped involuntarily as her sensitive nipple sent sparks through her body, making her legs squeeze around his arms, and her holes clench about their cocks."
    "All in the one motion though, his hand came back down, squeezing her breast as well."
    $ hentai_scene(10)
    guard1 "They... they're alright. I bet... hgn... Kira's are still better!"
    n "Kira?"
    "Neve couldn't help moan, their cocks speeding up. The sounds of their shafts slamming into her wet holes, and squelching out the pre-cum and grool they were almost too loud for Neve's comfort."
    "But she couldn't deny how great it felt, and her fingers tightened around their muscles, nails scratching lightly as she started to wriggle her hips, angling herself to best get impaled by their eager pummeling."
    guard1 "Y...yeah Kira! Her tits... are... AMAZING."
    n "And... mine uggh!"
    $ hentai_scene(13)
    call shake ("h")
    "Neve's words got cut off as both of them slammed into her at the same time, and she felt her back slide along the chiseled chest several inches, her toes curling in wanton lust."
    n "Mine... mine aren't?"
    guard2 "He's... he's right, Kira's are really good! Fuck... she's... nng! So hot! But... so are you! You're the hottest elf we've... ngg... ever seen!"
    $ hentai_scene(14)
    "His hand wrapped around her breast again, squeezing almost painfully as he spoke, more beads of sweat rolling down both of the bandits' foreheads as their pace quickened even further."
    "The immediate surroundings of the forest started to fill with the sounds of wet flesh slapping against eager, wet skin."
    "Neve raised a quivering eyebrow, annoyed that they were talking about some other girl while they were quite literally balls deep inside her."
    n "Who's Kira?"
    $ hentai_scene(15)
    guard1 "One 'a the captains from another camp... she's... ngg, everyone dreams about fucking her - but she only likes girls!"
    "Despite his words, he must have really liked Neve's tits as his hand found its way back there quickly, unable to stay away from them."
    n "What a coincidence. I like girls too... maybe we should-"
    $ hentai_scene(16)
    call shake ("h")
    n "Fuck!"
    "Neve barely managed to draw a breath with how hard they rutted into her."
    $ hentai_scene(15)
    n "Do you boys like seeing girls together?"
    "Though they didn't say anything, their answer was clear. She knew they were imagining her and this Kira captain together, their cocks twitching within her eagerly."
    "Neve felt every bump and vein as they slammed in and out of her, her hard nipples rubbing against their callused hands, an extra source of constant sensory delight."
    "Her lips curled into a sly smile as her tits bounced, ass slamming down on the bandit's thighs, and her pussy dripping around the throbbing width of the other bandit's cock."
    n "Maybe... you two can introduce me to Kira? And we can have some fun... and if you're good, we might invite you!"
    n "It's always good to have some fun and-"
    $ hentai_scene(16)
    call shake ("h")
    "The image her few words painted in their minds was obvious to Neve, and their thrusting became frantic and uncontrolled, desperate to cum. Their breath was haggard, uneven."
    guard1 "Fuck! Gonna... gonna cum!"
    guard2 "Ugggghhhhhh!"
    $ hentai_scene(17)
    call shake ("h")
    "Neve felt both of the loads erupt within her at the same time."
    "She felt the heat of it filling her up as they convulsed within her, twitching, pulsing and swelling up just a little more, stretching her holes just that much more."
    "Their fingers gripped her tightly like a vice as they groaned, balls emptying rope after rope after rope of sticky cum, surely painting her white on the inside."
    $ hentai_scene(18)
    n "You boys done? It's not nice to finish before the lady..."
    guard1 "It's just... fuck, we couldn't, it's-"
    $ hentai_scene(20)
    guard2 "What're we meant to do when you're talking about-"
    guard1 "You and Kira sucking dick together! Fuck, big tits and smooth lips together-"
    guard2 "Yeah, that's like, impossible to not blow especially when you're balls deep in elf-holes!"
    n "And if I wanted to join your group... I'd talk to Kira?"
    guard2 "Yes! Oh fuck... Kira's-"
    guard1 "Yeah! She's gonna be at a meeting in another three moons. You should definitely go and join properly!"
    n "I bet you guys just want me to get into Kira's pants for you..."
    guard2 "Well... yeah we won't say no to that..."
    n "So where is the meeting, then?"
    guard1 "You know the old Lundari gold mine? It's abandoned. A bit north of there, I'm sure an elf can spot it!"
    n "I'm sure I can... well, since you've talked this Kira up so much, I think I'll have to go."
    "Though Neve really would have preferred to be finished off, she knew that she'd probably spent a bit too long here as it was."
    $ hentai_scene(19)
    n "Well, maybe next time, boys? In three moons time, maybe!"
    n "I've gotta get back... but if Kira lets me join and we hit it off, the two of us might have to say 'thank you' to you."
    guard1 "Fuck yeah!"
    "Getting up, Neve pulled herself off the slowly softening cocks. They were still big enough to almost be a plug, and as they popped out with a loud {i}fwwwoph!{/i}, massive loads of jizz oozed out of her holes, and down her thighs."
    scene bg black with dissolve
    "She wiped herself up quickly, and redressed, before heading off to find where Sabia had gone - much to the disappointment of the two bandits."
    guard1 "Shouldn't she know who Kira is?"
    guard1 "I ain't seen her around before..."
    guard2 "Shut the fuck up you idiot. We just got to fuck and dump a massive load inside a hot elf. Just don't say anything... maybe we'll get lucky again."
    guard2 "And besides the captain's gonna be fucking mad if he knows we left just to fuck an elf."
    guard1 "...yeah, alright."
    if gallery_workaround == True:
        jump gallery
    return


label neve_bandits_kill:
    play music sex1 fadeout 2.0 fadein 2.0
    $ hentai_scene(1,"neve_human_bandits",dissolve)
    "Neve's face was a light red, and the stark white-grey hair clung to her forehead, a sheen of sweat there. Another few beads of sweat rolled down her smooth cheeks."
    "All three of them were gleaming with sweat, and their chests rose and fell, hearts pumping as they breathed a little haggardly."
    $ hentai_scene(2)
    n "You boys have... mmh! Pretty big cocks..."
    "The praise seemed to urge them to try a little bit harder, and their heavy thrusting became a little more insistent."
    "The bandit holding her in place made sure his thick shaft plunged further into Neve's tight ass."
    "A thick coat of pre-cum covered his cock and made it slide in easier, but even still Neve couldn't help but bite her lip each time it pushed in, making her tight anal ring stretch around the throbbing girth."
    $ hentai_scene(3)
    "Above her, the other excited bandit pumped with a steady rhythm into her wet slit - true to what Neve had said, his member was long and thick as well."
    "Each time he thrust in, his toned stomach slapped wetly up against Neve's raised thighs, her pussy lips kissed the shaft tightly, stretching just a little as well."
    guard1 "...fuck!"
    $ hentai_scene(4)
    guard1 "Elf pussy is so fucking... uggh! So fucking tight!"
    guard1 "Your 'lil cunt is just trying to milk our dicks, isn't it, elf slut?"
    $ hentai_scene(5)
    "Neve moaned loudly, eyes rolling back as he started to slam into her pussy faster. It caused her to jostle about, holes bouncing on the two thick shafts."
    "They weren't in sync with their pounding, but every now and then both of them pushed into Neve at the same time, and she felt herself fill up with girthy, eager meat."
    "Each time it happened, she felt the cocks pushing against each other inside her, rubbing the thin wall that separated her ass from her pussy."
    "A little squeak of pleasure rumbled in her throat, the feeling of being so full at the same time, both lengths of hot, throbbing cock surging in, stretching her holes and rubbing against everything."
    $ hentai_scene(6)
    guard2 "Gawd, she's so fuckin' hot!"
    guard2 "I'unno how... how long - nngg! I'm gonna be able to fuck this tight elf ass before cumming!"
    n "Mmmh! That's... that's sweet of you boys to say!"
    "Out of the corner of her eye, Neve spotted Sabia looking over behind some large bushes."
    $ hentai_scene(27)
    call shake ("h")
    n "Hnnng!"
    "Neve gasped in surprise."
    "The bandit that had been mostly supporting her had taken his hand away from her stomach, and grabbed one of her bouncing tits. His fingers squeezing, enjoying the feel of them sinking into the generous amounts of pillow flesh."
    "But doing so made Neve sink a few inches on his cock almost instantly, his balls slapping loudly against her dripping slit, the wetness making it squelch as their rapid fucking slowed down a little, focusing more on her tits."
    guard2 "Fuck these tits, they're really fucking good!"
    $ hentai_scene(9)
    "The first bandit sunk himself into Neve's pussy with a long, low groan of delight at his friend's words, and his hand whipped through the air, lightly slapping Neve's free breast."
    "His fingers grazed her nipple, and she yelped involuntarily as her sensitive nipple sent sparks through her body, making her legs squeeze around his arms, and her holes clench about their cocks."
    "All in the one motion though, his hand came back down, squeezing her breast as well."
    $ hentai_scene(10)
    guard1 "They... they're alright. I bet... hgn... Kira's are still better!"
    n "Kira?"
    "Neve couldn't help moan, their cocks speeding up. The sounds of their shafts slamming into her wet holes, and squelching out the pre-cum and grool they were almost too loud for Neve's comfort."
    "But she couldn't deny how great it felt, and her fingers tightened around their muscles, nails scratching lightly as she started to wriggle her hips, angling herself to best get impaled by their eager pummeling."
    guard1 "Y...yeah Kira! Her tits... are... AMAZING."
    n "And... mine uggh!"
    $ hentai_scene(13)
    call shake ("h")
    "Neve's words got cut off as both of them slammed into her at the same time, and she felt her back slide along the chiseled chest several inches, her toes curling in wanton lust."
    n "Mine... mine aren't?"
    guard2 "He's... he's right, Kira's are really good! Fuck... she's... nng! So hot! But... so are you! You're the hottest elf we've... ngg... ever seen!"
    $ hentai_scene(14)
    "His hand wrapped around her breast again, squeezing almost painfully as he spoke, more beads of sweat rolling down both of the bandits' foreheads as their pace quickened even further."
    "The immediate surroundings of the forest started to fill with the sounds of wet flesh slapping against eager, wet skin."
    "Neve raised a quivering eyebrow, annoyed that they were talking about some other girl while they were quite literally balls deep inside her."
    n "Who's Kira?"
    $ hentai_scene(15)
    guard1 "One 'a the captains from another camp... she's... ngg, everyone dreams about fucking her - but she only likes girls!"
    "Despite his words, he must have really liked Neve's tits as his hand found its way back there quickly, unable to stay away from them."
    n "What a coincidence. I like girls too... maybe we should-"
    $ hentai_scene(16)
    call shake ("h")
    n "Fuck!"
    "Neve barely managed to draw a breath with how hard they rutted into her."
    $ hentai_scene(15)
    n "Do you boys like seeing girls together?"
    "Though they didn't say anything, their answer was clear. She knew they were imagining her and this Kira captain together, their cocks twitching within her eagerly."
    "Neve felt every bump and vein as they slammed in and out of her, her hard nipples rubbing against their callused hands, an extra source of constant sensory delight."
    "Her lips curled into a sly smile as her tits bounced, ass slamming down on the bandit's thighs, and her pussy dripping around the throbbing width of the other bandit's cock."
    n "Maybe... you two can introduce me to Kira? And we can have some fun... and if you're good, we might invite you!"
    n "It's always good to have some fun and-"
    $ hentai_scene(16)
    call shake ("h")
    "The image her few words painted in their minds was obvious to Neve, and their thrusting became frantic and uncontrolled, desperate to cum. Their breath was haggard, uneven."
    guard1 "Fuck! Gonna... gonna cum!"
    guard2 "Ugggghhhhhh!"
    $ hentai_scene(17)
    call shake ("h")
    "Neve felt both of the loads erupt within her at the same time."
    "The heat of it filled her up as they convulsed within her, twitching, pulsing and swelling up just a little more, stretching her holes just that much more."
    "Their fingers gripped her tightly like a vice as they groaned, balls emptying rope after rope after rope of sticky cum, surely painting her white on the inside."
    $ hentai_scene(18)
    n "You boys done? It's not nice to finish before the lady..."
    guard1 "It's just... fuck, we couldn't, it's-"
    $ hentai_scene(20)
    guard2 "What're we meant to do when you're talking about-"
    guard1 "You and Kira sucking dick together! Fuck, big tits and smooth lips together-"
    guard2 "Yeah, that's like, impossible to not blow especially when you're balls deep in elf-holes!"
    n "And if I wanted to join your group... I'd talk to Kira?"
    guard2 "Yes! Oh fuck... Kira's-"
    guard1 "Yeah! She's gonna be at a meeting in another three moons. You should definitely go and join properly!"
    n "I bet you guys just want me to get into Kira's pants for you..."
    guard2 "Well... yeah we won't say no to that..."
    n "So where is the meeting, then?"
    guard1 "You know the old Lundari gold mine? It's abandoned. A bit north of there, I'm sure an elf can spot it!"
    n "I'm sure I can... well, since you've talked this Kira up so much, I think I'll have to-"
    stop music fadeout 2.0
    call shake ("h")
    s "Aahhhhhh"
    "Neve heard a squeal a hundred or so yards away, and she glanced back to where she had seen Sabia earlier."
    n "...sorry boys, seems it's your unlucky day."
    play music "<from 1.2>music/killers.mp3"
    $ hentai_scene(22,effect=dissolve)
    n "You're going to get to meet my friend."
    guard2 "Huh, whatcha mean, more elf girls?"
    n "Not quite. I don't think you're going to like him..."
    n "He's a bit of a jealous friend..."
    $ hentai_scene(23)
    call shake ("h")
    "The surge of power filled her, and the sword cut through the air like an arrow."
    $ hentai_scene(24)
    "Blood dripped down, oozing from where Neve's sword had sliced cleanly through flesh and dripping from the blade."
    "The weapon's power quickly faded from Neve, and she sighed."
    n "Seros, thy child offers this blood. Seros, thy child thanks thee. Seros, thy child walks with thee."
    $ hentai_scene(25,effect=dissolve)
    "The bandit guards gurgled out their surprise as Neve's blade drank the blood, the copper-scented liquid slowly disappearing as the blade gleamed in the light."
    guard1 "Gllk...gggkll!"
    n "Not how I would have liked it to end, but it seems my friend got caught... and that means there's no point in keeping you two alive."
    guard2 "I... b-butttggllkk..."
    $ hentai_scene(26)
    "It'll only hurt for a moment longer, don't worry. At least you had a nice goodbye."
    "Neve pulled herself off the two bandits, and wiped herself off as best she could with their discarded clothes, before donning her own garments. She flicked her sword swiftly, the blood splattering the ground."
    "Gently, Neve sheathed the sword once more, and headed off to find where Sabia had been taken to."
    if gallery_workaround == True:
        jump gallery
    return


label orc_bandits:
    play music sex2 fadeout 2.0 fadein 2.0
    "Sabia's eyelids fluttered open and she found herself looking up at the forest canopy, her back a little bit sore."
    $ hentai_scene(6,"sabia_orc_bandits",dissolve)
    s "...huh, whas... what's happening?"
    orc "Heh, little thief awake! Lucky for Rutjrod that Rutjrod see you in captain's cave! Captain doesn't care what happens to intruders."
    "It took a few seconds for Sabia to process what was happening, but the tingling in her pussy, and the fact that she was naked helped clear it up very quickly."
    $ hentai_scene(5)
    s "Hey - what the fuck?! Get OFF of me!"
    orc "No!"
    "The orc grinned, the thick green member sliding in and out of Sabia's pussy easily."
    "It was big, and the force of his thrusts were enough to jostle Sabia about the ground."
    orc "Never fuck human as hot as you!"
    orc "Definitely gonna finish and cum inside!"
    s "What?! Don't fucking cum inside me!"
    $ hentai_scene(7)
    call shake ("h")
    "Another orc came over from out of Sabia's line of sight, cock hard and ready. Crouching down, it slapped against Sabia's face with a noticeable thud before he rubbed the tip against her lips."
    $ hentai_scene(8)
    s "Get that thing away from me or I'll fucking bite it off!"
    orc2 "Shut up, you're not going to bite anything. You're lucky you weren't killed when you were knocked out."
    orc2 "Open your fucking mouth, and if you do a good job..."
    "Sabia took a second to contemplate the unspoken offer, though it was difficult with an orc cock slamming into her pussy over and over."
    "She doubted very much whether they were going to let her go after they caught her sneaking around."
    $ hentai_scene(9)
    call shake ("h")
    s "Gglkkghhhg!"
    $ hentai_scene(10)
    "Barely opening her lips seemed like it was enough of an opportunity for the orc, and he took the chance to bury his cock inside Sabia's mouth."
    "The entire length slammed down and bulged her throat out and cut off her air immediately - and even if it hadn't, the large set of eager balls resting on her nose would have made it impossible to breathe."
    s "Gnnnggg mnnmmm! Ggnnfff! Mmmmmgg!"
    "Sabia's lungs started to burn quickly as the need for air grew, and she started bucking wildly, trying to throw him off of her."
    $ hentai_scene(11)
    orc1 "Haha, purple-haired slut is getting excited - she likes it! She's going wild on Rutjrod's cock!"
    "Rutjrod started to speed up, his hips slapping hard against Sabia's thighs, the mix of sweat and pre-cum and grool making it squelch and slick, the sounds bouncing about the trees."
    s "NNGG! Nmmmng!"
    "She needed air, her nose was stifled by orc-balls, and her mouth was full of orc-cock, she couldn't breathe."
    "Her chest heaved, jerking wildly in her desperation. It only served to squeeze her throat tighter about the second orc and it did little else except help Rutjrod's thrusts bury themselves deeper in her quivering slit."
    call shake ("h")
    $ hentai_scene(12)
    "Rutjrod groaned out, impaling every inch of his cock inside Sabia as he came, while the second orc pulled back a little and made sure the tip of his cock was resting on Sabia's tongue as his cock splattered the monstrous load inside Sabia's mouth."
    $ hentai_scene(13)
    "Immediately, she tried spitting it out and taking a breath at the same time. The cum quickly ran down her face and covered her nose, and her breath resulted in cum gushing down her nostrils."
    "She coughed wildly, the seed's salty taste and scent filled her senses quickly, and she coughed some more."
    $ hentai_scene(14)
    "Mercifully, they both pulled out, and with tears running down her cheeks and mixing with the orc's seed, she managed to catch a ragged, deep breath. It tasted like orc."
    "She spat as much of the foul stuff out as she could, and writhed her legs in vain, trying to rid herself of the cum leaking out of her pussy."
    $ hentai_scene(15)
    orc2 "Here, you can have her."
    orc1 "Rutjrod done too!"
    $ hentai_scene(16,effect=dissolve)
    "It seemed that at least one other patrol had heard about the purple-haired, big-titted human that was found, and had come over to use Sabia after the first two had finished."
    $ hentai_scene(17)
    "The two new orcs argued over who was getting what hole, but when they settled on it, they quickly pushed themselves into Sabia, despite her pleading and protests."
    "She felt sickened at the sound of cum gushing out of her from the cock forcing its way in."
    "Air was running low again, and just when she thought she was going to pass out-"
    $ hentai_scene(18)
    call shake ("h")
    orc2 "SHIT WHAT THE FUCK?!"
    "The still-headed orc pulled himself out of Sabia quickly, and scrambled to his feet and his weapon nearby."
    if gallery_workaround == True:
        jump gallery
    return


label human_bandits:
    play music sex2 fadeout 2.0 fadein 2.0
    $ hentai_scene(1,"sabia_human_bandits",dissolve)
    "Sabia's eyelids fluttered open and she found herself on her back on the forest floor."
    "A hulking frame loomed atop her, and she jumped in surprise. Or tried to at least. Her hands were bound, wrapped tightly with rope."
    "The world spun about her as she blinked a few times, trying to focus. A cool breeze passed over and she realized that she was stripped bare, and a hot hard cock was rubbing against her pussy."
    $ hentai_scene(2)
    bandit1 "Heh, you're awake you little sneaky slut. Trying to steal from us!"
    bandit1 "Well, I bet you'll regret that now."
    "Grinning as he rocked his hips back and forth, grinding his hard shaft against Sabia's sensitive pussy, his hand reached up and gave a light slap to her tits."
    "It brushed against both of her nipples and Sabia hated the little groan that rumbled in her throat from it."
    bandit1 "Look how wet your cunt is, and how hard your nipples are. Probably don't even need to have you tied down, do I?"
    $ hentai_scene(3)
    s "Fuck you! I'll drive my blade into you when I get-"
    $ hentai_scene(4)
    call shake ("h")
    bandit1 "Hmph! That shut you up for a little bit, didn't it?"
    $ hentai_scene(5)
    bandit1 "Fuck, you're pretty tight. With tits and a face like that I thought you might've fucked a bunch of dicks already, heh!"
    $ hentai_scene(6)
    "Smirking to himself, he leaned forward a little bit, using the angle as leverage to start rutting into Sabia."
    "Her tits bounced and jiggled from the force of his thrusting, and her wrists pulled painfully on the bonds and pegs as they slid about."
    s "Get the fuck off me, you bastard! How dare you!"
    bandit1 "Hey, get over here! Do something about this cunt's mouth. I like her better when she can't talk!"
    $ hentai_scene(7)
    call shake ("h")
    "Another bandit, already naked, stepped over Sabia's head and squatted down, his cock landing with a heavy thud on her face."
    "The first one was pumping away at her pussy, and in the back of Sabia's mind she had to admit he knew what he was doing."
    $ hentai_scene(8)
    s "What the fuck? Get that off me! I hope you don't think that's going in my mouth, I'll fucking bite it off!"
    $ hentai_scene(9)
    call shake ("h")
    s "Glkkg!"
    $ hentai_scene(10)
    "Sabia shuddered as it impaled her. The head forced its way past her lips, and pushed her tongue down against the bottom of her mouth, and made her cheeks puff out."
    "It pushed up uncomfortably against the back of her throat, and with a grunt of frustration the second bandit jerked forward. The tip slipped down into the rest of her esophagus, and bulged her neck out."
    s "Mnnggfflkl... hhfggooo nggnnaaa nnnnffkkk ai!"
    "Her attempt at a threat ended up just being a series of loud gags, with her throat rumbling, tightening around the cock."
    bandit2 "Heh, she is better when she's quiet. And don't worry, you're not gonna be biting anything off. Not with something that big in your throat!"
    "Chuckling to himself, he squeezed his hand around Sabia's throat a little tighter."
    "Almost immediately, Sabia's chest heaved, and she started writhing against the weight of the men atop her. Her eyes were running, watering, and her nostrils flared in vain as she tried to breathe."
    $ hentai_scene(11)
    "A few seconds before she was sure she'd pass out, some mixed relief came as they started to piston in and out of her holes."
    "As the cock pulled out of her throat, it gave her a half-second to catch a quick breath of air before it plunged back in, spit and pre-cum from his cock being scooped up by her lips."
    s "Nnggg! Rrrran... gglkh!"
    bandit1 "Fuck me, she's still trying to talk. What a stupid cunt. Save that air for breathing!"
    "Their pace quickened further, and Sabia could barely breathe, even with the small reprieves. There was so much of the mix of liquids that it pooled over her nose, popping up in little bubbles as she tried to keep it from oozing down."
    "More of the stuff started to drip down further onto her eyes, coating her face in the sticky mixture."
    bandit2 "Haha, when she tries to breathe or talk, it just makes her squeeze my dick tighter! Feels fucking great."
    s "...glk... gglk..."
    "Sabia's chest burned with the need for air, and she felt herself starting to go lax. With her muscles not as tense, her tits started to bounce about even more wildly as they started to hammer in, ready to unload in each of Sabia's holes."
    $ hentai_scene(12)
    call shake ("h")
    bandit2 "Nnngg FUCK!"
    bandit1 "...ugh! Fuck, what a great cunt!"
    $ hentai_scene(13)
    "The one in her throat started dumping his load first - at least Sabia thought it was him. She wasn't sure, the other one started cumming almost at the same time, pulling out halfway through and splattering her stomach with a healthy dose."
    "There was the familiar tell-tale warmth spreading from her depths, but it was quickly superseded by the feeling of hot jizz gushing down her throat, her jaw aching as the cock swelled up a little thicker."
    "It ran down, settling into her stomach with a slosh that she swore she could hear. Or it might have just been the blood pounding in her ears as the need for air almost made her pass out."
    $ hentai_scene(16)
    "Sabia coughed, wretching violently and spitting up as much of the cum as she could, and a thick load of it oozed over her lips and down her chin while more of it bubbled up from her nose."
    bandit2 "Heh, it's a good throat. Next time I'm taking her pussy though."
    bandit1 "Sounds good. I'll take her throat since she's a bit annoying when she's talking anyway... but I'm sure that can be fixed."
    s "Nnggh... gglk! F... fuck you, you bastards!"
    "Sabia's chest stung as she managed to get some air down, her eyes coated in jizz, and tears and cum mixed as it ran down her cheeks."
    $ hentai_scene(17)
    bandit1 "We'll go get cleaned up, and we'll be back for you in a minute..."
    if gallery_workaround == True:
        jump gallery
    return


label mino_badend:
    play music sex2 fadeout 2.0 fadein 2.0
    "Sabia's eyelids fluttered open and she found herself on her back on the forest floor."
    "A hulking frame loomed atop her, and she jumped in surprise. Or tried to at least. Her hands were bound, wrapped tightly with rope."
    "The world spun about her as she blinked a few times, trying to focus. Something soft and warm brushed against her legs, and a heavy warmth was resting on her stomach."
    minotaur "You're awake?"
    s "Ugh... my head hurts..."
    s "What's going-"
    $ hentai_scene(19,"sabia_minotaur_bandit",dissolve)
    s "Hey, wait a minute."
    "The coolness of the air quickly made sense as she saw her bared breasts, hard nipples pointing skyward, and a thick flared minotaur shaft resting on her stomach."
    "It was already oozing pre-cum, a heavy stream that would almost match a human's normal load. And it was much stronger, a heavy salty scent that filled the air even in the open space."
    s "That's {i}not{/i} going to fit inside me, it's way too fucking big and-"
    $ hentai_scene(4)
    call shake ("h")
    "The minotaur angled himself back, and the heavy cock pulled against Sabia's stomach, leaving a glistening trail of musky pre-cum behind before he lined the tip up against her opening and slammed forward."
    $ hentai_scene(5)
    "His nostrils flared widely as he snorted, several inches of his cock still not yet inside Sabia, even though she was almost entirely full."
    s "Fucking... get off of me!"
    "Sabia's eyes wandered down a little, and saw the bump of her stomach, the minotaur's girth big enough to bulge her out."
    $ hentai_scene(6)
    s "Get your filthy hand off me, and untie me now!"
    "Sabia writhed about on the ground, trying at the same time to both get away from the hand gripping her body, and to try and pull herself free from the pegs in the ground."
    "The bonds about her wrists were tight enough that there was no slack and her efforts were in vain. She didn't have long to ponder it though."
    $ hentai_scene(7)
    "The minotaur grabbed the other side of her body with hands as big as her head, and started to pullf her back and forth, sliding Sabia along the ground."
    "Despite herself, Sabia's mouth opened and her eyes rolled back as the full weight of the minotaur's cock slammed into her almost-too-small hole."
    "Each time the minotaur pulled Sabia off his leaking cock, it felt like it left her empty inside for the instant before he yanked her back down."
    $ hentai_scene(9)
    "Sabia grit her teeth, clenching her jaw as her pussy started to tingle and throb. The heat of the cock was filling her up from inside, the warmth from his grip on her."
    "A sheen of sweat quickly covered most of her body, and her arms started to ache a little bit, shoulders pulled up and down with every thrust the minotaur made."
    minotaur "Humans are so weak. I don't know how we ever lost to Lundar... you can barely stop yourself moaning, desperate for more."
    "Sabia hurled a wad of spit that landed on the minotaur's face, though he just chuckled."
    s "I'm not moaning."
    $ hentai_scene(10)
    call shake ("h")
    s "Hhhnnnngg!"
    $ hentai_scene(11)
    "Sabia's blush deepened considerably as she couldn't help screaming out. The minotaur's thrusts became more determined, and the entire length impaled her frame."
    "The gut-wrenching behemoth of a cock unloaded within her small frame, an immense load of hot bull cum erupting inside."
    "Sabia's eyes widened even further as she felt the balls against her thighs, almost burning hot and pulsing, more and more and more cum being dumped in her tight tunnel."
    $ hentai_scene(12)
    "Not needing to say anything, the minotaur snorted again, and before long his load started to bubble out from the seal his thick cock and her tight pussy were making with loud, squelching sounds that made Sabia shudder."
    s "Okay... you're done now... you can... you can... nggg... {i}fuck!{/i}"
    $ hentai_scene(13)
    "He pulled out of her abruptly, and swung the still rock-hard member down on Sabia's belly. The impact caused a squirt of his cum to gush out of her gaping pussy, coating her thighs in the thick, sticky smelly stuff."
    s "You can let me go now... since you're done."
    "Sabia grimaced as she spoke. The smell of crushed blades of grass mingled with the minotaur seed in the air, and she knew her back was going to be almost a stark green for how viciously she'd been sliding back and forth on the forest floor."
    $ hentai_scene(14)
    minotaur "Done...?"
    "A wicked smile curled about his lips, teeth glinting. His hand grabbed Sabia's side once more and squeezed."
    $ hentai_scene(15)
    minotaur "We're just starting."
    "Sabia looked down, and saw the flared, thick head of the shaft still rock hard, twitching and pointing at her. Cum was dribbling out the tip, more and more coating her belly with the stuff."
    "Her pussy throbbed from how hard she'd just been fucked, and she didn't know if she could take another pounding from the relentlessly strong beast."
    "Slowly, his cock crept down further as he teased her with the weight of it, down, down her stomach, the tip leaving a new trail of hot seed behind."
    s "No... no no, that's - you're going to hurt me if you fuck me again like that!"
    "He ignored her, cock creeping down past her pelvis."
    $ hentai_scene(16)
    s "PLEASE! Don't, please! There's already so much cum inside! I don't want to get pregnant either! You're going to-"
    $ hentai_scene(17)
    call shake ("h")
    "The minotaur rammed his hard cock back into Sabia, his length sliding along her sensitive, red pussy lips as at least half the load of cum gushed out from the force, splattering everywhere."
    $ hentai_scene(18)
    "Sabia's bouncing body made the cum on her stomach move slowly, oozing down to the lowest point, a lot of it settling into her belly-button and cooling."
    "As the other cum dried, it started to pull softly, tugging at her skin as she was jostled about like the minotaur's new toy."
    "Before long, she felt the swollen sack slap up against her cum-coated thighs once more, and pump another load of minotaur cum into her."
    s "Nngh... no... no more... I'm so... so full... please."
    s "It's like..."
    minotaur "I'm not done yet..."
    if gallery_workaround == True:
        jump gallery
    return


label bandit_ultimate_bad_end:
    play music sex2 fadeout 2.0 fadein 2.0
    $ hentai_scene(1,"sabia_bandits_badend",dissolve)
    "Several months had passed, and Sabia hadn't been outside since she had been brought here."
    "The bandits had made her their free use toy, open to anyone who needed to dump a load in something."
    "Something - not someone. None of them saw Sabia as someone anymore, just a set of holes to fuck."
    $ hentai_scene(2)
    "She barely felt the orcs pounding every one of her holes as her pregnant belly swayed uncomfortably underneath her."
    "Her tits had grown slowly, filling with milk."
    "She didn't even know who the father was."
    "Certainly one of the human bandits, but whom? She didn't know."
    $ hentai_scene(3)
    call shake ("h")
    "Sabia's lips stretched around the cock inside her mouth as he slammed forward, his fingers entwined with her hair, helping to yank her down. The other two held nothing back as they reamed her ass and pussy."
    $ hentai_scene(4)
    "A few tears rolled down her face as she struggled to breathe, cum filling her up once more."
    $ hentai_scene(5)
    "After a few moments, she felt the cock sliding out past her lips, the heavy scent of orc cum stinging her nostrils."
    "She glanced up with a dead look in her eyes."
    s "Thank you..."
    orc "Heh, no worries. Yarnak come give you your dinner tomorrow too. Yarnak can't wait till you pop out this kid, Yarnak will knock you up next time for sure."
    scene bg black with dissolve
    "Sabia watched him leave, only for another hard cock to enter the room, ready to take Yarnak's place."
    if gallery_workaround == True:
        jump gallery
    return


label neve_sabia_dance_dom:
    play music sex1 fadeout 2.0 fadein 2.0
    $ hentai_scene(1,"sabia_dancing_practice",dissolve)
    n "And? Go on, over there. Show me your moves, Sabia."
    "Neve couldn't help but have a smirk on her face as she pointed to the pole."
    "With a little hesitation and some palpable trepidation, Sabia wrapped her hands around the pole and arched her back."
    $ hentai_scene(2)
    s "Like this?"
    n "Well, it's certainly a view I'm not sad to see. But you'll actually have to dance - so go on, show me what you have."
    "Sabia tried her best to remember back to her dance lessons when she was younger, though the dance was a little bit different than what she had to do now."
    "Her thoughts then went to the girls that worked in her mother's establishment, and slowly, she started her best to emulate them."
    $ hentai_scene(4)
    "Taking a little wider of a stance, she let her hands slip down further around the pole, sticking her ass out more."
    "With a languid grace that she barely managed, Sabia started to dance, her back undulating in long, slow motions."
    n "What's your other hand doing?"
    s "I... what?"
    n "You've got one hand on the pole. And the other is...? Just hanging there? Doing nothing?"
    "Neve bit her lip, trying to stop her smirk widening. Sabia felt the elf was enjoying this far too much already."
    $ hentai_scene(5)
    "But nevertheless, Sabia gave her rear a gentle slap with a smile, and dug her fingers into her soft flesh as she rolled her hips side to side."
    "The movement was slow enough that the thin piece of fabric that - admittedly - barely covered her slit continued to... barely cover it."
    n "Make that ass bounce, Sabia! Don't be so timid, you've got to make it exciting for them."
    "Sabia glanced back and saw Neve grinning."
    n "If you're worried about them seeing your pussy, don't worry - I brought a present for you. I thought it might help."
    "Neve answered by producing something small in her hands - Sabia didn't see where she had it hidden."
    $ hentai_scene(6)
    s "What's that?"
    n "It'll cover your pussy. Then you can move more, and not worry about your cute little dress flitting about and letting your audience see your pussy."
    s "..."
    s "How is it going to stay there? It's just one tiny piece of-"
    $ hentai_scene(7)
    n "It goes up your butt."
    "Neve pointed to the little jeweled end of the plug, tapping it with her nail."
    $ hentai_scene(8)
    "Sabia huffed, and yanked her hand away from her ass."
    s "I'm not dancing around in front of orcs with something up my ass, Neve!"
    s "Dancing dressed up like this wasn't my first choice as it is!"
    n "Why not?"
    n "It'll be fun."
    $ hentai_scene(9)
    n "Plus, if you don't, then everyone will see your pussy and ass. And no one's going to know that it's plugged up except you and me."
    "Neve twirled the little bejeweled c-string about in her fingers deftly, an eager look etched on her face."
    n "C'mon. It'll look hot on you."
    $ hentai_scene(8)
    s "No stuff up my butt!"
    $ hentai_scene(10)
    n "Okay, okay then. Just thought it was a good idea. Get back to showing me your dance moves, then. You'll need to move a little faster!"
    $ hentai_scene(7)
    "Sabia frowned, before resuming her practice. This time she moved a little bit faster."
    "Shaking her ass side to side, she felt it bouncing around, her thighs jiggling."
    "Her tits pressed up against the pole, the metal slipping between them as she arched her back out even further."
    "Biting her lip as she tried to concentrate, she didn't see Neve smirked, sucking on the plug."
    "The Elf swirled her tongue around it, making it nice and wet as her eyes greedily drank in the sight of Sabia's toned ass."
    "Waiting for the perfect moment, Neve saw it and moved with the speed and grace that only an Elf can exhibit."
    $ hentai_scene(12)
    call shake ("h")
    "With delicate and skilled fingers, Neve slipped the plug up against Sabia's hole, and pushed it in, smirking at Sabia's surprised yelp."
    $ hentai_scene(13)
    "Neve chortled to herself, and leaned back in her seat."
    s "What the fuck, Neve!"
    n "Relax Sabia. It suits you."
    $ hentai_scene(14)
    "Ignoring Sabia's blustering, Neve ran her thumb over Sabia's now-covered slit, pressing gently while her index finger made sure every inch of the plug was inside."
    n "And besides, now you won't need to worry about the orcs seeing your pussy. If that was a problem."
    n "So you can dance properly now, right?"
    $ hentai_scene(15)
    "Neve pulled her hand away slowly, making sure to tease as she did so, running her fingers against the tiny slip of fabric."
    s "It would have been nice for you to at least warn me."
    "Neve smirked again, and licked her lips."
    n "I did. But you said no. So I took it into my own hands."
    n "Back to dancing, Sabia! I can't help if you don't dance, after all."
    $ hentai_scene(16)
    "Sabia grumbled, but still started to sway back and forth to a beat that only she heard."
    $ hentai_scene(17)
    "Putting a smile back on her face, her hips started to rock more."
    "The c-string with the plug on it both made her feel a little bit more confident, and at the same time more vulnerable."
    "She wasn't entirely sure how she felt about it - on one hand, she did like the idea that her piece of fabric wouldn't be flitting about and letting the entire tribe get a good look at her slit."
    "But on the other hand, she couldn't help but give a few little squeaks and moans as the plug pushed against her, inside, with every little movement jostling it about."
    "Still, her dancing got more evocative, and she started to use the pole more, remembering the spins and dances that the girls in her mother's establishments did."
    "Sabia gripped the pole tightly, and tried to spin around while holding her legs up in the air."
    "It wasn't nearly as easy as she thought it was going to be, but she still managed to do a full circle around the pole and-"
    $ hentai_scene(18)
    call shake ("h")
    s "NEVE!"
    $ hentai_scene(19)
    n "I couldn't help myself."
    n "It's just such a nice ass... and right there. And such a nice show you're putting on for me."
    $ hentai_scene(20)
    "Sabia looked back. Neve had an almost predatory smile on her face, and the elf showed no signs of taking her hand away."
    n "I'm just trying to help. You don't think there will be orcs coming up, trying to grope that ass?"
    $ hentai_scene(21)
    n "It's just preparation. You'll need to be ready for it - as well as able to dance."
    n "You do want my help right?"
    s "Well, yes, I do want your help, it's just that..."
    "Sabia wriggled about, rubbing her thighs together. She found that she was a little more excited than she had anticipated from doing this."
    "After her protests, she didn't want to say it - but the fabric over her pussy was probably a good idea, even though she felt it slowly getting wetter and wetter."
    n "It's just what? Shh, don't worry Sabia, just put that pretty smile back on your face, and start moving again."
    "Neve winked, and Sabia realized how much the elf was enjoying it. She could see it on the elf's flushed face, and the hard nipples poking out from Neve's top."
    $ hentai_scene(23)
    "Sabia resumed her show - after all, getting everyone excited really was the whole point of it."
    $ hentai_scene(24)
    call shake ("h")
    s "UGH! I thought you weren't going to do that anymore!"
    $ hentai_scene(25)
    n "I never said that."
    $ hentai_scene(26)
    s "Well, you better not be doing it anymore."
    n "Alright, alright Sabia!"
    s "That means take your paws off, Neve!"
    "Sabia grit her teeth together, trying to ignore how good the plug felt inside her tight hole."
    $ hentai_scene(27)
    "Looking up at Sabia's angry gaze, Neve licked her lips, and then looked back down to Sabia's ass."
    n "Don't be that way. You've got such a great ass, Sabia."
    s "Hands off!"
    $ hentai_scene(29)
    n "Okay, okay. Just trying to have a little bit of fun, Sabia."
    n "But you know the orcs will be doing the same."
    n "And even if you scold them, they might not be so complicit as me."
    $ hentai_scene(30)
    "Not answering straight away, Sabia started to sway and spin about the pole again. Every few moments, the sound of her hand against her red ass filled the small area."
    "Now that she wasn't being badgered by Neve's ministrations and groping, she was getting more into the rhythm of it - but she knew she would need a bit more practice before she held the event."
    $ hentai_scene(31)
    s "Well... that just means that I'll need someone to come along and make sure they keep their hands off."
    "Neve smiled, and leaned back a little bit. Now that she'd been effectively banned from touching Sabia, she made it no secret how much she was enjoying the show."
    "Her nipples were hard, and one of her hands played lazily at her mound, through the fabric of her leggings."
    n "I'll think about it..."
    n "But until then, don't stop the show. And you'll need some more practice."
    $ hentai_scene(32)
    s "...looks like you're enjoying it enough."
    n "One can find appreciation in both expert and amateur levels, Sabia..."
    "Sabia spent a little bit longer practicing dancing, all the while her pussy was tingling a little more, and the pressure against her soft insides from the plug more insistent."
    "She wasn't sure if she could hold off until Neve left, but she knew she'd have to relieve herself when Neve did leave."
    if gallery_workaround == True:
        jump gallery
    return


label neve_sabia_dance_sub:
    play music sex1 fadeout 2.0 fadein 2.0
    $ hentai_scene(1,"sabia_dancing_practice",dissolve)
    n "And? Go on, over there. Show me your moves, Sabia."
    "Neve couldn't help but have a smirk on her face as she pointed to the pole."
    "With a little hesitation and some palpable trepidation, Sabia wrapped her hands around the pole and arched her back."
    $ hentai_scene(2)
    s "Like this?"
    n "Well, it's certainly a view I'm not sad to see. But you'll actually have to dance - so go on, show me what you have."
    "Sabia tried her best to remember back to her dance lessons when she was younger, though the dance was a little bit different than what she had to do now."
    "Her thoughts then went to the girls that worked in her mother's establishment, and slowly, she started her best to emulate them."
    $ hentai_scene(4)
    "Taking a little wider of a stance, she let her hands slip down further around the pole, sticking her ass out more."
    "With a languid grace that she barely managed, Sabia started to dance, her back undulating in long, slow motions."
    n "What's your other hand doing?"
    s "I... what?"
    n "You've got one hand on the pole. And the other is...? Just hanging there? Doing nothing?"
    "Neve bit her lip, trying to stop her smirk widening. Sabia felt the elf was enjoying this far too much already."
    $ hentai_scene(5)
    "But nevertheless, Sabia gave her rear a gentle slap with a smile, and dug her fingers into her soft flesh as she rolled her hips side to side."
    "The movement was slow enough that the thin piece of fabric that - admittedly - barely covered her slit continued to... barely cover it."
    n "Make that ass bounce, Sabia! Don't be so timid, you've got to make it exciting for them."
    "Sabia glanced back and saw Neve grinning."
    n "If you're worried about them seeing your pussy, don't worry - I brought a present for you. I thought it might help."
    "Neve answered by producing something small in her hands - Sabia didn't see where she had it hidden."
    $ hentai_scene(6)
    s "What's that?"
    n "It'll cover your pussy. Then you can move more, and not worry about your cute little dress flitting about and letting your audience see your pussy."
    s "..."
    s "How is it going to stay there? It's just one tiny piece of-"
    $ hentai_scene(7)
    n "It goes up your butt."
    "Neve pointed to the little jeweled end of the plug, tapping it with her nail."
    $ hentai_scene(8)
    "Sabia huffed, and yanked her hand away from her ass."
    s "I'm not dancing around in front of orcs with something up my ass, Neve!"
    s "Dancing dressed up like this wasn't my first choice as it is!"
    n "Why not?"
    n "It'll be fun."
    $ hentai_scene(9)
    n "Plus, if you don't, then everyone will see your pussy and ass. And no one's going to know that it's plugged up except you and me."
    "Neve twirled the little bejeweled c-string about in her fingers deftly, an eager look etched on her face."
    n "C'mon. It'll look hot on you."
    $ hentai_scene(8)
    s "No stuff up my butt!"
    $ hentai_scene(10)
    n "Okay, okay then. Just thought it was a good idea. Get back to showing me your dance moves, then. You'll need to move a little faster!"
    $ hentai_scene(7)
    "Sabia frowned, before resuming her practice. This time she moved a little bit faster."
    "Shaking her ass side to side, she felt it bouncing around, her thighs jiggling."
    "Her tits pressed up against the pole, the metal slipping between them as she arched her back out even further."
    "Biting her lip as she tried to concentrate, she didn't see Neve smirked, sucking on the plug."
    "The Elf swirled her tongue around it, making it nice and wet as her eyes greedily drank in the sight of Sabia's toned ass."
    "Waiting for the perfect moment, Neve saw it and moved with the speed and grace that only an Elf can exhibit."
    $ hentai_scene(12)
    call shake ("h")
    "With delicate and skilled fingers, Neve slipped the plug up against Sabia's hole, and pushed it in, smirking at Sabia's surprised yelp."
    $ hentai_scene(13)
    "Neve chortled to herself, and leaned back in her seat."
    s "What the fuck, Neve!"
    n "Relax Sabia. It suits you."
    $ hentai_scene(14)
    "Ignoring Sabia's blustering, Neve ran her thumb over Sabia's now-covered slit, pressing gently while her index finger made sure every inch of the plug was inside."
    n "And besides, now you won't need to worry about the orcs seeing your pussy. If that was a problem."
    n "So you can dance properly now, right?"
    $ hentai_scene(15)
    "Neve pulled her hand away slowly, making sure to tease as she did so, running her fingers against the tiny slip of fabric."
    s "It would have been nice for you to at least warn me."
    "Neve smirked again, and licked her lips."
    n "I did. But you said no. So I took it into my own hands."
    n "Back to dancing, Sabia! I can't help if you don't dance, after all."
    $ hentai_scene(16)
    "Sabia grumbled, but still started to sway back and forth to a beat that only she heard."
    $ hentai_scene(17)
    "Putting a smile back on her face, her hips started to rock more."
    "The c-string with the plug on it both made her feel a little bit more confident, and at the same time more vulnerable."
    "She wasn't entirely sure how she felt about it - on one hand, she did like the idea that her piece of fabric wouldn't be flitting about and letting the entire tribe get a good look at her slit."
    "But on the other hand, she couldn't help but give a few little squeaks and moans as the plug pushed against her, inside, with every little movement jostling it about."
    "Still, her dancing got more evocative, and she started to use the pole more, remembering the spins and dances that the girls in her mother's establishments did."
    "Sabia gripped the pole tightly, and tried to spin around while holding her legs up in the air."
    "It wasn't nearly as easy as she thought it was going to be, but she still managed to do a full circle around the pole and-"
    $ hentai_scene(18)
    call shake ("h")
    s "NEVE!"
    $ hentai_scene(19)
    n "I couldn't help myself."
    n "It's just such a nice ass... and right there. And such a nice show you're putting on for me."
    $ hentai_scene(20)
    "Sabia looked back. Neve had an almost predatory smile on her face, and the elf showed no signs of taking her hand away."
    n "I'm just trying to help. You don't think there will be orcs coming up, trying to grope that ass?"
    $ hentai_scene(21)
    n "It's just preparation. You'll need to be ready for it - as well as able to dance."
    n "You do want my help right?"
    s "Well, yes, I do want your help, it's just that..."
    "Sabia wriggled about, rubbing her thighs together. She found that she was a little more excited than she had anticipated from doing this."
    "After her protests, she didn't want to say it - but the fabric over her pussy was probably a good idea, even though she felt it slowly getting wetter and wetter."
    n "It's just what? Shh, don't worry Sabia, just put that pretty smile back on your face, and start moving again."
    "Neve winked, and Sabia realized how much the elf was enjoying it. She could see it on the elf's flushed face, and the hard nipples poking out from Neve's top."
    $ hentai_scene(23)
    "Sabia resumed her show - after all, getting everyone excited really was the whole point of it."
    $ hentai_scene(24)
    call shake ("h")
    s "UGH! I thought you weren't going to do that anymore!"
    $ hentai_scene(25)
    n "I never said that."
    $ hentai_scene(27)
    n "Besides, I know you like it."
    "Neve smiled, and with her right thumb she reached over, rubbing at the now soaked piece of fabric."
    n "Look how wet it is."
    n "Are you sure this wasn't all just an act to get some more time with me, Sabia? You could've just asked, you know..."
    $ hentai_scene(28)
    "Sabia wanted to snap back, but she couldn't. Her chest thumped as her heart pounded."
    "Neve wasn't wrong, she could feel her arousal dripping down, slick against her thighs."
    "And Neve's warm fingers against her bared ass felt fantastic, kneading and groping her like she was a piece of meat."
    $ hentai_scene(29)
    n "But... if you prefer me to stop, I suppose I can."
    "With palpable reluctance, Neve slowly pulled her fingers away from Sabia's ass, dragging her nails along the reddened pale skin."
    "Sabia bit her lip as she squeezed her thighs together a bit tighter, trying to writhe without Neve noticing."
    s "Well... I mean, you don't have-"
    $ hentai_scene(33)
    call shake ("h")
    s "Mmmnnggf!"
    $ hentai_scene(25)
    n "Good, because I didn't intend to."
    s "I... you're... mmnfff!"
    "Sabia whimpered, as the harsh slap from both hands sent a jolt of pleasure surging through her. Enough to tip her over the edge."
    "Neve gave a little chuckle as she squeezed Sabia's ass harder, waiting for the orgasm to pass over Sabia."
    "Her grip on Sabia's ass made it all the more enjoyable for her, as she could feel every shudder, every little shiver and whimper and twitch that rocked Sabia's body."
    $ hentai_scene(27)
    n "Did you just cum?"
    $ hentai_scene(32)
    s "..."
    s "...No..."
    n "Sure."
    "Neve smirked, and they both knew Sabia was lying."
    n "Not bad, but you'll need a bit more practice."
    n "Let me know when you want to do so... though we'll have to focus on the dancing, and not on... well."
    "Neve's grin grew wider, and her teeth glimmered in the light as she left it unspoken."
    if gallery_workaround == True:
        jump gallery
    return


label ba_ashi_party_dom:
    play music sex1 fadeout 2.0 fadein 2.0
    $ hentai_scene(1,"ba_ashi_party_dom",dissolve)
    "Sabia stepped out on to the stage slowly. The ruckus of the orcs and the party, Jadk, Neve and Alioch, and everyone else who had come was still prominent."
    "But she knew it would die down."
    $ hentai_scene(2)
    "She took to the pole, wrapping her fingers about the cold metal, and started doing as her and Neve had practiced."
    $ hentai_scene(3)
    "She moved with a grace that she had thought she couldn't possess."
    "Every movement was intentional, decided. Sensual. A promise of what might be, of what could be."
    $ hentai_scene(4)
    "And barely anyone was paying attention."
    "Neve's grand introduction seemed to have had less of an impact than Sabia had hoped."
    "Sabia picked up the pace, leaning in closer against the pole so that she could do some twirls and spins about it."
    $ hentai_scene(6)
    "Every time she did, the plug inside her ass shifted about, pushing against her and she had to bite her lips to stop from moaning."
    "The chain that connected the pasties on her nipples bounced about, jingling with pretty light metallic taps as it clinked against the metal pole."
    $ hentai_scene(7)
    "Still, most of the guests didn't notice she was dancing. A few orcs saw her and couldn't keep their eyes off, though and she shot them a smile."
    "It was hard to do so, when Sabia's ass sunk down almost to the floor, below her high heels and her back arched ridiculously."
    "Neve noticed the lack of audience watching Sabia."
    $ hentai_scene(9)
    n "WHOOO! GIRLS!"
    "The half-drunken cry almost drowned out the rest of the chatter, and all eyes shot to the elf, before darting over to where Neve's gaze lay."
    "Sabia froze."
    $ hentai_scene(4)
    "The jewelry stopped moving against her skin and went silent."
    "It felt like the only light in the room was on her, and she suddenly realized just {i}how{/i} naked she was, and she felt every inch of bared skin."
    "As much as she hated to admit it, she was thankful for the small c-string. Even if it had a plug for her ass. And even if that plug was {i}up{/i} her ass right now."
    "The thought sent a little shiver through her spine, and she couldn't help wriggling her thighs together."
    $ hentai_scene(1)
    "She blinked, and came back to herself, realizing that she needed to dance, to perform."
    "Sabia once again started to sway, dancing and twirling, spinning. Every move that she and Neve had practiced."
    "The beads and bangles that were part of her outfit started to once again clink and jingle, a nice medley that matched her movement."
    "Out of the corner of her eye, Sabia saw one of the orcs grinning, clearly intending to get up on stage with her."
    $ hentai_scene(9)
    s "Please not being on to the stages!"
    "Her heart pounded as she called out, hoping that no one would recognize her voice. It was an accent she recalled from one of her mother's friends, years ago."
    "She was positive she was butchering it, but it worked well enough at the moment. Out of the corner of her eye she saw Neve snickering at it."
    $ hentai_scene(8)
    "The orc that had intended to jump on the stage blinked, surprised that the woman in the relief tent had said no. Whether he was feeling nice, or just the sheer shock of it, he moved a few steps back."
    "Deciding she had best pick it up a bit, Sabia started to shake her ass more, the thin veil dancing with her."
    $ hentai_scene(6)
    orc "Why no pussy!"
    orc2 "Show pussy!"
    orc "NO! SHOW TITS! TITS BETTER!"
    $ hentai_scene(1)
    "Sabia thought she'd show them wrong."
    "She started bouncing her ass with as much vigor as she could, jiggling the round bubble butt."
    $ hentai_scene(19)
    "{i}THWAP!{/i}"
    "Her hand whistled through the air as she spread her legs a bit, letting her jiggling, bouncing thighs join in on the show before her hand landed with a loud spank on her ass."
    orc2 "Ok! Ass best! Show more ass!"
    $ hentai_scene(21)
    "She managed to sneak a glance here and there every few moments, and could see more and more orcs drinking in the show, their excitement palpable from the tents in their pants."
    "Several more minutes passed as Sabia continued to dance, getting more into the rhythm. As she did, her heart beat faster from both the exertion, as well as the pumping desire that was bubbling up within her."
    $ hentai_scene(25)
    call shake ("h")
    orc "Dancer girl got good ass!"
    $ hentai_scene(26)
    s "YHEY!"
    $ hentai_scene(28)
    s "YOU ARE TO NOT TOUCHING ME!"
    $ hentai_scene(29)
    call shake ("h")
    orc2 "Haha, you right! Very good ass, very squishy! Fat juicy ass! No wonder it look so good while dancing!"
    $ hentai_scene(30)
    orc "Look better bouncing on big orc dick! When can orcs fuck you?"
    $ hentai_scene(31)
    s "Sabia is telling me zhat you orcs are not to touching me!"
    s "Please to be not touching!"
    $ hentai_scene(35)
    "The orcs ignored her, and continued their enjoyment of her ass."
    "Their fingers roamed down further, thumbs pawing heavily at her thighs, sliding along the slick, grool-wet flesh."
    $ hentai_scene(33)
    s "Mmmnn!"
    "A squeak of pleasure managed to get past Sabia's lips, the thick thumbs too close to her sensitive, tingling pussy."
    $ hentai_scene(36)
    n "Hey, clear off! She said no touching! You don't just get to touch high class women like that."
    "Neve barged through, pushing the orcs away."
    $ hentai_scene(37)
    s "Thanking you for very much-"
    $ hentai_scene(39)
    call shake ("h")
    orc2 "Hey! Why you get to slap ass, Neve?"
    $ hentai_scene(41)
    n "Benefits of helping Sabia out tonight."
    "Neve gave a sly wink to Sabia before moving on, dragging her hands across the sensitive, red skin. The orcs hadn't been gentle."
    $ hentai_scene(42)
    "Sabia took a breath, trying to steady the pounding blood in her ears, and went back to rolling her hips, bouncing her ass, and anything else she knew the orcs would love."
    orc1 "Human ass is great! More jiggling!"
    orc2 "More boobs! Show more boobs! Take top off!"
    $ hentai_scene(44)
    "Sabia was glad that she had such thick layers of makeup on, hiding her blush as the orcs called and jeered, telling her to strip, commenting on her body like she was meat."
    "It seemed that being forbidden to touch, or take what they wanted from a girl in the relief tents was something they weren't used to."
    "And it was something that was driving them wild."
    "Her forehead started to bead with sweat, and the c-string was as wet as it had been when Neve had first slipped the plug in."
    $ hentai_scene(48)
    orc "Why you no fuck?! Orcs can see human's wet pussy from here, it's all shiny!"
    orc "Come down here and suck some big green cock!"
    $ hentai_scene(46)
    s "Am being sorry, but not can being fuck! Dancing onlys!"
    "A holler of disappointment washed over the crowd, yet none of them left. They just watched all the more eagerly, and Sabia knew that the teasing was working."
    "They'd been so long without a human in the tents by now, and to have one... so provocatively dressed and dancing in front of them, and not being able to touch them."
    "It would be in their minds for days."
    $ hentai_scene(48)
    orc1 "When can fuck?!"
    orc2 "Have gold! Lots Lundils, give lots for fucking!"
    "Sabia pulled herself up against the pole, making sure that she twirled around so she was facing her audience."
    "Her barely-covered tits - she was thankful that the pasties hid her diamond hard nipples - swallowed the metal up as they enveloped the pole."
    "She gave a soft, throaty chuckle."
    $ hentai_scene(46)
    s "Am being sorry, but orcs not affording to golds for me!"
    s "Expensive muchs!"
    $ hentai_scene(45)
    "Giving one last twirl about the pole, holding herself from it with one hand and a leg wrapped around, she fluttered her eyelashes and smiled."
    $ hentai_scene(46)
    s "Am being thanking for such niceness! Please coming and see again!"
    "Sabia left the stage, much to the dismay of most of the orcish audience."
    scene bg black with dissolve
    s "Well... that went pretty well. I can't say it was my first plan to dance like a whore on stage."
    s "But it seemed to work well, and I can tell they're not used to performances like this, or being teased so much. Nor with such high quality women."
    s "If I say so myself."
    if gallery_workaround == True:
        jump gallery
    return


label ba_ashi_party_sub:
    play music sex1 fadeout 2.0 fadein 2.0
    $ hentai_scene(1,"ba_ashi_party_sub",dissolve)
    "Sabia stepped out on to the stage slowly. The ruckus of the orcs and the party, Jadk, Neve and Alioch, and everyone else who had come was still prominent."
    "But she knew it would die down."
    $ hentai_scene(2)
    "She took to the pole, wrapping her fingers about the cold metal, and started doing as her and Neve had practiced."
    $ hentai_scene(3)
    "She moved with a grace that she had thought she couldn't possess."
    "Every movement was intentional, decided. Sensual. A promise of what might be, of what could be."
    $ hentai_scene(4)
    "And barely anyone was paying attention."
    "Neve's grand introduction seemed to have had less of an impact than Sabia had hoped."
    "Sabia picked up the pace, leaning in closer against the pole so that she could do some twirls and spins about it."
    $ hentai_scene(6)
    "Every time she did, the plug inside her ass shifted about, pushing against her and she had to bite her lips to stop from moaning."
    "The chain that connected the pasties on her nipples bounced about, jingling with pretty light metallic taps as it clinked against the metal pole."
    $ hentai_scene(7)
    "Still, most of the guests didn't notice she was dancing. A few orcs saw her and couldn't keep their eyes off, though and she shot them a smile."
    "It was hard to do so, when Sabia's ass sunk down almost to the floor, below her high heels and her back arched ridiculously."
    "Neve noticed the lack of audience watching Sabia."
    $ hentai_scene(9)
    n "WHOOO! GIRLS!"
    "The half-drunken cry almost drowned out the rest of the chatter, and all eyes shot to the elf, before darting over to where Neve's gaze lay."
    "Sabia froze."
    $ hentai_scene(4)
    "The jewelry stopped moving against her skin and went silent."
    "It felt like the only light in the room was on her, and she suddenly realized just {i}how{/i} naked she was, and she felt every inch of bared skin."
    "As much as she hated to admit it, she was thankful for the small c-string. Even if it had a plug for her ass. And even if that plug was {i}up{/i} her ass right now."
    "The thought sent a little shiver through her spine, and she couldn't help wriggling her thighs together."
    $ hentai_scene(1)
    "She blinked, and came back to herself, realizing that she needed to dance, to perform."
    "Sabia once again started to sway, dancing and twirling, spinning. Every move that she and Neve had practiced."
    "The beads and bangles that were part of her outfit started to once again clink and jingle, a nice medley that matched her movement."
    "Out of the corner of her eye, Sabia saw one of the orcs grinning, clearly intending to get up on stage with her."
    $ hentai_scene(9)
    s "Please not being on to the stages!"
    "Her heart pounded as she called out, hoping that no one would recognize her voice. It was an accent she recalled from one of her mother's friends, years ago."
    "She was positive she was butchering it, but it worked well enough at the moment. Out of the corner of her eye she saw Neve snickering at it."
    $ hentai_scene(8)
    "The orc that had intended to jump on the stage blinked, surprised that the woman in the relief tent had said no. Whether he was feeling nice, or just the sheer shock of it, he moved a few steps back."
    "Deciding she had best pick it up a bit, Sabia started to shake her ass more, the thin veil dancing with her."
    $ hentai_scene(6)
    orc "Why no pussy!"
    orc2 "Show pussy!"
    orc "NO! SHOW TITS! TITS BETTER!"
    $ hentai_scene(1)
    "Sabia thought she'd show them wrong."
    "She started bouncing her ass with as much vigor as she could, jiggling the round bubble butt."
    $ hentai_scene(19)
    "{i}THWAP!{/i}"
    "Her hand whistled through the air as she spread her legs a bit, letting her jiggling, bouncing thighs join in on the show before her hand landed with a loud spank on her ass."
    orc2 "Ok! Ass best! Show more ass!"
    $ hentai_scene(21)
    "She managed to sneak a glance here and there every few moments, and could see more and more orcs drinking in the show, their excitement palpable from the tents in their pants."
    "Several more minutes passed as Sabia continued to dance, getting more into the rhythm. As she did, her heart beat faster from both the exertion, as well as the pumping desire that was bubbling up within her."
    $ hentai_scene(25)
    call shake ("h")
    orc "Dancer girl got good ass!"
    $ hentai_scene(26)
    s "Y...yhey... you am not should be touching!"
    $ hentai_scene(29)
    call shake ("h")
    orc2 "Shutup dancer slut!"
    $ hentai_scene(30)
    orc2 "Haha, you right! Very good ass, very squishy! Fat juicy ass! No wonder it look so good while dancing!"
    $ hentai_scene(33)
    orc "Look better bouncing on big orc dick! When can orcs fuck you?"
    $ hentai_scene(34)
    s "Sabia is telling me zhat you orcs are not should be touching... even fucking!"
    s "Please to be not touching!"
    $ hentai_scene(33)
    "The orcs ignored her, and continued their enjoyment of her ass."
    "Their fingers roamed down further, thumbs pawing heavily at her thighs, sliding along the slick, grool-wet flesh."
    s "Mmmnn!"
    orc "Yeah, but, it seems like you like us groping your little ass, don't you? Humans sure are sluts sometimes."
    "A squeak of pleasure managed to get past Sabia's lips, the thick thumbs too close to her sensitive, tingling pussy."
    "The rough callused fingers dug into her pliant ass, kneading the flesh as she tried to ignore and dance."
    $ hentai_scene(31)
    "It was making it very difficult - and especially more so when that damned plug was lodged up her ass."
    "Her eyes rolled back as her thought went to it and involuntarily she squeezed her muscles around the plug, gasping as her breath was caught in her throat."
    "She felt her pussy dripping more and more, the tiny c-string doing very little now to soak up her juices."
    $ hentai_scene(33)
    orc2 "Fancy girl is really like big orc hands!"
    orc "Yah! She probably love orc cock more."
    $ hentai_scene(34)
    s "N... no being cocked in stage, pleasing!"
    $ hentai_scene(36)
    "For a moment, she thought she might have ruined the entire show as the orcs pulled their hands away from her now-sore rear."
    $ hentai_scene(35)
    "Gingerly, Sabia grabbed at her ass while she danced, the beads and bangles continuing to make their own music to accompany her steps."
    "She gasped, her ass burning where her fingers touched - she could almost feel the heat coming from the red, abused ass."
    $ hentai_scene(39)
    call shake ("h")
    orc "Human ass is great! More jiggling!"
    $ hentai_scene(40)
    "Sabia's eyes went wide as the veil was ripped away, the fabric that kept it about her waist tearing easily under the strength of the orc."
    orc2 "YEAH! Show more ass!"
    $ hentai_scene(41)
    "Sabia was glad that she had such thick layers of makeup on, hiding her blush as the orcs slapped and ripped away the clothing."
    s "Please to not being clothing breaking!"
    s "Much expens-"
    $ hentai_scene(43)
    call shake ("h")
    s "NNG! UUGGggghhhh!"
    $ hentai_scene(44)
    "It seemed that being forbidden to touch, or take what they wanted from a girl in the relief tents was something they weren't used to."
    s "I am being glad that enjoying dancing! But, please-"
    $ hentai_scene(45)
    call shake ("h")
    "Another orc hand. Another slap. Another surge of pleasure that made her legs shake, her spine shiver, and her pussy tingle more than she wanted it to."
    s "Pleasing, ass is being very-"
    $ hentai_scene(48)
    call shake ("h")
    s "...hmmph..."
    $ hentai_scene(49)
    "Her forehead started to bead with sweat, and the c-string was as wet as it had been when Neve had first slipped the plug in."
    "Another orc had moved in, a crowd forming around Sabia. She could barely see the rest of the guests, and she felt orc fingers digging into her thighs and ass everywhere."
    $ hentai_scene(53)
    "She didn't hate it though. Her heart was pounding, thumping inside her chest faster and faster."
    "Her dancing had slowed now, and she found herself pushing herself back against the multitude of hands, rocking her hips up and down and helping them massage her ass and pussy."
    "They pawed at her, and before long she found that their fingers were running along the sopping, absolutely drenched c-string, pushing at her throbbing pussy lips."
    $ hentai_scene(55)
    orc "Why you try say no? All orcs can see how wet dancing slut is! Sabia pick good girl!"
    $ hentai_scene(54)
    s "No... cannot being fucking!"
    "It felt far too good, and Sabia knew that if she stuck around too long, she might end up needing to fuck an orc or two."
    $ hentai_scene(55)
    "And that would not do well at all. She couldn't let any of them know that she was the one dancing."
    orc "Maybe just suck cock then? Sabia said that ok or what?"
    $ hentai_scene(54)
    s "Am being sorry, but not can being fuck or suck! Dancing only! And finishing dancing!"
    $ hentai_scene(56)
    "A holler of disappointment washed over the close crowd, and they backed off a little bit. Some of the orcs in the back, not on the platform heard her and groaned their protest as well."
    "They'd been so long without a human in the tents by now, and to have one... so provocatively dressed and dancing in front of them, and pawing, groping at the girl only for her to reciprocate but say no fucking or sucking..."
    "It would be in their minds for days."
    $ hentai_scene(59)
    orc1 "When can fuck?!"
    orc2 "Have gold! Lots Lundils, give lots for fucking!"
    "Sabia pulled herself up against the pole, making sure that she twirled around so she was facing her audience."
    "She did her best to not let her voice be too breathy."
    "Her barely-covered tits - she was thankful that the pasties hid her diamond hard nipples - swallowed the metal up as they enveloped the pole."
    "The words were a little haggard and rough as she spoke, her voice wavering."
    $ hentai_scene(58)
    s "Am being sorry, but orcs not affording to golds for me!"
    s "Expensive much!"
    "Giving one last twirl about the pole, holding herself from it with one hand and a leg wrapped around, she fluttered her eyelashes and smiled."
    s "Am being thanking for such niceness! Please coming and see again!"
    "Sabia left the stage, much to the dismay of most of the orcish audience."
    scene bg black with dissolve
    s "Well... that went pretty well. I can't say it was my first plan to dance like a whore on stage."
    s "And it wasn't my plan to get felt up like a piece of meat."
    s "...and it wasn't my plan to enjoy it so fucking much. Ugh. I need to get this plug out..."
    if gallery_workaround == True:
        jump gallery
    return


label sabia_fluff_tooth:
    play music sex1 fadeout 2.0 fadein 2.0
    $ hentai_scene(2,"sabia_fluff_tooth",dissolve)
    "Sabia couldn't get through to the other side. In her haste to avoid the kennelmaster, she had tried to dive head first through the small hole, and got stuck."
    $ hentai_scene(3)
    s "...fuck!"
    $ hentai_scene(5)
    "Fluff Tooth kept yipping and snapping playfully at her feet."
    $ hentai_scene(3)
    s "No! Shh... Fluff Tooth stop it! Be {i}quiet{/i}!"
    "With every movement Sabia made in her attempt to get out, the wall and the wood support beams groaned in protest, creaking loudly."
    "The kennelmaster's footsteps kept pacing, and Sabia just hoped that she was far enough in the corner and the dark that he wouldn't see her ass and legs sticking out."
    s "Fluff Tooth, can you help push me through?"
    "Sabia wasn't sure if the hound was going to help or not, but it was worth a shot. Waiting until the footsteps sounded a bit farther away, she started wriggling, her ass shaking from side to side as she tried to squeeze through."
    "Fluff Tooth started panting louder, and gave an excited bark."
    s "No... shh! Please, be quiet! If I get caught you won't have any visitors, Fluff-"
    $ hentai_scene(10)
    call shake ("h")
    "Sabia yelped as Fluff Tooth jumped forward and his long, rough tongue pressed against her pussy through the flimsy orc rags."
    $ hentai_scene(11)
    "She barely managed to silence herself, biting down hard on her tongue and causing a tear to roll down her cheek from the pain."
    $ hentai_scene(12)
    "Embarrassment flushed over her as Fluff Tooth started licking more eagerly, his saliva soaking into the rag and making it cling to her ass and pussy."
    s "No.... boy, no! Get off! Help me out, not lick me there!"
    s "Bad boy! Bad Fluff Tooth!"
    "But the hound was enjoying himself too much, savoring Sabia's sweet taste and his licking became more insistent."
    s "Please... please stop! I hear the kennelmaster... coming back!"
    s "Hey... Fluff Tooth, NO!"
    $ hentai_scene(16)
    "Sabia had to stifle herself with a hand, covering her mouth until she managed to get her voice back under control."
    $ hentai_scene(17)
    "Surprisingly delicate for a hellhound, Fluff Tooth had taken the loincloth in his teeth, and yanked it off with a low growl."
    s "Bad boy!"
    s "I need to get out of here before the kennelmaster spots me..."
    "Trying to push herself out with her hands against the outside of the wall proved fruitless."
    $ hentai_scene(21)
    "Fluff Tooth was enjoying the show though, watching Sabia's wet pussy rocking back and forth. The scent was driving his canine senses wild, and it was only a few moments before he went back to licking Sabia's pussy."
    $ hentai_scene(22)
    "A groan of delight almost escaped Sabia's lips and she just barely managed to clench her jaw together, cutting it off before the kennelmaster could hear."
    "The tongue started to lap more eagerly. Sabia shivered. It was different from what she was used to. It was wider - much wider."
    "Instead of just running along her lips soft and gentle or playing lightly at the clit, Fluff Tooth's tongue did all of that. At once."
    "It pressed down hard, running along, the coarseness of it giving it an added sensation that Sabia didn't know how to express. Only that she had to admit to herself it felt good."
    "The wet slops and slurping sounds coming from her pussy burned in her ears, and although one part of her knew that it wasn't truly that loud, another part was certain the kennelmaster would hear."
    $ hentai_scene(23)
    s "Nmmng... Fluff Tooth... you... ugh, you have to stop!"
    $ hentai_scene(25)
    "But he clearly had no intention of stopping, instead moving a bit closer, his paws brushing against her stuck legs."
    "Sabia moaned again, desperately trying to silence herself as the tongue moved faster. It splayed out over both of her lips, and pushed hard enough that it teased her entrance and every nub on it seemed to caress her clit eagerly."
    $ hentai_scene(24)
    s "Stop... nng... you... need... oh! to... stop!"
    "Fluff Tooth's breath was like fire between her legs with how hot it was, embracing her thighs warmly."
    "Sabia felt the familiar sensation boiling up within her. Fluff Tooth's eager attention was bringing her closer and closer to an orgasm."
    "She knew that if he pulled away, her own arousal would be leaking from her slit."
    "Fluff Tooth did the opposite of pull away."
    $ hentai_scene(26)
    s "Hnng... fuck... Fluffff Toooooth! Fuck!"
    $ hentai_scene(27)
    call shake ("h")
    "Sabia whimpered, her thighs shaking as Fluff Tooth continued lapping eagerly through her orgasm, wave after wave of electric shocks surging through Sabia's body and mind."
    $ hentai_scene(28)
    "Her toes curled and she gasped as she came down from the high."
    $ hentai_scene(29)
    s "T-thank you Fluff Tooth, but now... now you need to help me get through! Before the kennelmaster comes back!"
    s "Fuck, I hope he doesn't see this... it would be bad enough with the embarrassment of being stuck in a wall and getting-"
    $ hentai_scene(32)
    call shake ("h")
    "Sabia realized with a start that Fluff Tooth was anything but done."
    $ hentai_scene(33)
    "He pounced, his thick, rock-hard cock already leaking. His haunches and powerful legs slapped up against Sabia's ass."
    "The feel of the soft fur against her skin was... different. And that, with the hot shaft pressing insistently against her pussy, she couldn't help but moan."
    "Louder than she wanted, the cry erupted from her lips as her eyes went wide with shock."
    s "...fuck, I hope the kennelmaster didn't hear that."
    "Sabia tried her best to stay silent as Fluff Tooth started thrusting wildly with some grunting, trying to get the tip of his cock to line up with Sabia's soaked pussy."
    s "Fluff Tooth! I'll tell Maply how bad you were if you don't stop this now!"
    "Her hope of invoking Maply for an escape was dashed as quickly as Fluff Tooth sunk his cock into her once he found her entrance."
    $ hentai_scene(38)
    call shake ("h")
    "It pierced her depths easily, the thinner leaking tip slipping in and helping spread her for the much wider base."
    $ hentai_scene(39)
    s "I... nngg! Fuck! Get off, Fluff Tooth!"
    "Sabia felt a few drops of hound saliva drip down onto her back, and Fluff Tooth eagerly started to use his powerful legs to drive his burning cock into Sabia."
    $ hentai_scene(40)
    "Even with the thick canine cock pumping into her, Sabia couldn't help but focus on the fur. It was like... velvet. Caressing her legs and ass with a gentle, oh-so soft touch."
    $ hentai_scene(41)
    "Sabia realized that Maply not being able to visit him was keeping him... backed up. Even still, she was surprised with how quiet he was. Some low panting and growls, nothing that the kennelmaster would suspect being out of the ordinary."
    $ hentai_scene(42)
    "His erratic pounding was an animal's desire, and Sabia knew that he wasn't trying to please her, he was focused on his own feelings."
    $ hentai_scene(43)
    "She was nothing but a bitch for him right now, his red rocket slamming in, the thick knot pressing against her pussy lips insistently, but not slipping in."
    $ hentai_scene(44)
    s "I don't... Fluff... ngg, you-can't-fit-that-knot-in-me!"
    "The words came out a tumble of gasps and moans. Her face darkened even further with a deep scarlet blush as her mind conjured up pictures of someone coming along and seeing a hellhound fucking her."
    $ hentai_scene(46)
    s "...nmmmghf!"
    $ hentai_scene(47)
    "Her body shook with a jolt at that thought, images of her tied to Fluff Tooth, his knot lodged inside her with her pussy sealed tight - no cum leaking out."
    "Cum and her own grool making the velvet-like fur sticky and matted, clinging to her skin as a torrent of burning hellhound seed filled her up, leaving another to knock her up if only she could carry hellhound puppies."
    $ hentai_scene(48)
    call shake ("h")
    s "No... no no no!"
    $ hentai_scene(49)
    s "Nnnggg!"
    "Fluff Tooth growled out as his knot slammed up against Sabia's pussy. It only half went in - but the poor hound was so desperate that it was enough for him to cum. A torrent of seed burst out from his red shaft, filling Sabia up quickly."
    "The burning heat from the knot, and how much pressure it was putting on her lips and clit tipped her over the edge and she came at the same time, to the thought of what people would think if she were carrying a litter of hellhound puppies."
    $ hentai_scene(50)
    "Her thighs shuddered again, and would have collapsed on the floor like jelly if it weren't for Fluff Tooth's paws and legs supporting her."
    "She didn't know if it were possible, but Sabia was sure her blush deepened further. Thankfully no one would need to know what happened - or worse, what her thoughts were as it happened."
    "The scent of hellhound cum managed to eke through to the other side as he stayed there, still within Sabia as his load dripped out. He whined pitifully, confused as to why he hadn't knotted and sealed up Sabia."
    $ hentai_scene(51)
    s "Hmph... see if you get any treats next time!"
    if gallery_workaround == True:
        jump gallery
    return


label rokgrid_contact_scene_dom:
    scene bg black with dissolve
    play music sex1 fadeout 2.0 fadein 2.0
    "Sabia quickly stripped out of her clothing, and moved down to her knees."
    "She could see the growing bulge in the soldier's leggings."
    $ hentai_scene(3,"rokgridcontact_dom",dissolve)
    s "Did I stutter?"
    s "Pants. Off. {i}Now.{/i}"
    s "Before I change my mind."
    $ hentai_scene(2)
    soldier "Uh... shit, yeah, yeah okay."
    soldier "Sorry..."
    "Sabia glared at him, waiting for him to undress."
    "His leggings dropped quickly, and he had to yank his underwear down past his throbbing shaft."
    "It bounced out from the confines, and he took a hesitant step towards Sabia."
    $ hentai_scene(12)
    s "Not bad. I guess. I've seen better."
    s "Maybe it won't be too un-enjoyable for me. Come on, then."
    $ hentai_scene(11)
    "He couldn't take his eyes off Sabia. They were glued to her breasts, and he walked over to her in half a haze."
    "His cock bounced with every step, and Sabia had to admit to herself it was nice. This would be fun."
    "But she wasn't going to tell him that."
    $ hentai_scene(22)
    s "Excuse me? Get your fucking hand off me."
    $ hentai_scene(9)
    soldier "I... uh, I thought we were going to..."
    $ hentai_scene(3)
    s "I didn't say you could touch my tits."
    s "If you're a good boy, maybe I'll let you. But not without me saying so."
    s "Do you understand?"
    $ hentai_scene(4)
    soldier "Uh... yes, I understand... sorry..."
    $ hentai_scene(12)
    s "Good."
    s "Move closer, then."
    $ hentai_scene(11)
    "Sabia watched him shift his weight from foot to foot with each command, each reprimand."
    "She knew she was in control."
    "She licked her lips, relishing the power. He was nothing but putty in her hands, and the thought was exhilarating."
    $ hentai_scene(30)
    s "Excited, are you?"
    soldier "Y... yes!"
    "Sabia made sure she was close enough that her warm breath hit the end of his shaft."
    $ hentai_scene(32)
    s "Mmm... is this what you want?"
    "She ran the tip of her index finger along the length of his shaft. Starting from the very base, right to his tip."
    "His cock throbbed under her touch, and she slowly moved her hand up, wrapping her fingers around the length. One at a time."
    $ hentai_scene(33)
    soldier "That's... yes, that's what I- ah fuck!"
    $ hentai_scene(34)
    "Sabia laughed, sliding her hand back and forth a bit faster."
    s "Are you going to cum already... I only just started!"
    $ hentai_scene(52)
    "The soldier's hips bucked slightly, as he tried to thrust into Sabia's rhythm."
    "Sabia smirked, and her pace slowed."
    $ hentai_scene(32)
    s "I asked you a question."
    $ hentai_scene(52)
    "Her fingers squeezed tighter about his shaft, and she gingerly moved them back and forth."
    "The tip of her finger circled about the underside of his length, just where the head ended, turning into shaft."
    soldier "Fuck... I... shit, yes, almost... you need to slow... slow down! You said you'd... you suck my cock! Not just... fuck!"
    "His barely managed to bite his words off as Sabia looked up at him with the corners of her mouth turned up."
    $ hentai_scene(32)
    s "I did. But I'm just not sure you're going to last that long..."
    s "I'll be nice though, since you're doing us a favor. You can touch my tits..."
    $ hentai_scene(34)
    s "If it's not going to make you cum."
    $ hentai_scene(35)
    "His hand flew down toward her breast, but halfway Sabia had already started pumping her hand once more."
    "He gasped, toes digging against the ground and his first attempt missed, instead grabbing onto Sabia's shoulder for balance."
    "It didn't take him more than a second for him to correct it, and his fingers pawed at Sabia's breast eagerly."
    soldier "Holy fuck... they're so... goo... good!"
    $ hentai_scene(37)
    s "Aren't you being such a nice boy, then?"
    $ hentai_scene(36)
    s "But it looks like you're too close to cumming."
    $ hentai_scene(35)
    "Sabia gave him a coy smirk, and pulled him closer to her by his cock."
    "He moved with her easily, the excitement on his face palpable - almost as evident as his pre-cum dripping cock."
    $ hentai_scene(38)
    "Directing him closer, Sabia opened her mouth slowly. Her tongue ran over her top lip as his throbbing length ached so close."
    soldier "Shit... don't... you gotta go slow..."
    $ hentai_scene(40)
    s "Hmm?"
    "Sabia pushed a pool of spit up to the front of her mouth, and let it bubble out of her bottom lip."
    $ hentai_scene(41)
    soldier "Fuck... fuck!"
    "The soldier grit his teeth, trying to not cum as Sabia's grip started to slide up and down his length once more."
    $ hentai_scene(42)
    "Her tongue had barely managed to slide down, past her lip before he grunted."
    soldier "I'm gonna... gonna cum in a second... fuck!"
    "Instead of using it to lap at the sensitive head, she kept it there as his hand reached back down."
    $ hentai_scene(43)
    "She could feel his desperation, his need to climax in his excited, uneven grip."
    "His fingers pawed haphazardly, trying to squeeze her nipple as he thrust his hips out, trying to push the tip of his cock into Sabia's mouth."
    $ hentai_scene(44)
    "Instead, she pulled back a little, and flicked her tongue side to side. Keeping it pressed up against the shaft, hard."
    $ hentai_scene(45)
    soldier "I can't... it's too... fuck!"
    $ hentai_scene(46)
    "He grunted with ragged breath, legs shaking and his fingers digging painfully into Sabia's breast."
    $ hentai_scene(47)
    "His cock swelled a little bigger, pulsing as his load erupted from the end. It splattered over Sabia's tongue and lips."
    "Some of it managed to find its way into her mouth, despite her efforts."
    soldier "Holy... fuck, Relona's tits!"
    "He hunched over, a few more spurts painting the rest of her chin white with the stuff."
    soldier "S... sorry!"
    $ hentai_scene(48)
    "He took a sheepish step back, his eyes heavy on Sabia's cum-drenched face, admiring his work."
    $ hentai_scene(49)
    s "What do you say?"
    soldier "But I didn't... you didn't even suck my cock!"
    s "So? You already came. If you can't manage to last past a handjob, I don't know what to say. But I know what YOU should be saying."
    "He glared down at her, his cock still half-hard, and a rope of cum still clinging to Sabia's chin."
    "The silhouette of Knorgath was visible even from where they were."
    soldier "...thank you."
    s "Good boy... see, that wasn't so hard, was it? Which I suppose was an issue for you... hmm."
    $ hentai_scene(50)
    s "So, no more debt owed. Everyone wins."
    $ hentai_scene(51)
    "The soldier nodded, half-reluctantly. Disappointment was etched on his face that he had not been able to hold back his orgasm, until at least he was in Sabia's mouth."
    if gallery_workaround == True:
        jump gallery
    return


label rokgrid_contact_scene_sub:
    scene bg black with dissolve
    play music sex1 fadeout 2.0 fadein 2.0
    "Sabia slowly undressed as the soldier watch her."
    "One foot out of her leggings... then the other, she stepped out of them entirely."
    "Grinning at Sabia, he moved over to her before she could take anything else off, and removed her top for her, before pushing her down to the ground with a forcefully placed hand-atop-head."
    $ hentai_scene(6,"rokgridcontact_sub",dissolve)
    s "Like this...?"
    $ hentai_scene(20)
    "With one hand rubbing at the bulge in his own leggings, he smirked down at Sabia. His open palm whipped through the air, and the harsh slap rang out as he brought his fingers back down to paw at Sabia's bared breast."
    soldier "Yeah... just like that."
    $ hentai_scene(22)
    s "That... that kinda hurts, don't be so rough, please..."
    $ hentai_scene(11)
    soldier "I'll be as rough as I think five hundred lundils is fucking worth."
    "He spat the words out in a frustrated anger, his vitriol was palpable."
    "Walking around Sabia, he inspected her from every angle, his hand never leaving the now-large bulge at his crotch."
    $ hentai_scene(28)
    soldier "What happened to that submissive attitude, anyway?"
    soldier "I grab your tits... and all of a sudden you're thinking twice about it? I can leave and you can report back to Rokgrid you failed, if you want."
    $ hentai_scene(29)
    "Every time Sabia tried to give a meek response, his fingers pinched her nipple harsh enough to make her yelp."
    $ hentai_scene(31)
    s "N... no! I... ugh! I'm sorry... I'll be... good..."
    $ hentai_scene(30)
    "She knew Knorgath would be back somewhere, watching as she was manhandled."
    "The thought sent a tingle through her body, and she squeezed her thighs together."
    $ hentai_scene(11)
    soldier "Yeah... you better."
    "With a smug look etched on his face, he took a step back to undress himself - he took no time to push his cock up against her face after doing so."
    $ hentai_scene(38)
    soldier "Here you go, slut. Get to work then. You owe me five hundred lundils."
    soldier "But I don't think you can give that much yourself... so you better get nice and ready to choke on it."
    $ hentai_scene(40)
    "Sabia grimaced. Even though the thought that Knorgath - and even anyone else who might come along - was able to watch was more exciting than she had imagined..."
    "She wasn't sure just how rough she wanted to be used. This was simply paying a debt to her."
    $ hentai_scene(42)
    "Frowning, Sabia nonetheless started to pump his cock with her hand. Just small strokes, while she wanted to be clear with him about what she was happy to do."
    s "There's a limit to how rough I'm going to let you be, it's not like-"
    $ hentai_scene(44)
    soldier "Like what?"
    $ hentai_scene(45)
    soldier "Heh, too excited for dick to be able to finish your sentence?"
    soldier "Or maybe you're just panting too heavily from me playing with your nipples."
    s "(Fuck... I don't want to admit it, but this is turning me on more than I thought it would...)"
    s "First off, I-"
    $ hentai_scene(48)
    "Sabia's word was cut off. The soldier grabbed her head once more, and maneuvered her so that the head of his cock slowly dragged over her face, right down to her lips."
    "Her pussy throbbed as the salty, musky scent of pre-cum hit her heavily."
    $ hentai_scene(49)
    "She looked up. Through her eyelashes, she saw the confident smile on his face."
    "Pre-cum was slowly eeking out of his shaft, painting her lips with the shining stuff."
    soldier "Do you not know how to suck cock? If I have to teach you, you're going to end up owing me more than five hundred lundils."
    $ hentai_scene(51)
    soldier "Use your tongue."
    "Sabia's face flushed with a red warmth every time he gave another command."
    "She obeyed, letting her tongue wrap around the ridge of his sensitive head, gliding along softly with an audible slurp."
    $ hentai_scene(52)
    soldier "Argh, fuck, yesss!"
    $ hentai_scene(53)
    soldier "That's fucking better."
    "He threw his head back and groaned with satisfaction as his girth forced Sabia's jaws wide, her lips tight around his length."
    $ hentai_scene(54)
    "Sabia whimpered, her air cut off as he forced himself another half an inch deeper."
    $ hentai_scene(55)
    soldier "Ugh, fucking... choke on it!"
    "His grip on her head tightened, and he held her there, his feet digging into the ground as he pushed his cock against the back of her throat."
    "Every time Sabia's body took an involuntary shuddering attempt to breathe, her throat convulsed and tightened around the inch he had managed to ram that far down."
    "She tapped on his leg almost desperately."
    $ hentai_scene(56)
    "Begrudgingly, he pulled out."
    "Sabia hacked violently, a wad of pre-cum and spit gushing out as air rushed in."
    $ hentai_scene(58)
    soldier "Don't give me that look, slut, I'll do what I want until I'm satisfied I've got my five hundred lundils worth."
    soldier "Whore."
    $ hentai_scene(59)
    "Sabia wanted to snap back at the retort. Instead, she gagged on cock, the head pushing down farther as more tears welled up."
    "He started thrusting, just a little. Not enough to make it easy to breathe, just enough for him to work his cock down a bit deeper every thrust."
    $ hentai_scene(60)
    "Sabia coughed violently as he pulled out again. Spit and pre-cum splattered over his cock head, dripping down."
    "Some of it caught in her nose, burning her nostrils and ensuring the only thing she could smell was cum."
    $ hentai_scene(61)
    "Her head swam as he plunged back down her throat, the tiny gasp of air she had managed to inhale doing little."
    "Breasts bounced wildly as he readjusted his feet, and starting thrusting into Sabia's mouth."
    "Every plunge was accompanied by a low growl of primal pleasure from him, his breaths getting shorter and shorter."
    "His grip tighter, and his grunts more ragged."
    "Sabia's head started to hurt from the lack of air, and all she could taste was his cock."
    "He said something... she didn't hear it over the sound of her blood pounding and wet throat squelching with every thrust in."
    $ hentai_scene(62)
    "Roaring out his climax, he buried himself as deep as he could."
    $ hentai_scene(63)
    "Cum hit the back of Sabia's throat as her eyes widen in shock, trying to yank back away from him as he held her tighter."
    "Some of it she swallowed reflexively, choking and gagging on it, while the rest gushed out of her lips, making her face a wet mess."
    "She tapped his leg weakly, desperate for air."
    s "Nnmm... nngg..."
    soldier "Wait until I'm... d-ugh, done!"
    "He grunted it out, jerking forward as his cock swelled and another rope of cum painted Sabia's throat white."
    $ hentai_scene(64)
    soldier "...there you go."
    "Sabia's eyes head still hurt, but at least her vision started to stop spinning as she breathed."
    $ hentai_scene(66)
    "He gave her a playful slap on her breasts, before wiping the tip of his cock off with her lips."
    soldier "I think that's about five hundred lundils worth."
    if gallery_workaround == True:
        jump gallery
    return


label veteran_orcs_help:
    play music sex1 fadeout 2.0 fadein 2.0
    scene bg black with dissolve
    "The group of orcs pushed Sabia into her own tent, wicked grins on their faces, and laughter on their lips."
    "Jerrak ripped Sabia's clothes off, ruining them entirely. If she wanted to use them again, she would have to see about getting it repaired."
    "With the same easy confidence, he picked Sabia up, and put her on top of her chest, pushing her knees apart and baring her slit to the group of smug orcs."
    $ hentai_scene(1,"orcveterans",dissolve)
    orc1 "At least humans are good at one thing."
    $ hentai_scene (2)
    orc2 "Sucking cock?"
    orc1 "Hmph. Well, it's certainly not assassinations, is it?"
    $ hentai_scene (3)
    s "If you're so good at it, then why didn't Tekrok get you guys to kill Knorgath, huh?"
    $ hentai_scene (4)
    orc1 "Maybe Tekrok knew you'd fail, and he wanted to see the purple-haired harlot get fucked and shown her proper place in the tribe..."
    orc1 "Or maybe he gave you more credit than you deserve. I won't make that mistake, seeing your pathetic attempt."
    $ hentai_scene (5)
    orc1 "Maybe if you were a mage, you might be useful. But... a human warrior. Hmph. Pathetic."
    "Jerrak's verbal assault was unrelenting, and he clearly did not intend to slow it down."
    $ hentai_scene (6)
    s "That's not fair. I've fought many of the orcs in the tribe and-"
    $ hentai_scene (9)
    orc1 "Stop talking, bitch."
    orc1 "No one cares what you have to say, unless it's pleading for more cock in your holes."
    $ hentai_scene (3)
    s "Like that's going to happen. I'll fulfill my part of the deal with Tekrok, but it doesn't mean I'm going to end up whimpering and pleading like a pathetic broken person."
    $ hentai_scene (12)
    "Jerrak grunted, moving behind Sabia and grabbing hold of her thighs. He picked her up with ease, and slid onto the chest, letting Sabia land down on his lap with a loud slap of skin against skin."
    $ hentai_scene (13)
    "Sabia gasped in spite of herself, Jerrak's cock rubbing against her ass cheeks, twitching in front of her pussy as his fingers dug into her thighs greedily."
    $ hentai_scene (15)
    orc1 "Good idea to offer yourself on your chest here... we'll fuck you, and maybe, if you're lucky, our loads of seed will seep down through the cracks, onto your clothes."
    orc1 "Then you can smell like the orc whore you want to be so badly."
    $ hentai_scene (14)
    s "Talking about it doesn't mean it's true."
    s "And besides, there's no way that's going to fit inside me, I-"
    $ hentai_scene (17)
    "Jerrak laughed at Sabia's protest, licking her cheek with his tongue, lapping noisily and ensuring his spit ran down the length of the muscle onto Sabia's skin."
    orc1 "Not going to fit? Hah! How many times have you said that since you've come to Grok og Dar, I wonder..."
    $ hentai_scene (18)
    "The other orcs couldn't help letting out loud, derisive guffaws of amusement as they stripped down, tossing their tunics and leggings aside."
    "Sabia grit her teeth at it, trying her best to ignore their judging looks."
    $ hentai_scene (19)
    "She'd just have to bear it for now. She wouldn't be in Grok og Dar forever."
    orc1 "Nice tits... too bad they won't get used by us today."
    $ hentai_scene (20)
    "One of the other orcs moved in closer, his engorged shaft twitching, a bead of pre-cum oozing down the length of it."
    $ hentai_scene (22)
    "She took hold of it, letting her fingers run along the head of the shaft, carrying the pre-cum with her grip."
    $ hentai_scene (23)
    orc1 "See? Not even told what to do, and you're already working hard, pumping that thick orc meat."
    $ hentai_scene (24)
    s "Because-"
    orc1 "Hmph. Don't worry about trying to justify it with useless words."
    orc1 "You won't be able to use words once we start abusing your holes, whore. Pathetic, cock-hungry human slut."
    $ hentai_scene (25)
    "Sabia's eyes flickered down to the girthy length she was sitting on, and her hand around the other cock slowed."
    "The hand pawing at her breast was the least on her mind with that threat in the air."
    $ hentai_scene (26)
    s "Hey, come on, that's not going to fit in my ass... why don't we just take it nice and easy?"
    s "I could wrap my breasts around it... or maybe I can use my lips to-"
    pause (0.3)
    $ hentai_scene (27)
    call shake ("h")
    s "Fuuuck!"
    $ hentai_scene (28)
    "Sabia's yelp was drowned out by rough laughter and she trailed off into a harsh groan as the orc's fingers tightened their grip on her thighs, and pulled her down hard against his thrust."
    $ hentai_scene (29)
    "Sabia's hand dropped from the cock she had been stroking, her thighs twitching and breath short."
    orc1 "What were you saying?"
    "The smugness in the orc's voice was heavy, and he started to rock his hips gently, his cock rubbing against Sabia's tiny entrance."
    $ hentai_scene (30)
    "He was big. Bigger than Sabia had realized... or maybe her ass was just too small."
    "It was stretching her out, and every tiny movement pushed against her now-throbbing ring, her ass squeezing tight against it."
    s "I... fuck... it's too big, you need... you need to pull out, pleaseeeee..."
    $ hentai_scene (31)
    "Her words peeled off into a high squeak."
    "Jerrak started to thrust into her ass, pulling out a few inches before driving himself back in, tongue lapping at her face in possessive glee."
    $ hentai_scene (33)
    "Sabia could feel the warmth of his breath on the side of his face, wafting past her nose as she inhaled erratically, his cock slowly breaking her ass in."
    "His pre-cum was oozing out of the tip, painting her insides with the stuff and making every thrust audible with a loud squelch that burned her ears red in embarrassment."
    orc1 "Are you already too overwhelmed by just one orc cock? There's one to your left. Don't forget about that one."
    $ hentai_scene (34)
    "Whimpering, Sabia did as she was told. Her arm trembled as she brought it up, before latching on to the cock and starting to pump it dutifully once more."
    $ hentai_scene (35)
    "Sabia's eyes widened once more in shock and a little bit of fright, and her hand froze its movement."
    "Another cock slapped down, this time on her pussy."
    $ hentai_scene (36)
    s "Whoa... hng... okay! No... no way!"
    $ hentai_scene (37)
    "Her answer was a wicked grin of sharp teeth, the force of Jerrak's pounding was enough to make the cock rub against her slit, pushing her lips apart."
    "Sabia couldn't help a rough, drawn out intake of breath, haggard and uneven. The orcs didn't miss it."
    $ hentai_scene (36)
    s "C-C'mon... there's no way you can put... put both inside me..."
    s "I'll do... nng... something else!"
    "She got no answer as the orc moved back a little, pressing the tip of his cock against her wet slit."
    pause (0.3)
    $ hentai_scene (39)
    call shake ("h")
    s "Ugghnnnnngggg!"
    $ hentai_scene (40)
    "They both pushed in simultaneously. Sabia grunted, her whole body jerking from the force, her skin tingling as she broke out in a flush."
    "She had never felt so full, both of the throbbing, hot cocks pushing against her walls, straining her entrances, pushing against each other inside her."
    "Another low ragged gasp was ripped from her chest as her tongue lolled out, drops of spit falling down onto the orc's hand squeezing her breast."
    orc1 "Don't forget that one in your hand again. Whore. If you can even hear me through your cock-drunk haze."
    s "Whha... hng?"
    "Sabia half nodded, her eyelids fluttering."
    $ hentai_scene (41)
    s "Ng... ugh!"
    "(Don't forget... hand...)"
    "The words bounced in the back of her mind, and with a constant low moan rumbling in her throat, Sabia started to pump the cock with her hand again."
    "Not content any longer to simply fill Sabia's holes, Jerrak and the other orc started to push in and out. Eager to both unload deep inside Sabia, as well as prove Jerrak's words."
    $ hentai_scene (42)
    "Jerrak grunted in glee, licking Sabia's face again to no reaction, other than a whimpering mewl as she was jostled back and forth between both thrusting cocks."
    "Her bouncing breasts proved enough of a distraction for the hand on her head to be lifted, roaming down and pawing at them, the fingers squeezing harshly."
    s "Ggnnn... hmmmngg..."
    "Sabia's moans filled the tent, saliva flying off her hanging tongue each time enough drops of it gathered there."
    $ hentai_scene (43)
    "Jerrak and the eager orc in her pussy roared, burying their lengths deep in Sabia. She yelped as they forced their way in, she would have sworn that they were pushing her insides out of the way to accommodate."
    $ hentai_scene (44)
    "The complete and utter fullness tipped Sabia over, and her whole body shuddered, a rolling wave of pleasure hitting her hard. Her hand kept pumping, but her fingers tightened, squeezing."
    "The third orc grunted, his balls tensing and the tip of his shaft shooting several heavy ropes of viscous orc seed over the side of Sabia's face, some of it landing in her open mouth and her tongue."
    "But the ones in either of holes did not stop. They kept slowly thrusting, eager to milk every drop of cum. Every push and pull made a loud wet squelch as it oozed and bubbled out of her throbbing ass and hot pussy."
    "Sabia just whimpered, in the throes of her orgasm, unable to form a word even if she wanted to."
    scene bg black with dissolve
    "Jerrak picked Sabia up after they finished, and dumped her on the chest. He watched with a wicked grin as the two monstrous loads of their cum oozed down through the cracks."
    "When he was pleased enough that her belongings would smell like cum for days, he pushed her to the ground."
    "Sabia grunted as her sensitive nipples brushed against the coarse surface."
    "Jerrak hooked his hands around Sabia's thighs, and yanked her back, and then her ass up, pushing her head down with his foot."
    s "Please... please... no... no more... you were- ahn!"
    "Her ass rippled with a harsh slap, a large red mark quickly appearing."
    orc1 "We're not done yet, whore."
    if gallery_workaround == True:
        jump gallery
    return


label drunk_orcs_help:
    play music sex1 fadeout 2.0 fadein 2.0
    scene bg black with dissolve
    $ hentai_scene(1,"orcdrunks",dissolve)
    "The cool air managed to rustle through the tent, Sabia's bared nipples hardening despite herself."
    $ hentai_scene(2)
    orc1 "Heh, look, the dumb slut is already getting all excited for it!"
    orc2 "Of course she is. She couldn't do a simple job for Tekrok, she probably was too busy thinking about orc cock!"
    orc1 "Yeah, you are probably right, heh!"
    $ hentai_scene(3)
    s "You guys know I can hear you right?"
    $ hentai_scene(4)
    orc3 "Well that's good. Maybe this time you can fucking follow a direction, huh?"
    $ hentai_scene(11)
    "Sabia swallowed her pride, and nodded along."
    $ hentai_scene(6)
    s "Well, what do you want to do then?"
    $ hentai_scene(12)
    "One of the orcs grinned as Sabia changed her tune, his hand reaching out and taking a commanding heft of one of her breasts."
    $ hentai_scene(13)
    orc2 "Heh, that didn't take much! Fuck, me glad that Sabia failed at task. Now we get to fuck her!"
    "Sabia did her best to grin and bear it as another large orc hand reached over, mauling at her like he saw her as nothing more than a toy."
    orc3 "Not sure why Tekrok thought Sabia would be able to do it. Thought it was sneaky."
    $ hentai_scene(15)
    s "Well... I... mn, it was harder than I... fuck! Not so hard!"
    "Sabia groaned, her nipples twinging in a sharp jolt of pain as one of the orcs pinched them harshly, between thumb and forefinger."
    s "Is this... how you fuck? No wonder you needed someone designated to you..."
    $ hentai_scene(13)
    orc3 "Yeah, but, if me and others can do job, why Tekrok ask Sabia?"
    $ hentai_scene(16)
    "The first orc pushed his way in, knocking the darker skinned one aside and sidled up close against Sabia's back."
    $ hentai_scene(17)
    orc1 "Because me bet she wanted to be railed by orc cock! She probably begged and begged and begged Tekrok."
    orc1 "Human sluts always like parties... that's why Sabia held one in the tents, me reckon."
    $ hentai_scene(18)
    s "That's not... fuck! Please... not so hard on my tits!"
    $ hentai_scene(19)
    "His fingers squeezed tighter, Sabia's breast spilling between his grip as his fingertips dragged slowly across her soft flesh, leaving marks behind."
    "Sabia shuddered as his tongue ran slowly along the side of her face, leaving a trail of saliva behind."
    orc1 "Me bet it is... you wanted to party when you saw me and my friends drinking... wanted to join in."
    orc1 "But too shy to ask, isn't that right?"
    $ hentai_scene(20)
    "Sabia grimaced, a surge of anger rising through her as the orcs kept laughing at her."
    "Her free breast didn't go untended for long, the other orc coming in with glee. His fingers pawed at her, his cock growing noticeable in his leggings."
    "Sabia could feel the one behind her, his shaft was almost rock hard, and he kept grinding against her ass, his breath on the nape of her neck."
    $ hentai_scene(21)
    "If they were going to insult her, Sabia was going to play their game."
    s "Yeah, you're right. We do like to party."
    s "Unfortunately we only like to party with guys that have cocks big enough to use, and know how to satisfy. Not stupid brutes."
    $ hentai_scene(22)
    "Sabia looked toward the orc in front of her, his grip on her breast loosening a little at her words."
    $ hentai_scene(23)
    orc1 "Stupid brutes? Me will show you how a stupid brute deals with an annoying slut that won't stop talking, then."
    "The atmosphere in the room had changed rapidly, and the main orc's jovial insulting tone had changed."
    $ hentai_scene(24)
    "The feel of his spit running down her chin was in the back of her mind as she watched him walk around, moving close to her, but just far enough that they didn't touch."
    $ hentai_scene(25)
    "With his leggings dropped, his cock was bared, throbbing with readiness. Several veins bulged, engorged with blood."
    orc1 "Hand on it. Now."
    $ hentai_scene(26)
    "Sabia rolled her eyes, and wrapped her hand around the cock."
    s "You got worked up easily... did I hit too close to home?"
    orc1 "Just do your job. Or me tell Tekrok you didn't."
    $ hentai_scene(27)
    "Sabia started to pump her hand along the cock. It was larger than she would have wanted to give him credit for."
    $ hentai_scene(28)
    "The other two orcs had started drinking, had already downed a few mugs of ale."
    orc2 "Hey, she slowed down!"
    orc3 "Probably just wants it in her mouth already... she stopped complaining when you said you were gonna fuck her mouth... haha"
    $ hentai_scene(26)
    s "That's not why at all! It's because this brute shoved his cock right in front of my face and-"
    $ hentai_scene(29)
    orc1 "This is right in front of your face, not before! Heh."
    $ hentai_scene(31)
    "The weight of the cock slamming against her eye and cheek pushed her back a few inches, and the musky scent was overpowering."
    $ hentai_scene(32)
    s "Ugh, can you get that thing off my eye? Just let me finish jerking you off. I'm sure you'll be done in a few seconds."
    $ hentai_scene(34)
    "The orc snorted in laughter, moving his hips and letting his shaft run down Sabia's face until the head of his cock pushed against her lips."
    "Sabia furrowed her brow, but let her lips part."
    orc1 "See? You shouldn't talk, heh. You're more pleasant to be around when there's a cock in your mouth."
    orc1 "Use your tongue... go on."
    $ hentai_scene(35)
    "The other orcs quaffed some more ale, raucously laughing as Sabia followed the instructions."
    "Sabia let her tongue swirl about the underside of the orc's cock lazily. The taste filled her mouth quickly, helped along by the oozing pre-cum from the tip."
    orc1 "Stop looking over there, you can have a turn with them later... me first though, heh..."
    pause (0.3)
    $ hentai_scene(38)
    call shake ("h")
    "Sabia had no time to react as he rammed his cock into Sabia's mouth."
    $ hentai_scene(39)
    "She tried to pull away, but his hand kept her head steady, the force of his thrust enough to part her lips around his girth, pushing her tongue down flat."
    "Sabia gagged on it, the head pushing against the back of her throat. Her lips sputtered, spit and pre-cum splattering down the half of cock that still wasn't lodged inside her throat."
    "More of the mixture dripped down her chin."
    $ hentai_scene(40)
    orc1 "Heh, got nothing to say now?"
    $ hentai_scene(41)
    s "Mmnnfg!"
    orc1 "Fuck!"
    "Sabia groaned again. Her throat rumbled, vibrating against the throbbing intruder, the hot warmth of his pre-cum slowly running down inside her."
    "Though the other orcs were cheering and laughing at her treatment, their sounds were dulled to her."
    "She could only hear the sound of the orc's meat, throbbing inside her."
    "The sound of her heart, pumping loudly."
    $ hentai_scene(42)
    "Sabia whimpered as more of the orc's seed dribbled down into her belly, the sounds fading away as the burning of her chest took their place."
    "Her head started to swim as she struggled to breathe."
    "Tears ran down her cheeks, her nostrils flaring and her breasts bouncing about as her chest heaved."
    "With every breath she tried to draw, the orc's monstrous shaft was in the way."
    $ hentai_scene (43)
    "The orc groaned out in delight, enjoying the tightness convulsing about his cock as Sabia struggled."
    orc1 "Heh... look... look at the bitch trying to breathe!"
    "Sabia's tongue pushed against her bottom lip, straining, before managing to sneak through - she needed air. The edges of her vision were starting to turn white."
    "His shaft was too thick, and her attempt at making space for air failed, her tongue pushed tight against her lips from the pressure of his meat."
    $ hentai_scene (44)
    orc3 "Haha, dumb slut choking on cock!"
    "Sabia felt their hands on her breasts, their greedy, callused fingers pawing almost painfully at them."
    "But it was... in the background."
    "Her mind reeled, desperate for air as more tears painted her cheeks."
    $ hentai_scene (45)
    "Beads of sweat rolled down her body, her vision nothing but a blurred mess of unfocused green orc cock."
    "Her chest burned with need, her head light."
    "The orc smirked to himself, and slowly, so slowly, started to pull his cock out from Sabia's mouth."
    "Sabia's eyelids fluttering as she teetered on the brink of consciousness made the orc want to push back in, and make the bitch pass out."
    $ hentai_scene (46)
    orc1 "You're lucky me such nice friend, and want to let everyone else use you too... instead of just me."
    "Sabia's mind whirled with a fresh intake of air. Her whole body heaved as she sucked in as much as she could."
    "Her nostrils stung, pre-cum and spit flying in as well, the orc's cock still rubbing against her lips - pre-cum was the only thing she could taste."
    $ hentai_scene (47)
    orc3 "Me thought you were gonna let her pass out!"
    orc1 "Nah... me want her to be awake to swallow every drop of cum."
    orc1 "So she knows what she is..."
    $ hentai_scene (48)
    "Sabia wanted to shoot back a retort, but she was barely hanging on to consciousness, a desperate flurry of breaths rocking through her body as her vision started to righten."
    $ hentai_scene (49)
    orc1 "A little cock swallowing slut for Tekrok to use as a reward... heh."
    $ hentai_scene (50)
    "Sabia glowered at him as he pushed back in."
    "His grip on Sabia's head tightened, and he pushed her forward, driving another inch of cock into Sabia's throat."
    $ hentai_scene (51)
    "He kept her there as her eyes continued to run and her nipples ached, her chest starting to burn once again."
    s "Nn.. mng!"
    $ hentai_scene (52)
    orc1 "There... have a breath before me cum."
    "Sabia hated that doing so made her feel like she was following his command."
    $ hentai_scene (53)
    "Tears flew off her face, falling to the ground as he rammed back in, her tits and hair jostling about wildly."
    pause (0.3)
    $ hentai_scene (54)
    call shake ("h")
    "His fingertips dug harshly into her scalp as he roared."
    $ hentai_scene (55)
    "The orc's cock pulsed, before erupting inside Sabia's throat."
    "The first few spurts gushed down into her belly, the warmth spreading out from her center."
    "But it kept coming, his heavy balls tense against her arm."
    "It bubbled up, breaking through the seal of her lips and his shaft."
    "A torrent of thick seed that clung to her chin and cheeks. Sabia grunted, trying to catch a breath."
    "Some of the cum gushed up her nose, stinging painfully and she gagged, snorting. A wad of the stuff oozed down into her throat from her nose as the tears mixed with the popping bubbles of cum."
    orc1 "Heh. That's better. Me hope you had fun... cause you aren't done yet."
    "His lips turned up in a wicked smile as he rubbed his cock over Sabia's face, spreading his seed around, some of it dripping down onto her breasts."
    $ hentai_scene (57)
    "Sabia choked some more, trying to clear her nose and throat of the heavy load of orc seed."
    $ hentai_scene (58)
    s "I... I need a break before I can do any... anymore..."
    $ hentai_scene (59)
    "The last orc howled in disappointment at Sabia's words, moving in close."
    orc2 "What?! No break. Me wanna cum now!"
    scene bg black with dissolve
    "The other two orcs used Sabia's throat as brutally as the first, and by the end of it, she was almost breathing cum."
    "Her belly was sloshing with several loads of orc seed, and her face was a mess. When they finally let her leave the tent, she stumbled a few steps away, to clean herself."
    if gallery_workaround == True:
        jump gallery
    return


label sober_orcs_help:
    play music sex1 fadeout 2.0 fadein 2.0
    scene bg black with dissolve
    $ hentai_scene(11,"orcsober",dissolve)
    "Entering her tent, she quickly stripped, the orcs followed suit, grinning at each other."
    $ hentai_scene(10)
    "Sabia glanced around the room."
    "The orcs were already rock hard. They had clearly been excited for this."
    "Sabia sighed silently as the first one walked over."
    $ hentai_scene(12)
    orc2 "So? What you gonna do? Me not gonna help for free."
    $ hentai_scene(13)
    orc1 "Yeah... not free."
    "Another moved in. Both of them took a few steps closer so that their twitching cocks kept brushing against Sabia."
    "They seemed far less aggressive than the other groups of Tekrok's orcs, and Sabia hoped she could get away with something easier."
    $ hentai_scene(15)
    s "I was gonna give you boys a nice handjob... stroke those big, throbbing shafts off."
    "She did her best attempt at a sultry, lustful voice."
    $ hentai_scene(17)
    "It seemed to work. At least, in exciting them."
    "They look at each other, grins growing wider, one of them reaching down with his hand."
    "He let it roam over Sabia's flesh, slowly as the rough callused grip dragged over her soft skin."
    $ hentai_scene(18)
    s "Hey, don't squeeze too hard. It can hurt."
    $ hentai_scene(19)
    orc1 "Huh, really?"
    orc1 "What about this?"
    "The sound of a slap rang about the small area as his hand whipped through the air, landing on Sabia's breast just a little harder than she would have preferred."
    s "Ow! Yes! That hurts!"
    $ hentai_scene(20)
    "Amused by her reaction, the other orc's fingers pawed more harshly, pinching Sabia's nipple with his fingers."
    "Sabia grunted, a spasm of pained pleasure jolting through her body."
    s "Fuck! Can you not?"
    orc2 "Yeah, yeah... get to work. You want job done or not?"
    $ hentai_scene(21)
    "He gave her breast another quick slap before moving up, fingers digging into Sabia's hair."
    $ hentai_scene(22)
    "Obeying the command, Sabia wrapped her fingers around his shaft, much to his satisfaction. He let out a long low groan as the warmth of her fingers enveloped his length."
    $ hentai_scene(23)
    orc1 "What, you think you just do one cock at a time?"
    "The other hulking frame of orc snorted his annoyance, moving his hand away and jutting his hips out, pushing his meat closer to Sabia."
    $ hentai_scene(24)
    "Sabia wriggled about as she complied. With both arms up, and angled as they were, she felt her tits stick out a bit farther."
    $ hentai_scene(25)
    s "Let's help you boys cum, then..."
    "Sabia decided to forgo any foreplay, and instead spat a wad of saliva on each length, and started stroking them quickly."
    "She kept her fingers tight enough, making sure that she kept gliding her fingers over the sensitive ridge of the head."
    $ hentai_scene(26)
    s "Ow! Really?!"
    $ hentai_scene(27)
    orc2 "Yeah, really. Don't stop jerking, Sabia! Me know you like it, haha!"
    "The other orc found it as funny as his friend, laughing and slapping Sabia's breast as well."
    $ hentai_scene(29)
    s "So... you'll help me out after you cum, right?"
    $ hentai_scene(26)
    orc1 "Maybe... not know yet. Sabia not made me cum."
    $ hentai_scene(29)
    s "Well... I'll do my best job to make you boys cum, then!"
    "Her arms started to burn a little, her pace quickening. Faster they blew, the faster she could get the group of orcs out of her tent."
    $ hentai_scene(30)
    orc2 "Fuck! Sabia go too fast... ugh! Fuuuuck!"
    $ hentai_scene(31)
    orc1 "Arrgh!"
    "The one on her left grunted, gripping her head tight as his cock pulsed noticeable in her grip, erupting first. A giant rope of the stuff hit her right in the side of the cheek."
    "The second followed an instant later, more landing on her lips, cheeks and even in her mouth as she turned away from the first orc assault."
    $ hentai_scene(32)
    s "Ugh... in my hair?!"
    "Sabia's pumping slowed and stopped, but the orcs thrust forward, using her still-present hold as an aid to push out another few spurts."
    $ hentai_scene(33)
    s "You could have at least warned me before cumming."
    $ hentai_scene(34)
    "They didn't answer her. Not in words, at any rate."
    "Sabia's tits jiggled from the weight of their cocks as they gave her a few slaps with them, dragging the tips along and leaving a trail of cum behind."
    s "Alright... who's next, then?"
    "At least it seemed-"
    $ hentai_scene(35)
    "Sabia's eyes shot wide and her mouth shut, jaws closing. Some of the cum lingering on her lips was squished, forced into her mouth."
    $ hentai_scene(36)
    s "No, come on... it's just handjobs I'm giving. There's too many of you for anything else..."
    "Not really incorrect, Sabia realized. She looked around and there was at least four orcs waiting. She swore there had been fewer at the start..."
    $ hentai_scene(37)
    orc3 "But me wanna fuck you!"
    $ hentai_scene(38)
    orc3 "Sabia like it. Trust me!"
    s "Look, I'm okay to jerk you guys off, but if you think I'm going to let you-"
    pause (0.3)
    $ hentai_scene(39)
    call shake ("h")
    orc3 "-fuck your pussy?"
    $ hentai_scene(40)
    "Sabia groaned. She probably should have expected one of Tekrok's orcs to just thrust in, despite what she said."
    $ hentai_scene(41)
    "The heat of his balls was palpable as they pushed up against her inner thighs."
    s "Fuck... can you... can you not? It's too big for it to be comfortable, and-"
    $ hentai_scene(42)
    orc3 "Stop complain! Me done soon. Sabia very tight, not last long!"
    $ hentai_scene(43)
    s "Nnnggg!"
    "Sabia had wanted to say 'exactly' - agreeing with her being too tight."
    $ hentai_scene(44)
    "Her fingers curled, tightening about the edge of the chest as she gripped, every thrust from the orc slamming her back another inch."
    "The whole shaft was buried with each push, his balls slapping up against Sabia's wet flesh. She didn't even see the other orc pushing his length up against her side."
    $ hentai_scene(45)
    orc4 "Hey! Stop fucking her. Sabia not see me while you fuck her."
    "Reluctantly, he slowed his movements, letting just the tip of his cock rest inside Sabia, her lips tight around his shaft."
    s "H... huh?"
    $ hentai_scene(46)
    orc4 "Here, Sabia..."
    "He guided her hand to his rod, and she grabbed hold of it, starting to stroke it almost eagerly."
    $ hentai_scene(47)
    s "Huuuuhnngg!"
    "The thrusting had turned harsher, and more erratic. He was using Sabia as a means to get off, desperately rutting into her almost like an animal."
    "The more brutal his haphazard pounding of Sabia, the more she moaned, the tighter her fingers wrapped around the shaft in their grip, pre-cum making them slide up and down."
    $ hentai_scene(48)
    "His cock pushed deep, swelling up as roared."
    $ hentai_scene(49)
    "The feeling of warmth as his cum emptied into her, spread within her depths. The sensation rolled over her, and she drew a slow, shuddering breath."
    "She twisted her neck as another several ropes of fresh, warm stuff landed on her face, the now half-dried cum pulling against her skin."
    "Some of the cum still clinging to her face was sucked in with her uneven breath, hitting the back of her throat and she choked on it, gagging."
    orc3 "Fuck... Sabia so tight, me already cum..."
    orc4 "Me too! Fuck... me wanted to wait for turn in pussy..."
    $ hentai_scene(50)
    "Sabia huffed, breathing deeply as cum ran down the cock in her hand, oozing farther, running along her fingers."
    "One of the other orcs grunted, shoving the one still lodged balls deep inside her out of the way."
    "His length slipped out of her with a loud 'shluck', and the next orc slapped his own down on top of her, cum spattering over her thighs."
    $ hentai_scene(51)
    s "Come on... my pussy is throbbing from how rough he was, can't we just do some more handjobs, please...?"
    $ hentai_scene(52)
    orc5 "Hah, sure! Here you go Sabia."
    scene bg black with dissolve
    "Sabia's pleas to just be allowed to jerk them off were only half listened to. They all let her use her hands..."
    "But they still all fucked her pussy, leaving her a dripping, cum-soaked mess by the time they had finished."
    "Sabia fell to the floor, breathing heavily, cum bubbling from her nostrils, as they left to set up for the required help."
    if gallery_workaround == True:
        jump gallery
    return


label tekrok_orcs_final:
    play music sex1 fadeout 2.0 fadein 2.0
    scene bg black with dissolve
    "She was shoved forward, Tekrok's large presence loomed behind her."
    "His hands were all over her, ripping her clothes off, and pushing her down onto her knees."
    $ hentai_scene(8,"orcsfinal",dissolve)
    s "Come on... this wasn't part of the deal! I've already paid all of you..."
    orc1 "Hah, yes! Now you pay again!"
    $ hentai_scene(12)
    "They undressed about as quickly as was capable for an orc, their cocks already hard."
    "Why wouldn't they be? Sabia thought. They already knew how much they enjoyed her..."
    $ hentai_scene(13)
    "More orcs moved over. She felt a sense of trepidation, realizing that it was not just going to be two or three orcs."
    "Another cock pushed up against her pussy as one of the orcs sidled up behind her, helping to part her legs as he rubbed his shaft between her ass cheeks."
    $ hentai_scene(16)
    orc2 "Hope Sabia ready for a long night..."
    scene bg black with dissolve
    pause (0.01)
    $ hentai_scene(17,effect=dissolve)
    "Sabia lost track of the hours as the night passed, and she was passed around from orc, to orc, and back again."
    $ hentai_scene(18)
    "She was sure that each orc had made sure to cum in or on her at least twice."
    "Her body was slick with sweat, and coated in orc seed. Some of it still wet, and more of it dry, pulling tautly on her skin as she was jostled about."
    "About an hour ago her ass had stopped hurting... instead just the odd feeling of being full with every orc who pushed in, and her pussy was almost numb."
    "She knew her breasts were going to be a dark blue in the morning, along with her thighs, ass and other parts where they had groped and slapped her."
    "Several times she had passed out... only to wake up with a fresh load of cum gushing down into her belly, balls up against her chin and her lungs burning."
    "...and they looked like they had no intention to stop."
    "Sabia looked over at Tekrok weakly... he only smirked, watching her being used over and over."
    if gallery_workaround == True:
        jump gallery
    return


label kira_bandits_badend:
    play music sex2 fadeout 2.0 fadein 2.0
    scene bg black with dissolve
    $ hentai_scene(1,"kira_badend",dissolve)
    kira "Come, pet."
    $ hentai_scene(2)
    "Sabia whimpered, her voice muffled against the gag."
    "Kira bent down, wrapping her fingers around the leash. She yanked Sabia over, hard."
    pause(0.3)
    $ hentai_scene(3)
    call shake ("h")
    "Sabia did her best to crawl over, the collar pressing up harshly against the nape of her neck."
    "Her bound arms did nothing to help, nor did the toys lodged in both of her holes. Every movement, she felt them pushing against her, pushing against each other inside her."
    $ hentai_scene(5)
    kira "Good girl..."
    kira "You look... so pretty. Don't you, pet? With all those... wonderful marks on your ass. On your breasts. Like a nice dress. Isn't it?"
    $ hentai_scene(4)
    "Sabia nodded."
    s "Mng...mmhmm!"
    "For the first few days, the constant stream of saliva that oozed out around the ball-gag had humiliated her. She couldn't stop it."
    "Now... she barely noticed it."
    pause(0.3)
    $ hentai_scene(7)
    call shake ("h")
    "The sound of the crop whistling through the air hit her ears before it landed, and a surge of anticipated fear rocked through her. Sabia screamed into the gag."
    $ hentai_scene(8)
    "Fire."
    "It felt like fire, across her ass. Her flesh red and tender, her thighs shuddering as the pain lanced through her."
    $ hentai_scene(9)
    "Kira bit her lip, her head leaning back a little as a pleased moan rumbled softly in her throat."
    "Her pet kept whimpering and squeaking under that gag as she played lightly with the crop, running it along with a tease."
    $ hentai_scene(10)
    "She placed the crop aside for a moment, and she took hold of Sabia's head from behind."
    s "NNGn...nnng!"
    "'I've been good!' is what she tried to say as she flinched. It didn't come out like that."
    $ hentai_scene(11)
    kira "Such sweet sounds, my pet..."
    kira "I think you've earned... another strike. Haven't you? Hmm?"
    s "NNMNNMMM!"
    "Sabia tried to shake her head wildly, but her movements were hamstrung by Kira's grip on neck and leash."
    pause(0.3)
    $ hentai_scene(12)
    call shake ("h")
    kira "Bad girl!"
    $ hentai_scene(13)
    s "Annnnggg!"
    $ hentai_scene(14)
    "Kira's groan of delight was drowned out by Sabia's harsh cry."
    "Sabia's eyes were wet with tears, squelching against the bridge of her nose and the blindfold."
    "The pain flared up again from the harsh strike, and she shuddered once more. It hurt. So. Bad."
    $ hentai_scene(15)
    "It was almost difficult to focus on the pain though. It was drowned out by the pleasure she hated feeling."
    "The pleasure that was never satisfied."
    "Sabia had been on the edge for so long..."
    "The temptation, the burning need deep within to reach release... but she knew it was not coming."
    "Kira would not let her cum."
    $ hentai_scene(16)
    kira "It's time you put that tongue to use, I think... after all that training, it would be a shame to let it go to waste."
    "A stream of Sabia's spit gushed out of her mouth as Kira unlatched the gag. She swallowed the rest of it."
    "Being able to simply swallow without struggling... it felt almost as good as an orgasm. Sabia shuddered, thighs writhing against one another."
    pause(0.3)
    $ hentai_scene(19)
    call shake ("h")
    kira "What have I told you about that?!"
    $ hentai_scene(20)
    s "AHH! I'm s-sorrY MISS Kira...!"
    $ hentai_scene(21)
    "Sabia's voice rose and fell as she tried to apologize, wracked with heaving sobs."
    $ hentai_scene(22)
    kira "Oh! Those little yelps you do... they make me shiver so delightfully."
    pause(0.3)
    $ hentai_scene(20)
    call shake ("h")
    s "AHN! Mmmhhh..."
    $ hentai_scene(21)
    "Sabia threw her head back and her whole body spasmed from the crop."
    kira "Yessss! Ahh... yes...!"
    "Kira dragged the crop up Sabia's ass, pushing it against the dildo in Sabia's pussy first, smirking at the desperate whimpering."
    $ hentai_scene(22)
    kira "What do you say...?"
    $ hentai_scene(24)
    s "Thank... I..."
    "Sabia panted, her heart pounding."
    s "Thank you... Miss Kira..."
    $ hentai_scene(25)
    "Kira's pulled Sabia closer, forcing her pet's lips and tongue against her pussy."
    $ hentai_scene(26)
    "Sabia knew what to do. She knew what would happen if she was... bad."
    "It was not as if she had much choice. Kira's hand pushed her head down forcefully, and Sabia's obedience showed."
    "She lapped at Kira, running her tongue along the elf's nethers. Kira tasted much sweeter than she was, Sabia had found."
    $ hentai_scene(27)
    kira "Ah... ah-ah!"
    "Kira's fingers tightened, twisting about Sabia's purple locks of hair. She pushed the girl in farther, moaning happily."
    kira "And you thought... you were a warrior...!"
    "Her laugh was a little trill that stung in Sabia's ears."
    $ hentai_scene(28)
    kira "But you were wrong... weren't you?"
    "Sabia's spread her tongue as wide as she could manage, and ran it up Kira's petals before pulling back a half an inch."
    "She panted, taking the moment for a breath as she shook her head. Sabia's top lip glistened with Kira's arousal, a rope of grool connected the two women."
    s "Yes Miss Kira... I was wrong."
    kira "What are you?"
    s "Worthless, Miss-"
    pause(0.3)
    $ hentai_scene(29)
    call shake ("h")
    s "Uuunnnnggh!"
    $ hentai_scene(32)
    "Sabia's howl of pain bounced off the walls."
    "Kira threw the crop aside, her hand coming back to Sabia's head."
    "No words were needed, she pushed the still-whimpering Sabia back against her pussy."
    kira "Ah- Ah- Ah! Scream... cry out! Yessss!"
    $ hentai_scene(33)
    "Kira's legs spread a little wider, and her ass slid against the seat as she pushed herself into Sabia's trembling mouth."
    $ hentai_scene(34)
    "The whimpering yelps and squeaks had been too much for her... Kira couldn't hold it in any longer."
    "Her nails dragged painfully across Sabia's flesh as she let herself have her release."
    $ hentai_scene(35)
    "The minutes passed as Kira kept Sabia down, dutifully licking and worshiping her clit... she had trained the girl well."
    kira "Good girl..."
    s "Thank... thank you, Miss Kira..."
    pause(0.3)
    $ hentai_scene(36)
    call shake ("h")
    s "Hnng... ugggh!"
    $ hentai_scene(37)
    kira "Maybe as a reward... I can take those toys out of your ass and pussy... what do you think?"
    kira "You might even cum... just from that."
    s "Please! Please, Miss Kira!"
    "Sabia's words were muffled. The sounds of her tongue, lips and nose at Kira's wet mound filled the room, renewed, as she hoped to earn her release."
    scene bg black with dissolve
    kira "After all... it will be difficult for the camp to fuck you with your holes plugged up."
    s "Miss... Miss Kira? Please, no..."
    kira "You broke so quickly... it's no longer fun anymore."
    kira "Turn around. Let me take the toys out, 'warrior'. And then call for the camp to come and join you..."
    kira "Don't worry though my little mauve delight... my crop and I aren't going anywhere."
    kira "We'll stay with you while the rest of the camp relieves themselves... in you..."
    kira "Oh, it's going to be a beautiful night!"
    if gallery_workaround == True:
        jump gallery
    return


label chufkhunt_kia:
    play music sex1 fadeout 2.0 fadein 2.0
    scene bg black with dissolve
    $ hentai_scene(1,"chufkhunt_kia",dissolve)
    "Sabia attempted to break the bonds of the tentacle's - for a lack of a better word - web, by writhing about."
    $ hentai_scene(2)
    s "Oh, fuck..."
    $ hentai_scene(3)
    s "That's not helping at all..."
    $ hentai_scene(7)
    "With every wriggle and movement she made, the slack from the slimey tentacle seemed to disappear, growing tighter and more rigid."
    $ hentai_scene(8)
    "Sabia was going to need to have some words with Kia when she got out of this predicament."
    "And they weren't going to be nice, either. Her teeth were grinding against each other as she seethed."
    $ hentai_scene(9)
    s "KIA!"
    $ hentai_scene(8)
    "There was a little bit of light that managed to reach in front where Sabia had entangled herself."
    "Kia's head popped over the edge of the hollow, and looked down."
    $ hentai_scene(10)
    kia "{i}Chufk{/i} come?"
    $ hentai_scene(9)
    s "You need to come down and get me out, Kia!"
    $ hentai_scene(8)
    kia "Why?"
    kia "{i}Chufk{/i} come!"
    $ hentai_scene(9)
    s "That's. Not. The. Point."
    s "I do {i}not{/i} appreciate being thrown in as sexual bait."
    $ hentai_scene(8)
    "Sabia could make out Kia frowning, unsure about Sabia's words."
    "Then the makhor cocked her head, claws curling about the hollow's edge as she inched a bit forward."
    $ hentai_scene(1)
    "Sabia heard the familiar low keening sound, thrumming in the cave."
    "She could sense... unease, warring with desire."
    $ hentai_scene(12)
    "Two tendrils slithered out, faster than Sabia could track with her eyes."
    $ hentai_scene(13)
    "They coiled about her arms, the slick, slimey movement against her skin sending a tingle down her spine."
    $ hentai_scene(14)
    "It didn't take longer than a second. The tingling that began throughout her body."
    "Sabia's nipples were hardening as they pointed downward, the aphrodisiac effect of the slime making her arms flush with heat."
    $ hentai_scene(15)
    "Another tentacle joined Sabia, the tapered tip caressing her ass. Almost playfully."
    "The hot flush began to burn there too, a trail of slimey stuff lingering where the tip touched."
    $ hentai_scene(16)
    s "A-ahn!"
    $ hentai_scene(17)
    "She hated how the tingling flush in her breasts made her gasp audibly."
    "And more so, Sabia hated how she was quite literally hanging there, legs spread wide."
    "At least she didn't have an audience - more than Kia peering in, that is."
    $ hentai_scene(18)
    "Slowly the tapered end of the tendril recoiled from Sabia, but not without first running down her leg."
    "Almost painfully slow, it left a trail of slime where it touched. Sabia's heart pounded faster and faster, unable to fight the growing arousal."
    "She moaned again. Soft. A trill in her throat as the tentacle slipped around, giving a quick touch on her inner thigh."
    $ hentai_scene(19)
    s "A-ah! Fuck... I... aaaah!"
    "Sabia's nostrils flared as she inhaled quickly, legs straining in a vain attempt to writhe her thighs together."
    $ hentai_scene(20)
    "The cave thrummed with its low keening. Sabia could tell it sensed her burgeoning hunger, her desire."
    "More tentacles emerged from cracks and crevices."
    "With the need burning between her legs, Sabia knew the tentacle monster wasn't going to relent."
    pause (0.3)
    $ hentai_scene(21)
    call shake ("h")
    s "Shit!"
    $ hentai_scene(22)
    "Sabia's throat tightened. Panic surged through her mind and body, and she felt her heart pound faster."
    "The tentacles slid around her neck, coiling about with a firm grip."
    $ hentai_scene(24)
    "It was tight enough that breathing was not unhindered, yet not anywhere too tight that it was difficult to breathe."
    "Sabia felt the mix of adrenaline and lust burning within her, aided by the tentacle's slime."
    $ hentai_scene(25)
    "Another tendril made its way down, the tip trailing along and poking softly against the curves of her ass."
    "It was starting to get difficult to not admit how good the soft, writhing tendrils felt against her skin."
    $ hentai_scene(26)
    s "Ahhhn!"
    "Sabia's body shuddered and her toes curled."
    $ hentai_scene(27)
    "The tentacles wrapped around her breasts, squeezing against them. They felt far more sensitive that normal, and Sabia felt the roiling pleasure within, like a lapping wave, threatening to crash against her."
    "Some of the tendrils thrummed happily against her skin. In the back of her increasingly pleasure-addled mind, Sabia realized that sensed her arousal."
    $ hentai_scene(28)
    "The tentacle atop her ass moved slowly, stroking the curves of her rear almost lovingly."
    $ hentai_scene(29)
    call shake ("h")
    "Sabia cried out in shock, the sound bouncing off the cave walls."
    $ hentai_scene(30)
    "Several tapered tips pushed into her ass, spreading her tight ring open easily."
    "Sabia's breath caught in her throat and she struggled to inhale."
    $ hentai_scene(31)
    "Surges of pleasure pounded through her body, thundered in her ears."
    "It didn't hurt at all."
    "Instead... Sabia had to admit it felt good."
    "They writhed inside, pushing gently against her walls as another playfully teased at the entrance to her pussy."
    "Her legs twitched, straining against the tentacle's web. It was too much. The touch, soft and slick, against her entrance."
    "She needed it..."
    $ hentai_scene(32)
    "They started to pull out of her ass quickly, her hole tight about them as their length grew thinner."
    $ hentai_scene(33)
    "Only to push back in with enough force for Sabia to jiggle in her bonds, her tits kept still by more greedy tentacles."
    s "Ugh... come... on! Just... a little... ahn!"
    "Sabia's words came out in long, ragged pants as she tried to push back against the teasing tentacle, still playing lightly against her slick pussy."
    $ hentai_scene(34)
    s "Please... please, please... just a bit closer..."
    $ hentai_scene(35)
    "Sabia heard the sound of Kia's growl, and the satisfied, pleased keening thrum of the tentacle monster abruptly stopped."
    kia "Sabia! Kia catch {i}chufk{/i}."
    $ hentai_scene(37)
    "Sabia grit her teeth. She had been so close, on the edge, the threshold. Her whole body was still pounding with need, and her pussy felt like it was on fire."
    $ hentai_scene(39)
    "Kia's paw felt... Sabia's spine tingled under its touch. Soft. Warm. Powerful."
    "It was hard to think with it there."
    s "Why... why am I... still stuck here then?"
    $ hentai_scene(38)
    kia "Not know!"
    $ hentai_scene(39)
    "Kia chirped it out almost happily."
    $ hentai_scene(40)
    "Another paw on Sabia's other ass cheek. Her mind was still a messy haze, a desperate need for relief rolling about her thoughts."
    $ hentai_scene(43)
    s "You need to..."
    "Sabia's words trailed off as Kia's tongue lapped at her skin."
    $ hentai_scene(44)
    kia "But Sabia want mate! Can smell..."
    $ hentai_scene(45)
    "Kia's tongue lapped at Sabia's folds. She felt every inch of the coarse tongue against her soft folds."
    $ hentai_scene(46)
    s "Ugh... come on... c'mon Kia, let- Ahn!"
    $ hentai_scene(47)
    "Kia's tongue flattened, and ran the length of Sabia's lips, right up to her clit."
    "Sabia's body shuddered under Kia's ministrations."
    $ hentai_scene(48)
    kia "But Sabia like!"
    s "That's... that's not the point!"
    "Sabia huffed the words out, even as the waves of pleasure grew larger and larger."
    s "Get me out of... out of these tentacles and-"
    $ hentai_scene(49)
    "Kia's paws gripped Sabia's ass tighter. The makhor's tongue was more insistent now, pushing eagerly against Sabia's entrance, pleased with the moans and gasps that she was earning from Sabia."
    $ hentai_scene(51)
    s "Kiaaaa...!"
    $ hentai_scene(52)
    "Sabia's couldn't breathe. Not from the tentacles. Her whole body seemed to stop, and the moment Kia's tongue lapped at her clit threw her into the waves."
    "The instant seemed to stretch, longer and longer as her whole body jerked and shook, toes curling and her fingers balling into a fist."
    $ hentai_scene(53)
    "Kia's chest rumbled happily."
    $ hentai_scene(54)
    kia "See, Sabia like, Kia like. Fun!"
    $ hentai_scene(55)
    s "..."
    "Sabia could do nothing but pant, her chest burning as air rushed back in, her thoughts slowly coming back..."
    scene bg black with dissolve
    "It took almost a quarter of an hour before Kia managed to free Sabia from the web, and another half an hour still for Sabia's body to stop tingling with need."
    "They doused the tentacle monster with enough of the orcish potion to ensure it would not wake up for some time, before taking it back to the small makeshift holding cell in Kia's suggested cave."
    "Kia was still reluctant to do so, but seemed willing to entertain the idea it could be taught how to hunt properly."
    if gallery_workaround == True:
        jump gallery
    return


label chufkhunt_nokia:
    play music sex1 fadeout 2.0 fadein 2.0
    scene bg black with dissolve
    $ hentai_scene(1,"chufkhunt_nokia",dissolve)
    "Sabia attempted to break the bonds of the tentacle's - for a lack of a better word - web, by writhing about."
    $ hentai_scene(2)
    s "Oh, fuck..."
    $ hentai_scene(3)
    s "That's not helping at all..."
    $ hentai_scene(7)
    "With every wriggle and movement she made, the slack from the slimey tentacle seemed to disappear, growing tighter and more rigid."
    $ hentai_scene(8)
    "Even if she had agreed to luring out the tentacle monster with her body, she hadn't intended to be stuck like this."
    $ hentai_scene(9)
    s "KIA!"
    $ hentai_scene(8)
    "There was a little bit of light that managed to reach in front where Sabia had entangled herself."
    "Kia's head popped over the edge of the hollow, and looked down."
    $ hentai_scene(10)
    kia "{i}Chufk{/i} come?"
    $ hentai_scene(9)
    s "You need to come down and get me out, Kia!"
    $ hentai_scene(8)
    kia "Why?"
    kia "{i}Chufk{/i} come!"
    $ hentai_scene(9)
    s "That's. Not. The. Point."
    s "I don't want to be stuck here in its slimey... tentacle-y webs while it does what it wants to me!"
    $ hentai_scene(8)
    "Sabia could make out Kia frowning, unsure about Sabia's words."
    "Then the makhor cocked her head, claws curling about the hollow's edge as she inched a bit forward."
    $ hentai_scene(1)
    "Sabia heard the familiar low keening sound, thrumming in the cave."
    "She could sense... unease, warring with desire."
    $ hentai_scene(12)
    "Two tendrils slithered out, faster than Sabia could track with her eyes."
    $ hentai_scene(13)
    "They coiled about her arms, the slick, slimey movement against her skin sending a tingle down her spine."
    $ hentai_scene(14)
    "It didn't take longer than a second. The tingling that began throughout her body."
    "Sabia's nipples were hardening as they pointed downward, the aphrodisiac effect of the slime making her arms flush with heat."
    $ hentai_scene(15)
    "Another tentacle joined Sabia, the tapered tip caressing her ass. Almost playfully."
    "The hot flush began to burn there too, a trail of slimey stuff lingering where the tip touched."
    $ hentai_scene(16)
    s "A-ahn!"
    $ hentai_scene(17)
    "She hated how the tingling flush in her breasts made her gasp audibly."
    "And more so, Sabia hated how she was quite literally hanging there, legs spread wide."
    "At least she didn't have an audience - more than Kia peering in, that is."
    $ hentai_scene(18)
    "Slowly the tapered end of the tendril recoiled from Sabia, but not without first running down her leg."
    "Almost painfully slow, it left a trail of slime where it touched. Sabia's heart pounded faster and faster, unable to fight the growing arousal."
    "She moaned again. Soft. A trill in her throat as the tentacle slipped around, giving a quick touch on her inner thigh."
    $ hentai_scene(19)
    s "A-ah! Fuck... I... aaaah!"
    "Sabia's nostrils flared as she inhaled quickly, legs straining in a vain attempt to writhe her thighs together."
    $ hentai_scene(20)
    "The cave thrummed with its low keening. Sabia could tell it sensed her burgeoning hunger, her desire."
    "More tentacles emerged from cracks and crevices."
    "With the need burning between her legs, Sabia knew the tentacle monster wasn't going to relent."
    $ hentai_scene(21)
    pause (0.3)
    call shake ("h")
    s "Shit!"
    $ hentai_scene(22)
    "Sabia's throat tightened. Panic surged through her mind and body, and she felt her heart pound faster."
    "The tentacles slid around her neck, coiling about with a firm grip."
    $ hentai_scene(24)
    "It was tight enough that breathing was not unhindered, yet not anywhere too tight that it was difficult to breathe."
    "Sabia felt the mix of adrenaline and lust burning within her, aided by the tentacle's slime."
    $ hentai_scene(25)
    "Another tendril made its way down, the tip trailing along and poking softly against the curves of her ass."
    "It was starting to get difficult to not admit how good the soft, writhing tendrils felt against her skin."
    $ hentai_scene(26)
    s "Ahhhn!"
    "Sabia's body shuddered and her toes curled."
    $ hentai_scene(27)
    "The tentacles wrapped around her breasts, squeezing against them. They felt far more sensitive that normal, and Sabia felt the roiling pleasure within, like a lapping wave, threatening to crash against her."
    "Some of the tendrils thrummed happily against her skin. In the back of her increasingly pleasure-addled mind, Sabia realized that sensed her arousal."
    $ hentai_scene(28)
    "The tentacle atop her ass moved slowly, stroking the curves of her rear almost lovingly."
    $ hentai_scene(29)
    call shake ("h")
    "Sabia cried out in shock, the sound bouncing off the cave walls."
    $ hentai_scene(30)
    "Several tapered tips pushed into her ass, spreading her tight ring open easily."
    "Sabia's breath caught in her throat and she struggled to inhale."
    $ hentai_scene(31)
    "Surges of pleasure pounded through her body, thundered in her ears."
    "It didn't hurt at all."
    "Instead... Sabia had to admit it felt good."
    "They writhed inside, pushing gently against her walls as another playfully teased at the entrance to her pussy."
    "Her legs twitched, straining against the tentacle's web. It was too much. The touch, soft and slick, against her entrance."
    "She needed it..."
    $ hentai_scene(32)
    "They started to pull out of her ass quickly, her whole tight about them as their length grew thinner."
    $ hentai_scene(33)
    "Only to push back in with enough force for Sabia to jiggle in her bonds, her tits kept still by more greedy tentacles."
    s "Ugh... come... on! Just... a little... ahn!"
    "Sabia's words came out in long, ragged pants as she tried to push back against the teasing tentacle, still playing lightly against her slick pussy."
    $ hentai_scene(48)
    s "Please... please, please... just a bit closer..."
    $ hentai_scene(36)
    s "Mmnggg!"
    $ hentai_scene(37)
    "A tentacle pushed into her mouth eagerly."
    $ hentai_scene(38)
    "Not so far that it made her choke, or made it difficult to breathe. But the heat of it was palpable, and the taste of its slime was heavy on her tongue."
    "Like... something sweet. Almost fruit. It was difficult to place."
    $ hentai_scene(39)
    "Trepidation set back in as the multitude of tendrils violating her rear started to thrust; the one in her mouth coiling and writhing about."
    $ hentai_scene(40)
    "But with the trepidation, there was desire and pleasure."
    "The tentacle at her pussy still teased, and as the ones about her neck tightened just a little, she squirmed in the creature's grip, pleading silently into the one thrusting past her strained lips."
    $ hentai_scene(42)
    "Sabia moaned into the tendril, knowing if she weren't held up like this, she would be a crumpled, whimpering mess on the floor."
    "She heard another cluster of tentacles moving, and she tried to look behind her."
    $ hentai_scene(43)
    s "MMMHPH!"
    "It felt so good as the tentacles pushed in, her throbbing pussy finally getting some attention."
    "The one that had been gently caressing her lower back squeezed between her ass cheeks, pushing down with a coiling motion until the tip managed to push against her ass as well."
    $ hentai_scene(44)
    "She had never felt so full before..."
    "But the creature was not done yet."
    "Sabia gagged on the new additions... they weren't pushing down. But they were oozing a thick and heavy stream of whatever it was that the creature secreted."
    $ hentai_scene(45)
    "Sabia groaned, her throat convulsing around the stuff. The tentacles squeezed her neck, forcing it down into her belly were it felt extremely warm."
    "She would have been humiliated at being force-fed the creature's cum... except for how good it felt that they were finally thrusting into her pussy."
    "Several tentacles, filling her tunnel up as much as it had ever been. Several smaller ones with delicate tips stroked her lips while the larger ones moved faster, pounding into her."
    $ hentai_scene(46)
    "It was too much. Too much. Everything was too much..."
    $ hentai_scene(47)
    "Her whole body was aflame with desire and lust, and the tentacles came."
    "Sabia moaned heavily, her whole body rocking from the force, the webs straining and her toes curling. Nipples hard and eyes rolling to the back of her head as she struggled to stay conscious."
    "More and more... and more of the creature's cum filled her, she could feel it in her belly, her throat; mouth and nostrils... everywhere."
    "She was sure she was going to pass out with the taste of tentacle monster cum bubbling up from deep within her..."
    scene bg black with dissolve
    "Several minutes passed as Sabia hung there, being filled."
    "And abruptly, it stopped."
    "Sabia groaned, eyelids fluttering."
    kia "Kia catch {i}chufk{/i}!"
    kia "Easy!"
    s "Mmng..."
    "With the creature incapacitated, Kia helped Sabia extricate herself from the tentacles still clutching her. They doused the beast with as much potion as they had, taking care not to inhale while it dissipated quickly."
    "It took some arguing, but eventually Sabia convinced Kia to follow the plan she had laid out."
    "It was difficult to take with all of its tentacles, but between the two of them they managed to return it to Kia's suggested cave, and imprison it in the makeshift jail they had fashioned."
    "There was no telling how many days it would take to wake again."
    if gallery_workaround == True:
        jump gallery
    return


label mariana_quest_interrogation:
    play music sex1 fadeout 2.0 fadein 2.0
    scene bg black with dissolve
    $ hentai_scene(2,"mariana_interrogation",dissolve)
    "Mariana's eyes fluttered open, confusion and shock warring on her face as she glanced about."
    "Her wrists were tied to a tree, arms up behind her head, and legs tied bound as well."
    $ hentai_scene(8)
    mariana "What... what's going on? Why did you tie me up - and where the fuck are my clothes?!"
    $ hentai_scene(7)
    n "You, asking the questions? No, no. That's not your job right now."
    n "Your job is to answer questions."
    n "So... answer this: why did you stop reporting to Dajrab?"
    $ hentai_scene(8)
    mariana "Untie me and I'll consider telling you something!"
    mariana "But I'm sure as fuck not going to answer any of your questions while I'm bound like this!"
    $ hentai_scene(7)
    "Mariana thrashed about, writhing on the grass and trying in vain to break the bonds by wrenching her arms and legs about."
    $ hentai_scene(8)
    mariana "Ugh! Let me go! I'll gut both of you if you don't!"
    $ hentai_scene(7)
    s "And you're going to do that... how?"
    n "Ooh, she's feisty, isn't she? And so cute too..."
    $ hentai_scene(8)
    "Mariana snarled her anger."
    mariana "Fuck you!"
    $ hentai_scene(7)
    "A wide smile grew on Neve's face."
    n "Now there's an idea, little Mari..."
    s "I don't think this is the time to be-"
    $ hentai_scene(6)
    n "I think it is the best time, actually, Sabia..."
    "Neve smirked at her friend, quickly undressing. She was already excited, imagining all the teasing torments they could enact on their bound prey."
    $ hentai_scene(10)
    mariana "I don't know what you think you two are going to do, but if you-"
    $ hentai_scene(11)
    "Neve bit her lip as she stepped over Mariana, sinking down to her knees."
    "Her soft thighs up against Mari's breasts made her know she had made the right choice."
    $ hentai_scene(13)
    mariana "What're you doing? Get that outta my face...!"
    $ hentai_scene(12)
    s "What {i}are{/i} you doing, Neve? We needed information... not a plaything."
    n "We can have both, she's cute."
    "Neve smirked, her fingers digging further into Mariana's hair."
    $ hentai_scene(14)
    mariana "I'm right here. Don't talk about me like I'm... I'm a toy!"
    mariana "If I weren't-"
    $ hentai_scene(16)
    mariana "Hmmmph!"
    $ hentai_scene(17)
    s "How are we supposed to get answers out of her now?!"
    n "Fun now... answers later, Sabia. Or during."
    n "You better use that tongue, little Mari, or I'm not moving..."
    $ hentai_scene(18)
    "Sabia frowned. Neve looked like she was enjoying herself, with her eyes half-lidded and legs writhing with a gentleness against Mariana's sides."
    n "Ah... yes! Good Mari... you're not... so bad at this, are you?"
    n "Are you just going to sit there and watch, Sabia? Go on, dig in to her pussy. I'll teach you how to eat pussy properly, while we have such a nice toy to play with..."
    mariana "Mmmph!"
    $ hentai_scene(19)
    "Neve frowned, her fingers tightening about the lock of hair as she yanked Mariana's head back, and then pushed her in between her thighs roughly."
    $ hentai_scene(20)
    mariana "Wha-what the fuck?!"
    $ hentai_scene(21)
    "Neve ignored Mariana's exclamations, instead watching with a predatory eye as Sabia kneeled down, and crawled closer."
    s "I already know how to-"
    $ hentai_scene(22)
    n "Not as well as you could. I'm sure we can coax out a few answers from her if you listen to my instructions, as well..."
    n "Mari... why did you leave Kira's camp?"
    $ hentai_scene(26)
    mariana "Why the fuck would I tell you?! I'm not going to tell you... not when you've tied me up - and you're probably sent here by Kira!"
    $ hentai_scene(25)
    "Neve clicked her tongue, shaking her head. With one hand each on Mariana and Sabia's head, she relished the situation."
    "She could still feel Mariana's warm breath on her... the soft dampness of Mariana's lips against her petals..."
    $ hentai_scene(27)
    n "What are you waiting for, Sabia? Get to work."
    $ hentai_scene(28)
    "Neve pushed Sabia closer, and Sabia obeyed, her tongue lapping over Mariana's whole mound."
    $ hentai_scene(29)
    n "No, Sabia... not like that... you won't coax any answers out of Mari doing that."
    n "Teasing, Sabia... slow, methodical. Slide your tongue up and down, along one lip at a time. Neglect the other lip... until she's begging for more..."
    $ hentai_scene(28)
    "Sabia's ears burned at the command, but she followed Neve's instruction. A few moments passed... and she felt Mariana's legs twitching against her sides, the soft moans of desire rumbling in the bandit's throat."
    n "Good... but that's enough for now, Sabia. You need to drag it out."
    $ hentai_scene(26)
    mariana "W-why did you stop?!"
    $ hentai_scene(25)
    n "I'll let Sabia go back down there if you answer just a simple question... you {i}were{/i} working as Dajrab's contact, weren't you?"
    n "It's just a simple yes or no... it won't even tell us much... and I still have so many things to teach Sabia about pleasing a girl."
    "Mariana tried to stifle her soft moans. The warmth of Sabia's breath on her was... almost overbearing. She could almost feel Sabia's tongue on her lips... but just out of reach."
    $ hentai_scene(26)
    mariana "Y-yes... I was..."
    "Neve smiled."
    n "See, that wasn't so hard?"
    $ hentai_scene(28)
    "Without saying another word, Neve's fingers pressed against Sabia's head. She moved forward, tongue playing lightly once more, soft. A brush here... a gentle caress there."
    n "Run your fingers along her thighs, Sabia..."
    "Neve watched as Mariana shuddered under Sabia's ministrations. She felt the girl's heaving, uneven breaths underneath her."
    $ hentai_scene(30)
    mariana "Oh... ahn! Fuck..."
    "Neve sighed softly, her command of the situation making her blood boil, her lust burn red. She felt herself dripping with excitement, with power."
    "Sabia let herself be pushed down again, Neve's grip on her firm, and unyielding."
    "Her lips pressed upon Mariana's nethers, and she pushed her tongue in, pushing against Mariana's silky insides."
    $ hentai_scene(31)
    n "Tongue, Mari! Tongue..."
    n "And Sabia... you need quit neglecting her clit. She should be screaming into me, moaning with unrestrained pleasure!"
    $ hentai_scene(32)
    "Sabia's eyes flickered, and she turned her attention back to Mariana."
    "She raised her lips up high and her tongue out, giving Mariana's clit a brief swipe with her tongue."
    "Almost immediately, she felt a reaction. Mariana groaned, her muscular legs tensing tightly around Sabia's head, not letting her go."
    n "Yes! Yes... like that! Oh... mmm, little Mari, excellent...!"
    "Words of praise flowed from Neve's lips like a river of silk as Mariana's whimpering moans thrummed against her mound."
    "Neve grunted, adjusting her weight and roughly slamming her crotch back down against Mariana's face."
    $ hentai_scene(33)
    "The surge of pleasure welled up, overwhelming Neve. She gasped in delight, arching her back and pushing herself more harshly against Mariana, nails almost scratching painfully against both Sabia and Mariana's heads."
    $ hentai_scene(34)
    "She shuddered, with thighs shaking and breasts heaving. Her white hair clinging to her forehead as she rode the waves."
    "It wasn't that Mariana was good... it was her control of the situation, the power... it was intoxicating to her and with every moment longer with Mariana buried between her legs, the thrill continued."
    $ hentai_scene(35)
    "Neve held herself there for a few more minutes, Mariana's desperation for air increasing, before she finally moved off."
    "She relinquished her forceful hand on Sabia."
    "Sabia's lips were wet with a mix of spit and Mariana's arousal."
    $ hentai_scene(36)
    mariana "I didn't... but... d-don't stop..."
    "She gasped, taking a few long breaths..."
    n "Don't worry little Mari... there's more to teach Sabia still."
    n "...if you keep answering questions."
    scene bg black with dissolve
    "Neve continued orchestrating their questioning, until Sabia's tongue and lips tingled, and Mariana had passed out. Overwhelmed and far too tired."
    "Sabia and Neve consolidated the information they had learned - Mariana had seen massive amounts of money pouring in. More than from what they had been getting from raids."
    "Troops and weapons beyond what bandits should be able to..."
    "She suspected a captain from Grok og Dar had been involved in Groknak's disappearance, and she had fled in fear of both Kira and Dajrab..."
    "But not confident enough, she had relied on the old orc's help and advice, hiding near Lake Sorthyos."
    if gallery_workaround == True:
        jump gallery
    return


label ba_ashi_soldier_dom_scene:
    play music sex1 fadeout 2.0 fadein 2.0
    $ hentai_scene(12,"ba_ashi_soldier_dom",dissolve)
    s "Leaving catgirls alone! Not tolerating misbehaving!"
    "It would be better if Bris didn't have to deal with a drunk, self-important Whitecrest envoy."
    $ hentai_scene(16)
    "Sabia fluttered her eyelids at the misbehaving Whitecrest soldier."
    $ hentai_scene(11)
    "Doing a little spin, Sabia settled into a gentle sway, rocking her hips side to side, and arching her back."
    "The roar of approval that answered her was deafening."
    "Even still, she made sure to note that Bris and the other catgirls were walking and talking."
    "After a few moments of being pat on the back, he grinned, swaying to his feet. He was several drinks deep, his leggings were tented, and his desire was clear."
    "The other Whitecrest men cheered him as he stumbled up the stage, ripping his shirt off, and managing to step out of his pants without falling over."
    $ hentai_scene(20)
    soldier "Y'don't need these anymore!"
    $ hentai_scene(21)
    "Sabia gasped as hipped the thin slip of fabric off, and then removed the tiny c-string panties too."
    "The plug made a soft pop, only audible to his and Sabia's ears - the rest of the raucous night drowning it out for anyone else."
    $ hentai_scene(23)
    soldier "H-holy... shit! B-by Relona!"
    $ hentai_scene(24)
    "He grunted his desire, a deep rumble inside his chest as he slapped his cock down on Sabia's ass."
    "A trickle of pre-cum already ran from tip down his shaft. Sabia nibbled at her lip as she felt the wetness against her skin."
    s "Hmm? Not knowing to what do?"
    s "Ba Ashi then helping! Silly boy..."
    $ hentai_scene(26)
    soldier "I know... fuck, I know... what... I know what to do, fuck!"
    $ hentai_scene(25)
    "Sabia rocked her hips back and forth, sliding the cock between her ass cheeks. His excitement was palpable, and with every move, she could feel his pre-cum dripping down."
    "Before he got to do anything else though, Sabia reached back and wrapped her fingers around his shaft, squeezing tight."
    s "Not to be bothering friendlies catgirls, okay?"
    soldier "Fuck - ow, okay, okay... yes I won't, alright?"
    $ hentai_scene(26)
    "Sabia nodded her acknowledgment and wriggled her ass."
    $ hentai_scene(27)
    "His started to thrust into her movements. Sabia's damp slit pressed up against his balls, and the warmth of them made her blush a darker red."
    $ hentai_scene(28)
    "He growled, hunching forward and both of his hands came down with a loud slap on each of Sabia's ass cheeks."
    "His pace quickened, and his hands pushed her cheeks tighter around his shaft."
    s "Oh! Already going?!"
    $ hentai_scene(29)
    soldier "FUCK! Hnnggg! It's not... ugh, cumming!"
    $ hentai_scene(30)
    "He sunk forward, balls against Sabia's pussy as he came. They pulsed, tense, and she could feel it before every rope splattered over her back."
    $ hentai_scene(31)
    soldier "That was... mmm... very good."
    "With his pleasure sated, he grunted, slapping Sabia's ass again, and wiping himself off on her pale flesh before stumbling back to his seat."
    $ hentai_scene(32)
    s "(I thought I was at least going to get off too... ugh. Useless.)"
    scene bg black with dissolve
    "Sabia spent another hour or so dancing and performing for the rest - though she did not let any of the others have a chance with their cocks."
    "By the end, most of the visitors from Whitecrest were completely smashed, and the catgirls were among them, asking question and flirting."
    if gallery_workaround == True:
        jump gallery
    return


label ba_ashi_soldier_sub_scene:
    play music sex1 fadeout 2.0 fadein 2.0
    $ hentai_scene(12,"ba_ashi_soldier_sub",dissolve)
    s "Leaving catgirls alone! Not tolerating misbehaving!"
    "It would be better if Bris didn't have to deal with a drunk, self-important Whitecrest envoy."
    $ hentai_scene(14)
    soldier "Heh! Then I'll come misbehave on stage!"
    "The rest of his group roared with laughter as he stumbled, half-drunk, onto the stage."
    $ hentai_scene(19)
    s "No staging pleases!"
    $ hentai_scene(20)
    soldier "Heh... don't be a fucking tease!"
    $ hentai_scene(21)
    s "You are not meaning to be-"
    "He ignored Sabia's protest, and instead yanked the half-transparent slip of fabric off, letting it pile delicately on the floor."
    "He wasted no time in removing her tiny c-string panties either, chuckling just loud enough for Sabia to hear as she whimpered when her ass relinquished the plug."
    $ hentai_scene(22)
    soldier "Don't worry about it... you wouldn't have called me out if you didn't want it... heh..."
    "He groped at Sabia's ass, dragging his fingers across her soft flesh as he snickered to himself."
    "Sabia pursed her lips, letting him paw her as he desired."
    $ hentai_scene(23)
    "His cock slapped down on Sabia's ass, and she couldn't help but gasp. A tremor of concern ran through her mind at the sheer weight of it resting there."
    $ hentai_scene(24)
    "Looking back at his smug grin, Sabia started to roll her hips, rubbing her ass against the underside of the throbbing length."
    $ hentai_scene(25)
    soldier "Haha, eager for cock, are you? Maybe dancing isn't the job for you...?"
    "He smirked to himself, chuckling as he dug his fingers into her ass again. His cock rubbed along her pale skin, dripping with anticipation."
    $ hentai_scene(26)
    soldier "C'mere... no more... hic! No more playing!"
    "His hand wrapped around her arm easily, and he pushed his leg in between her own."
    "A jolt of surprise washed over Sabia, even as she parted her legs a little at the insistent knee."
    s "Not being to-"
    $ hentai_scene(27)
    s "Nnng!"
    $ hentai_scene(28)
    "The tips of Sabia's ears burned red underneath her veil, his cock slamming into her tight entrance - the wet, squelching sounds surely loud enough for everyone to hear?"
    $ hentai_scene(29)
    "Sabia's fingers curled about the pole a bit tighter as his cock throbbed within her depths, her lips stretched around his girth."
    $ hentai_scene(30)
    "Sabia's fingertips brushed against the sides of his leg as he started to veritably hammer into her."
    "He wasted no time, he wanted to pound Ba Ashi. And pounding Ba Ashi was what he was doing."
    "His whole body rocked with his efforts, driving himself balls deep into Sabia with every thrust."
    $ hentai_scene(31)
    "Sabia jumped as his hand landed on her ass. She realized before it had been a tap. This one stung, and her muscles convulsed, squeezing around his length involuntarily."
    $ hentai_scene(33)
    soldier "Hnng... fuck... she loves it, boys!"
    "Grunting his amusement, he started to speed up."
    "His balls slapped loudly against Sabia, wet, warm and full of cum-"
    s "Not insiding pleaseeee!"
    $ hentai_scene(34)
    "Sabia's request was too late. The soldier slammed into her, his fingernails dragging almost painfully across her ass, and her arm immobile with his grip."
    $ hentai_scene(35)
    "A few quick spurts, and the still-half-drunkard dumped his whole load inside Sabia's tunnel. She felt the familiar feeling of warmth spreading out from within her center."
    "More of it oozed out, overflowing."
    $ hentai_scene(36)
    soldier "That... ugh! That was great...!"
    $ hentai_scene(37)
    "Laughing, he gave her another playful slap on her ass. This one stung more than the other playful slaps - her ass still sore from the harsh whack."
    scene bg black with dissolve
    "The rest of the group laughed and cheered as he stumbled back to his seat, though thankfully Sabia didn't have any more coming to join her on stage."
    if gallery_workaround == True:
        jump gallery
    return


label avion_ritual:
    play music sex1 fadeout 2.0 fadein 2.0
    scene bg black with dissolve
    "It was clear to her that her teasing and taunting had only made Avion all the more excited for the ritual."
    "Sabia felt like she weighed nothing. Avion had picked her up with ease, and held her like she was nothing more than a doll."
    $ hentai_scene(2,"avion_ritual",dissolve)
    "Despite her confidence, the hot and heavy weight of Avion's throbbing shaft against her tiny slit was suddenly a lot more intimidating."
    "The ridge of his sheathe pressed in against her legs."
    $ hentai_scene(3)
    "Still, she was sure she could handle Avion."
    $ hentai_scene(4)
    s "You really think you're going to last long with that massive thing inside me?"
    s "There's no way!"
    $ hentai_scene(3)
    avion "Hmph... I think the question you should be asking is how long are you going to last before you lose yourself?"
    avion "Do you know how many human women we have in Naltaan? They broke into cock-hungry sluts so easily."
    $ hentai_scene(5)
    s "Huh, really? I guess that's why you're over here instead of in Naltaan then, is it?"
    $ hentai_scene(6)
    "Avion grunted at Sabia's quip, his fingers pressing on her harder. He rolled his hips a few times, rubbing his cock up and down Sabia's lips."
    "The salty musk of sex and cum was already heavy in the forest air, the tip of his shaft dripping in excitement."
    $ hentai_scene(7)
    s "Hah, see! Already getting too excited at the idea of getting to fuck me, aren't you?"
    s "There's no way you'll win... you just won't be able to control yourself as soon as that's inside me... and I'm able to wriggle and squeeze down on it."
    $ hentai_scene(8)
    "Avion's whole body rumbled in a smug, confident chuckle as he leaned forward, his tongue lapping along Sabia's cheek."
    "It was almost as big as her head."
    avion "To me it seems like you are far too eager to find out how big it is going to be inside your hole."
    $ hentai_scene(10)
    s "And to me it feels like you're making a lot of excuses, and still haven't started {i}actually{/i} fucking me."
    $ hentai_scene(13)
    "Sabia could feel Avion smirking down on her as her pulled his tongue back."
    avion "Let's see what you have to say then, human."
    $ hentai_scene(14)
    pause (0.3)
    call shake ("h")
    s "UUGGHNNN!"
    $ hentai_scene(15)
    avion "That's what I thought. Nothing but another human slut waiting to be clothed properly in Naltaan."
    $ hentai_scene(16)
    "Avion had only thrust his tip into her, but Sabia's little outburst was accompanied by a red blush across her cheeks."
    "She looked down, gritting her teeth as her pussy lips tingled, force wide enough to let Avion in."
    $ hentai_scene(17)
    s "Fuck... is that all you have?"
    s "You've only put your head in! Heh, too tight for you?"
    "Sabia grinned, rolling her hips back and forth under Avion's unyielding grasp, teasing the tip of his towering cock."
    $ hentai_scene(18)
    avion "I don't want to break you too fast. I am just letting you get used to it... letting your wet cunt prepare for me."
    avion "But you're so eager, rolling around on me. Desperate to try and be filled."
    $ hentai_scene(19)
    s "Desperate? Maybe, but by someone that can handle me."
    s "I doubt you'll last-"
    $ hentai_scene(21)
    pause (0.3)
    call shake ("h")
    s "F- uGGHHH! Hnggg..."
    $ hentai_scene(22)
    "Avion gave one last languid lick, enjoying the taste of Sabia's pale flesh before his hands forced her forward and her gaze down."
    "She was still whimpering and gasping."
    avion "Look at you. You can barely take me in."
    $ hentai_scene(23)
    s "(...fuck! It's so big... I can...!)"
    "Sabia grit her teeth again, her feet dangling above her as she saw the outline of the cock through her belly."
    "Her pussy was throbbing, and she had {i}never{/i} felt so full in her life."
    $ hentai_scene(24)
    s "I can see it... and I can feel your breath coming faster, Avion."
    s "I can feel the eager throb in your cock as it pushes against my walls, as it pulses deep inside..."
    s "I'll have you cumming before you know it!"
    $ hentai_scene(25)
    avion "I'd love to see that, maybe you have aspirations for Naltaan after all, I-"
    "His words cut off as Sabia squeezed herself against his cock, shimmying side to side."
    "Steam billowed from Avion's nostrils, but he was not to be outdone."
    $ hentai_scene(26)
    s "What- I, hnng!"
    "Avion snorted, clearly pleased."
    "Sabia had only just started to get used to such a large thing lodged inside her before Avion ripped himself out."
    "Her pussy lips gripped the length of it as he did so, and she shuddered, whimpered and moaned all at once."
    $ hentai_scene(27)
    pause (0.3)
    call shake ("h")
    avion "Hmph. With such pathetic - UGH!"
    "Avion thrust himself back into Sabia mid-sentence. Despite his claims of stamina and endurance, he couldn't help but admit to himself just how tight Sabia was."
    "And just how much better she was than some of the other humans he had used in rituals."
    $ hentai_scene(28)
    s "H-huh... W-what's that? I couldn't... hmpf... couldn't hear you over the sound of... of you groaning in pleasure...!"
    "Sabia's words were trembling. Her heart was pounding and she felt hot, beads of sweat dripping down her face and her body."
    $ hentai_scene(29)
    pause (0.3)
    call shake ("h")
    avion "Just cum. There is no way a human... a human like you can- can stand up to the endurance and might of a... minotaur!"
    $ hentai_scene(30)
    "Sabia was having difficulty speaking. Avion's rhythmic thrusting felt like his cock was making a new home inside her."
    "With every harsh bestial grunt from Avion, came the sight of her bulging belly just peeking over the curves of her tits."
    $ hentai_scene(32)
    avion "Pathetic, worthless human... can't stand... up to... the endurance!"
    "Sabia was groaning, letting words be forgotten."
    "Her face ran with a mix of sweat and Avion's spit. The heavy, bestial scent of him twisting through her senses."
    "But she knew Avion was close to his climax as well."
    $ hentai_scene(34)
    pause (0.3)
    call shake ("h")
    "Avion roared as he buried his cock into Sabia."
    $ hentai_scene(35)
    "Sabia's legs spasmed, twitching and pushing against Avion's bulging arms as she felt the last half of the cock buried inside her erupt."
    "Her tongue lolled from her mouth and she didn't have the breath to speak, but she could not help a smug sense of satifaction flow through her shuddering body."
    $ hentai_scene(36)
    s "Looks like... unng... looks like you couldn't... couldn't hold it in, huh?"
    "Sabia practically panted the words out. Avion's cock still throbbed, more of his seed filling her and gushing out past her tingling lips."
    $ hentai_scene(37)
    avion "..."
    s "Looks like neither of us won..."
    if gallery_workaround == True:
        jump gallery
    return


label avion_ritual_rough:
    play music sex2 fadeout 2.0 fadein 2.0
    scene bg black with dissolve
    "Sabia's clothes did not stand up to Avion's anger and strength."
    "His cock was already hard by the time he wrapped his arms around her and lifted her up like a toy."
    $ hentai_scene(1,"avion_ritual_rough",dissolve)
    "Avion's arms were tight against the backs of her knees, the fur rough on her skin."
    "His hands cradled - no, they gripped her head. Forcefully."
    $ hentai_scene(2)
    "Sabia had expected something harsh, but this surprised even her."
    $ hentai_scene(5)
    s "This isn't what we agreed to!"
    $ hentai_scene(4)
    avion "Does the shark care what it says to the fish it eats?"
    avion "Be quiet and serve your purpose."
    $ hentai_scene(5)
    s "..."
    s "This is just a bit-"
    $ hentai_scene(6)
    "Sabia gasped as Avion slathered her features with his tongue. A sharp intake of breath caught some of the dripping ropes of spit."
    "The taste spread in her mouth and she shuddered, her pussy rubbing against the towering cock."
    $ hentai_scene(7)
    "She hated the way it felt on her skin. He ran it over everything, and she scrunched her eye shut."
    $ hentai_scene(10)
    avion "I will enjoy hearing your screams, and feeling you about me..."
    "Slowly, Avion pulled his hips back. His wet cock dragged down over Sabia's belly and lips. Farther. The tip throbbed against her opening."
    $ hentai_scene(7)
    avion "I can see your fear. I can {i}taste{/i} your anger."
    avion "My cock is going to break you, and hollow your insides until your holes are nothing but a sheathe for minotaur cock."
    $ hentai_scene(9)
    "Avion moved down a bit more, until he was pushing against her ass."
    s "WAIT! No! No, no, no! That could barely fit inside my pussy... you'll break me if you put it in there!"
    $ hentai_scene(11)
    pause (0.3)
    call shake ("h")
    avion "{i}I HOPE SO!{/i}"
    $ hentai_scene(12)
    "Sabia choked on her own spit and breath as Avion pierced her tight ring with his vicious thrust."
    "It hurt. Badly."
    "She cried out in pain."
    $ hentai_scene(13)
    avion "Hmph... see. Even half of me is enough to make you whimper, sputter and cry."
    $ hentai_scene(14)
    "Sabia huffed angrily, trying her best to ignore the pulsing cock pushing her tiny hole to its limits and beyond."
    "Trying her best to ignore the dripping spit and the warmth filling her from the inside."
    s "Of c-course! It's... it's too big! You have to... have to take it out!"
    $ hentai_scene(15)
    "Her nose wrinkled in disgust as the thick, flat tongue lapped at her face again. Avion's fingertips pressed against her skull hard."
    "The involuntary urge to try and get away from it was still there, and the muscles in her neck burned as she tried to pull her face away from his eagerness."
    $ hentai_scene(16)
    avion "Take it out? Stop talking back, human whore!"
    $ hentai_scene(17)
    pause (0.3)
    call shake ("h")
    avion "HMPH! You are {i}mine{/i} to do with as {i}I{/i} wish!"
    $ hentai_scene(18)
    s "Fuck, fuck fuck fuck... Relona, please, take it ouuuut! It hurts!"
    $ hentai_scene(19)
    avion "Good."
    "Avion smirked to himself, slamming his hips against Sabia's pinned ass and driving another few inches of his far-too-large shaft into Sabia."
    avion "This is not just the ritual now. It is punishment."
    $ hentai_scene(20)
    "Sabia whimpered pathetically as he pulled back. The head of his flared shaft was still coating the insides of her ass with his pungent pre cum."
    $ hentai_scene(21)
    pause (0.3)
    call shake ("h")
    avion "Watch!"
    "Avion snorted his amusement, forcing Sabia's head forward."
    avion "Watch as I break your holes, as my cock makes you scream and cry!"
    $ hentai_scene(22)
    s "Not again! It's too big! Please stop! I'm s-sorry!"
    "She could feel her tears running down, dripping onto her tits."
    "Every squeak and yelp she made from the pain of Avion's brutal, rough fucking only made Avion more excited, and more pleased with himself."
    $ hentai_scene(23)
    pause (0.3)
    call shake ("h")
    "His breath wafted over Sabia's face. Hot, warm and wet. She hated it. And she hated the shuddering tingle that surged through her body from it."
    s "I- ugh.... nnf! P-p-please!"
    $ hentai_scene(22)
    avion "Be silent, you worthless piece of meat!"
    "Sabia gasped as his cock ripped out, her tight ring clinging to the throbbing veins. She could feel the blood pumping through it, pushing against her insides."
    "...she was sure she would never be able to walk again, that fear sinking its teeth into the back of her mind. Fear... with just a little bit of..."
    $ hentai_scene(21)
    pause (0.3)
    call shake ("h")
    s "Nng! Eeeaaagh!"
    "Avion's cock slammed into Sabia, her cheeks rippling from the impact, his balls slapping up against her slit."
    "Sabia squeaked again, trying to stifle the short spasm of pleasure that she felt jolt through her."
    $ hentai_scene(20)
    avion "Pathetic, snivelling human... you think you can keep pace with a minotaur?"
    $ hentai_scene(21)
    pause (0.3)
    call shake ("h")
    "Sabia's yelps and squeaks bounced off the trees as Avion began to hammer her ass."
    "Tears rolled down as Sabia started sobbing in earnest. She tried to hold it off, not to let Avion see."
    $ hentai_scene(23)
    avion "Hmph... I'm going to paint your entire body white with seed!"
    "His pounding quickened, and Sabia cried, pleading for him to at least slow down - just a little bit."
    "But the words came out as a garbled, half-choke as she gagged on her own spit and struggled to breathe."
    "Her ass was going to rip, she knew it! Avion was fucking her like she was a minotaur... her mind had all of its thoughts ripped away, and she could only focus on the pain Avion was fucking into her."
    $ hentai_scene(26)
    s "Puh- p- puh...lease! I... s-sorryyyy!"
    "Her words came out in a long, drawn out moan that shook and shivered. She could hear Avion's cock pounding her ass through her own words."
    "With every vicious thrust into her, it shook her whole body and and made her voice tremble. She hoped that it put a shroud over the small moans and squeaks of pleasure Avion's ritual was causing."
    $ hentai_scene(27)
    pause (0.3)
    call shake ("h")
    avion "Worthless human! Ugh!"
    $ hentai_scene(35)
    "Avion's cock swelled up with his orgasm, Sabia's whimpered as her ass throbbed and screamed in protest as it stretched to its absolute limits to accommodate it."
    "Her head pounded as Avion's hands gripped her like a vice, and his load erupted inside her."
    "She felt the first splatter of the stuff hit her insides."
    s "You have to- to... uggghhflkkkkh!"
    "Avion continued to ram himself into Sabia's tight hole, milking the monstrous load of seed in his balls. Sabia's words cut short as she felt the odd sensation."
    $ hentai_scene(36)
    "His load never stopped, it kept coming, and coming, and coming... filling her belly, and then gushing up."
    "She tried to shake her head, desperate to not have it happen and swallowed in vain."
    "The stuff forced its way up her throat, and filled her mouth. The strong, salt taste of Avion's cum permeated her senses even as more of it gushed mouth-ward."
    $ hentai_scene(28)
    "It slowly started to ooze out of her lips as she kept her mouth closed, trying to deny it. But there was too much."
    "Her mouth opened, and Avion's cum rushed out of her mouth like a torrent, painting her lips and chin white as it dripped down onto her tits."
    $ hentai_scene(29)
    "Avion produced a small ritualistic marker from somewhere Sabia couldn't see."
    "She glanced down over the cum still pouring from her lips. She tried to swallow, but her whole system was full of the stuff. Sabia gagged on it, more tears running down her face."
    avion "Hmph. There."
    "Just barely, Sabia could make it out a small marking on her breast, where Avion had drawn it."
    s "Nnnfgkkk...fnnk R'na..."
    "'Fuck, thank Relona that's over' is what Sabia had {i}wanted{/i} to say."
    $ hentai_scene(30)
    avion "Now we can begin."
    s "!"
    s "Vaahwt?!"
    $ hentai_scene(31)
    "Avion threw Sabia to the ground and pulled her back to his cock by her ankles."
    "She scrabbled on the forest floor, trying to pull herself away, but his cock sunk back into her ass."
    "She wasn't sure how long Avion spent using every one of her holes. But the sun had gone down, the moon had come up."
    "About halfway through Avion's punishment, Sabia's mind and body had given in to the treatment. The pain had dulled, and the pleasure had grown, and grown. Until it was almost overwhelming."
    "It had only served to urge Avion all the more, his cock smashing orgasm after orgasm into Sabia's slowly dizzying mind. It had worked, she had cum... more times than she could count."
    "And she {i}ached{/i}. Everywhere."
    "She could see patches of grass that had been bent and broken, outlines of where she had been rammed hard into the ground, splotches of cum painting where her hole had been {i}used{/i}."
    "A few trees had broken branches, or roots that had been uprooted. Made into nothing more than a tool to help abuse and fuck Sabia."
    "With every time Avion came, he marked Sabia again, seemingly pleased with himself."
    $ hentai_scene(32)
    avion "Hmph..."
    "Avion jerked his hips forward and dumped the last amount of cum his balls could muster inside Sabia's ass."
    $ hentai_scene(34)
    avion "That will do for now, the ritual is complete. The Gods will be satisfied by this."
    avion "And such a better place for a pathetic not-even-worthy-of Tlactina such as you."
    avion "You are a good bitch to use. I will be having fun with you in the future."
    "Sabia whimpered."
    avion "And not just for rituals."
    $ hentai_scene(33)
    s "M... mmf... enn..."
    if gallery_workaround == True:
        jump gallery
    return


label living_vessel_ritual:
    play music sex2 fadeout 2.0 fadein 2.0
    scene bg black with dissolve
    "Sabia struggled, her brows furrowed. The bonds around her wrists and ankles were unescapable for her."
    $ hentai_scene(1,"living_vessel_ritual",dissolve)
    s "Is this necessary?! I can't move!"
    $ hentai_scene(2)
    brug "This much better. Should have just done this to Sabia when she first come."
    dul "Haha, Dul wishes..."
    $ hentai_scene(3)
    s "Are you listening to me? I can't move at all, and this thing in my ass... I can't move my head forward!"
    $ hentai_scene(7)
    pause (0.3)
    call shake ("h")
    brug "Of course not! You must replace the object you broke."
    $ hentai_scene(9)
    "Brug was almost sad that Sabia couldn't see his smug grin as his fingers pressed against her ass."
    $ hentai_scene(10)
    "She did her best to ignore Dul's greedy hand on her breast. It was hard. The calloused roughness brushed against her sensitive nipple."
    "With his hand and the clamp... it was too much."
    "Sabia tried to muffle her squeak, but Dul and Brug both heard it, chuckling to themselves."
    $ hentai_scene(11)
    s "You could at least take that hook out... surely that's not necessary! And why are my breasts tied up and my nipples clamped!"
    $ hentai_scene(12)
    s "And I don't think- ggnnfrhg!"
    $ hentai_scene(13)
    brug "Hey, that's a good idea. Brug is surprised Dul think of it!"
    "Sabia gagged as his fingers pushed in, choking on her own words."
    brug "Where are the ritual tokens going, if there is no band from one tit to the other, huh?"
    brug "Dumb slut."
    s "Mmng! Rrrnng!"
    $ hentai_scene(14)
    s "!"
    dul "Sabia must be good at sucking dick. My fingers go down her throat so easy, hah!"
    s "..."
    "Her chest heaved as she tried to breathe - which only served to push herself further into Dul's grip. She started to drool, spit running down her chin and she found herself unable to stop it."
    brug "And head need to be kept up. Not move. Like the ritual urn, that you broke."
    $ hentai_scene(15)
    "The two orcs must have nodded to each other, Sabia thought. Their hands left her body and throat."
    $ hentai_scene(16)
    "She gasped, breathing in deeply. Her chest heaved from it, a few drops of wine spilling from the horn lodged between her tits."
    $ hentai_scene(17)
    dul "Dul do example of ritual. Make sure not to talk. Don't move. Sabia meant to be urn."
    $ hentai_scene(18)
    "Dul removed the horn from its position and took a small sip, before pushing it back between Sabia's bound cleavage. He leaned forward."
    "Sabia could feel his breath on her face."
    brug "Open mouth."
    "Sabia grimaced to herself, but was not in a position to argue."
    $ hentai_scene(19)
    brug "Good."
    brug "Sabia better not do anything to ruin ritual. Ornshakar won't be pleased. Rest of tribe won't be pleased."
    $ hentai_scene(20)
    "Her chance to speak back was cut short as a stream of wine and spit poured from Dul's lips. It caught just in her mouth, a few drops spilling out."
    $ hentai_scene(21)
    "Dul pulled back. The two orcs waited for a moment while Sabia endured the humiliation of spit and wine lingering in her mouth."
    dul "Swallow it! It must be imbibed by vessel!"
    $ hentai_scene(22)
    "Sabia closed her mouth, wrinkled her nose, and swallowed it."
    "She wasn't sure, but it felt like a very potent wine. For an Orcish ritual... it made sense. But she wasn't happy about it."
    "Sabia had sensed a small something added to the band coming from the clamps around her nipples, the weight almost imperceptibly more."
    $ hentai_scene(23)
    pause (0.3)
    call shake ("h")
    s "Argh!"
    $ hentai_scene(24)
    s "It's hard to be quiet when you're bringing down your hand hard enough to leave bruises!"
    $ hentai_scene(25)
    dul "Shut up. No talking!"
    brug "Brug and Dul trying to make sure Sabia can keep quiet through ritual, and any surprises that might happen. That's all. Should be thanking Brug and Dul."
    $ hentai_scene(26)
    dul "Open mouth. Say thanks."
    "Bristling at their words and wanting to snap back, Sabia took a deep breath. No point in antagonizing them. Especially in this position."
    $ hentai_scene(27)
    s "Fine. Thanks for-"
    $ hentai_scene(29)
    s "Did you just {i}spit{/i} on me?!"
    "Both Dul and Brug had pulled their hands off, laughing uproariously at Sabia."
    s "That {i}can't{/i} be part of the ritual!"
    $ hentai_scene(30)
    "Sabia tried to press her lips together, to stop the invading fingers."
    "It only earned a snicker from the orcs, and Dul pushed harder, forcing his way in."
    s "Mmnnf!"
    $ hentai_scene(31)
    brug "Slut! Brug tell you! NOT SPEAK. NO NOISE."
    dul "Be {i}quiet{/i}!"
    s "MMMMRGH!"
    $ hentai_scene(32, effect=dissolve)
    "Dul and Brug's groping and teasing continued for a short while before Ornshakar called on them."
    "She could hear many orcs arriving outside the tent."
    "Murmured surprise and a sense of unsureness rumbled through the congregation as Ornshakar explained that the ritual would be performed the old way."
    "Sabia heard Ornshakar reassuring the crowd, and after a few minutes of hoping she might get out of this, the first orc entered."
    $ hentai_scene(33)
    "The world was spinning. Even with the blindfold on, Sabia knew that the world was tumbling over itself."
    "Her head pounded. She had lost count of how many had participated in the ritual already."
    "What's more, every muscle in her body ached and screamed in protest; they all burned and throbbed dully at the same time."
    "She desperately wanted to put her head forward... just a little bit. But the hook prevented it, pulling painfully against her ass if she moved too much..."
    $ hentai_scene(34)
    "The orc pulled away, adding another token to the others."
    "By now, her nipples were almost numb. Or were they far too sensitive? Sabia wasn't sure."
    "She knew that the weight was pulling on her tits though, and the hook in her ass was no longer painful... it almost felt good."
    $ hentai_scene(35)
    "She had barely swallowed the mouthful of wine before the next orc entered the tent."
    $ hentai_scene(36)
    "He took the horn. There was still a little left. He swished it around and Sabia dutifully opened her mouth."
    "If she weren't tied and restrained, opening her mouth would probably be enough to send her toppling to the floor with how drunk she was."
    $ hentai_scene(37)
    "The last orc let the wine and spit mixture fall into Sabia's mouth, added the token to the others and even offered a curt 'thank you.'"
    $ hentai_scene(38)
    "Sabia struggled to swallow the alcohol. She already felt so full."
    "A few minutes passed and no new orcs came in. Was it over? She didn't dare speak..."
    $ hentai_scene(39)
    pause (0.3)
    call shake ("h")
    s "Ahn! Y... nnfg! That'sh... ugh..."
    $ hentai_scene(40)
    brug "Open mouth. One last orc to go, then ritual finished. You did well so far."
    $ hentai_scene(41)
    "Sabia obeyed, letting her lips part."
    $ hentai_scene(42)
    "She swore that she could hear some muffled snickering... but it was difficult to listen when her head was pounding and thumping so heavily."
    $ hentai_scene(43)
    dul "Hahaha..."
    "Dul laughed as he spat the wad into Sabia's mouth."
    dul "Don't forget to imbibe it."
    "He grinned to Brug over Sabia, his fingers squeezing Sabia's breast almost painfully, the row of tokens clinking against one."
    $ hentai_scene(44)
    brug "She's so drunk."
    dul "Heh... Dul know. Dul have good idea!"
    dul "Open mouth! One last orc."
    s "B-but... whashn't there... that'sh... lastsh of thh.. went they gone... orcsh?"
    s "Ahn! O... okay...!"
    $ hentai_scene(45)
    "Sabia whimpered as their grips tightened, squeezing painfully into her ass and her breast. She parted her lips again, wine and spit clinging to her chin and going cold on her chest."
    $ hentai_scene(46)
    brug "Heh."
    "Grinning to his friend, Dul ripped his pants off and let his cock spill out. It had been hard since before the ritual."
    $ hentai_scene(47)
    "Dul wrapped his hand around his cock, groaning at the pressure along his sensitive shaft. He quickly started to stroke, the tip of his cock a hair's breadth from Sabia's lips."
    $ hentai_scene(48)
    s "That'sh... the shmell... ish that... wiiineee?"
    $ hentai_scene(49)
    dul "Ugh! Fuck! Yes. Dul sure... mf, sure it's wine!"
    $ hentai_scene(50)
    "Dul gasped, his breath shaking as he unloaded all of his seed into Sabia's mouth. Several strong ropes of the sticky stuff shooting right inside, and a few that draped down over her chin."
    s "Doeshn't... tashte!"
    brug "Is wine. Trust Brug and Dul. Swallow it."
    s "..."
    $ hentai_scene(51)
    "Sabia went to nod, and gasped as the hook pulled on her ass. She swallowed Dul's load."
    "The taste was muddled with spit and more than enough wine to get an orc drunk."
    dul "Heh! Dumb drunk bitch. Believe anything we say. If Dul knew it this easy to get Sabia like this, would have just bought her a drink weeks ago..."
    brug "Haha. Brug same!"
    scene bg black with dissolve
    if gallery_workaround == True:
        jump gallery
    return


label cum_drinking_bet:
    play music sex1 fadeout 2.0 fadein 2.0
    $ hentai_scene(1,"cum_drinking_bet",dissolve)
    s "O... okay! I'm sitting down... do I get, uhm. Do I get my lundils now?"
    yeralg "What? No, of course not! We said you gotta be friends with us. "
    yeralg "You gotta show tits!"
    $ hentai_scene(2)
    "Sabia blinked slowly, her mouth opening and closing with no words coming out. Slowly, her gaze moved down."
    $ hentai_scene(3)
    s "But... I've got my tits out... see?"
    $ hentai_scene(2)
    trag "Yeah, you got your slutty tits out, you cock-hungry little cumdump."
    trag "But obviously you have to let Trag and Trag's friends play with them."
    "Grinning, Trag beckoned one of his other friends over to sit at the table with him and Yeralg."
    $ hentai_scene(4)
    "Without waiting for the drunk Sabia to realize what Trag said, Yeralg smirked and reached over."
    "His hand was more than large enough to cup Sabia's generous breast."
    "She squeaked softly as the warmth pressed against her cool flesh, the skin coarse and rough on her nipple."
    $ hentai_scene(6)
    orc "Hah, the slut's like a fucking cow with udders this fucking big."
    "Sabia's mouth hung open, a stream of garbled, intelligible drunkenness coming out as she tried to protest. It was quickly silenced."
    "The orc's hand struck Sabia's breast from below, the sound a loud sharp ringing that easily filled the room, and burned in Sabia's ears."
    $ hentai_scene(5)
    trag "Hah, truer words have never been spoken in the Silvertusk, Trag thinks!"
    trag "Don't you agree, Sabia?"
    $ hentai_scene(6)
    s "Agree...?"
    "Yeralg made sure it wasn't easy for Sabia to speak. His fingers were digging into her flesh, as if she were nothing but a toy for him."
    yeralg "Yeah. Agree with Trag, Sabia!"
    $ hentai_scene(2)
    s "I- ugh! That... that hurts..."
    "Both of the orcs pulled their hands off, gripping each of Sabia's nipples tightly between thumb and forefinger. They snickered at Sabia's yelp."
    trag "Agree with me. Or no lundils!"
    $ hentai_scene(3)
    s "But- But I want... I need my lundils...!"
    $ hentai_scene(1)
    yeralg "Exactly. That's why Sabia got to agree. What is Sabia like? Tell Yeralg, Trag and Yeralg's friend!"
    $ hentai_scene(3)
    s "..."
    s "I'm... my tits make me like... like a cow, cause they're so fat..."
    "Sabia's face flushed hot and red as she said it, knowing full well that all three sets of orc eyes were glued on her tits, and their cocks hard between their legs."
    "She couldn't help but feel a little bit excited, a little bit of lust burning within her as she tried to rub her thighs together subtly."
    $ hentai_scene(4)
    yeralg "Heh, that's right. Dumb slut. Like a human slut with fat cow-tits."
    $ hentai_scene(6)
    orc "Me not sure... you guys maybe wrong. Maybe she like a broodmare, haha!"
    "Sabia's breath caught in her throat as the second hand came swiping down through the air to land on her already sore breast."
    $ hentai_scene(2)
    trag "Or maybe just a fuck pig. Hah. Probably been dreaming about this, Sabia, eh? Wanting us to fuck you hard, you little cow-titted pig."
    "Sabia's mouth was salivating at the talk. She struggled to swallow, her breath almost catching and her legs twitching, wriggling her thighs together almost eagerly."
    trag "Go on, say it Sabia."
    yeralg "You want lundils? Say you just wanna be an orc fuck pig!"
    "It seemed like the room was going to topple over as the orcs laughed, leaning back in their seats. Sabia had drunk far too much. And she really wanted those lundils..."
    $ hentai_scene(3)
    "Trying not to look too eager Sabia put a reticent face on. She hoped the effect was not ruined by the wet squelching of her pussy juices smooshing against her thighs."
    s "I'm... I want those lundils... so... 'cause I want- want them... I'm... a pig... orc fuck pig..."
    "Her tongue did a lap over her top lip quickly, before she could stop herself."
    $ hentai_scene(1)
    trag "And how you write that in human?"
    $ hentai_scene(3)
    s "I... huh? Sorry... I... I'm confused..."
    $ hentai_scene(1)
    trag "Simple question. How you write 'pig' and 'cow' in human. Show Trag, so he can write it on you. Trag thinks Sabia needs to show everyone what she is, hah!"
    "Yeralg and their friend roared their agreement, banging the table with their fists."
    $ hentai_scene(3)
    s "I... mmmg..."
    "Sabia whimpered, moaning loudly as she rolled her hips back and leaned forward, palpably desperate to keep trying to rub her legs together now."
    s "Okay..."
    $ hentai_scene(2)
    "Panting, she showed them how to write it."
    "How to write insults, that they were going to mark on her body."
    "That thought caught her breath, and she gasped audibly."
    $ hentai_scene(7)
    "One of the orcs leaned over, grinning as he wrote the first word on Sabia."
    $ hentai_scene(8)
    "In careful script, he spelled out 'ORC SLUT' above her tits."
    $ hentai_scene(9)
    s "H-hey! That's not... not what I said! I'm {i}not{/i} an orc slut..."
    trag "Haha, Trag learn that one before Sabia come back tonight... because he know Sabia orc slut."
    $ hentai_scene(8)
    yeralg "Maybe Sabia need 'fuck me' too? So everyone know to just fuck Sabia."
    trag "Good idea! Teach Yeralg that one, Sabia. Maybe if you lucky, we follow your body instructions, hah!"
    "The cold tip of the pen over her skin had been electrifying. The words left behind... marking her like a piece of meat. Slowly, she nodded and showed Yeralg - muttering 'lundilsh' under her breath half-heartedly."
    $ hentai_scene(10)
    trag "Heh, that looks pretty, Sabia. Now everyone knows!"
    yeralg "Well..."
    yeralg "Yeralg and Trag saying before how she a cumdump, right? That needs to be there too. Most important!"
    "The orcs looked at Sabia, and her lip quivered. She showed them how to write it in the human tongue without them needing to ask."
    $ hentai_scene(11)
    yeralg "Good little orc slut cumdump! Haha!"
    "Sabia watched Trag on the other side of the table with heavy, drunk- and lust-laboured breathing. He was rubbing his cock under the table with a satisfied smirk."
    trag "But now Trag and others forget how to write Pig and Cow! Haha, Sabia show again. Unless she not wants the lundils..."
    $ hentai_scene(12)
    "Sabia looked down, the dizzying world still just barely stable enough for her to see all the writing over her skin."
    s "Lun... uhm... do I-"
    "She swallowed, struggling to get her words out."
    trag "Aaargh, fuck!"
    s "Uhm... do I get- when, I mean, 'cause I did... the lundilsh hey... what are you doing...?"
    $ hentai_scene(15)
    "Yeralg and the other orc roared their laughter at Sabia. The table's legs screeched in protest as Trag slammed the mug down in front of Sabia."
    trag "It's another drink, so Sabia doesn't go thirsty, heh! You want lundils, drink up, cumdump. I got some cum, and it needs to be dumped somewhere."
    "His cock was still in his hands, and the tip was dripping into another fresh, empty mug."
    "Trag's loudness had called a few other interested orcs over. They stood next to the table, asking Trag and Yeralg what the words on her body meant."
    $ hentai_scene(16)
    s "HEY! That wasn't- not part of the deal!"
    "She stammered her protest. But only about the mug of cum. The pawing, greedy hands ravishing her emblazoned tits only sent a few shivers of pleasure tingling down her spine."
    $ hentai_scene(17)
    orc "Why you care? Orc slut should be happy to have orc cum to dump in your belly! Hahah! Maybe if you good, Sabia get fucked later."
    $ hentai_scene(18)
    s "But-"
    $ hentai_scene(19)
    s "MMMFG!"
    $ hentai_scene(20)
    "A mouthful of the thick, salty orc cum flooded her mouth. Already speaking, it rushed down her throat and she choked on it, gagging and sputtering."
    $ hentai_scene(21)
    "Even if she wanted to move, the orcs grabbing her tits had a tight enough grip that she was practically pinned there."
    "She whimpered into the slowly rising mug as it kept flowing, and she desperately tried to swallow fast enough to get a breath of air."
    "The thick, sticky warmth of the cum flowed down into her belly. She could feel its warmth spreading out from within her, filling her up like she had just had a meal."
    $ hentai_scene(22)
    s "Eeeennnm!"
    yeralg "Haha, should have put 'cum guzzler' on her instead!"
    "They all snickered at the joke. They gave Sabia's nipples a firm yank before they wrapped a hand around their own cocks, each grabbing a mug."
    "Her nostrils flared as what little breath she had gushed out of her in long, ragged shudders. The cum built up and started to overflow before she began to drink it again, dripping down and coating her chin."
    "The mug tipped up high enough that Sabia didn't see the rest of the orcs preparing more drinks for her."
    $ hentai_scene(23)
    "When it was empty, he slammed it down and Sabia coughed, cum running out her nose in little bubbles that popped and dribbled down over her lip, back into her mouth."
    "At least half of it was painted over her face and tits... and her pussy was absolutely sopping wet and throbbing with desire."
    $ hentai_scene(24)
    s "That's... I must... that should be lotsa... lotsa lundils... right?"
    $ hentai_scene(25)
    yeralg "Haha, don't worry. You fucking cow-tits, cumdump... there's lots of lundils coming just after..."
    $ hentai_scene(26)
    s "Mmnf!"
    "The other orc slapped his hand back onto her. Her nipples were beyond sensitive, her head dizzy with the musk of orc seed, alcohol and lust."
    orc "Yeah... lots! Just after you finish your drinks!"
    $ hentai_scene(27)
    "Several orcs pushed in, slamming down their own mugs full of their cum."
    trag "Well? Get started, you worthless cheating cumdump."
    s "..."
    "Sabia gave a little whimper of trepidation as one of the orcs grabbed the handle on a mug..."
    "It was going to be a long night for Sabia."
    if gallery_workaround == True:
        jump gallery
    return


label v10shaman_ritual:
    play music sex2 fadeout 2.0 fadein 2.0
    $ hentai_scene(1,"v10shaman_ritual",dissolve)
    "Sabia grimaced, looking out at the few orcs that were filing in front outside the tent."
    "She could see Ornshakar's enjoyment as he looked over at her with a wicked smirk etched on his face."
    "The three orcs she had invited had shown up, but Sabia noted that there were a few additional orcs... it seemed Ornshakar had decided three was too few."
    $ hentai_scene(2)
    "Sabia felt their leering eyes on her. It was hard to feel anything else when she was pinned, legs spread and pussy wide on display."
    "She could feel the embarrassment burning within her, but she grit her teeth. She would not let Ornshakar get to her so easily."
    s "You said it would only be three orcs... I can see at least five!"
    $ hentai_scene(3)
    "Sabia looked back towards the small congregation. They all bore smug grins. Ornshakar shook his head."
    $ hentai_scene(4)
    ornshakar "No, no. Ornshakr sent you to invite three orcs. He did not say that only three orcs would be participating. He did not lie, it is still a much smaller and more private ritual than last time."
    ornshakar "Ornshakar believes that all of you have seen or participated in this virility ritual before, but to enlighten our vessel as to the purpose..."
    "Sabia could practically feel the smugness dripping from Ornshakar's words."
    ornshakar "Those warriors who participate will rid themselves of their old seed... allowing the growth of new virility. As Sabia is the reason why the tribe's artifact was... unavailable..."
    ornshakar "She shall serve as the vessel."
    "Ornshakar grunted while nodding at Brug."
    $ hentai_scene(5)
    "Carrying something in his hand that Sabia could not quite see from her upside down vantage, Brug moved closer to her and brought his hand down on her ass with a commanding slap."
    $ hentai_scene(6)
    s "Hey! I agreed to help with your ritual, not to be pawed, groped and slapped at the same time."
    s "Let alone being tied up like this!"
    $ hentai_scene(7)
    "A rumbling of anger spread through the attending orcs."
    "Ornshakar hissed his frustration, red eyes burning with fury."
    ornshakar "You will do as is needed, and you will not interrupt our ritual! Do not forget that you are here because of yourself."
    $ hentai_scene(9)
    "Brug took a step back, before returning quickly."
    $ hentai_scene(10)
    "He bent down over Sabia, his loincloth falling forward and letting his half-hard cock rest on Sabia's bared mound as he pushed the gag in and tied it up."
    $ hentai_scene(11)
    ornshakar "Better. Now the ritual may begin properly."
    s "Mmmrf! MMMGNF!"
    "Sabia struggled against her bonds, trying to protest as Brug pushed something into her ass."
    s "MMMF!"
    "She wriggled, twisting against the shackles but it was pointless. She could do nothing to stop it."
    $ hentai_scene(12)
    "Her ankles next to her head; tits hanging out and bared, spread pussy had been bad enough."
    $ hentai_scene(13)
    "But this was a much worse degree of humiliation. Her hole forced open... unable to move..."
    "Sabia felt far too... {i}exposed{/i}."
    $ hentai_scene(14)
    "She looked away from the looming figure above her as he ran his finger over the rim of her ass."
    s "Nng...!"
    ornshakar "You may begin now."
    $ hentai_scene(15)
    "Brug stepped away, leaving the exposed Sabia in her shackled position as the orcs began to line up."
    "Vekgor ripped his loincloth off as he walked closer to Sabia. His dislike of her was clear, easily read on his face as he began to pump his thick cock."
    $ hentai_scene(16)
    "Sabia expected more jeers and calls from the small congregation as Vekgor's weight slapped down on her ass with a heavy thud."
    "But perhaps she should not have, given the solemnity that most of the orcs had held in the previous ritual."
    $ hentai_scene(17)
    "Vekgor brought his other hand down, shifting his weight. Sabia winced as she felt herself pressed against the floor harder."
    $ hentai_scene(18)
    "She looked away as Vekgor wasted no time, starting to thrust against her spread ass and her bared slit."
    $ hentai_scene(19)
    "It only took a few minutes before she realized Vekgor was ready. A few of his grunts rumbling in the air as he took hold of the base of his length."
    $ hentai_scene(20)
    s "Nnnaahhnf!"
    $ hentai_scene(21)
    "Sabia glared up at Vekgor's smug, satisfied smirk. All the while, she felt the heat of his cum dripping down over her lips... down her ass."
    $ hentai_scene(22)
    "He walked away, making room for the next orc. The odd sensation of her ass being kept open like it was, along with the heat of the cum slowly oozing down her walls, inside... it sent a shiver through her spine."
    "She bit down on the gag, trying to grind her teeth in anger."
    "It was as pointless as trying to break free though."
    $ hentai_scene(24)
    "Another orc moved forward, already at the brink of cumming."
    "Beads of heady orc cum were dripping from the tip of his cock, and it needed only a few moments of attention before he emptied his old seed onto, and inside Sabia."
    $ hentai_scene(25)
    "Most of his load landed over her thighs and midriff... slowly dripping down and threatening to fall onto the bottom of her tits or her face."
    $ hentai_scene(26)
    "The orc made sure to milk the last few drops of the thick stuff onto her ass before he left."
    "Sabia felt the hot, sticky seed starting to cool against her skin... felt the loads dripping into her hole and filling her up."
    $ hentai_scene(27)
    "It seemed like almost two hours passed... a few of the orcs returning for a second, third round."
    "'To properly cleanse themselves of old seed,' Ornshakar had said."
    "All Sabia knew was that it meant her whole body was dripping with viscous orc cum, the smell of sex burning in her nostrils, and the feeling of her ass overflowing with seed."
    $ hentai_scene(28)
    s "..."
    $ hentai_scene(29)
    s "Mmnf..."
    $ hentai_scene(30)
    s "Rrth iizth... oaaavathh?"
    $ hentai_scene(31)
    "Bashnak grabbing her ass with his eager grip answered her muffled question."
    "Not yet."
    "It was not yet over."
    $ hentai_scene(32)
    s "Nmmf!"
    $ hentai_scene(33)
    s "NMNGF! Nnnttt nnnfiiid!"
    $ hentai_scene(34)
    "The orc ignored Sabia's protest, pushing his length into her cum-pool of an ass."
    $ hentai_scene(35)
    "Sabia glared, recognizing that it was Bashnak, the orc who felt she had cheated him in the Red God's Arena."
    "She grimaced about the ball gag, her nose twitching up as cum gushed out from the force of his thrust."
    "It bubbled up and out in a loud, sloppy squelch that everyone could hear."
    $ hentai_scene(36)
    "Bashnak leaned forward, thrusting with his weight and strength."
    "The floor squeaked with every thrust down as Sabia slipped a fraction of an inch, the cum that had managed to not erupt from her ass being forced deeper and deeper inside her."
    $ hentai_scene(37)
    "Half-cooled cum splattered everywhere as he slammed into Sabia, burying his length inside her gaped ass."
    $ hentai_scene(38)
    "Bashnak grunted, his fingers curling slightly, nails dragging across Sabia's skin as he emptied himself in her already overflowing hole."
    "Immediately it began to bubble and squelch up, beginning to ooze down her pussy and her back as she whimpered into her gag."
    $ hentai_scene(39)
    "With a satisfied grunt, Bashnak pulled out, gave his cock a few strokes to eke every drop of seed from it and walked off."
    "Sabia was left there, drenched in several orc's worth of cum, her belly sloshing and feeling bloated with the seed that Bashnak had pounded deeper into her."
    s "Mmmr... rggh?"
    scene bg black with dissolve
    "Ornshakar completed the ritual by speaking for a few minutes, all the while leaving Sabia bound and dripping."
    "When the congregation began to dissipate, Dul and Brug finally came over to unlock Sabia and help her clean up."
    if gallery_workaround == True:
        jump gallery
    return


label v10camp_badend:
    play music sex2 fadeout 2.0 fadein 2.0
    $ hentai_scene(1,"v10camp_badend",dissolve)
    "She wasn't sure how long she had been kept in the camp with Master Grak."
    "Sabia had lost track of time a long while ago..."
    $ hentai_scene(2)
    "The sounds of the orcs rutting into her... it had been humiliating to start with, but it had been so long that she had become deadened to it."
    "Dried cum stuck to her skin, her hair was matted with the stuff."
    "About the only consideration they gave her was taking her out here... away from the camp. But only so that the loads they emptied inside her didn't drip out and mess their camp up."
    $ hentai_scene(3)
    "Sabia choked on the cock, balls against her chin."
    "She was overflowing again... from both ends..."
    "It had become so common... she hated how normal of a day this was. But she could do nothing else other than desperately try to swallow the orc's load down."
    "There would be no other dinner tonight."
    $ hentai_scene(4)
    "...at least she could scoop up whatever oozed from her pussy and clung to her legs..."
    $ hentai_scene(5)
    "Cum bubbled up from her lips, sputtering out. Some of it gushing from her nose, burning the sensitive insides as her nails raked down the orc's legs."
    "It only earned her a snort of laugher."
    scene bg black with dissolve
    "They pulled out, dragging Sabia back to camp by her hair..."
    if gallery_workaround == True:
        jump gallery
    return


label v10neve_scene:
    play music sex1 fadeout 2.0 fadein 2.0
    $ hentai_scene(1,"v10neve_scene",dissolve)
    "Neve settled into position atop Sabia. Her thighs resting against Sabia's breasts and ass wriggling just above Sabia's face."
    $ hentai_scene(2)
    n "If I had known you liked following orders this much, little pet, I would have done this much earlier."
    "Sabia found herself spreading her legs just a little bit more as Neve spoke. Her heart thumped in her chest as lust and desire burned within her."
    "Even so, though..."
    $ hentai_scene(3)
    s "I'm not sure about that pet thing, Neve, it's not-"
    $ hentai_scene(4)
    s "Mmmf!"
    $ hentai_scene(5)
    "Sabia whimpered under Neve's touch. The rough, calloused finger of a warrior rubbing softly against her clit sent shivers through her spine, and she writhed under Neve's weight."
    $ hentai_scene(6)
    n "I really need to teach you better, it seems."
    n "Maybe we should make a routine of this...?"
    "Neve knew her words were falling on half deaf ears as her expert ministrations turned Sabia into a moaning pile of eager flesh underneath her."
    $ hentai_scene(7)
    "Sabia gasped in disappointed as Neve's fingers disappeared, leaving a glistening trail behind."
    $ hentai_scene(8)
    n "If you want more, you have to be a good pet and answer your Mistress. I said, maybe we should make a routine of this to teach you properly."
    "Sabia's breath left her in a long, ragged exhale. Neve's weight on her body, and the dominant words in her ears..."
    $ hentai_scene(9)
    s "Yes, Mistress..."
    $ hentai_scene(10)
    n "Good pet!"
    $ hentai_scene(11)
    "Sabia cried out, gaze flickering to the door and hoping that no one heard."
    "Neve's fingers slipped inside her, thumb attending to her sensitive and desperate button."
    $ hentai_scene(12)
    "Delight and pleasure roiled up from deep within Sabia as she squirmed underneath Neve, rolling her hips against Neve's finger."
    s "Ahnn! Please... please, more!"
    $ hentai_scene(13)
    "Neve gave a wicked grin, slowly pulling her fingers away until just the tips of them were playing lightly on Sabia's outer lips."
    s "...Ne- ...Mistress, please!"
    $ hentai_scene(14)
    n "Mmm... I'm glad you're learning, pet!"
    $ hentai_scene(15)
    "Neve licked her lips, savouring the dominance over the dripping, eager Sabia below."
    n "But it's not about your pleasure. You need to get to work, slave."
    s "Mmmmf!"
    $ hentai_scene(16)
    n "...oh? Do you like that... being my slave?"
    "Sabia could not have answered had she been inclined to do so. Neve's wet slit was pressing on her lips, arousal leaking over Sabia's chin as it dripped down her chin."
    n "Get to work, slave... or I stop."
    s "Mmmf... ggllfk!"
    $ hentai_scene(17)
    "Sabia obeyed. How could she do anything else? She was desperate to have Neve's attention back between her legs... and the sweet taste of Neve was tantalizingly close to her lips."
    $ hentai_scene(18)
    n "Yesss! Good.... mmm, good slave!"
    "Neve's legs twitched, squeezing tighter against Sabia as she felt the eager tongue lapping at her entrance."
    "Sabia's replies were a mix of wet squelches and half-stifled whimpering moans. Her body was burning in lust from Neve's domineering."
    "She wanted to obey, wanted to please Neve. Mistress Neve."
    n "Ah- ahn! Good... you... maybe I should keep you as my permanent... mmmf! Permanent pussy eating slave!"
    $ hentai_scene(19)
    s "Annnghh!"
    $ hentai_scene(20)
    "Sabia's legs spasmed, toes curling and gripping the thick blanket and her pussy convulsing around Neve's expert fingers. She couldn't stop her hips bucking against Neve."
    "She felt Neve's orgasm rocking through the Elven body as well, twitching and writhing, grinding against Sabia's eager, open mouth..."
    "But her thoughts were ajumble, eyes rolling to the back of her head as Neve pressed her weight down harder."
    $ hentai_scene(21)
    "Slowly, Neve pulled away from Sabia."
    s "Ahhh...!"
    "Sabia found herself almost following Neve, craning her neck up to try and keep her tongue inside Neve's depths as the slick juices of her Mistress' orgasm dripped down her features."
    $ hentai_scene(22)
    "Sabia's throat rumbled with moans and satisfied whimpers as Neve's finger continue playing lightly against her dripping nethers all the while."
    $ hentai_scene(23)
    n "..."
    n "Good slave. You know what to say."
    s "...thank you, Mistress!"
    scene bg black with dissolve
    "Neve smiled to herself, pleased, as she pulled herself off Sabia. She gave a light slap to Sabia's slick piussy as she did so, earning a surprised yelp from her pet."
    if gallery_workaround == True:
        jump gallery
    return


label v10neve_scene_dom:
    play music sex1 fadeout 2.0 fadein 2.0
    $ hentai_scene(1,"v10neve_scene",dissolve)
    "Neve settled into position atop Sabia. Her thighs resting against Sabia's breasts and ass wriggling just above Sabia's face."
    $ hentai_scene(2)
    n "If I had known you liked following orders this much, little pet, I would have done this much earlier."
    "Sabia found herself spreading her legs just a little bit more as Neve spoke. Her heart thumped in her chest as lust and desire burned within her. She was enjoying this much more than she had anticipated..."
    $ hentai_scene(3)
    s "I'm not sure about that pet thing, Neve, it's not-"
    $ hentai_scene(4)
    s "Mmmf!"
    $ hentai_scene(5)
    "Sabia whimpered under Neve's touch. The rough, calloused finger of a warrior rubbing softly against her clit sent shivers through her spine, and she writhed under Neve's weight."
    $ hentai_scene(6)
    n "I really need to teach you better, it seems."
    n "Maybe we should make a routine of this...?"
    $ hentai_scene(7)
    "Sabia gasped in disappointed as Neve's fingers disappeared, leaving a glistening trail behind."
    $ hentai_scene(8)
    n "If you want more, you have to be a good pet and answer your Mistress. I said, maybe we should make a routine of this to teach you properly."
    "Sabia's breath left her in a long, ragged exhale. Neve's weight on her body, and the dominant words in her ears..."
    $ hentai_scene(9)
    s "If you're going to keep doing that... maybe, Mistress Neve."
    $ hentai_scene(10)
    n "Good pet!"
    $ hentai_scene(11)
    "Sabia cried out, her legs feet sliding across the floor as she spread herself a little wider, letting Neve take what she wanted."
    "Neve's fingers slipped inside her, thumb attending to her sensitive and desperate button."
    $ hentai_scene(12)
    "Delight and pleasure roiled up from deep within Sabia as she squirmed underneath Neve, rolling her hips against Neve's finger."
    s "Ahnn! More!"
    $ hentai_scene(13)
    "Neve gave a wicked grin, slowly pulling her fingers away until just the tips of them were playing lightly on Sabia's outer lips."
    s "...Ne- ...Mistress, please! Don't leave me there... mmfg!"
    $ hentai_scene(14)
    n "Mmm... I'm glad you're learning, pet!"
    $ hentai_scene(15)
    "Neve licked her lips, savouring the dominance over the dripping, eager Sabia below."
    n "But it's not about your pleasure. You need to get to work, slave."
    $ hentai_scene(16)
    n "Do you like that... being my slave?"
    s "Mmm... it's... quite fun, Mistress Neve. If you keep using your fingers... you might be able to convince me again."
    "Sabia grinned wickedly, running her tongue along the length of her lips with a slow tease."
    n "Get to work, slave... or I stop."
    s "Mmmf..."
    $ hentai_scene(17)
    "Sabia obeyed. How could she do anything else? She was desperate to have Neve's attention back between her legs... and the sweet taste of Neve was tantalizingly close to her lips."
    $ hentai_scene(18)
    n "Yesss! Good.... mmm, good slave!"
    "Neve's legs twitched, squeezing tighter against Sabia as she felt the eager tongue lapping at her entrance."
    "Sabia's replies were a mix of wet squelches and half-stifled whimpering moans. Her body was burning in lust from Neve's domineering."
    "She wanted to bey, wanted to please Neve. Mistress Neve."
    n "Ah- ahn! Good... you... maybe I should keep you as my permanent... mmmf! Permanent pussy eating slave!"
    $ hentai_scene(19)
    s "Annnghh!"
    $ hentai_scene(20)
    "Sabia's legs spasmed, toes curling and gripping the thick blanket and her pussy convulsing around Neve's expert fingers. She couldn't stop her hips bucking against Neve."
    "She felt Neve's orgasm rocking through the Elven body as well, twitching and writhing, grinding against Sabia's eager, open mouth..."
    "But her thoughts were ajumble, eyes rolling to the back of her head as Neve pressed her weight down harder."
    $ hentai_scene(21)
    "Slowly, Neve pulled away from Sabia."
    s "Ahhh...!"
    "Sabia found herself almost following Neve, craning her neck up to try and keep her tongue inside Neve's depths as the slick juices of her Mistress' orgasm dripped down her features."
    $ hentai_scene(22)
    "Sabia's throat rumbled with moans and satisfied whimpers as Neve's finger continue playing lightly against her dripping nethers all the while."
    $ hentai_scene(23)
    n "..."
    n "Good slave. You know what to say."
    s "...thank you, Mistress!"
    scene bg black with dissolve
    "Neve smiled to herself, pleased, as she pulled herself off Sabia. She gave a light slap to Sabia's slick piussy as she did so, earning a surprised yelp from her pet."
    if gallery_workaround == True:
        jump gallery
    return


label v10ranak_cowgirl:
    play music sex1 fadeout 2.0 fadein 2.0
    $ hentai_scene(1,"v10ranak_cowgirl",dissolve)
    "Slowly, Sabia slid until she was stopped by Ranak's eager length. She gave a soft trill of laughter, reaching back with a hand and teasing her own entrance with Ranak's cock."
    s "Be a good boy for me... alright?"
    $ hentai_scene(2)
    "Sabia grinned down at Ranak's flustered features as she sunk back onto his length."
    s "Mmmm...!"
    "Ranak grunted in eagerness, moving to grab hold of Sabia's thighs."
    ranak "Ow fuck!"
    s "No."
    "Sabia slapped his face hard, leaving a sheen of red on his green skin."
    s "No touching."
    "A smirk grew on Sabia's face. Placing both hands on Ranak's chest - her nails scratching lightly - she started to push back and forth."
    "Letting the thick length of orc cock spread her wide, groaning in delight at the feel of being so full."
    "Ranak almost whimpered, grabbing hold of the blanket with fists, clearly desperate to begin to rut into her."
    ranak "..."
    $ hentai_scene(3)
    "Sabia's eyelids fluttered close... moving faster, bouncing on his cock."
    ranak "Argh..."
    "Slowly, she dragged her hand down between her legs, leaving a trail of nail marks across Ranak's chest."
    s "You better not cum before I'm done..."
    "She bit her lip, fingers sliding over her sensitive clit. Her throat rumbled with desire and lust."
    "She leaned forward, letting most of her weight fall to her elbows as they pushed against Ranak's chest."
    $ hentai_scene(4)
    s "Yessss...!"
    "Sabia moaned with abandon, not caring if anyone outside the tent heard as she sped up... the force inside her building. So close to crashing, to breaking..."
    s "Fuck, I'm going... going to-!"
    "Ranak growled in pain. Sabia's nails dug into his flesh, drawing blood as she slammed down on his cock with a heavy thud."
    "Her pleasure had reached a crescendo, roiling over and crashing through her whole being. Her pussy convulsed, squeezing and tightening around Ranak's length in spasms as she came."
    $ hentai_scene(5)
    "Ranak's feet twitched as he found himself unable to stop from cumming, grunting as he pulsed within her."
    "Sabia threw her head back exulting in the sensations, as she ground herself on Ranak's length."
    scene bg black with dissolve
    $ temp = Sabia.armor
    $ Sabia.unequip(Sabia.armor)
    s "..."
    s "Mmm, I'm done."
    "Sabia stood, leaving Ranak's cock twitch, cum dripping down his length."
    scene bg sabiatent
    $ GenericOrc1.extras = ["Loincloth"]
    $ Sabia.face = "happy2"
    show Sabia at left
    show GenericOrc1 at right
    with dissolve
    s "Mmm... good boy. I suppose. Next time I'll have to make sure you don't cum without permission, though."
    $ Sabia.face = "lick1"
    call shake ("h")
    "She smirked, running a finger across his cheek softly before pulling back and giving a quick, firm slap."
    scene bg black with dissolve
    $ Sabia.equip(temp)
    if gallery_workaround == True:
        jump gallery
    return


label v10ranak_mating_press:
    play music sex1 fadeout 2.0 fadein 2.0
    ranak "Wake up, slut. Ranak decided to let you be a lucky human tonight. Get to please some orc cock."
    "Sabia's eyes fluttered open, surprised and shocked at the sight of Ranak's large silhouette looming over her."
    $ hentai_scene(1,"v10ranak_mating_press",dissolve)
    s "Hey! What do you think you're doing?! Get off!"
    $ hentai_scene(2)
    "Ranak snorted his amusement, ignoring what Sabia said as he pushed her legs forward so that her feet were dangling in the air."
    "The tip of his dripping cock was slathering pre-cum over Sabia's entrance as he grinned, leaning forward and running his tongue over her lips."
    s "Get off! This isn't- not why you're here! Get off!"
    "Sabia tried to push the weight of him off in vain. Ranak grunted, grabbing hold of both of her wrists with one hand and pinning them above her head with ease."
    ranak "Dumb human slut. Shut up or someone might hear! Weak race like yours is made for taking orc cock... can't even stop me!"
    s "Please, get off, I-"
    s "Unnnghh!"
    $ hentai_scene(3)
    "Sabia's mouth opened wide as she groaned, and then hung agape as Ranak slammed his length into Sabia's tight hole."
    "He stifled his roar of pleasure as best he could, leaning in and pressing his lips against Sabia's with a hungry, sloppy kiss."
    "Sabia yelped as he pulled out and slammed back in, the sound of his legs and balls slapping against her flesh turned her ears red."
    s "Please, ah - fuck!"
    "Rakan began to pound into Sabia without any care, worried only about his own lust."
    "Faster and harder, his desperate thrusting made Sabia's ass jiggle and her tits heave wildly under his weight."
    "Sabia did her best to bite the whimpering mewls and squeaks that tried to escape from her lips."
    $ hentai_scene(4)
    ranak "Dumb... ugh, useless human cunt!"
    $ hentai_scene(5)
    "Ranak grunted again, burying his length inside Sabia. His balls pressed up against the curves of her ass cheeks as they throbbed, emptying his load."
    s "W- not inside!"
    "Ranak ignored her, intent on pumping her full of cum. Several moments passed before he grunted again, abruptly pulling out."
    "A torrent of cum gushed out of her pussy, running down the curves of her ass as her legs moved back to the ground."
    ranak "Ranak thinks you talk too much, hmph."
    scene bg black with dissolve
    "Ranak gave Sabia's ass a solid slap as he rolled over to go to sleep."
    "Sabia rolled the other way, cum still oozing out of her abused slit, running down to soak into the blanket."
    if gallery_workaround == True:
        jump gallery
    return


label v10ranak_standing:
    play music sex1 fadeout 2.0 fadein 2.0
    "True to his word, Ranak at least made the stripping fast. Sabia's strength wasn't enought to contend with Ranak's, and she was soon naked."
    $ hentai_scene(1,"v10ranak_standing",dissolve)
    "She wriggled in his grip, trying to get away while his cock throbbed against her ass, dripping pre-cum onto her lower back."
    $ hentai_scene(2)
    ranak "Stop wriggling, slut!"
    "Ranak growled his frustrations, reaching out and pinning Sabia's arms with a tight grip on her head."
    s "Let go!"
    ranak "Human bitch."
    s "Ugh, you're getting pre-cum all between my legs!"
    "Sabia grimaced at the wet stickiness as it slathered over her smooth skin."
    ranak "Hmph, that's just a little bit, will be more after Ranak cums."
    $ hentai_scene(3)
    "Without wasting another moment, Ranak started thrusting, rocking his hips back and forth against Sabia's ass, before angling so that it slipped between her thighs."
    "The sound of her cheeks clapping against his crotch quickly filled the room and sent a flourish of red to overtake Sabia's face."
    "He hadn't even bothered to slip inside her, just rutting against her thighs with abandon, her feet barely on the ground, toes just grazing the floor."
    s "..."
    "Sabia's lips quivered as she felt the heat of the thick, hard shaft rubbing against her entrance, her thighs pressing against it."
    "With every thrust more pre-cum beaded at the tip of Ranak's shaft, only to paint against her legs and pussy."
    "It wasn't long before the tent smelled heavy of sweat and sex, Sabia's hair sticking to her forehead and her bouncing, jiggling tits glistening with a sheen of sweat."
    $ hentai_scene(4)
    "Ranak grunted his lust in Sabia's ear as he slammed forward, hard. The sound of Sabia's ass slapping against Ranak filled the tent, drowned out only by the orc's grunting."
    $ hentai_scene(5)
    "His first rope of cum erupted, splattering out over the floor in a wide arc as he shifted his feet, making sure Sabia's legs were tight against his cock."
    ranak "Argh, fuck! Heh... Ranak made you night time snack."
    "His words were ragged as a few more spurts of cum splattered out with much less force. They dripped down his shaft and over his balls."
    "He pulled back from Sabia, dragging his length from between her thighs, leaving a pooling mess of cum to drip down Sabia's legs onto the floor."
    scene bg black with dissolve
    "Ranak sighed."
    $ GenericOrc1.face = "smile3"
    ranak "Hmph. Not bad for human slut. Thighs bit small, not strong like orc."
    "He gave her ass a slap before lying down to sleep, leaving the cum-splattered blanket to Sabia."
    if gallery_workaround == True:
        jump gallery
    return


label v10ranak_bent:
    play music sex1 fadeout 2.0 fadein 2.0
    $ hentai_scene(1,"v10ranak_bent",dissolve)
    "Ignoring Sabia's protests, Ranak grabbed hold of her hair and yanked her over to the wooden bench, and threw her forward."
    $ hentai_scene(2)
    "She barely managed to stick her arms out in time to stop herself from slamming head first into it."
    ranak "Spread more, won't fit Ranak's cock otherwise!"
    "Of course, he didn't really expect Sabia to spread her legs more for him. He just liked saying it. He smirked to himself as he pulled her legs apart with a firm grip."
    s "Do we... do we really have to... to do this now?"
    "Ranak answered with a finger rubbing between her legs, right along her slit."
    ranak "You tell Ranak, slut. Pussy already dripping for orc cock. But since you help Ranak escape, Ranak will be nice."
    ranak "He will still fuck you even if you tell him not to, since he knows you want orc cock inside your cunt."
    "Sabia's fingers curled."
    "It was hard to deny that excitement was coursing through her body... but she didn't want to admit it out loud."
    $ hentai_scene(3)
    "She bit her lip as Ranak wrapped his hands tight around her waist, pushing her forward and letting his heavy cock slap down on her ass."
    s "That's... it's too big!"
    ranak "Nah, Ranak don't think so. Me know that Sabia has fucked orcs before!"
    "While he spoke, he positioned his cock so that it was pressing against Sabia's eager, wet entrance."
    ranak "Mmmf, fuck, Sabia tight!"
    "He licked his lips as he buried himself in Sabia's slit. The force of his thrust sent ripples through her ass and her tits heaved wildly."
    "She slipped a few inches forward on the bench."
    s "Fuck... fuck, fuck!"
    "Sabia whimpered, her legs shuddering and twitching as every thrust sent pleasure piercing into her depths."
    "Grunting, Ranak picked up the pace."
    "Every inch of his cock was slamming into Sabia's sopping pussy, a mix of Ranak's pre-cum and her arousal dripping down onto the floor."
    ranak "Sabia made for orc cock... like every human! Mnng, ugh!"
    $ hentai_scene(4)
    "With every pull out, Ranak's fingers tightened around Sabia's midriff and pulled her back onto his cock, meeting his animalistic rutting."
    $ hentai_scene(5)
    "He growled, leaning forward as he emptied himself in Sabia's tunnel."
    "She bit her lip, toes curling and her knees like jelly as she felt the warmth filling her from within, sure that his cum was filling her womb just as sure as she knew it was bubbling out of her in a viscous mess."
    "Thank Relona at least orcs couldn't impregnate her... or she thought Ranak might be a father..."
    ranak "Hmph. Not bad. At least one thing humans are good for."
    "Ranak snorted in laughter, spitting on the ground and walking off, leaving Sabia clutching the bench as her legs shuddered and her pussy dripped his load out."
    if gallery_workaround == True:
        jump gallery
    return


label v10orcs_dp:
    play music sex1 fadeout 2.0 fadein 2.0
    "Sabia wore a confident, almost eager smile on her face as she walked over to the first orc, squatting down over his midriff, resting her ass on his belly."
    $ hentai_scene(1,"v10orcs_dp",dissolve)
    "Reaching back, she enveloped the orc's length in her fingers with a slow, painful tease that made him whimper in need. Sabia let a cruel chuckle rumble in her throat, before letting the orc push inside."
    "With a beckoning finger, she gave permission to the other orc."
    $ hentai_scene(2)
    s "Ahh! Good... good boys!"
    "The orcs both grunted, starting to push themselves deep into Sabia, urged on by her encouraging words."
    s "Show me what you can, boys. Don't hold back, or I'll send you back to pris- ahhn!"
    s "Fuck!"
    "Both unbelieving of their luck and eager to take advantage of Sabia's offer, both orcs began to rut like desperate animals."
    $ hentai_scene(3)
    "They slammed themselves balls deep with every thrust, burying every inch of their shafts within Sabia's depths."
    s "Hmph... is that, ah! Is that all you two have?!"
    "Sabia's smirk widened as she taunted, nails digging into the orc's leg as she taunted them."
    orc1 "...me can do b-better... ugh!"
    s "Are you... mmf, sure?"
    orc2 "..."
    "Sabia's eyes rolled to the back of her head, mouth open. A long string of spit hung from her lips, swaying from the force of the orcs ravaging her."
    orc2 "Oh... fuck, fuck! Me... me gonna cum!"
    s "...already?"
    $ hentai_scene(4)
    "Sabia moved her hands down to the ground, using it as leverage to thrust back against them. The sound of her ass slapping against them, the balls against her... it filled the room."
    $ hentai_scene(5)
    "The orcs couldn't handle it... they couldn't take it. It was too much for them, and they grunted almost pathetically, hips bucking out wildly as they came inside Sabia."
    s "...oh."
    orc1 "Fuck! Me... me sor- ugh, sorry!"
    orc2 "..."
    s "Hmph."
    scene bg black with dissolve
    "Sabia frowned, pulling herself off the two orcs. Standing over them, she let her holes drip cum down onto them, though a not insignificant amount clung to her legs, oozing down her thighs as well."
    if gallery_workaround == True:
        jump gallery
    return


label v10orcs_doublestand:
    play music sex1 fadeout 2.0 fadein 2.0
    "Sabia's eyelids fluttered open, the words barely registering in her mind."
    orc1 "Don't worry, she wake up after we start."
    "Sabia though, found herself waking up as they dragged her upright."
    $ hentai_scene(1,"v10orcs_doublestand",dissolve)
    "She also found herself quickly without clothes, and two very hard, very thick orc cocks pressing against both of her holes."
    $ hentai_scene(2)
    s "I... can we please not... I mean, maybe not right now, because I was sleeping, and-"
    s "Ahhhn!"
    "Sabia's back arched involuntarily as the orc slipped inside her pussy."
    "She groaned, rolling her back. Her hair brushed against the orc behind her. She felt small in his strong grip."
    s "Ugh, fuck!"
    $ hentai_scene(3)
    "Her quickly hardening nipples brushed against the coarse chest of the orc in front of her as she slumped forward, gritting her teeth as her tight, rear entrance was abruptly invaded."
    orc2 "Hmph... nothing but a moaning slut..."
    "Sabia could do little to argue with the statement. She was rolling her hips, desperately trying to match the thrusting orcs."
    "Lust was clouding her mind, the feeling of being taken in her own tent... by the orcs she had broken out of prison."
    "She knew she should be humiliated, embarrassed... but instead..."
    s "Mmmnh!"
    "She groaned, arching her back more, sticking her ass out and slamming back. The sounds of flesh against flesh filled the tent, and in her desire-riddled hazy mind she had the briefest thought that people might hear."
    orc1 "The little whore loves it! Hmph. Always knew Sabia was a worthless, cock-craving bitch."
    "Sabia bit her lip. She wanted to tell them no. Tell them fuck off."
    "She knew she should..."
    $ hentai_scene(4)
    s "Ahhhn!"
    $ hentai_scene(5)
    "But instead she let them speak, insult her as they cummed, their loads quickly starting to drip down out of her abused entrances... down her thighs and her legs."
    "Onto the floor... drip, drip, drip."
    "They left her there, ignoring her as they moved to go to sleep."
    "Sabia fell to the ground, a puddle of their cum quickly pooling under her, sticking to her legs and feet."
    "...she would have to clean up before the morning."
    if gallery_workaround == True:
        jump gallery
    return


label v10orcs_dp_sub:
    play music sex1 fadeout 2.0 fadein 2.0
    "Both of the orcs bellowed a raucous laugh as they moved to either side of Sabia."
    $ Sabia.face = "surprised1"
    "The first orc ripped her clothes off, and the second threw her to the ground before following her."
    $ Sabia.face = "surprised3"
    s "Hey!"
    s "Stop this now!"
    $ Sabia.face = "angry1"
    s "Or I will-"
    $ Sabia.face = "surprised3"
    s "Mmmmf! Argh!"
    "The first orc ignored Sabia's protests, dragging her on top of him with one hand, and with the other positioning his cock at the entrance to Sabia's pussy."
    $ hentai_scene(1,"v10orcs_dp_sub",dissolve)
    "Smirking at the sight of Sabia's ass poking up and out, the second orc quickly got into his own spot, his eager throbbing shaft pressing against Sabia's ass."
    $ hentai_scene(2)
    s "Ah, fuck!"
    "Her next attempt at a protest was silenced by a set of fingers shoved roughly into her mouth. Almost immediately, she felt herself starting to drool with no way to stop."
    "Spit ran down, dripping from her chin and swaying in long ropes as her whole body rocked from the force of the two orcs."
    s "It'sch... 'oo chhh!"
    $ hentai_scene(3)
    "Sabia whimpered about the fingers as the two orcs began to pound her."
    orc1 "Shut up, whore!"
    "Their rutting sped up, slamming into her tight holes with abandon."
    "Sabia groaned, feeling their thick lengths stretching her to her limit... feeling them rubbing against each other through the thin wall within her."
    orc2 "Fuck! Ass... argh, fuck, her ass is too tight!"
    $ hentai_scene(4)
    "Both of the orcs grunted, their thrusts losing their rhythm, devolving into a haphazard rutting as they neared the edge."
    s "Mmnggg...!"
    $ hentai_scene(5)
    "Sabia's breath caught in her throat as she felt both orcs swell up inside her as they erupted, thick hot streams of cum gushing out into her tunnels."
    s "..."
    "The orcs gave a few more thrusts, their balls pulsing against her ass until they were done."
    scene bg black with dissolve
    "Unceremoniously, they pulled out, letting Sabia fall to a heap on her blanket, orc seed oozing from both holes."
    "She would have to clean the blanket... let alone herself."
    if gallery_workaround == True:
        jump gallery
    return


label v10orcs_spitroast:
    play music sex1 fadeout 2.0 fadein 2.0
    orc1 "Time to make Sabia useful."
    orc2 "C'mere, slut."
    "The second orc grunted, reaching down and burying his fingers in her locks of hair, only to wrenched her up and slam her face against his cock."
    $ hentai_scene(1,"v10orcs_spitroast",dissolve)
    "Hands already working, the other orc had quickly stripped Sabia of her clothes, and dug his fingers about her midriff tightly."
    $ hentai_scene(2)
    "Sabia gagged as the cock plunged down her throat."
    "Her fingers spalyed out against the powerful thighs of the orc in front of her, desperate to try and push herself off for a gulp of air."
    "Instead, her lungs burned with the need for it, and she felt her nose bump against the orc, her lips sliding down farther."
    orc1 "Don't make the slut choke out..."
    orc1 "I want to fuck the whore's cunt properly."
    orc2 "..."
    orc2 "You fucking her now. Just go faster."
    "Sabia tapped the orc fervently as she heard that remark... but her efforts were ignored."
    $ hentai_scene(3)
    "She was only rewarded with her tits heaving underneath her as her ass clapped back with a loud slap, her tunnel stretching about the intruding orc."
    s "Mmmnnffgghh!"
    orc2 "Fuck... that's good! Her throat gets real tight when you do that! Do it more!"
    orc1 "I wasn't gonna not do it..."
    "Grinning to each other, the orc's fingers dug into her belly painfully, and she struggled to balance herself on her feet as he started slamming her back and forth, grunting and panting in effort."
    s "NMNNfggGGGH!"
    "Sabia's need for air was growing. She wriggled and squirmed in the grip of the orc, but could not break free."
    "Tears quickly made her face a wet mess, along with pre-cum and spit that splattered out from her lips as she tried for fresh air..."
    $ hentai_scene(4)
    "All the while the sound of her ass slapping against the orc's midriff ringing in her ears..."
    $ hentai_scene(5)
    "Just as she thought she was going to pass out, the orc grunted, his cock dumping a few loads of cum right down into her belly before he pulled out, grinning as he wiped himself off on her hair."
    "Another moment later... and she felt the hot, sticky wetness of cum dribbling down her legs, oozing from her slit."
    scene bg black with dissolve
    "They let her crumple to the floor in a pile of cum-stained, gasping flesh."
    "...Sabia spent a few moments collecting herself before she went and cleaned up."
    if gallery_workaround == True:
        jump gallery
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
