from abc import ABC, abstractmethod
from pydantic import BaseModel

class BaseSettingsGroup(ABC, BaseModel):

    @abstractmethod
    def apply(self, plot):
        raise NotImplementedError()