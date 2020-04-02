import sys
import pygame
import knaeuljagd

N_MIN_OBJEKTE = 10
F_BREITE, F_HOEHE = 1000, 600

pygame.init()
fenster = pygame.display.set_mode((F_BREITE, F_HOEHE))
sprites = pygame.sprite.Group()
katze = knaeuljagd.Katze(F_BREITE, F_HOEHE)
sprites.add(katze)
uhr = pygame.time.Clock()

t_kollision_top = -100
t_kollision_flop = -100

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    n_neue_objekte = N_MIN_OBJEKTE - len(sprites) + katze.punkte // 2

    for i in range(n_neue_objekte):
        sprites.add(knaeuljagd.ZufallsObjekt(F_BREITE, F_HOEHE))

    for sprite in sprites:

        if sprite != katze and pygame.sprite.collide_rect(katze, sprite):
            if sprite.gut:
                katze.punkte += 1
                t_kollision_top = pygame.time.get_ticks()
            else:
                katze.leben -= 1
                t_kollision_flop = pygame.time.get_ticks()
                if katze.leben <= 0:
                    fenster.fill((255, 255, 255))
                    knaeuljagd.text("GAME OVER", fenster, (F_BREITE / 2, F_HOEHE / 2), 50)
                    knaeuljagd.text(str(katze.punkte) + " punkte", fenster, (F_BREITE / 2, F_HOEHE / 2 + 60), 30)
                    pygame.display.flip()
                    pygame.time.wait(1000)
                    pygame.quit()
                    sys.exit()
            sprite.kill()

    if pygame.time.get_ticks() - t_kollision_flop < 100:
        fenster.fill((255, 0, 0))
    elif pygame.time.get_ticks() - t_kollision_top < 100:
        fenster.fill((0, 255, 0))
    else:
        fenster.fill((255, 255, 255))

    sprites.update()
    sprites.draw(fenster)

    knaeuljagd.text("punkte: " + str(katze.punkte), fenster, (F_BREITE - 100, F_HOEHE - 50), 30)
    knaeuljagd.text("leben: " + str(katze.leben), fenster, (80, F_HOEHE - 50), 30)

    pygame.display.flip()
    uhr.tick(30)
