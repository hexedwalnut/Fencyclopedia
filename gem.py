import random

class gem:
    g_type = str("")
    value = int(0)

    def __init__(self):
        d20 = random.randint(1, 20)
        d4 = random.randint(1, 4)
        if d20 <= 4:
            types = ["Jasper", "Citrine", "Quartz", "Agate"]
            g_type = types[d4-1]
            value = 10
        elif d20 <= 9:
            types = ["Quartz", "Lapis Lazuli", "Amber", "Opal"]
            g_type = types[d4-1]
            value = 50
        elif d20 <= 15:
            types = ["Aquamarine", "Amethyst", "Turquoise", "Peridot"]
            g_type = types[d4-1]
            value = 100
        elif d20 <= 19:
            d3 = random.randint(1, 3)
            types = ["Ruby", "Emerald", "Sapphire"]
            g_type = types[d3-1]
            value = 500
        else:
            g_type = "Diamond"
            value = 1000

    def get():
        return str(g_type) + " (" + str(value) + ")" 
