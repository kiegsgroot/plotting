from .. import LinePlot, CorrelationPlot, BarPlot, WaterfallChart, BasePlot
import pandas as pd
from typing import Literal

def plot_factory(plot_type, data: pd.DataFrame, theme: Literal['resolve', 'return-stacked'] = "resolve") -> BasePlot:
    if plot_type == "line":
        return LinePlot(data, theme)
    elif plot_type == "bar":
        return BarPlot(data, theme)
    elif plot_type == "matrix":
        return CorrelationPlot(data, theme)
    elif plot_type == "waterfall":
        return WaterfallChart(data, theme)
    else:
        raise ValueError(f"Unsupported plot type: {plot_type}")