from dataclasses import dataclass
from . import Color


@dataclass
class DrawCursor:
    draw_color: Color  # color of the cursor drawing.
    draw_size: tuple  # representative size of each drawing.
    tool_selected: bool  # Whether a tool is selected.
