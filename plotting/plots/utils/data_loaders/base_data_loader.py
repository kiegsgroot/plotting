from abc import ABC, abstractmethod
import pandas as pd

class BaseDataLoader(ABC):
    def __init__(self, line) -> None:
          self.line = line

    @abstractmethod
    def download(self, start_date: str, end_date: str) -> pd.DataFrame:
        return NotImplementedError()
    
    @abstractmethod
    def process_data(self, data: pd.DataFrame) -> pd.DataFrame:
        return NotImplementedError()
    
    @staticmethod
    @abstractmethod
    def list_tickers() -> list[str]:
        return NotImplementedError()
    
    def run(self, start_date: str, end_date: str) -> pd.DataFrame:
        data = self.download(start_date, end_date)
        processed_data = self.process_data(data)
        return processed_data
    
    

