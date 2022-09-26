from . import ImageButton
from .. import draw_cursor


class DrawSizeUpButton(ImageButton):
    def __init__(self, *args, **kwargs):
        super(DrawSizeUpButton, self).__init__(*args, **kwargs)

    def run(self):
        x, y = draw_cursor.draw_size
        draw_cursor.draw_size = (x + 1, y + 1)


class DrawSizeDownButton(ImageButton):
    def __init__(self, *args, **kwargs):
        super(DrawSizeDownButton, self).__init__(*args, **kwargs)

    def run(self):
        x, y = draw_cursor.draw_size

        # boundary check
        if x == 1 or y == 1:
            return

        draw_cursor.draw_size = (x - 1, y - 1)
