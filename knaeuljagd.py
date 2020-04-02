import pygame
import random


class Katze(pygame.sprite.Sprite):
    def __init__(self, F_BREITE, F_HOEHE):
        super().__init__()
        self.F_BREITE = F_BREITE
        self.F_HOEHE = F_HOEHE
        self.image = pygame.image.load("katze.png")
        self.rect = self.image.get_rect()
        self.rect.center = (self.F_BREITE / 2, self.F_HOEHE / 2)
        self.punkte = 0
        self.leben = 7

    def update(self):
        gedrueckt = pygame.key.get_pressed()
        if gedrueckt[pygame.K_UP]:
            self.rect.y -= 8
        if gedrueckt[pygame.K_DOWN]:
            self.rect.y += 8
        if gedrueckt[pygame.K_LEFT]:
            self.rect.x -= 8
        if gedrueckt[pygame.K_RIGHT]:
            self.rect.x += 8
        self.rect.clamp_ip(pygame.Rect(0, 0, self.F_BREITE, self.F_HOEHE))


class ZufallsObjekt(pygame.sprite.Sprite):
    bilder_top = [pygame.image.load("maus.png"),
                  pygame.image.load("falter.png"),
                  pygame.image.load("knaeul.png")]

    bilder_flop = [pygame.image.load("wasser.png"),
                   pygame.image.load("laerm.png"),
                   pygame.image.load("hund.png")]

    def __init__(self, F_BREITE, F_HOEHE):
        super().__init__()
        self.F_BREITE = F_BREITE
        self.F_HOEHE = F_HOEHE

        self.gut = random.choice((True, False))

        if self.gut:
            self.image = random.choice(ZufallsObjekt.bilder_top)
        else:
            self.image = random.choice(ZufallsObjekt.bilder_flop)

        self.rect = self.image.get_rect()

        self.rect.center = (random.randint(0, self.F_BREITE),
                            random.randint(-self.F_HOEHE, -self.rect.height))

        self.x_speed = random.randint(-2, 2)
        self.y_speed = random.randint(1, 5)

    def update(self):
        if self.rect.top > self.F_HOEHE:
            self.kill()
        else:
            self.rect.x += self.x_speed
            self.rect.y += self.y_speed
            if random.randint(0, 120) == 0:
                self.x_speed = random.randint(-2, 2)


def text(text, fenster, position, groesse):
    font = pygame.font.SysFont('arial', groesse)
    text = font.render(text, False, (0, 0, 0))
    F_BREITE = text.get_rect().width
    fenster.blit(text, (position[0] - (F_BREITE / 2), position[1]))
