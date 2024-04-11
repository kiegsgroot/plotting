import os
import yaml
from pydantic import BaseModel
from pydantic import Field
from .utils.groups import TitleSettings, ChartSettings, ThemeSettings


class BasePlotSettings(BaseModel):
    title_settings: TitleSettings = Field(..., alias="Title Settings")
    chart_settings: ChartSettings = Field(..., alias="Chart Settings")
    theme_settings: ThemeSettings = Field(..., alias="Theme Settings")

    @classmethod
    def from_yaml(cls, file_path: str) -> "BasePlotSettings":
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"The file '{file_path}' does not exist.")
        with open(file_path, "r") as file:
            yaml_data = yaml.safe_load(file)
            print(yaml_data)
        return cls(**yaml_data)

    def to_yaml(self, file_path: str) -> None:
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, "w") as file:
            yaml.dump(self.model_dump(by_alias=True), file)

    def apply_all_settings(self, plot):
        for attr_name in self.model_fields.keys():
            attribute = getattr(self, attr_name)
            if hasattr(attribute, "apply"):
                plot = attribute.apply(plot)

            print(attr_name, "complete.")
        return plot
