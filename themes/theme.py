from typing import Literal
import os
import yaml

DEFAULT_HORIZONTAL_LINE_TYPE = "dashed"
DEFAULT_HORIZONTAL_LINE_COLOR = "black"
DEFAULT_LEGEND_POSITION = "top"
DEFAULT_FONT_STYLE = "Arial"
DEFAULT_FIGURE_DIMENSIONS = (500, 1200) 
DEFAULT_PANEL_BORDER = True

class Theme:
    def __init__(self, color_pallet: dict, font_style: str = DEFAULT_FONT_STYLE):
        self.color_pallet = color_pallet
        self.font_style = font_style

    @classmethod
    def from_yaml(cls, file_path: str) -> "Theme":
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"The file '{file_path}' does not exist.")
        
        with open(file_path, "r") as file:
            attributes_dict = yaml.safe_load(file)
        
        # Filter out only the keys relevant to Theme
        theme_attributes = {key: attributes_dict[key] for key in ['color_pallet', 'font_style'] if key in attributes_dict}
        
        return cls(**theme_attributes)
    
    def to_yaml(self, name: str = "theme.yaml", path: str = "./plot_theme/") -> None:
        os.makedirs(path, exist_ok=True)
        attributes_dict = self.__dict__
        file_path = os.path.join(path, name)
        with open(file_path, "w") as file:
            yaml.safe_dump(attributes_dict, file, sort_keys=False)

    def from_name(name: Literal["resolve", "rational", "horizons"]) -> "Theme":
        theme_path = f"./plots/styles/themes/{name}.yaml"
        theme = Theme.from_yaml(theme_path)
        return theme


    def list_themes() -> list[str]:
        themes_loc = "./plots/styles/themes"
        if os.path.exists(themes_loc):
            themes = [os.path.splitext(file)[0] for file in os.listdir(themes_loc) if file.endswith('.yaml') or file.endswith('.yml')]
            return themes