import pandas as pd
from .base_line import BaseLine
from typing import Literal

class MovingAverageLine(BaseLine):
    line_type: Literal['moving_average'] = 'moving_average'

    def transform_data(self) -> None:
        self._data['Price'] = self._data['Price'].astype(float)

        moving_average_20d = self._data['Price'].rolling(window=20).mean()

        result = pd.DataFrame({
            'Date': self._data['Date'],
            'Asset': self._data['Asset'],
            'Price': moving_average_20d
        })

        self._data = result
