

init -999 python:



    class Skill(object):
        def __init__(self, objname, name, description, stype, ep, momentum, stance, dtype, formula, variance, text, sfx):
            self.objname = objname
            self.name = name
            self.description = description
            self.stype = stype
            self.ep = int(ep)
            self.momentum = int(momentum)
            self.stance = stance
            self.dtype = dtype
            self.formula = formula
            self.variance = int(variance)
            self.text = text
            self.sfx = sfx








    def startskills(filename):
        with renpy.file(filename) as skillslist:
            for line in skillslist:
                line = line.decode("utf-8")
                data = line.rstrip().split("\t")
                if data == "" or data[0][0] == "#": continue
                try: 
                    globals()[data[0]]
                except KeyError: 
                    globals()[data[0]] = Skill(*data)
                else: 
                    globals()[data[0]].name = data[1]
                    globals()[data[0]].description = data[2]
                    globals()[data[0]].stype = data[3]
                    globals()[data[0]].ep = int(data[4])
                    globals()[data[0]].momentum = int(data[5])
                    globals()[data[0]].stance = data[6]
                    globals()[data[0]].dtype = data[7]
                    globals()[data[0]].formula = data[8]
                    globals()[data[0]].variance = int(data[9])
                    globals()[data[0]].text = data[10]
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
