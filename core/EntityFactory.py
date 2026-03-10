#!/usr/bin/python
# -*- coding: utf-8 -*-
from symtable import Class

from pygame.examples.grid import WINDOW_HEIGHT

from core.Background import Background
from core.Const import WIND_WIDTH
from core.Player import Player

class EntityFactory:

    @staticmethod

    def get_entity(entity_name: str, position=(0, 0)):

        if entity_name == 'Level1Bg':

            list_bg = []
            for i in range(0, 7):
                list_bg.append(Background(f'Level1Bg{i}', position))
                list_bg.append(Background(f'Level1Bg{i}', (WIND_WIDTH, 0)))

            return list_bg

        if entity_name == 'Player1':
             return Player('Player1', (10, WINDOW_HEIGHT / 2 - 30 ))

        if entity_name == 'Player2':
            return Player('Player2', (10, WINDOW_HEIGHT / 2 + 30))




