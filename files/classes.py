class balls:
    def __init__(self, charge, x, y, r):
        self.charge = charge
        self.x = x
        self.y = y
        self.r = r

class charges: 
    slowVal = 2
    def __init__(self, charge, x, y, r, a, dir, c):
        self.charge = charge
        self.x = x
        self.y = y
        self.r = r
        self.a = a
        self.dir = dir
        self.c = c

    def attraction(self, ball):
        if self.dir == "horizontal":
            if self.x <= ball.x:
                self.x += self.a + charges.slowVal
                self.a += 1
            if self.x >= ball.x:
                self.x += self.a - charges.slowVal
                self.a -= 1
        elif self.dir == "vertical":
            if self.y <= ball.y:
                self.y += self.a + charges.slowVal
                self.a += 1
            if self.y >= ball.y:
                self.y += self.a - charges.slowVal
                self.a -= 1
        elif self.dir == "neg":
            if self.y <= ball.y:
                self.y += self.a + charges.slowVal
                self.x += self.a + charges.slowVal
                self.a += 1
            if self.y >= ball.y:
                self.y += self.a - charges.slowVal
                self.x += self.a - charges.slowVal
                self.a -= 1
        elif self.dir == "pos":
            if self.y <= ball.y:
                self.y += self.a + charges.slowVal
                self.x -= self.a + charges.slowVal
                self.a += 1
            if self.y >= ball.y:
                self.y += self.a - charges.slowVal
                self.x -= self.a - charges.slowVal
                self.a -= 1

class dummy:
    def __init__(self, c, x, y, r):
        self.c = c
        self.x = x
        self.y = y
        self.r = r