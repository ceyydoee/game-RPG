print("parris is awesome")

print("ogga booga")
from rpg.weapon  import weapon 
from rpg.armor import armor 
from rpg.character import character
from rpg.monster import monster
from rpg.combat import combat 

sword = weapon()
print (sword)
sword.load ("weapons/sword.json")


chainmail= armor()
print (chainmail)
chainmail.load("armor /chainmail.json")



def ply_function():
    print("hi, im the function")
def end_game_function():
    print("Game Over")


zerk= character()
print(zerk)
zerk.load("character/zerk.json")

monster = monster()
monster.name = "skeleton"
monster.hit_p_max = 4
monster.l_d =1
monster.h_d = 4

game = combat({zerk},{monster},ply_function,end_game_function)




# genorator = Genorator()
# new_character = genorator.character()
# print(new_character.hit_p_max,new_character.intel,new_character.race,new_character.p_class)


