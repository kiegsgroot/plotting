from lets_plot import *
import pandas as pd
import numpy as np
from ..base_plot import BasePlot
from typing import Literal

class MatrixPlot(BasePlot):
    def __init__(
        self,
        data: list[pd.DataFrame],
        theme: Literal["resolve", "return-stacked"] = "resolve",
        settings: str = "./plots/styles/settings/default.yaml",
    ):
        super().__init__(data, theme, settings)

        self.settings.legend_position = "none"
        self.settings.panel_border = False
        self.settings.figure_width, self.settings.figure_height = 500, 500
        self.data = self._prepare_data(data)

    @staticmethod
    def _prepare_data(data: pd.DataFrame) -> pd.DataFrame:

        corr_matrix = data.corr().round(2)
        corr_matrix = corr_matrix[::-1]

        corr_data = corr_matrix.reset_index().melt(id_vars="index")
        corr_data.columns = ["x", "y", "value"]

        corr_data = corr_data[(corr_data["x"] < corr_data["y"])]

        return corr_data

    def create_plot(self):
        self.plot = (
            ggplot(self.data, aes("x", "y", fill="value"))
            + geom_tile()
            + geom_text(aes(label="value"), family=self.theme.font_style)
            + scale_fill_gradient2(
                low=self.settings.matrix_color_low,
                mid=self.settings.matrix_color_mid,
                high=self.settings.matrix_color_high,
                midpoint=0,
            )
        )
        self.style_plot()

    def style_plot(self):
        super().style_plot()
        self.plot += coord_fixed(ratio=1) + theme(
            panel_grid=element_blank(),
            axis_line_y=element_blank(),
            axis_line_x=element_blank(),
            axis_ticks_x=element_blank(),
        )
