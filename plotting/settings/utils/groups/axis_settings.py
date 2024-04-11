from pydantic import Field
from ..fields import Label
from .base_settings_group import BaseSettingsGroup
from lets_plot import *


class AxisSettings(BaseSettingsGroup):
    x_axis_label: Label = Field(...,
        title="X-Axis Label",
    )
    y_axis_label: Label = Field(...,
        title="Y-Axis Label",
    )
    y_axis_log2: bool = Field(
        title="Y-Axis Logarithmic Scale",
        default=False,
    )

    def apply(self, plot):
        plot += labs(x=self.x_axis_label.text, y=self.y_axis_label.text)
        plot += theme(
            axis_title_x=element_text(size=self.x_axis_label.font_size),
            axis_title_y=element_text(size=self.y_axis_label.font_size),
        )
        plot += scale_x_datetime(expand=[0.00, 0])

        if self.y_axis_log2:
            plot += scale_y_log2()
        else:
            plot += scale_y_continuous()

        return plot
