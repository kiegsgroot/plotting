from .. import *
from ..base_line import Asset, BaseLine

LINE_MAP: dict[str, BaseLine] = {
    "investment_growth": InvestmentGrowthLine,
    "percent_change": PercentChangeLine,
    "volatility": VolatilityLine,
    "moving_average": MovingAverageLine,
}

class LineFactory:
    @staticmethod
    def from_symbols(
        line_type: str,
        assets: list[Asset],
        name: str,
        id: str,
        start_date: str,
        end_date: str,
        color: str = "",
    ) -> BaseLine:

        line_class = LINE_MAP.get(line_type)

        if line_class is None:
            raise ValueError(f"Unsupported line type: {line_type}")

        return line_class.from_symbols(
            id=id,
            assets=assets,
            name=name,
            line_type=line_type,
            start_date=start_date,
            end_date=end_date,
            color=color,
        )
    @staticmethod
    def from_file(path: str) -> BaseLine:
        raise NotImplementedError()