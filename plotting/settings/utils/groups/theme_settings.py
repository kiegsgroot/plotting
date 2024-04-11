from pydantic import Field
from typing import Literal
from .base_settings_group import BaseSettingsGroup


class ThemeSettings(BaseSettingsGroup):
    theme: Literal["ReSolve", "Return-Stacked"] = Field(
        title="Theme",
        default="ReSolve",
    )

    def apply(self, plot):
        return plot
