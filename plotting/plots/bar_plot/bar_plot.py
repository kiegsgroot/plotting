from lets_plot import *
from plotting_backend.plotting.plots.base_plot import BasePlot

from .bar_plot_settings import BarPlotSettings
from typing import Literal, Union
from pydantic import Field
from typing_extensions import Annotated



class BarPlot(BasePlot):
    plot_type: Literal['Bar Plot'] = 'Bar Plot'
    settings: BarPlotSettings


    def create_plot(self):
        
        return NotImplementedError()
