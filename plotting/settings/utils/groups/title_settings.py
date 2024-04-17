from pydantic import Field
from ..fields import JustifiableLabel
from .base_settings_group import BaseSettingsGroup
from lets_plot import *


class TitleSettings(BaseSettingsGroup):
    title: JustifiableLabel = Field(
        alias="Title",
    )
    subtitle: JustifiableLabel = Field(
        alias="Subtitle",
    )
    caption: JustifiableLabel = Field(
        alias="Caption",
    )

    def apply(self, plot):
        plot += labs(
            title=self.title.text,
            subtitle=self.subtitle.text,
            caption=self.caption.text,
        )
        plot += theme(
            plot_title=element_text(size=self.title.font_size, hjust=self.title.justify),
            plot_subtitle=element_text(
                size=self.subtitle.font_size, hjust=self.subtitle.justify
            ),
            plot_caption=element_text(
                size=self.caption.font_size, hjust=self.caption.justify
            ),
        )
        return plot
