from pydantic import BaseModel
import importlib.resources as pkg_resources
from ..common.functions.load_yaml import load_yaml_as_dict
import contextlib

class Theme(BaseModel):
    theme_name: str
    colors: list[str] = []

    def __init__(self, **data):
        super().__init__(**data)
        with pkg_resources.path("plotting.themes", "color_themes.yaml") as path:
            colors_dict = load_yaml_as_dict(str(path))
        self.colors = colors_dict.get(self.theme_name, [])
