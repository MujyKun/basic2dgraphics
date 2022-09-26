from . import ImageButton
import pygame


class ShapeButton(ImageButton):
    def __init__(self, *args, **kwargs):
        super(ShapeButton, self).__init__(*args, **kwargs)

    def run(self):
        return True  # Button is now selected.

    def draw(
        self, main_surface: pygame.Surface, size: tuple, color: tuple, position: tuple
    ):
        """Draw the Shape."""


class SquareButton(ShapeButton):
    def __init__(self, *args, **kwargs):
        super(ShapeButton, self).__init__(*args, **kwargs)

    def draw(self, main_surface, size, color, position):
        """Draw a Square."""
        pygame.draw.rect(main_surface, color, (position, size))


class CircleButton(ShapeButton):
    def __init__(self, *args, **kwargs):
        super(ShapeButton, self).__init__(*args, **kwargs)

    def draw(self, main_surface, size: tuple, color, position):
        """Draw a Circle"""
        pygame.draw.circle(main_surface, color, position, size[0])


class Polygon(ShapeButton):
    def __init__(self, *args, **kwargs):
        super(Polygon, self).__init__(*args, **kwargs)

    def draw(self, main_surface, size: tuple, color, position):
        """Draw a Polygon."""
        cursor_x, cursor_y = position
        size_x, size_y = size

        left_point = (cursor_x - size_x, cursor_y)
        right_point = (cursor_x + size_x, cursor_y)
        self._draw_data(
            main_surface,
            size,
            color,
            points=[left_point, right_point],
            position=position,
        )

    def _draw_data(self, main_surface, size, color, points, position):
        """Draw the data out for the concrete object."""


class TopTriangleButton(Polygon):
    def __init__(self, *args, **kwargs):
        super(TopTriangleButton, self).__init__(*args, **kwargs)

    def _draw_data(self, main_surface, size, color, points, position):
        points.append((position[0], position[1] - size[0]))
        pygame.draw.polygon(main_surface, color, points=points)


class BottomTriangleButton(Polygon):
    def __init__(self, *args, **kwargs):
        super(Polygon, self).__init__(*args, **kwargs)

    def _draw_data(self, main_surface, size, color, points, position):
        points.append((position[0], position[1] + size[0]))
        pygame.draw.polygon(main_surface, color, points=points)


class DownArrowButton(Polygon):
    def __init__(self, *args, **kwargs):
        super(Polygon, self).__init__(*args, **kwargs)

    def _draw_data(self, main_surface, size, color, points, position):
        points.append((position[0], position[1] + size[0]))
        pygame.draw.polygon(main_surface, color, points=points, width=size[0])


class UpArrowButton(Polygon):
    def __init__(self, *args, **kwargs):
        super(Polygon, self).__init__(*args, **kwargs)

    def _draw_data(self, main_surface, size, color, points, position):
        points.append((position[0], position[1] - size[0]))
        pygame.draw.polygon(main_surface, color, points=points, width=size[0])
