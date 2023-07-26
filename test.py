from attack import *
from dice import *
att = attacks([attack(1, "weapon", dice("1d6"), "or by weapon")])
print(att.get())
