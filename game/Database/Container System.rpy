

init -999 python:



    class Container(object):
        def __init__(self):
            self.items = []
            self.weapons = []
            self.armors = []
            self.accs = []
            self.recipes = []
            self.keyitems = []
        
        
        def pointer(self, what):
            if what.type == "Item": return(self.items)
            
            elif what.type == "Weapon": return(self.weapons)
            elif what.type == "Offense": return(self.weapons)
            
            elif what.type == "Armor": return(self.armors)
            elif what.type == "Defense": return(self.armors)
            
            elif what.type == "Accessory": return(self.accs)
            
            elif what.type == "Recipe": return(self.recipes)
            
            elif what.type == "Key item": return(self.keyitems)
            elif what.type == "Utility": return(self.keyitems)
        
        
        def indexitem(self, what):
            for i in range(0,len(self.pointer(what))):
                if self.pointer(what)[i][0] == what: return(i)
        
        
        def has_item(self, what, quantity=1):
            if not any(e[0] == what for e in self.pointer(what)): return(0)
            return(self.pointer(what)[self.indexitem(what)][1])
        
        
        def add_item(self, what, quantity=1):
            if self.has_item(what) == 0: self.pointer(what).append([what, 0])
            self.pointer(what)[self.indexitem(what)][1] += quantity
        
        
        def rem_item(self, what, quantity=1):
            self.pointer(what)[self.indexitem(what)][1] -= quantity
            if self.has_item(what) <= 0: self.pointer(what).pop(self.indexitem(what))           





    def startinventories():
        Inventories = ["Inventory", "EnemyInv", "TroopInv"]
        for i in range (0,len(Inventories)):
            try: 
                globals()[Inventories[i]]
            except:
                globals()[Inventories[i]] = Container()
        return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
