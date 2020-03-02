# Import the pygame module
import pygame

# Import random for random numbers
import random

# Import pygame.locals for easier access to key coordinates
# Updated to conform to flake8 and black standards
from pygame.locals import (
    RLEACCEL,
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_SPACE,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)
from PIL import Image, ImageDraw, ImageFont
from pdb import pm
import os, time

# Define constants for the screen width and height
SCREEN_WIDTH = 1400
SCREEN_HEIGHT = 600

# Define a player object by extending pygame.sprite.Sprite
# The surface drawn on the screen is now an attribute of 'player'
class Player(pygame.sprite.Sprite):
    def __init__(self, *, points=0):
        super().__init__()
        self.surf = pygame.image.load("jet.bmp").convert_alpha()
        #self.surf.set_colorkey((255, 255, 255), RLEACCEL)
#        self.surf = pygame.Surface((75, 25))
#        self.surf.fill((255, 255, 255))
        self.rect = self.surf.get_rect()
        self.points = points
        self.last_fired = time.time()
                
    # Move the sprite based on user keypresses
    def update(self, pressed_keys):
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -5)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, 5)
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-5, 0)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(5, 0)
        if pressed_keys[K_SPACE]:
            global bullets, all_sprites
            if time.time() - self.last_fired > 0.3:
                self.last_fired = time.time()
                bullet = Bullet(pos = self.rect.center)
                bullets.add(bullet)
                all_sprites.add(bullet)
        # Keep player on the screen
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT
        self.status_bar()
    
    def __repr__(self):
        return super().__repr__() + f'\nPoints: {self.points!r}'
    
    def status_bar(self, size=(100, 45)):
        img = Image.new("RGBA", size, (0,0,0,0))
        draw = ImageDraw.Draw(img)
        draw.text((10,15), repr(self).split('\n')[1], fill=(0,0,0,255))#, font=ImageFont.truetype("/etc/fonts/fonts.conf"))
        draw.text((10,25), f'Highscore: 12', fill = (0,0,0,255))
        bts = img.tobytes('raw', 'RGBA')
        self.surf_status = pygame.image.fromstring(bts, img.size, 'RGBA').convert_alpha()
        
    def kill(self):
        self.highscore #  Touches the highscore property, just to write it if is better than last time
        super().kill()
    
    @property
    def highscore(self):
        def write():
            with open('highscore.txt', 'w') as fout:
                self._highscore = self.points
                fout.write(str(self._highscore))
        try:
            with open('highscore.txt', 'r') as f:
                self._highscore = int(f.read())
                if self.points > self._highscore:
                    write()
        except Exception as e:
            print(e)
            write()
                
        return self._highscore

#            
    


class Bullet(pygame.sprite.Sprite):
    def __init__(self, pos = (200,200)):
        super().__init__()
        self.surf = pygame.image.load("bullet.bmp").convert_alpha()
        self.surf = pygame.transform.scale(self.surf, (50, int(50/self.surf.get_size()[0]*self.surf.get_size()[1])))
        self.rect = self.surf.get_rect(center=pos)
        self.speed = 25
    
    def update(self):
        self.rect.move_ip(self.speed, 0)
        if self.rect.left > SCREEN_WIDTH:
            self.kill()
            

        

        
        

# Define the enemy object by extending pygame.sprite.Sprite
# The surface you 7draw on the screen is now an attribute of 'enemy'
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = pygame.image.load("missile.bmp").convert_alpha()
#        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
#        self.surf = pygame.Surface((20, 10))
#        self.surf.fill((255, 255, 255))
        self.rect = self.surf.get_rect(
            center=(
                random.randint(SCREEN_WIDTH + 20, SCREEN_WIDTH + 100),
                random.randint(0, SCREEN_HEIGHT),
            )
        )
        self.speed = random.randint(5, 13)

    # Move the sprite based on speed
    # Remove the sprite when it passes the left edge of the screen
    def update(self):
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 0:
            self.kill()
            
# Define the cloud object by extending pygame.sprite.Sprite
# Use an image for a better-looking sprite
class Cloud(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
#        self.surf = pygame.Surface((59, 39))
#        self.surf.fill((255, 255, 255))
        self.surf = pygame.image.load("cloud.bmp").convert_alpha()
        #self.surf.set_colorkey((0, 0, 0), RLEACCEL)
        # The starting position is randomly generated
        self.rect = self.surf.get_rect(
            center=(
                random.randint(SCREEN_WIDTH + 20, SCREEN_WIDTH + 100),
                random.randint(0, SCREEN_HEIGHT),
            )
        )

    # Move the cloud based on a constant speed
    # Remove the cloud when it passes the left edge of the screen
    def update(self):
        self.rect.move_ip(-5, 0)
        if self.rect.right < 0:
            self.kill()

# Setup for sounds. Defaults are good.
#pygame.mixer.init()

# Initialize pygame
pygame.init()

# Setup the clock for a decent framerate
clock = pygame.time.Clock()

# Create the screen object
# The size is determined by the constant SCREEN_WIDTH and SCREEN_HEIGHT
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Create a custom event for adding a new enemy
ADDENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(ADDENEMY, 800)
ADDCLOUD = pygame.USEREVENT + 2
pygame.time.set_timer(ADDCLOUD, 1000)
#ADDBULLET= pygame.USEREVENT + 3

# Instantiate player. Right now, this is just a rectangle.
player = Player()

# Create groups to hold enemy sprites and all sprites
# - enemies is used for collision detection and position updates
# - all_sprites is used for rendering
enemies = pygame.sprite.Group()
clouds = pygame.sprite.Group()
bullets = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)

# Variable to keep the main loop running
running = True

# Main loop
while running:
    # for loop through the event queue
    for event in pygame.event.get():
        # Check for KEYDOWN event
        if event.type == KEYDOWN:
            # If the Esc key is pressed, then exit the main loop
            if event.key == K_ESCAPE:
                running = False
        # Check for QUIT event. If QUIT, then set running to false.
        elif event.type == QUIT:
            running = False
    
        # Add a new enemy?
        elif event.type == ADDENEMY:
            # Create the new enemy and add it to sprite groups
            new_enemy = Enemy()
            enemies.add(new_enemy)
            all_sprites.add(new_enemy)
        
        # Add a new cloud?
        elif event.type == ADDCLOUD:
            # Create the new cloud and add it to sprite groups
            new_cloud = Cloud()
            clouds.add(new_cloud)
            all_sprites.add(new_cloud)
    
        #  Add a new bullet
#        elif event.type == ADDBULLET:
#            new_bullet = Bullet()
         
    # Get the set of keys pressed and check for user input
    pressed_keys = pygame.key.get_pressed()

    # Update the player sprite based on user keypresses
    player.update(pressed_keys)
    
    # Update enemy position
    clouds.update()
    enemies.update()
    bullets.update()

    # Fill the screen with sky blue
    screen.fill((135, 206, 250))

    # Draw all sprites
    for entity in all_sprites:
        screen.blit(entity.surf, entity.rect)
        
    # Check if any enemies are hit by bullets
    for bullet in bullets:
        if pygame.sprite.spritecollide(bullet, enemies, False):
            enemy = pygame.sprite.spritecollideany(bullet, enemies)
            player.points += enemy.speed
            bullet.kill()
            enemy.kill()
        
#    for bullet in bullets:
#        for enemy in enemies:
#            if pygame.sprite.spritecollide(bullet, enemy):
#                bullet.kill()
#                enemy.kill()
    
    # Check if any enemies have collided with the player
    if pygame.sprite.spritecollideany(player, enemies):
        # If so, then remove the player and stop the loop
        player.kill()
        running = False

    # Draw the player-->status on the screen
    screen.blit(player.surf_status, (0,0))
#    screen.blit(player.surf2, (0,0))

    # Update the display
    pygame.display.flip()
    
    # Ensure program maintains a rate of 30 frames per second
    clock.tick(30)
    
# Done! Time to quit.
pygame.quit()