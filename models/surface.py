from dataclasses import dataclass
from typing import List, Union
from pygame import Surface
from . import draw_cursor


@dataclass
class PersistentSurface:
    """
    A surface that should remain persistent on a canvas.

    Attributes
    ----------
    surface: :ref:`pygame.Surface`
        The surface that will remain persistent.
    position: tuple
        The position of the surface.

    """
    surface: Surface
    position: tuple


@dataclass
class PersistentShape:
    """
    A surface that should remain persistent on a canvas.

    Attributes
    ----------
    button: :ref:`ShapeButton`
        The shape button that will remain persistent.
    size: tuple
        The size of the shape
    color: tuple
        The color of the shape
    position: tuple
        The position of the shape.
    """
    button: object
    size: tuple
    color: tuple
    position: tuple

    def draw(self, surface):
        """Draw the shape."""
        self.button.draw(surface, self.size, self.color, self.position)


@dataclass
class PersistentObjects:
    """
    Holds all persistent objects.

    surfaces: List[:ref:`PersistentSurface`]
        The list of persistent surfaces drawn on the canvas.
    shapes: List[:ref:`PersistentShape`]
        The list of persistent shapes drawn on the canvas.
    undone: List[Union[:ref:`PersistentShape`, :ref:`PersistentSurface`]]
        The list of undone objects.
    """
    surfaces: List[PersistentSurface]
    shapes: List[PersistentShape]
    undone: List[Union[PersistentShape, PersistentSurface]]

    def reset(self):
        """Clear the persistent objects."""
        self.undone += self.surfaces
        self.undone += self.shapes
        self.surfaces = []
        self.shapes = []

    def undo(self):
        """Undo the latest persistent object."""
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
        """Redo the latest undo."""
        if not self.undone:
            return

        obj = self.undone[-1]
        del self.undone[-1]
        if isinstance(obj, PersistentSurface):
            self.surfaces.append(obj)
        else:
            self.shapes.append(obj)
