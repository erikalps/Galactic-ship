import pygame

from code.Menu import Menu

pygame.mixer.pre_init(44100, -16, 1, 512)
pygame.init()


class Game:
    def __init__(self):

        if pygame.mixer.get_init() is None:
            print("Mixer NÃO inicializou")
        else:
            print("Mixer OK:", pygame.mixer.get_init())

        self.window = pygame.display.set_mode((800,600))

    def run(self):
        while True:
            menu = Menu(self.window)
            menu.run()