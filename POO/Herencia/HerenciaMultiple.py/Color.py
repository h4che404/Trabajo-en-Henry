class Color:
    def __init__(self, color) -> None:
        self._Color = color
    
    def __str__(self) -> str:
        return f"El color es:{self._Color}"

    @property
    def get_Color(self):
        return self._Color
    @get_Color.setter
    def set_Color(self, pintura):
         self._Color = pintura