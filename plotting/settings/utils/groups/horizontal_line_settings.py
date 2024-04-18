from pydantic import Field
from typing import Union, Literal
from .base_settings_group import BaseSettingsGroup
from lets_plot import *

linetype_mapping = {
    "Solid": 1,
    "Dashed": 2,
    "Dotted": 3,
    "Dot-Dash": 4,
    "Long-Dash": 5,
    "Two-Dash": 6,
}

class HorizontalLineSettings(BaseSettingsGroup):
    place_horizontal_line_at: int = Field(
        title="Placement",
        default=None,
    )
    horizontal_line_type: Literal["Solid", "Dashed", "Dotted", "Dot-Dash", "Long-Dash", "Two-Dash"] = Field(
        title="Line Type",
        default="Solid",
    )
    horizontal_line_color: str = Field(
        title="Line Color", 
        default="#000000", 
        pattern=r"^#(?:[0-9a-fA-F]{3}){1,2}$"
    )
    horizontal_line_size: int = Field(
        title="Line Size",
        default=1, 
    )

    def apply(self, plot):
        if self.place_horizontal_line_at is not None:
            line_type = linetype_mapping[self.horizontal_line_type]

            plot += geom_hline(
                yintercept=self.place_horizontal_line_at,
                linetype=line_type,
                color=self.horizontal_line_color,
                size=self.horizontal_line_size,
            )
        return plot
