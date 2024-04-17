from .resolve_theme import ReSolveTheme
from .return_stacked_theme import ReturnStackedTheme

from typing_extensions import Annotated
from typing import Union
from pydantic import Field

Theme = Annotated[
    Union[ReSolveTheme, ReturnStackedTheme],
    Field(discriminator="theme_name"),
]