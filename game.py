import pygame
import time
import random

pygame.init()

black     = (  0,   0,   0)   # черный      
blue      = (  0,   0, 255)   # синий       
white     = (255, 255, 255)   # белый       
yellow    = (255, 255,   0)   # желтый   
red       = (255,   0,   0)   # красный    



done=False
clock=pygame.time.Clock()


win = pygame.display.set_mode((320, 500))

pygame.display.set_caption(" CAR VS BLOCKS")

x = 50
y = 50
widht = 40
height = 60
speed = 5

cactus_width = 70
cactus_height = 20

rand = random.uniform(1,3)

if rand < 2:
	cactus_x = 44
elif rand < 3:
	cactus_x = 125
else:
	cactus_x = 206

cactus_y = 10

shot = 0

def draw_cactus():
	global cactus_x, cactus_y, cactus_width, cactus_height, shot
	if cactus_y <= 500:
		win.blit(block,(cactus_x,cactus_y))
		cactus_y += 8
	else:
		shot += 1
		cactus_y = 10
		rand = random.uniform(1,3)

		if rand < 2:
			cactus_x = 44
		elif rand < 3:
			cactus_x = 125
		else:
			cactus_x = 206

x1 = 125
y1 = 10

x2 = 125

fon = pygame.image.load('fon.jpg')
fon1 = pygame.image.load('fon1.jpg')
car = pygame.image.load('car.png')
block = pygame.image.load('block.png')


win.blit(fon,(0,0))
win.blit(car,(x2,353))
run = True
while run:
	pygame.time.delay(90)


	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False

	keys = pygame.key.get_pressed()

	if keys[pygame.K_LEFT] and x2 > 44:
		x2 = x2 - 81
	if keys[pygame.K_RIGHT] and x2 < 206:
		x2 = x2 + 81

	if keys[pygame.K_ESCAPE]:
		paused = True
		while paused:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					run = False

			keys = pygame.key.get_pressed()	
			if keys[pygame.K_RETURN]:
				paused = False	

		pygame.display.update()
		

	win.blit(fon,(0,0))
	win.blit(car,(x2,353))
	draw_cactus()

	if x2 == cactus_x:
		if cactus_y >= 325:
			win.blit(fon1,(0,0))

			fontObj = pygame.font.SysFont('serif', 20)
			fullstrin = 'Количество набранных очков: ' + str(shot)
			text = fontObj.render(fullstrin, True, red, black)

			win.blit(text, (30,250))

			pygame.display.update()

			paused = True
			while paused:
				for event in pygame.event.get():
					if event.type == pygame.QUIT:
						run = False

				keys = pygame.key.get_pressed()	
				if keys[pygame.K_RETURN]:
					paused = False	

			pygame.display.update()

	
    # Тут можно рисовать

	fontObj = pygame.font.SysFont('serif', 20)
	strin = 'Количество очков: ' + str(shot)
	text = fontObj.render(strin, True, black, white)


	#win.blit(fon,(0,0))
	win.blit(text, (123,1))

    # Рисунок появится после обновления экрана
	pygame.display.flip()

pygame.quit()
