import pandas as pd
from .base_line import BaseLine
from typing import Literal

class InvestmentGrowthLine(BaseLine):
    line_type: Literal['investment_growth'] = 'investment_growth'
    
    def transform_data(self) -> None:
        self._data['Price'] = self._data['Price'].astype(float)
        cumulative_returns = (1 + self._data['Price'].pct_change(fill_method=None)).cumprod()
        investment_growth = cumulative_returns * 100
        result = pd.DataFrame({
            'Date': self._data['Date'],
            'Asset': self._data['Asset'],
            'Price': investment_growth
        })

        self._data = result