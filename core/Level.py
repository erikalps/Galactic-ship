from idlelib.calltip import get_entity
from typing import List

from pygame import Surface, Rect
from pygame.examples.go_over_there import clock
from pygame.examples.grid import WINDOW_HEIGHT
from pygame.ftfont import Font


from core.Const import COLOR_WHITE, MENU_OPTION
from core.Entity import Entity
from core.EntityFactory import EntityFactory
import pygame

class Level:
    def __init__(self, window, name, game_mode):
        self.timeout = 2000
        self.timeout = 0
        self.window = window
        self.name = name
        self.game_mode = game_mode
        self.entity_list: List[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity(self.name + 'Bg'))
        self.entity_list.append(EntityFactory.get_entity('Player1'))

        if game_mode in[MENU_OPTION[1], MENU_OPTION[2]]:
            self.entity_list.append(EntityFactory.get_entity('Player2'))

    def run(self):
        Clock = pygame.time.Clock()
        running = True
        while running:
            Clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            # 2. Desenhar
            for ent in self.entity_list:
                self.window.blit(ent.surf, ent.rect)
                ent.move()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()


            #printed text

            self.level_text(14, f'Level {self.name} - Time: {self.timeout / 1000:.1f}s', COLOR_WHITE, (10, 5))
            self.level_text(14, f'fps: {clock.get_fps():.0f}', COLOR_WHITE, (10, WINDOW_HEIGHT - 35))
            self.level_text(14, f'entidades: {len(self.entity_list)}', COLOR_WHITE, (10, WINDOW_HEIGHT - 20))

    def level_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans TypeWriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(left=text_pos[0], top=text_pos[1])
        self.window.blit(text_surf, text_rect)


        pygame.display.flip()

        pass