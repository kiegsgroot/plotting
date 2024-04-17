from pydantic import BaseModel
from typing import Literal
from .base_theme import BaseTheme

class ReSolveTheme(BaseTheme):
    theme_name: Literal['ReSolve'] = 'ReSolve'
    colors: list[str] = [
        "#00488d", "#d3d800", "#f29400", "#6f4596", "#89d2ff", 
        "#b3d852", "#7e768c", "#81aec6", "#e6c245", "#63cc77", 
        "#00abff", "#293645", "#fbba00", "#88949e"
    ]


