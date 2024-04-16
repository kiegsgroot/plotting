import pandas as pd
from abc import ABC, abstractmethod
from pydantic import BaseModel, Field
from ...utils.data_loaders.adam_data_loader import AdamDataLoader
from ...utils.data_loaders.base_data_loader import BaseDataLoader
from ....common.functions.load_yaml import load_yaml_as_dict
import importlib.resources as pkg_resources

with pkg_resources.path("plotting.themes", "color_themes.yaml") as path:
    color_themes_path = str(path)

default_data_loader = AdamDataLoader


class Asset(BaseModel, ABC):
    symbol: str = Field(..., examples=default_data_loader.list_tickers(), alias="name")
    weight: int = Field(default=100, alias="value")

class BaseLine(BaseModel):
    _data_loader: BaseDataLoader = default_data_loader
    _data: pd.DataFrame = None 

    assets: list[Asset] = Field(...)
    name: str = Field(
        default="New Line"
    )
    id: str = Field(...)
    color: str = Field(
        default="#000000", 
        pattern=r"^#(?:[0-9a-fA-F]{3}){1,2}$", 
        json_schema_extra={
            "options_by_theme": load_yaml_as_dict(str(pkg_resources.path("plotting.themes", "color_themes.yaml")))
        }
    )
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
    ) -> None:
        data = self._data_loader(self).run(start_date, end_date)
        self._data = data

    @abstractmethod
    def transform_data() -> None:
        return NotImplementedError()
    
    def prepare_data(
        self,
        start_date: str, 
        end_date: str, 
    ) -> None:
        self.download_data(start_date, end_date)
        self.transform_data()