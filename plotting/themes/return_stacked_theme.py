from pydantic import BaseModel
import importlib.resources as pkg_resources
from ..common.functions.load_yaml import load_yaml_as_dict
from typing import Literal

class ReturnStackedTheme(BaseModel):
    theme_name: Literal['Return-Stacked'] = 'Return-Stacked'
    colors: list[str] = ['#323A46', '#3A6A9C', '#95E885', '#008EB8', '#14CFA6', '#EBE96A']

