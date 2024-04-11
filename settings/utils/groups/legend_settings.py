from pydantic import Field
from typing import Optional
from .base_settings_group import BaseSettingsGroup
from lets_plot import *
from typing import Literal


class LegendSettings(BaseSettingsGroup):
    legend_position: Literal['left', 'right', 'bottom', 'top'] = Field(
        title="Position",
        default="top", 
    )
    legend_size: int = Field(
        title="Size",
        default=10,
    )
    legend_direction: Literal['horizontal', 'vertical'] = Field(
        title="Direction",
        default='horizontal',
    )
    values_size: int = Field(
        title="Values Size",
        default=10,
    )
    
    def apply(self, plot):
        plot += theme(
            legend_position=self.legend_position,
            legend_title=element_blank(),
            legend_text=element_text(size=self.legend_size),
            legend_direction=self.legend_direction,
        )
        return plot
