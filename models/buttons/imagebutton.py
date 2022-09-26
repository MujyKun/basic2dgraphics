from . import BaseButton
from typing import Optional
import pygame


class ImageButton(BaseButton):
    """Load an image onto the canvas as a button."""
    def __init__(self, image, scale_to: tuple = None, *args, **kwargs):
        self.file_name = image
        self.scale_to: Optional[tuple] = scale_to
        super(ImageButton, self).__init__(*args, **kwargs)

    def render(self, surface: pygame.surface.Surface):
        """
        Render the button.

        Creates an image surface,
        then creates a surface to hold the image,
        then applies it to main surface.

        :param surface: :ref:`pygame.surface.Surface`
            The surface to apply the button to.
        :return:
        """
        if not self.surface:
            # create individual surface for the image.
            self.surface = pygame.image.load(self.file_name)
            if self.scale_to:
                self.surface = pygame.transform.scale(self.surface, self.scale_to)

        # add to main surface.
        surface.blit(self.surface, self.position)
