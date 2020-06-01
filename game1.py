>>> import pygame
>>> pygame.init()
#(6, 0)
>>> screen = pygame.display.set_mode([800,600])
>>> keepGoing = True
>>> GREEN = (0,255,0)
>>> radius = 50
>>> while keepGoing:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			keepGoing = False
	pygame.draw.circle(screen, GREEN, (100,100), radius)
	pygame.display.update()
	
>>> pygame.quit()
	
>>> import pygame
>>> pygame.init()
#(6, 0)
>>> screen = pygame.display.set_mode([800,600])
>>> keepGoing = True
>>> pic = pygame.image.load("CrazySmile.bmp")
