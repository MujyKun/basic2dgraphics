from . import TextButton


class ClearButton(TextButton):
    """Button to clear a canvas."""
    def __init__(self, *args, **kwargs):
        super(ClearButton, self).__init__(*args, **kwargs)
