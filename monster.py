#imports
from attack import *
from movement import movement
from description import description
from dice import dice

# This class details of the information for a monster in the Old School Essentials (OSE) RPG system.
class monster:
    #ac values
    des_ac = int(-1)
    asc_ac = int(-1)

    #hit dice values
    fixed  = int(-1)     #note: that if fixed is "int(-1)" it does not have a fixed value
    hd     = float(-1.0)
    hd_mod = int(0)
    
    #special abilities 
    asterisk = int(0)

    #attacks
    atts = attacks()

    #saves
    sv_d      = int(-1) #death/poison
    sv_w      = int(-1) #wand
    sv_p      = int(-1) #paralysis/petrification
    sv_b      = int(-1) #breath
    sv_s      = int(-1) #spells/rods/staves
    sv_reason = str("hd") #the reason for the saves

    #movement rate
    mv = movement()

    #alignment
    al = str("N")

    #xp
    xp = float(-1.0)

    #number appearing
    na_dun = dice("1")
    na_wil = dice("1") #note: also number appearing in a lair (in a dungeon)

    #treasure type
    tt = treasure()

    #descriptions
    dess = []

    def __init__(self):
        self.des_ac = int(9)
        self.acs_ac = 19 - self.des_ac

        self.fixed = int(-1)
        self.hd = float(0.5)
        self.hd_mod = int(0)

        self.asterisk = int(0)

        self.att = attacks([attack(1, "weapon", dice("1d6"), "or by weapon")])

        self.set_saves(14, 15, 16, 17, 18, "NH")

        self.mv = movement(120)

        self.al = str("Any, usually Lawful")

        self.xp = self.calc_xp(1)

        self.na_dun = dice("1d4")
        self.na_wil = dice("1d20")

        tt = treasure("u")

    def set_saves(self, d, w, p, b, s, reason):
        self.sv_d = d
        self.sv_w = w
        self.sv_p = p
        self.sv_b = b
        self.sv_s = s
        self.sv_reason = reason

    def calc_xp(self, multiplier):
        value = 0
        if self.hd < 1:
            value = 5 + self.asterisk
        elif self.hd <= 1:
            value = 10 + (self.asterisk * 3)
            if self.hd_mod > 0:
                value += 5 + self.asterisk
        elif self.hd <= 2:
            value = 20 + (self.asterisk * 5)
            if self.hd_mod > 0:
                value += 5 + (self.asterisk * 5)
        elif self.hd <= 3:
            value = 35 + (self.asterisk * 15)
            if self.hd_mod > 0:
                value += 15 + (self.asterisk * 10)
        elif self.hd <= 4:
            value = 75 + (self.asterisk * 50)
            if self.hd_mod > 0:
                value += 50 + (self.asterisk * 25)
        elif self.hd <= 5:
            value = 175 + (self.asterisk * 125)
            if self.hd_mod > 0:
                value += 50 + (self.asterisk * 50)
        elif self.hd <= 6:
            value = 275 + (self.asterisk * 225)
            if self.hd_mod > 0:
                value += 75 + (self.asterisk * 75)
        elif self.hd <= 7:
            value = 450 + (self.asterisk * 400)
        elif self.hd <= 8:
            value = 650 + (self.asterisk * 550)
        elif self.hd <= 10:
            value = 900 + (self.asterisk * 700)
        elif self.hd <= 12:
            value = 1100 + (self.asterisk * 800)
        elif self.hd <= 16:
            value = 1350 + (self.asterisk * 950)
        elif self.hd <= 20:
            value = 2000 + (self.asterisk * 1150)
        else:
            value = 2500 + (self.asterisk * 2000)
        return value * multiplier
