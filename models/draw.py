from dataclasses import dataclass
from . import Color


@dataclass
class DrawCursor:
    """
    Information about the cursor's current drawing selections.

    Attributes
    ----------
    draw_color: :ref:`Color`
        The current draw color.
    draw_size: tuple
        The current amplifier size of the draw tool.
    tool_selected: bool
        Whether a tool/shape is selected.
    """
    draw_color: Color  # color of the cursor drawing.
    draw_size: tuple  # representative size of each drawing.
    tool_selected: bool  # Whether a tool is selected.
