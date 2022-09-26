from .color import Color
from .draw import DrawCursor

draw_cursor = DrawCursor(Color(0, 0, 0), (25, 25), False)

from .surface import PersistentSurface, PersistentShape, PersistentObjects

persistent_objects = PersistentObjects([], [], [])
from models.buttons import *


def get_color_buttons(main_surface, relative_surface_position: tuple):
    """Get the color buttons."""
    return [
        DrawColorButton(
            Color.black(),
            "Black",
            background_color=Color.black(),
            position=(0, 0),
            main_surface=main_surface,
            font_color=Color.white(),
            relative_surface_position=relative_surface_position,
        ),
        DrawColorButton(
            Color.red(),
            "Red",
            background_color=Color.red(),
            position=(0, 25),
            main_surface=main_surface,
            font_color=Color.white(),
            relative_surface_position=relative_surface_position,
        ),
        DrawColorButton(
            Color.magenta(),
            "Magenta",
            background_color=Color.magenta(),
            position=(0, 50),
            main_surface=main_surface,
            font_color=Color.white(),
            relative_surface_position=relative_surface_position,
        ),
        DrawColorButton(
            Color.lime(),
            "Lime",
            background_color=Color.lime(),
            position=(0, 75),
            main_surface=main_surface,
            font_color=Color.white(),
            relative_surface_position=relative_surface_position,
        ),
        DrawColorButton(
            Color.blue(),
            "Blue",
            background_color=Color.blue(),
            position=(0, 100),
            main_surface=main_surface,
            font_color=Color.white(),
            relative_surface_position=relative_surface_position,
        ),
        DrawColorButton(
            Color.yellow(),
            "Yellow",
            background_color=Color.yellow(),
            position=(0, 125),
            main_surface=main_surface,
            font_color=Color.white(),
            relative_surface_position=relative_surface_position,
        ),
        DrawColorButton(
            Color.cyan(),
            "Cyan",
            background_color=Color.cyan(),
            position=(0, 150),
            main_surface=main_surface,
            font_color=Color.white(),
            relative_surface_position=relative_surface_position,
        ),
        DrawColorButton(
            Color.silver(),
            "Silver",
            background_color=Color.silver(),
            position=(0, 175),
            main_surface=main_surface,
            font_color=Color.white(),
            relative_surface_position=relative_surface_position,
        ),
        DrawColorButton(
            Color.gray(),
            "Gray",
            background_color=Color.gray(),
            position=(0, 200),
            main_surface=main_surface,
            font_color=Color.white(),
            relative_surface_position=relative_surface_position,
        ),
        DrawColorButton(
            Color.maroon(),
            "Maroon",
            background_color=Color.maroon(),
            position=(0, 225),
            main_surface=main_surface,
            font_color=Color.white(),
            relative_surface_position=relative_surface_position,
        ),
        DrawColorButton(
            Color.olive(),
            "Olive",
            background_color=Color.olive(),
            position=(0, 250),
            main_surface=main_surface,
            font_color=Color.white(),
            relative_surface_position=relative_surface_position,
        ),
        DrawColorButton(
            Color.green(),
            "Green",
            background_color=Color.green(),
            position=(0, 275),
            main_surface=main_surface,
            font_color=Color.white(),
            relative_surface_position=relative_surface_position,
        ),
        DrawColorButton(
            Color.purple(),
            "Purple",
            background_color=Color.purple(),
            position=(0, 300),
            main_surface=main_surface,
            font_color=Color.white(),
            relative_surface_position=relative_surface_position,
        ),
        DrawColorButton(
            Color.teal(),
            "Teal",
            background_color=Color.teal(),
            position=(0, 325),
            main_surface=main_surface,
            font_color=Color.white(),
            relative_surface_position=relative_surface_position,
        ),
        DrawColorButton(
            Color.navy(),
            "Navy",
            background_color=Color.navy(),
            position=(0, 350),
            main_surface=main_surface,
            font_color=Color.white(),
            relative_surface_position=relative_surface_position,
        ),
        DrawColorButton(
            Color.white(),
            "Eraser",
            background_color=Color.black(),
            position=(0, 375),
            main_surface=main_surface,
            font_color=Color.white(),
            relative_surface_position=relative_surface_position,
        ),
    ]


def get_draw_size_buttons(main_surface, relative_surface_position: tuple):
    """Get the draw size buttons."""
    return [
        DrawSizeUpButton(
            "images/plus.png",
            scale_to=(50, 50),
            position=(0, 0),
            background_color=Color.black(),
            main_surface=main_surface,
            relative_surface_position=relative_surface_position,
        ),
        DrawSizeDownButton(
            "images/minus.png",
            scale_to=(50, 50),
            position=(50, 0),
            background_color=Color.red(),
            main_surface=main_surface,
            relative_surface_position=relative_surface_position,
        ),
    ]


def get_shape_buttons(main_surface, relative_surface_position: tuple):
    return [
        SquareButton(
            "images/square.png",
            scale_to=(50, 50),
            position=(0, 0),
            background_color=Color.black(),
            main_surface=main_surface,
            relative_surface_position=relative_surface_position,
        ),
        CircleButton(
            "images/circle.png",
            scale_to=(50, 50),
            position=(50, 0),
            background_color=Color.black(),
            main_surface=main_surface,
            relative_surface_position=relative_surface_position,
        ),
        TopTriangleButton(
            "images/toptriangle.png",
            scale_to=(50, 50),
            position=(0, 50),
            background_color=Color.black(),
            main_surface=main_surface,
            relative_surface_position=relative_surface_position,
        ),
        BottomTriangleButton(
            "images/bottomtriangle.png",
            scale_to=(50, 50),
            position=(50, 50),
            background_color=Color.black(),
            main_surface=main_surface,
            relative_surface_position=relative_surface_position,
        ),
        UpArrowButton(
            "images/upwardarrow.png",
            scale_to=(50, 50),
            position=(0, 100),
            background_color=Color.black(),
            main_surface=main_surface,
            relative_surface_position=relative_surface_position,
        ),
        DownArrowButton(
            "images/downwardarrow.png",
            scale_to=(50, 50),
            position=(50, 100),
            background_color=Color.black(),
            main_surface=main_surface,
            relative_surface_position=relative_surface_position,
        ),
        NoShapeButton(
            "images/noshape.png",
            scale_to=(50, 50),
            position=(0, 150),
            background_color=Color.black(),
            main_surface=main_surface,
            relative_surface_position=relative_surface_position,
        ),
    ]


def get_clear_buttons(main_surface, relative_surface_position: tuple):
    return [
        ClearButton(
            "Clear",
            background_color=Color.black(),
            position=(0, 0),
            main_surface=main_surface,
            font_color=Color.white(),
            relative_surface_position=relative_surface_position,
        )
    ]


def get_draw_action_buttons(main_surface, relative_surface_position: tuple):
    return [
        UndoButton(
            "images/undo.png",
            scale_to=(50, 50),
            position=(0, 0),
            background_color=Color.black(),
            main_surface=main_surface,
            relative_surface_position=relative_surface_position,
        ),
        RedoButton(
            "images/redo.png",
            scale_to=(50, 50),
            position=(50, 0),
            background_color=Color.black(),
            main_surface=main_surface,
            relative_surface_position=relative_surface_position,
        ),
    ]
