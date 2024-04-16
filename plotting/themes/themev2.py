from pydantic import BaseModel, Field
import importlib.resources as pkg_resources
from ..common.functions.load_yaml import load_yaml_as_dict

class Theme(BaseModel):
    theme_name: str 
    colors: list[str] = load_yaml_as_dict(str(pkg_resources.path("plotting.themes", "color_themes.yaml")))[theme_name]


