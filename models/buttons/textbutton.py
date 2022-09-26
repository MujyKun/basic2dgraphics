from . import BaseButton
from ..color import Color
from typing import Union, Optional
import pygame


class TextButton(BaseButton):
    def __init__(
        self,
        text,
        font_color: Union[tuple, Color],
        font="Corbel",
        font_size=25,
        *args,
        **kwargs
    ):
        self.text = text
        self.font_size = font_size
        self.font_type = font
        self.font = pygame.font.SysFont(self.font_type, self.font_size, bold=True)

        self.color = (
            font_color if not isinstance(font_color, Color) else font_color.rgb
        )  # text color

        self.font_surface: Optional[pygame.Surface] = None

        super(TextButton, self).__init__(*args, **kwargs)

    def render(self, surface: pygame.surface.Surface):
        """
        Render the button.

        Creates a font surface,
        then creates a surface to hold the background color and font surface,
        then applies it to main surface.

        :param surface: :ref:`pygame.surface.Surface`
            The surface to apply the button to.
        :return:
        """
        if not self.font_surface:
            # create individual surface for the text.
            self.font_surface = self.font.render(self.text, True, self.color)
        if not self.surface:
            # create individual surface for the button.
            self.surface = pygame.Surface(self.font_surface.get_size())

        # Add background color to button surface.
        self.surface.fill(self.background_color)

        # Add text to center of button surface.
        font_surface_center_x, font_surface_center_y = (
            self.font_surface.get_width() // 2,
            self.font_surface.get_height() // 2,
        )
        font_position = (
            (font_surface_center_x - self.surface.get_width() // 2),
            (font_surface_center_y - self.surface.get_height() // 2),
        )
        self.surface.blit(self.font_surface, font_position)

        # add to main surface.
        surface.blit(self.surface, self.position)
