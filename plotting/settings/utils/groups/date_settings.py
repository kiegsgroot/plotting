from pydantic import Field, constr
from .base_settings_group import BaseSettingsGroup
from datetime import datetime

class DateSettings(BaseSettingsGroup):
    start_date: str = Field(
        default="1980-01-01",
        title="Start Date", 
        pattern=r'^\d{4}-\d{2}-\d{2}$',
    )
    end_date: str = Field(
        default=datetime.now().strftime("%Y-%m-%d"),
        title="End Date", 
        pattern=r'^\d{4}-\d{2}-\d{2}$', 
    )

    def apply(self, plot):
        return plot