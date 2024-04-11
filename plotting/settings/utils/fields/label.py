from pydantic import BaseModel, Field
from typing import Union

class Label(BaseModel):
    text: str = Field(default='', title="Text")
    font_size: int = Field(default=10, title="Font Size", gt=0)

