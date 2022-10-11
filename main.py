print("parris is awesome")

print("ogga booga")
from rpg.weapons  import weapon 
from rpg.armor import armor 

sword = weapon()
print (sword)
sword.load ("weapons/sword.json")


chainmail= armor()
print (chainmail)
chainmail.load("armor /chainmail.json")


