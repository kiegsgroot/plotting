import pandas as pd
from .base_line import BaseLine
from typing import Literal

class VolatilityLine(BaseLine):
    line_type: Literal['Volatility'] = 'Volatility'

    def transform_data(self) -> None:
        self._data['Price'] = self._data['Price'].astype(float)

        daily_returns = self._data['Price'].pct_change()

        rolling_volatility = daily_returns.rolling(window=20).std()

        result = pd.DataFrame({
            'Date': self._data['Date'],
            'Asset': self._data['Asset'],
            'Price': rolling_volatility
        })

        self._data = result
