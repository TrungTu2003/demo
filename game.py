import pygame
from random import randint

pygame.init()
screen = pygame.display.set_mode((400,600))
pygame.display.set_caption("Game")
running = True
GREEN = (0,200,0)
RED = (255,0,0)
BLACK = (0,0,0)
clock = pygame.time.Clock()
backgroud = GREEN

font = pygame.font.SysFont('sans',30)
text = font.render("RD",True,BLACK)

text_box = text.get_rect() #co 4 gia tri (0,1,2,3)
print(text.get_rect())
random_pos = (50,50)

while running:
	clock.tick(60)
	screen.fill(backgroud)
	mouse_x, mouse_y = pygame.mouse.get_pos()

	pygame.draw.rect(screen,RED,(random_pos[0],random_pos[1],text_box[2],text_box[3]))

	screen.blit(text,(random_pos))

	for event in pygame.event.get():
		if event.type == pygame.MOUSEBUTTONDOWN:
			if event.button == 1:
				if mouse_x>50 and mouse_x<100 and mouse_y>50 and mouse_y<100:
					backgroud = (randint(0,255), randint(0,255), randint(0,255))

		if event.type == pygame.QUIT:
			running = False

	pygame.display.flip()

pygame.quit()