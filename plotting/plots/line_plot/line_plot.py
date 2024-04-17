from lets_plot import *
from plotting.plots.base_plot import BasePlot
from .line_types import (
    InvestmentGrowthLine,
    VolatilityLine,
    PercentChangeLine,
    MovingAverageLine,
)
from .line_plot_settings import LinePlotSettings
from typing import Literal, Union
from pydantic import Field
from typing_extensions import Annotated
from ...themes import Theme

Line = Annotated[
    Union[InvestmentGrowthLine, VolatilityLine, PercentChangeLine, MovingAverageLine],
    Field(discriminator="line_type"),
]


class LinePlot(BasePlot):
    plot_type: Literal["Line Plot"] = "Line Plot"
    lines: list[Line]
    settings: LinePlotSettings
    theme: Theme

    def create_plot(self):
        plot_range = (
            self.settings.date_settings.start_date,
            self.settings.date_settings.end_date,
        )

        for line in self.lines:
            line.prepare_data(*plot_range)
            self._plot += geom_line(
                aes(x="Date", y="Price", color="Asset"),
                data=line.data,
                color=line.color,
                label=line.name,
            )

        color_map = {line.name: line.color for line in self.lines}
        self._plot += scale_color_manual(values=color_map)
