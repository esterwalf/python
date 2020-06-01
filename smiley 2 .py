Python 3.6.3 (v3.6.3:2c5fed8, Oct  3 2017, 17:26:49) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import pygame
>>> pygame.init()
(6, 0)
>>> screen = pygame.diplay.set_mode([800,600])
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    screen = pygame.diplay.set_mode([800,600])
AttributeError: module 'pygame' has no attribute 'diplay'
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
	pygame.quit()

	
<rect(50, 50, 100, 100)>
Traceback (most recent call last):
  File "<pyshell#8>", line 2, in <module>
    for event in pygame.event.get():
pygame.error: video system not initialized
>>> 
