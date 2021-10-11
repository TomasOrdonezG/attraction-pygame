#import and initialize
from classes import balls, charges, dummy
import pygame, random
pygame.init()

#create screen/canvas
cnvW, cnvH = 800, 800
canvas = pygame.display.set_mode((cnvW, cnvH))
pygame.display.set_caption("Attraction")

chargeA = []
slowVal = 2

# Assign FPS a value
FPS = 30
FramePerSec = pygame.time.Clock()
frameCount = 0

#create balls
negBall = balls(False, cnvW / 2, cnvH / 2, 5)
posBall = balls(True, cnvW - 300, cnvH / 2, 5)

#create dummy
dummy0 = dummy((255, 255, 170), cnvW / 2, cnvH / 2, 2)
dummy45 = dummy((255, 255, 170), cnvW / 2, cnvH / 2, 2)
dummy90 = dummy((255, 255, 170), cnvW / 2, cnvH / 2, 2)
dummy135 = dummy((255, 255, 170), cnvW / 2, cnvH / 2, 2)

def getColourBall(ball):
    if ball.charge == False:
        return (255, 100, 70)
    elif ball.charge == True:
        return (60, 100, 210)
    elif ball.charge == "rand":
        return ball.c

def drawCirc(CircObj):
    colour = getColourBall(CircObj)
    pygame.draw.circle(canvas, colour, (CircObj.x, CircObj.y), CircObj.r)

def randColour():
    return random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255)

def attraction(charge, ball):
    if charge.dir == "horizontal":
        if charge.x <= ball.x:
            charge.x += charge.a + slowVal
            charge.a += 1
        if charge.x >= ball.x:
            charge.x += charge.a - slowVal
            charge.a -= 1
    elif charge.dir == "vertical":
        if charge.y <= ball.y:
            charge.y += charge.a + slowVal
            charge.a += 1
        if charge.y >= ball.y:
            charge.y += charge.a - slowVal
            charge.a -= 1
    elif charge.dir == "neg":
        if charge.y <= ball.y:
            charge.y += charge.a + slowVal
            charge.x += charge.a + slowVal
            charge.a += 1
        if charge.y >= ball.y:
            charge.y += charge.a - slowVal
            charge.x += charge.a - slowVal
            charge.a -= 1
    elif charge.dir == "pos":
        if charge.y <= ball.y:
            charge.y += charge.a + slowVal
            charge.x -= charge.a + slowVal
            charge.a += 1
        if charge.y >= ball.y:
            charge.y += charge.a - slowVal
            charge.x -= charge.a - slowVal
            charge.a -= 1

def createCharge():
    if (mouseY > ((cnvH / 2) / cnvW * mouseX) + cnvH / 4 and mouseY < ((cnvH / 2) / cnvW * -(mouseX - cnvW)) + cnvH / 4) or (mouseY < ((cnvH / 2) / cnvW * mouseX) + cnvH / 4 and mouseY > ((cnvH / 2) / cnvW * -(mouseX - cnvW)) + cnvH / 4):
        charge = charges("rand", mouseX, cnvH / 2, 5, 1, "horizontal", randColour())
        chargeA.append(charge)
    elif (mouseX > ((cnvH / 2) / cnvW * mouseY) + cnvH / 4 and mouseX < ((cnvH / 2) / cnvW * -(mouseY - cnvW)) + cnvH / 4) or (mouseX < ((cnvH / 2) / cnvW * mouseY) + cnvH / 4 and mouseX > ((cnvH / 2) / cnvW * -(mouseY - cnvW)) + cnvH / 4):
        charge = charges("rand", cnvW / 2, mouseY, 5, 1, "vertical", randColour())
        chargeA.append(charge)
    elif (mouseY > ((cnvH / 2) / cnvW * mouseX) + cnvH / 4 and mouseY < cnvH / (cnvW / 2) * (mouseX - cnvW / 4)) or (mouseY < ((cnvH / 2) / cnvW * mouseX) + cnvH / 4 and mouseY > cnvH / (cnvW / 2) * (mouseX - cnvW / 4)):
        charge = charges("rand", mouseX, dummy135.y + mouseX - cnvH / 2, 5, 1, "neg", randColour())
        chargeA.append(charge)
    elif (-mouseY + cnvH > ((cnvH / 2) / cnvW * mouseX) + cnvH / 4 and -mouseY + cnvH < cnvH / (cnvW / 2) * (mouseX - cnvW / 4)) or -mouseY + cnvH < ((cnvH / 2) / cnvW * mouseX) + cnvH / 4 and -mouseY + cnvH > cnvH / (cnvW / 2) * (mouseX - cnvW / 4):
        charge = charges("rand", mouseX, dummy45.y - mouseX + cnvH / 2, 5, 1, "pos", randColour())
        chargeA.append(charge)

def drawDummy():
    if (mouseY > ((cnvH / 2) / cnvW * mouseX) + cnvH / 4 and mouseY < ((cnvH / 2) / cnvW * -(mouseX - cnvW)) + cnvH / 4) or (mouseY < ((cnvH / 2) / cnvW * mouseX) + cnvH / 4 and mouseY > ((cnvH / 2) / cnvW * -(mouseX - cnvW)) + cnvH / 4):
        #horizontal
        pygame.draw.circle(canvas, dummy0.c, (mouseX, cnvH / 2), dummy0.r)
    elif (mouseX > ((cnvH / 2) / cnvW * mouseY) + cnvH / 4 and mouseX < ((cnvH / 2) / cnvW * -(mouseY - cnvW)) + cnvH / 4) or (mouseX < ((cnvH / 2) / cnvW * mouseY) + cnvH / 4 and mouseX > ((cnvH / 2) / cnvW * -(mouseY - cnvW)) + cnvH / 4):
        #vertical
        pygame.draw.circle(canvas, dummy90.c, (cnvW / 2, mouseY), dummy90.r)
    elif (mouseY > ((cnvH / 2) / cnvW * mouseX) + cnvH / 4 and mouseY < cnvH / (cnvW / 2) * (mouseX - cnvW / 4)) or (mouseY < ((cnvH / 2) / cnvW * mouseX) + cnvH / 4 and mouseY > cnvH / (cnvW / 2) * (mouseX - cnvW / 4)):
        #neg
        pygame.draw.circle(canvas, dummy135.c, (mouseX, dummy135.y + mouseX - cnvH / 2), dummy135.r)
    elif (-mouseY + cnvH > ((cnvH / 2) / cnvW * mouseX) + cnvH / 4 and -mouseY + cnvH < cnvH / (cnvW / 2) * (mouseX - cnvW / 4)) or -mouseY + cnvH < ((cnvH / 2) / cnvW * mouseX) + cnvH / 4 and -mouseY + cnvH > cnvH / (cnvW / 2) * (mouseX - cnvW / 4):
        #pos
        pygame.draw.circle(canvas, dummy45.c, (mouseX, dummy45.y - mouseX + cnvH / 2), dummy45.r)

#Game loop
running = True
while running:
    frameCount += 1
    mouseX, mouseY = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            createCharge()
    
    #BG Colour
    canvas.fill((30, 30, 30))

    #draw dummy charge
    drawDummy()

    #draw circles
    drawCirc(negBall)
    #drawCirc(posBall)
    for x in range(len(chargeA)):
        if chargeA[x].dir == "horizontal" or chargeA[x].dir == "neg":
            #stop detection
            if frameCount % 0.5 == 0:
                pos1 = chargeA[x].x - negBall.x
            if frameCount % 1 == 0:
                pos2 = chargeA[x].x - negBall.x
                if pos1 + pos2 >= 5 or pos1 + pos2 <= -5:
                    drawCirc(chargeA[x])
        elif chargeA[x].dir == "vertical" or chargeA[x].dir == "pos":
            #stop detection
            if frameCount % 0.5 == 0:
                pos1 = chargeA[x].y - negBall.y
            if frameCount % 1 == 0:
                pos2 = chargeA[x].y - negBall.y
                if pos1 + pos2 >= 5 or pos1 + pos2 <= -5:
                    drawCirc(chargeA[x])
        #Attraction
        attraction(chargeA[x], negBall)

    #Update display
    pygame.display.update()
    FramePerSec.tick(FPS)