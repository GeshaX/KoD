

init -999 python:
    class Panel(object):
        def __init__(self, objname, view, actor, expression, armor, mode, *args):
            self.objname = objname
            self.view = view
            self.actor = actor
            self.expression = expression
            self.armor = armor
            self.mode = mode
            self.extras = []
            if args:
                for i in range(0,len(args)):
                    self.extras.append(args[i])
            self.blush = False



    def startpanels():
        globals()["Tpanel"] = Panel("Tpanel", "Torso", "Sabia", "Base 1", "Nude", "Normal")
        globals()["Bpanel"] = Panel("Bpanel", "Butt", "Sabia", "Base 1", "Nude", "Normal")

    def startpanelimages():
        renpy.image("Tpanel", DynamicDisplayable(defpanel, "Tpanel"))
        renpy.image("Bpanel", DynamicDisplayable(defpanel, "Bpanel"))

    def defpanel(st, at, panel):
        panel = globals()[panel]
        layers=[]
        bottomlayers = ["slapmarkleft", "panties"]
        
        layers.append(Solid("#000000CC", xsize=563, ysize=840))
        
        if panel == Tpanel:
            layers.append("Database/Panels/{}/{}/{}.png".format(panel.actor, panel.view, panel.expression))
        
        else:
            layers.append("Database/Panels/{}/{}/Base.png".format(panel.actor, panel.view))
        
        if panel.extras:
            for i in range(0,len(panel.extras)):
                if panel.extras[i] in bottomlayers:
                    layers.append("Database/Panels/{}/{}/{}/{}.png".format(panel.actor, panel.view, panel.armor, panel.extras[i]))
        
        layers.append("Database/Panels/{}/{}/{}/{}.png".format(panel.actor, panel.view, panel.armor, panel.armor))
        
        if panel.extras:
            for i in range(0,len(panel.extras)):
                if panel.extras[i] in bottomlayers:
                    continue
                else:
                    layers.append("Database/Panels/{}/{}/{}/{}.png".format(panel.actor, panel.view, panel.armor, panel.extras[i]))
        
        layers.append("Database/Panels/frame.png")
        
        if panel.blush == True:
            layers.append("Database/Panels/{}/{}/blush.png".format(panel.actor, panel.view))
        
        return Flatten(Fixed (*layers, fit_first=True)), None
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
