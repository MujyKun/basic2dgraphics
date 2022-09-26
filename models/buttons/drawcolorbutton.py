from . import TextButton
from .. import draw_cursor, Color
from typing import Union


class DrawColorButton(TextButton):
    """
    Button to switch colors.
    """
    def __init__(self, color: Union[tuple, Color], *args, **kwargs):
        super(DrawColorButton, self).__init__(*args, **kwargs)
        self.color = color if not isinstance(color, Color) else color.rgb

    def run(self):
        """Set the new color of the cursor."""
        draw_cursor.draw_color.set_rgb(*self.color)
