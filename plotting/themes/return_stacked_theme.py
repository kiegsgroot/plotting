from pydantic import BaseModel
from typing import Literal
from .base_theme import BaseTheme

class ReturnStackedTheme(BaseTheme):
    theme_name: Literal['Return-Stacked'] = 'Return-Stacked'
    colors: list[str] = ['#323A46', '#3A6A9C', '#95E885', '#008EB8', '#14CFA6', '#EBE96A']

