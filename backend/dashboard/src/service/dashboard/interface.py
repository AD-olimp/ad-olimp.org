from abc import ABC, abstractmethod


class DashboardServiceInterface(ABC):
    """Интерфейс сервиса по работе с публикациями"""
    
    
    @classmethod
    @abstractmethod
    async def get_list_data(session, data, data_filter):
        ...

    @classmethod
    @abstractmethod
    async def get_current_data(session, data_id):
        ...