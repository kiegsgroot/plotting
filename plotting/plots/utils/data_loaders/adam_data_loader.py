from data_handling import LoadData
from datetime import datetime
import pandas as pd
from .base_data_loader import BaseDataLoader
import os

class AdamDataLoader(BaseDataLoader):

    def download(self, start_date: str, end_date: str) -> pd.DataFrame:
        symbols = [asset.symbol for asset in self.line.assets]
        data_loader = LoadData(symbols=symbols, download_data=False)
        data_loader.load_and_combine_data()
        combined_data = data_loader.df
        
        start_datetime = datetime.strptime(start_date, "%Y-%m-%d")
        end_datetime = datetime.strptime(end_date, "%Y-%m-%d")
        filtered_data = combined_data.loc[start_datetime:end_datetime]
        return filtered_data
    
    def process_data(self, data: pd.DataFrame) -> pd.DataFrame:
        weights = {column: asset.weight / 100 for asset, column in zip(self.line.assets, data.columns)}
        weighted_data = data.multiply(weights)

        portfolio_performance = weighted_data.sum(axis=1).to_frame(name=self.line.name)

        plot_data = portfolio_performance.reset_index().melt(
            id_vars=[portfolio_performance.index.name],
            value_vars=[self.line.name],
            var_name="Asset",
            value_name="Price"
        )

        return plot_data
    
    @staticmethod
    def list_tickers() -> list[str]:
        data_loc = "./Data"
        data_points = []
        for filename in os.listdir(data_loc):
            if os.path.isfile(os.path.join(data_loc, filename)):
                basename = os.path.splitext(filename)[0]
                data_points.append(basename)
        return data_points