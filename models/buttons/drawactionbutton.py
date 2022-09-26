from . import ImageButton
from .. import persistent_objects


class UndoButton(ImageButton):
    def __init__(self, *args, **kwargs):
        super(UndoButton, self).__init__(*args, **kwargs)

    def run(self):
        persistent_objects.undo()


class RedoButton(ImageButton):
    def __init__(self, *args, **kwargs):
        super(RedoButton, self).__init__(*args, **kwargs)

    def run(self):
        persistent_objects.redo()