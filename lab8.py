import pygame
pygame.init()

screen = pygame.display.set_mode((640,480))
background = pygame.Surface(screen.get_size())
background.fill((255,255,255))
background.convert()
background2 = background.copy()

ballsurface = pygame.Surface((50,50))
# ballsurface.fill((255,255,255))
ballsurface.set_colorkey((0, 0, 0))

pygame.draw.circle(ballsurface, (,0,0), (25,25), 25)
ballsurface.convert_alpha()

FPS=60
gametime=0.0
clock = pygame.time.Clock()
running = True
dx, dy = 228, 0
ballx , bally = 0, 0
cleanup = True

while (running == True):
    milliseconds = clock.tick(FPS)
    seconds = milliseconds / 1000.0
    gametime = gametime + seconds
    for event in pygame.event.get():
        if (event.type == pygame.QUIT):
            running = False
        elif (event.type == pygame.KEYDOWN):
            if (event.key == pygame.K_ESCAPE):
                running = False
            elif (event.key == pygame.K_0):
                FPS = 1
            elif (event.key == pygame.K_1):
                FPS = 10
            elif (event.key == pygame.K_2):
                FPS = 20
            elif (event.key == pygame.K_3):
                FPS = 30
            elif (event.key == pygame.K_4):
                FPS = 40
            elif (event.key == pygame.K_5):
                FPS = 50
            elif (event.key == pygame.K_6):
                FPS = 60
            elif (event.key == pygame.K_7):
                FPS = 70
            elif (event.key == pygame.K_8):
                FPS = 80
            elif (event.key == pygame.K_9):
                FPS = 90
            elif (event.key == pygame.K_DOWN):
                dx = 0
                dy = 228
            elif (event.key == pygame.K_UP):
                dx = 0
                dy = -228
            elif (event.key == pygame.K_RIGHT):
                dx = 228
                dy = 0
            elif (event.key == pygame.K_LEFT):
                dx = -228
                dy = 0
            elif (event.key == pygame.K_y):
                cleanup = not cleanup
    pygame.display.set_caption("0-9: limit FPS to {}"
                               " (now): {:.2f}".format(FPS, clock.get_fps()))
    if cleanup:
        screen.blit(background, (0, 0))
    if ( (ballx + 50 > 640 and dx == 228) or (ballx < 0 and dx == -228) ):
        dx = dx * (-1)
    elif ( (bally + 50 > 480 and dy == 228) or (bally < 0 and dy == -228)):
        dy = dy * (-1)
    
    ballx = ballx + dx * seconds
    bally = bally + dy * seconds

    screen.blit(ballsurface, ( round (ballx, 0), round (bally,0)))
    pygame.display.flip()

pygame.quit()