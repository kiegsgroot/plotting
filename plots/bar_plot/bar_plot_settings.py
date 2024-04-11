from pydantic import Field
from ...settings.base_plot_settings import BasePlotSettings
from ...settings.utils.groups import AxisSettings, LegendSettings, HorizontalLineSettings

class BarPlotSettings(BasePlotSettings):
    axis_settings: AxisSettings = Field(..., alias="Axis Settings")
    legend_settings: LegendSettings = Field(..., alias="Legend Settings")
    horizontal_line_settings: HorizontalLineSettings = Field(
        ..., alias="Horizontal Line Settings"
    )
