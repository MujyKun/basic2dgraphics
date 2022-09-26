from dataclasses import dataclass
from typing import List

import pygame
from pygame import Surface
from . import ShapeButton


@dataclass
class PersistentSurface:
    surface: Surface
    position: tuple


@dataclass
class PersistentShape:
    button: ShapeButton
    size: tuple
    color: tuple
    position: tuple

    def draw(self, surface):
        self.button.draw(surface, self.size, self.color, self.position)


@dataclass
class PersistentObjects:
    surfaces: List[PersistentSurface]
    shapes: List[PersistentShape]

    def reset(self):
        self.surfaces = []
        self.shapes = []
