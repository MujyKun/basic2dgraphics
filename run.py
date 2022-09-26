from typing import Union, Optional

import pygame
from models import (
    Color,
    BaseButton,
    PersistentShape,
    ShapeButton,
    draw_cursor,
    get_color_buttons,
    get_draw_size_buttons,
    get_shape_buttons,
    persistent_objects,
    PersistentSurface,
    DrawSizeUpButton,
    DrawSizeDownButton,
    ClearButton,
    get_clear_buttons,
    DrawColorButton,
)

pygame.init()
WIDTH = 1080
HEIGHT = 600
display = pygame.display
display.set_caption("2D Graphics")
display.set_icon(pygame.image.load("images/iu_icon.jpg"))
surface = display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()


def add_persistent_surface(
    surface_dimensions: tuple, color: Union[tuple, Color], position: tuple = None
):
    """
    Add a surface that will stay on the screen.

    :param surface_dimensions:
        The width and height of the new surface.
    :param color: :ref:`Color`
        The color object to fill the surface with.
    :param position: tuple
        The width and height position of the surface. Will default to (0,0)
    """
    _surface = pygame.surface.Surface(surface_dimensions)
    if isinstance(color, Color):
        color = color.rgb
    _surface.fill(color)
    if not position:
        position = (0, 0)
    pers_surf = PersistentSurface(_surface, position)
    draw_persistent_surface(pers_surf.surface, pers_surf.position)
    persistent_objects.surfaces.append(pers_surf)


def add_persistent_shape(
    button: ShapeButton, color: Union[tuple, Color], position: tuple = None
):
    """
    Add a shape surface that will stay on the screen.

    :param button:
        The button that will render the shape.
    :param color: :ref:`Color`
        The color object to fill the shape with.
    :param position: tuple
        The width and height position of the surface. Will default to (0,0)
    """
    if isinstance(color, Color):
        color = color.rgb
    if not position:
        position = (0, 0)
    pers_shape = PersistentShape(button, draw_cursor.draw_size, color, position)
    draw_persistent_shape(pers_shape)
    persistent_objects.shapes.append(pers_shape)


def draw_persistent_objects():
    """
    Draw any persistent surfaces and shapes.
    """
    [draw_persistent_surface(pers_surface.surface, pers_surface.position)
        for pers_surface in persistent_objects.surfaces]

    [draw_persistent_shape(pers_shape) for pers_shape in persistent_objects.shapes]


def draw_persistent_shape(_shape):
    _shape.draw(surface)


def draw_persistent_surface(_surface, _position):
    surface.blit(_surface, _position)


def check_button_interactions(cursor_position, boundary_size=None):
    for button in buttons:
        if button.is_touching(position=cursor_position, boundary_size=boundary_size):
            return button


def get_buttons():
    color_buttons = get_color_buttons(surface)
    draw_size_buttons = get_draw_size_buttons(surface)
    shape_buttons = get_shape_buttons(surface)
    clear_buttons = get_clear_buttons(surface)
    return color_buttons + draw_size_buttons + shape_buttons + clear_buttons


def update_cursor_position():
    cursor_pos_surface = sys_font.render(f"{cursor_pos}", True, Color.black())
    surface.blit(cursor_pos_surface, (0, 0))


def update_fps_counter():
    fps_surface = sys_font.render(f"{clock.get_fps()}", True, Color.black())
    surface.blit(fps_surface, (0, 50))


if __name__ == "__main__":
    keep_going = True
    sys_font = pygame.font.SysFont("Corbel", 25)
    shape_button_selected: Optional[ShapeButton] = None

    while keep_going:
        surface.fill(Color.white())  # reset frame
        buttons = get_buttons()

        cursor_pos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keep_going = False
            if pygame.mouse.get_pressed()[0]:  # mouse is held down.
                # check for any button presses
                button_pressed: Union[BaseButton] = check_button_interactions(
                    cursor_pos, boundary_size=draw_cursor.draw_size
                )
                if button_pressed:
                    result = button_pressed.run()
                    # Clear the canvas.
                    if isinstance(button_pressed, ClearButton):
                        persistent_objects.reset()

                    # do not change shapes if we are just changing the draw size or color.
                    if not isinstance(
                        button_pressed,
                        (DrawSizeDownButton, DrawSizeUpButton, DrawColorButton),
                    ):
                        draw_cursor.tool_selected = bool(result)
                        shape_button_selected = None if not result else button_pressed
                else:
                    if not shape_button_selected:
                        # regular draw
                        add_persistent_surface(
                            surface_dimensions=draw_cursor.draw_size,
                            color=draw_cursor.draw_color.rgb,
                            position=cursor_pos,
                        )
                    else:
                        # shape draw
                        add_persistent_shape(
                            button=shape_button_selected,
                            color=draw_cursor.draw_color.rgb,
                            position=cursor_pos,
                        )

        update_cursor_position()
        update_fps_counter()
        # draw_persistent_objects()
        # display.update()
        clock.tick(144)
        display.flip()

