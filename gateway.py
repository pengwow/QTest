from abc import ABC, abstractmethod


class BaseGateway(ABC):
    @abstractmethod
    def test_connect(self):
        """Test Connectivity"""
        pass

    @abstractmethod
    def get_all_symbols(self):
        pass

