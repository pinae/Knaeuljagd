import pygame


class Katze(pygame.sprite.Sprite):
    def __init__(self, F_BREITE, F_HOEHE):
        super().__init__()
        self.F_BREITE = F_BREITE
        self.F_HOEHE = F_HOEHE
        self.image = pygame.image.load("katze.png")
        self.rect = self.image.get_rect()
        self.rect.center = (self.F_BREITE / 2, self.F_HOEHE / 2)

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
