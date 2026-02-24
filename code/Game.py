from operator import truediv
import code
from code.Menu import Menu
import pygame


class Game:
    def __init__(self): #construtor
        pygame.init()
        window = pygame.display.set_mode(size=(800, 600))

    def run(self): #metodo
        while True:
            menu = Menu(self.window)
            menu.run()
            pass

          #for event in pygame.event.get():
           #     if event.type == pygame.QUIT:
            #        pygame.quit()
             #       quit()




