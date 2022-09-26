from . import ImageButton
import pygame


class ShapeButton(ImageButton):
    """An abstract button for a shape."""
    def __init__(self, *args, **kwargs):
        super(ShapeButton, self).__init__(*args, **kwargs)

    def run(self):
        """Run the button and have it select the button."""
        return True  # Button is now selected.

    def draw(
        self, main_surface: pygame.Surface, size: tuple, color: tuple, position: tuple
    ):
        """Draw the Shape."""


class SquareButton(ShapeButton):
    """Represents a button to draw a square."""
    def __init__(self, *args, **kwargs):
        super(ShapeButton, self).__init__(*args, **kwargs)

    def draw(self, main_surface, size, color, position):
        """Draw a Square."""
        pygame.draw.rect(main_surface, color, (position, size))


class CircleButton(ShapeButton):
    """Represents a button to draw a circle."""
    def __init__(self, *args, **kwargs):
        super(ShapeButton, self).__init__(*args, **kwargs)

    def draw(self, main_surface, size: tuple, color, position):
        """Draw a Circle"""
        pygame.draw.circle(main_surface, color, position, size[0])


class Polygon(ShapeButton):
    """Represents an abstract button to draw a polygon."""
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
    """Represents a button to draw a top triangle."""
    def __init__(self, *args, **kwargs):
        super(TopTriangleButton, self).__init__(*args, **kwargs)

    def _draw_data(self, main_surface, size, color, points, position):
        points.append((position[0], position[1] - size[0]))
        pygame.draw.polygon(main_surface, color, points=points)


class BottomTriangleButton(Polygon):
    """Represents a button to draw a bottom triangle."""
    def __init__(self, *args, **kwargs):
        super(Polygon, self).__init__(*args, **kwargs)

    def _draw_data(self, main_surface, size, color, points, position):
        points.append((position[0], position[1] + size[0]))
        pygame.draw.polygon(main_surface, color, points=points)


class DownArrowButton(Polygon):
    """Represents a button to draw a down arrow."""
    def __init__(self, *args, **kwargs):
        super(Polygon, self).__init__(*args, **kwargs)

    def _draw_data(self, main_surface, size, color, points, position):
        points.append((position[0], position[1] + size[0]))
        pygame.draw.polygon(main_surface, color, points=points, width=size[0])


class UpArrowButton(Polygon):
    """Represents a button to draw an up arrow."""
    def __init__(self, *args, **kwargs):
        super(Polygon, self).__init__(*args, **kwargs)

    def _draw_data(self, main_surface, size, color, points, position):
        points.append((position[0], position[1] - size[0]))
        pygame.draw.polygon(main_surface, color, points=points, width=size[0])
