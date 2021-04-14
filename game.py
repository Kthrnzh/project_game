import pygame
import time
import random
import sys

pygame.init()

black     = (  0,   0,   0)   # черный      
blue      = (  0,   0, 255)   # синий       
white     = (255, 255, 255)   # белый       
yellow    = (255, 255,   0)   # желтый   
red       = (255,   0,   0)   # красный    



done=False
clock=pygame.time.Clock()


win = pygame.display.set_mode((320, 500))
screen = pygame.Surface((400, 400))
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


class Menu:
	def __init__(self, punkts = [120, 140, u'Game', (250, 250, 30), (250, 30, 250), 0]):
		self.punkts = punkts
	def render(self, screen, font, num_punkt):
		for i in self.punkts:
			if num_punkt == i[5]:
				screen.blit(font.render(i[2], 1, i[4]), (i[0], i[1]-30))
			else:
				screen.blit(font.render(i[2], 1, i[3]), (i[0], i[1]-30))
	def menu(self):
		done = True

		pygame.mouse.set_visible(True)
		pygame.key.set_repeat(0,0)
		font_menu = pygame.font.SysFont('serif', 50)
		punkt = 0
		while done:
			screen.fill((0,0,0))

			mp = pygame.mouse.get_pos()
			for i in self.punkts:
				if mp[0]>i[0] and mp[0]<i[0]+155 and mp[1]>i[1] and mp[1]<i[1]+50:
					punkt = i[5]
			self.render(screen, font_menu, punkt)

			for e in pygame.event.get():
				if e.type == pygame.QUIT:
					sys.exit()
				if e.type == pygame.KEYDOWN:
					if e.key == pygame.K_RETURN:
						if punkt == 0:
							done = False
						if punkt == 1:
							sys.exit()
					if e.key == pygame.K_ESCAPE:
						sys.exit()
					if e.key == pygame.K_UP:
						if punkt > 0:
							punkt -= 1
					if e.key == pygame.K_DOWN:
						if punkt < len(self.punkts)-1:
							punkt += 1
				if e.type == pygame.MOUSEBUTTONDOWN and e.button == 1:
					if punkt == 0:
						done = False
					if punkt == 1:
						sys.exit()
            
            
			win.blit(screen, (0, 30))
			pygame.display.update()

punkts = [(50, 225, u'Играть', (250, 250, 30), (250, 30, 250), 0),
          (50, 275, u'Выход', (250, 250, 30), (250, 30, 250), 1)]
game = Menu(punkts)
game.menu()


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
		game.menu()
		pygame.key.set_repeat(1,1)
		pygame.mouse.set_visible(False)	
		


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


	fontObj = pygame.font.SysFont('serif', 20)
	strin = 'Количество очков: ' + str(shot)
	text = fontObj.render(strin, True, black, white)

	win.blit(text, (123,1))
	pygame.display.flip()

pygame.quit()
