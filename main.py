import pygame

pygame.init()

DISPLAYSURFACE = pygame.display.set_mode([800,600])
FPS_CLOCK = pygame.time.Clock()
while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
    DISPLAYSURFACE.fill((50, 50, 50))
    pygame.draw.rect(DISPLAYSURFACE, (0, 0, 0), (0, 0, 800, 425))
    pygame.draw.arc(DISPLAYSURFACE, (75, 75, 75), (300, 60, 20, 70), -300, 500, 100)
    pygame.draw.arc(DISPLAYSURFACE, (75, 75, 75), (480, 60, 20, 70), -300, 500, 100)
    pygame.draw.circle(DISPLAYSURFACE, (0, 100, 0), (400, 200), 150)
    pygame.draw.circle(DISPLAYSURFACE, (100, 100, 100), (400, 150), 70)
    pygame.draw.circle(DISPLAYSURFACE, (0, 50, 0), (400, 150), 20)
    pygame.draw.circle(DISPLAYSURFACE, (0, 0, 0), (400, 150), 10)
    pygame.draw.circle(DISPLAYSURFACE, (100, 100, 100), (412, 140), 3)
    pygame.draw.arc(DISPLAYSURFACE, (0, 0, 0), (343, 250, 120, 70), -300, 500, 700)
    pygame.draw.circle(DISPLAYSURFACE, (0, 0, 0), (400, 280), 30)
    pygame.draw.rect(DISPLAYSURFACE, (0, 100, 0), (300, 310, 20, 180))
    pygame.draw.rect(DISPLAYSURFACE, (0, 100, 0), (480, 310, 20, 180))
    pygame.draw.arc(DISPLAYSURFACE, (0, 50, 0), (343, 277, 120, 40), -300, 500, 500)
    pygame.draw.rect(DISPLAYSURFACE, (0, 50, 0), (368, 290, 75, 20))
    pygame.draw.rect(DISPLAYSURFACE, (0, 100, 0), (250, 220, 20, 180))
    pygame.draw.rect(DISPLAYSURFACE, (0, 100, 0), (530, 220, 20, 180))

    pygame.display.update()
    FPS_CLOCK.tick(30)
