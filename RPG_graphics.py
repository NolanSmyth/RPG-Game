import sys, pygame
from pygame.locals import *

movement_speed = 10

# Initialize screen
pygame.init()
size = [width, height] = [800, 600]
screen = pygame.display.set_mode(size)
white = [250, 250, 250]
speed = [8,3]

def main():
	# Background
	background_img = pygame.image.load("background.jpg")
	background = pygame.Surface(screen.get_size())
	background = background.convert()
	# background.fill(white)

	# Display text

	# font = pygame.font.Font(None, 40)
	# text = font.render("Euler's Quest", True, [10,10,10])
	# textpos = text.get_rect()
	# textpos.centerx = background.get_rect().centerx
	# textpos.centery = background.get_rect().centery
	
	# Character Movement
	player = pygame.image.load("ball.png")
	player_pos = Rect(50,50,128,128)
	


	# Event loop
	while True:
		
		# textpos = textpos.move(speed)
		# screen.blit(text, textpos)
		# pygame.display.update(textpos)

		key = pygame.key.get_pressed()
		if key[pygame.K_LEFT]:
			player_pos.left -= movement_speed
		if key[pygame.K_RIGHT]:
			player_pos.left += movement_speed
		if key[pygame.K_UP]:
			player_pos.top -= movement_speed
		if key[pygame.K_DOWN]:
			player_pos.bottom += movement_speed
		pygame.time.delay(30)

		for event in pygame.event.get():
			if event.type == QUIT:
				return

		background.blit(background_img, (0,0))
		background.blit(player,player_pos)
		screen.blit(background,(0,0))
		pygame.display.flip()

	    


if __name__ == '__main__': main()