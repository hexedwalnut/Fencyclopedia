from enum import Enum
from Item import item


class TypeMagicItem(Enum):
    ARMOR_SHIELD = 1
    MISC_ITEM = 2
    POTION = 3
    RING = 4
    ROD_STAFF_WAND = 5
    SCROLL_MAP = 6
    SWORD = 7
    WEAPON = 8
    NON_WEAPON = 9


class MagicItem(item):
    def __init__(self):
        super().__init__()
        pass

    def __init__(self, type_m_i):
        super().__init__()
        pass

    def get(self):
        pass
