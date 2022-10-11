import json 




class weapon():
    def __init__(self):
        self.name = ""
        self.price = 0
        self.size = 0
        self.damage_low =1
        self.damage_high = 4

def load (self,path):

    with open(path)as f :
        weapons_f = json.load(f)

        pass

    print (weapon)
    self.name = weapon["name"]
    self.price= weapon("price")
    self.weight= weapon("weight ")
    self.size= weapon("size")
    self.L_D= weapon.get ("Damage")[0]
    self.H_D= weapon.get("damage")[1]