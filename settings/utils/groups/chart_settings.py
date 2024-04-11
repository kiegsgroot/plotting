from pydantic import Field
from .base_settings_group import BaseSettingsGroup
from lets_plot import *


class ChartSettings(BaseSettingsGroup):
    figure_height: int = Field(
        title="Height", 
        default=700, 
        gt=0,
    )
    figure_width: int = Field(
        title="Width",
        default=1200,
        gt=0
    )
    panel_border: bool = Field(
        title="Panel Border",
        default=True,
    )

    def apply(self, plot):
        plot += theme(panel_border=element_rect(blank=not self.panel_border))
        if self.figure_height and self.figure_width:
            plot += ggsize(self.figure_width, self.figure_height)
        return plot
