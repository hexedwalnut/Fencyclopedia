from enum import Enum
from item import item

class type_m_i(Enum):
    ARMOR_SHIELD = 1
    MISC_ITEM = 2
    POTION = 3
    RING = 4
    ROD_STAFF_WAND = 5
    SCROLL_MAP = 6
    SWORD = 7
    WEAPON = 8
    NON_WEAPON = 9

class magic_item(item):
    def __init__(self):
        pass

    def __init__(self, type_m_i):
        pass

    def get():
        pass
