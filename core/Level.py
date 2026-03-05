from typing import List

from core.Entity import Entity
from core.EntityFactory import EntityFactory, get_entity
import pygame

class Level:
    def __init__(self, window, name, game_mode):
        self.window = window
        self.name = name
        self.game_mode = game_mode
        self.entity_list: List[Entity] = []
        self.entity_list.extend(get_entity('Level1Bg'))

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            # 2. Desenhar
            for ent in self.entity_list:
                self.window.blit(ent.surf, ent.rect)
                ent.move()
            pygame.display.flip()