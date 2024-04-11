import pandas as pd
from .base_line import BaseLine
from typing import Literal

class PercentChangeLine(BaseLine):
    line_type: Literal['percent_change'] = 'percent_change'

    def transform_data(self) -> None:
        pass
