import pygame
from core.Menu import Menu
from core.Level import Level
from core.Const import MENU_OPTION

class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((800, 600))

    def run(self):
        while True:
            menu = Menu(self.window)
            menu_return = menu.run()

            if menu_return in MENU_OPTION[:3]:
                level = Level(self.window, 'Level1', menu_return)
                level.run() # Você esqueceu de chamar o .run() do nível aqui!

            elif menu_return == MENU_OPTION[4]:
                pygame.quit()
                quit()