
from abc import ABC, abstractmethod
import pygame
import os

class Entity(ABC):
    def __init__(self, name: str, position: tuple):
        self.name = name
        current_dir = os.path.dirname(__file__)
        file_path = os.path.join(current_dir, '..', 'asset', f'{name}.png')
        self.surf = pygame.image.load(file_path).convert_alpha()
        self.rect = self.surf.get_rect(left=position[0], top=position[1])
        self.speed = 0



    @abstractmethod
    def move(self, ):
        pass
