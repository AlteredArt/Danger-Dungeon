import pygame
import constants
from character import Character

pygame.init()

screen = pygame.display.set_mode(
    (constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
pygame.display.set_caption("Danger Dungeon")

# MAINTAIN FRAMERATE
clock = pygame.time.Clock()

# DEFINE PLAYER MOVEMENT SPEED
moving_left = False
moving_right = False
moving_up = False
moving_down = False

# CREATE PLAYER
player = Character(100, 100)


# MAIN GAME LOOP
run = True
while run:

  # CONTROL FRAME
  clock.tick(constants.FPS)
  # CHANGE BACKGROUND COLOR
  screen.fill(constants.BG)

  # CALCULATE PLAYER MOVEWMENT
  dx = 0
  dy = 0
  if moving_right == True:
    dx = 5
  if moving_left == True:
    dx = -5
  if moving_up == True:
    dy = -5
  if moving_down == True:
    dy = 5 
    
  # UPDATE PLAYER POSITION
  player.move(dx, dy)

  # DRAW PLAYER ON SCRREN
  player.draw(screen)

  # EVENT HANDLER
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      run = False
      # TAKE KEYBOARD PRESSES
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_a:
          moving_left = True
        if event.key == pygame.K_d:
          moving_right = True
        if event.key == pygame.K_w:
          moving_up = True
        if event.key == pygame.K_s:
          moving_down = True
        # TAKE KEYBOARD RELEASES
        if event.type == pygame.KEYUP:
          if event.key == pygame.K_a:
            moving_left = False
          if event.key == pygame.K_d:
            moving_right = False
          if event.key == pygame.K_w:
            moving_up = False
          if event.key == pygame.K_s:
            moving_down = False
      

  pygame.display.update()
pygame.quit()