import sys, pygame
from pygame.locals import *

# Initialize screen
pygame.init()
size = [width, height] = [600, 400]
screen = pygame.display.set_mode(size)
white = [250, 250, 250]
speed = [8,3]

def main():
	# Background
	background_img = pygame.image.load("background.jpg")
	background = pygame.Surface(screen.get_size())
	background = background.convert()
	background.fill(white)

	# Display text

	font = pygame.font.Font(None, 40)
	text = font.render("Euler's Quest", True, [10,10,10])
	textpos = text.get_rect()
	textpos.centerx = background.get_rect().centerx
	textpos.centery = background.get_rect().centery
	
		

	# Event loop
	while True:
		if textpos.left <= 0 or textpos.right >= width:
			speed[0] = -speed[0]
		if textpos.top <= 0 or textpos.bottom >= height:
			speed[1] = -speed[1]
		screen.blit(background_img, text.get_rect())
		textpos = textpos.move(speed)
		screen.blit(text, textpos)
		pygame.display.update(textpos)
		pygame.time.delay(100)
		for event in pygame.event.get():
			if event.type == QUIT:
				return

	    


if __name__ == '__main__': main()