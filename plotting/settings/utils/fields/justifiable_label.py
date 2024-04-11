from pydantic import Field
from typing import Literal
from .label import Label

class JustifiableLabel(Label):
    justify: Literal["0", "0.5", "1"] = Field(
        default="0",
        title="Justify",
        json_schema_extra={"display": "justifiable_label"}
    )
