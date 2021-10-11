class balls:
    def __init__(self, charge, x, y, r):
        self.charge = charge
        self.x = x
        self.y = y
        self.r = r

class charges:
    def __init__(self, charge, x, y, r, a, dir, c):
        self.charge = charge
        self.x = x
        self.y = y
        self.r = r
        self.a = a
        self.dir = dir
        self.c = c

class dummy:
    def __init__(self, c, x, y, r):
        self.c = c
        self.x = x
        self.y = y
        self.r = r