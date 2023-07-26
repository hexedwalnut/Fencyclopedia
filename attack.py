from dice import dice

class attack:
    times  = int(0)     #how many times can this attack be done
    wep    = str("")    #what it is
    damage = dice("0")     #how much damage does this attack do
    note   = str("")    #optional notes about attack

    def __init__(self):
        self.times = int(0)
        self.wep = str("")
        self.damage = dice()
        self.note = str("")

    def __init__(self, times, wep, damage):
        self.times = times
        self.wep = wep
        self.damage = damage
        self.note = str("")

    def __init__(self, times, wep, damage, note):
        self.times = times
        self.wep = wep
        self.damage = damage
        self.note = note
  
    def get(self):
        if self.note == "":
            return str(self.times) + " x " + str(self.wep) + " " + str(self.damage.get())
        else:
            return str(self.times) + " x " + str(self.wep) + " (" + str(self.damage.get()) + " " + str(self.note) + ")"

class attacks:
    sets = []

    def __init__(self):
        self.att = []

    def __init__(self, atts):
        self.addSet(atts)

    def addSet(self, atts):
        self.sets.append(atts)

    def get(self):
        output = ""
       
        for i in range(0, len(s)):
            a = s[i]
            for j in range (0, len(a)):
                output += a.get()
                if (j + 1) < len(a):
                    output += ", "


        return output.strip()
