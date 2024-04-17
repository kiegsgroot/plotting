from pydantic import BaseModel
import importlib.resources as pkg_resources
from ..common.functions.load_yaml import load_yaml_as_dict
from typing import Literal

class ReSolveTheme(BaseModel):
    theme_name: Literal['ReSolve'] = 'ReSolve'
    colors: list[str] = [
    "#00488d", "#d3d800", "#f29400", "#6f4596", "#89d2ff", 
    "#b3d852", "#7e768c", "#81aec6", "#e6c245", "#63cc77", 
    "#00abff", "#293645", "#fbba00", "#88949e"
    ]


