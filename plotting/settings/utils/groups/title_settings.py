from pydantic import Field
from ..fields import JustifiableLabel
from .base_settings_group import BaseSettingsGroup
from lets_plot import *


class TitleSettings(BaseSettingsGroup):
    title: JustifiableLabel = Field(
        title="Title",
        default={"text": None, "font_size": 15, "justify": "0.5"}
    )
    subtitle: JustifiableLabel = Field(
        title="Subtitle",
        default={"text": None, "font_size": 15, "justify": "0.5"}
    )
    caption: JustifiableLabel = Field(
        title="Caption",
        default={"text": None, "font_size": 15, "justify": "1"}
    )

    def apply(self, plot):
        plot += labs(
            title=self.title.text,
            subtitle=self.subtitle.text,
            caption=self.caption.text,
        )
        plot += theme(
            plot_title=element_text(size=self.title.size, hjust=self.title.justify),
            plot_subtitle=element_text(
                size=self.subtitle.size, hjust=self.subtitle.justify
            ),
            plot_caption=element_text(
                size=self.caption.size, hjust=self.caption.justify
            ),
        )
        return plot
