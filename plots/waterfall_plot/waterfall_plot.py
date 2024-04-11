from lets_plot import *
import pandas as pd
from ..base_plot import BasePlot
from typing import Literal

class WaterfallChart(BasePlot):
    def __init__(
        self,
        data: pd.DataFrame,
        theme: Literal["resolve", "return-stacked"] = "resolve",
    ):
        super().__init__(data, theme)
        self.settings.legend_position = "none"

    def create_plot(self, bar_width=0.8):
        # Convert index to a column, assuming it contains the steps/categories for the x-axis
        self.data.reset_index(inplace=True)
        self.data.rename(columns={'index': 'Step'}, inplace=True)
        self.data['Step'] = pd.Categorical(self.data['Step'], categories=self.data['Step'], ordered=True)

        # Assuming 'Change' is the first column after resetting the index
        # Calculate 'Start' and 'End' positions for each rectangle
        self.data["Start"] = self.data["Change"].cumsum().shift(1).fillna(0)
        self.data["End"] = self.data["Change"].cumsum()

        # Determine fill color based on positive or negative change
        self.data["Fill"] = self.data["Change"] > 0

        # Create a numeric position for each step to adjust bar width, matched to 'Step' categories
        self.data["Position"] = self.data['Step'].cat.codes

        # Adjusting 'xmin' and 'xmax' based on desired bar width
        self.data["xmin"] = self.data["Position"] - bar_width / 2
        self.data["xmax"] = self.data["Position"] + bar_width / 2

        # Creating the plot with categories on the x-axis
        self.plot = (
            ggplot(self.data) +
            geom_rect(
                aes(xmin="xmin", xmax="xmax", ymin="Start", ymax="End", fill="Fill"),
                color="rgba(0, 0, 0, 0)",
            )
        )
        super().create_plot()

    def style_plot(self):
        super().style_plot()
        self.plot += (
            scale_fill_manual(
                    values={
                        True: self.settings.waterfall_positive_color,
                        False: self.settings.waterfall_negative_color,
                    }
                ) +
            scale_x_continuous(breaks=self.data["Position"], labels=self.data["Step"])
        )
    
