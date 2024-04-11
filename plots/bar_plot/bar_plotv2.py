from lets_plot import *
from pandas.core.api import DataFrame as DataFrame
from ..base_plot import BasePlot
from plotting_backend.common.contrasting_colors import contrasting_colors
from typing import Literal 

class BarPlot(BasePlot):
    plot_type: Literal['BarPlot'] = 'BarPlot'


    def create_plot(
        self
    ):
        return NotImplementedError()
        

    def style_plot(self):
        return NotImplementedError()
