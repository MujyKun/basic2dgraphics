from . import ImageButton
from .. import persistent_objects, draw_cursor


class UndoButton(ImageButton):
    """Undo an action on a canvas."""
    def __init__(self, *args, **kwargs):
        super(UndoButton, self).__init__(*args, **kwargs)

    def run(self):
        """Undo an action."""
        persistent_objects.undo()


class RedoButton(ImageButton):
    """Redo an action on a canvas that was undone."""
    def __init__(self, *args, **kwargs):
        super(RedoButton, self).__init__(*args, **kwargs)

    def run(self):
        """Redo an action."""
        persistent_objects.redo()


class NoShapeButton(ImageButton):
    """Remove any shape tool selected on a canvas."""
    def __init__(self, *args, **kwargs):
        super(NoShapeButton, self).__init__(*args, **kwargs)

    def run(self):
        """Unselect any shapes."""
        draw_cursor.tool_selected = False
