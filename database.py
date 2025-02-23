from abc import ABC, abstractmethod
from datetime import datetime


class BaseDatabase(ABC):
    @abstractmethod
    def save_bar_data(self, symbol: str, interval: '', bars: list) -> bool:
        pass

    @abstractmethod
    def load_bar_data(self, symbol: str, interval: '', start: int, end: int) -> list:
        pass

    @abstractmethod
    def delete_bar_data(self, symbol: str, interval: '') -> int:
        pass
