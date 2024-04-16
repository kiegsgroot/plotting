import pandas as pd
from abc import ABC, abstractmethod
from pydantic import BaseModel, Field
from ...utils.data_loaders.adam_data_loader import AdamDataLoader
from ...utils.data_loaders.base_data_loader import BaseDataLoader
from typing import Literal

default_data_loader = AdamDataLoader


class Asset(BaseModel, ABC):
    symbol: str = Field(..., examples=default_data_loader.list_tickers())
    weight: int = Field(default=100)

class BaseLine(BaseModel):
    assets: list[Asset] = Field(...)
    name: str = Field(default="New Line")
    id: str = Field(...)
    _data: pd.DataFrame = None 
    color: str = Field(default="#000000", pattern=r"^#(?:[0-9a-fA-F]{3}){1,2}$")

    class Config:
        arbitrary_types_allowed = True 

    @property
    def data(self) -> pd.DataFrame:
        if self._data is None:
            raise ValueError("Data has not been loaded yet")
        return self._data

    def download_data(
        self,
        start_date: str, 
        end_date: str, 
        data_loader: BaseDataLoader = default_data_loader
    ) -> None:
        data_loader = data_loader(self)
        data = data_loader.run(start_date, end_date)
        self._data = data

    @abstractmethod
    def transform_data() -> None:
        return NotImplementedError()
    
    def prepare_data(
        self,
        start_date: str, 
        end_date: str, 
        data_loader: BaseDataLoader = AdamDataLoader
    ) -> None:
        self.download_data(start_date, end_date, data_loader)
        self.transform_data()