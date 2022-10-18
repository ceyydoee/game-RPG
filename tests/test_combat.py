import unittest
from rpg.character import charater 
class Test_combat(unittest.TestCase):

    def test_charater_creation(self):
        # creat a new character 
        char1 = charater()
        # test the characters name is "zerk"
        # print(char1.name == "player")
        self.assertEqual(char1.name,"player")

        #load a character from a file
        char2 = charater()
        char2.load_from_json("characters/zerk.json")
        self.assertEqual("zerk",char2.name)