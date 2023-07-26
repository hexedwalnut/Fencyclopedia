import random

class jewellery:
    value = int(0)

    def __init__(self):
        value = (random.randint(1, 6) + random.randint(1, 6) + random.randint(1, 6)) * 100

    def get():
        return "Jewellery " + str(value)
