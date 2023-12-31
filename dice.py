import random


class Roll:
    times = int(0)
    sides = int(0)

    def __init__(self, times, sides):
        self.times = times
        self.sides = sides

    def __repr__(self):
        return "<dice.roll object \"" + str(self.times) + "d" + str(self.sides) + "\">"

    def __str__(self):
        return str(self.times) + "d" + str(self.sides)

    def eval(self):
        result = 0
        for i in range(0, self.times):
            result = random.randint(1, self.sides)
        return result


def tokenize(eq):
    tok = []

    i = 0
    while i < len(eq):
        c = eq[i]
        if c.isnumeric():
            num = ""
            while i < len(eq) and eq[i] != " " and eq[i].isnumeric():
                num += eq[i]
                i += 1
            tok.append(num)
            i -= 1
        elif c == "+" or c == "-" or c == "*" or c == "/":
            tok.append(c)
        elif c == "d":
            times = int(tok.pop())
            num = ""
            i += 1
            while i < len(eq) and eq[i] != " " and eq[i].isnumeric():
                num += eq[i]
                i += 1
            sides = int(num)
            i -= 1
            die = Roll(times, sides)
            tok.append(die)
        elif c == " ":
            pass
        else:
            raise Exception("Invalid character found (", c, ")")
        i += 1
    return tok


class Dice:
    equation = str("")

    def __init__(self, equation):
        self.equation = equation

    def eval(self):
        eq = self.equation
        tok = tokenize(eq)
        return self.parse(tok[1:len(tok)], tok[0])

    def parse(self, tok, cur):
        if isinstance(cur, Roll):
            value = cur.eval()
        elif cur.isnumeric():
            value = float(cur)
        elif cur == "-":
            value = -1 * float(tok[0])
            tok = tok[1:len(tok)]
        else:
            raise Exception("This should be impossible, if not, oh no! (value is off)")

        # base case
        if len(tok) == 0:
            return value

        op = tok[0]
        if op == "+":
            return value + self.parse(tok[2:len(tok)], tok[1])
        if op == "-":
            return value - self.parse(tok[2:len(tok)], tok[1])
        if op == "*":
            return value * self.parse(tok[2:len(tok)], tok[1])
        if op == "/":
            return value / self.parse(tok[2:len(tok)], tok[1])

        raise Exception("This should be impossible, if not, oh no! (operator is off)")

    def get(self):
        return self.equation
