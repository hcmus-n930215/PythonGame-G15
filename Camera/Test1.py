# code.Pylet - Scrolling Background With Player
# watch the video here - https://youtu.be/AX8YU2hLBUg
# Any questions? Just ask!

import math, random, sys
import pygame
from pygame.locals import *

# exit the program
def events():
	for event in pygame.event.get():
		if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
			pygame.quit()
			sys.exit()

# define display surface			
W, H = 1280, 720
HW, HH = W / 2, H / 2
AREA = W * H

# initialise display
pygame.init()
CLOCK = pygame.time.Clock()
DS = pygame.display.set_mode((W, H))
pygame.display.set_caption("code.Pylet - Scrolling Background with Player")
FPS = 500

# define some colors
BLACK = (0, 0, 0, 255)
WHITE = (255, 255, 255, 255)

bg = pygame.image.load("Background.png")
bg = pygame.transform.scale(bg, (W,H))
lead = pygame.transform.scale(pygame.image.load("rc_lead1.png"), (100,100))
bgWidth, bgHeight = bg.get_rect().size
stageWidth = bgWidth * 3
stagePosX = 0

startScrollingPosX = HW
circleRadius = 25
circlePosX = circleRadius

playerPosX = circleRadius
playerPosY = 585
playerVelocityX = 0
print(stageWidth)
# main loop
while True:

	playerVelocityX = 3
	playerPosX += playerVelocityX
	if playerPosX > stageWidth - 100:
		break
	if playerPosX < 0:
		playerPosX = 100
	if playerPosX < startScrollingPosX:
		circlePosX = playerPosX
	elif playerPosX > stageWidth - startScrollingPosX:
		circlePosX = playerPosX - stageWidth + W
	else:
		circlePosX = startScrollingPosX
		stagePosX += -playerVelocityX
	
	rel_x = stagePosX % bgWidth
	DS.blit(bg, (rel_x - bgWidth, 0))
	DS.blit(bg, (rel_x, 0))
	
	#pygame.draw.circle(DS, WHITE, (int(circlePosX), playerPosY - circleRadius), circleRadius)
	DS.blit(lead, (circlePosX,200))
	pygame.display.update()
	CLOCK.tick(FPS)
	DS.fill(BLACK)
