import pygame

from core.Const import ENTITY_SPEED, WIND_WIDTH
from core.Entity import Entity

class Player( Entity):
    def __init__(self, name: str, positon: tuple):
        super().__init__(name, positon)


    def move(self, ):
        pressed_key = pygame.key.get_pressed() #pega o evento de precionar a tecla

        if pressed_key[pygame.K_UP] and self.rect.top > 0:
            self.rect.centery -= ENTITY_SPEED[self.name]
        if  pressed_key[pygame.K_DOWN] and self.rect.bottom <  WIND_WIDTH:
            self.rect.centery += ENTITY_SPEED[self.name]
        if pressed_key[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.centerx -= ENTITY_SPEED[self.name]
        if pressed_key[pygame.K_RIGHT] and self.rect.right < WIND_WIDTH:
            self.rect.centerx += ENTITY_SPEED[self.name]
        pass



