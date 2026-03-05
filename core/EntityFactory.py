#!/usr/bin/python
# -*- coding: utf-8 -*-
from core.Background import Background
from core.Const import WIND_WIDTH


class EntityFactory:
    pass


def get_entity(entity_name: str, position=(0, 0)):

    if entity_name == 'Level1Bg':

        list_bg = []

        for i in range(0, 7):
            list_bg.append(Background(f'Level1Bg{i}', position))
            list_bg.append(Background(f'Level1Bg{i}', (WIND_WIDTH, 0)))




        return list_bg