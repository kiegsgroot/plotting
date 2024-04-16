import pandas as pd
from .base_line import BaseLine
from typing import Literal

class PercentChangeLine(BaseLine):
    line_type: Literal['Percent Change'] = 'Percent Change'

    def transform_data(self) -> None:
        pass
