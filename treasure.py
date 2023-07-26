import random

from gem import gem
from jewellery import jewellery
from magic_item import magic_item
from magic_item import type_m_i

class treasure:
    cp = int(0)
    sp = int(0)
    ep = int(0)
    gp = int(0)
    pp = int(0)
    gems = []
    jewellery = []
    magic_items = []

    def __init__(self):
        cp = int(0)
        sp = int(0)
        ep = int(0)
        gp = int(0)
        pp = int(0)
        gems = []
        jewellery = []
        magic_items = []
    
    def __init__(self, t_type):
        if t_type = "A" or t_type = "a":
            if random.randint(1, 100) <= 25:
                self.cp = random.randint(1, 6) * 1000
            if random.randint(1, 100) <= 30:
                self.sp = random.randint(1, 6) * 1000
            if random.randint(1, 100) <= 20:
                self.ep = random.randint(1, 4) * 1000
            if random.randint(1, 100) <= 35:
                self.gp = (random.randint(1, 6) + random.randint(1, 6)) * 1000
            if random.randint(1, 100) <= 25:
                self.pp = random.randint(1, 2) * 1000
            if random.randint(1, 100) <= 50:
                num_g = random.randint(1, 6) + random.randint(1, 6) + random.randint(1, 6) + random.randint(1, 6) + random.randint(1, 6) + random.randint(1, 6)
                for i in range(0, num_g):
                    gems.append(gem())
            if random.randint(1, 100) <= 50:
                num_jewellery = random.randint(1, 6) + random.randint(1, 6) + random.randint(1, 6) + random.randint(1, 6) + random.randint(1, 6) + random.randint(1, 6)
                for i in range(0, num_jewellery):
                    jewellery.append(jewellery())
            if random.randint(1, 100) <= 30:
                for i in range(0, 3):
                    magic_items.append(magic_item())
        if t_type = "B" or t_type = "b":
            if random.randint(1, 100) <= 50:
                self.cp = random.randint(1, 8) * 1000
            if random.randint(1, 100) <= 25:
                self.sp = random.randint(1, 6) * 1000
            if random.randint(1, 100) <= 25:
                self.ep = random.randint(1, 4) * 1000
            if random.randint(1, 100) <= 25:
                self.gp = random.randint(1, 3) * 1000
            if random.randint(1, 100) <= 25:
                num_g = random.randint(1, 4)
                for i in range(0, num_g):
                    gems.append(gem())
            if random.randint(1, 100) <= 25:
                num_jewellery = random.randint(1, 6)
                for i in range(0, num_jewellery):
                    jewellery.append(jewellery())
            if random.randint(1, 100) <= 10:
                t_m_i = random.randint(1, 3)
                if t_m_i == 1:
                    magic_items.append(magic_item(type_m_i.SWORD))
                elif t_m_i == 2:
                    magic_items.append(magic_item(type_m_i.ARMOUR_SHIELD))
                else t_m_i == 3:
                    magic_items.append(magic_item(type_m_i.WEAPON))
        if t_type = "C" or t_type = "c":
            if random.randint(1, 100) <= 20:
                self.cp = random.randint(1, 12) * 1000
            if random.randint(1, 100) <= 30:
                self.sp = random.randint(1, 4) * 1000
            if random.randint(1, 100) <= 10:
                self.ep = random.randint(1, 4) * 1000
            if random.randint(1, 100) <= 25:
                num_g = random.randint(1, 4)
                for i in range(0, num_g):
                    gems.append(gem())
            if random.randint(1, 100) <= 25:
                num_jewellery = random.randint(1, 4)
                for i in range(0, num_jewellery):
                    jewellery.append(jewellery())
            if random.randint(1, 100) <= 10:
                for i in range(0, 2):
                    magic_items.append(magic_item())
        if t_type = "D" or t_type = "d":
            if random.randint(1, 100) <= 10:
                self.cp = random.randint(1, 8) * 1000
            if random.randint(1, 100) <= 15:
                self.sp = random.randint(1, 12) * 1000
            if random.randint(1, 100) <= 60:
                self.gp = random.randint(1, 6) * 1000
            if random.randint(1, 100) <= 30:
                num_g = random.randint(1, 8)
                for i in range(0, num_g):
                    gems.append(gem())
            if random.randint(1, 100) <= 30:
                num_jewellery = random.randint(1, 8)
                for i in range(0, num_jewellery):
                    jewellery.append(jewellery())
            if random.randint(1, 100) <= 15:
                for i in range(0, 2):
                    magic_items.append(magic_item())
                magic_items.append(magic_item(type_m_i.POTION))
        if t_type = "E" or t_type = "e":
            if random.randint(1, 100) <= 5:
                self.cp = random.randint(1, 10) * 1000
            if random.randint(1, 100) <= 30:
                self.sp = random.randint(1, 12) * 1000
            if random.randint(1, 100) <= 25:
                self.ep = random.randint(1, 4) * 1000
            if random.randint(1, 100) <= 25:
                self.gp = random.randint(1, 8) * 1000
            if random.randint(1, 100) <= 10:
                num_g = random.randint(1, 10)
                for i in range(0, num_g):
                    gems.append(gem())
            if random.randint(1, 100) <= 10:
                num_jewellery = random.randint(1, 10)
                for i in range(0, num_jewellery):
                    jewellery.append(jewellery())
            if random.randint(1, 100) <= 25: 
                for i in range(0, 3):
                    magic_items.append(magic_item())
                magic_items.append(magic_item(type_m_i.SCROLL_MAP))
        if t_type = "F" or t_type = "f":
            if random.randint(1, 100) <= 10:
                self.sp = (random.randint(1, 10) + random.randint(1, 10)) * 1000
            if random.randint(1, 100) <= 20:
                self.ep = random.randint(1, 8) * 1000
            if random.randint(1, 100) <= 45:
                self.gp = random.randint(1, 12) * 1000
            if random.randint(1, 100) <= 30:
                self.pp = random.randint(1, 3) * 1000
            if random.randint(1, 100) <= 20:
                num_g = random.randint(1, 12) + random.randint(1, 12)
                for i in range(0, num_g):
                    gems.append(gem())
            if random.randint(1, 100) <= 10:
                num_jewellery = random.randint(1, 12)
                for i in range(0, num_jewellery):
                    jewellery.append(jewellery())
            if random.randint(1, 100) <= 30: 
                for i in range(0, 3):
                    magic_items.append(magic_item(type_m_i.NON_WEAPON))
                magic_items.append(magic_item(type_m_i.POTION))
                magic_items.append(magic_item(type_m_i.SCROLL_MAP))
        if t_type = "G" or t_type = "g":
            if random.randint(1, 100) <= 50:
                self.gp = random.randint(1, 4) * 10000
            if random.randint(1, 100) <= 50:
                self.pp = random.randint(1, 6) * 1000
            if random.randint(1, 100) <= 25:
                num_g = random.randint(1, 6) + random.randint(1, 6) + random.randint(1, 6)
                for i in range(0, num_g):
                    gems.append(gem())
            if random.randint(1, 100) <= 25:
                num_j = random.randint(1, 10)
                for i in range(0, num_j):
                    jewellery.append(jewellery())
            if random.randint(1, 100) <= 35:
                for i in range(0, 4):
                    magic_items.append(magic_item())
                magic_items.append(magic_item(type_m_i.SCROLL_MAP))
        if t_type = "H" or t_type = "h":
            if random.randint(1, 100) <= 25:
                self.cp = (random.randint(1, 8) + random.randint(1, 8) + random.randint(1, 6)) * 1000
            if random.randint(1, 100) <= 50:
                self.sp = random.randint(1, 100) * 1000
            if random.randint(1, 100) <= 50:
                self.ep = random.randint(1, 4) * 10000
            if random.randint(1, 100) <= 50:
                self.gp = random.randint(1, 6) * 10000
            if random.randint(1, 100) <= 25:
                self.pp = (random.randint(1, 4) + random.randint(1, 4) + random.randint(1, 4) + random.randint(1, 4) + random.randint(1, 4)) * 1000
            if random.randint(1, 100) <= 50:
                num_g = randint(1, 100)
                for i in range(0, num_g):
                    gems.append(gem())
            if random.randint(1, 100) <= 50:
                num_j = randint(1, 4) * 10
                for i in range(0, num_j):
                    jewellery.append(jewellery())
            if random.randint(1, 100) <= 15:
                for i in range(0, 4):
                    magic_items.append(magic_item())
                magic_items.append(magic_item(type_m_i.POTION))
                magic_items.append(magic_item(type_m_i.SCROLL_MAP))
        if t_type = "I" or t_type = "i":
        if t_type = "J" or t_type = "j":
        if t_type = "K" or t_type = "k":
        if t_type = "L" or t_type = "l":
        if t_type = "M" or t_type = "m":
        if t_type = "N" or t_type = "n":
        if t_type = "O" or t_type = "o":
        if t_type = "P" or t_type = "p":
        if t_type = "Q" or t_type = "q":
        if t_type = "R" or t_type = "r":
        if t_type = "S" or t_type = "s":
        if t_type = "T" or t_type = "t":
        if t_type = "U" or t_type = "u":
        if t_type = "V" or t_type = "v": 
