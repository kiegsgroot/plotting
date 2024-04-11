from pydantic import BaseModel, Field
from typing import Union

class Label(BaseModel):
    text: Union[str, None] = Field(default='', title="Text")
    font_size: int = Field(default=10, title="Font Size", gt=0)

