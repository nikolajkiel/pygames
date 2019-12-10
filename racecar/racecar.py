import pygame
import time
import random
import urllib.request
import io

pygame.init()

display_width = 1920
display_height = 1080

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)

car_width = 73



def url2img(url):
    with urllib.requestst.urlopen(url) as response:
    img = io.BytesIO(response.read())
    return pygame.image.load(img)



gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('A bit Racey')
clock = pygame.time.Clock()

carImg = url2img('https://pythonprogramming.net/static/images/pygame/racecar.png')
penguinImg = [pygame.image.load('penguin.png'), pygame.image.load('penguin_1.png')]

def things_dodged(count):
    font = pygame.font.SysFont(None, 25)
    text = font.render("Dodged: "+str(count), True, black)
    gameDisplay.blit(text,(0,0))

def things(thingx, thingy, thingw, thingh, color):
    pygame.draw.rect(gameDisplay, color, [thingx, thingy, thingw, thingh])

def car(x,y,image=carImg):
    gameDisplay.blit(image,(x,y))

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def things(items,width):
    img = random.choice(penguinImg)
    factor = width/img.get_size()[0]
    size = tuple([int(s*factor) for s in img.get_size()])
    print(size)
    return pygame.transform.scale(img,size)
        
        

def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf',115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)

    pygame.display.update()

    time.sleep(2)

    game_loop()
    
    

def crash():
    message_display('You Crashed')
    
def game_loop():
    x = (display_width * 0.45)
    y = (display_height * 0.8)

    x_change = 0

    thing_startx = random.randrange(0, display_width)
    thing_starty = -600
    thing_speed = 7
    thing_width = 100
    #thing_height = 128
    img = penguinImg[0]
    
    thingCount = 1

    dodged = 0

    gameExit = False

    while not gameExit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -7
                if event.key == pygame.K_RIGHT:
                    x_change = 7

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0

        x += x_change
        gameDisplay.fill( (128,128,0) )

        # things(thingx, thingy, thingw, thingh, color)
        #things(thing_startx, thing_starty, thing_width, thing_height, black)
        car(thing_startx,thing_starty,image=img)
        thing_starty += thing_speed
        car(x,y)
        things_dodged(dodged)
        
        if x > display_width - car_width or x < 0:
            crash()

        if thing_starty > display_height:
            thing_starty = 0 -img.get_height()
            img = things(penguinImg,thing_width)
            thing_startx = random.randrange(0,display_width)
            dodged += 1
            thing_speed += 1
            
            thing_width += (dodged * 1.2)

        ####
        if y < thing_starty+img.get_height():
            print('y crossover')

            if x > thing_startx and x < thing_startx + img.get_width() or x+car_width > thing_startx and x + car_width < thing_startx+img.get_width():
                print('x crossover')
                crash()
        ####
        
        pygame.display.update()
        clock.tick(60)


game_loop()
pygame.quit()
quit()
