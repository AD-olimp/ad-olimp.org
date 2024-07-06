from abc import ABC, abstractmethod


class ForecastServiceInterface(ABC):
    """Интерфейс сервиса по работе с публикациями"""
    
    
    @classmethod
    @abstractmethod
    async def get_forecast(session, data):
        ...
        