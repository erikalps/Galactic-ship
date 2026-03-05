#!/usr/bin/python
# -*- coding: utf-8 -*-
from core.Const import WIND_WIDTH, ENTITY_SPEED
from core.Entity import Entity


class Background(Entity):
    def __init__(self, name: str, position: tuple):
        """

        :rtype: None
        """
        super().__init__(name, position)

    def move(self, ):
        self.rect.centerx -= ENTITY_SPEED[self.name]
        if self.rect.centerx <= 0:
            self.rect.left = WIND_WIDTH
        pass


