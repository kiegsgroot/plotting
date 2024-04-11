from lets_plot import *
from lets_plot.geo_data import *
from lets_plot.export import ggsave
from abc import ABC, abstractmethod
from ..settings.base_plot_settings import BasePlotSettings
from pydantic import BaseModel, PrivateAttr
from typing import Optional
from lets_plot.plot.core import PlotSpec


class BasePlot(BaseModel, ABC):
    _plot: Optional[PlotSpec] = PrivateAttr(default_factory=ggplot)
    settings: BasePlotSettings

    @abstractmethod
    def create_plot(self):
        return NotImplementedError

    def save_plot(self, filename: str = "plot.pdf", path: str = None):
        if self._plot is not None:
            ggsave(self._plot, filename=filename, path=path)
        else:
            return "No plot created."

    def style_plot(self):
        self._plot = self.settings.apply_all_settings(self._plot)
