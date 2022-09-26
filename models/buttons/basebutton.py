from typing import Union, Optional
import pygame
from models.color import Color


class BaseButton:
    def __init__(
        self,
        relative_surface_position: tuple,
        position: tuple = None,
        background_color: Union[tuple, Color] = None,
        main_surface=None,
    ):
        if not background_color:
            background_color = Color.black()

        self.surface: Optional[pygame.Surface] = None

        self.background_color = (
            background_color
            if not isinstance(background_color, Color)
            else background_color.rgb
        )  # bg color

        self.position = position if position else (0, 0)
        self.relative_position = relative_surface_position

        if main_surface:
            self.render(main_surface)

    def run(self) -> bool:
        """
        Run/Execute the button's tasks.
        """

    def render(self, surface: pygame.surface.Surface):
        """
        Render the button.

        :param surface: :ref:`pygame.surface.Surface`
            The surface to apply the button to.
        """

    def is_touching(self, position, boundary_size=None):
        """
        Determine whether a position is in the region of the button.

        :param position: tuple
            The position to check if it is in range of the button.
        :param boundary_size: tuple
            An amplifier of the position to determine if an entire object fits inside the button.
        """
        min_cursor_x, min_cursor_y = position
        if not boundary_size:
            boundary_size = (1, 1)
        bound_x, bound_y = boundary_size

        max_cursor_x, max_cursor_y = min_cursor_x + bound_x, min_cursor_y + bound_y
        return self._determine_in_range(
            min_cursor_x, min_cursor_y
        ) or self._determine_in_range(max_cursor_x, max_cursor_y)

    def _determine_in_range(self, x, y):
        """Determine if a position is in the range of the button.
        :param x: int
            The x (width) coordinate.
        :param y: int
            The y (height) coordinate.

        """
        pos_x, pos_y = self.position  # the button's applied position on a sub-surface.

        # relative potions to the MAIN surface it is applied on
        rel_pos_x, rel_pos_y = (
            pos_x + self.relative_position[0],
            pos_y + self.relative_position[1],
        )
        rect = self.surface.get_rect()
        if rel_pos_x + rect.width >= x >= rel_pos_x:
            if rel_pos_y + rect.height >= y >= rel_pos_y:
                return True
