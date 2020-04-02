



init -999:
    default shop = ""
    default shop_item = ""
    default shop_dialogue = ""
    default shop_page = 0
    default shoptext = []
    default shop_payment = 0
    default shop_currency = "money"
    default shop_setscreen_xy = 10000



init -999 python:



    class Shop(object):
        def __init__(self, shopname, bgimg, owner, ownercharacter, textfile, payment, *inventory):
            self.shopname = shopname
            self.bgimg = bgimg
            self.owner = owner
            self.ownercharacter = ownercharacter
            self.textfile = textfile
            self.payment = [int(payment.split(",")[0]), int(payment.split(",")[1])]
            self.inventory = []
            for i in range(0,len(inventory)):
                if inventory[i].split(",")[2] == "∞":
                    self.inventory.append([globals()[inventory[i].split(",")[0]], int(inventory[i].split(",")[1]), inventory[i].split(",")[2]])
                else:
                    self.inventory.append([globals()[inventory[i].split(",")[0]], int(inventory[i].split(",")[1]), int(inventory[i].split(",")[2])])
            self.dialogue = ""
        
        
        def indexstock(self, what):
            for i in range(0,len(self.inventory)):
                if self.inventory[i][0] == what: return(i)
        
        
        
        def stock(self, what, quantity):
            if what == "All":
                for i in range(0,len(self.inventory)):
                    if self.inventory[i][2] == "∞": 
                        pass
                    elif self.inventory[i][0].oosimg == "None": 
                        pass
                    else:
                        self.inventory[i][2] += quantity
                        if self.inventory[i][2] < 0:
                            self.inventory[i][2] = 0
            else:
                self.inventory[self.indexstock(what)][2] += quantity
                if self.inventory[self.indexstock(what)][2] == "∞": 
                    self.inventory[self.indexstock(what)][2] = 0
                if self.inventory[self.indexstock(what)][2] < 0:
                    self.inventory[self.indexstock(what)][2] = 0
        
        
        
        def reprice(self, what, value):
            if what == "All":
                for i in range(0,len(self.inventory)):
                    self.inventory[i][1] += value
                    if self.inventory[i][1] < 0:
                        self.inventory[i][1] = 0
            else:
                self.inventory[self.indexstock(what)][1] += value
                if self.inventory[self.indexstock(what)][1] < 0:
                    self.inventory[self.indexstock(what)][1] = 0
        
        
        def remove(self, what):
            self.inventory.pop(self.indexstock(what))








    def startshops(filename):
        with renpy.file(filename) as shopslist:
            for line in shopslist:
                line = line.decode("utf-8")
                data = line.rstrip().split("\t")
                if data == "" or data[0][0] == "#": continue
                try: 
                    globals()[data[0]]
                except KeyError: 
                    globals()[data[0]] = Shop(*data[1:])
                else: 
                    globals()[data[0]].shopname = data[1]
                    globals()[data[0]].bgimg = data[2]
                    globals()[data[0]].owner = data[3]
                    globals()[data[0]].ownercharacter = data[4]
                    globals()[data[0]].textfile = data[5]


    def shopbuy():
        global money
        renpy.block_rollback()
        money -= item_buy[1]
        if item_buy[2] != "∞":
            shop.inventory[shop.indexstock(item_buy[0])][2] -= 1
        if shop.inventory[shop.indexstock(item_buy[0])][2] == 0 and item_buy[0].oosimg == "None": 
            shop.inventory.pop(shop.indexstock(item_buy[0]))
        Inventory.add_item(item_buy[0])


    def shopreactions(filename):
        global shoptext
        shoptext[:] = [[],[],[],[],[]]
        j = 0
        with renpy.file(filename) as textlist:
            for line in textlist:
                data = line.rstrip().split("\t")
                if data == '' or data[0][0] == '#': continue
                if data[0] == "welcome": j = 0 
                elif data[0] == "buy": j = 1 
                elif data[0] == "leave": j = 2 
                elif data[0] == "work": j = 3 
                elif data[0] == "hover": j = 4 
                else: continue
                if not any(e[0] == data[1] for e in shoptext[j]):
                    shoptext[j].append([data[1]])
                for i in range(0,len(shoptext[j])):
                    if shoptext[j][i][0] == data[1]:
                        shoptext[j][i].append(data[2])


    def getshopreactions(shop_action):
        global shoptext
        global shop_item
        shop.dialogue = shop_item 
        if shop_action == "welcome":
            if len(shoptext[0]) == 0: 
                shop.dialogue = "Welcome to {}!".format(shop.shopname)
            else:
                shop.dialogue = renpy.random.choice(shoptext[0][0][1:])
        elif shop_action == "shop_buy":
            for i in range(0,len(shoptext[1])):
                if shoptext[1][i][0] == shop_item:
                    shop.dialogue = renpy.random.choice(shoptext[1][i][1:])
            if shop.dialogue == shop_item: 
                shop.dialogue = "Here's your {}. Thanks for buying.".format(shop_item)
        elif shop_action == "leave":
            if len(shoptext[2]) == 0: 
                shop.dialogue = "Thanks for buying at {}. Come again!".format(shop.shopname)
            else:
                shop.dialogue = renpy.random.choice(shoptext[2][0][1:])
        elif shop_action == "shop_hover":
            for i in range(0,len(shoptext[4])):
                if shoptext[4][i][0] == shop_item:
                    shop.dialogue = renpy.random.choice(shoptext[4][i][1:])
            if shop.dialogue == shop_item: 
                shop.dialogue = "What do you want to buy?"


    def shop_work():
        global money
        global shop_text
        global shop
        global Sabia
        if Sabia.stamina < 25:
            shop.dialogue = "Sabia was too tired to work."
        elif money >= 1000:
            shop.dialogue = "Sabia: I have more than I need, I should focus on my objectives."
        else:
            Sabia.stamina -= 25        
            shop_payment = renpy.random.randint(shop.payment[0],shop.payment[1])
            money += shop_payment
            if len(shoptext[3]) == 0: 
                shop.dialogue = "Thank you for assisting us. Here's {} Lundils for your help.".format(shop_payment)
            else:
                shop.dialogue = "{} Here's {} Lundils for your help.".format(renpy.random.choice(shoptext[3][0][1:]),shop_payment)



transform shop_right:
    anchor (0.0,1.0) pos (0.675,1.0)




label openshop(shop):
    $ renpy.block_rollback()
    scene expression shop.bgimg
    $ shop = shop
    $ shop_page = 0
    $ shopreactions("Shop/{}".format(shop.textfile))


    if shop == Orcequipmentshop:
        $ GenericOrc1.face = "smile1"
        $ GenericOrc1.extras = ["Loincloth", "Necklace", "Piercing", "beard2", "Wrap"]

    elif shop == Orcgeneralshop:
        $ GenericOrc1.face = "smile1"
        $ GenericOrc1.extras = ["Loincloth", "Stomach", "Necklace", "Piercing", "Hair"]

    elif shop == Orcclothshop:
        $ GenericOrc2.face = "smile1"
        $ GenericOrc2.extras = ["Loincloth", "Hair", "Strap", "Shoulder", "Wrists", "Beard1"]

    elif shop == Elmyshop:
        $ Elmy.extras = ["arm"]
        $ Elmy.face = "happy1"

    elif shop == ElmyshopEnslaved:
        $ Elmy.extras = ["arm"]
        $ Elmy.face = "angry1"

    elif shop == Aliochshop:
        $ Alioch.face = "happy"


    show expression shop.owner at shop_right
    $ getshopreactions("welcome")
    $ renpy.say(globals()[shop.ownercharacter], "[shop.dialogue]")
    $ shop.dialogue = "What do you want to buy?"
    $ renpy.retain_after_load()
    call screen shop_screen
    $ getshopreactions("leave")
    $ renpy.say(globals()[shop.ownercharacter], "[shop.dialogue]")
    hide expression shop.owner
    return

label setscreen:
    if globals()[shop_currency] >= shop_setscreen_xy:
        $ dom -= 2
        $ sub -= 2
        $ freedom -= 2
        $ slavery -= 2
    return


screen shop_screen:
    if shop.payment[1] != 0:
        imagebutton:
            auto "Shop/buttons/workhere_%s.png"
            align (0.025, 0.025)
            focus_mask True
            hovered SetField(shop, "dialogue", "Want to make a few coins? We're in need of help if you're willing.")
            unhovered SetField(shop, "dialogue", "Want to make a few coins? We're in need of help if you're willing.")
            action Function(shop_work)
    frame:
        align (0.015,0.605)
        xysize (320, 215)
        background None
        text "[shop.dialogue]"
    text "[money]" size 25 align (0.1175,0.925)
    imagebutton:
        auto "Shop/buttons/leaveshop_%s.png"
        align (0.5,1.0)
        focus_mask True
        hovered SetField(shop, "dialogue", "Are you sure you don't need anything else?")
        unhovered SetField(shop, "dialogue", "Are you sure you don't need anything else?")
        action Return
    $ x=365
    $ y=403
    $ shop_nextpage = shop_page + 1
    if shop_nextpage > int(len(shop.inventory)/12):
        $ shop_nextpage = 0

    for i in range(0,len(shop.inventory)):
        if i+1 <= (shop_page+1)*12 and i+1 > shop_page*12:
            button:
                pos (x,y)
                xysize (90,90)
                hover_background "Shop/buttons/highlight.png"
                clicked [Show("item_buy_screen"), SetVariable("item_buy", shop.inventory[i]), Hide("shop_screen"), Hide("item_hover")]
                hovered [SetVariable("shop_item",shop.inventory[i][0].name), Show("item_hover", i=i), Function(getshopreactions,shop_action="shop_hover")]
                unhovered [Hide("item_hover"), SetField(shop, "dialogue", "What do you want to buy?")]
                if shop.inventory[i][2] == 0:
                    background None
                    add shop.inventory[i][0].oosimg size (90,90) align (0.5,0.5)
                else:
                    background None
                    add shop.inventory[i][0].fullimg size (90,90) align (0.5,0.5)
                $ stockamount = shop.inventory[i][2]
                text "{b}[stockamount]{/b}" size 14 anchor (1.0,1.0) align (1.1,1.05)
            $ x+=100
            if x > 665:
                $ x = 365
                $ y += 100

    if len(shop.inventory)>12:
        imagebutton:
            auto "Shop/buttons/nextpage_%s.png"
            align (0.5,0.875)
            focus_mask True
            action [SetVariable('shop_page', shop_nextpage), Show("shop_screen"), SetField(shop, "dialogue", "Keep browsing and try to find something you'd like!")]



screen item_hover(i):
    vbox:
        align (0.022,0.800)
        xysize (320,90)
        text "{}".format(shop.inventory[i][0].name)
        text "{} Lundils".format(shop.inventory[i][1]) color "#E39024"



screen item_buy_screen:
    modal True
    add Solid("#000000E6")
    add "Shop/gui/grad.png" yalign 0.77
    add item_buy[0].fullimg align (0.5,0.15)
    text "[item_buy[0].name]" align (0.5,0.52) size 32
    text "[item_buy[0].description]" align (0.5,0.6)
    text "Cost: {color=#E39024}[item_buy[1]] Lundils{/color}" align (0.5,0.7)
    if money >= item_buy[1] and item_buy[2] > 0:
        imagebutton:
            auto "Shop/buttons/buy_%s.png"
            align (0.43,0.93 )
            focus_mask True
            clicked [SetVariable("shop_item",item_buy[0].name), Hide("item_buy_screen"), Show("shop_screen"), Function(shopbuy), Function(getshopreactions, shop_action="shop_buy")]
        imagebutton auto "Shop/buttons/return_%s.png" align (0.57,0.93) focus_mask True action [Hide("item_buy_screen"), Show("shop_screen"), SetField(shop, "dialogue", "Keep browsing and try to find something you'd like!")]
    elif item_buy[2] <= 0:
        add "Shop/buttons/buy_null.png" align (0.43,0.93)
        imagebutton auto "Shop/buttons/return_%s.png" align (0.57,0.93) focus_mask True action [Hide("item_buy_screen"), Show("shop_screen"), SetField(shop, "dialogue", "Sorry, all gone. I'm hoping to get more soon.")]
        text "Item is out of stock." align (0.5,0.75) color "#FF0000"
    else:
        add "Shop/buttons/buy_null.png" align (0.43,0.93)
        imagebutton auto "Shop/buttons/return_%s.png" align (0.57,0.93) focus_mask True action [Hide("item_buy_screen"), Show("shop_screen"), SetField(shop, "dialogue", "It looks like you don't have enough money. Try something cheaper perhaps?")]
        text "Sabia doesn't have enough money to buy this item." align (0.5,0.75) color "#FF0000"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
