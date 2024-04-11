from pydantic import Field, constr
from .base_settings_group import BaseSettingsGroup
from datetime import datetime

class DateSettings(BaseSettingsGroup):
    start_date: str = Field(
        ...,
        title="Start Date", 
        pattern=r'^\d{4}-\d{2}-\d{2}$',
        examples=['2000-01-01'],
    )
    end_date: str = Field(
        ...,
        title="End Date", 
        pattern=r'^\d{4}-\d{2}-\d{2}$', 
        examples=['2010-01-01'], 
    )

    def apply(self, plot):
        return plot
