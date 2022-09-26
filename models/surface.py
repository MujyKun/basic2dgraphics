from dataclasses import dataclass
from typing import List, Union
from pygame import Surface
from . import draw_cursor


@dataclass
class PersistentSurface:
    surface: Surface
    position: tuple


@dataclass
class PersistentShape:
    button: object
    size: tuple
    color: tuple
    position: tuple

    def draw(self, surface):
        self.button.draw(surface, self.size, self.color, self.position)


@dataclass
class PersistentObjects:
    surfaces: List[PersistentSurface]
    shapes: List[PersistentShape]
    undone: List[Union[PersistentShape, PersistentSurface]]

    def reset(self):
        self.undone += self.surfaces
        self.undone += self.shapes
        self.surfaces = []
        self.shapes = []

    def undo(self):
        if not self.surfaces and not self.shapes:
            return

        if draw_cursor.tool_selected:
            try:
                obj = self.shapes[-1]
                del self.shapes[-1]
            except IndexError:
                # User selected a tool without drawing a shape.
                draw_cursor.tool_selected = False
                self.undo()
                draw_cursor.tool_selected = True
                return
        else:
            try:
                obj = self.surfaces[-1]
                del self.surfaces[-1]
            except IndexError:
                # User drew with a shape.
                draw_cursor.tool_selected = True
                self.undo()
                draw_cursor.tool_selected = False
                return

        self.undone.append(obj)

    def redo(self):
        if not self.undone:
            return

        obj = self.undone[-1]
        del self.undone[-1]
        if isinstance(obj, PersistentSurface):
            self.surfaces.append(obj)
        else:
            self.shapes.append(obj)
