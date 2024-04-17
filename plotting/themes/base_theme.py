from pydantic import BaseModel

class BaseTheme(BaseModel):
    colors: list[str]
